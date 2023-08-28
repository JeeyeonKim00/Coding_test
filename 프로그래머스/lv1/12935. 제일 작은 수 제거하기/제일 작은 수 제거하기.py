def solution(arr):
    arr.remove(min(arr))
    return arr if len(arr) > 1 else [-1]
    # arr.remove(min(arr))
    # return arr
#     if len(arr) > 1:
#         arr.sort(reverse=True)
#         arr.remove(min(arr))
#         return arr     
#     elif len(arr) <= 1:
#         return [-1]
     