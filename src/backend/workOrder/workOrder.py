import factory.AbstractMachine

class WorkOrder:
    
    def __init__(self, id, machineList, componentMap):
        self.id = id
        self.machineList = machineList
        self.componentMap = componentMap
        #SOMETHING TO SQL HERE

    def execute(self): 
        machine: factory.AbstractMachine.AbstractMachine
        task = 1
        quantity = 5
        for machine in self.machineList:
            for item in self.componentMap:
                if item.machine == machine:
                    machine.execute(item.taskCode, self.componentMap[quantity])



    def loadWorkOrderFromDatabase():
        readfromDB = True

if __name__ == "__main__":
    myWorkOrder = WorkOrder(1)
    myWorkOrder.execute()