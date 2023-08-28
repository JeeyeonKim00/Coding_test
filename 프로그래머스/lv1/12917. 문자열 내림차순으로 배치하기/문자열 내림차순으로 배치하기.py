def solution(s):
    sorted_lst = sorted(s, reverse=True)
    return ''.join(sorted_lst)
    # return answer