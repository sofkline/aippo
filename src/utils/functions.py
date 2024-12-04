from flask import flash, render_template
from email_validator import validate_email


def check_input(name, surname, email, activeSeats):
    if len(name) < 2 or len(surname) < 2:
        flash("Имя или фамилия введены некорректно!")
        return render_template('confirm.html', activeSeats=activeSeats)
        # Обработка неверной почты
    if email == '' or not validate_email(email):
        flash("Почта не существует!")
        return render_template('confirm.html', activeSeats=activeSeats)