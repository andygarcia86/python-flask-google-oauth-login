from flask import Flask
from flask import render_template, redirect
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    logout_user,
)

app = Flask(__name__)

# User session management setup
# https://flask-login.readthedocs.io/en/latest
login_manager = LoginManager()
login_manager.init_app(app)


@app.route("/")
def hello_world():
    if current_user.is_authenticated:
        return render_template("index.html")
    else:
        return redirect("/login", code=302)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

