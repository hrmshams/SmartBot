from threading import Thread
from .Constants import Constants
from .TelegramInteracotor import TelegramInteractor
from Model.Texts import Texts


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

        try:
            self.__username = update["message"]["from"]["username"]
        except Exception as e:
            self.__username = None

        self.__chat_id = update["message"]["chat"]["id"]
        self.__message_id = update["message"]["message_id"]
        self.__language = update["message"]["from"]["language_code"]
        self.__text = update["message"]["text"]
        self.__is_private = update["message"]["chat"]["type"]
        try:
            self.__type = update["message"]["entities"][0]["type"]
        except Exception as ae:
            print (update)
            print (ae)
            self.__type = Constants.MESSAGE_TYPE_ORDINARY

    """
    routine of answering happens in this function!
    """
    def run(self):
        print("request got from : ", self.__first_name , "\ntext : " , self.__text)
        if self.__type == Constants.MESSAGE_TYPE_BOT_COMMAND:
            if self.__text == Constants.MESSAGE_TEXT_START:
                self.ans_start_command()
                return

            if self.__text == Constants.MESSAGE_TEXT_COMMAND1:
                self.ans_command1()
                return

        elif self.__type == Constants.MESSAGE_TYPE_ORDINARY:
            self.ans_ordinary_req()
        else:
            pass

    def ans_start_command(self):
        TelegramInteractor.send_message(self.__chat_id, Texts.START_TEXT)
        print("request answered to : ", self.__first_name)

    def ans_command1(self):
        TelegramInteractor.send_message(self.__chat_id, "دستور اول خواسته شد")
        print("request answered to : ", self.__first_name)

    def ans_ordinary_req(self):
        TelegramInteractor.send_message(self.__chat_id, "متن عادی")
        print("request answered to : ", self.__first_name)
