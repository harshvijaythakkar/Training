cube = lambda x : (x*x*x)

def fibonacci(n):
    l = []    
    a = 0
    b = 1
    l.extend([a,b])

    for _ in range(n):    
        c = a+b
        l.append(c)
        a = b
        b = c
    return l[:n] #only n fibonacci numbers



n = int(input())

print(list(map(cube, fibonacci(n))))


