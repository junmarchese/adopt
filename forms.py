from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, AnyOf

class AddPetForm(FlaskForm):
    """Form for adding a new pet."""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired(), AnyOf(['cat', 'dog', 'porcupine'])])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes", validators=[Optional()])


class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Available")