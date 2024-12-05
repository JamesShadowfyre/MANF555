from backend.externalCommunication.database import Database
class User:
    currentUser: str
    userid: int
    admin: bool

    def verify(username, password):
        db = Database()
        returnedUser = db.select(table='USER', fields=r'id, username, password, admin', conditions=('username = \'' + username + '\''))
        try:
            loggingUser = returnedUser.fetchone()
            if (loggingUser[2] == password):
                User.admin = loggingUser[3]
                User.userid = loggingUser[0]
                User.currentUser = username
                return True
        except Exception as e:
            print(e)
            return False
        return False

    def getUser(): #called by other classes to return the username ]
        return User.currentUser
    def getId():
        return User.userid
    
    #Jon's additions start, please modify if they cause issue   
    def getAdmin(): 
        return User.admin
    #Jon's additions end

