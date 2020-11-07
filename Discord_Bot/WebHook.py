import requests
import discord
from discord import Webhook, RequestsWebhookAdapter, File
WEBHOOK_TOKEN = 'GqsVp3fOfFOuPL4X3VQTyqCpGaI7TZZqAThtRADojkDkQRi1f_5z0WAnEHjDuy5tfMah'
WEBHOOK_ID = 774626469237358642
# Create webhook
webhook = Webhook.partial(WEBHOOK_ID, WEBHOOK_TOKEN, \
                          adapter=RequestsWebhookAdapter())

webhook.send('Yoooo Samuel!')