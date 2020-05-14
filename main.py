from flask import Flask, render_template, request, make_response
from get_menu import get_menu
import pandas as pd

app = Flask(__name__)


@app.route("/")
def test():
    args = request.args
    url = args.get("url")
    if url is not None:
        df = get_menu(url)
    else:
        df = pd.DataFrame([])

    return render_template("index.html", url=url, tables=[df.to_html(classes='u-full-width', index=False)])


@app.route('/csv/')
def download_csv():
    url = "https://www.ubereats.com/au/melbourne/food-delivery/leonards-house-of-love/wB5LCl7BSNugoFXljJbKOQ"
    df = get_menu(url)
    resp = make_response(df.to_csv(index=False))
    resp.headers["Content-Disposition"] = "attachment; filename=export.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp
