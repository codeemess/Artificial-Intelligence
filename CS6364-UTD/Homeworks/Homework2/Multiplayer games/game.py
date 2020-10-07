from collections import deque
import operator
import json
INITIAL_BOARD = [[1,"None","None",2],["None","None","None","None"],["None","None","None","None"],[4,"None","None",3]]
    
class State(object):
    
    players = "None"
    playerPositions = {}
    currentPlayer = "None"
    parent = "None"
    repeated = "None"
    action = "None"
    depth = "None"
    terminal = "None"
    winner = "None"
    
    def __init__(self,players):
        for player in range(1,5):
            self.playerPositions[player] =  players[player-1].position
        
    def generateValidPositions(state):
        pass

    def isTerminatingCondition(position):
        pass


class Player(object):
    utility = "None"
    position = "None"
    TERMINATING_POSITION = "None"
    def __init__(self,position,terminating_pos):
        self.position = position
        self.TERMINATING_POSITION = terminating_pos
    
    def getAllActions():
        pass
    
    def generateNextMove():
        pass

    def moveUp(self,position,board):
        newBoard = board
        x = []
        x.append(position[0]-1)
        x.append(position[1])
        if(position[0]-1 > 0 and board[position[0]-2][position[1]-1]=="None"):
            # x = (position[0]-1,position[1])
            newBoard[position[0]-2][position[1]-1] = board[position[0]-1][position[1]-1]
            newBoard[position[0]-1][position[1]-1] = "None"
            
        if(x[0]>0):
            return tuple(x),newBoard
        else:
            return 0
    
    def moveDown(self,position,board):
        newBoard = board
        x = []
        x.append(position[0]+1)
        x.append(position[1])
        if(x[0] < 5 and board[position[0]][position[1]-1]=="None"):
            board[position[0]][position[1]-1] = board[position[0]-1][position[1]-1]
            newBoard[position[0]-1][position[1]-1] = "None"
        if(x[0]<5):
            return tuple(x),newBoard
        else:
            return 0
    
    def moveLeft(self,position,board):
        newBoard = board
        x = []
        x.append(position[0])
        x.append(position[1]-1)
        if(position[1]-1 > 0 and board[position[0]-1][position[1]-2]=="None"):
            # x = (position[0],position[1]-1)
            board[position[0]-1][position[1]-2] = board[position[0]-1][position[1]-1]
            newBoard[position[0]-1][position[1]-1] = "None"
        if(x[1]>0 ):
            return tuple(x),newBoard
        else:
            return 0
    
    def moveRight(self,position,board):
        newBoard = board
        x = []
        x.append(position[0])
        x.append(position[1]+1)
        if(position[1]+1 <5  and board[position[0]-1][position[1]]=="None"):
            # x = (position[0],position[1]+1)
            board[position[0]-1][position[1]] = board[position[0]-1][position[1]-1]
            newBoard[position[0]-1][position[1]-1] = "None"
            
        if(x[1]<5):
            return tuple(x),newBoard
        else:
            return 0

    def isTerminatingCondition(self,position):
        if position == self.TERMINATING_POSITION:
            return True
        return False


class Game(object):

    GameTree = []
    exploredStates = ()
    Player1 = Player((1,1),(4,4))
    Player2 = Player((1,4),(4,1))
    Player3 = Player((4,4),(1,1))
    Player4 = Player((4,1),(1,4))

    players = [Player1,Player2,Player3,Player4]
    queue = deque()
    initial_state = State(players)
    root = {"State": initial_state.playerPositions, "Parent": "None", "Level": 0, "Action": "None", "Current Player": 0, 
    "Repeated": False, "Terminating": False, "Winner": "None", "Board":INITIAL_BOARD}
    queue.append(root)
    playerTurn = 1
        
    while(queue):
        
        current = queue.popleft()
        listx = [(k, v) for k, v in current["State"].items()]
        x = tuple(listx)
        temp = list(exploredStates)
        temp.append(x)
        exploredStates = tuple(temp)
        exploredStates = set(exploredStates)
        
        parent = current["State"]
        level = current["Level"] + 1
        playerTurn = current["Current Player"]
        
        if current["Current Player"] == 4:
            playerTurn = 1
        else:
            playerTurn = playerTurn +1
        
        player = players[playerTurn-1]

        if(current["Terminating"] == False or current["Repeated"] == False):

            o = player.moveDown(current['State'][playerTurn],current['Board'])
            if(o != 0):
                
                # down = player.moveDown(current['State'][playerTurn],current['Board'])
                # print(down)
                updatedState = current["State"]
                updatedState[playerTurn] = o[0]
                board = o[1]
                repeated = False
                terminate = False
                winner = "None"
                listzzz = tuple([(k, v) for k, v in updatedState.items()])
                if listzzz in exploredStates:
                    repeated = True
                if player.isTerminatingCondition(o[0]):
                    terminate = True
                    winner = playerTurn
                newNode = {}
                newNode["State"] = updatedState
                newNode["Parent"] = parent
                newNode["Level"] = level
                newNode["Action"] = "Down"
                newNode["Current Player"] = playerTurn
                newNode["Repeated"] = repeated
                newNode["Board"] = board
                newNode["Terminating"] = terminate
                newNode["Winner"] = winner
                print(newNode)
                queue.append(newNode)
                GameTree.append(newNode)

            p = player.moveUp(current['State'][playerTurn],current['Board']) 
            if(p != 0):    
                up = player.moveUp(current['State'][playerTurn],current['Board'])
                updatedState = current["State"]
                updatedState[playerTurn] = p[0]
                board = p[1]
                repeated = False
                terminate = False
                winner = "None"
                listzzz = tuple([(k, v) for k, v in updatedState.items()])
                if listzzz in exploredStates:
                    repeated = True
                if player.isTerminatingCondition(p[0]):
                    terminate = True
                    winner = playerTurn
                newNode = {}
                newNode["State"] = updatedState
                newNode["Parent"] = parent
                newNode["Level"] = level
                newNode["Action"] = "Up"
                newNode["Current Player"] = playerTurn
                newNode["Repeated"] = repeated
                newNode["Board"] = board
                newNode["Terminating"] = terminate
                newNode["Winner"] = winner
                print(newNode)
                queue.append(newNode)
                GameTree.append(newNode)
            
            q = player.moveLeft(current['State'][playerTurn],current['Board'])
            if(q != 0):
                left = player.moveLeft(current['State'][playerTurn],current['Board']) 
                updatedState = current["State"]
                updatedState[playerTurn] = q[0]  
                board = q[1]
                repeated = False
                terminate = False
                winner = "None"
                listzzz = tuple([(k, v) for k, v in updatedState.items()])  
                if listzzz in exploredStates:
                    repeated = True
                if player.isTerminatingCondition(q[0]):
                    terminate = True
                    winner = playerTurn
                newNode = {}
                newNode["State"] = updatedState
                newNode["Parent"] = parent
                newNode["Level"] = level
                newNode["Action"] = "Left"
                newNode["Current Player"] = playerTurn
                newNode["Repeated"] = repeated
                newNode["Board"] = board
                newNode["Terminating"] = terminate
                newNode["Winner"] = winner
                print(newNode)
                queue.append(newNode)
                GameTree.append(newNode)
            
            r= player.moveRight(current['State'][playerTurn],current['Board'])
            if(r != 0):
                right = player.moveRight(current['State'][playerTurn],current['Board'])
                updatedState = current["State"]
                updatedState[playerTurn] = r[0]
                board = r[1]
                repeated = False
                terminate = False
                winner = "None"
                listzzz = tuple([(k, v) for k, v in updatedState.items()])
                if listzzz in exploredStates:
                    repeated = True
                if player.isTerminatingCondition(r[0]):
                    terminate = True
                    winner = playerTurn
                newNode = {}
                newNode["State"] = updatedState
                newNode["Parent"] = parent
                newNode["Level"] = level
                newNode["Action"] = "Right"
                newNode["Current Player"] = playerTurn
                newNode["Repeated"] = repeated
                newNode["Board"] = board
                newNode["Terminating"] = terminate
                newNode["Winner"] = winner
                print(newNode) 
                queue.append(newNode)
                GameTree.append(newNode)
    
    with open("sample.json", "w") as outfile: 
        json.dump(GameTree, outfile) 


g = Game()

# [Current player =???| Father node (if not initial node) =???| Action= ????| Current game node =???| 
# if the game node is repeated, write REPEATED; if the current game node corresponds to a winning situation for one of the players, write WINS[PLAYER???]]
# P1 P2 
# Hint: Successors of repeated game nodes should not be considered!