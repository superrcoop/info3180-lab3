from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'passphrase' 
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io' 
app.config['MAIL_PORT'] = '465' 
app.config['MAIL_USERNAME'] = '82b624680044e3' 
app.config['MAIL_PASSWORD'] = 'd34e5796da9010' 
 
mail = Mail(app) 

from app import views