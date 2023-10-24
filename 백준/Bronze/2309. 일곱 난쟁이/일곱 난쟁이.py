lst = [int(input()) for _ in range(9)]
num_lst = []
for i in lst:
    for j in lst:
        if (i,j) not in num_lst and (j,i) not in num_lst and i != j:
            num_lst.append((i,j))   

test_lst = []
for i in num_lst:
    lst2 = lst.copy()
    if i[0] in lst2:
        lst2.remove(i[0])
    if i[1] in lst2: 
        lst2.remove(i[1])
    sum_lst = sum(lst2)
    if sum_lst == 100:
        test_lst.append((i[0],i[1]))

lst.remove(test_lst[0][0])
lst.remove(test_lst[0][1])
lst.sort()
print(*lst,sep='\n')