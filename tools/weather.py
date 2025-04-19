# 檔案：tools/weather.py

import requests
from config import OPEN_WEATHER_API_KEY

def get_weather(city):
    params = {
        "q": city.lower(),
        "appid": OPEN_WEATHER_API_KEY,
        "units": "metric",  # 使用攝氏
        "lang": "zh_tw",    # 設定語言為繁體中文
    }

    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        return {
            "city": city,
            "temperature": temperature,
            "description": description,
            "humidity": humidity,
            "wind_speed": wind_speed,
            "api_key_used": OPEN_WEATHER_API_KEY,
        }
    else:
        return "❌ 無法取得天氣資料，請檢查城市名稱或 API 金鑰"