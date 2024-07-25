import requests
from bs4 import BeautifulSoup
from collections import defaultdict

url = 'https://en.wikipedia.org/wiki/List_of_districts_of_Thailand'

response = requests.get(url)

province_district_dict = defaultdict(list)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    tables = soup.find_all('table', class_='wikitable')
    if tables:
        table = tables[0]  # Assuming the first wikitable is the desired one
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 3:
                district_name_tag = cols[0].find('a')
                province_name_tag = cols[2].find('a')
                
                if district_name_tag and province_name_tag:
                    district_name = district_name_tag.text
                    province_name = province_name_tag.text
                    province_district_dict[province_name].append(district_name)

# Print the dictionary
for province, districts in province_district_dict.items():
    print(f'Province: {province}, Districts: {districts}')
