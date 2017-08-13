from bs4 import BeautifulSoup
import requests

"""
WARNING :
IT MUST BE CREATED THAT GIVEN DATA FROM SERVER WILL BE SAVED IN THE DATABASE
AND ALWAYS NOT TO GET DATA FROM SERVER AND SOME TIMES GETS DATA FROM DATABASE!
"""
class TvPlans:

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

    def get_tv_plans(self, channel_id):
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

        print(start_times, len(start_times))
        print(end_times, len(end_times))
        print(plans_name, len(plans_name))
        return
