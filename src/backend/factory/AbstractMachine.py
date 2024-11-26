from abc import ABC

class AbstractMachine(ABC):
    def __init__(self):
        super().__init__()
        self.nodeMap = {}
        self.address = 0
    
    def setNodeMap(self, nodeMap):
        self.nodeMap = nodeMap
    
    def getNodeMap(self):
        return self.nodeMap
    
    def setAddress(self, address):
        self.address = address

    def getAddress(self):
        return self.address
    
    def execute(self, task, quantity):
        pass