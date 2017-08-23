import requests
import json
from .StringImplementer import StringImplementer
from Controller.Constants import Constants

"""
gets data from http://service.arzlive.com/p.js
or http://service.arzlive.com/e.js

0_1 =>once jahani tala
3_2 =>mesghal tala dar bazar iran
3_3 =>geram talaye 18 ayar
3_10 =>seke bahar azadi
3_11 =>seke emami
3_12 =>seke nim
3_13 =>seke rob
3_14 =>seke geram
# 3_40 =>
3_41 =>euro
3_42 =>pond
3_43 =>derham
3_44 =>dolar canada
17_40 =>dolar sarafi
"""


class CoinCurrencyPrice:

    TEXT_GLOBAL_ONCE = "انس جهانی"
    TEXT_MESGHAL_TALA_IRAN = "مثقال طلا در ایران"
    TEXT_GERAM_TALAYE_18 = "هر گرم طلای ۱۸ عیار"
    TEXT_SEKE_BAHAR_AZADI = "سکه بهار آزادی"
    TEXT_SEKE_EMAMI = "سکه امامی"
    TEXT_SEKE_NIM = "نیم سکه"
    TEXT_SEKE_ROB = "ربع سکه"
    TEXT_SEKE_GERAM = "سکه یک گرم"
    TEXT_EURO = "یورو"
    TEXT_POND = "پوند"
    TEXT_DERHAM = "درهم"
    TEXT_DOLAR_SARAFI = "دلار صرافی"
    TEXT_DOLAR_CANADA = "دلار کانادا"

    TEXT_SPACE = " "
    TEXT_DOLAR = "دلار"
    TEXT_TOMAN = "تومان"

    rial_to_toman_list = ["3_2", "3_3", "3_10", "3_11", "3_12", "3_13", "3_14", "3_41", "3_42", "3_43", "3_44", "17_40"]

    # return a json
    @staticmethod
    def get_coin_currency_price():
        url = "http://service.arzlive.com/e.js"
        result = requests.get(url, None)
        if result.status_code == 200:
            data = result.text
        else:
            print("Error : couldn't get data from arzlive.com")
            return

        time_json_str = StringImplementer.string_cutter(data, "update=", ";")

        price_json_str = StringImplementer.string_cutter(data, "last=", ";")
        # changes_json_str = StringImplementer.string_cutter(data, "change=", ";")
        price_json = json.loads(price_json_str)

        for k, v in price_json.items():
            if k in CoinCurrencyPrice.rial_to_toman_list:
                price_json[k] = CoinCurrencyPrice.third_tokenize(v[:-1])

        result = {
            "time": time_json_str,
            "price_json": price_json
        }
        return result

    @staticmethod
    def third_tokenize(string):
        """
        2,777,123
        len => 7
        index => [1,5]
        [0,1],[1,5],[5,len(str)]

        123,123,123
        len => 9
        index => [3,7]

        12,131,513,512
        len=>11
        index => [2,6,10]
        """
        length = len(string)

        index = length % 3
        if index == 0:
            index = 3
        index_list = [0]
        while index < length:
            index_list.append(index)
            index += 3

        index_list.append(length)

        new_string = ""
        for i in range(0, len(index_list)-1):
            new_string = new_string + string[index_list[i]:index_list[i+1]] + ","

        new_string = new_string[:-1]
        return new_string

    """
    just converts the initial data into the proper data to be presented into the user!
    """
    @staticmethod
    def get_final_data():
        result = CoinCurrencyPrice.get_coin_currency_price()
        time = result["time"]
        price = result["price_json"]

        SPACE = " "

        text = "💰 قیمت سکه و ارز به تاریخ : " + time + "\n\n"
        text = text + CoinCurrencyPrice.TEXT_GLOBAL_ONCE + SPACE + price["0_1"] + SPACE + CoinCurrencyPrice.TEXT_DOLAR + "\n"
        text = text + CoinCurrencyPrice.TEXT_MESGHAL_TALA_IRAN + SPACE + price["3_2"] + SPACE + CoinCurrencyPrice.TEXT_TOMAN + "\n"
        text = text + CoinCurrencyPrice.TEXT_GERAM_TALAYE_18 + SPACE + price["3_3"] + SPACE + CoinCurrencyPrice.TEXT_TOMAN + "\n"
        text = text + CoinCurrencyPrice.TEXT_SEKE_BAHAR_AZADI + SPACE + price["3_10"] + SPACE + CoinCurrencyPrice.TEXT_TOMAN + "\n"
        text = text + CoinCurrencyPrice.TEXT_SEKE_EMAMI + SPACE + price["3_11"] + SPACE + CoinCurrencyPrice.TEXT_TOMAN + "\n"
        text = text + CoinCurrencyPrice.TEXT_SEKE_NIM + SPACE + price["3_12"] + SPACE + CoinCurrencyPrice.TEXT_TOMAN + "\n"
        text = text + CoinCurrencyPrice.TEXT_SEKE_ROB + SPACE + price["3_13"] + SPACE + CoinCurrencyPrice.TEXT_TOMAN + "\n"
        text = text + CoinCurrencyPrice.TEXT_SEKE_GERAM + SPACE + price["3_14"] + SPACE + CoinCurrencyPrice.TEXT_TOMAN + "\n"
        text = text + CoinCurrencyPrice.TEXT_DOLAR_SARAFI + SPACE + price["17_40"] + SPACE + CoinCurrencyPrice.TEXT_TOMAN + "\n"
        text = text + CoinCurrencyPrice.TEXT_EURO + SPACE + price["3_41"] + SPACE + CoinCurrencyPrice.TEXT_TOMAN + "\n"
        text = text + CoinCurrencyPrice.TEXT_POND + SPACE + price["3_42"] + SPACE + CoinCurrencyPrice.TEXT_TOMAN + "\n"
        text = text + CoinCurrencyPrice.TEXT_DERHAM + SPACE + price["3_43"] + SPACE + CoinCurrencyPrice.TEXT_TOMAN + "\n"
        text = text + "\n" + Constants.BotInfo.BOT_USERNAME

        return text
