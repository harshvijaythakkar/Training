def wrap(string, max_width):
    start = 0
    end = max_width
    ans = ""
    while end<=len(string):
        l = ""
        l = string[start:end]
        ans=ans+l+"\n"
        #print(ans)
        start = end
        end += max_width
    if end > len(string):
        ans=ans+string[start:len(string)]
    return str(ans)

string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)
