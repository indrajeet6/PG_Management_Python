from flask_wtf import FlaskForm, CSRFProtect
from wtforms.validators import DataRequired, Length, NumberRange
from wtforms import StringField, SubmitField, TextAreaField, IntegerField

class AddNewTenant(FlaskForm):
    # Python Script to generate an Add New Tenant Form
    
    #Tenant Details
    strTenantName = StringField("Name of Tenant", validators=[DataRequired()])
    strTenantOccupation = StringField("Occupation", validators=[DataRequired()])
    strCurrentAddress = TextAreaField("Current Address", validators=[DataRequired()])
    strPermanentAddress = TextAreaField("Permanent Address", validators=[DataRequired()])
    strOfficeAddress = TextAreaField("Office Address", validators=[DataRequired()])
    strMobile= IntegerField("Mobile Phone Number", validators=[DataRequired(), NumberRange(min=1000000000, max=9999999999)])
    strRentAmount = IntegerField("Rent Amount", validators=[DataRequired(), NumberRange(min=1000, max=9999999999)])
    
    #Tenant Father Details
    strFatherName = StringField("Name of Father", validators=[DataRequired()])
    strFatherOccupation = StringField("Occupation", validators=[DataRequired()])
    strFatherCurrentAddress = TextAreaField("Current Address", validators=[DataRequired()])
    strFatherPermanentAddress = TextAreaField("Permanent Address", validators=[DataRequired()])
    strFatherOfficeAddress = TextAreaField("Office Address", validators=[DataRequired()])
    strFatherMobile= IntegerField("Mobile Phone Number", validators=[DataRequired(), NumberRange(min=1000000000, max=9999999999)])
    
    #Tenant LG Details
    strLGName = StringField("Name of LG", validators=[DataRequired()])
    strLGOccupation = StringField("Occupation", validators=[DataRequired()])
    strLGCurrentAddress = TextAreaField("Current Address", validators=[DataRequired()])
    strLGPermanentAddress = TextAreaField("Permanent Address", validators=[DataRequired()])
    strLGOfficeAddress = TextAreaField("Office Address", validators=[DataRequired()])
    strLGMobile= IntegerField("Mobile Phone Number", validators=[DataRequired(), NumberRange(min=1000000000, max=9999999999)])
    
    submit = SubmitField("Submit")