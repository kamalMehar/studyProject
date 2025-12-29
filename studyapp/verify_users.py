"""
Quick script to verify test users exist and check their credentials.
Run: python manage.py shell < verify_users.py
Or: python manage.py shell, then copy-paste this code
"""
from account.models import User

print("\n=== Checking Test Users ===\n")

# Check Admin
try:
    admin = User.objects.get(username='admin')
    print(f"✓ Admin user found:")
    print(f"  Email: {admin.email}")
    print(f"  Username: {admin.username}")
    print(f"  Role: {admin.role}")
    print(f"  User ID (UUID): {admin.id}")
    print(f"  Is Active: {admin.is_active}")
    print(f"  Password check (admin123): {admin.check_password('admin123')}\n")
except User.DoesNotExist:
    print("✗ Admin user NOT found\n")

# Check Teacher
try:
    teacher = User.objects.get(username='teacher')
    print(f"✓ Teacher user found:")
    print(f"  Email: {teacher.email}")
    print(f"  Username: {teacher.username}")
    print(f"  Role: {teacher.role}")
    print(f"  User ID (UUID): {teacher.id}")
    print(f"  Is Active: {teacher.is_active}")
    print(f"  Password check (teacher123): {teacher.check_password('teacher123')}\n")
except User.DoesNotExist:
    print("✗ Teacher user NOT found\n")

# Check CS-Rep
try:
    csrep = User.objects.get(username='csrep')
    print(f"✓ CS-Rep user found:")
    print(f"  Email: {csrep.email}")
    print(f"  Username: {csrep.username}")
    print(f"  Role: {csrep.role}")
    print(f"  User ID (UUID): {csrep.id}")
    print(f"  Is Active: {csrep.is_active}")
    print(f"  Password check (csrep123): {csrep.check_password('csrep123')}\n")
except User.DoesNotExist:
    print("✗ CS-Rep user NOT found\n")

print("=== Done ===\n")

