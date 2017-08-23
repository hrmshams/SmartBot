from bs4 import BeautifulSoup
import requests
from Controller.Constants import Constants
"""
WARNING :
IT MUST BE CREATED THAT GIVEN DATA FROM SERVER WILL BE SAVED IN THE DATABASE
AND ALWAYS NOT TO GET DATA FROM SERVER AND SOME TIMES GETS DATA FROM DATABASE!
"""


class TvPlans:

    channels_names = ["شبکه یک", "شبکه دو", "شبکه سه", "شبکه چهار", "شبکه تهران", "شبکه خبر", "شبکه آموزش", "شبکه قرآن",
                      "شبکه مستند", "شبکه نمایش", "شبکه افق", "شبکه ورزش", "شبکه پویا", "شبکه سلامت", "شبکه نسیم",
                      "شبکه امید", "شبکه تماشا"]

    #TODO proper code for each one!
    CHANNEL_ONE = 31
    CHANNEL_TWO = 32
    CHANNEL_THREE = 33
    CHANNEL_FOUR = 34
    CHANNEL_TEHRAN = 35
    CHANNEL_KHABAR = 36
    CHANNEL_AMOOZESH = 37
    CHANNEL_QURAN = 38
    CHANNEL_MOSTANAD = 39
    CHANNEL_NAMAYESH = 42
    CHANNEL_OFOGH = 43
    CHANNEL_VARZESH = 47
    CHANNEL_POOYA = 29
    CHANNEL_SALAMAT = 48
    CHANNEL_NASIM = 49
    CHANNEL_OMID = 104
    CHANNEL_TAMASHA = 69

    @staticmethod
    def get_channel_names():
        channels_names = {"شبکه یک": TvPlans.CHANNEL_ONE, "شبکه دو": TvPlans.CHANNEL_TWO, "شبکه سه": TvPlans.CHANNEL_THREE,
                          "شبکه چهار": TvPlans.CHANNEL_FOUR, "شبکه تهران": TvPlans.CHANNEL_TEHRAN, "شبکه خبر": TvPlans.CHANNEL_KHABAR,
                          "شبکه آموزش": TvPlans.CHANNEL_AMOOZESH, "شبکه قرآن": TvPlans.CHANNEL_QURAN, "شبکه مستند": TvPlans.CHANNEL_MOSTANAD,
                          "شبکه نمایش": TvPlans.CHANNEL_NAMAYESH, "شبکه افق": TvPlans.CHANNEL_OFOGH, "شبکه ورزش": TvPlans.CHANNEL_VARZESH,
                          "شبکه پویا": TvPlans.CHANNEL_POOYA, "شبکه سلامت": TvPlans.CHANNEL_SALAMAT, "شبکه نسیم": TvPlans.CHANNEL_NASIM,
                          "شبکه امید": TvPlans.CHANNEL_OMID, "شبکه تماشا": TvPlans.CHANNEL_TAMASHA}

        return channels_names

    @staticmethod
    def get_tv_plans(channel_id: int):
        # getting xml data from sedasima server!
        url = "https://www.irib.ir/include/pages/conductor-ajax-process.php"
        params = {
            "epg_id": channel_id
        }
        r = requests.get(url, params)

        if r.status_code == 200:
            xml = r.text
        else:
            print("ERROR:\nCouldn't send the request! status code ::", r.status_code)
            return

        # parsing the data into usable data!
        y = BeautifulSoup(xml, 'html.parser')

        # decoding data from xml into arrays!
        start_times = []
        end_times = []
        plans_name = []
        ul_tags = y.findAll("ul")
        for ul in ul_tags:
            li_tags = ul.findAll("li")
            start_time = li_tags[0].span.string
            end_time = li_tags[1].span.string
            start_times.append(start_time)
            end_times.append(end_time)

        h4_tags = y.findAll("h4")
        for h4 in h4_tags:
            plans_name.append(h4.string)

        # print("access",plans_name)
        return [start_times, end_times, plans_name]

    @staticmethod
    def get_final_result(channel_name):
        tv_plan = TvPlans()
        result = tv_plan.get_tv_plans(TvPlans.get_channel_names()[channel_name])

        plans_name = result[2]
        plans_start = result[0]
        plans_end = result[1]

        text = "📺 برنامه های " + channel_name + " 📺" + "\n\n"
        text = text + "نام برنامه" + " | " + "تاریخ شروع" + " | " + "تاریخ پایان" + "\n"

        for i in range(0, len(plans_name)):
            text = text + plans_name[i] + " :\n" + "<code>" + " | " + plans_start[i] + " | " + plans_end[i] + " | " + "</code>" + "\n"

        text = text + "\n" + Constants.BotInfo.BOT_USERNAME

        return text

    @staticmethod
    def get_channels_keyboard():
        keyboard =[
            [{"text": Constants.KEYBOARD_BACK}],
            [{"text": "شبکه سه"}, {"text": "شبکه دو"}, {"text": "شبکه یک"}],
            [{"text": "شبکه خبر"}, {"text": "شبکه تهران"}, {"text": "شبکه چهار"}],
            [{"text": "شبکه مستند"}, {"text": "شبکه قرآن"}, {"text": "شبکه آموزش"}],
            [{"text": "شبکه ورزش"}, {"text": "شبکه افق"}, {"text": "شبکه نمایش"}],
            [{"text": "شبکه نسیم"}, {"text": "شبکه سلامت"}, {"text": "شبکه پویا"}],
            [{"text": "شبکه تماشا"}, {"text": "شبکه امید"}]
        ]
        reply_keyboard_markup = {
            "keyboard": keyboard,
            "resize_keyboard": True,
            "one_time_keyboard": True
        }

        return reply_keyboard_markup
