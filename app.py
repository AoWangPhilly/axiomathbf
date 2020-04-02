from flask import Flask, render_template,request
from wtforms import Form, FloatField, StringField, validators
from axiomathbf.multivariate_calculus import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("chapter1.html")

class PointInput(Form):
    point1 = StringField(label="point1")
    point2 = StringField(label="point2")
    x1 = FloatField(label="x", validators=[validators.InputRequired()])
    y1 = FloatField(label="y", validators=[validators.InputRequired()])
    z1 = FloatField(label="z")
    x2 = FloatField(label="x", validators=[validators.InputRequired()])
    y2 = FloatField(label="y", validators=[validators.InputRequired()])
    z2 = FloatField(label="z")

class VectorInput(Form):
    v1 = FloatField(label="i", validators=[validators.InputRequired()])
    v2 = FloatField(label="j", validators=[validators.InputRequired()])
    v3 = FloatField(label="k")
    w1 = FloatField(label="i", validators=[validators.InputRequired()])
    w2 = FloatField(label="j", validators=[validators.InputRequired()])
    w3 = FloatField(label="k")

@app.route('/', methods=['GET','POST'])
def part1():
    form1 = VectorInput(request.form)
    form2 = PointInput(request.form)
    if request.method == "POST" and form1.validate():
        angle = angle_between_vectors(make_vector(form1.v1.data, form1.v2.data, form1.v3.data),
                                       make_vector(form1.w1.data, form1.w2.data, form1.w3.data))
        return render_template("chapter1.html", form1=form1, angle=angle)
    if request.method == "POST" and form2.validate():
        p_to_p = form2.point1.data + form2.point2.data
        p1 = Point(form2.x1.data, form2.y1.data, form2.z1.data)
        p2 = Point(form2.x2.data, form2.y2.data, form2.z2.data)
        vector = point_to_point_vector(p1,p2)
        return render_template("chapter1.html", form2=form2, vector=vector, p_to_p=p_to_p)    
    return render_template("chapter1.html")
    
if __name__ == "__main__":
    app.run(debug=True)