from src import app, db
from flask import render_template, send_from_directory, request, redirect, url_for, flash
from src.repo.rep import dbHelper
from src.utils.functions import check_input


dbase = dbHelper()

# Главная страница
@app.route("/", methods=['GET', 'POST'])
def index():
    perfs = dbase.getAllPerfs()
    return render_template("home.html", perfs=perfs)


# Функция для загрузки изображений для предтсавлений
@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


# Страница с изображением мест
@app.route("/<perf_id>/hall")
def perf(perf_id):
    seats = dbase.getSeatsForPerf(perf_id)
    return render_template("hall.html", seats=seats)


activeSeats = []
@app.route('/getActiveSeats', methods=['GET', 'POST'])
def getActiveSeats():
    if request.method == 'POST':
        data = request.get_json()
        global activeSeats
        activeSeats = data.get('seats')
    return '', 200


# Страница с заполнением данных и подтверждением выбора мест
@app.route('/confirm')
def confirm():
    #if len(activeSeats) == 0: сделать логику на случай, если юзер не выбрал ни одного места
     #   flash('Выберите места!')
      #  return redirect(url_for('perf'))
    return render_template('confirm.html', activeSeats=activeSeats)


@app.route('/confirmOrder', methods=['POST', 'GET'])
def confirm_order():
    if request.method == 'POST':
        global activeSeats
        if request.form['action'] == 'submit':
            name = request.form.get('name')
            surname = request.form.get('surname')
            email = request.form.get('email')

            check_input(name=name, surname=surname, email=email, activeSeats=activeSeats)
            dbase.addClient(name=name, surname=surname, email=email)

            for seat in activeSeats:
                dbase.addTicket(seat_id=seat, client_id=dbase.getClientIdByEmail(email=email))
            tickinfo = dbase.getTicketsInfo()
            return render_template('tickets.html', tickets=tickinfo)

        elif request.form['action'] == 'cancel':
            activeSeats = []
            return redirect(url_for('index'))
    return '', 200
