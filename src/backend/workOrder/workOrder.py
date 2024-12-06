import backend.factory.AbstractMachine
import backend.inventory.item
from backend.externalCommunication.database import Database
from backend.loginSystem.User import User

class WorkOrder:
    db: Database
    db = Database()

    def __init__(self, id, machineList, componentMap, quantity, customer, operator):
        self.id = id
        self.machineList = machineList
        self.componentMap = componentMap
        self.quantity = quantity
        self.customer = customer 
        self.duration = WorkOrder.setDuration(componentMap, quantity)
        self.operator = operator
        self.completed = False
        self.stats = []

    def execute(self): 
        machine: backend.factory.AbstractMachine.AbstractMachine
        item: backend.inventory.item.item
        for machine in self.machineList:
            for item in self.componentMap:
                if item.getMachine() == machine.nameString():
                    self.stats.append(machine.execute(item.getTaskCode(), self.componentMap[self.quantity]))
        self.completed = True

    def getDuration(self):
        return self.duration

    def getStats(self):
        sum = 0
        for x in self.stats:
            sum += float(x)
        return sum
    
    def getCompleted(self):
        return self.completed
    def getQuantity(self):
        return self.quantity
    def getCustomer(self):
        return self.customer
    def getComponent(self):
        return self.componentMap
    
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
    
    def loadMap():
        workOrderMap = {}
        workOrders = WorkOrder.db.select(table='workOrder', fields=r'*', conditions='1 = 1')
        workOrders = workOrders.fetchall()
        print(workOrders)
        for x in range(workOrders.__len__()):
            workOrderMap[workOrders[x][0]] = WorkOrder(workOrders[x][0], ['Drilling'], {}, workOrders[x][5], '', '')
        return workOrderMap