from unittest.mock import patch, MagicMock
from src.repo.rep import dbHelper
from src import app


def test_getAllPerfs():
    with app.app_context():

        mock_perf1 = MagicMock()
        mock_perf1.id = 1
        mock_perf1.name = 'Нос'
        mock_perf1.date = '2024-01-01'

        mock_perf2 = MagicMock()
        mock_perf2.id = 2
        mock_perf2.name = 'Лебединое озеро'
        mock_perf2.date = '2024-02-01'

        with patch('src.models.tables.models.PerformancesTable.query') as mock_querry:
            mock_querry.all.return_value = [mock_perf1, mock_perf2]

            helper = dbHelper()
            result = helper.getAllPerfs()

            assert len(result) == 2
            assert result[0].name == "Нос"
            assert result[1].name == "Лебединое озеро"

def test_get_seats_for_perf():
    with app.app_context():
        # Настройка мок-объектов
        mock_seat1 = MagicMock()
        mock_seat1.id = 1
        mock_seat1.seat_num = 101
        mock_seat1.row_num = 1
        mock_seat1.performance_id = 1

        mock_seat2 = MagicMock()
        mock_seat2.id = 2
        mock_seat2.seat_num = 102
        mock_seat2.row_num = 1
        mock_seat2.performance_id = 1

        with patch('src.models.tables.models.SeatsTable.query') as mock_query:
            # Настройка метода filter_by
            mock_filter = mock_query.filter_by.return_value
            mock_filter.all.return_value = [mock_seat1, mock_seat2]

            helper = dbHelper()
            result = helper.getSeatsForPerf(1)

            # Проверяем результат
            assert len(result) == 2
            assert result[0].seat_num == 101
            assert result[1].seat_num == 102
            assert result[0].performance_id == 1
            assert result[1].performance_id == 1


def test_add_ticket():
    with app.app_context():
        with patch('src.models.tables.models.TicketsTable.query') as mock_ticket_query, \
             patch('src.models.tables.models.SeatsTable.query') as mock_seat_query, \
             patch('src.repo.rep.db.session') as mock_session:

            # Настройка поведения моков
            mock_ticket_query.filter_by.return_value.first.return_value = None
            mock_seat_query.filter_by.return_value.update.return_value = 1
            mock_ticket = MagicMock()
            mock_session.add.return_value = None
            mock_session.commit.return_value = None

            helper = dbHelper()
            helper.addTicket(1, 2)

            # Проверки
            mock_ticket_query.filter_by.assert_called_with(seat_id=1, client_id=2)
            mock_seat_query.filter_by.assert_called_with(id=1)
            mock_session.add.assert_called()
            mock_session.commit.assert_called()


def test_add_ticket_existing():
    with app.app_context():
        with patch('src.models.tables.models.TicketsTable.query') as mock_ticket_query, \
                patch('src.models.tables.models.SeatsTable.query') as mock_seat_query, \
                patch('src.repo.rep.db.session') as mock_session:

            # Создаем фейковый объект билета (имитируем, что он уже существует)
            mock_ticket = MagicMock()
            mock_ticket_query.filter_by.return_value.first.return_value = mock_ticket

            # Настраиваем SeatsTable, но вызовы не должны происходить
            mock_seat_query.filter_by.return_value.update.return_value = None

            # Мокаем методы добавления и коммита
            mock_session.add.return_value = None
            mock_session.commit.return_value = None

            # Тестируем метод addTicket
            helper = dbHelper()
            helper.addTicket(1, 2)

            # Проверки
            mock_ticket_query.filter_by.assert_called_with(seat_id=1, client_id=2)  # Проверяем вызов для билета
            mock_seat_query.filter_by.assert_not_called()  # Проверяем, что SeatsTable не трогается
            mock_session.add.assert_not_called()  # Никаких операций добавления
            mock_session.commit.assert_not_called()  # Никаких операций коммита


def test_add_client():
    with app.app_context():
        with patch('src.models.tables.models.ClientsTable.query') as mock_client_query, \
             patch('src.repo.rep.db.session') as mock_session:

            # Настройка поведения моков
            mock_client_query.filter_by.return_value.first.return_value = None
            mock_client = MagicMock()
            mock_session.add.return_value = None
            mock_session.commit.return_value = None

            helper = dbHelper()
            helper.addClient('Андрей', 'Попов', 'asd.@example.com')

            # Проверки
            mock_client_query.filter_by.assert_called_with(name='Андрей', surname='Попов', email='asd.@example.com')
            mock_session.add.assert_called()
            mock_session.commit.assert_called()

def test_get_client_id_by_email():
    with app.app_context():
        with patch('src.models.tables.models.ClientsTable.query') as mock_client_query:
            mock_client = MagicMock(id=123)
            mock_client_query.filter_by.return_value.all.return_value = [mock_client]

            helper = dbHelper()
            client_id = helper.getClientIdByEmail('asd.@example.com')

            # Проверки
            mock_client_query.filter_by.assert_called_with(email='asd.@example.com')
            assert client_id == 123

def test_get_client_by_id():
    with app.app_context():
        with patch('src.models.tables.models.ClientsTable.query') as mock_client_query:
            mock_client = MagicMock()
            mock_client.id = 1
            mock_client.name = 'Андрей'
            mock_client.surname = 'Попов'
            mock_client.email = 'asd.@example.com'
            mock_client_query.filter_by.return_value.first.return_value = mock_client

            helper = dbHelper()
            client = helper.getClientById(1)

            # Проверки
            mock_client_query.filter_by.assert_called_with(id=1)
            assert client.id == 1
            assert client.name == 'Андрей'

def test_get_info_by_seat_id():
    with app.app_context():
        with patch('src.models.tables.models.SeatsTable.query') as mock_seat_query, \
             patch('src.models.tables.models.PerformancesTable.query') as mock_perf_query:

            mock_seat = MagicMock()
            mock_seat.seat_num = 101
            mock_seat.performance_id = 1
            mock_perf = MagicMock()
            mock_perf.name = 'Нос'

            mock_seat_query.filter_by.return_value.first.return_value = mock_seat
            mock_perf_query.filter_by.return_value.first.return_value = mock_perf

            helper = dbHelper()
            info = helper.getInfoBySeatId(1)

            # Проверки
            assert info['seat_num'] == 101
            assert info['perf_name'] == 'Нос'

def test_get_tickets_info():
    with app.app_context():
        with patch('src.models.tables.models.TicketsTable.query') as mock_tickets_query, \
             patch('src.models.tables.models.ClientsTable.query') as mock_client_query, \
             patch('src.models.tables.models.SeatsTable.query') as mock_seat_query, \
             patch('src.models.tables.models.PerformancesTable.query') as mock_perf_query:

            # Настройка мок-объектов
            mock_ticket = MagicMock()
            mock_ticket.client_id = 1
            mock_ticket.seat.id = 1
            mock_client = MagicMock()
            mock_client.name = 'Андрей'
            mock_client.surname = 'Попов'
            mock_client.email = 'asd.@example.com'
            mock_seat = MagicMock()
            mock_seat.seat_num = 101
            mock_seat.performance_id = 1
            mock_perf = MagicMock()
            mock_perf.name = 'Нос'

            # Настройка возвращаемых значений
            mock_tickets_query.all.return_value = [mock_ticket]
            mock_client_query.filter_by.return_value.first.return_value = mock_client
            mock_seat_query.filter_by.return_value.first.return_value = mock_seat
            mock_perf_query.filter_by.return_value.first.return_value = mock_perf

            helper = dbHelper()
            tickets_info = helper.getTicketsInfo()

            # Проверки
            assert len(tickets_info) == 1
            assert tickets_info[0]['client_name'] == 'Андрей'
            assert tickets_info[0]['seat_num'] == 101
            assert tickets_info[0]['perf_name'] == 'Нос'