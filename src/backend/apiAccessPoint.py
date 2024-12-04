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
        self.workOrderMap = {}
        self.workOrderID = self.workOrderMap.keys().__len__()

    def calculateMetrics(metricType):
        if metricType == 'OEE':
            a = 0
        elif metricType == 'KPI':
            a = 0
        elif metricType == 'FPFY':
            a = 0
        elif metricType == 'TSP':
            a = 0

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
        return self.workOrderList
    
    def setWorkOrderFunctions(self, functionType, **kwargs):
        if functionType == 'create':
            self.workOrderMap[self.workOrderID + 1] = (WorkOrder(id=(self.workOrderID + 1), 
                                                machineList=['Drilling'], 
                                                componentMap={kwargs['case']: kwargs['taskCode']},
                                                quantity=kwargs['quantity'],
                                                customer=kwargs['customer'],
                                                operator=None
                                                ))
            self.workOrderID = self.workOrderMap.keys().__len__()
            return True
        elif functionType == 'getList':
            return self.getWorkOrderList()
        elif functionType == 'getDateRange':
            return self.getWorkOrderList()
        elif functionType == 'edit':
            a = 0
        elif functionType == 'delete':
            a = 0
        elif functionType == 'getCompleted':
            a = 0

    #
    def userFunctions(self, functionType, **kwargs):
        if functionType == 'login':
            return User.verify(username=kwargs['username'], password=kwargs['password'])
        elif functionType == 'get':
            return User.getUser()
    
    def customerFunctions(self, functionType, **kwargs):
        if functionType == 'create':
            a = 0
        elif functionType == 'edit':
            a = 0
        elif functionType == 'remove':
            a = 0
        elif functionType == 'get':
            a = 0