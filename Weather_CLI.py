import requests
import sys

try:
    lat= float(sys.argv[1])
    lon= float(sys.argv[2])
    weather_description={

        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Fog",
        61: "Light rain",
        63: "Moderate rain",
        65: "Heavy rain",
}

    url=f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m,weather_code"

    response= requests.get(url)
    if response.status_code!=200:
        print(" ❌ API error")
        sys.exit()
    data=response.json()
    print('''╔══════════════════════════════╗
║      🌦️ WEATHER REPORT      ║
╚══════════════════════════════╝\n''')
    print(f"📍 Coordinates : {lat}, {lon}\n")
    if data.get("error"):
        print(data['reason'])
        sys.exit()
    else:
        code=data['current']['weather_code']
        print(f"🌡️ Temperature : {data['current']['temperature_2m']} °C")
        print(f"💨 Wind Speed : {data['current']['wind_speed_10m']} km/h\n")
        print(f"──────────────────────────────\n")
        print(f"🕒 Time : {data['current']['time']}\n")
        print(f"🌦️ Weather : {weather_description.get(code, 'unknown weather')}\n")
        print(f"☀️ Have a nice day!")
except requests.exceptions.ConnectionError:
    print(""" ❌ Unable to connect to weather service.
Please check your internet connection.""")

except IndexError:
    print(" ❌ Usage: python Weather_CLI.py <latitude> <longitude>")
    sys.exit()
except ValueError:
    print(" ❌ Latitude and longitude must be numbers.")


