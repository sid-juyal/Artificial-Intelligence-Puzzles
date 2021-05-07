
initial, final = [3, 3, 1], [0, 0, 0]



def check(current):
    if 0 <= current[0] <= 3 and 0 <= current[1] <= 3:
        return True
    else:
        return False



def checkstate(current):
    rightside = [initial[i] - current[i] for i in range(3)]
    if current[1] > current[0] and current[0] != 0:
        x=0
    else:
        x=1
    if rightside[1] > rightside[0] and rightside[0] != 0:
        y=0
    else:
        y=1

    if x==1 and y==1:
        return True
    else:
        return False


def choose(current):
    actions = [[1, 0, 1], [0, 1, 1], [1, 1, 1], [2, 0, 1], [0, 2, 1]]
    moves = []
    for i in actions:
        if current[2] == 1:
            j= [current[x] - i[x] for x in range(3)]
        else:
            j= [current[x] + i[x] for x in range(3)]
        if check(j) and checkstate(j):
            moves.append(j)
    return moves

ans = []

def solution(nextstate, visited):
    visitedcopy = visited.copy()
    if nextstate == final:
        visitedcopy.append(nextstate)
        ans.append(visitedcopy)
        return
    elif nextstate in visited:
        return
    else:
        visitedcopy.append(nextstate)
        for i in choose(nextstate):
            solution(i, visitedcopy)

solution([3, 3, 1], [])
print(*ans, sep="\n")
