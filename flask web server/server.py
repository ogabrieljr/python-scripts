from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/<string:page>')
def template(page):
    return render_template(page)


@app.route('/<string:page>', methods=["POST", "GET"])
def submit_form(page):
    if request.method == "POST":
        data = request.form.to_dict()
        return redirect("/thankyou.html")
