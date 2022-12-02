#app.pyのコード
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,ImageSendMessage,
)
import datetime

app = Flask(__name__)

#SMT
CHANNEL_ACCESS_TOKEN = 'Wuzg/4E0bMThi2u4o4OZKhXUUODvUFW0X13emdCRKhWVbRLmgrpy+roF1eQDZ8WX+RdqOJ/LlkokPHL9Yz1VhvJ7Dy/Y2kIJbbThT9F/S0gFiawVqG8hwIFfopi+iJZ4Tt09Q5L1DI6W9ut0uQ82DAdB04t89/1O/w1cDnyilFU='
CHANNEL_SECRET = '57c8ebcf72913480d4cb03d1c8bcec39'

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

@app.route("/test", methods=['GET', 'POST'])
def test():
    follower = line_bot_api.get_insight_followers('20221201')
    print(follower.followers)

    gender = line_bot_api.get_insight_demographic()
    print(gender.genders)

    broadcast = line_bot_api.get_message_delivery_broadcast('20221201')
    print(broadcast.success)

    msg = line_bot_api.get_insight_message_delivery('20221201')
    print(msg.api_broadcast)
    return 'I\'m alive!'

if __name__ == "__main__":
    app.run()