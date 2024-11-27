import datetime

from src import app, db

class TicketsTable(db.Model):
    __tablename__ = 'tickets'
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))
    date = db.Column(db.DateTime(), nullable=False)


class ClientsTable(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True)
    seat_id = db.Column(db.Integer, db.ForeignKey('seats.id'))
    name = db.Column(db.Integer, nullable=False)
    surname = db.Column(db.Integer, nullable=False)
    patronymic = db.Column(db.String)


class SeatsTable(db.Model):
    __tablename__ = 'seats'
    id = db.Column(db.Integer, primary_key=True)
    seat_num = db.Column(db.Integer, nullable=False)
    row_num = db.Column(db.Integer)
    price = db.Column(db.Integer)
    is_available = db.Column(db.Boolean, default=True)


class PerformancesTable(db.Model):
    __tablename__ = 'performances'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    cover = db.Column(db.String(50), nullable=False, default='default.jpg')
    discription = db.Column(db.String(255))



with app.app_context():
    #db.drop_all()
    db.create_all()
