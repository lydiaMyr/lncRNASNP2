from flask import render_template, make_response

from lncRNASNP2 import app
from lncRNASNP2.core import mongo


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/download_sequence/lncrna/<lncrna>")
def download_lncrna(lncrna):
    record = mongo.db.lncrna_sequence.find_one({"lncrna": lncrna})
    fasta_file_content = record['sequence']
    title = '>'+lncrna+'\r\n'
    response = make_response(title+fasta_file_content)
    response.headers['Content-Type'] = "text/plain"
    return response

