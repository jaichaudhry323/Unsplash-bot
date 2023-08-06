# from flask import Flask
# import sys

# app = Flask(__name__)
# # cors = CORS(app)

# if __name__ == '__main__':
#   app.run(host='0.0.0.0', port=80)

# import requests
# resp = requests.get(http://0.0.0.0:80/healthcheck)
# print("healthcheck response: ", resp)


import telegram
from flask import Flask, request

app = Flask(__name__)

global bot
bot = telegram.Bot(token='5602023512:AAETtyiKUXT8b-jmXtkk5jkt79xw9YcD0qo')


@app.route('/HOOK', methods=['POST'])
def webhook_handler():
    if request.method == "POST":
        # retrieve the message in JSON and then transform it to Telegram object
        update = telegram.Update.de_json(request.get_json(force=True))

        chat_id = update.message.chat.id

        print("chat_id: ", chat_id)

        # Telegram understands UTF-8, so encode text for unicode compatibility
        text = update.message.text.encode('utf-8')
        
        # repeat the same message back (echo)
        bot.sendMessage(chat_id=chat_id, text=text)

    return 'ok'


@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook('https://testbot1-jaichaudhry323.b4a.run/HOOK')
    if s:
        print("webhook setup ok")
        return "webhook setup ok"
    else:
        print("webhook setup not ok")
        return "webhook setup failed"

@app.route('/healthcheck', methods=['GET'])
def set_webhook():
    
    if s:
        print("health check ok")
        return "health check ok"
    else:
        return "health check ok"
  
