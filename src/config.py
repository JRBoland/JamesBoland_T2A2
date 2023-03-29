import os

class Config(object):
    # To avoid getting terminal warnings
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get("SECRET_KEY")

    # Creates a getter and setter property
    @property 
    def SQLALCHEMY_DATABASE_URI(self):
        #access to .env and get the value of DATABASE_URL, 
        # the variable name can be any but needs to match
        db_url = os.environ.get("DATABASE_URL")

        if not db_url:
            # Inform the user of error
            raise ValueError("DATABASE_URL is not set")
        
        return db_url


# Setting config
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

