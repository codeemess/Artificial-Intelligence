
INITIAL_STATE = [[1,None,None,2],[None,None,None,None],[None,None,None,None],[4,None,None,3]]

def checkTerminalState(state):
    if state[0][0] == 3:
        return 3
    elif state[0][3] == 4:
        return 4 
    elif state[3][3] == 1:
        return 1
    elif state[3][0] == 2:
        return 2
    else: return 

