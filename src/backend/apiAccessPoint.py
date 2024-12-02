import workOrder.workOrder as workOrder

class ApplicationHome():
    def init_app(self):
        #Inventory Manager Initializaiton
        #WorkOrder List initialization 
        #Calendar Initialization 
        #database initialization
        #initialize global user 
        a = 0
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
    
    def workOrderFunctions(self, functionType, **kwargs):
        if functionType == 'create':
            self.workOrderList.append(workOrder.WorkOrder(id=(self.workOrderID + 1), 
                                                machineList=['Drilling'], 
                                                componentMap={kwargs['case']: kwargs['newTaskCode']},
                                                quantity=kwargs['quantity'],
                                                customer=kwargs['customer'],
                                                operator=None
                                                ))
            self.workOrderID = self.workOrderList.__len__()
        elif functionType == 'getList':
            return self.getWorkOrderList()
                
    #
    def userFunctions():
        a = 0
        return True
