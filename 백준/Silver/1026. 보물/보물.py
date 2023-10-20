N = int(input())
A = list(map(int, input().split()))
A.sort()
B = list(map(int, input().split()))

tot = 0
for i in range(N):
    tot += A[i]*max(B)
    B.pop(B.index(max(B)))

print(tot)
    
