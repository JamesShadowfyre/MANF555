from abc import ABC

class AbstractMachine(ABC):
    
    def setNodeMap(self):
        self.tag = 0
    
    def getNodeMap(self):
        return self.tag
    
    def setAddress(self):
        self.address = 0

    def getAddress(self):
        return self.address
    
    def execute():
        pass