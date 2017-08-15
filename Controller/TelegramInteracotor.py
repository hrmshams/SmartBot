import requests,json


# be aware you should use this class methods as static!
# don't make any instances from this class!
class TelegramInteractor:

    # methods #
    send_message_met = "sendMessage"
    get_updates_met = "getUpdates"

    # #
    token = "438668023:AAEZsIovdbO8jwOoE6bghB2B4Q0ijOFASG8" # cascoye sokhangoo!
    telegram = "https://api.telegram.org/bot"

    def __init__(self):
        pass

    @staticmethod
    def send_message(chat_id, text, reply_markup=[]):
        params = {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "HTML",
        }
        if reply_markup is not None:
            str_key = json.dumps(reply_markup)
            params["reply_markup"] = str_key

        print(reply_markup)
        result = TelegramInteractor.send_req_to_telegram_server(TelegramInteractor.send_message_met, params)
        return result

    @staticmethod
    def get_updates(offset):
        params = {
            "offset": offset
        }
        if offset is None:
            print ("access")
            params = None

        result = TelegramInteractor.send_req_to_telegram_server(TelegramInteractor.get_updates_met, params)
        return result

    @staticmethod
    def send_req_to_telegram_server(req_method, params):
        url = TelegramInteractor.telegram + TelegramInteractor.token + "/" + req_method
        r = requests.post(url, params)

        return r
