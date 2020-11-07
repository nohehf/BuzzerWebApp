import requests
import discord
from discord import Webhook, RequestsWebhookAdapter, File

def get_webhook_info():
    txt = open('url.txt','r')
    url = txt.readline()
    txt.close()
    url_list = url.split('/')
    WEBHOOK_ID = url_list[3]
    WEBHOOK_TOKEN = url_list[4]
    return (WEBHOOK_ID,WEBHOOK_TOKEN)

# Create webhook
(WEBHOOK_ID,WEBHOOK_TOKEN) = get_webhook_info()
webhook = Webhook.partial(WEBHOOK_ID, WEBHOOK_TOKEN, \
                          adapter=RequestsWebhookAdapter())

webhook.send('Timoté a buzzé!')