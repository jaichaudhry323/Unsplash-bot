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
import asyncio
from flask import Flask, request

app = Flask(__name__)

global bot
bot = telegram.Bot(token='5602023512:AAETtyiKUXT8b-jmXtkk5jkt79xw9YcD0qo')

# using telegram.Bot
async def send(chat, msg):
    bot.send_message(chat_id=chat, text=msg)

@app.route('/hook', methods=['GET','POST'])
def webhook_handler():
    print("received message 1")

    if request.method == "POST":
        print("received message 2")
        
        # retrieve the message in JSON and then transform it to Telegram object
        update = telegram.Update.de_json(request.get_json(force=True), bot)

        chat_id = update.message.chat.id

        print("chat_id: ", chat_id)

        # Telegram understands UTF-8, so encode text for unicode compatibility
        text = update.message.text.encode('utf-8')
        
        # repeat the same message back (echo)
        # await bot.send_message(chat_id=chat_id, text=text) | await async errors
        asyncio.run(send(chat_id, "msg"))

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
def set_healthcheck():
    
    print("health check found")
    try:
        print("health check ok")
        return "health check ok"
    except:
        print("health check exception")
        return "health check ok"

app.run('0.0.0.0', port=80)
