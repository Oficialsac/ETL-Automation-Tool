class Node():
    def __init__(self, data):
        self.data = data
        self.link = None
        
    def getData(self):
        return self.data
    
    def setData(self, data):
        self.data = data
        
    def getLink(self):
        return self.link
    
    def setLink(self, link):
        self.link = link