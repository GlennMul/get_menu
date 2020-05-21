from flask import Flask, render_template, request, make_response, session, jsonify
from get_menu import get_menu
import pandas as pd
import os

app = Flask(__name__)
app.secret_key = os.urandom(28)


@app.route("/", methods=["GET", "POST"])
def index():
    session.clear()
    args = request.args
    url = args.get("url")
    if url is not None:
        menu = get_menu(url)

    else:
        menu = '{}'

    return render_template("index.html", menu=menu, url=url,
                           tables=[pd.read_json(menu).to_html(classes='u-full-width', index=False)])


@app.route('/csv/<path:url>')
def download_csv(url):
    menu = get_menu(url)
    menu = pd.read_json(menu)
    resp = make_response(menu.to_csv(index=False))
    resp.headers["Content-Disposition"] = "attachment; filename=export.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp

@app.route('/upload/', methods = ["GET", "POST"])
def upload():

    return 200