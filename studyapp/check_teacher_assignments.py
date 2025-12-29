from account.models import User, Teacher
from assingment.models import TeacherAssignment

users = User.objects.filter(role='TEACHER')
print(f"Total teachers: {users.count()}")
for u in users:
    print(f"Teacher: {u.get_full_name()}, ID: {u.id}")
    if hasattr(u, 'teacher_profile'):
        tp = u.teacher_profile
        tas = TeacherAssignment.objects.filter(teacher=tp)
        print(f"  Assigned tasks: {tas.count()}")
        for ta in tas:
            print(f"    - Student: {ta.assignment.student.user.get_full_name()}, Assignment: {ta.assignment.title}")

