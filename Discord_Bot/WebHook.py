import requests
import discord
from discord import Webhook, RequestsWebhookAdapter, File

def get_webhook_info(): #On récupère les info pour utiliser le webhook
    txt = open('url.txt','r')
    WEBHOOK_ID = txt.readline()
    WEBHOOK_TOKEN = txt.readline()
    url = txt.readline()
    txt.close()
    return (WEBHOOK_ID,WEBHOOK_TOKEN)

def create_webhook_object(discord_folder_path):# On crée l'objet webhook pour lui faire faire des actions
    (WEBHOOK_ID,WEBHOOK_TOKEN) = get_webhook_info(discord_folder_path)
    webhook = Webhook.partial(WEBHOOK_ID, WEBHOOK_TOKEN, adapter=RequestsWebhookAdapter())
    return webhook

def buzz_webhook_send(username):
    webhook = create_webhook_object()
    webhook.send(f'{username} a buzzé!')

