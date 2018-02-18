from wtforms import Form, BooleanField, StringField, PasswordField, validators

class ContactForm(Form):
    name = StringField('Name', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=40)])
    subject = StringField('Subject', [validators.Length(min=1, max=50)])
    message = StringField('Message', [validators.Length(min=3, max=500)])