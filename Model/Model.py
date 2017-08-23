from .Translator import Translator
from Controller.Constants import Constants
from Model.FileImplementer import FileImplementer


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
        json = Translator.translate(english_text)
        text = json["text"]

        final_text = english_text + "\n\n" + "ترجمه:" + "\n" + text + "\n\n" + Constants.BotInfo.BOT_USERNAME
        return{
            "text": final_text,
            "voice": json["voice"]
        }
