from collections import deque
INITIAL_STATE = [[1,None,None,2],[None,None,None,None],[None,None,None,None],[4,None,None,3]]
    
class State(object):
    
    players = None
    playerPositions = {}
    currentPlayer = None
    parent = None
    repeated = None
    action = None
    depth = None
    terminal = None
    winner = None
    
    def __init__(self,players):
        for player in range(1,5):
            self.playerPositions[player] =  players[player-1].position
        
    def generateValidPositions(position,action):
        pass
    
    def isTerminatingCondition(position):
        pass


class Player(object):
    utility = None
    position = None
    def __init__(self,position):
        self.position = position
    
    def getAllActions():
        pass
    
    def generateNextMove():
        pass

class Game(object):
    GameTree = []
    exploredStates = {}
    Player1 = Player((1,1))
    Player2 = Player((1,4))
    Player3 = Player((4,4))
    Player4 = Player((4,1))
    players = [Player1,Player2,Player3,Player4]
    queue = deque()
    initial_state = State(players)
    root = {"State": initial_state.playerPositions, "Parent": None, "Level": 0, "Action": None, "Current Player": None, "Parent": None, 
    "Repeated": False, "Terminating": False, "Winner": None}
    queue.append(root)
    while(queue):
        current = queue.popleft()
        print(current)   
    #print(initial_state.playerPositions)
    #def generateGameTree(players,chance):
        

        
g = Game()

# [Current player =???| Father node (if not initial node) =???| Action= ????| Current game node =???| 
# if the game node is repeated, write REPEATED; if the current game node corresponds to a winning situation for one of the players, write WINS[PLAYER???]]
# P1 P2 
# Hint: Successors of repeated game nodes should not be considered!