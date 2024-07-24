import requests
import re
import pandas as pd

DAYS_TO_PREDICT = ['1', '2', '3', '4', '5', '6', '7']

def scrape_weather():
    base_url = 'https://www.accuweather.com/en/th/bangkok/318849/evening-weather-forecast/318849?day='
    start = 0

    url_weather = f"{base_url}{DAYS_TO_PREDICT[start]}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Patterns for catching information from the system
    humidity_pattern = r'Humidity\s*<span class="value">(\d+)%</span>'
    precipitation_pattern = r'Probability of Precipitation\s*<span class="value">(\d+)%</span>'
    temperature_pattern = r'<div class=\"temperature\">(\d+)[^\d]*0;</div>'

    while url_weather:
        
        response = requests.get(url_weather, headers=headers)
        if response.status_code == 200:
            html_content = (response.text)
            
            humidity_match = int(re.search(humidity_pattern, html_content).group(1))
            precipitation_match = int(re.search(precipitation_pattern, html_content).group(1))
            
            temperature_match = re.findall(temperature_pattern, html_content)
            temp_max = temperature_match[0]
            temp_min = temperature_match[-1]
            temp_avg = temperature_match[2]

            # Update DataFrame at row
            df.at[start, 'humidity'] = humidity_match
            df.at[start, 'precipprob'] = precipitation_match
            df.at[start, 'tempmax'] = temp_max
            df.at[start, 'tempmin'] = temp_min
            df.at[start, 'temp'] = temp_avg

            start += 1

        if start >= len(DAYS_TO_PREDICT):
            url_weather = None 
            break
        url_weather = f"{base_url}{DAYS_TO_PREDICT[start]}"

def scrape_pressure():
    url_pressure = 'https://tides4fishing.com/th/thailand/bangkok/forecast/atmospheric-pressure'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url_pressure, headers=headers)

    max_pressure_pattern = r'<td class=\"f_datos_temp_text\">MAX\. PRESSURE<\/td>\s*<td class=\"f_dato_color\"><div class=\"f_dato_color1 f_tam1 f_gris_1 f_dato_font_small\">\s*(\d+) hPa\s*<\/div><\/td>'
    min_pressure_pattern = r'<td class=\"f_datos_temp_text\">MAX\. PRESSURE<\/td>\s*<td class=\"f_dato_color\"><div class=\"f_dato_color1 f_tam1 f_gris_1 f_dato_font_small\">\s*(\d+) hPa\s*<\/div><\/td>'

    if response.status_code == 200:
        html_content = (response.text)
        max_pressure_match = re.findall(max_pressure_pattern, html_content)
        min_pressure_match = re.findall(min_pressure_pattern, html_content)
        print(max_pressure_match, min_pressure_match)
        avg_pressures = [
            (int(max_pressure_match[i]) + int(min_pressure_match[i])) // 2
            for i in range(len(max_pressure_match))
        ]

        for i in range(0, len(min_pressure_match)):
            df.at[i, 'pressure'] = avg_pressures[i]

if __name__ == '__main__':
    columns = ['humidity', 'precipprob', 'tempmin', 'temp', 'tempmax', 'pressure']
    df = pd.DataFrame(columns=columns)
    scrape_weather()
    scrape_pressure()

    df.to_excel('ForecastedWeather.xlsx', index=False)
