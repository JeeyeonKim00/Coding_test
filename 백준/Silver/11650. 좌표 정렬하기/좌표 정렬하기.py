N = int(input())
num_lst = [tuple(map(int, input().split())) for _ in range(N)]
new_lst = sorted(num_lst, key = lambda x: (x[0],x[1]))
for i in new_lst:
    print(i[0], i[1])