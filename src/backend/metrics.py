class metrics:
    
    def calculateOEE(totalitems, totalWorkTime, totalExpectedDuration):
        availability = 1
        performance = totalExpectedDuration*totalitems / totalWorkTime
        quality=1
        return availability*performance*quality
        #Go through list of workorders to gather all stats