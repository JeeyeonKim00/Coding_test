from bisect import bisect_left, bisect_right

def search_bin(array, target):
    lst.sort()
    left_index = bisect_left(array,target)
    right_index = bisect_right(array, target)
    return right_index-left_index

n = int(input())
lst = list(map(int, input().split()))
v = int(input())
print(search_bin(lst, v))