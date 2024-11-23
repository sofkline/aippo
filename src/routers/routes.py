from src import app
from src.models.tables.models import PerformancesTable
from flask import render_template, send_from_directory


@app.route("/")
def index():
    return render_template("home.html")

@app.route("/tst")
def tst():
    perf = PerformancesTable.query.all()
    return render_template("tst.html", perf=perf)


