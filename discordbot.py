import discord
import os

token = os.environ['bot_token']

client = discord.Client()

@client.event
async def on_ready():
    print('**---起動しました--**')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '_test':
        await message.channel.send('**---Botは正常にインストールされています---**')

client.run(token)
