from account.models import Student
students = Student.objects.all()
print(f"Total students: {students.count()}")
for s in students:
    print(f"Name: {s.user.get_full_name()}, UUID: {s.id}, StudentID: {s.student_id}")

