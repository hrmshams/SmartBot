class Constants:
    MESSAGE_TYPE_BOT_COMMAND = "bot_command"
    MESSAGE_TYPE_ORDINARY = "not_bot_command"

    ANSWER_BOT_HELP = """
    رنگو یک بات چندکارس !
کارهایی که در حال حاضر میتونه انجام بده :

1️⃣ ترجمه انگلیسی به انگلیسی لغات و هم چنین ارسال تلفظ کلمه!
 اطلاعات از دیکشنری لانگمن (longman) دریافت میشه !
حداکثر ۱۰ مورد از معانی لغت مورد نظر نشون داده میشه ضمن اینکه ممکنه لغات مشابه یا هم خانواده لغتی که سرچ کردید رو درنتایج ببینید که این موضوع در یادگیری بیشتر اون لغت کمک میکنه.
در بعضی از موارد یک کاربرد در جمله نیز آورده شده!

2️⃣ اعلام وضعیت آب و هوای مراکز استان های کشور
که اطلاعات رو از سایت weather.yahoo.com دریافت می کنه.

3️⃣ اعلام برنامه های شبانه روزی شبکه های سیمای ملی.
بعد از درخواست شبکه موردنظرتون رو انتخاب کنید تا برنامه ی همون روز رو بهتون نشون بده!

4️⃣ قیمت روزانه سکه و ارز.

درصورتی که هرگونه مشکلی در پاسخ دهی بات بوجود اومد یا نظری پیشنهادی چیزی ! در مورد بات داشتید میتونید از طریق آیدی زیر با سازنده بات درارتباط باشید ! :) (کسانی که علاقه مند به همکاری در توسعه بات هستن هم میتونن پی ام بدن :)))
@hrmshamc
"""

    class Commands:
        COMMAND_START = "/start"
        COMMAND_SHOW_KEYBOARD = "/showkeyboard"

    class KeyboardButtons:
        KEYBOARD_TV_PLANS = "📺 برنامه های تلویزیون"
        KEYBOARD_COIN_CURRENCY = "💰 قیمت سکه و ارز"
        KEYBOARD_HELP = "⁉️ راهنمای بات"
        KEYBOARD_TRANSLATE = "مترجم " + "🇬🇧"
        KEYBOARD_WEATHER = "🌤 آب و هوا"

        KEYBOARD_BACK = "بازگشت ↩️"

    class States:
        NORMAL = 1
        ENGLISH_WORD_ENTERING = 2
        TV_PLAN_CHANNEL_ENTERING = 3
        WEATHER_CITY_ENTERING = 4

    class BotInfo:
        BOT_USERNAME = "@ranggobot"
        BOT_TOKEN = "393845550:AAEQkQ_c_w2xtjXUm8cBXZ7rg_VJ3qQilmk"

    class TranslationMessages:
        INITIAL_MESSAGE = "لغت موردنظر خود را وارد کنید." + "\n"
        ILLEGAL_CHARACTER_LEN = "طول متن واردشده بیشتر از ۲۰ کاراکتر است."+"\n"+"لطفا متن یا لغت دیگری وارد کنید"
