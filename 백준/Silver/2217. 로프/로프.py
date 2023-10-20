N =int(input())
l = [int(input()) for _ in range(N)]
l.sort()

index_lst = [N-i for i in range(len(l))]
mul_lst = [l[i]*index_lst[i] for i in range(len(l))]
print(max(mul_lst))