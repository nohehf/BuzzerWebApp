import discord

client = discord.Client()
chara = '_'

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(f'{chara}help') or client.user.mentioned_in(message):
        await message.channel.send('aide')

if __name__ == "__main__":
    client.run('Nzc0NDE1MjE3NjQ3OTQzNjgy.X6XcXw.UIe9ZesQhp4RGU1yB_xUtTI2oi0')
    pass