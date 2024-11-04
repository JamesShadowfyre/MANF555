import os
from flask import Flask
from flask_login import LoginManager

#FLASK uses a factory design pattern
#This method creates the app
def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    login = LoginManager(app)
    

    app.config.from_mapping(
        SECRET_KEY='test_change_later',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #db.init_app(app)
    app.app_context().push()
    
    
    # #part of app, this guides the login and user. 
    # @login.user_loader
    # def load_user(id):
    #     try:
    #         if db.get_db().execute("SELECT id from PremiumUser where userid = (?)", (id,)).fetchone()['id'] > 0:
    #             return SuperUser(userid=id)
    #     except Exception as a:
    #         print(a)
    #         return User(userid=id)
        
    return app