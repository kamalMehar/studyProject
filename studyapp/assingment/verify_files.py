"""
Quick verification script to check if assignment files are saved in the database.
Run this from Django shell: python manage.py shell
Then: from assingment.verify_files import verify_assignment_files
"""

from assingment.models import Assignment, AssignmentFile

def verify_assignment_files(assignment_id=None, assignment_code=None):
    """
    Verify that files are saved in the database for an assignment.
    
    Usage:
        verify_assignment_files(assignment_id='uuid-here')
        verify_assignment_files(assignment_code='ASG-2025-001')
    """
    try:
        if assignment_id:
            assignment = Assignment.objects.get(id=assignment_id)
        elif assignment_code:
            assignment = Assignment.objects.get(assignment_code=assignment_code)
        else:
            print("Please provide either assignment_id or assignment_code")
            return
        
        print(f"\n{'='*60}")
        print(f"Verification for Assignment: {assignment.assignment_code}")
        print(f"Title: {assignment.title}")
        print(f"{'='*60}\n")
        
        # Get all files for this assignment
        files = AssignmentFile.objects.filter(assignment=assignment)
        
        print(f"Total files found in database: {files.count()}\n")
        
        if files.exists():
            print("Files Details:")
            print("-" * 60)
            for idx, f in enumerate(files, 1):
                print(f"{idx}. File Name: {f.file_name}")
                print(f"   File ID: {f.id}")
                print(f"   File Type: {f.file_type} ({f.get_file_type_display()})")
                print(f"   Uploaded By: {f.uploaded_by.get_full_name() if f.uploaded_by else 'Unknown'}")
                print(f"   Created At: {f.created_at}")
                try:
                    file_url = f.file.url if f.file else "No file path"
                    file_size = f.file.size if f.file else 0
                    print(f"   File URL: {file_url}")
                    print(f"   File Size: {file_size} bytes ({file_size / 1024:.2f} KB)")
                except (ValueError, AttributeError) as e:
                    print(f"   File URL: Error - {str(e)}")
                print("-" * 60)
        else:
            print("⚠ WARNING: No files found in database for this assignment!")
            print("This could mean:")
            print("  1. Files were not uploaded during form submission")
            print("  2. Files failed to save (check server logs)")
            print("  3. Files were deleted")
        
        print(f"\n{'='*60}\n")
        
    except Assignment.DoesNotExist:
        print(f"Assignment not found with ID: {assignment_id} or Code: {assignment_code}")
    except Exception as e:
        print(f"Error: {str(e)}")

