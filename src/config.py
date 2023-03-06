import os

#DO NOT INCLUDE. In theory this line alone could work for basic config
#app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.environ.get("DATABASE_URL")


class Config(object):
    #To avoid getting terminal warnings
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #access to .env and get the value of  SECRET_KEY, the variable name can be any but needs to match
    #JWT_SECRET_KEY = os.environ.get("SECRET_KEY")

    @property #creates a getter and setter property
    def SQLALCHEMY_DATABASE_URI(self):
        #access to .env and get the value of DATABASE_URL, the ariable name can be any but needs to match
        db_url = os.environ.get("DATABASE_URL")

        if not db_url:
            #so the user can know what the issue is
            raise ValueError("DATABASE_URL is not set")
        
        return db_url


class DevelopmentConfig(Config):
    DEBUT = True


class ProductionConfig(Config):
    pass


class TestingConfig(Config):
    TESTING = True


app_environment = os.environ.get("FLASK_DEBUG")
#app_environment = os.environ.get("FLASK_ENV")


if app_environment == "production":
    app_config = ProductionConfig()
elif app_environment == "testing":
    app_config = TestingConfig()
else:
    app_config = DevelopmentConfig()

