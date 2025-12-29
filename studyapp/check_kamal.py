from account.models import Student
student = Student.objects.get(id=1)
print(f"Student: {student.user.get_full_name()}")
print(f"Email: '{student.user.email}'")
print(f"Student ID: '{student.student_id}'")

