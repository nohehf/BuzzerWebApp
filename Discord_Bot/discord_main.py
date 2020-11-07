import discord


intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
chara = '_'

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    try:
        if message.webhook_id == 774626469237358642:
            mess = message.content.split()
            name = mess[0]
            answer = 'Bien reçu ! Je démute ' + str(name) + '!!!'
            await message.channel.send(answer)
    except:
        pass
    if message.content.startswith(f'{chara}help') or client.user.mentioned_in(message):
        await message.channel.send('aide')
    if message.content.startswith(f'{chara}setup'):
        channel = message.channel
        k=0
        webhook_list = await channel.webhooks()
        print(webhook_list)
        for webhook in webhook_list:
            print(str(webhook))
            if str(webhook) == 'WeBuzzerBot':
                k=1
        if k==0:
            webhook_created = await channel.create_webhook(name='WeBuzzerBot')
            id = webhook_created.id
            token = webhook_created.token
            webhook_url = 'discordapp.com/api/webhooks/' + str(id) + '/' + str(token)
            txt = open('url.txt','w')
            txt.write(webhook_url)
            txt.close()
            check = 'WebHook créé ! url= ' + webhook_url
            await channel.send(check)
        else:
            await channel.send('Ce channel est déjà prêt.')



if __name__ == "__main__":
    client.run('Nzc0NDE1MjE3NjQ3OTQzNjgy.X6XcXw.UIe9ZesQhp4RGU1yB_xUtTI2oi0')
    pass