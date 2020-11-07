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
        if message.webhook_id == 774626469237358642: #Si le message vient du bot on peut faire les actions necessaires et on récupère l'username
            mess = message.content.split()
            name = mess[0]
            answer = 'Bien reçu ! Je démute ' + str(name) + '!!!'
            await message.channel.send(answer)
    except: #Sinon on passe aux conditions suivantes
        pass
    if message.content.startswith(f'{chara}help') or client.user.mentioned_in(message): #Pour afficher la page d'aide quand elle sera faite...
        await message.channel.send('aide')
    if message.content.startswith(f'{chara}setup'): #Le setup permet de créer le webhook dans le bon channel (chaque webhook est lié à un channel seulement)
        channel = message.channel
        k=0
        webhook_list = await channel.webhooks() #On prend la liste des webhook du channel pour vérifier si il n'est pas déja créé
        for webhook in webhook_list:
            if str(webhook) == 'WeBuzzerBot':
                k=1
        if k==0: #Le webhook n'est pas créé : on le crée
            webhook_created = await channel.create_webhook(name='WeBuzzerBot') #création
            id = str(webhook_created.id) #webhook_id
            token = webhook_created.token #webhook_token
            webhook_url = 'discordapp.com/api/webhooks/' + str(id) + '/' + str(token) #webhook_url
            txt = open('url.txt','w') #on ecrit l'url dans un .txt pour faciliter l'exploitation dans les autres fichiers (jsp si cest le mieux)
            for L in [id, token, webhook_url]:
                txt.write(L+'\n')
            txt.close()
            check = 'WebHook créé ! url= ' + webhook_url
            await channel.send(check)
        else:
            await channel.send('Ce channel est déjà prêt.') #Le webhook est déja créé, on ne fait rien.



if __name__ == "__main__":
    client.run('Nzc0NDE1MjE3NjQ3OTQzNjgy.X6XcXw.UIe9ZesQhp4RGU1yB_xUtTI2oi0') #On run le bot avec son token secret mis à la zeub :)
    pass