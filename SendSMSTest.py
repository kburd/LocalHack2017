from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def hello_monkey():
    """Respond and greet the caller by name."""
    # Try adding your own number to this list!
    callers = {
        "+13026822230": "Bonard",
        "+12153501332": "Ben",
        "+14158675311": "Virgil",
    }
    from_number = request.values.get('From', None)
    message = callers[from_number] if from_number in callers else "Monkey"
    message_body = request.form['Body']

    resp = MessagingResponse()
    resp.message("{}, thanks for saying {}!".format(message,message_body))

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)