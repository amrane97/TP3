from email.policy import default
from http import client
import discord
from dotenv import load_dotenv
import os
import random

default_intents = discord.Intents.default()
default_intents.members = True #activer les intents relatifs aux membres
client = discord.Client(intents = default_intents)

load_dotenv(dotenv_path="config")
token = os.getenv("token")

class DocBot(discord.Client):
        
    @client.event
    async def on_ready(self):
        print ("Amrane's bot connected...")

    #reponse à un message
    @client.event
    async def on_message(self, message):
        if message.content == "Ping" or message.content =="ping":
            await message.channel.send("Pong")
        elif message.content == "bonjour" or message.content == "Bonjour":
            await message.channel.send("salut") #attention faut pas mettre la meme chaine que dans le if

        elif message.content.startswith("!del"):
            number = int(message.content.split()[1])
            messages = await message.channel.history(limit=number + 1).flatten() #historique des messages postés
            for each_message in messages:
                await each_message.delete()
        
        elif message.content.startswith("!help"):
            await message.channel.send("!del -chiffre- : ca vous permet de supprime les n message\n !help : vous affiche les commandes que vous pouvez utilisé \n !random (n1 n2) : genere un chiffre aleatoirement entre les 2 nombre que vous mettrez \n !play : ")
        
        elif message.content.startswith("!random"):
            a = int(message.content.split()[1])
            b = int(message.content.split()[2])
            x = random.randrange(a, b)
            await message.channel.send(x)


        elif message.content.startswith("!play"):
            number = random.randint(1,10)
            await message.channel.send('I have a number in mind between 1 and 10, guess')
            #await message.channel.send(number)
            if int(message.content) == number:
                await message.channel.send('You got it!')
            else:
                await message.channel.send("you loose")

        #*****************************************************    

    #arrivée d'un nouveau membre

    @client.event
    async def on_member_join(self, member):
        general_channel: discord.Textchannel = client.get_channel(958699791393632276)
        await general_channel.send(content=f"bienvenue sur le serveur {member.display_name} ")
        

client = DocBot()
client.run(token)


