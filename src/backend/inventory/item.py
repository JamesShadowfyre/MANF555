import factory.AbstractMachine
import factory.DrillingMachine
class item:
    def __init__(self, name, colour, taskCode, machine):
        self.name = name
        self.colour = colour
        self.taskCode = taskCode
        self.machine: factory.AbstractMachine.AbstractMachine = self.setMachine(machine)

    def getName(self):
        return self.name
    
    def getTaskCode(self):
        return self.taskCode
    
    def getMachine(self):
        return self.machine.nameString()

    def setName(self, name):
        self.name = name   

    def setMachine(machine):
        if machine == "Drilling":
            return factory.DrillingMachine.DrillingMachine()
