from collections import Counter

def solution(participant, completion):
    participant_count = Counter(participant)
    completion_count = Counter(completion)

    diff = participant_count - completion_count
    answer = list(diff.keys())[0]
    
    return answer
