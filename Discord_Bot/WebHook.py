import requests
import discord
import os
import sys
from discord import Webhook, RequestsWebhookAdapter, File

def get_webhook_info(): #On récupère les info pour utiliser le webhook
    current_path = os.getcwd()  # On setup le bon path pour être sur d'avoir les modules de bien importés, peut n'importe l'interpréteur.
    split = current_path.split('\\')
    if split[-1] != 'Discord_Bot':
        split.pop()
        split.append('Discord_Bot')
        BuzzerWebApp_folder_path = '\\'.join(split)
        sys.path.append(BuzzerWebApp_folder_path)
    else:
        BuzzerWebApp_folder_path = current_path
    txt_path = BuzzerWebApp_folder_path + r'\url.txt'
    txt = open(txt_path,'r')
    WEBHOOK_ID = txt.readline()
    WEBHOOK_TOKEN = txt.readline()
    url = txt.readline()
    txt.close()
    return (WEBHOOK_ID,WEBHOOK_TOKEN)

def create_webhook_object():# On crée l'objet webhook pour lui faire faire des actions
    (WEBHOOK_ID,WEBHOOK_TOKEN) = get_webhook_info()
    webhook = Webhook.partial(WEBHOOK_ID, WEBHOOK_TOKEN, adapter=RequestsWebhookAdapter())
    return webhook

def buzz_webhook_send(username):
    webhook = create_webhook_object()
    webhook.send(f'{username} a buzzé!')

