from Controller.Controller import Controller
from Model.TvPlans import TvPlans
from Model.StringImplementer import StringImplementer
from Model.CoinCurrencyPrice import CoinCurrencyPrice
from Model.Model import Model

# t = Controller()
# t.invoke()

# print(Texts.START_TEXT)

# tvpl = TvPlans()
# tvpl.get_tv_plans(TvPlans.CHANNEL_POOYA)

# mainStr = "hamid={}"
# firstStr = "="
# endStr = "="
#
# cuttenStr = StringImplementer.string_cutter(mainStr, firstStr, endStr)
# print(cuttenStr)

print(CoinCurrencyPrice.get_coin_currency_price())
# str = "123"
# print (str[0:len(str)])

# CoinCurrencyPrice.third_tokenize("1123123123123123")
