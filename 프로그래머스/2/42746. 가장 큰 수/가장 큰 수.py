import functools

def comparator(a,b): # a,b는 문자열
    t1 = a+b
    t2 = b+a
    return (int(t1)>int(t2))- (int(t1)<int(t2))

def solution(numbers):
    n = [str(i) for i in numbers]
    n = sorted(n, key = functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer