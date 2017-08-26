"""
gets data from yahoo weather api!
"""
import urllib, json
import urllib.parse
import requests

"""
https://fa.wikipedia.org/wiki/%D8%A7%D8%B3%D8%AA%D8%A7%D9%86%E2%80%8C%D9%87%D8%A7%DB%8C_%D8%A7%DB%8C%D8%B1%D8%A7%D9%86
"""
cities_eng_per = {
    "tabriz": "تبریز",
    "orumiyeh": "ارومیه",
    "ardabil": "اردبیل",
    "esfahan": "اصفهان",
    "karaj": "کرج",
    "ilam": "ایلام",
    "Bandar-e Bushehr": "بوشهر",
    "tehran": "تهران",
    "shahr kord": "شهرکرد"
}

states_eng_per = {
    "Sunny": "آفتابی"
}

class Weather:
    def __init__(self):
        pass

    '''
    gets the whole data(primary data or raw data) from yahoo api and then
    return this as a json object.
    city is a string!
    '''
    @staticmethod
    def get_whole_data_weather(city):

        base_url = "https://query.yahooapis.com/v1/public/yql?"
        yql_query = "select * from weather.forecast where " \
                    "woeid in (select woeid from geo.places(1) where text=\"%s, ir\") " \
                    "and u='c'" % city

        yql_url = base_url + urllib.parse.urlencode({'q': yql_query}) + "&format=json"

        result = requests.get(yql_url)
        result_json = json.loads(result.text)

        return result_json

    '''
    first calls the get_whole_data_weather method and then
    extract the desired data from that!
    and then return the final text to be shown to the user!
    '''
    @staticmethod
    def get_desired_weather(city):
        json_result = Weather.get_whole_data_weather(city)

        weather_result = json_result["query"]["results"]["channel"]["item"]

        final_weather = {
            "cur_temp": weather_result["condition"]["temp"],
            "cur_date": weather_result["condition"]["date"],
            "state": weather_result["condition"]["text"],

            "forecast_0": {
                "day": weather_result["forecast"][0]["day"],
                "high": weather_result["forecast"][0]["high"],
                "low": weather_result["forecast"][0]["low"],
                "state": weather_result["forecast"][0]["text"]
            },
            "forecast_1": {
                "day": weather_result["forecast"][1]["day"],
                "high": weather_result["forecast"][1]["high"],
                "low": weather_result["forecast"][1]["low"],
                "state": weather_result["forecast"][1]["text"]
            },
            "forecast_2": {
                "day": weather_result["forecast"][2]["day"],
                "high": weather_result["forecast"][2]["high"],
                "low": weather_result["forecast"][2]["low"],
                "state": weather_result["forecast"][2]["text"]
            }
        }

        try:
            text = "آب و هوای شهر " + cities_eng_per[city] + "\n" + final_weather["cur_date"] + "\n"
            text = text + "هوای فعلی :" + "\n" + final_weather["cur_temp"] + " - " \
                   + states_eng_per[final_weather["state"]]
        except:
            text = "در دریافت اطلاعات مشکلی بوجود آمده است."

        return text
    
