N = int(input())
word_lst = [input() for _ in range(N)]
word_lst = list(set(word_lst))
word_lst_2 = [(i, len(i))for i in word_lst]
sorted_lst = sorted(word_lst_2, key= lambda x: (x[1],x[0]))
fin_lst = [i[0] for i in sorted_lst]
print(*fin_lst, sep='\n')