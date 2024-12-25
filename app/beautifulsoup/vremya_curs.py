import requests
from bs4 import BeautifulSoup
from datetime import datetime


def clock():
    clock = datetime.now().strftime('%I:%M:%S %p')
    return clock


def cursval():

    url = 'https://www.cbr.ru/'

    response = requests.get(url)

    curs = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        lst = soup.findAll('div', class_='main-indicator_rate')
        curs = lst[1].text.strip()
    return curs

# print(clock())
# print(cursval())