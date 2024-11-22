class Schedule():
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Schedule, cls).__new__(cls)
            return cls.instance
        return Schedule
    def __init__(self) -> None:
        self.schedule = []
        self.operators = []

    def getSchedule(self):
        return self.schedule
    
    def getOperatorCount(self, time):
        operatorCount = 0 
        for operator in self.operators:
            if time in [operator.getStartTime(),operator.getStartTime() + operator.dayLength()]:
                operatorCount = operatorCount + 1
        return operatorCount

    
    def schedule_WorkOrder(self, workOrder, dueDate):
        if(dueDate - workOrder.getDuration() < currentTime): 
            return False
        for x in range(dueDate - workOrder.getDuaration(), dueDate):
            if self.getOpperatorCount() == 0:
                break
            if x == dueDate:
                self.schedule.append(workOrder)
                return True
        return self.getSchedule(self, workOrder, dueDate - 1)