def count_substring(string, sub_string):
    sublen = len(sub_string)
    index = 0
    count = 0
    while index < len(string):
        sub = string[index:sublen+index]
        if sub == sub_string:
            count += 1
        index += 1
        
    return count


string = input().strip()
sub_string = input().strip()

count = count_substring(string, sub_string)
print(count)

