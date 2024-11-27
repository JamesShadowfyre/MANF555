import factory.AbstractMachine

class WorkOrder:
    


    

    def execute(self): 
        self.machineList = []
        machine: factory.AbstractMachine.AbstractMachine
        task = 1
        quantity = 5
        for machine in self.machineList:
            machine.execute(task, quantity)

    def loadWorkOrderFromDatabase():
        readfromDB = True