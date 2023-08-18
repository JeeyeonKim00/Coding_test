def solution(s):
    s_low = s.lower()
    return True if s_low.count('p') == s_low.count('y') else False
