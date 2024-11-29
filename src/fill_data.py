# Файл только для заполнения бд из json файла.
# Заполняются неизменяемые юзером значения (представления, инфа про сидения)

from src.models.tables.models import PerformancesTable, SeatsTable
from src import db, app
import json, random


def load_perfs():
    with open('Performances.json', encoding="utf8") as f:
        performances_json = json.load(f)
        for perf in performances_json:
            print(perf)
            perf = PerformancesTable(name=perf['name'], date=perf['date'], discription=perf['discription'],
                                     cover=perf['cover'])
            with app.app_context():
                db.session.add(perf)
                db.session.commit()

def load_seats():
    with open('seats.json', encoding='utf8') as f:
        seats_json = json.load(f)
        for seat in seats_json:
            seat = SeatsTable(seat_num=seat['seat_num'], price=seat['price'], performance_id=seat['performance_id'],
                              row_num=seat['row_num'], is_available=seat['is_available'])
            with app.app_context():
                db.session.add(seat)
                db.session.commit()

def gen_seats():
    for perf in PerformancesTable.query.all():
        for j in range (1, 2):
            for i in range (1, 21):
                seat = SeatsTable(
                seat_num = i,
                row_num = j,
                price = 300,
                performance_id = perf.id,
                is_available = bool(random.getrandbits(1)))
                db.session.add(seat)
    db.session.commit()

with app.app_context():
    #load_seats()
    load_perfs()
    gen_seats()
