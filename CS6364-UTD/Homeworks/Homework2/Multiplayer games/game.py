from collections import deque
import operator
INITIAL_BOARD = [[1,None,None,2],[None,None,None,None],[None,None,None,None],[4,None,None,3]]
    
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
        
    def generateValidPositions(state):
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

    def moveUp(self,board):
        newBoard = board
        position = self.position
        x = ()
        if(position[0]-1 > 0 and board[position[0]-2][position[1]-1]==None):
            x = (position[0]-1,position[1])
            return x
    
    def moveDown(self,board):
        newBoard = board
        position = self.position
        x = ()
        if(position[0]+1 < 5 and board[position[0]][position[1]-1]==None):
            x = (position[0]+1,position[1])
            return x
    
    def moveLeft(self,board):
        newBoard = board
        position = self.position
        x = ()
        if(position[1]-1 > 0 and board[position[0]-1][position[1]-2]==None):
            x = (position[0],position[1]-1)
            return x
    
    def moveRight(self,board):
        newBoard = board
        position = self.position
        x = ()
        if(position[1]+1 <5  and board[position[0]-1][position[1]]==None):
            x = (position[0],position[1]+1)
            return x

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
    up = Player2.moveLeft(INITIAL_BOARD)
    print(up)

    # while(queue):
    #     current = queue.popleft()
    #     print(current)
    #print(initial_state.playerPositions)
    #def generateGameTree(players,chance):
        

        
g = Game()

# [Current player =???| Father node (if not initial node) =???| Action= ????| Current game node =???| 
# if the game node is repeated, write REPEATED; if the current game node corresponds to a winning situation for one of the players, write WINS[PLAYER???]]
# P1 P2 
# Hint: Successors of repeated game nodes should not be considered!