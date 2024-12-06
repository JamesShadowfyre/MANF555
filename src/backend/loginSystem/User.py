from backend.externalCommunication.database import Database
class User:
    currentUser: str
    userid: int
    admin: bool
    db: Database

    def verify(username, password):
        User.db = Database()
        returnedUser = User.db.select(table='USER', fields=r'id, username, password, admin', conditions=('username = \'' + username + '\''))
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

    def loadAll():
        users = User.db.select(table='user', fields=r'id, username, admin', conditions='1 = 1')
        users = users.fetchall()
        print(str(users))
        return users
    
    def createUser(username, password, admin):
        User.db.insert(table='user', columns='username, password, admin',values=str(
            '\'' + username + '\',' + 
            '\'' + password + '\',' + 
            '\'' + str(admin) + '\''
        ))

    def delete(id):
        User.db.delete(table='user', conditions=str('id =' + id))
    def changePassword(id, password):
        User.db.update(table='user', arguments='password = \'' + password + '\'', conditions='id = ' + id)

