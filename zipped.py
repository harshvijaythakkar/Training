n,x = map(int, input().split(" "))
l1, l2, l3 = [], [], []
list2 = []
for num in range(x):
    l = [float(a) for a in input().split(" ")]
    list2.append(l)

print(list2)
l1.extend(list2[0])
l2.extend(list2[1])
l3.extend(list2[2])
print(l1, l2, l3)
s = (list(zip(l1,l2,l3)))
print(s)

sum1 = list(map(sum, s))

print(sum1)

for num in sum1:
    print(num/x)
