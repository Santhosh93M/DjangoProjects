from googletrans import Translator


def translate(text, target="ta"):
    translator = Translator()
    translation = translator.translate(text=text, dest=target)
    return translation


strin = "how are you"
print(translate(strin).text)