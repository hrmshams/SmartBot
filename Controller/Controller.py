from .TelegramInteracotor import TelegramInteractor
from Controller.RequestHandler import RequestHandler
import time
import json
from .Constants import Constants


class Controller:
    __offset = 0

    """
    a collection :
    key => user_id
    value => request handler thread
    """
    __requests = {}

    def __init__(self):
        pass

    """
    note :
     in a loop => checks the updates form telegram server
     then assign to all updates a thread
     and then starts the thread
    """
    def invoke(self):
        # initializing the keyboard
        keyboard = [
            [{"text": Constants.KEYBOARD_COIN_CURRENCY}, {"text": Constants.KEYBOARD_TV_PLANS}],
            [{"text": Constants.KEYBOARD_TRANSLATE}],
            [{"text": Constants.KEYBOARD_HELP}]
        ]
        main_reply_keyboard_markup = {
            "keyboard": keyboard,
            "resize_keyboard": True,
            "one_time_keyboard": True
        }

        while True:
            # sending the request to telegram for getting the updates!
            respond = TelegramInteractor.get_updates(self.__offset)

            # checking if request has done properly!
            if respond.status_code == 200:
                updates_text = respond.text
            else:
                print("ERROR:\nCouldn't send the request! status code ::", respond.status_code)
                return

            # converting updates string into json !
            updates = json.loads(updates_text)["result"]

            # implementing the req_handler for all updates!
            for u in updates:
                # checking if request exists in the collection!

                user_id = u["message"]["from"]["id"]
                if Controller.is_key_exist(self.__requests, user_id):
                    # getting the user text and starting the thread
                    req_handler = self.__requests[user_id]
                    req_handler.init_user_text(u)

                    req_handler.invoke()
                    print("access to collec")

                else:
                    # adding the request to the collection!
                    req_handler = RequestHandler(u, main_reply_keyboard_markup)
                    self.__requests[user_id] = req_handler
                    req_handler.invoke()
                    print("access to not collec")

                # checking the offset!
                update_id = u["update_id"]
                if self.__offset < update_id: # Do we need this ?
                    self.__offset = update_id

            if len(updates) != 0:
                self.__offset += 1

            time.sleep(0.5)
        # END OF WHILE #

    @staticmethod
    def is_key_exist(collection, key):
        if key in collection:
            return True
        else:
            return False

