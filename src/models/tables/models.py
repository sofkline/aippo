from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Theater(db.Model):
    __tablename__ = 'theaters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255))
    box_office_address = db.Column(db.String(255))
    halls = db.relationship('Hall', backref='theater', lazy=True)

    def repr(self):
        return f"<Theater(id={self.id}, name='{self.name}')>"


class Hall(db.Model):
    __tablename__ = 'halls'
    id = db.Column(db.Integer, primary_key=True)
    theater_id = db.Column(db.Integer, db.ForeignKey('theaters.id'), nullable=False)
    name = db.Column(db.String(255))
    capacity = db.Column(db.Integer)
    seats = db.relationship('Seat', backref='hall', lazy=True)

    def repr(self):
        return f"<Hall(id={self.id}, theater_id={self.theater_id}, name='{self.name}', capacity={self.capacity})>"


class Seat(db.Model):
    __tablename__ = 'seats'
    id = db.Column(db.Integer, primary_key=True)
    hall_id = db.Column(db.Integer, db.ForeignKey('halls.id'), nullable=False)
    row = db.Column(db.Integer)
    seat_number = db.Column(db.Integer)
    section = db.Column(db.String(255))
    price = db.Column(db.Numeric(10, 2))

    def repr(self):
        return f"<Seat(id={self.id}, hall_id={self.hall_id}, row={self.row}, seat_number={self.seat_number}, section='{self.section}', price={self.price})>"


class Actor(db.Model):
    __tablename__ = 'actors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(255))
    performance = db.Column(db.String(255))
    troupe_id = db.Column(db.Integer, db.ForeignKey('troupes.id'))

    def repr(self):
        return f"<Actor(id={self.id}, name='{self.name}', role='{self.role}')>"


class Troupe(db.Model):
    __tablename__ = 'troupes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    number_of_members = db.Column(db.Integer)
    actors = db.relationship('Actor', backref='troupe', lazy=True)
    salary = db.relationship('Salary', backref='troupe', lazy=True)

    def repr(self):
        return f"<Troupe(id={self.id}, name='{self.name}', number_of_members={self.number_of_members})>"


class Performance(db.Model):
    __tablename__ = 'performances'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    age_restriction = db.Column(db.Integer)
    shows = db.relationship('Show', backref='performance', lazy=True)
    cover = db.Column(db.String(50), nullable=False, default='default.jpg')

    def repr(self):
        return f"<Performance(id={self.id}, name='{self.name}', age_restriction={self.age_restriction})>"


class Show(db.Model):
    __tablename__ = 'shows'
    id = db.Column(db.Integer, primary_key=True)
    performance_id = db.Column(db.Integer, db.ForeignKey('performances.id'), nullable=False)
    show_time = db.Column(db.Time)
    show_date = db.Column(db.Date)
    tickets = db.relationship('Ticket', backref='show', lazy=True)

    def repr(self):
        return f"<Show(id={self.id}, performance_id={self.performance_id}, show_time={self.show_time}, show_date={self.show_date})>"


class Ticket(db.Model):
    __tablename__ = 'tickets'
    id = db.Column(db.Integer, primary_key=True)
    show_id = db.Column(db.Integer, db.ForeignKey('shows.id'), nullable=False)
    purchase_time = db.Column(db.DateTime)
    seat_id = db.Column(db.Integer, db.ForeignKey('seats.id'))
    buyer_name = db.Column(db.String(255))
    visitor_name = db.Column(db.String(255))
    visitor_dob = db.Column(db.Date)
    quantity = db.Column(db.Integer)

    def repr(self):
        return f"<Ticket(id={self.id}, show_id={self.show_id}, purchase_time={self.purchase_time}, seat_id={self.seat_id}, buyer_name='{self.buyer_name}')>"


class Salary(db.Model):
    __tablename__ = 'salaries'
    id = db.Column(db.Integer, primary_key=True)
    actor_id = db.Column(db.Integer, db.ForeignKey('actors.id'), nullable=False)
    salary_amount = db.Column(db.Numeric(10, 2))
    
    def repr(self):
        return f"<Salary(id={self.id}, actor_id={self.actor_id}, salary_amount={self.salary_amount})>"