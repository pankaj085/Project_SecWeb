from flask import Flask, render_template, redirect, session, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "SecWeb_Seceret_Key"

# Configure SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Database Model
class User(db.Model):  # Class variables
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


# Home route
@app.route("/")
def home():
    if "username" in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('register'))


# Login route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            session['username'] = user.username
            session['email'] = user.email
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Invalid Credentials")

    return render_template('login.html')


# Register route
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()

        if user:
            return render_template("register.html", error="User already exists!")
        else:
            new_user = User(username=username, email=email)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            session['username'] = username
            session['email'] = email
            return redirect(url_for('dashboard'))

    return render_template('register.html')


# Dashboard route
@app.route("/dashboard")
def dashboard():
    if "username" in session:
        return render_template('dashboard.html', username=session['username'])
    return redirect(url_for('login'))


# Logout route
@app.route("/logout")
def logout():
    session.pop('username', None)
    session.pop('email', None)
    return redirect(url_for('login'))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
