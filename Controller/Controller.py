from Controller.TelegramInteracotor import TelegramInteractor
from Controller.RequestHandler import RequestHandler

class Controller:
    __offset = 0

    def __init__(self):
        return None

    def invoke(self):
        while True:
            requests = TelegramInteractor.get_updates(self.__offset)

            for req in requests:
                req_handler = RequestHandler(req)
                req_handler.start()
