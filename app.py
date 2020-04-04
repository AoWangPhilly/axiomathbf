from flask import Flask, request, render_template
from forms import VectorDomainForm
from axiomathbf.multivariate_calculus import * 
app = Flask(__name__)

app.config["SECRET_KEY"] = '4af46c5f760d6b6a017235ba711c5a2e'
@app.route("/")
@app.route("/home")
def index():
	return render_template("index.html")


@app.route("/vector_domain", methods=["GET", "POST"])
def vector_domain():
    form = VectorDomainForm()
    try:
        if form.validate_on_submit():
            if "^" in form.vect1.data:
                form.vect1.data = form.vect1.data.replace("^", "**")
            if "^" in form.vect2.data:
                form.vect2.data = form.vect2.data.replace("^", "**")
            if "^" in form.vect3.data:
                form.vect3.data = form.vect3.data.replace("^", "**")
            domain = latex(find_domain_of_vector_function(make_vector(eval(form.vect1.data), eval(form.vect2.data), eval(form.vect3.data))))
            return render_template("vector_domain.html", title="Vector Domain", form=form, domain=domain, parts=[latex(eval(form.vect1.data)),
                                                                                                                 latex(eval(form.vect2.data)),
                                                                                                                 latex(eval(form.vect3.data))])
    except (TypeError, NameError, SyntaxError) as e:
        print("NO!")
    return render_template("vector_domain.html", title="Vector Domain", form=form)

if __name__ == "__main__":
    app.run(debug=True)