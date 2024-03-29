"""
The flask application package.
"""
import secrets
from flask_bootstrap import Bootstrap5
from flask import Flask
from flask_wtf import CSRFProtect
app = Flask(__name__)

strSecretKey = secrets.token_urlsafe(16)
app.secret_key = strSecretKey
#app.secret_key = 'tO$&!|0wkamvVia0?n$NqIRVWOG'

# Bootstrap-Flask requires this line
bootstrap = Bootstrap5(app)
# Flask-WTF requires this line
csrf = CSRFProtect(app)


import PG_Management.views
