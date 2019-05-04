import os
import telegram

from google.cloud import datastore
from google.cloud import storage
import random

bot = telegram.Bot(token=os.environ["TELEGRAM_TOKEN"])

def getpepe():
    datastore_client = datastore.Client()
    query = datastore_client.query(kind='Pepe')
    image_entities = list(query.fetch())
    #Only 1 img, testing
    idx = (int) (random.randrange(0, len(image_entities)))
    image_entities = [image_entities[idx]]
    return image_entities[0]['image_public_url']

def webhook(request):
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        luckynumber = (int) (random.randrange(0,100))
        if(update.message.text=='/randompepe' or luckynumber==69):
            chat_id = update.message.chat.id
            pepeurl=getpepe()
            # Reply with the same message
            if(luckynumber==69):
                bot.send_photo(chat_id=chat_id,photo=pepeurl,caption="Lucky pepe")
            else:
                bot.send_photo(chat_id=chat_id, photo=pepeurl)
    return "ok"


