def solution(p):
    def seperate_w(p):  # u,v로 문리하는 함수
        cnt = 0
        flag = True
        for i in range(len(p)):
            if p[i] == '(':
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                break
            if cnt < 0:
                flag = False
        return p[:i + 1], p[i + 1:], flag

    def reverse_p(strp):
        result = ''
        for p in strp:
            result += '(' if p == ')' else ')'
        return result

    def rearrange(p):
        if not p:
            return p
        u, v, flag = seperate_w(p)
        if flag:
            return u + rearrange(v)
        else:
            return '(' + rearrange(v) + ')' + reverse_p(u[1:-1])

    return rearrange(p)