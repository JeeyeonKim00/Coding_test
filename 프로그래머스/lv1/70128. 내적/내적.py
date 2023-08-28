def solution(a, b):
    i = 0
    for k in range(len(a)):
        print(a[k], b[k])
        i += (a[k]*b[k])
    return i