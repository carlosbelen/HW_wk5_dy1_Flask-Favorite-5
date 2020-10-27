# Import the app variable from the init
from Fav_5 import app

# Import specific packages from flask
from flask import render_template

# Default Home Route
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Favorite_5')
def fav_5():
    names = ['Muhammad Ali','Jim Brown', 'Jim Thorpe','Jackie Robinson', 'Gary Carter', ]
    return render_template('Favorite_5.html',list_names = names)