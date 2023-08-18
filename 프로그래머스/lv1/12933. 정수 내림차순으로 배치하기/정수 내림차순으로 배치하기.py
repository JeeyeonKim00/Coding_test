def solution(n):
    a = [i for i in str(n)]
    a.sort(reverse=True)
    b = ''.join(a)
    
    return int(b)