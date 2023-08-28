def solution(price, money, count):
    total_money = 0
    for i in range(1,count+1):
        total_money += price*i
    answer = total_money - money
    if answer > 0 :
        return answer
    else:
        return 0
