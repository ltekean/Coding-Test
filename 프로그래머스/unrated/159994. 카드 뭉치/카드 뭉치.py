from collections import deque
def solution(cards1, cards2, goal):
    idx1=0
    idx2=0
    for i in range(len(goal)):
        if idx1< len(cards1) and cards1[idx1] == goal[i] :
            idx1+=1
        elif idx2 < len(cards2) and cards2[idx2] == goal[i] :
            idx2+=1
        else:
            return "No"
    
    return "Yes"