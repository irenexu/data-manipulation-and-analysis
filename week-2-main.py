from flask import Flask, render_template
import requests
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
    response_cat = requests.get(url="https://api.thecatapi.com/v1/images/search")
    cat = response_cat.json()
    img_url = cat[0]['url']

    response_weather = requests.get(url="https://api.openweathermap.org/data/2.5/weather?lat=51.507351&lon=-0.127758&appid=93146e366d37fc681f5daf1f33371a50")
    weather = response_weather.json()
    weather_info = weather['weather'][0]['description']
    temp_info = round(float(weather['main']['temp'] - 273.15), 2)

    response_forecast = requests.get(url="https://api.openweathermap.org/data/2.5/forecast?lat=51.507351&lon=-0.127758&cnt=1&appid=93146e366d37fc681f5daf1f33371a50")
    forecast = response_forecast.json()
    next_time = forecast['list'][0]['dt_txt']
    forecast_info = forecast['list'][0]['weather'][0]['description']

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return render_template("week-2-index.html", image = img_url, weather = weather_info, temp = temp_info, time = current_time, next_time = next_time, forecast = forecast_info)

if __name__ == "__main__":
    app.run(debug=True)


# HTML/CSS learnt from Udemy Python Course - 100 Days of Code: The Complete Python Pro Bootcamp
# https://www.udemy.com/course/100-days-of-code/learn/lecture/22060308#overview