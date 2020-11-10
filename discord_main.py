import discord
import asyncio
import time

#CONFIG FILE:
from configparser import ConfigParser
config = ConfigParser()
config.read("config.ini")


# Initialisation du bot
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

# Paramétrage du bot
bot_token = config["DISCORD"]['token'] # Le token du bot mis à la zeub (pas très secure :) )
chara = config["DISCORD"]['chara'] # Le charactère pour les commandes

@client.event # La décoration indique au bot qu'un évènement vient après : c'est comme cela que fonctionne le bot.
async def on_ready(): # La coroutine se lance lorsque le bot est bien opérationnel.
    print('We have logged in as {0.user}'.format(client))
@client.event # La décoration indique au bot qu'un évènement vient après : c'est comme cela que fonctionne le bot.
async def on_message(message): # La coroutine se lance lorsqu'un nouveau message est envoyé
    if message.author == client.user: # On ne veut pas que le bot réponde à ses propres messages
        return
    try: # On regarde si le message a été envoyé par le webhook
        txt_id = config['WEBHOOK']['webhook_id']
        if int(message.webhook_id) == int(txt_id): # Si le message vient du bot on peut faire les actions necessaires et on récupère l'id
            start = time.time() # On lance le chrono !
            mess = message.content
            name = mess[:-9]
            guild = message.guild
            VoiceChannel_name = config['DISCORD']['voicechannel'] # On lit le salon vocal du setup
            member_buzzer = discord.utils.get(guild.members,display_name=name)  # On essaie d'avoir le membre correspondant à au surnom (ou nom) fourni
            if member_buzzer == None:
                member_buzzer = discord.utils.get(guild.members,name=name)  # On essaie d'avoir le membre correspondant au nom fourni
                if member_buzzer == None:
                    member_buzzer = discord.utils.get(guild.members,id=name)  # On essaie d'avoir le membre correspondant à l'id fourni
            VoiceChan = discord.utils.get(guild.voice_channels, name=str(VoiceChannel_name))
            whitelist = config["DISCORD"]['whitelist']
            try:
                whitelist.append(member_buzzer.id) #... à laquelle on ajoute temporairement le membre qui a buzzé.
            except:
                pass
            for member in VoiceChan.members: # Pour chaque membre du salon vocal, on regarde si il est dans la whitelist
                if str(member) in whitelist:
                    await member.edit(mute=False) # Oui, on le démute
                else:
                    await member.edit(mute=True) # Non, on le mute
            end = time.time() # On stop le chrono !
            délai = end - start
            check = 'Voila ! Fait en ' + str(round(délai,2)) + ' secondes!'
            await message.channel.send(check)
    except: # Sinon on passe aux conditions suivantes
        pass
    if message.content.startswith(f'{chara}help') or client.user.mentioned_in(message): # Pour afficher la page d'aide sous forme d'embed
        embed = discord.Embed(title="BuzzerWebApp Help Sheet", description="List of all the availables commands :")
        embed.add_field(name=f"{chara}setup ",
                        value="Start the setup phase. You have to send it in the TextChannel where the game will take place. You will be able to choose the VoiceChannel afterwards.",
                        inline=False)
        embed.add_field(name=f"{chara}clear",
                        value="Clear the WebHook created by the bot in this TextChannel. Use only if the WebHook is not responding.",
                        inline=True)
        await message.channel.send(embed=embed)
    if message.content.startswith(f'{chara}setup'): # Le setup permet de créer le webhook dans le bon channel (chaque webhook est lié à un channel seulement)
        channel = message.channel
        k=0
        webhook_list = await channel.webhooks() # On prend la liste des webhook du channel pour vérifier si il n'est pas déja créé
        txt_id = config['WEBHOOK']['webhook_id']
        for webhook in webhook_list:
            if webhook.id == int(txt_id):
                k=1
        if k==0: # Le webhook n'est pas créé : on le crée
            webhook_img = open('webhook_img.jpg','rb') #On choisit la belle image du webhook
            img = webhook_img.read()
            webhook_created = await channel.create_webhook(name='Etoiles',avatar=img) #création
            webhook_img.close()
            id = str(webhook_created.id) #webhook_id
            config["WEBHOOK"]["webhook_id"] = id
            token = webhook_created.token #webhook_token
            config["WEBHOOK"]["webhook_token"] = token
            with open('config.ini', 'w') as conf:
                config.write(conf)
            check = 'WebHook créé !'
            await channel.send(check)
        else:
            await channel.send('WebHook déja configuré.') # Le webhook est déja créé, on ne fait rien.
        await channel.send("Veuillez rentrer le nom du channel vocal où se passe l'évènement :")
        try:
            reponse = await client.wait_for("message", timeout=30) # On attend la réponse d'un membre : on arrête après 30 secondes
            try:
                reponse = reponse.content
                guild = message.guild
                VoiceChan = discord.utils.get(guild.voice_channels, name=reponse) # On prend le salon vocal qui correspond au mieux à la réponse donnée
                if VoiceChan == None: # Si il n'y en n'a pas, on raise et on affiche un message d'erreur
                    raise
                check = 'Le Channel sélectionné est : '+str(VoiceChan)+'. Voulez-vous continuer?' # Si c'est bon, on demande vérification aux membres
                message = await channel.send(check)
                emoji = '👍'
                await message.add_reaction(emoji)
                emoji = '👎'
                await message.add_reaction(emoji)
                await asyncio.sleep(1) # On tempo une seconde pour que le bot ne prenne pas en compte ses propres reactions
                try:
                    try:
                        react = await client.wait_for("reaction_add", timeout=30) # On attend la reaction d'un membre
                        react = str(react)
                        emoji = react[18]
                        print(emoji)
                        if emoji != '👍': # Si c'est 👍, on continue
                            raise # Sinon on raise :)
                        config['DISCORD']['voicechannel'] = str(VoiceChan) #ON CHANGE LE CHANNEL
                        with open('config.ini', 'w') as conf:
                            config.write(conf)

                        await message.channel.send("C'est fait!")
                    except:
                        await message.channel.send("OK, on annule tout!")
                except:
                    await message.channel.send("Arrêt de la séquence de setup pour inactivité.")

            except:
                await message.channel.send("Le nom entré est invalide, veuillez recommencer...")
        except:
            await message.channel.send("Arrêt de la séquence de setup pour inactivité.")
    if message.content.startswith(f'{chara}clear'): # Permet de clean tous les webhooks du channel créés par le bot. A utiliser en cas de pb. Pas besoin d'effacher les .txt, on réécrit dessus à chaque procédure de setup
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
    client.run(bot_token) # On run le bot avec son token secret!
    pass