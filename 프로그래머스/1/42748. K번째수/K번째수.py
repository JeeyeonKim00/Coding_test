def solution(array, commands):
    fin_lst = []
    for i,j,k in commands:
        lst = array[i-1:j]
        lst.sort()
        fin_lst.append(lst[k-1])
    return fin_lst