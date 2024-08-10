from translate import Translator

translator = Translator(from_lang="english", to_lang="arabic")
hindi = translator.translate("Hello World!")
print(hindi)