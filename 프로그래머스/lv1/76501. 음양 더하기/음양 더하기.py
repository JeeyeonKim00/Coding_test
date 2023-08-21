def solution(absolutes, signs):
    signs_modified = ['-' if i == False else '+' for i in signs ]
    fin_num = 0
    for num, pm in zip(absolutes, signs_modified):
        fin_num += int(pm+str(num))
    
    return fin_num