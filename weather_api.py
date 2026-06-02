from flask import Flask, request, jsonify
import requests
app= Flask(__name__)

@app.route("/")
def home():
    return "Weather API is running 🌦️"

@app.route("/weather")
def weather():
    lat=request.args.get("lat")
    lon=request.args.get("lon")

    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m,weather_code"

    response=requests.get(url)
    data= response.json()
    temp = data["current"]["temperature_2m"]
    wind = data["current"]["wind_speed_10m"]
    code = data["current"]["weather_code"]

    return jsonify({
        "temperature": temp,
        "wind_speed": wind,
        "weather_code":code
    })



if __name__== "__main__":
    app.run(debug=True)
