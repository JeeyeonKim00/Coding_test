def solution(s):
    import re
    if s.isdigit() == True and (len(s)==4 or len(s)==6):
        answer = True
    else:
        answer = False
    return answer
    
    