from app import app
from flask import render_template


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/trendingVideos")
def trendingVideos():
    return render_template("trendingVideos.html")

@app.route("/mostCommentedPage")
def index2():
    return render_template("mostCommentedPage.html")


@app.route("/popularityByRegion")
def index3():
    return render_template("popularityByRegion.html")


@app.route("/factorsImpactingPopularity")
def index4():
    return render_template("factorsImpactingPopularity.html")
