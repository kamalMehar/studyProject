from homework.models import Homework
from account.models import Student

hws = Homework.objects.all()
print(f"Total homeworks: {hws.count()}")
for h in hws:
    print(f"ID: {h.id}, Title: {h.title}, Student: {h.student.user.get_full_name()}, StudentID: {h.student.id}, Status: {h.status}")

students = Student.objects.all()
for s in students:
    print(f"Student: {s.user.get_full_name()}, id: {s.id}")

