import discord

#initialisation du bot
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

chara = '_' #le charactère pour les commandes
@client.event
async def on_ready(): #La coroutine se lance lorsque le bot est bien opérationnel.
    print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message): #La coroutine se lance lorsqu'un nouveau message est envoyé
    if message.author == client.user: #On ne veut pas que le bot réponde à ses propres messages
        return
    try: #On regarde si le message a été envoyé par le webhook
        txt = open('url.txt', 'r')
        txt_id = txt.readline()
        if int(message.webhook_id) == int(txt_id): #Si le message vient du bot on peut faire les actions necessaires et on récupère l'username
            mess = message.content.split()
            name = mess[0]
            answer = 'Bien reçu ! Je démute ' + str(name) + '!!!'
            await message.channel.send(answer)
        txt.close()
    except: #Sinon on passe aux conditions suivantes
        txt.close()
        pass
    if message.content.startswith(f'{chara}help') or client.user.mentioned_in(message): #Pour afficher la page d'aide quand elle sera faite...
        await message.channel.send('aide')
    if message.content.startswith(f'{chara}setup'): #Le setup permet de créer le webhook dans le bon channel (chaque webhook est lié à un channel seulement)
        channel = message.channel
        k=0
        webhook_list = await channel.webhooks() #On prend la liste des webhook du channel pour vérifier si il n'est pas déja créé
        txt = open('url.txt', 'r')
        txt_id = txt.readline()
        txt.close()
        for webhook in webhook_list:
            if webhook.id == int(txt_id):
                k=1
        if k==0: #Le webhook n'est pas créé : on le crée
            webhook_img = open('webhook_img.jpg','rb') #On choisit la belle image du webhook
            img = webhook_img.read()
            webhook_created = await channel.create_webhook(name='Etoiles',avatar=img) #création
            webhook_img.close()
            id = str(webhook_created.id) #webhook_id
            token = webhook_created.token #webhook_token
            webhook_url = 'discordapp.com/api/webhooks/' + str(id) + '/' + str(token) #webhook_url
            txt = open('url.txt','w')
            for L in [id, token, webhook_url]:
                txt.write(L+'\n')
            txt.close()
            check = 'WebHook créé !'
            await channel.send(check)
        else:
            await channel.send('Ce channel est déjà prêt.') #Le webhook est déja créé, on ne fait rien.
    if message.content.startswith(f'{chara}clear'): #Permet de clean tous les webhooks du channel créés par le bot. A utiliser en cas de pb.
        channel = message.channel
        webhook_list = await channel.webhooks()
        nbr = 0
        for webhook in webhook_list:
            if str(webhook.user) == str(client.user):
                await webhook.delete()
                nbr+=1
        check = str(nbr) + ' Webhook(s) supprimé(s)'
        await channel.send(check)



if __name__ == "__main__":
    client.run('Nzc0NDE1MjE3NjQ3OTQzNjgy.X6XcXw.UIe9ZesQhp4RGU1yB_xUtTI2oi0') #On run le bot avec son token secret mis à la zeub :)
    pass