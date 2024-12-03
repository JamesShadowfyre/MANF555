from backend.externalCommunication.database import Database
class User:
    currentUser: str

    def verify(username, password):
        db = Database()
        returnedUser = db.select(table='USER', fields=r'username, password', conditions=('username = \'' + username + '\''))
        if (returnedUser.fetchone()[1] == password):
            
            User.currentUser = username
            print(User.getUser())
            return True
        return False

    def getUser(): #called by other classes to return the username ]
        return User.currentUser


