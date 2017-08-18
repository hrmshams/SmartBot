from threading import Thread

from Model.Model import Model
from Model.Texts import Texts
from Model.TvPlans import TvPlans
from .Constants import Constants
from .TelegramInteracotor import TelegramInteractor


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

    __main_keyboard = None

    def __init__(self, update):
        super(RequestHandler, self).__init__()
        self.get_important_data(update)

        keyboard = [
            [{"text": Constants.KEYBOARD_COIN_CURRENCY}, {"text": Constants.KEYBOARD_TV_PLANS}],
            [{"text": Constants.KeyBOARD_HELP}]
        ]
        reply_keyboard_markup = {
            "keyboard": keyboard,
            "resize_keyboard": True,
            "one_time_keyboard": True
        }
        self.__main_keyboard = reply_keyboard_markup

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
            self.__type = Constants.MESSAGE_TYPE_ORDINARY

    """
    routine of answering happens in this function!
    """
    def run(self):
        print("request got from : ", self.__first_name , "\ntext : ", self.__text)

        if self.__type == Constants.MESSAGE_TYPE_BOT_COMMAND:
            if self.__text == Constants.MESSAGE_TEXT_START:
                TelegramInteractor.send_message(self.__chat_id, Texts.START_TEXT, self.__main_keyboard)

        else:
            if self.__text == Constants.KEYBOARD_TV_PLANS:
                self.ans_tv_plan(1)

            elif self.__text in TvPlans.channels_names:
                self.ans_tv_plan(2)

            elif self.__text == Constants.KEYBOARD_BACK:
                TelegramInteractor.send_message(self.__chat_id, Texts.BACK_TEXT, self.__main_keyboard)

            elif self.__text == Constants.KEYBOARD_COIN_CURRENCY:
                TelegramInteractor.send_message(self.__chat_id, Model.get_coin_currency(), None)

            elif self.__text == Constants.KeyBOARD_HELP:
                pass

            else:
                self.ans_ordinary_req()
                print("request answered to : ", self.__first_name)

    def ans_tv_plan(self, step: int):
        if step == 1:
            message = "کانال موردنظر را انتخاب کنید."
            TelegramInteractor.send_message(self.__chat_id, message, TvPlans.get_channels_keyboard())
        elif step == 2:
            try:
                message = Model.get_tv_plans(self.__text)
                TelegramInteractor.send_message(self.__chat_id, message, None)
            except Exception as e:
                print("Error: in getting TvPlans data => RequestHandler line 90")
                message = "در دریافت اطلاعات شبکه خطایی رخ داد." + "\n" + "لطفا این موضوع را به سازنده بات اطلاع دهید."
                TelegramInteractor.send_message(self.__chat_id, message, None)

    def ans_ordinary_req(self):
        TelegramInteractor.send_message(self.__chat_id, "منظوری دریافت نشد!", None)
