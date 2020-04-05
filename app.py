from flask import Flask, request, render_template
from forms import VectorDomainForm
from axiomathbf.multivariate_calculus import * 
app = Flask(__name__)

app.config["SECRET_KEY"] = '4af46c5f760d6b6a017235ba711c5a2e'

def clean_up_input(n):
    if "^" in n:
        n = n.replace("^", "**")
    if "e" in n:
        n = n.replace("e", "E")
    if "ln" in n:
        n = list(n)
        if n.index("n")-n.index("l") == 1:
            n.insert(n.index("n")+1,"(abs")
            n.insert(n.index(")"), ")")
            n = "".join(n)
    return n


@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")


@app.route("/vector_domain", methods=["GET", "POST"])
def vector_domain():
    form = VectorDomainForm()
    try:
        if form.validate_on_submit():
            vect = [form.vect1.data, form.vect2.data, form.vect3.data]
            for idx in range(len(vect)):
                vect[idx] = eval(clean_up_input(vect[idx]))
            domains = find_domain_of_vector_function(make_vector(vect[0], vect[1], vect[2]))
            intersected_domain = latex(domains[0])
            return render_template("vector_domain.html", title="Vector Domain", form=form, intersected_domain=intersected_domain, multiple_domains=domains[1], parts=[latex(v) for v in vect])
    except (TypeError, NameError, SyntaxError) as e:
        print("Error! >:D")
    return render_template("vector_domain.html", title="Vector Domain", form=form)


@app.route("/gradient", methods=["GET", "POST"])
def finding_gradient():
    form = GradientForm()
    try:
        if form.validate_on_submit():
            pass
    except:
        print("Error")

        
if __name__ == "__main__":
    app.run(debug=True)