from src import app
from src.models.tables.models import PerformancesTable, SeatsTable
from flask import render_template, send_from_directory, request


@app.route("/")
def index():
    perfs = PerformancesTable.query.all()
    return render_template("home.html", perfs=perfs)

@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route("/<perf_name>/hall")
def perf(perf_name):
    perf = PerformancesTable.query.get_or_404(perf_name)
    seats = SeatsTable.query.filter_by(performance_id=perf.id).all()
    print(perf.id)
    return render_template("performance.html", seats=seats)


active_buttons_id = []
@app.route('/toggleColor', methods=['POST'])
def toggle_color():
    data = request.get_json()
    button_id = data['button_id']
    if button_id not in active_buttons_id:
        active_buttons_id.append(button_id)
        print(button_id + 'added')
    elif button_id in active_buttons_id:
        active_buttons_id.remove(button_id)
        print(button_id + 'extended')
    print(active_buttons_id)
    # Сохраняем данные о нажатой кнопке в базе данных
    return '', 200

@app.route('/confirmChoice', methods=['GET', 'POST'])
def confirm_order():
    if request.method == 'POST':
        print(228)
        data = request.get_json()
        name = data['name']
        print(name)
    return '', 200



