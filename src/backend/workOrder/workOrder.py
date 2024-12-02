import factory.AbstractMachine
import inventory.item

class WorkOrder:

    def __init__(self, id, machineList, componentMap, quantity):
        self.id = id
        self.machineList = machineList
        self.componentMap = componentMap
        self.quantity = quantity
        #SOMETHING TO SQL HERE
        self.stats = []

    def execute(self): 
        machine: factory.AbstractMachine.AbstractMachine
        item: inventory.item.item
        for machine in self.machineList:
            for item in self.componentMap:
                if item.getMachine() == machine.nameString():
                    self.stats.append(machine.execute(item.getTaskCode(), self.componentMap[self.quantity]))



    def loadWorkOrderFromDatabase():
        readfromDB = True

    def getStats(self):
        return self.stats

if __name__ == "__main__":
    myWorkOrder = WorkOrder(1)
    myWorkOrder.execute()