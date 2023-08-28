def solution(s):
    if len(s)%2 ==0:
        i = len(s)//2
        answer = s[i-1]+s[i]
    else:
        i = round(len(s)//2)
        answer = s[i]
    print(i)
    return answer