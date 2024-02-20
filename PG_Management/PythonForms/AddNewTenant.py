from flask_wtf import FlaskForm, CSRFProtect
from wtforms.validators import DataRequired, Length
from wtforms import StringField, SubmitField, TextAreaField

class AddNewTenant(FlaskForm):
    # Python Script to generate an Add New Tenant Form
    
    #Tenant Details
    strTenantName = StringField("Name of Tenant", validators=[DataRequired()])
    strTenantOccupation = StringField("Occupation", validators=[DataRequired()])
    strCurrentAddress = TextAreaField("Current Address", validators=[DataRequired()])
    strPermanentAddress = TextAreaField("Permanent Address", validators=[DataRequired()])
    strOfficeAddress = TextAreaField("Office Address", validators=[DataRequired()])
    strMobile= StringField("Mobile Phone Number", validators=[DataRequired(), Length(10)])
    
    #Tenant Father Details
    strFatherName = StringField("Name of Father", validators=[DataRequired()])
    strFatherOccupation = StringField("Occupation", validators=[DataRequired()])
    strFatherCurrentAddress = TextAreaField("Current Address", validators=[DataRequired()])
    strFatherPermanentAddress = TextAreaField("Permanent Address", validators=[DataRequired()])
    strFatherOfficeAddress = TextAreaField("Office Address", validators=[DataRequired()])
    strFatherMobile= StringField("Mobile Phone Number", validators=[DataRequired(), Length(10)])
    
    #Tenant LG Details
    strLGName = StringField("Name of LG", validators=[DataRequired()])
    strLGOccupation = StringField("Occupation", validators=[DataRequired()])
    strLGCurrentAddress = TextAreaField("Current Address", validators=[DataRequired()])
    strLGPermanentAddress = TextAreaField("Permanent Address", validators=[DataRequired()])
    strLGOfficeAddress = TextAreaField("Office Address", validators=[DataRequired()])
    strLGMobile= StringField("Mobile Phone Number", validators=[DataRequired(), Length(10)])
    
    submit = SubmitField("Submit")
    