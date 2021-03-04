def solution(s, n):
    result = ''
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].islower():
                x = chr(ord(s[i])+n-26) if ord(s[i])+n>ord('z') else chr(ord(s[i])+n)
                result += x
            else:
                x = chr(ord(s[i])+n-26) if ord(s[i])+n>ord('Z') else chr(ord(s[i])+n)
                result += x
        else:
            result += ' '
        # print(chr((ord(s[i])+1)%26))
    return result