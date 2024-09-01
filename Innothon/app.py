from flask import Flask, render_template, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy
import numpy as np
import re

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///SKITM_MedIQ.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'SKITM_MedIQ'
db = SQLAlchemy(app)

class App1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    airtemperature = db.Column(db.Float(), nullable=False)
    pressure = db.Column(db.Float(), nullable=False)
    windspeed = db.Column(db.Float(), nullable=False)

# ********************************** DB User table **********************************
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(15), nullable=False)
    lastName = db.Column(db.String(15), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

# ********************************** DB Contact Us table **********************************
class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

# ********************************** Creates all DB tables **********************************
with app.app_context():
    db.create_all()

name_pattern = re.compile(r'^[a-zA-Z]{1,15}$')
username_pattern = re.compile(r'^[a-z0-9_.]{6,}$')
email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@(?:gmail|yahoo|outlook)\.com$')
password_pattern = re.compile(r'^(?=.[a-z])(?=.[A-Z])(?=.\d)(?=.[@$!%?&])[A-Za-z\d@$!%?&]{8,}$')

# ******* alzheimers *******
@app.route('/alzheimers_img_yes')
def alzheimers_img_yes():
    return render_template('/alzheimers_img_yes.html')

@app.route('/alzheimers_img_no')
def alzheimers_img_no():
    return render_template('/alzheimers_img_no.html')

@app.route('/alzheimers_img')
def alzheimers_img():
    return render_template('/alzheimers_img.html')

@app.route('/alzheimers')
def alzheimers():
    return render_template('/alzheimers.html')

# ******* asthama *******
@app.route('/asthama_ques_no')
def asthama_ques_no():
    return render_template('/asthama_ques_no.html')

@app.route('/asthama_ques_yes')
def asthama_ques_yes():
    return render_template('/asthama_ques_yes.html')

@app.route('/asthama_ques')
def asthama_ques():
    return render_template('/asthama_ques.html')

@app.route('/asthma')
def asthma():
    return render_template('/asthama.html')

# ******* bp *******
@app.route('/bp_ques_no')
def bp_ques_no():
    return render_template('/bp_ques_no.html')

@app.route('/bp_ques_yes')
def bp_ques_yes():
    return render_template('/bp_ques_yes.html')

@app.route('/bp_ques')
def bp_ques():
    return render_template('/bp_ques.html')

@app.route('/bp')
def bp():
    return render_template('/bp.html')

# ******* brain *******
@app.route('/brain_img_yes')
def brain_img_yes():
    return render_template('/brain_img_yes.html')

@app.route('/brain_img_no')
def brain_img_no():
    return render_template('/brainimg_no.html')

@app.route('/brain_img')
def brain_img():
    return render_template('/brain_img.html')

@app.route('/brain')
def brain():
    return render_template('/brain.html')

# ******* breast *******
@app.route('/breast_ques_no')
def breast_ques_no():
    return render_template('/breast_ques_no.html')

@app.route('/breast_ques_yes')
def breast_ques_yes():
    return render_template('/breast_ques_yes.html')

@app.route('/breast_ques')
def breast_ques():
    return render_template('/breast_ques.html')

@app.route('/breast')
def breast():
    return render_template('/breast.html')

# ******* Choose *******
@app.route('/choose')
def choose():
    return render_template('/choose.html')

# ******* Diabetes *******
@app.route('/diabetes_ques_no')
def diabetes_ques_no():
    return render_template('/diabetes_ques_no.html')

@app.route('/diabetes_ques_yes')
def diabetes_ques_yes():
    return render_template('/diabetes_ques_yes.html')

@app.route('/diabetes_ques')
def diabetes_ques():
    return render_template('/diabetes_ques.html')

@app.route('/diabetes')
def diabetes():
    return render_template('/diabetes.html')

# ******* Emotion Detection *******
@app.route('/emotion_detection')
def emotion_detection():
    return render_template('/emotion_detection.html')

# ******* Heart *******
@app.route('/heart_ques_no')
def heart_ques_no():
    return render_template('/heart_ques_no.html')

@app.route('/heart_ques_yes')
def heart_ques_yes():
    return render_template('/heart_ques_yes.html')

@app.route('/heart_ques')
def heart_ques():
    return render_template('/heart_ques.html')

@app.route('/heart')
def heart():
    return render_template('/heart.html')

# ******* Home *******
@app.route('/home')
def home():
    return render_template('/home.html')

# ******* Index *******
@app.route('/')
def index():
    return render_template('/index.html')

# ******* Kidney *******
@app.route('/kidney_img_no')
def kidney_img_no():
    return render_template('/kidney_img_no.html')

@app.route('/kidney_img_yes')
def kidney_img_yes():
    return render_template('/kidney_img_yes.html')

@app.route('/kidney_img')
def kidney_img():
    return render_template('/kidney_img.html')

@app.route('/kidney')
def kidney():
    return render_template('/kidney.html')

# ******* Lungs *******
@app.route('/lungs_img_no')
def lungs_img_no():
    return render_template('/lungs_img_no.html')

@app.route('/lungs_img_yes')
def lungs_img_yes():
    return render_template('/lungs_img_yes.html')

@app.route('/lungs_img')
def lungs_img():
    return render_template('/lungs_img.html')

@app.route('/lungs')
def lungs():
    return render_template('/lungs.html')

# ******* Mental *******
@app.route('/mental_ques_no')
def mental_ques_no():
    return render_template('/mental_ques_no.html')

@app.route('/mental_ques_yes')
def mental_ques_yes():
    return render_template('/mental_ques_yes.html')

@app.route('/mental_ques')
def mental_ques():
    return render_template('/mental_ques.html')

@app.route('/mental')
def mental():
    return render_template('/mental.html')

# ******* Obesity *******
@app.route('/obesity_ques_no')
def obesity_ques_no():
    return render_template('/obesity_ques_no.html')

@app.route('/obesity_ques_yes')
def obesity_ques_yes():
    return render_template('/obesity_ques_yes.html')

@app.route('/obesity_ques')
def obesity_ques():
    return render_template('/obesity_ques.html')

@app.route('/obesity')
def obesity():
    return render_template('/obesity.html')

# ******* Parkinsons *******
@app.route('/parkinsons_ques_no')
def parkinsons_ques_no():
    return render_template('/parkinsons_ques_no.html')

@app.route('/parkinsons_ques_yes')
def parkinsons_ques_yes():
    return render_template('/parkinsons_ques_yes.html')

@app.route('/parkinsons_ques')
def parkinsons_ques():
    return render_template('/parkinsons_ques.html')

@app.route('/parkinsons')
def parkinsons():
    return render_template('/parkinsons.html')

# ******* SignIn *******
@app.route('/signin', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Find user by username
        user = User.query.filter_by(username=username).first()

        if user:
            # Check if the password matches
            if user.password == password:
                flash('sign_in successful!', 'success')
                return redirect('/home')
            else:
                flash('Incorrect password. Please try again.', 'error')
                return redirect('/signin')  # Redirect after flashing error message
        else:
            flash('User not found. Please sign up first.', 'error')
            return redirect('/signup')

    return render_template('signin.html')

# ******* SignUp *******
@app.route('/signup',  methods=['GET', 'POST']) # Accept both GET and POST requests
def sign_up():
    if request.method == 'POST':
        firstName = request.form['firstname']
        lastName = request.form['lastname']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check if the first name and last name meet the criteria
        if not name_pattern.match(firstName) or not name_pattern.match(lastName):
            flash('First name and last name must be between 1 and 15 characters long and contain only letters.', 'error')
            return redirect('/signup')


        # Check if the email meets the criteria
        if not email_pattern.match(email):
            flash('Email must be in a valid format (@gmail.com, @yahoo.com, @outlook.com, etc.)', 'error')
            return redirect('/signup')

        # Check if the password meets the criteria
        if not password_pattern.match(password):
            flash('Password must contain at least 8 characters, 1 capital letter, 1 small letter, and 1 symbol.', 'error')
            return redirect('/signup')

        # Check if the username or email already exists
        if User.query.filter_by(username=username).first() is not None:
            flash('User already exists! Choose a different username.', 'error')
            return redirect('/signup')
        elif User.query.filter_by(email=email).first() is not None:
            flash('Email already exists! Use a different email address.', 'error')
            return redirect('/signup')

        # If all validation passes, create a new user
        new_user = User(firstName=firstName, lastName=lastName, username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful. Now, user can sign in.', 'success')
        return redirect('/signin')

    # If it's a GET request, just render the sign_up form
    return render_template('signup.html')

# ******* Skin *******
@app.route('/skin_img_no')
def skin_img_no():
    return render_template('skin_img_no.html')

@app.route('/skin_img_yes')
def skin_img_yes():
    return render_template('skin_img_yes.html')

@app.route('/skin_img')
def skin_img():
    return render_template('skin_img.html')

@app.route('/skin')
def skin():
    return render_template('skin.html')

# ******* TB *******
@app.route('/tb_ques_no')
def tb_ques_no():
    return render_template('tb_ques_no.html')

@app.route('/tb_ques_yes')
def tb_ques_yes():
    return render_template('tb_ques_yes.html')

@app.route('/tb_ques')
def tb_ques():
    return render_template('tb_ques.html')

@app.route('/tb')
def tb():
    return render_template('tb.html')

# ******* Thyroid *******
@app.route('/thyroid_ques_no')
def thyroid_ques_no():
    return render_template('thyroid_ques_no.html')

@app.route('/thyroid_ques_yes')
def thyroid_ques_yes():
    return render_template('thyroid_ques_yes.html')

@app.route('/thyroid_ques')
def thyroid_ques():
    return render_template('thyroid_ques.html')

@app.route('/thyroid')
def thyroid():
    return render_template('thyroid.html')

if __name__ == "__main__":
    app.run(debug=True)