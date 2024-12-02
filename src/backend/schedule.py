from datetime import datetime

class Schedule():
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Schedule, cls).__new__(cls)
            return cls.instance
        return Schedule
        
    def __init__(self) -> None:
        self.schedule = []
        self.operators = []
        self.workOrders = []
        self.completeWorkOrders = []

    def getSchedule(self):
        return self.schedule
    
    def getOperatorCount(self, time):
        operatorCount = 0 
        for operator in self.operators:
            if time in [operator.getStartTime(),operator.getStartTime() + operator.dayLength()]:
                operatorCount = operatorCount + 1
        return operatorCount

    #DEFINE CURRENT TIME, UPDATAE the - 1 on recursive algorithm
    def schedule_WorkOrder(self, workOrder, dueDate):
        #update dates to be Time Objects
        if(dueDate - workOrder.getDuration() < datetime.now().strftime('%H:%M:%S')): 
            return False
        for x in range(dueDate - workOrder.getDuaration(), dueDate):
            if self.getOpperatorCount() == 0:
                break
            if x == dueDate:
                #Remember to remove operator for this set time
                self.schedule.append(workOrder)
                return True
        return self.schedule_WorkOrder(self, workOrder, dueDate - 1) #1 should be minute based on our average time scale
    
    #Bits for async call of scheduled action
        #import sched, time

        # def action():
        #     Task to call on 

        # # Set up scheduler
        # s = sched.scheduler(time.localtime, time.sleep)
        # # Schedule when you want the action to occur
        # s.enterabs(time.strptime('Tue May 01 11:05:17 2018'), 0, action)
        # # Block until the action has been run
        # s.run()