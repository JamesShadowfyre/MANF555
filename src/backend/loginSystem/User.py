from backend.externalCommunication.database import Database
class User:

    def verify(username, password):
        db = Database()
        returnedUser = db.select(table='USER', fields=r'username, password', conditions=('username = \'' + username + '\''))
        if (returnedUser.fetchone()[1] == password):
            return True
        return False

    def getUser (): #called by other classes to return the username 
        return username

    def getUserId ():
        return userId

    def createWorkOrder():
        pass

    def createProductionSchedule():
        pass
    
    def updateInventory():
        pass

