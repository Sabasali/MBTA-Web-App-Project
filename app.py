from flask import Flask, render_template, request
from MBTA import get_lat_lng, get_nearest_station, get_next_arrival
from dotenv import load_dotenv

# Initialize Flask app
app = Flask(__name__)

# Load environment variables
load_dotenv()

@app.route("/", methods=["GET", "POST"])
def home():
    # Initialize variables for template
    place = station_name = lat = lon = arrival = None
    wheelchair = None
    error = None

    if request.method == "POST":
        place = request.form.get("place", "").strip()

        try:
            if not place:
                raise ValueError("Please enter a location.")

            # Get coordinates from Mapbox
            lat, lon = get_lat_lng(place)

            # Get nearest MBTA station
            station_name, stop_id, wheelchair = get_nearest_station(lat, lon)

            # Get next arrival time
            arrival = get_next_arrival(stop_id)

        except Exception as e:
            error = f"Error: {str(e)}"

    return render_template(
        "index.html",
        place=place,
        station_name=station_name,
        lat=lat,
        lon=lon,
        wheelchair=wheelchair,
        arrival=arrival,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True)