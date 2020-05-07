from flask import Flask, render_template, request
from get_menu import get_menu
import pandas as pd
from rq import Queue
from worker import conn

q = Queue(connection=conn)
result = q.enqueue(get_menu, 'http://heroku.com')

app = Flask(__name__)

"""
df = pd.DataFrame({'A': [0, 1, 2, 3, 4],
                   'B': [5, 6, 7, 8, 9],
                   'C': ['a', 'b', 'c--', 'd', 'e']})
"""

# df = get_menu("https://www.ubereats.com/au/melbourne/food-delivery/ez-thai-cafe/osnrZYXYTbe6HFMa_JU-7g/27ced650-2a4b-4371-b22c-2bf9335b771a")


@app.route("/")
def test():
    args = request.args
    url = args.get("url")
    if url is not None:
        df = get_menu(url)
    else:
        df = pd.DataFrame([])

    return render_template("index.html", url=url, tables=[df.to_html(classes='u-full-width', index=False)])
