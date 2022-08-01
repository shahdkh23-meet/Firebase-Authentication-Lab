from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config = {
"apiKey": "AIzaSyCftFrZbHcMC0dz2XqzVva0B1RXnBp9qCk",

"authDomain": "first-try-firebase-6e2dd.firebaseapp.com",

"projectId": "first-try-firebase-6e2dd",

"storageBucket": "first-try-firebase-6e2dd.appspot.com",

"messagingSenderId": "572341558806",

"appId": "1:572341558806:web:acacd3a8dab8d879fbdf37",

"measurementId": "G-TQTQ9ZV9CN",
"databaseURL": ""
  } 


firebase = pyrebase.initialize_app(config)
auth = firebase.auth()




app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'



@app.route('/', methods=['GET', 'POST'])
def signin():
   return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            return redirect(url_for('add_tweet.html'))
        except:
            error = "Authentication failed"
    else: 
        return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")




if __name__ == '__main__':
    app.run(debug=True)