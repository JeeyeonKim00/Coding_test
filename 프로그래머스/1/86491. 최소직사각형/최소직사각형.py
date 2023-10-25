# def solution(sizes):
# #     for i in sizes:
# #         if i[0] < i[1]:
# #             i[0],i[1] = i[1], i[0]

# #     width = []
# #     height = []

# #     for i in sizes:
# #         width.append(i[0])
# #         height.append(i[1])

# #     answer = max(width)*max(height)
#     return answer

def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)