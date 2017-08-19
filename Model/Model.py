from .TvPlans import TvPlans
from .CoinCurrencyPrice import CoinCurrencyPrice
from .Translator import Translator


class Model:

    """
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

    @staticmethod
    def get_tv_plans(channel_name):
        tv_plan = TvPlans()
        result = tv_plan.get_tv_plans(TvPlans.get_channel_names()[channel_name])

        plans_name = result[2]
        plans_start = result[0]
        plans_end = result[1]

        text = "📺 برنامه های " + channel_name + " 📺" + "\n\n"
        text = text + "نام برنامه" + " | " + "تاریخ شروع" + " | " + "تاریخ پایان" + "\n"

        for i in range(0, len(plans_name)):
            text = text + plans_name[i] + " :\n" + "<code>" + " | " + plans_start[i] + " | " + plans_end[i] + " | " + "</code>" + "\n"

        text = text + "\n" + "@casscobot"

        return text

    @staticmethod
    def get_coin_currency():
        result = CoinCurrencyPrice.get_coin_currency_price()
        time = result["time"]
        price = result["price_json"]

        SPACE = " "

        text = "💰 قیمت سکه و ارز به تاریخ : " + time + "\n\n"
        text = text + Model.TEXT_GLOBAL_ONCE + SPACE + price["0_1"] + SPACE + Model.TEXT_DOLAR + "\n"
        text = text + Model.TEXT_MESGHAL_TALA_IRAN + SPACE + price["3_2"] + SPACE + Model.TEXT_TOMAN + "\n"
        text = text + Model.TEXT_GERAM_TALAYE_18 + SPACE + price["3_3"] + SPACE + Model.TEXT_TOMAN + "\n"
        text = text + Model.TEXT_SEKE_BAHAR_AZADI + SPACE + price["3_10"] + SPACE + Model.TEXT_TOMAN + "\n"
        text = text + Model.TEXT_SEKE_EMAMI + SPACE + price["3_11"] + SPACE + Model.TEXT_TOMAN + "\n"
        text = text + Model.TEXT_SEKE_NIM + SPACE + price["3_12"] + SPACE + Model.TEXT_TOMAN + "\n"
        text = text + Model.TEXT_SEKE_ROB + SPACE + price["3_13"] + SPACE + Model.TEXT_TOMAN + "\n"
        text = text + Model.TEXT_SEKE_GERAM + SPACE + price["3_14"] + SPACE + Model.TEXT_TOMAN + "\n"
        text = text + Model.TEXT_DOLAR_SARAFI + SPACE + price["17_40"] + SPACE + Model.TEXT_TOMAN + "\n"
        text = text + Model.TEXT_EURO + SPACE + price["3_41"] + SPACE + Model.TEXT_TOMAN + "\n"
        text = text + Model.TEXT_POND + SPACE + price["3_42"] + SPACE + Model.TEXT_TOMAN + "\n"
        text = text + Model.TEXT_DERHAM + SPACE + price["3_43"] + SPACE + Model.TEXT_TOMAN + "\n"
        text = text + "\n" + "@ranggobot"

        return text

    @staticmethod
    def translate(english_text):
        return Translator.translate(english_text)