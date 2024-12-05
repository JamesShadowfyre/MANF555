from backend.externalCommunication.database import Database
class User:
    currentUser: str
    admin: bool

    def verify(username, password):
        db = Database()
        returnedUser = db.select(table='USER', fields=r'username, password, admin', conditions=('username = \'' + username + '\''))
        try:
            loggingUser = returnedUser.fetchone()
            if (loggingUser[1] == password):
                User.admin = loggingUser[2]
                User.currentUser = username
                return True
        except Exception as e:
            print(e)
            return False
        return False

    def getUser(): #called by other classes to return the username ]
        return User.currentUser


