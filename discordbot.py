import discord
import os

token = os.environ['bot_token']

client = discord.Client()

# ここからプログラム
prefix = '_'
casting = []

@client.event
async def on_ready():
    print('**---起動しました--**')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content[0] == prefix:
        cmd = message.content.split()[0][1:]
        args = message.content.split()[1:]
        if cmd == 'test':
            await message.channel.send('**---Botは正常にインストールされています---**')
        elif cmd == 'prefix':
            prefix = args[0]
        
client.run(token)
