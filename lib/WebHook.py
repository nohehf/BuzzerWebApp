import discord
from discord import Webhook, RequestsWebhookAdapter, File

def get_webhook_info(config): #On récupère les info pour utiliser le webhook

    WEBHOOK_ID = config['WEBHOOK']['webhook_id']
    WEBHOOK_TOKEN = config['WEBHOOK']['webhook_token']
    return (WEBHOOK_ID,WEBHOOK_TOKEN)

def create_webhook_object(config):# On crée l'objet webhook pour lui faire faire des actions
    (WEBHOOK_ID,WEBHOOK_TOKEN) = get_webhook_info(config)
    webhook = Webhook.partial(WEBHOOK_ID, WEBHOOK_TOKEN, adapter=RequestsWebhookAdapter())
    return webhook

def buzz_webhook_send(username,config):
    webhook = create_webhook_object(config)
    webhook.send(f'{username} a buzzé!')

if __name__ == "__main__":
    pass

