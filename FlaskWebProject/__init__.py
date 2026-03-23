import logging
import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)
# 🔥 FORCE LOCAL DB (IMPORTANT FIX)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///local.db"

# ✅ SESSION FIX
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = '/tmp/flask_session'
app.config['SESSION_PERMANENT'] = False

# ✅ ADD THIS LINE (VERY IMPORTANT)
os.makedirs('/tmp/flask_session', exist_ok=True)

# Initialize session
Session(app)

db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views
