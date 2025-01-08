from src import app, db
from flask import render_template, send_from_directory, request, redirect, url_for, flash
from src.repo.rep import dbHelper
from src.utils.functions import check_input


class RouteFactory:
    @staticmethod
    def create_route(route_type, **kwargs):
        if route_type == 'index':
            return lambda: render_template("home.html", perfs=kwargs.get('perfs'))
        elif route_type == 'hall':
            return lambda: render_template("hall.html", seats=kwargs.get('seats'))
        elif route_type == 'confirm':
            return lambda: render_template('confirm.html', activeSeats=kwargs.get('activeSeats'))
        elif route_type == 'admin_performance.html':
            return lambda: render_template('admin_performance.html', perfs=kwargs.get('perfs'))
        else:
            raise ValueError(f"Unknown route type: {route_type}")


dbase = dbHelper()


@app.route('/admin/performance', methods=['GET', 'POST'])
def show_performances():
    perfs = dbase.getAllPerfs()
    route = RouteFactory.create_route('admin_performance.html', perfs=perfs)
    return route()

@app.route('/admin/performance/add', methods=['GET', 'POST'])
def add_performance():
    if request.method == 'POST':
        name = request.form['name']
        age_restriction = request.form['age_restriction']
        cover = request.form['cover']
        print('suka')
        new_perf = dbase.addPerf(name=name, age_restriction=age_restriction, cover=cover)
        print('sukkka')
        return redirect(url_for('show_performances'))

    return render_template('add_performance.html')


# Функция для загрузки изображений для представлений
@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


# Главная страница с представлениями
@app.route("/", methods=['GET', 'POST'])
def index():
    perfs = dbase.getAllPerfs()
    print(perfs)
    route = RouteFactory.create_route('index', perfs=perfs)
    return route()

@app.route("/performance/<int:perf_id>")
def performance_detail(perf_id):
    performance = dbase.getAllPerfs(perf_id)
    shows = dbase.getAllShowsByPerfID()

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
            print(name, surname, email)
            dbase.addClient(name=name, surname=surname, email=email)

            for seat in activeSeats:
                dbase.addTicket(seat_id=seat, client_id=dbase.getClientIdByEmail(email=email))
            tickinfo = dbase.getTicketsInfo()
            return render_template('tickets.html', tickets=tickinfo)

        elif request.form['action'] == 'cancel':
            activeSeats = []
            return redirect(url_for('index'))
    return '', 200
