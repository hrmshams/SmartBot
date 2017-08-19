import requests
import json
from .StringImplementer import StringImplementer


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
