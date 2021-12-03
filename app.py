from flask import Flask, render_template, request, redirect, url_for

import requests


app = Flask(__name__)

def get_weather_data_by_city(city):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=102bac7e0c03b99c4025a5fd59aca168".format(city)
    r = requests.get(url)

    return r.json()
    
@app.route('/', methods=["GET", "POST"])
def index():
    weather_data = None
    if request.method == "POST":
        city = request.form['city']
        weather_data=get_weather_data_by_city(city)
    return render_template("index.html", weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)