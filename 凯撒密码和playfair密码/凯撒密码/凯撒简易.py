s = input()
t = ""
for c in s:
    if 'A'<= c <= 'Z':
        t += chr(ord('A') + (ord(c)-ord('A')+3)%26)
    elif 'a'<= c <= 'z':
        t += chr(ord('a') + (ord(c)-ord('a')+3)%26)
    else:
        t += c
print(t)
