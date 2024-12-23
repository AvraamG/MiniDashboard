import requests
import os

# Load API key
maps_api_key = os.getenv("Map_key")
if not maps_api_key:
    raise ValueError("Google_Api_Key environment variable not set.")

# Define origin and destination
my_origin = os.getenv("origin_key")
my_destination = os.getenv("destination_key")

def get_traffic_info():
    """
    Fetch traffic info and drive duration between two locations.
    """
    url = "https://maps.googleapis.com/maps/api/distancematrix/json"
    params = {
        "origins": my_origin,
        "destinations": my_destination,
        "departure_time": "now",  # Fetch real-time traffic data
        "key": maps_api_key,
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for HTTP error codes

        data = response.json()

        # Check for a valid response
        if data.get("status") != "OK":
            raise ValueError(f"API error: {data.get('error_message', 'Unknown error')}")

        # Extract duration and duration_in_traffic
        element = data["rows"][0]["elements"][0]
        if element["status"] == "OK":
            duration = element["duration"]["text"]
            duration_in_traffic = element.get("duration_in_traffic", {}).get("text", "N/A")
            return duration, duration_in_traffic
        else:
            raise ValueError(f"Element status error: {element['status']}")

    except Exception as e:
        print(f"Error fetching traffic info: {e}")
        return None, None
