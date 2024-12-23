import os

location="Drama"
weather_api_key = os.getenv("Weather_key")
import requests

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

# Example Usage
dynamic_location = update_geolocation()
if dynamic_location:
    print(f"City: {dynamic_location['city']}, Country: {dynamic_location['country']}")
    print(f"Latitude: {dynamic_location['lat']}, Longitude: {dynamic_location['lon']}")
    location = dynamic_location['city']
else:
    print("Failed to fetch geolocation.")


def get_weather():
    update_geolocation()
    import requests
    url = f"http://api.weatherapi.com/v1/forecast.json?key={weather_api_key}&q={location}&days=2&aqi=no&alerts=no"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Extract current weather
        current_temp = data["current"]["temp_c"]
        # Extract tomorrow's forecast
        tomorrow_forecast = data["forecast"]["forecastday"][1]["day"]["condition"]["text"]
        tomorrow_max_temp = data["forecast"]["forecastday"][1]["day"]["maxtemp_c"]
        tomorrow_min_temp = data["forecast"]["forecastday"][1]["day"]["mintemp_c"]
        return current_temp, tomorrow_forecast, tomorrow_max_temp, tomorrow_min_temp
    else:
        return None, None, None, None