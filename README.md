# 🌦️ Weather Project (CLI + API)

This is a learning project where I built a weather application using Python.

## 🎯 Purpose

This project was created as part of my learning journey in Python programming.

I am currently studying:
- Python fundamentals
- working with APIs
- CLI applications
- basic backend development with Flask

## 📚 What I learned from this project

Through this project, I practiced and learned:

- How to use external APIs (Open-Meteo API)
- How to work with JSON data
- How to build CLI applications using `sys.argv`
- How to handle errors using `try/except`
- How to build a simple backend API using Flask
- How different systems communicate (CLI vs Web API)

## 🚀 Features

### CLI Version
- Get weather data using latitude and longitude
- Displays temperature, wind speed, and weather description
- Handles errors like invalid input or no internet connection

### API Version (Flask)
- REST API endpoint `/weather`
- Returns weather data in JSON format
- Accepts latitude and longitude as query parameters

## ⚙️ How to run

### CLI version:
```bash
python cli.py 40 49