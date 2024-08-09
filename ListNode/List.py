from .Node import Node

class List():
    def __init__(self):
        self.first = None
        
    def isEmpty(self):
        return self.first == None
        
    def addFirst(self, data):
        self.first = Node(data)
            
    def deleteNode(self):
        if self.isEmpty() == False:
            self.first = self.first.getLink()   
            return True
        return False
    
    def count(self):
        i = 0
        aux = self.first
        while aux != None:
            i = i + 1
            aux = aux.getLink()
        return i
                    
    def getData(self):
        return self.first.getData()