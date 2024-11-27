from src import app
from src.models.tables.models import PerformancesTable, SeatsTable
from flask import render_template, send_from_directory


@app.route("/")
def index():
    perfs = PerformancesTable.query.all()
    return render_template("home.html", perfs=perfs)

@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route("/<perf_name>")
def perf(perf_name):
    perf = PerformancesTable.query.get_or_404(perf_name)
    seats = SeatsTable.query.all()
    return render_template("performance.html", perf=perf, seats=seats)

@app.route("/tst")
def tst():
    perfs = PerformancesTable.query.all()
    return render_template("tst.html", perfs=perfs)


