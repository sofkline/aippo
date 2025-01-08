from src.models.tables.models import *
from src import db


class dbHelper:
    def addPerf(self, name, age_restriction, cover):
        new_perf = Performance(name=name, age_restriction=age_restriction, cover=cover)
        print('222')
        db.session.add(new_perf)
        db.session.commit()
        return new_perf

    def getAllPerfs(self):
        try:
            perfs = Performance.query.all()
            print(f"Полученные представления {perfs}")
            if perfs: return perfs
            else:
                print("Нет представлений в базе данных.")
                return []
        except Exception as e:
            print('getAllPerfs ОШИБКА: ', e)

    def getAllShowsByPerfID(self, perf_id):
        try:
            shows = Show.query.filter_by(performance_id=perf_id).all()
            if shows: return shows
        except Exception as e:
            print('Ошибка: ', e)


    #def getSeatsForPerf(self, perf_id):
    #    try:
    #        seats = SeatsTable.query.filter_by(performance_id=perf_id).all()
    #        if seats: return seats
    #    except:
    #        print('getSeatsForPerf: Ошибка чтения из БД')
    #    return []
#
    #def addTicket(self, seat_id, client_id):
    #    try:
    #        ticket = TicketsTable.query.filter_by(seat_id=seat_id, client_id=client_id).first()
    #        if ticket is None:
    #            ticket = TicketsTable(seat_id=seat_id, client_id=client_id)
    #            SeatsTable.query.filter_by(id=seat_id).update({SeatsTable.is_available: False})
    #            db.session.add(ticket)
    #            db.session.commit()
    #        else:
    #            print('addTicket: Билет уже есть в БД.')
    #    except:
    #        print('addTicket: Ошибка добавления')
#
#
    #def addClient(self, name, surname, email):
    #    try:
    #        client = ClientsTable.query.filter_by(name=name, surname=surname, email=email).first()
    #        if client is None:
    #            client = ClientsTable(name=name, surname=surname, email=email)
    #            db.session.add(client)
    #            db.session.commit()
    #        else:
    #            print('addClient: Пользователь уже есть в БД.')
    #    except:
    #        print('addClient: Ошибка добавления')
    #    return []
#
    #def getClientIdByEmail(self, email):
    #    try:
    #        client = ClientsTable.query.filter_by(email=email).all()
    #        client_id = client[0].id
    #        if client_id: return client_id
    #    except:
    #        print('getClientIdByEmail: Ошибка выборки')
    #    return []
#
    #def getClientById(self, id):
    #    try:
    #        client = ClientsTable.query.filter_by(id=id).first()
    #        if client: return client
    #    except:
    #        print('getClientById: Ошибка чтения из БД')
    #    return []
#
    #def getInfoBySeatId(self, id):
    #    try:
    #        seat_info = SeatsTable.query.filter_by(id=id).first()
    #        seat_num = seat_info.seat_num
    #        perf = PerformancesTable.query.filter_by(id=seat_info.performance_id).first()
    #        perf_name = perf.name
    #        info = {'seat_num': seat_num,
    #                'perf_name': perf_name}
    #        return info
    #    except:
    #        print('getSeatInfoById: Ошибка чтения из БД')
    #    return []
#
#
    #def getTicketsInfo(self):
    #    try:
    #        res = []
    #        tickets = TicketsTable.query.all()
    #        for ticket in tickets:
    #            client = ClientsTable.query.filter_by(id=ticket.client_id).first()
    #            seat = SeatsTable.query.filter_by(id=ticket.seat_id).first()
    #            client_name = client.name
    #            client_surname = client.surname
    #            client_email = client.email
    #            seat_num = seat.seat_num
    #            perf = PerformancesTable.query.filter_by(id=seat.performance_id).first()
    #            perf_name = perf.name
    #            data = {'client_name': client_name,
    #                    'client_surname': client_surname,
    #                    'client_email': client_email,
    #                    'seat_num': seat_num,
    #                    'perf_name': perf_name}
    #            res.append(data)
    #        if res: return res
    #    except:
    #        print('Какая то ошибка...')
    #    return []