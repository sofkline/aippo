import datetime

from src import app, db

class TicketsTable(db.Model):
    __tablename__ = 'tickets'
    id = db.Column(db.Integer, primary_key=True)
    seat_id = db.Column(db.Integer, db.ForeignKey('seats.id'))

    def __repr__(self):
        return f"TicketsTable {TicketsTable.id}"


class ClientsTable(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    surname = db.Column(db.String, nullable=False)
    patronymic = db.Column(db.String, nullable=True)
    ticket_id = db.Column(db.Integer, db.ForeignKey('tickets.id'))

    def __repr__(self):
        return f"ClientsTable {ClientsTable.id}"



class SeatsTable(db.Model):
    __tablename__ = 'seats'
    id = db.Column(db.Integer, primary_key=True)
    seat_num = db.Column(db.Integer, nullable=False)
    row_num = db.Column(db.Integer)
    price = db.Column(db.Integer)
    is_available = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f"ClientsTable {ClientsTable.id}"

class HallTable(db.Model):
    __tablename = 'halls'
    id = db.Column(db.Integer, primary_key=True)

class PerformancesTable(db.Model):
    __tablename__ = 'performances'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    cover = db.Column(db.String(50), nullable=False, default='default.jpg')
    discription = db.Column(db.String(255))

    def __repr__(self):
        return f"ClientsTable {ClientsTable.id}"



with app.app_context():
    #db.drop_all()
    db.create_all()
