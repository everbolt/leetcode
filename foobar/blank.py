def solution(n):    
    box = {i: [] for i in range(4, n + 1)}
    box[3] = [[1,2]]
    for i in range(4, n + 1):
        old_list = box[i - 1]
        for old in old_list:
            temp = old[:]
            temp[-1] += 1
            if temp not in box[i]:
                box[i].append(temp) #Add list with +1 to last
            
            if old[0] > 1: #First element is not 1
                temp = [1] + old
                if temp not in box[i]:
                    box[i].append(temp) #Add list with 1 appended to start

            for j in range(len(old) - 1):
                if old[j] < old[j + 1] - 1:
                    temp = old[:]
                    temp[j] += 1
                    if temp not in box[i]:
                        box[i].append(temp)
    return len(box[n])
    #return box

example = {
    3: [[1,2]], #0
    4: [[1,3]], #3
    5: [[1,4], [2,3]], #4
    6: [[1,5], [2,4], [1,2,3]], #5
    7: [[1,6], [2,5], [3,4], [1,2,4]], #6
    8: [[1,7], [2,6], [3,5], [1,2,5], [1,3,4]], #8
    9: [[1,8], [2,7], [3,6], [4,5], [1,2,6], [1,3,5], [2,3,4]]
}

#Rules
#Seq doesn't start with 1
#Add 1 to any part of seq
    #That has room

#print(solution(50))
n = 100
print(solution(n))