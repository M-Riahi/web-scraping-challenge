# MongoDB and Flask Application
#################################################

# Dependencies and Setup
from flask import Flask, render_template
from flask_Pymongo import PyMongo
import nasa_scraper
from bs4 import BeautifulSoup as bs
import requests
import pymongo
import pandas as pd

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# PyMongo Connection Setup
#################################################
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#################################################
# Flask Routes
#################################################
# Root Route to Query MongoDB & Pass Mars Data Into HTML Template: index.html to Display Data
@app.route("/")
def index():
    mars_si = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars_si)

# Scrape Route to Import `nasa_scraper.py` Script & Call `scrape` Function
@app.route("/scrape")
def scrapper():
    mars_si = mongo.db.mars_si
    mars_data = nasa_scraper.scrape_all()
    mars_si.update({}, mars_data, upsert=True)
    return "Scraping Successful"

# Define Main Behavior
if __name__ == "__main__":
    app.run()