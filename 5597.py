import sys
input = sys.stdin.readline

students = []
for i in range(1, 31):
    students.append(i)

for j in range(28):
    try:
        student = int(input())
        students.remove(student)
    except:
        pass

for student in students:
    print(student)