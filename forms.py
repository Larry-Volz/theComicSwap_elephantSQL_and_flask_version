from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateField, DateTimeField, IntegerField, StringField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, Email, NumberRange, AnyOf, URL



class EditComicsForm(FlaskForm):

    owner = StringField("Owner's Name", 
        validators = [InputRequired(message = "cannot be blank")])

    title = StringField("Title of Comic", 
        validators = [InputRequired(message = "cannot be blank")])

    issuenumber = IntegerField("Issue Number")

    year = IntegerField("Year")

    price = FloatField("Price")

    publisher = StringField("Publisher", 
        validators = [InputRequired(message = "cannot be blank")])

    pedigree = IntegerField("Pedigree")

    location = IntegerField("Location")

    grade = FloatField("Grade")

    assessed_source = StringField("Grading Source", 
        validators = [InputRequired(message = "cannot be blank")])

    email = StringField("Email", 
        validators = [Optional(), Email()])

    notes = StringField("Notes", 
        validators = [InputRequired(message = "cannot be blank")])




class SubscriptionForm(FlaskForm):
    fname = StringField("First Name", 
        validators = [InputRequired(message = "cannot be blank")])

    lname = StringField("Last Name", 
        validators = [InputRequired(message = "cannot be blank")])

    username = StringField("User Name", 
        validators = [InputRequired(message = "cannot be blank")])
    
    email = StringField("Email", 
        validators = [Optional(), Email()])

    password = StringField("Password", 
        validators = [InputRequired(message = "cannot be blank")])

    address1 = StringField("Address", 
        validators = [Optional()])

    address2 = StringField("Address 2 (optional)", 
        validators = [Optional()])

    city = StringField("City)", 
        validators = [Optional()])

    state = StringField("State", 
        validators = [Optional()])

    zip = StringField("Zip code", 
        validators = [Optional()])

