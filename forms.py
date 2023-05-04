from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class DataForm(FlaskForm):
    winch_choices = StringField(
        "Winch Choices (comma separated)", validators=[DataRequired()]
    )
    line_number = StringField("Line Number", validators=[DataRequired()])
    operation = StringField(
        "Operation (recovery or deployment)", validators=[DataRequired()]
    )
    column_index = IntegerField("Column Index", validators=[DataRequired()])
    submit = SubmitField("Submit")
