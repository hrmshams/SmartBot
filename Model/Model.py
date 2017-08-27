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
        translate_json = Translator.translate(english_text)
        text = translate_json["text"]

        final_text = english_text + "\n\n" + "ترجمه:" + "\n" + text + "\n\n" + Constants.BotInfo.BOT_USERNAME
        return{
            "text": final_text,
            "voice": translate_json["voice"]
        }

    @staticmethod
    def get_weather(city):
        add = "Model/Data/Weather"
        json_text = FileImplementer.read_file(add)
        json_weather = json.loads(json_text)

        print("====")
        print(json_weather['تهران'])

        try:
            data = json_weather[city]
        except:
            data = "شهرموردنظر پیدا نشد!"

        print(type(data))
        return data
