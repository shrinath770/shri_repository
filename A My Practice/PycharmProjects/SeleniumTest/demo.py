import requests
from bs4 import BeautifulSoup

page=requests.get("https://digital.weather.gov/")
soup= BeautifulSoup(page.content,'html.parser')
week=soup.find(id='seven-day-forecast-body')
print(week)