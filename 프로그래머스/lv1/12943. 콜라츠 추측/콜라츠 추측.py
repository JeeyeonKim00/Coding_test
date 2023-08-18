def solution(num):
    try_num = 0
    
    while num !=1:
        if num % 2 ==0:
            num = num /2
        else:
            num = (num*3)+1
        try_num += 1
        if try_num >= 500:
            try_num = -1
            break
    return try_num