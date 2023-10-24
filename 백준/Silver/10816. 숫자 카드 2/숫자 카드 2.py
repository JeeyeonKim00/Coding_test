n = int(input())
n_lst = list(map(int, input().split()))
m = int(input())
m_lst = list(map(int, input().split()))

cnt_d = {}

for num in n_lst:
    cnt_d[num] = cnt_d.get(num,0)+1

for num in m_lst:
    cnt = cnt_d.get(num,0)
    print(cnt, end = ' ')