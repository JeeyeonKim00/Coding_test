def solution(citations):
    max_citation = max(citations)
    paper_count = [0] * (max_citation + 1)

    # 각 인용 횟수별 논문 수를 센다.
    for citation in citations:
        paper_count[citation] += 1

    total_papers = 0

    # H-지수를 계산한다.
    for h in range(max_citation, -1, -1):
        total_papers += paper_count[h]
        if total_papers >= h:
            return h

    return 0  # H-지수를 찾지 못한 경우 0을 반환한다.