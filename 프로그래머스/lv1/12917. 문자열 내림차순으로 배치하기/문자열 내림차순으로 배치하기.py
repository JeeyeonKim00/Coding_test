def solution(s):
    lst = []
    for i in range(len(s)):
        lst.append(s[i])
    lst.sort(reverse=True)
    answer =''
    for k in lst:
        answer += k
    return answer