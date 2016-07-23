from flask_wtf import Form
from wtforms.fields import StringField, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, Regexp


regex_string = '^[A-Za-z0-9_]{3,}$'
regex_err = "Usernames must consist of letters, numbers and underscores."


class ContactForm(Form):
    name = StringField('Name: ', validators=[DataRequired(), Length(3, 80),
                                             Regexp(regex_string,
                                                    message=regex_err)])
    email = EmailField('Email: ', validators=[DataRequired(), Length(3, 254)])
    subject = StringField('Subject')
    message = TextAreaField('Message: ', validators=[DataRequired(), Length(1, 8192)])
