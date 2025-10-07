import openai
import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

openai.api_key = os.getenv("chave")

app = Flask(__name__)


@app.route("/sms", methods=['GET','POST'])
def sms_reply():
    inbound_text_message = request.values.get('Body', None)
    phone_number = request.values.get('From', None)

    chatgpt_response = openai.ChatCompletion.create(
        model="gpt-4.0",
        messages=[
            {"role": "system", "content": "Es uma assistente util"},
            {"role": "user", "content": inbound_text_message}

        ]

    )

    chatgpt_message = chatgpt_response['choices'][0]['message']['content']


    message_response = MessagingResponse()
    message_response.message('Hello')

    return str(message_response)
if __name__ == "__main__":
    app.run(debug=True)










