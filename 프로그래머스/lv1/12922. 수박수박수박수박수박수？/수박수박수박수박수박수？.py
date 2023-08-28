def solution(n):
    string = ''
    while len(string) < 10000:
        string += '수'
        string += '박'
    answer = string[:n]
    return answer