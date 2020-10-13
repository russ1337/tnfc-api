from flask import Flask
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_restful import Api
from resources.errors import errors
from database.db import initialize_db

from flask_mail import Mail


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config.from_envvar('ENV_FILE_LOCATION')
mail= Mail(app)

from resources.routes import initialize_routes

api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)


app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb+srv://admin:supersi1a@cluster0-quirc.mongodb.net/TNFC?retryWrites=true&w=majority'
}

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'russ1337mock@gmail.com'
app.config['MAIL_PASSWORD'] = 'supersi1a'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

initialize_db(app)
initialize_routes(api)

app.run(host="0.0.0.0", port=3500)
