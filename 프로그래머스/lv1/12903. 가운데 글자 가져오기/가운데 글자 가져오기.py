def solution(s):
 
    return s[len(s)//2-1]+s[len(s)//2] if len(s)%2 == 0 else s[round(len(s)//2)]