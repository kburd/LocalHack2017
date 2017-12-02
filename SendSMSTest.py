from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def hello_monkey():
    """Take in message and send to broken english"""
    message_body = request.form['Body']

    resp = MessagingResponse()
    resp.message("Your message in broken english:\n{}".format(message_body))

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)