import requests, json
from Controller.Constants import Constants


class Translator:
    @staticmethod
    def google_translate(english_word):
        translate_url = "https://translate.googleapis.com/translate_a/t?client=gtx&sl=en&tl=fa&dt=t&q=" + english_word
        result = requests.get(translate_url, None)

        if result.status_code == 200:
            translate = result.text
        else:
            return -1

        voice_url = "https://translate.googleapis.com/translate_tts?ie=UTF-8&q="+english_word\
                    +"&tl=en&total=1&idx=0&textlen=5&client=gtx"

        return {
            "text": translate,
            "voice": voice_url
        }

    numbers = [
        "1️⃣",
        "2️⃣",
        "3️⃣",
        "4️⃣",
        "5️⃣",
        "6️⃣",
        "7️⃣",
        "8️⃣",
        "9️⃣",
        "🔟"
    ]

    '''
    website : http://developer.pearson.com/apis/dictionaries
    '''
    @staticmethod
    def longman_translate(english_word):
        url = "http://api.pearson.com/v2/dictionaries/ldoce5/entries?headword="
        url += english_word

        try:
            result = requests.get(url)
        except Exception as ex:
            print("connection error in dictionary!! => maybe peyvandha!")
            # print(ex.with_traceback())
            return -1

        if result.status_code == 200:

            # extracting desired data from json!
            try:
                # is_pronunciations_got = False
                result_json = json.loads(result.text)

                # british_pronunciation = ""
                # american_pronunciation = ""
                final_text = "📖 searching for word : <b>" + english_word + "</b>\n" \
                             "📖 results from <b>Longman Dictionary of Contemporary English</b>\n\n"

                # array of translations!
                translations = result_json["results"]
                for i in range(0, len(translations)):
                    if i > 9:
                        break

                    # trying to get pronunciations
                    # if not is_pronunciations_got:
                    #     try:
                    #         audio_list = translations[i]["pronunciations"]
                    #         for a in audio_list:
                    #             if a["audio"][0]["type"] == "pronunciation":
                    #                 if a["audio"][0]["lang"] == "British English":
                    #                     british_pronunciation = a["audio"][0]["url"]
                    #                     # print("<><><>", british_pronunciation)
                    #                 else:
                    #                     american_pronunciation = a["audio"][0]["url"]
                    #                     # print("------", american_pronunciation)
                    #                 is_pronunciations_got = True
                    #     except Exception as e:
                    #         print("couldn't get the pronunciation arguments!")
                    #         # print(e)

                    # getting the definition and example!
                    try:
                        definition = translations[i]["senses"][0]["definition"][0]
                    except:
                        definition = ""
                        # print("no definition!")

                    try:
                        example = translations[i]["senses"][0]["examples"][0]["text"]
                    except:
                        example = ""
                        # print("no example!")

                    try:
                        type = translations[i]["part_of_speech"]
                    except:
                        type = ""

                    final_text = final_text + "<b>" + Translator.numbers[i] + " " + translations[i]["headword"] + "</b>" \
                                 + " - " + "<i>" + type + "</i>" + "\n"
                    final_text = final_text + "<i>" + "definition : " + "</i>" + "\n"
                    final_text = final_text + definition + "\n"
                    if example != "":
                        final_text = final_text + "<i>" + "example : " + "</i>" + "\n"
                        final_text = final_text + "<pre>" + example + "</pre>" + "\n"

                    final_text += "\n"

                final_text += Constants.BotInfo.BOT_USERNAME

                # if american_pronunciation != "":
                #     voice_url = "http://api.pearson.com" + american_pronunciation
                # elif british_pronunciation != "":
                #     voice_url = "http://api.pearson.com" + british_pronunciation
                # else:
                #     voice_url = -1

                voice_url = "http://api.voicerss.org/?key=99cba9fb3d404cd68eeadae592daa8a4&hl=en-us&src=" + english_word
                return {
                    "text": final_text,
                    "voice": voice_url,
                    "word": english_word
                }

            except Exception as ex:
                print("something bad happed when getting data from longman json!")
                print(ex.with_traceback())
        else:
            return -1
