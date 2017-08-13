from .TelegramInteracotor import TelegramInteractor
from Controller.RequestHandler import RequestHandler
import time
import json

class Controller:
    __offset = 0
    # __requests = []

    def __init__(self):
        pass

    """
    note :
     in a loop => checks the updates form telegram server
     then assign to all updates a thread
     and then starts the thread
    """
    def invoke(self):
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
                # adding to collection and running that!
                req_handler = RequestHandler(u)
                # self.__requests.append(req_handler)
                req_handler.start()

                # checking the offset!
                update_id = u["update_id"]
                if self.__offset < update_id: # Do we need this ?
                    self.__offset = update_id

            if len(updates) != 0:
                self.__offset += 1

            time.sleep(0.5)
        # END OF WHILE #
