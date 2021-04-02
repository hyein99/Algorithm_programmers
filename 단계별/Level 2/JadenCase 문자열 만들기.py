def make_jaden(substr):
    if not substr:
        return ''
    return substr[0].upper() + substr[1:].lower()

def solution(s):
    new_s = ''
    tmpstr = ''
    for i in range(len(s)):
        if s[i] == ' ':
            new_s += make_jaden(tmpstr)
            new_s += ' '
            tmpstr = ''
        else:
            tmpstr += s[i]
    new_s += make_jaden(tmpstr)
    return new_s