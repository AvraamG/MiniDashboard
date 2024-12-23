import os
import requests

weather_api_key = os.getenv("Weather_key")

def update_geolocation():
    try:
        # Geolocation API endpoint
        response = requests.get("http://ip-api.com/json/")
        if response.status_code == 200:
            data = response.json()
            city = data["city"]
            region = data["regionName"]
            country = data["country"]
            lat = data["lat"]
            lon = data["lon"]
            return {"city": city, "region": region, "country": country, "lat": lat, "lon": lon}
        else:
            return None
    except Exception as e:
        print(f"Error fetching geolocation: {e}")
        return None

def get_weather():
    location = update_geolocation()
    if not location:
        print("Geolocation update failed. Using default location.")
        return None, None, None, None

    # Use city name or latitude and longitude for WeatherAPI
    city = location["city"]
    # Alternative: lat_lon = f'{location["lat"]},{location["lon"]}'

    url = f"http://api.weatherapi.com/v1/forecast.json"
    params = {
        "key": weather_api_key,
        "q": city,  # Use city or lat_lon here
        "days": 2,
        "aqi": "no",
        "alerts": "no",
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for HTTP codes >= 400
        data = response.json()

        # Extract current weather
        current_temp = data["current"]["temp_c"]
        # Extract tomorrow's forecast
        tomorrow_forecast = data["forecast"]["forecastday"][1]["day"]["condition"]["text"]
        tomorrow_max_temp = data["forecast"]["forecastday"][1]["day"]["maxtemp_c"]
        tomorrow_min_temp = data["forecast"]["forecastday"][1]["day"]["mintemp_c"]

        return current_temp, tomorrow_forecast, tomorrow_max_temp, tomorrow_min_temp

    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None, None, None, None