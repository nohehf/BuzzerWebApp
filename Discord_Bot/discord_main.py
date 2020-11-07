import discord


intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
chara = '_'
channel_setup = None


@client.event
async def buzzer_discord():
    print(channel_setup)
    await channel_setup.send('Buzzed')
    return 'y'

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print(client.guilds)
    global all_guilds
    all_guilds = client.guilds
    print(all_guilds)
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    try:
        if message.webhook_id == 774626469237358642:
            await message.channel.send('Bonjour Rayou !')
    except:
        pass
    if message.content.startswith(f'{chara}help') or client.user.mentioned_in(message):
        await message.channel.send('aide')
    if message.content.startswith(f'{chara}setup'):
        global channel_setup
        channel_setup = message.channel
        check = 'Channel is set to ' + str(message.channel)
        await message.channel.send(check)
    if message.content.startswith(f'{chara}check'):
        await message.channel.send(channel_setup)
    if message.content.startswith(f'{chara}def'):
        buzzer_discord()


if __name__ == "__main__":
    client.run('Nzc0NDE1MjE3NjQ3OTQzNjgy.X6XcXw.UIe9ZesQhp4RGU1yB_xUtTI2oi0')
    pass