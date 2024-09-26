from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
import psycopg2



app = Flask(__name__)

app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:Kratos1000Kratos@localhost:2000/querydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



from custom import routes