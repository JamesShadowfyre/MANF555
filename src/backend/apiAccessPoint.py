from backend.workOrder.workOrder import WorkOrder
from backend.loginSystem.User import User
from backend.externalCommunication.database import Database

class ApplicationHome:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ApplicationHome, cls).__new__(cls)
            return cls.instance
        return cls.instance
    def init_app(self):
        #Inventory Manager Initializaiton
        #WorkOrder List initialization 
        #Calendar Initialization 
        #database initialization
        #initialize global user 
        self.database = Database()
        self.database.connect()
        self.workOrderList = []
        self.workOrderID = self.workOrderList.__len__()

    def calculateMetrics(metricType):
        #takes in type of metric as an argument, processes
        a = 0
        #returns required functional value

    def calendarFunction(functionType, **kwargs):
        a = 0 
        #returns necessary object 

    def inventoryFunction(functionType, **kwargs):
        a = 0
        #returns necessary object 

    def getWorkOrderList(self):
        return self.workOrderList
    
    def setWorkOrderFunctions(self, functionType, **kwargs):
        if functionType == 'create':
            self.workOrderList.append(WorkOrder(id=(self.workOrderID + 1), 
                                                machineList=['Drilling'], 
                                                componentMap={kwargs['case']: kwargs['taskCode']},
                                                quantity=kwargs['quantity'],
                                                customer=kwargs['customer'],
                                                operator=None
                                                ))
            self.workOrderID = self.workOrderList.__len__()
            return True
        elif functionType == 'getList':
            return self.getWorkOrderList()
                
    #
    def userFunctions(self, functionType, **kwargs):
        if functionType == 'login':
            return User.verify(username=kwargs['username'], password=kwargs['password'])
        