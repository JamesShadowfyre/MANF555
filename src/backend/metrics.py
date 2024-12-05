class metrics:
    
    def calculateOEE(totalitems, totalWorkTime, totalExpectedDuration):
        availability = 1
        try:
            performance = totalExpectedDuration*totalitems / totalWorkTime
        except:
            performance = 0
        quality=1
        return availability*performance*quality
        #Go through list of workorders to gather all stats