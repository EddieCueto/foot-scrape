import requests
from datetime import datetime
from bs4 import BeautifulSoup


def dateStringToIntDay(date: str):
    data_tuple = tuple(map(int,date.split('-')))
    return datetime(*data_tuple).weekday()


getIndexes = lambda x, xs: [i for (y, i) in zip(xs, range(len(xs))) if x == y]


def getDaySubLists(week_list: list, day_dict: dict, current_day: int):
    week_indexes = []
    indexes = list(range(current_day,current_day+7))
    indexes = [i%7 for i in indexes]
    indexes = [day_dict[i] for i in indexes]
    for d in indexes:
        week_indexes.append(
            getIndexes(d,week_list)[0]
        )
    day_indexes = []
    for i in range(1,7):
        day_indexes.append(week_indexes[i-1:i+1])
    day_indexes.append([week_indexes[6]])
    week_list_per_day = []
    for t in day_indexes:
        if len(t) > 1:
            week_list_per_day.append(week_list[t[0]:t[1]])
        else:
            temp = week_list[t[0]:]
            rt = getIndexes('09:00',temp)
            if len(rt) < 2:
                week_list_per_day.append(temp[0:])
            else:
                week_list_per_day.append(temp[0:rt[1]])
    return week_list_per_day


date = '2023-07-06'
pitch_4 = '465'
pitch_3 = '466'
pitch_3a = '467'
pitch_3b = '468'
int_week_day = dateStringToIntDay(date)

day_dict = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}

week_day = day_dict[int_week_day]

url = 'https://portal.sportskey.com/venues/tu-dublin-city-campus/facilities/{}/time_slots?date={}&mp=true'.format(pitch_4,date)
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
text = soup.get_text()

text_split = text.split()

test = getDaySubLists(text_split, day_dict, int_week_day)

#pitch_4 = soup.find_all('div', class_='facility', id='facility_465')
#week = soup.find_all('div',class_=['col', 'p-1', week_day])
#print(week[0])
#print(pitch_4[0].find_all('div',class_=['slots']))