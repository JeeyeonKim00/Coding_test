def solution(s):
    lst = list(s)
    sorted_lst = sorted(lst, reverse=True)
    return ''.join(sorted_lst)
    # return answer