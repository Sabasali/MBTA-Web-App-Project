from flask import Flask, render_template, request
from MBTA import find_stop_near, get_lat_lng
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Load environment variables
load_dotenv()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        place = request.form.get("place")

        if not place:
            return render_template("index.html", error="Please enter a place.")

        # Use your MBTA.py functions (clean and consistent)
        try:
            stop_name, wheelchair = find_stop_near(place)
            lat, lon = get_lat_lng(place)
        except Exception as e:
            return render_template("index.html", place=place, error=str(e))
        return render_template(
            "index.html",
            place=place,
            stop=stop_name,
            lat=lat,
            lon=lon,
            wheelchair=wheelchair
        )

    # GET request
    return render_template("index.html")
    

if __name__ == '__main__':
    app.run(debug=True)