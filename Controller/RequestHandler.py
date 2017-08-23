from threading import Thread
from Model.Model import Model
from Model.Texts import Texts
from Model.TvPlans import TvPlans
from .Constants import Constants
from .TelegramInteracotor import TelegramInteractor


class RequestHandler:
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

    #
    __state = Constants.States.NORMAL

    def get_state(self):
        return self.__state

    """
    if the class instanced for the first time (not existed in the collection)
    it must be called just the __init__ method just by instancing the class!
    but if the class there exist in the collection then method get_user_text must be called;
    before calling run method !!!
    """
    def __init__(self, update, reply_keyboard_markup):
        # super(RequestHandler, self).__init__()
        self.get_const_data(update)
        self.init_user_text(update)

        # the main keyboard that will be shown to the user
        self.__main_keyboard = reply_keyboard_markup

    def get_const_data(self, update):
        # self.__message_id = update["message"]["message_id"] #
        self.__user_id = update["message"]["from"]["id"]
        self.__first_name = update["message"]["from"]["first_name"]
        self.__chat_id = update["message"]["chat"]["id"]
        self.__is_private = update["message"]["chat"]["type"]

        try:
            self.__username = update["message"]["from"]["username"]
        except Exception:
            self.__username = None

        try:
            self.__type = update["message"]["entities"][0]["type"]
        except Exception:
            self.__type = Constants.MESSAGE_TYPE_ORDINARY

    def init_user_text(self, update):
        try:
            self.__text = update["message"]["text"]
        except:
            print("couldn't get the user text")
    """
    initializes the thread for answer_request method!!
    """
    def invoke(self):
        t = Thread(target=self.answer_request)
        t.start()

    """
    routine of answering happens in this function!
    """
    def answer_request(self):
        print("request got from : ", self.__first_name, "\ntext : ", self.__text)

        if self.__type == Constants.MESSAGE_TYPE_BOT_COMMAND:
            if self.__text == Constants.MESSAGE_TEXT_START:
                TelegramInteractor.send_message(self.__chat_id, Texts.START_TEXT, self.__main_keyboard)

        else:
            if self.__state == Constants.States.NORMAL:

                if self.__text == Constants.KEYBOARD_TV_PLANS:
                    self.ans_tv_plan(1)

                elif self.__text == Constants.KEYBOARD_TRANSLATE:
                    self.ans_english_word(1)

                elif self.__text == Constants.KEYBOARD_COIN_CURRENCY:
                    TelegramInteractor.send_message(self.__chat_id, Model.get_coin_currency(), None)

                elif self.__text == Constants.KEYBOARD_BACK:
                    self.__state = Constants.States.NORMAL
                    TelegramInteractor.send_message(self.__chat_id, Texts.BACK_TEXT, self.__main_keyboard)

                elif self.__text == Constants.KEYBOARD_HELP:
                    pass

                else:
                    self.ans_ordinary_req()
                    # print("request answered to : ", self.__first_name)

            elif self.__state == Constants.States.TV_PLAN_CHANNEL_ENTERING:
                self.ans_tv_plan(2)

            elif self.__state == Constants.States.ENGLISH_WORD_ENTERING:
                self.ans_english_word(2)

        print("request answered to : ", self.__first_name)

    def ans_english_word(self, step: int):
        if step == 1:
            self.__state = Constants.States.ENGLISH_WORD_ENTERING
            message = Constants.TranslationMessages.INITIAL_MESSAGE
            TelegramInteractor.send_message(self.__chat_id, message, None)

        elif step == 2:
            if len(self.__text) > 75:
                message = Constants.TranslationMessages.ILLEGAL_CHARACTER_LEN
                TelegramInteractor.send_message(self.__chat_id, message, None)

            else:
                self.__state = Constants.States.NORMAL
                translate_json = Model.translate(self.__text)
                text = translate_json["text"]
                voice = translate_json["voice"]
                TelegramInteractor.send_voice(self.__chat_id, voice, self.__main_keyboard, text)

    def ans_tv_plan(self, step: int):
        if step == 1:
            self.__state = Constants.States.TV_PLAN_CHANNEL_ENTERING
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
