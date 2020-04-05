from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, Length

class VectorDomainForm(FlaskForm):
    vect1 = StringField(validators=[DataRequired()], render_kw={"placeholder":"1st component"})
    vect2 = StringField(validators=[DataRequired()], render_kw={"placeholder":"2nd component"})
    vect3 = StringField(validators=[DataRequired()], render_kw={"placeholder":"3rd component"})
    submit = SubmitField("Calculate")
    

class GradientForm(FlaskForm):
    function = StringField(validators=[DataRequired()], render_kw={"placeholder":"function"})
    point_x = FloatField(validators=[DataRequired()], render_kw={"placeholder":"x"})
    point_y = FloatField(validators=[DataRequired()], render_kw={"placeholder":"y"})
    point_z = FloatField(validators=[DataRequired()], render_kw={"placeholder":"z"})
    submit = SubmitField("Calculate")
                        