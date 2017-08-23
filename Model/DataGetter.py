from Model.CoinCurrencyPrice import CoinCurrencyPrice
from Model.TvPlans import TvPlans
from Model.FileImplementer import FileImplementer
"""
this class contains methods that gets data from site servers
data like coin currency information and tv plans!
in our server this script must be invoke in a schedule
invoke method gives data from the servers and records data into files in Data folder!
files just contain the whole text that must be presented to the user!

summary : just save the servers data into the files !
"""


class DataGetter:
    def __init__(self):
        pass

    @staticmethod
    def invoke():
        # getting coin currency data and saving them!
        coin_currency_data = CoinCurrencyPrice.get_final_data()
        FileImplementer.rewrite_file("Model/Data/CoinCurrencyData", coin_currency_data)

        # getting tv plans data and saving them!
        channel_names = TvPlans.get_channel_names()
        for chn in channel_names:
            string = TvPlans.get_final_result(chn)
            print(string)
            FileImplementer.rewrite_file("Model/Data/"+"TvPlansData"+chn, string)

DataGetter.invoke()
