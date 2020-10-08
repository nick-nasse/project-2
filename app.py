from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import csv

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/nyt")


@app.route('/')
def db():
    data = []
    with open("us-counties.csv") as file:
        filereader = csv.DictReader(file)
        for row in filereader:
            data.append(row)

    covidData = mongo.db.covid
    covidData.insert_many(data)
    return redirect("/home")

@app.route('/home')
def home():
    covidData = mongo.db.covid
    return render_template('home.html', covidData=covidData)

@app.route('/vis_1')
def vis_1():
    covidData = mongo.db.covid
    return render_template('vis_1.html', covidData=covidData)

@app.route('/vis_2')
def vis_2():
    covidData = mongo.db.covid
    return render_template('vis_2.html', covidData=covidData)

@app.route('/vis_3')
def vis_3():
    covidData = mongo.db.covid
    return render_template('vis_3.html', covidData=covidData)

if __name__ == '__main__':
    app.run(debug=True)

