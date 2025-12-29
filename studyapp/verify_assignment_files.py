"""
Quick script to verify assignment files are saved in database.
Run: python manage.py shell
Then: exec(open('verify_assignment_files.py').read())
Or: python manage.py shell < verify_assignment_files.py
"""
from assingment.models import Assignment, AssignmentFile
from django.utils import timezone
from datetime import timedelta

print("\n" + "="*60)
print("ASSIGNMENT FILES VERIFICATION")
print("="*60 + "\n")

# Get recent assignments (last 24 hours)
recent_assignments = Assignment.objects.filter(
    created_at__gte=timezone.now() - timedelta(hours=24)
).order_by('-created_at')[:10]

if not recent_assignments.exists():
    print("No recent assignments found (last 24 hours)")
else:
    print(f"Found {recent_assignments.count()} recent assignment(s):\n")
    
    for assignment in recent_assignments:
        files = AssignmentFile.objects.filter(assignment=assignment)
        file_count = files.count()
        
        print(f"Assignment: {assignment.assignment_code}")
        print(f"  Title: {assignment.title}")
        print(f"  Created: {assignment.created_at}")
        print(f"  Files in database: {file_count}")
        
        if file_count > 0:
            print("  File details:")
            for idx, f in enumerate(files, 1):
                try:
                    file_url = f.file.url if f.file else "No file"
                    file_size = f.file.size if f.file else 0
                    print(f"    {idx}. {f.file_name}")
                    print(f"       ID: {f.id}, Type: {f.file_type}")
                    print(f"       URL: {file_url}")
                    print(f"       Size: {file_size} bytes ({file_size/1024:.2f} KB)")
                except Exception as e:
                    print(f"    {idx}. {f.file_name} (Error getting file info: {str(e)})")
        else:
            print("  ⚠ WARNING: No files found in database!")
        
        print()

print("="*60)
print("Verification complete!")
print("="*60 + "\n")

