from flask import Flask, render_template, request, redirect, url_for

import requests


app = Flask(__name__)

# Add your openweathermap.org api key here (Current Weather Data)
api_key = ""

def get_weather_data_by_city(city, temp_unit, api_key):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units={}&appid={}".format(city, temp_unit, api_key)
    r = requests.get(url)

    return r.json()
    
@app.route('/', methods=["GET", "POST"])
def index():
    weather_data = None
    temp_unit = None
    if request.method == "POST":
        city = request.form['city']
        temp_unit = request.form['temp-unit']
        weather_data = get_weather_data_by_city(city, temp_unit, api_key)
    return render_template("index.html", weather_data=weather_data, temp_unit=temp_unit)

if __name__ == '__main__':
    app.run(debug=True)