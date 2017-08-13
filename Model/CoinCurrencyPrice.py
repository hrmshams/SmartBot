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

    # return a json
    @staticmethod
    def get_coin_currency_price():
        url = "http://service.arzlive.com/e.js"
        result = requests.get(url, None)
        if result.status_code == 200:
            data = result.text
        else:
            print("Error : couldn't get data from arz;ive.com")
            return

        price_json_str = StringImplementer.string_cutter(data, "last=", ";")
        # changes_json_str = StringImplementer.string_cutter(data, "change=", ";")
        price_json = json.loads(price_json_str)
        return price_json

