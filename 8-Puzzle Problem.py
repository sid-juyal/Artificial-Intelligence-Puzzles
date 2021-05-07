import copy
frontier = []
explored = []

''' METHOD FOR FINDING THE POSITION OF BLANK SLIDE '''

def find_pos(current):
    for i in range(3):
        for j in range(3):
            if current[i][j] == 0:
                r,c = i, j
                return r,c

''' METHOD FOR THE UP MOVEMENT OF THE BLANK SLIDE '''

def up(current, r, c):
    if r != 0:
        child = copy.deepcopy(current)
        child[r][c],child[r - 1][c] = (child[r - 1][c],0)
        if child not in frontier and child not in explored:
            frontier.append(child)
            return child
    return None

''' METHOD FOR THE DOWN MOVEMENT OF THE BLANK SLIDE'''

def down(current, r, c):
    if r != 2:
        child = copy.deepcopy(current)
        child[r][c], child[r+1][c] = (child[r+1][c],0)
        if child not in frontier and child not in explored:
            frontier.append(child)
            return child
    return None

''' METHOD FOR THE LEFT MOVEMENT OF THE BLANK SLIDE '''

def left(current, r, c):
    if c != 0:
        child = copy.deepcopy(current)
        child[r][c], child[r][c-1] = (child[r][c-1],0)
        if child not in frontier and child not in explored:
            frontier.append(child)
            return child
    return None

''' METHOD FOR THE RIGHT MOVEMENT OF THE BLANK SLIDE '''

def right(current, r, c):
    if c != 2:
        child = copy.deepcopy(current)
        child[r][c], child[r][c+1] = (child[r][c+1],0)
        if child not in frontier and child not in explored:
            frontier.append(child)
            return child
    return None

''' METHOD FOR CHECKING IF CURRENT STATE IS THE GOAL STATE '''

def is_goal(current, goal_state):
    if current == goal_state:
        return True
    else:
        return False
''' METHOD TO SEARCH  FOR THE GOAL STATE'''

def search():
    initial_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
    goal_state = [[2, 8, 1], [0, 4, 3], [7, 6, 5]]
    #goal_state = [[8, 2, 4], [5, 7, 0], [6, 1, 3]]
    frontier.append(initial_state)
    flag = 1
    while flag:
        current = frontier.pop(0)
        if is_goal(current,goal_state):
            flag = 0
            print(len(explored))
        else:
            r,c = find_pos(current)
            neighbor = [0] * 4
            neighbor[0] = up(current,r,c)
            neighbor[1] = down(current,r,c)
            neighbor[2] = left(current,r,c)
            neighbor[3] = right(current,r,c)
            explored.append(current)
            for i in neighbor:
                if i != None and i != 0:
                    if is_goal(i,goal_state):
                        flag = 0
                        print("All states visited from start state to reach goal state:")
                        for state in explored:
                            print(state)
                        print("Number of states explored", len(explored))

search()

