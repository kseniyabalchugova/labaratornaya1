from bs4 import BeautifulSoup
import requests
import transliterate
import re
def parser():
    url='https://omgtu.ru/general_information/faculties/'
    page = requests.get(url)
    print(page.status_code)  # смотрим ответ
    faculteti=[]
    soup = BeautifulSoup(page.text, "html.parser")  # передаем страницу в bs4
    faculteti = soup.findAll('div', id='pagecontent')  # находим  контейнер с нужным классом
    description = ''
    with open('file1.txt', 'w') as f:
        for data in faculteti:
            if data.find('a'):
                description = data.text
            f.write(description)
#бальчугова ксения ивт221