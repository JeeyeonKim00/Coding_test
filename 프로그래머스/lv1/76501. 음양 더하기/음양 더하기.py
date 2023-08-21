def solution(absolutes, signs):
  
    return sum([-ab if si == False else +ab for ab,si in zip(absolutes, signs)])

