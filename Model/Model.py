from .Translator import Translator
from Controller.Constants import Constants
from Model.FileImplementer import FileImplementer
import json


class Model:
    @staticmethod
    def get_tv_plans(channel_name):
        add = "Model/Data/TvPlansData" + channel_name
        data = FileImplementer.read_file(add)
        return data

    @staticmethod
    def get_coin_currency():
        add = "Model/Data/CoinCurrencyData"
        data = FileImplementer.read_file(add)
        return data

    @staticmethod
    def translate(english_text):
        translate_json = Translator.longman_translate(english_text)

        if translate_json == -1:
            return{
                "text": "جوابی پیدا نشد!",
                "voice": -1
            }
        else:
            return translate_json

    @staticmethod
    def get_weather(city):
        add = "Model/Data/Weather"
        json_text = FileImplementer.read_file(add)
        json_weather = json.loads(json_text)

        try:
            data = json_weather[city]
        except:
            data = "شهرموردنظر پیدا نشد!"

        return data
