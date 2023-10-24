n, m = map(int, input().split())

never_heard = [input() for i in range(n)]
never_seen = [input() for i in range(m)]

dict2 = {}
for word in never_heard:
    dict2[word] = dict2.get(word,0)

for word in never_seen:
    if word in dict2.keys():
        dict2[word] = dict2.get(word,0) +1

tot_lst = [i for i,j in dict2.items() if j>=1]
tot_lst.sort()
print(len(tot_lst))
print(*tot_lst,sep='\n')