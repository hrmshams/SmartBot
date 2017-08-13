import requests


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
        return None

    @staticmethod
    def send_message(chat_id, text):
        params = {
            "chat_id": chat_id,
            "text": text
        }
        result = TelegramInteractor.send_req_to_telegram_server(TelegramInteractor.send_message_met, params)
        return result

    @staticmethod
    def get_updates(offset):
        params = {
            "offset": offset
        }
        if offset is None:
            print("access")
            params = None

        result = TelegramInteractor.send_req_to_telegram_server(TelegramInteractor.get_updates_met, params)
        return result

    @staticmethod
    def send_req_to_telegram_server(req_method, params):
        url = TelegramInteractor.telegram + TelegramInteractor.token + "/" + req_method
        r = requests.post(url, params)

        return r
