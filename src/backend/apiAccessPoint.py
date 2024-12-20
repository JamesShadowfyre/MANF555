from backend.workOrder.workOrder import WorkOrder
from backend.loginSystem.User import User
from backend.externalCommunication.database import Database
from backend.metrics import metrics
import datetime


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
        totalExpectedDuration = 0
        totalCycles = 0
        x: WorkOrder
        for x in self.workOrderMap.values():
            totalWorkTime += float(x.getStats())/1000
            print(x.getStats())
            if x.getCompleted() == True:
                totalitems += x.getQuantity()
                totalCycles += 1
                totalExpectedDuration += x.getDuration()*60

        if metricType == 'OEE':
            return metrics.calculateOEE(totalCycles, totalWorkTime, totalExpectedDuration, float(float((datetime.datetime.now() - self.startTime).total_seconds() - totalWorkTime)))
        elif metricType == 'FPFY':
            return 1
        elif metricType == 'TSP':
            return totalitems
        elif metricType == 'Idle':
            return float(float((datetime.datetime.now() - self.startTime).total_seconds() / 60 - totalWorkTime)) # / float((datetime.datetime.now() - self.startTime).total_seconds() / 60)
        elif metricType == 'ScheduledDown':
            return 0
        elif metricType == 'Unexpected':
            return 0
        elif metricType == 'totalComplete':
            return totalitems

        
            
    def calendarFunction(functionType, **kwargs):
        a = 0 
        #returns necessary object 

    def inventoryFunction(self, functionType, **kwargs):
        if functionType == 'create':
            self.database.insert(table='item', columns='clientid, createdby, operatorid, duration, quantity', 
                            values=(str('\'' + kwargs['clientid'] + '\',' + 
                                        '\'' + kwargs['userid'] + '\'' 
                                        )))
        elif functionType == 'edit':
            self.database.delete(table='item', conditions='name = ' + kwargs['name'])
        elif functionType == 'remove':
            self.database.delete(table='item', conditions='accountName = ' + kwargs['accountName'])
        elif functionType == 'get':
            self.database.select()

    def getWorkOrderList(self):
        return self.workOrderMap
    
    def setWorkOrderFunctions(self, functionType, **kwargs):
        if functionType == 'create':
            self.workOrderMap[self.workOrderID + 1] = (WorkOrder(id=(self.workOrderID + 1), 
                                                machineList=['Drilling'], 
                                                componentMap={kwargs['case']: kwargs['taskCode']},
                                                quantity=kwargs['quantity'],
                                                customer=kwargs['customer'],
                                                operator=None,
                                                taskcode=kwargs['taskCode'],
                                                startDate=kwargs['date']
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
            self.getWorkOrderList[kwargs['id']] = (WorkOrder(id=(self.workOrderID + 1), 
                                                machineList=['Drilling'], 
                                                componentMap={kwargs['case']: kwargs['taskCode']},
                                                quantity=kwargs['quantity'],
                                                customer=kwargs['customer'],
                                                operator=None,
                                                taskcode=kwargs['taskCode'],
                                                startDate=kwargs['date']
                                                ))
            self.workOrderMap.get(kwargs['id']).save()
        elif functionType == 'delete':
            self.database.delete(table='workOrder', conditions='id = ' + kwargs['id'])
            self.workOrderMap.pop(int(kwargs['id']))
        elif functionType == 'getCompleted':
            completedList = []
            for workOrder in self.workOrderMap.values():
                if workOrder.getCompleted() == True:
                    completedList.append(workOrder)
            return completedList
        elif functionType=='completed':
            return WorkOrder.loadComplete()
        elif functionType =='loadmain':
            return WorkOrder.loadmain()
        elif functionType == 'loadOverview':
            return WorkOrder.loadOverviewTable()
        elif functionType=='execute':
            self.workOrderMap.get(kwargs['id']).execute()
    def userFunctions(self, functionType, **kwargs):
        if functionType == 'login':
            return User.verify(username=kwargs['username'], password=kwargs['password'])
        elif functionType == 'get':
            return User.getUser()
        elif functionType == 'loadall':
            return User.loadAll()
        elif functionType == 'create':
            User.createUser(kwargs['username'], kwargs['password'], kwargs['admin'])
        elif functionType == 'delete':
            User.delete(kwargs['id'])
        elif functionType=='passwordchange':
            User.changePassword(kwargs['id'], kwargs['password'])

    # Morgan's addition, please remove or modify if required
        
    def operatorFunctions(self, functionType, **kwargs):
        if functionType == 'loadall':
            operators = self.database.select(table='operator', fields=r'*', conditions=('1 = 1'))
            return operators.fetchall()
        elif functionType == 'create':
            self.database.insert(table='operator', columns='name', 
                            values=(str('\'' + kwargs['name'] + '\'' #+ 
                                        # '\'' + userid + '\',' + 
                                        # '\'' + str(self.operator) + '\',' + 
                                        # '\'' + str(self.duration) + '\',' + 
                                        # '\'' +  str(self.quantity) +'\''
                                        )))
        elif functionType == 'delete':
           self.database.delete(table='operator', conditions='name = ' + kwargs['name'])
        
    # Morgan's additions end

    #Jon's additions start, please modify if they cause issue   
    def userFunctions2(self):
            return User.getAdmin()
    #Jon's additions end
        
    
    
    def customerFunctions(self, functionType, **kwargs):
        if functionType == 'create':
            self.database.insert(table='customer', columns='accountName', 
                            values=(str('\'' + kwargs['accountName'] + '\'' #+ 
                                        # '\'' + userid + '\',' + 
                                        # '\'' + str(self.operator) + '\',' + 
                                        # '\'' + str(self.duration) + '\',' + 
                                        # '\'' +  str(self.quantity) +'\''
                                        )))
        elif functionType == 'edit':
            self.database.delete(table='customer', conditions='id = ' + '\'' + kwargs['id'] + '\'')
            self.database.insert(table='customer', columns='accountName', 
                            values=(str('\'' + kwargs['accountName'] + '\'' #+ 
                                        # '\'' + userid + '\',' + 
                                        # '\'' + str(self.operator) + '\',' + 
                                        # '\'' + str(self.duration) + '\',' + 
                                        # '\'' +  str(self.quantity) +'\''
                                        )))
        elif functionType == 'remove':
            self.database.delete(table='customer', conditions='id = ' + kwargs['id'])
        elif functionType == 'get':
            customers = self.database.select(table='customer', fields=r'*', conditions=('accountName = \'' + kwargs['accountName'] + '\''))
            return customers.fetchall()
        elif functionType == 'getall':
            customers = self.database.select(table='customer', fields=r'id, accountName', conditions=('1 = 1'))
            return customers.fetchall()


