from flask import Flask, render_template

import data_utils

papers_data, confs_data = data_utils.load_data()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", conferences=confs_data)

@app.route("/<conference>/")
def conference(conference):
    conference_name = data_utils.beautify_conf_name_year(conference)
    return render_template("papers.html", 
                            conference=conference, 
                            papers=papers_data[conference], 
                            conference_name=conference_name)

@app.route("/about/")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True, port=8001)