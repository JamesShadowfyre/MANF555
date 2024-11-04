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
        DATABASE=os.path.join(app.instance_path, 'src.sqlite'),
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #db.init_app(app)
    app.app_context().push()
        
    return app