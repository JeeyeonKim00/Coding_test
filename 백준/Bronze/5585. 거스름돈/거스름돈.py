N = int(input())
N =1000-N
coin_lst = [500,100,50,10,5,1]

lst =[i for i in coin_lst if i<= N]
cnt =0


while N>0:
    cnt += N//max(lst)
    N = N%max(lst)
    lst.pop(lst.index(max(lst)))
print(cnt)