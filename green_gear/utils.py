import re


def calculate_reading_time(text):
    # Очистка текста от HTML-тегов
    clean_text = re.sub('<.*?>', '', text)
    # Подсчет количества слов
    word_count = len(clean_text.split())
    # Средняя скорость чтения в словах в минуту
    average_reading_speed = 200  # Примерное значение
    # Вычисление времени на чтение
    reading_time_minutes = word_count / average_reading_speed
    return round(reading_time_minutes)
