
INITIAL_STATE = [[1,None,None,2],[None,None,None,None],[None,None,None,None],[4,None,None,3]]

class State(object):
    currentPosition = ()
    
    def __init__(self,position):
        self.currentPosition = position
    
    def generateValidPositions(position,action):
        pass

class Player(object):
    state = None

    def __init__(self,position):
        self.state = State(position)
        print("hi")
    
    def getAllActions():
        pass

class Game(object):
    GameTree = {}
    exploredStates = {}
    Player1 = Player((1,1))
    Player2 = Player((1,4))
    Player3 = Player((4,4))
    Player4 = Player((4,1))
    
    def generateGameTree(player,chance):

        
g = Game()