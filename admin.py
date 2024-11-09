from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import unittest


#импорт бд
#import 

#изменение данных бд
def db_change(seat_data:list):
    print()

#покупка места
def buy_seat(seat_data:list):
    print()

#проверка существаования места
def check_seat(seat_data:list):
    print()

#проверка почты
def check_email(user_email: str):
    print("hello world")

#отправка билета
def send_ticket(user_email:str, seat_data:list):
    print()


def check_session(session_id: str):
		# Проверяем на непустую сессию
    if session_id:
        for session in SESSIONS:
            if session["id"] == session_id:
                break  # Мы нашли сессию, прерываем цикл
        else:
            # Сюда мы попадём, если конструкцию break не выполнится, т.е. сессия не найдётся
            return {
                "error": "Сессия с таким айди не существует на сервере. Авторизуйтесь снова"
            }
    else:
        # Клиент не указал сессию при отправке данных
        return {
            "error": "Вы не авторизованы!"
        }


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SESSIONS = []


@app.get("/echo")
def echo(message: str, session: str = None):
    # Вызываем функцию, для проверки существования сессии
    error = check_session(session)
    # Если функция вернула ошибку, то возвращаем её клиенту
    if error:
        return error

    return {"data": message}


@app.get("/history")
def history(session: str = None):
    # Вызываем функцию, для проверки существования сессии
    error = check_session(session)
    # Если функция вернула ошибку, то возвращаем её клиенту
'''   if error:
        return error
    for _session in SESSIONS:        
            if _session["id"] == session:
                for user in USERS:
                    if user["username"] == _session["username"]:
                        
                        return {"data": user["history"]} '''
