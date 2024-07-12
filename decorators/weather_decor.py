import requests
from requests.exceptions import RequestException
import time

API_KEY = "DWEFDUWHRZ2DN4SAZ64QB6T9G"

def retry(func):
    def wrapper_retry(*args, **kwargs):
        retries = [5, 30]
        for seconds in retries:
            try:
                return func(*args, **kwargs)
            except RequestException:
                print(f"Failed to get data. Retrying in {seconds} seconds")
                time.sleep(seconds)
        return func(*args, **kwargs)
    return wrapper_retry

@retry
def get_weather_by_hours_from_api(*, date: str, city: str) -> list[dict]:
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/{date}/{date}?key={API_KEY}"
    response = requests.get(url=url)
    weather_by_days = response.json()["days"]
    weather_by_hours = weather_by_days[0]["hours"]
    return weather_by_hours

def fahrenheit_to_celsius(*, farenheit_temperature: float) -> int:
    return round((farenheit_temperature -32) * 5 / 9)

def get_dangeroues_uv_hours(*, weather_by_hour: list[dict]) -> list[dict]:
    dangeroust_uv_hours = []
    for weather in weather_by_hour:
        uv_index = weather["uvindex"]
        time = weather["datetime"]
        celsius_temperature = fahrenheit_to_celsius(farenheit_temperature=weather["temp"])
        if uv_index >= 3:
            dangeroust_uv_hours.append({"time": time, "uv_index": uv_index, "temperature": celsius_temperature})
    return dangeroust_uv_hours

date = "2024-07-12"
city = "Toronto, CA"
weather_by_hours = get_weather_by_hours_from_api(date=date, city=city)
dangerous_hours = get_dangeroues_uv_hours(weather_by_hour=weather_by_hours)
print(dangerous_hours)