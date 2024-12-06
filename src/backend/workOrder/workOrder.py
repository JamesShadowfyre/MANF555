import backend.factory.AbstractMachine
import backend.inventory.item
from backend.externalCommunication.database import Database
from backend.loginSystem.User import User
import datetime

class WorkOrder:
    db: Database
    db = Database()

    def __init__(self, id, machineList, componentMap, quantity, customer, operator, taskcode, startDate):
        self.id = id
        self.machineList = machineList
        self.componentMap = componentMap
        self.quantity = quantity
        self.customer = customer 
        self.duration = WorkOrder.setDuration(componentMap, quantity)
        self.taskCode = taskcode
        self.operator = operator
        self.completed = False
        self.startDate = startDate
        self.stats = []

    def execute(self): 
        machine: backend.factory.AbstractMachine.AbstractMachine
        item: backend.inventory.item.item
        for machine in self.machineList:
            for item in self.componentMap:
                if item.getMachine() == machine.nameString():
                    self.stats.append(machine.execute(self.taskCode, self.componentMap[self.quantity]))
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
    def getTaskCode(self):
        return self.taskCode
    
    def setDuration(componentMap, quantity):
        return quantity*0.5 # 30s cycle time on drill station
        #This needs to cycle through all components and sum expected durations

    def save(self):
        clientid = '1'#WorkOrder.db.select(table='customer', fields=r'id', conditions=('accountName = \'' + self.customer + '\'')).fetchone()[0]
        userid = str(User.getId())
        print(self.taskCode)
        WorkOrder.db.insert(table='workOrder', columns='clientid, createdby, operatorid, duration, quantity, taskcode, startDate', 
                            values=(str('\'' + clientid + '\',' + 
                                        '\'' + userid + '\',' + 
                                        '\'' + str(self.operator) + '\',' + 
                                        '\'' + str(self.duration) + '\',' + 
                                        '\'' +  str(self.quantity) +'\',' + 
                                        '\'' +  str(self.taskCode) +'\',' + 
                                        '\'' +  str(self.startDate) +'\''
                                        )))
    
    def loadMap():
        workOrderMap = {}
        workOrders = WorkOrder.db.select(table='workOrder', fields=r'*', conditions='1 = 1')
        workOrders = workOrders.fetchall()
        print(workOrders)
        for x in range(workOrders.__len__()):
            workOrderMap[workOrders[x][0]] = WorkOrder(workOrders[x][0], ['Drilling'], {'B': workOrders[x][6]}, workOrders[x][5], '', '', taskcode=workOrders[x][6], startDate=workOrders[x][7])
        return workOrderMap
    
    def loadmain():
        workOrders = WorkOrder.db.select(table='workOrder', fields=r'id, startDate, startTime, duration, quantity', conditions=str('startDate =\'' + str(datetime.date.today())+'\''))
        workOrders = workOrders.fetchall()
        return workOrders
    def loadOverviewTable():
        workOrders = WorkOrder.db.select(table='workOrder', fields=r'id, startDate, startTime, clientid, taskcode', conditions='1 = 1')
        workOrders = workOrders.fetchall()
        return workOrders