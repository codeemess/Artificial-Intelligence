from queue import Queue
import json

class GenerateGameTree(object):
    ROOT = {"State": {1:(1,1), 2:(4,1), 3:(4,4), 4:(1,4)}, "Parent": "None", "Level": 0, "Action": "None", "CurrentPlayer": 0, 
    "Repeated": False, "Terminating": False, "Winner": "None", "WinStates" : {1:(4,4), 2:(1,4), 3:(1,1), 4:(4,1)}, "Utility": {}}
    GameTree = {}
    ExploredStates = ()

    def moveLeft(self,node,parent):
        if node["Terminating"] == True or node["Repeated"] == True:
            return "Invalid"
        else:
            newNode = {}
            newNode["Parent"] = node["State"]
            newNode["ParentNode"] = parent
            player = node["CurrentPlayer"] + 1
            if player == 5:
                player = 1
            move = node["State"][player]
            newMove = "None"
            newNode["State"] = {}
            if (move[0]-1) > 0:
                newMove = (move[0]-1, move[1])
                newNode["State"][player] = newMove
            for p in node["State"].keys():
                if player != p:
                    if(newMove == node["State"][p]):
                        newMove = "None"
            for p in node["State"].keys():
                if player != p:
                    newNode["State"][p] = node["State"][p]
            if newMove != "None":
                newNode["CurrentPlayer"] = player
                newNode["Action"] = "left"
                newNode["Level"] = node["Level"] + 1
                newNode["Repeated"] = False
                newNode["Winner"] = "None"
                newNode["WinStates"] = node["WinStates"]
                newNode["Terminating"] = False
                newNode["Utility"] = {}
                return newNode
            else:
                return "Invalid"
    
    def moveRight(self,node,parent):
        if node["Terminating"] == True or node["Repeated"] == True:
            return "Invalid"
        else:
            newNode = {}
            newNode["Parent"] = node["State"]
            newNode["ParentNode"] = parent
            player = node["CurrentPlayer"] + 1
            if player == 5:
                player = 1
            move = node["State"][player]
            newMove = "None"
            newNode["State"] = {}
            if (move[0]+1) < 5:
                newMove = (move[0]+1, move[1])
                newNode["State"][player] = newMove
            for p in node["State"].keys():
                if player != p:
                    if(newMove == node["State"][p]):
                        newMove = "None"
            for p in node["State"].keys():
                if player != p:
                    newNode["State"][p] = node["State"][p]
            if newMove != "None":
                newNode["CurrentPlayer"] = player
                newNode["Action"] = "right"
                newNode["Level"] = node["Level"] + 1
                newNode["Repeated"] = False
                newNode["Winner"] = "None"
                newNode["WinStates"] = node["WinStates"]
                newNode["Terminating"] = False
                newNode["Utility"] = {}
                return newNode
            else:
                return "Invalid"
    
    def moveDown(self,node,parent):
        if node["Terminating"] == True or node["Repeated"] == True:
            return "Invalid"
        else:
            newNode = {}
            newNode["Parent"] = node["State"]
            newNode["ParentNode"] = parent
            player = node["CurrentPlayer"] + 1
            if player == 5:
                player = 1
            move = node["State"][player]
            newMove = "None"
            newNode["State"] = {}
            if (move[1]+1) < 5:
                newMove = (move[0], move[1]+1)
                newNode["State"][player] = newMove
            for p in node["State"].keys():
                if player != p:
                    if(newMove == node["State"][p]):
                        newMove = "None"
            for p in node["State"].keys():
                if player != p:
                    newNode["State"][p] = node["State"][p]
            if newMove != "None":
                newNode["CurrentPlayer"] = player
                newNode["Action"] = "down"
                newNode["Level"] = node["Level"] + 1
                newNode["Repeated"] = False
                newNode["Winner"] = "None"
                newNode["WinStates"] = node["WinStates"]
                newNode["Terminating"] = False
                newNode["Utility"] = {}
                return newNode
            else:
                return "Invalid"
    
    def moveUp(self,node,parent):
        if node["Terminating"] == True or node["Repeated"] == True:
            return "Invalid"
        else:
            newNode = {}
            newNode["Parent"] = node["State"]
            newNode["ParentNode"] = parent
            player = node["CurrentPlayer"] + 1
            if player == 5:
                player = 1
            move = node["State"][player]
            newMove = "None"
            newNode["State"] = {}
            if (move[1]-1) > 0:
                newMove = (move[0], move[1]-1)
                newNode["State"][player] = newMove
            for p in node["State"].keys():
                if player != p:
                    if(newMove == node["State"][p]):
                        newMove = "None"
            for p in node["State"].keys():
                if player != p:
                    newNode["State"][p] = node["State"][p]
            if newMove != "None":
                newNode["CurrentPlayer"] = player
                newNode["Action"] = "up"
                newNode["Level"] = node["Level"] + 1
                newNode["Repeated"] = False
                newNode["Winner"] = "None"
                newNode["WinStates"] = node["WinStates"]
                newNode["Terminating"] = False
                newNode["Utility"] = {}
                return newNode
            else:
                return "Invalid"

    def checkTerminalState(self,node):
        for k in node["State"].keys():
            if (node["State"][k] == node["WinStates"][k]) :
                node["Winner"] = k
                node["Terminating"] = True
                # print(k)
        return node
    
    def checkAndUpdateRepeatedState(self,node):
        StateTuple = tuple([(k, v) for k, v in node["State"].items()])
        if StateTuple in self.ExploredStates:
            node["Repeated"] = True
        else:
            temp = list(self.ExploredStates)
            temp.append(StateTuple)
            self.ExploredStates = tuple(temp)
            self.ExploredStates = set(self.ExploredStates)
        return node

    def generateGameTree(self,node):
        q = Queue(maxsize=0)
        
        q.put(node)
        count = 0
        while( q.empty() == False):
            current = q.get()
            
            current = self.checkTerminalState(current)
            current = self.checkAndUpdateRepeatedState(current)
            print(current)
            self.GameTree[count] = current
            if(current["Repeated"] == False and current["Terminating"] == False):
                Left = self.moveLeft(current,count)
                Right = self.moveRight(current,count)
                Up = self.moveUp(current,count)
                Down = self.moveDown(current,count)
                
                if(Left != "Invalid"):
                    #print(Left)
                    # print(Left)
                    q.put(Left)
                    
                if(Right != "Invalid"):
                    #print(Right)
                    q.put(Right)
                if(Up != "Invalid"):
                    #print(Up)
                    q.put(Up)
                if(Down != "Invalid"):
                    #print(Down)
                    q.put(Down)
                count += 1
            else:
                continue
    
    # def saveToFile(self):
    #     with open('result.json', 'w') as fp:
    #         json.dump(self.GameTree,fp)


g = GenerateGameTree()
g.generateGameTree(g.ROOT)
# g.saveToFile()
