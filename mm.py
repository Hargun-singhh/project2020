import requests
import json
import matplotlib.pyplot as plt

url = "https://api.covid19india.org/data.json"
response = requests.get(url)
# print(response.text)

# loads takes json and gives back python dictionary
covid_cases = json.loads(response.text)
# print(covid_cases)

covid_cases_statewise = covid_cases['statewise']
# print(covid_cases_time_series)

total_confirmed = []
for case in covid_cases_statewise:
    # data = int(case['totalconfirmed'])
    # print(data)
    total_confirmed.append(int(case['active']))

plt.barh(total_confirmed, )
plt.show()

# matplotlib assignment: draw graphs for all the states