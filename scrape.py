import requests
from bs4 import BeautifulSoup

date = '2023-07-13'
pitch_4 = '465'
pitch_3 = '466'
pitch_3a = '467'
pitch_3b = '468'


url = 'https://portal.sportskey.com/venues/tu-dublin-city-campus/facilities/{}/time_slots?date={}&mp=true'.format(pitch_4,date)
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup)
#pitch_4 = soup.find_all('div', class_='facility', id='facility_465')

week = soup.find_all('div',class_=['col', 'p-1'])
print(week[0])
#print(pitch_4[0].find_all('div',class_=['slots']))