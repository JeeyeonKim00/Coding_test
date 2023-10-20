N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]

coin_cnt = 0 

while K > 0 :
    lst = [num for num in coin if num <= K]

    coin_cnt += K//max(lst) #몫
    K = K%max(lst) 
print(coin_cnt)
    
    