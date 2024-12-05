from backend.workOrder.workOrder import WorkOrder
from backend.loginSystem.User import User
from backend.externalCommunication.database import Database
import datetime
import atexit

class ApplicationHome:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ApplicationHome, cls).__new__(cls)
            return cls.instance
        return cls.instance
    def init_app(self):
        self.database = Database()
        self.database.connect()
        self.workOrderMap = WorkOrder.loadMap()
        self.workOrderID = self.workOrderMap.keys().__len__()
        self.startTime = datetime.datetime.now()

    def calculateMetrics(self, metricType):
        totalWorkTime = 0
        totalitems = 0
        x: WorkOrder
        for x in self.workOrderMap.values():
            totalWorkTime += float(x.getStats())
            if x.getCompleted() == True:
                totalitems += x.getQuantity()

        if metricType == 'OEE':
            a = 0
        elif metricType == 'FPFY':
            a = 0
        elif metricType == 'TSP':
            a = 0
        elif metricType == 'Idle':
            return float(float(datetime.datetime.now() - self.startTime - totalWorkTime) / float(datetime.datetime.now() - self.startTime))
        elif metricType == 'ScheduledDown':
            return 0
        elif metricType == 'Unexpected':
            return 0
        elif metricType == 'totalComplete':
            return totalitems

        
            
    def calendarFunction(functionType, **kwargs):
        a = 0 
        #returns necessary object 

    def inventoryFunction(functionType, **kwargs):
        if functionType == 'create':
            a = 0
        elif functionType == 'edit':
            a = 0
        elif functionType == 'remove':
            a = 0
        elif functionType == 'get':
            a = 0

    def getWorkOrderList(self):
        return self.workOrderMap
    
    def setWorkOrderFunctions(self, functionType, **kwargs):
        if functionType == 'create':
            self.workOrderMap[self.workOrderID + 1] = (WorkOrder(id=(self.workOrderID + 1), 
                                                machineList=['Drilling'], 
                                                componentMap={kwargs['case']: kwargs['taskCode']},
                                                quantity=kwargs['quantity'],
                                                customer=kwargs['customer'],
                                                operator=None
                                                ))
            self.workOrderMap.get(self.workOrderID + 1).save()
            self.workOrderID = self.workOrderMap.keys().__len__()
            return True
        elif functionType == 'getList':
            return self.getWorkOrderList()
        elif functionType == 'get':
            return self.workOrderMap.get(kwargs['id'])
        elif functionType == 'edit':
            self.database.delete(table='workOrder', conditions='id = ' + kwargs['id'])
            self.getWorkOrderList[kwargs['id']] = (WorkOrder(id=kwargs['id'], 
                                                machineList=['Drilling'], 
                                                componentMap={kwargs['case']: kwargs['taskCode']},
                                                quantity=kwargs['quantity'],
                                                customer=kwargs['customer'],
                                                operator=None
                                                ))
            self.workOrderMap.get(kwargs['id']).save()
        elif functionType == 'delete':
            self.database.delete(table='workOrder', conditions='id = ' + kwargs['id'])
        elif functionType == 'getCompleted':
            completedList = []
            for workOrder in self.workOrderMap.values():
                if workOrder.getCompleted() == True:
                    completedList.append(workOrder)
    def userFunctions(self, functionType, **kwargs):
        if functionType == 'login':
            return User.verify(username=kwargs['username'], password=kwargs['password'])
        elif functionType == 'get':
            return User.getUser()
    
    def customerFunctions(self, functionType, **kwargs):
        if functionType == 'create':
            # self.database.insert(table='customer', columns='clientid, createdby, operatorid, duration, quantity', 
            #                 values=(str('\'' + clientid + '\',' + 
            #                             '\'' + userid + '\',' + 
            #                             '\'' + str(self.operator) + '\',' + 
            #                             '\'' + str(self.duration) + '\',' + 
            #                             '\'' +  str(self.quantity) +'\''
            #                             )))
            a = 0
        elif functionType == 'edit':
            self.database.delete(table='customer', conditions='accountName = ' + kwargs['accountName'])
            # self.database.insert(table='customer', columns='clientid, createdby, operatorid, duration, quantity', 
            #                 values=(str('\'' + clientid + '\',' + 
            #                             '\'' + userid + '\',' + 
            #                             '\'' + str(self.operator) + '\',' + 
            #                             '\'' + str(self.duration) + '\',' + 
            #                             '\'' +  str(self.quantity) +'\''
            #                             )))
        elif functionType == 'remove':
            self.database.delete(table='customer', conditions='accountName = ' + kwargs['accountName'])
        elif functionType == 'get':
            customers = self.database.select(table='customer', fields=r'*', conditions=('accountName = \'' + kwargs['accountName'] + '\''))
            return customers.fetchall()

