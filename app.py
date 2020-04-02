from flask import Flask, render_template,request
from wtforms import Form, FloatField, validators
from axiomathbf.multivariate_calculus import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("chapter1.html")

class PointInput(Form):
    x1 = FloatField(label="x", validators=[validators.InputRequired()])
    y1 = FloatField(label="y", validators=[validators.InputRequired()])
    z1 = FloatField(label="z", default=0)
    x2 = FloatField(label="x", validators=[validators.InputRequired()])
    y2 = FloatField(label="y", validators=[validators.InputRequired()])
    z2 = FloatField(label="z", default=0)

class VectorInput(Form):
    v1 = FloatField(label="i", validators=[validators.InputRequired()])
    v2 = FloatField(label="j", validators=[validators.InputRequired()])
    v3 = FloatField(label="k", default=0)
    w1 = FloatField(label="i", validators=[validators.InputRequired()])
    w2 = FloatField(label="j", validators=[validators.InputRequired()])
    w3 = FloatField(label="k", default=0)

@app.route('/', methods=['GET','POST'])
def part1():
    form1 = VectorInput(request.form)
    form2 = PointInput(request.form)
    if request.method == "POST" and form1.validate():
        angle = angle_between_vectors(make_vector(form1.v1.data, form1.v2.data, form1.v3.data),
                                       make_vector(form1.w1.data, form1.w2.data, form1.w3.data))
        return render_template("chapter1.html", form1=form1, angle=angle)
    if request.method == "POST" and form2.validate():
        vector = point_to_point_vector(Point(form2.x1.data, form2.y1.data, form2.z1.data),
                                       Point(form2.x2.data, form2.y2.data, form2.z2.data))
        return render_template("chapter1.html", form2=form2, vector=vector)
        
    return render_template("chapter1.html")
    
if __name__ == "__main__":
    app.run(debug=True)