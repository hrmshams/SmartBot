"""
gets data from yahoo weather api!
"""
import urllib, json
import urllib.parse
import requests
from Controller.Constants import Constants

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
    # TODO
}

states_eng_per = {
    "Sunny": ["آفتابی", "☀️ "],
    "Partly Cloudy": ["بخشی ابری", "🌤"],
    "Mostly Cloudy": ["اغلب ابری", "⛅️"],
    "Cloudy": ["ابری", "☁️"],
    "Fair": ["کمی ابری", "🌤"],
    "Thunderstorms": ["باران و رعدوبرق", "⛈"],
    "Scattered thunderstorms": ["رعدوبرق پراکنده", "⛈"],
    "Breezy": ["وزش باد", "💨"],
    "Blustery": ["وزش باد", "💨"],
    "Mostly Sunny": ["اغلب آفتابی", "☀️ "]
    # TODO
}

days_eng_per = {
    "Sat": "شنبه",
    "Sun": "یکشنبه",
    "Mon": "دوشنبه",
    "Tue": "سه شنبه",
    "Wed": "چهارشنبه",
    "Thu": "پنج شنبه",
    "Fri": "جمعه"
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

            "forecast": [{
                "day": weather_result["forecast"][0]["day"],
                "high": weather_result["forecast"][0]["high"],
                "low": weather_result["forecast"][0]["low"],
                "state": weather_result["forecast"][0]["text"]
            },
            {
                "day": weather_result["forecast"][1]["day"],
                "high": weather_result["forecast"][1]["high"],
                "low": weather_result["forecast"][1]["low"],
                "state": weather_result["forecast"][1]["text"]
            },
            {
                "day": weather_result["forecast"][2]["day"],
                "high": weather_result["forecast"][2]["high"],
                "low": weather_result["forecast"][2]["low"],
                "state": weather_result["forecast"][2]["text"]
            },
            {
                "day": weather_result["forecast"][3]["day"],
                "high": weather_result["forecast"][3]["high"],
                "low": weather_result["forecast"][3]["low"],
                "state": weather_result["forecast"][3]["text"]
            },
            {
                "day": weather_result["forecast"][4]["day"],
                "high": weather_result["forecast"][4]["high"],
                "low": weather_result["forecast"][4]["low"],
                "state": weather_result["forecast"][4]["text"]
            },
            {
                "day": weather_result["forecast"][5]["day"],
                "high": weather_result["forecast"][5]["high"],
                "low": weather_result["forecast"][5]["low"],
                "state": weather_result["forecast"][5]["text"]
            },
            {
                "day": weather_result["forecast"][6]["day"],
                "high": weather_result["forecast"][6]["high"],
                "low": weather_result["forecast"][6]["low"],
                "state": weather_result["forecast"][6]["text"]
            }]
        }

        # initializing the data for final text!
        try:
            city_name = cities_eng_per[city]
        except:
            city_name = city

        try:
            cur_state_text = states_eng_per[final_weather["state"]][0]
            cur_state_icon = states_eng_per[final_weather["state"]][1]
        except:
            cur_state_text = final_weather["state"]
            cur_state_icon = ""

        text = "آب و هوای شهر " + city_name + "\n\n" +\
               "هوای فعلی آپدیت شده در تاریخ: " + "\n" + final_weather["cur_date"] + "\n" +\
               cur_state_icon + cur_state_text + " - " + final_weather["cur_temp"] + "درجه سانتی گراد" + "\n\n" +\
               "پیش بینی وضع هوای روزهای آینده:" + "\n"

        for f in final_weather["forecast"]:
            try:
                state_text = states_eng_per[f["state"]][0]
                state_icon = states_eng_per[f["state"]][1]
            except:
                state_text = f["state"]
                state_icon = ""

            text = text + days_eng_per[f["day"]] + ":" + "\n" +\
            state_icon + state_text + " - " + "🔻" + f["low"] + "درجه - " +\
            "🔺" + f["high"] + "درجه" + "\n\n"
            # print(f)

        text = text + Constants.BotInfo.BOT_USERNAME

        return text
