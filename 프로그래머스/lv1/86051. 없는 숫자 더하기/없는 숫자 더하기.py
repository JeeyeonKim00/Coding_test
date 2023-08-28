def solution(numbers):
    num_lst =[0,1,2,3,4,5,6,7,8,9]
    num_not_in = [n for n in num_lst if n not in numbers] 
    # sum([i for i in [1,2,3,4,5,6,7,8,9,0] if i not in numbers])
    # print(num_not_in)
    return sum(num_not_in)

