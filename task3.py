# Задача 3. Планирование задач

from datetime import datetime, timedelta


def future_date(days_from_now):
    
    # Получение текущей даты и времени
    today = datetime.now()
    # Вычисление даты через указанное количество дней
    future_date = today + timedelta(days=days_from_now)
    # Форматирование будущей даты в строку в формате YYYY-MM-DD
    formatted_future_date = future_date.strftime('%Y-%m-%d')
    return formatted_future_date


if __name__ == '__main__':
    days = 33  # Количество дней для вычисления
    print(f'{days} дня от текущей даты: {future_date(days)}')