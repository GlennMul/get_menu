from flask import Flask, render_template, request, make_response, session
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
        df = get_menu(url)
        session["data"] = df.to_json()
    else:
        df = pd.DataFrame([])
        session["data"] = df.to_json()

    return render_template("index.html", url=url, tables=[df.to_html(classes='u-full-width', index=False)])


@app.route('/csv/')
def download_csv():
    df = session.get('data')
    df = pd.read_json(df)
    resp = make_response(df.to_csv(index=False))
    resp.headers["Content-Disposition"] = "attachment; filename=export.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp
