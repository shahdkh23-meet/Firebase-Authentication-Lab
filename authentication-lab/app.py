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
"databaseURL": "https://console.firebase.google.com/project/first-try-firebase-6e2dd/database/first-try-firebase-6e2dd-default-rtdb/data/~2F"
  } 


firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()




app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'



@app.route('/', methods=['GET', 'POST'])
def signin():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            user = {"name": "Ward", "email": "W@h.com"}
            db.child("Users").child(login_session['user']['localId']).set(user)
            return redirect(url_for('home'))
        except:
            error = "Authentication failed"
    return render_template("add_tweet.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            return redirect(url_for('home'))
        except:
            error = "Authentication failed"
    return render_template("add_tweet.html")





@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    if request.method == 'POST':
        try:
            tweet = {"name": request.form['name'],"content": request.form['content'], "uid": login_session['user']['localId']}
            db.child("tweet").push(tweet)
        except:
            print(" sorry Couldn't add tweet , try again ")
    return render_template("add_tweet.html")


@app.route('/all_tweets', methods=['GET', 'POST'])
def all_tweet():
    display = db.child("Display").get().val()
    return render_template("tweets.html")





if __name__ == '__main__':
    app.run(debug=True)