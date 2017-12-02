# Imports the Google Cloud client library
from google.cloud import translate
import emoji

translate_client = translate.Client.from_service_account_json('key.json')

def internal_translate(phrase,language):
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

def translate(text,target='zh-TW',flips='1'):
    target = 'zh-TW'
    text = emoji.demojize(text).replace(":","")
    text = text.replace("_"," ")
    try:
        flips = int(flips)
    except:
        flips = 1
    for i in range(flips):
        tmp = internal_translate(text,target)
        text = ' '.join(tmp)
    return text


