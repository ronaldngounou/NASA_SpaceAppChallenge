from app import app
from flask import render_template, request
import json


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/inspector")
def inspector():
    return render_template("inspector.html")

@app.route("/Tableau1")
def index2():
    return render_template("Tableau1.html")


@app.route("/Tableau2")
def index3():
    return render_template("Tableau2.html")


@app.route("/factorsImpactingPopularity")
def index4():
    return render_template("factorsImpactingPopularity.html")



@app.route('/search', methods=['POST', "Get"])
def search():
    with open('./data/meta.json') as f:
        data = json.load(f)
    query = request.form.get('query')
    print(query)

    results = []
    if request.method == 'POST':
        query = request.form.get('query')
        for iid,item in data.items():
            if query.lower() in item['name'].lower():
                item["iid"] = iid
                results.append(item)
    return render_template('index.html', results=results)

@app.route('/new_route')
def new_route():
    iid = request.args.get('iid')
    # Use the id to get the data for this item
    item = next((item for item in ["3","5"] if item == (iid)), None)
    return render_template('item.html', item=item)