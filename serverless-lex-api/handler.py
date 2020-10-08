import requests
import json

api_key = "your_api_key"

base_url = "http://api.openweathermap.org/data/2.5/weather?"


def get_weather(event, context):

    city_name = event["currentIntent"]["slots"]["city_name"]

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    response = requests.get(complete_url)

    x = response.json()

    content = ""

    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"] - 273.15
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        content = "Temperature (in celsius) = " + str("%.2f" % current_temperature) + "\nAtmospheric pressure (in hPa) = " + str(
            current_pressure) + "\nHumidity (in percentage) = " + str(current_humidiy) + "\nDescription = " + str(weather_description)
    else:
        content = "City not found"

    return {
        "sessionAttributes": event["sessionAttributes"],
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
                "contentType": "PlainText",
                "content": content
            }
        }
    }
