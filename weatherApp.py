from flask import Flask, request, jsonify
import requests
import time

app = Flask(__name__)

API_KEY = "560b182fba3a19682df6753868be4f1d"

@app.route("/weather", methods=["GET"])
def get_weather():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "City is required"}), 400

    api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    json_data = requests.get(api).json()

    if json_data.get("cod") != 200:
        return jsonify({"error": "City not found"}), 404

    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise']))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset']))

    return jsonify({
        "city": city,
        "condition": condition,
        "temp": temp,
        "min_temp": min_temp,
        "max_temp": max_temp,
        "pressure": pressure,
        "humidity": humidity,
        "wind_speed": wind,
        "sunrise": sunrise,
        "sunset": sunset
    })
