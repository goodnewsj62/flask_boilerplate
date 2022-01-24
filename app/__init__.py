from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_mail import Mail
from configuration import Config
from passlib.context import CryptContext



db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()
mail = Mail()

# dont forget to add def load_user(user_id) for flask login

pwd_context = CryptContext(
    schemes=["pbkdf2_sha256", "des_crypt"],
    default="pbkdf2_sha256",
    pbkdf2_sha256__default_rounds=30000
)

def create_app(config=Config()):
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_object(config)

    #init dependencies
    db.init_app(app)
    login_manager.init_app(app=app)
    migrate.init_app(app=app,db=db)
    mail.init_app(app=app)

    with app.app_context():
        #all your blueprint registration 
        pass
    return app
