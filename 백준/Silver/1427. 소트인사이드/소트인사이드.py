n = input()
lst = [int(x) for x in n]
lst.sort(reverse=True)
print(*lst,sep='')