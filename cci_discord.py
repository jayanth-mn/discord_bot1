from discord.ext import commands
import discord

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

def run():
    
    @bot.event
    async def on_message(message: discord.Message):
        content = message.content
        author = message.author
        channel = message.channel

        #print(message)
        print(author)
        print(channel)
        print(content)
    #run the bot with your token
    bot.run('MTEzMzM1NDE4Mjk3MjI4NTAyOQ.Gj6khd.BfkXA-tmTttYQ4wBKVlTZ_ccfLGvH0vTYGs-dU')


run()