from flask import Flask
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = '530dab7079cef3a285e72baf73af099a'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465'
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''

mail = Mail(app)
csrf = CSRFProtect(app) # Used to protect the form with a CSRF token. Step 3 of lab, instruction 3.
from app import views