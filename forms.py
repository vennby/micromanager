from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed

class EventForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    date = StringField('Date', validators=[DataRequired()])
    participants = IntegerField('Participants', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    image = FileField('Event Image', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Save')
