from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    first_name = "John"
    pizzas = ["Pepperoni", "cheese", "Mushrooms"]
    return render_template("index.html", first_name=first_name, pizzas=pizzas)


@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name=name)


# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


# Internal Server Error URL
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500
