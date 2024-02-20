"""
Routes and views for the flask application.
"""
from pickle import OBJ
import mysql.connector
from datetime import datetime
from flask import render_template, request
from PG_Management import app
from PG_Management.Config.ConfigReader import getConfig
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField
from flask import flash
from PG_Management.PythonForms.AddNewTenant import AddNewTenant
import PG_Management.PythonForms

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

@app.route('/NewTenant', methods=['GET', 'POST'])
def NewTenant():
    """Renders the contact page."""
    form = AddNewTenant()
    message = ""
    if request.method == "POST":
      if form.validate_on_submit():
          flash(f"Data Added Successfully!", category="success")
      else:
         flash(f"An Error Happened!", category="error")  
          
    return render_template(
        'AddNewTenant.html',
        title='Add data for a new Tenant',
        year=datetime.now().year,
        message='Add New Tenant',
        form=form
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
