#!/usr/bin/env python
"""
Test script to verify assignment creation with file uploads.
This simulates a form submission with attachments.
"""
import os
import sys
import django
from io import BytesIO

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studyapp.settings')
django.setup()

from django.test import Client
from django.contrib.auth import get_user_model
from account.models import Student
from assingment.models import Assignment, AssignmentFile

User = get_user_model()

def test_assignment_creation_with_files():
    """Test creating an assignment with file attachments"""
    
    # Find or create a test student
    try:
        student_user = User.objects.filter(role='STUDENT').first()
        if not student_user:
            print("❌ No student user found. Please create a student account first.")
            return False
        
        if not hasattr(student_user, 'student_profile'):
            print(f"❌ User {student_user.email} does not have a student profile.")
            return False
        
        student = student_user.student_profile
        print(f"✓ Using student: {student.user.get_full_name()} (ID: {student.student_id})")
        
    except Exception as e:
        print(f"❌ Error finding student: {e}")
        return False
    
    # Create test files - Django test client needs files as a list of tuples
    # For multiple files with same name, we need to use a different approach
    from django.core.files.uploadedfile import SimpleUploadedFile
    
    test_files = {
        'supportFiles': [
            SimpleUploadedFile('test_file_1.txt', b'Test file 1 content', content_type='text/plain'),
            SimpleUploadedFile('test_file_2.txt', b'Test file 2 content', content_type='text/plain'),
        ]
    }
    
    # Prepare form data
    form_data = {
        'assignmentTitle': 'Test Assignment with Files',
        'serviceType': 'assignment',
        'priority': 'medium',
        'dueDate': '2025-12-31',
        'serviceDetails': 'This is a test assignment to verify file uploads work correctly.',
    }
    
    # Create client and login
    client = Client()
    client.force_login(student_user)
    
    print("\n" + "="*60)
    print("Testing Assignment Creation with File Uploads")
    print("="*60)
    print(f"Student: {student.user.get_full_name()}")
    print(f"Title: {form_data['assignmentTitle']}")
    print(f"Files to upload: {len(test_files)}")
    print("="*60 + "\n")
    
    try:
        # Make POST request with files
        # For multiple files with same name, we need to send them differently
        response = client.post(
            '/assingment/create/',
            data=form_data,
            follow=True
        )
        
        # Try alternative approach - send files one by one in separate requests
        # Actually, let's use a manual approach to test
        from django.test import RequestFactory
        from django.contrib.messages.storage.fallback import FallbackStorage
        from django.contrib.sessions.middleware import SessionMiddleware
        from django.contrib.auth.middleware import AuthenticationMiddleware
        
        factory = RequestFactory()
        request = factory.post('/assingment/create/', data=form_data)
        
        # Add files manually
        for file_obj in test_files['supportFiles']:
            request.FILES.appendlist('supportFiles', file_obj)
        
        # Add middleware
        middleware = SessionMiddleware(lambda req: None)
        middleware.process_request(request)
        request.session.save()
        
        auth_middleware = AuthenticationMiddleware(lambda req: None)
        auth_middleware.process_request(request)
        request.user = student_user
        
        # Actually, let's just test with a single file first
        print("Testing with single file upload...")
        single_file = {
            'supportFiles': SimpleUploadedFile('test_file.txt', b'Test content', content_type='text/plain')
        }
        
        response = client.post(
            '/assingment/create/',
            data=form_data,
            files=single_file,
            follow=True
        )
        
        print(f"Response Status Code: {response.status_code}")
        
        if response.status_code == 200:
            try:
                result = response.json()
                print(f"\nResponse JSON:")
                print(f"  Success: {result.get('success', False)}")
                print(f"  Assignment Code: {result.get('assignment_code', 'N/A')}")
                print(f"  Files Received: {result.get('files_received', 0)}")
                print(f"  Files Uploaded: {result.get('files_uploaded', 0)}")
                
                if result.get('file_errors'):
                    print(f"  File Errors: {result.get('file_errors')}")
                
                if result.get('saved_files'):
                    print(f"\n  Saved Files:")
                    for f in result.get('saved_files', []):
                        print(f"    - {f.get('name')} (ID: {f.get('id')}, Type: {f.get('type')})")
                
                # Verify in database
                if result.get('assignment_code'):
                    assignment = Assignment.objects.get(assignment_code=result['assignment_code'])
                    files_in_db = AssignmentFile.objects.filter(assignment=assignment)
                    
                    print(f"\n{'='*60}")
                    print("Database Verification:")
                    print(f"{'='*60}")
                    print(f"Assignment: {assignment.assignment_code}")
                    print(f"Files in DB: {files_in_db.count()}")
                    
                    if files_in_db.count() > 0:
                        print("\nFiles found in database:")
                        for f in files_in_db:
                            print(f"  - {f.file_name} (ID: {f.id}, Type: {f.file_type})")
                        print(f"\n✅ SUCCESS - Files were saved to database!")
                    else:
                        print(f"\n❌ FAILED - No files found in database")
                    
                    return files_in_db.count() > 0
                else:
                    print(f"\n❌ FAILED - No assignment code in response")
                    if result.get('error'):
                        print(f"Error: {result.get('error')}")
                    return False
                    
            except Exception as e:
                print(f"\n❌ Error parsing response: {e}")
                print(f"Response content: {response.content[:500]}")
                return False
        else:
            print(f"\n❌ Request failed with status {response.status_code}")
            print(f"Response content: {response.content[:500]}")
            return False
            
    except Exception as e:
        print(f"\n❌ Error during test: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    success = test_assignment_creation_with_files()
    sys.exit(0 if success else 1)

