def fun(s):
    if '@' not in s:
        return False
    username = s.split('@')
    print(username)
    if (s.find('@') + 1 == ' '):
        return False
    if ' ' in username[0] or username[0] == '' or '@' in username[0]:
        return False
    for c in '!@#$%^&*()+=/<>?;:':
        if c in username[0]:                
            return False
    if '.' not in username[1]:
        return False
    web, ext = (username[-1].split('.'))
    
    print(web, ext)
    if len(ext) > 3:
        return False
    if not web.isalnum():
        return False
    
    return True



s = 'harsh@gmail.com'
print(s.isalnum())



def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)



