N = int(input())
num_lst = [int(input()) for _ in range(N)]
num_lst.sort()

print(*num_lst, sep='\n')