import requests
import datetime

def get_questions(url_get, days, filter_tags):
    # промежуточные вычисления необходимые для нахождения верхней и нижней границ интервала
    # даты и времени создания вопросов с точностью до секунды
    to_datetime = datetime.datetime.today()
    today_date = datetime.date.today()
    time_start_today_date = datetime.time(0, 0)
    today_start_datetime = datetime.datetime.combine(today_date, time_start_today_date)
    delta_datetime = datetime.timedelta(days-1)
    from_datetime = today_start_datetime - delta_datetime

    # верхняя граница интервала даты и времи создания вопроса с точность до секунды
    end_datetime = int(to_datetime.timestamp())
    # нижняя граница интервала даты и времи создания вопроса с точность до секунды
    start_datetime = int(from_datetime.timestamp())

    # формирование параметров запроса и его отправка
    PARAMS_GET = {'fromdate': start_datetime, 'todate': end_datetime, 'tagged': filter_tags, 'site': 'stackoverflow', 'sort': 'creation'}
    resp = requests.get(url_get, params=PARAMS_GET)

    # печать вопросов соответствующих параметрам запроса
    for question in resp.json().get('items'):
        print(f'Вопрос: {question["title"]}')


if __name__ == '__main__':
    # инициализация констант
    URL = 'https://api.stackexchange.com/2.2/questions'
    DELTA_DAYS = 2
    TAGS = 'Python'

    # Вызов функции отбора и печати вопросов соответствующих условиям задачи
    get_questions(URL, DELTA_DAYS, TAGS)