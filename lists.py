
n = int(input())

ans = []

while n > 0:
    l = []
    
    data = input().split()
    l.extend(data)
##    print(l)
    if l[0] == 'insert':
        e = int(l[2])
        i = int(l[1])
        ans.insert(i,e)
    elif l[0] == 'remove':
        e = int(l[1])
        ans.remove(e)
    elif l[0] == 'sort':
        ans.sort()
    elif l[0] == 'reverse':
        ans.reverse()
    elif l[0] == 'pop':
        ans.pop()
    elif l[0] == 'print':
        print(ans)
    elif l[0] == 'append':
        e = int(l[1])
        ans.append(e)
    else:
        pass
    n -= 1

##print(ans)










