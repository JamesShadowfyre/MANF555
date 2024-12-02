import backend.factory.AbstractMachine
import backend.inventory.item

class WorkOrder:

    def __init__(self, id, machineList, componentMap, quantity, customer, operator):
        self.id = id
        self.machineList = machineList
        self.componentMap = componentMap
        self.quantity = quantity
        self.customer = WorkOrder.createCustomer(customer) #customer as JSON style object
        self.duration = WorkOrder.setDuration(componentMap, quantity)
        self.db = 'db'
        self.operator = operator
        #SOMETHING TO SQL HERE
        self.stats = []

    def execute(self): 
        machine: backend.factory.AbstractMachine.AbstractMachine
        item: backend.inventory.item.item
        for machine in self.machineList:
            for item in self.componentMap:
                if item.getMachine() == machine.nameString():
                    self.stats.append(machine.execute(item.getTaskCode(), self.componentMap[self.quantity]))

    def getDuration(self):
        return self.duration

    def loadWorkOrderFromDatabase():
        readfromDB = True

    def getStats(self):
        return self.stats
    
    #database function, customer as JSON style object
    def createCustomer(customer):
        db = 'db'
        db.createTable(customer)

    def setDuration(componentMap, quantity):
        return 0
        #This needs to cycle through all components and sum expected durations

if __name__ == "__main__":
    myWorkOrder = WorkOrder(1)
    myWorkOrder.execute()