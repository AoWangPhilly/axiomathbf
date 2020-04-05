from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class VectorDomainForm(FlaskForm):
    vect1 = StringField(validators=[DataRequired()], render_kw={"placeholder":"1st component"})
    vect2 = StringField(validators=[DataRequired()], render_kw={"placeholder":"2nd component"})
    vect3 = StringField(validators=[DataRequired()], render_kw={"placeholder":"3rd component"})
    submit = SubmitField("Calculate")
    

class GradientForm(FlaskForm):
    pass