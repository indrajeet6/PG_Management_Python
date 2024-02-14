from flask_wtf import FlaskForm, CSRFProtect
from wtforms.validators import DataRequired, Length
from wtforms import StringField, SubmitField, TextAreaField

class AddNewTenant(FlaskForm):
    # Python Script to generate an Add New Tenant Form
    strTenantName = StringField("Name of Tenant", validators=[DataRequired()])
    strTenantOccupation = StringField("Occupation", validators=[DataRequired()])
    strCurrentAddress = TextAreaField("Current Address", validators=[DataRequired()])
    strPermanentAddress = TextAreaField("Permanent Address", validators=[DataRequired()])
    strOfficeAddress = TextAreaField("Office Address", validators=[DataRequired()])
    strMobile= StringField("Mobile Phone Number", validators=[DataRequired(), Length(10)])
    
    
    submit = SubmitField("Submit")
    