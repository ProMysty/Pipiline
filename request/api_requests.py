import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

if not api_key:
    print("API_KEY is not set")

api_url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q=Philippines&aqi=no"

def data_fetch():
    print("fetching data.")
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        print("Data fetching completed.")
        return response.json()
    
    except requests.exceptions.RequestException as e:
        print("Data fetching failed.")
        raise

def mock_data():
    return {'location': {'name': 'Manila', 'region': 'Manila', 'country': 'Philippines', 'lat':14.604, 'lon': 120.982, 'tz_id': 'Asia/Manila', 'localtime_epoch': 1790587438, 'localtime': '2026-09-28 17:23'}, 'current': {'last_updated_epoch': 1790586900, 'last_updated': '2026-09-28 17:15', 'temp_c': 29.6, 'temp_f': 85.2, 'is_day': 1, 'condition': {'text': 'Patchy rain nearby', 'icon': '//cdn.weatherapi.com/weather/64x64/day/176.png', 'code': 1063}, 'wind_mph': 10.1, 'wind_kph': 16.2, 'wind_degree': 240, 'wind_dir':'WSW', 'pressure_mb': 1011.0, 'pressure_in': 29.85, 'precip_mm': 0.01, 'precip_in': 0.0, 'humidity': 70, 'cloud': 99, 'feelslike_c': 34.0, 'feelslike_f': 93.2, 'windchill_c': 29.6, 'windchill_f': 85.2, 'heatindex_c': 34.0, 'heatindex_f': 93.2, 'dewpoint_c': 23.5, 'dewpoint_f': 74.2, 'vis_km': 10.0, 'vis_miles': 6.0, 'uv': 0.4, 'gust_mph': 10.1, 'gust_kph': 16.2, 'will_it_rain': 0, 'chance_of_rain': 18, 'will_it_snow': 0,'chance_of_snow': 0, 'wetbulb_c': 25.1, 'wetbulb_f': 77.2, 'short_rad': 418.34, 'diff_rad': 168.56, 'dni': 0.0, 'gti': 0.0}}

mock_data()

