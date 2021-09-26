def solution(s):
    answer = ''
    c = len(s) % 2
    d = len(s) // 2
    if c==0 :
        answer += s[d-1]+s[d]
    else :
        answer += s[d]
    return answer