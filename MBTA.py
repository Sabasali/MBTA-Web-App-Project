

import os
import json
import urllib.request
import urllib.parse
import pprint
from dotenv import load_dotenv

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


# Encode the query properly
query = "Babson College"
encoded_query = urllib.parse.quote(query)  # Encodes spaces and special characters
url = f"{MAPBOX_BASE_URL}?q={encoded_query}&access_token={MAPBOX_TOKEN}"

print(url)  # Try this URL in your browser first

# Fetch and parse JSON response
with urllib.request.urlopen(url) as resp:
    response_text = resp.read().decode("utf-8")
    response_data = json.loads(response_text)
    pprint.pprint(response_data)

# Function 1: get_json(url)
# ---------------------------
def get_json(url: str) -> dict:
    """Fetch JSON data from a given URL."""
    with urllib.request.urlopen(url) as resp:
        response_text = resp.read().decode("utf-8")
        return json.loads(response_text)
    
def get_lat_lng(place_name: str) -> tuple[str, str]:
    
# Build the URL using urlencode for proper encoding
    params = {
        "q": place_name,
        "access_token": MAPBOX_TOKEN
    }
    query_string = urllib.parse.urlencode(params)
    url = f"{MAPBOX_BASE_URL}?{query_string}"
    # Fetch JSON response
    data = get_json(url)
    
# Extract coordinates [lon, lat]
    coords = data["features"][0]["geometry"]["coordinates"]
    longitude, latitude = coords
    return str(latitude), str(longitude)

def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """Return (station_name, wheelchair_accessible) for nearest MBTA station."""
    params = {
        "filter[latitude]": latitude,
        "filter[longitude]": longitude,
        "sort": "distance",
        "api_key": MBTA_API_KEY
    }
    query_string = urllib.parse.urlencode(params)
    url = f"{MBTA_BASE_URL}?{query_string}"
    mbta_data = get_json(url)
    stop = mbta_data["data"][0]["attributes"]
    stop_name = stop["name"]
    wheelchair_accessible = stop["wheelchair_boarding"] == 1
    return stop_name, wheelchair_accessible

def find_stop_near(place_name: str) -> tuple[str, bool]:
    """Combine both APIs: Mapbox for coordinates, MBTA for nearest stop."""
    lat, lng = get_lat_lng(place_name)
    return get_nearest_station(lat, lng)

# Test the functions
if __name__ == "__main__":
    print(find_stop_near("Boston Common"))
    print(get_lat_lng("Boston Common"))  # Should return (lat, lng)
    print(find_stop_near("Fenway Park"))

