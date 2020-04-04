from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
	return render_template("index.html")

@app.route("/vector_domain")
def about():
	return render_template("vector_domain.html", title="Vector Domain")

if __name__ == "__main__":
    app.run(debug=True)