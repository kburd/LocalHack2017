from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from chatterbot import ChatBot
from google.cloud import translate
import emoji

from random import shuffle
from random import randint
app = Flask(__name__)
translate_client = translate.Client.from_service_account_json('key.json')
chatbot = ChatBot(
    'No_Speak Engrish',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

chatbot.train("chatterbot.corpus.english")

lang = ['de','zh-tw']
def internal_translate(phrase,language):
	out = []
	for word in phrase.split():
		translation = translate_client.translate(
			word,
            		target_language=language)
		out.append(translation['translatedText'])
	ret =[]
	for word in out:
        	translation = translate_client.translate(
            		word,
            	target_language='en')
        	ret.append(translation['translatedText'])
	return ret

def translate(text,lang=['de']):
	conv = len(lang)
	target = randint(1,conv-1)
	shuffle(lang)
	#print(lang)
	conv = lang[:target]
	text = emoji.demojize(text).replace(":","")
	text = text.replace("_"," ")
	for l in conv:
		tmp = internal_translate(text,l)
		text = ' '.join(tmp)
	#text = internal_translate(text,'en')
	return text

@app.route("/sms", methods=['GET', 'POST'])
def hello_monkey():
	"""Take in message and send to broken english"""
	message_body = request.form['Body']
	if "!*!" in message_body:
		message_body = message_body.replace("!*!",'')
		broken = translate(message_body,lang)
		resp = MessagingResponse()
		resp.message("Your message in broken english:\n{}".format(broken))
	else:
		broken = translate(message_body,lang)
		print(broken)
		broken = chatbot.get_response(broken)
		broken = str(broken)
		#print(type(broken))
		resp = MessagingResponse()
		resp.message(broken)
	return str(resp)

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5000)
