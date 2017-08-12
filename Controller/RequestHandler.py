from threading import Thread
from .Constants import Constants
from .TelegramInteracotor import TelegramInteractor
from .Texts import Texts

class RequestHandler(Thread):

    # user info
    __user_id = None
    __first_name = None
    __username = None

    # chat info
    __chat_id = None
    __is_private = None

    # message info
    __message_id = None
    __language = None
    __text = None
    __type = None

    def __init__(self, update):
        super(RequestHandler, self).__init__()
        self.get_important_data(update)

    def get_important_data(self, update):
        self.__user_id = update["message"]["from"]["id"]
        self.__first_name = update["message"]["from"]["first_name"]
        self.__username = update["message"]["from"]["username"]
        self.__chat_id = update["message"]["chat"]["id"]
        self.__message_id = update["message"]["message_id"]
        self.__language = update["message"]["from"]["language_code"]
        self.__text = update["message"]["text"]
        self.__is_private = update["message"]["chat"]["type"]
        try:
            self.__type = update["message"]["entities"]["type"]
        except AttributeError as ae:
            self.__type = Constants.MESSAGE_TYPE_ORDINARY

    """
    routine of answering happens in this function!
    """
    def run(self):
        if self.__type == Constants.MESSAGE_TYPE_BOT_COMMAND:
            if self.__text == Constants.MESSAGE_TEXT_START:
                self.ans_start_command()
                return
        elif self.__type == Constants.MESSAGE_TYPE_ORDINARY:
            pass
        else:
            pass

    def ans_start_command(self):
        TelegramInteractor.send_message(self.__chat_id , Texts.START_TEXT)

    def ans_command1(self):
        pass
