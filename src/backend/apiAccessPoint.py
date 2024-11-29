import workOrder

class ApplicationHome():
    def init_app():
        #Inventory Manager Initializaiton
        #WorkOrder List initialization 
        #Calendar Initialization 
        #database initialization
        #initialize global user 
        a = 0

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
        self.workOrderList = []
        return self.workOrderList
    
    def workOrderFunctions(self, functionType, **kwargs):
        if functionType == "Create":
            self.workOrderList.append(workOrder(kwargs['id'], kwargs['machineList'], kwargs['componentList']))
                
    #
    def userFunctions():
        a = 0
        return True
