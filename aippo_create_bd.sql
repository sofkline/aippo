-- Создание таблицы theatres
CREATE TABLE theatres (
                          id SERIAL PRIMARY KEY,
                          th_name VARCHAR(255) NOT NULL,
                          th_place VARCHAR(255) NOT NULL
);

-- Создание таблицы hall
CREATE TABLE hall (
                      id SERIAL PRIMARY KEY,
                      th_id INTEGER,
                      place_count INTEGER NOT NULL,
                      FOREIGN KEY (th_id) REFERENCES theatres(id) ON DELETE CASCADE
);

-- Создание таблицы performances
CREATE TABLE performances (
                              id SERIAL PRIMARY KEY,
                              perf_name VARCHAR(255) NOT NULL,
                              hall_id INTEGER,
                              perf_date DATE NOT NULL,
                              perf_time TIME NOT NULL,
                              FOREIGN KEY (hall_id) REFERENCES hall(id) ON DELETE CASCADE
);

-- Создание таблицы seats
CREATE TABLE seats (
                       id SERIAL PRIMARY KEY,
                       perf_id INTEGER,
                       row INTEGER NOT NULL,
                       seat INTEGER NOT NULL,
                       price INTEGER NOT NULL,
                       is_available BOOLEAN NOT NULL,
                       FOREIGN KEY (perf_id) REFERENCES performances(id) ON DELETE CASCADE
);

-- Создание таблицы tickets
CREATE TABLE tickets (
                         id SERIAL PRIMARY KEY,
                         seat_id INTEGER,
                         ticket_date DATE NOT NULL,
                         ticket_time TIME NOT NULL,
                         FOREIGN KEY (seat_id) REFERENCES seats(id) ON DELETE CASCADE
);

-- Создание таблицы client
CREATE TABLE client (
                        id SERIAL PRIMARY KEY,
                        ticket_id INTEGER,
                        name VARCHAR(255) NOT NULL,
                        surname VARCHAR(255) NOT NULL,
                        patronymic VARCHAR(255) NULL,
                        FOREIGN KEY (ticket_id) REFERENCES tickets(id) ON DELETE CASCADE
);

