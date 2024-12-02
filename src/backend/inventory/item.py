import factory.AbstractMachine
import factory.DrillingMachine
class item:
    def __init__(self, name, colour, taskCode, machine):
        self.name = name
        self.colour = colour
        self.taskCode = taskCode
        self.machine = machine

    def getName(self):
        return self.name
    
    def getTaskCode(self):
        return self.taskCode
    
    def getMachine(self):
        return self.machine

    def setName(self, name):
        self.name = name   

        
