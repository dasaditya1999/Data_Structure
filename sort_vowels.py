s = 'lEetcOde'

ascii_values = [97,101,105,111,117,65,69,73,79,85]

l =  [ i for i in s if ord(i) in ascii_values]
l.sort()

result = ""
index = 0
for i in range(0,len(s)):
    if ord(s[i]) in ascii_values:
        result = result + l[index]
        index = index + 1
    else:
        result = result + s[i]

print(s)
print(result)