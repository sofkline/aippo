# Файл только для заполнения бд из json файла.
# Заполняются неизменяемые юзером значения (представления, инфа про сидения)

from src.models.tables.models import PerformancesTable
from src import db, app
import json


with open('Performances.json', encoding="utf8") as f:
    performances_json = json.load(f)
    for perf in performances_json:
        perf = PerformancesTable(name=perf['name'], date=perf['date'])
        with app.app_context():
            db.session.add(perf)
            db.session.commit()
