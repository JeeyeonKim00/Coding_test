n = int(input())

min_lst = list(map(int, input().split()))
min_lst.sort()

total_time = 0
lst = []

for i in range(n):
    total_time += min_lst[i]
    lst.append(total_time)

print(sum(lst))


