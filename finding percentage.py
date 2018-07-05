n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

print(student_marks)
l = []

for name in student_marks:
    if name == query_name:
        l.extend(student_marks[query_name])
ans = sum(l)/3

print("%.2f" % (ans))
