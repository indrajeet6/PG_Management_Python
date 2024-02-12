"""
Routes and views for the flask application.
"""
from pickle import OBJ
import mysql.connector
from datetime import datetime
from flask import render_template
from PG_Management import app
from PG_Management.Config.ConfigReader import getConfig

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    mydb = mysql.connector.connect(
          host = getConfig("LocalDB","host"),
          user = getConfig("LocalDB","user"),
          password = getConfig("LocalDB","password"),
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM db_a6d03c_pgmgmt.`payment status`;")
    myresult = mycursor.fetchall()
    
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        data = myresult,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
