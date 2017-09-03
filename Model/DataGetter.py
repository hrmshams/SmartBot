from Model.CoinCurrencyPrice import CoinCurrencyPrice
from Model.TvPlans import TvPlans
from Model.FileImplementer import FileImplementer
from Model.Weather import Weather
from Model.Weather import cities_eng_per
import json

"""
this class contains methods that gets data from site servers
data like coin currency information and tv plans and etc!
in our server this script must be invoke in a schedule
invoke method gives data from the servers and records data into files in Data folder!
files just contain the whole text that must be presented to the user!

summary : just save the servers data into the files !
"""

# TODO : check seprating the files or all of data in one json file is it better or no difference?!


class DataGetter:
    def __init__(self):
        pass

    @staticmethod
    def invoke():
        # getting coin currency data and saving them!
        print("getting data :: coin_currency")
        coin_currency_data = CoinCurrencyPrice.get_final_data()
        FileImplementer.rewrite_file("Model/Data/CoinCurrencyData", coin_currency_data)

        # getting tv plans data and saving them!
        channel_names = TvPlans.get_channel_names()
        print("getting data :: tv channels")
        for chn in channel_names:
            print("     --", chn)
            string = TvPlans.get_final_result(chn)
            FileImplementer.rewrite_file("Model/Data/"+"TvPlansData"+chn, string)

        # getting weather data
        print("getting data :: weather")
        weather_json = {}
        for eng_city, per_city in cities_eng_per.items():
            print("     --", eng_city)
            final_data = Weather.get_desired_weather(eng_city)
            weather_json[per_city] = final_data
            # TODO sleep!

        weather_json_string = json.dumps(weather_json)
        FileImplementer.rewrite_file("Model/Data/Weather", weather_json_string)
