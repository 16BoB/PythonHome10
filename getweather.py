import requests
from bs4 import BeautifulSoup as bs

url = ['https://pogoda.mail.ru/prognoz/moskva/', 'https://pogoda.mail.ru/prognoz/ufa/']

def request_weather(arr_url):
    response = requests.get(arr_url).text
    soup = bs(response, 'html.parser')
    temperature = soup.find('div', class_="information__content__temperature").get_text(strip=True)
    return temperature