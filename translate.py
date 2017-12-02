# Imports the Google Cloud client library
from google.cloud import translate
import emoji
# Instantiates a client
translate_client = translate.Client.from_service_account_json('key.json')

def translate(phrase,language):
    out = []
    for word in phrase.split(" "):
        translation = translate_client.translate(
            word,
            target_language=language)
        out.append(translation['translatedText'])

    ret = []
    for word in out:
        translation = translate_client.translate(
            word,
            target_language='en')
        ret.append(translation['translatedText'])
    return ret


# The text to translate
text = input("Enter text to translate: ")
flips = input("Enter number of translate: ")
# The target language
target = 'zh-TW'
#target = 'de'

# out = []
# for word in text.split():
#     translation = translate_client.translate(
#         word,
#         target_language=target)
#     out.append(translation['translatedText'])
#
# target = 'en'
# ret = []
# for word in out:
#     translation = translate_client.translate(
#         word,
#         target_language=target)
#     ret.append(translation['translatedText'])
text = emoji.demojize(text).replace(":","")
text = text.replace("_"," ")

try:
    flips = int(flips)
except:
    flips = 1
for i in range(flips):
    tmp = translate(text,target)
    text = ' '.join(tmp)
print(text)


