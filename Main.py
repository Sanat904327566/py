from pip._vendor import requests

url = "https://api.telegram.org/bot941857434:AAFtsDAD3qWrkmTM949DmcitXU0AJaxc5E8/"
def get_chat_id(update):
    chat_id = update['message']["chat"]["id"]
    return chat_id
def get_message_text(update):
    message_text = update["message"]["text"]
    return message_text
def last_update(req):
    response = requests.get(req + " getUpdates")
