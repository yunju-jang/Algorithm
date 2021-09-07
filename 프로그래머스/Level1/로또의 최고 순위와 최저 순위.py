def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    zero = lottos.count(0)
    count = 0
    for i in lottos:
        for j in win_nums:
            if i == j:
                count += 1
            
    return rank[count+zero], rank[count]