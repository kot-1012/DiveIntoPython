# Задача 2. Работа с текущим временем и датой

from datetime import datetime


def display_current_datetime():
    # Получение текущего времени и даты
    now = datetime.now()
    # Форматирование даты и времени
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
    # Получение дня недели и номера недели
    day_of_week = now.strftime('%A')
    week_number = now.isocalendar()[1]
    print(f'Текущая дата: {formatted_date}')
    print(f'День недели: {day_of_week}')
    print(f'Номер недели: {week_number}')


if __name__ == '__main__':
    display_current_datetime()