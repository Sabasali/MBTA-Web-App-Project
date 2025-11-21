
import os
import json
import urllib.request
import urllib.parse
from dotenv import load_dotenv
import pprint

# Load environment variables
load_dotenv()
MAPBOX_TOKEN = os.getenv("MAPBOX_KEY")
MBTA_API_KEY = os.getenv("MBTA_API_KEY")
MAPBOX_BASE_URL = "https://api.mapbox.com/search/searchbox/v1/forward"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

if MAPBOX_TOKEN is None:
    raise RuntimeError("MAPBOX_TOKEN is not set. Check your .env file.")
if MBTA_API_KEY is None:
    raise RuntimeError("MBTA_API_KEY is not set. Check your .env file.")

def get_json(url: str) -> dict:
    """Fetch JSON data from a given URL."""
    with urllib.request.urlopen(url) as resp:
        response_text = resp.read().decode("utf-8")
        return json.loads(response_text)

def get_lat_lng(place_name: str) -> tuple[str, str]:
    """Use Mapbox to convert place name to latitude & longitude."""
    params = {
        "q": place_name,
        "access_token": MAPBOX_TOKEN
    }
    query_string = urllib.parse.urlencode(params)
    url = f"{MAPBOX_BASE_URL}?{query_string}"

    data = get_json(url)
    coords = data["features"][0]["geometry"]["coordinates"]  # [lon, lat]
    longitude, latitude = coords
    return str(latitude), str(longitude)

def get_nearest_station(latitude: str, longitude: str) -> tuple[str, str, bool]:
    """Return nearest MBTA stop name, stop ID, and wheelchair accessibility."""
    params = {
        "filter[latitude]": latitude,
        "filter[longitude]": longitude,
        "sort": "distance",
        "api_key": MBTA_API_KEY
    }
    query_string = urllib.parse.urlencode(params)
    url = f"{MBTA_BASE_URL}?{query_string}"

    mbta_data = get_json(url)
    stop_info = mbta_data["data"][0]
    stop_id = stop_info["id"]
    station_name = stop_info["attributes"]["name"]
    wheelchair_accessible = stop_info["attributes"]["wheelchair_boarding"] == 1
    return station_name, stop_id, wheelchair_accessible

def get_next_arrival(stop_id: str) -> str:
    """Fetch the next arrival time from the MBTA predictions API."""
    url = f"https://api-v3.mbta.com/predictions?filter[stop]={stop_id}&sort=arrival_time&api_key={MBTA_API_KEY}"
    data = get_json(url)
    if not data["data"]:
        return "No upcoming trains/buses"
    return data["data"][0]["attributes"]["arrival_time"]

def find_stop_near(place_name: str) -> tuple[str, bool, str]:
    """Returns nearest station name, accessibility, and next arrival time."""
    lat, lng = get_lat_lng(place_name)
    station_name, stop_id, wheelchair = get_nearest_station(lat, lng)
    arrival_time = get_next_arrival(stop_id)
    return station_name, wheelchair, arrival_time


# Test the functions
if __name__ == "__main__":
    print(find_stop_near("Boston Common"))
    print(get_lat_lng("Boston Common"))




