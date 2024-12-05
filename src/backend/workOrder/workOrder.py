import backend.factory.AbstractMachine
import backend.inventory.item
from backend.externalCommunication.database import Database
from backend.loginSystem.User import User

class WorkOrder:
    db: Database 
    def __init__(self, id, machineList, componentMap, quantity, customer, operator):
        self.id = id
        self.machineList = machineList
        self.componentMap = componentMap
        self.quantity = quantity
        self.customer = customer 
        self.duration = WorkOrder.setDuration(componentMap, quantity)
        WorkOrder.db = Database()
        self.operator = operator
        self.stats = []
        self.save()

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
    
    def setDuration(componentMap, quantity):
        return 0
        #This needs to cycle through all components and sum expected durations

    def save(self):
        clientid = '1'#WorkOrder.db.select(table='customer', fields=r'id', conditions=('accountName = \'' + self.customer + '\'')).fetchone()[0]
        userid = str(User.getId())
        WorkOrder.db.insert(table='workOrder', columns='clientid, createdby, operatorid, duration, quantity', 
                            values=(str('\'' + clientid + '\',' + 
                                        '\'' + userid + '\',' + 
                                        '\'' + str(self.operator) + '\',' + 
                                        '\'' + str(self.duration) + '\',' + 
                                        '\'' +  str(self.quantity) +'\''
                                        )))
