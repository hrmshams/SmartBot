import requests


class Translator:
    @staticmethod
    def translate(english_word):
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
