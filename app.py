from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo


app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
# app.config["MONGO_URI"] = "mongodb://localhost:27017/mars"
# mongo = PyMongo(app)


@app.route('/')
def home():
    # listings = mongo.db.listings
    return render_template('home.html')

@app.route('/vis_1')
def vis_1():
    # listings = mongo.db.listings
    return render_template('vis_1.html')

@app.route('/vis_2')
def vis_2():
    # listings = mongo.db.listings
    return render_template('vis_2.html')

@app.route('/vis_3')
def vis_3():
    # listings = mongo.db.listings
    return render_template('vis_3.html')

if __name__ == '__main__':
    app.run(debug=True)


# def home():
#     # listings = mongo.db.listings
#     return render_template('home.html', listings=listings)
