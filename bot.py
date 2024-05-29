# bot.py
# bot.py
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    slime_quotes = [
        'Quit',
        'You dont have a chance!',
        'hello please all cease making skins and only upload on my account, '
        'no cases for over a year',
        'no more cases',
        'time to take a break',
        'they will surley pick me',
        'stick to rust ty',
        'it is unfortunate',
        'Please move on with your lives',
        'I am a valve employee',
        'I work at valve',
        'Shut-up fam',
        'pooping your pants is free',
        'sounds like a skill issue',
        'its so over',
        'calm down',
        'LOOKS SIMILAR TO ANOTHER ON  OF THE 158K SKINS THAT ARE MADE',
        'this why they should only accept me',
        'that looks exactly like ai art',
        'its never been more over',
        'All stop making anything now',
        'Im going to make sure there are more ai skins',
        'All stop',
        'hello everyone please switch to rust workshop'
        'hello the council of slime has decided your design is too close to bloodsport',
        'actual dmca incoming',
        'all exit workshop',
        'you can do it',
        'you will not find what you are looking for here',
        'all quit workshop it is pointless',
        'you need to make stickers',
        '1/25000 chances each time!',
        'seek meaning elsewhere in life',
        'none of you will get accepts',
        'i literally have 0 cs2 accepts',
        'i wonder when i will get cs2 accept',
        'all make maps',
        'imagine you get accepted and its an operation accept',
        'just make skins or quit its that easy',
        'go back to tf2 where you belong',
        'my lawyers will be in touch shortly',
        'do NOT leave your house EVER again',
        '(it was never cool)',
        'seems a huge waste of time',
        'do not use plasticity do not read about plasticitiy',
        'please stop making content',
        'HAHAH',
        'take another rest day you deserve it',
        'dont worry it is very low chances of being picked anyway',
        'why your skin look like that',
        'just do it bro',
        'you have been placed on the sabotage list',
        'help my tummy hurts',
        'you are a rat',
        'yes your skin was reviewed in game and rejected',
        'do one with your face on it',
        'its all a scam',
        'bro is less useful than a lump of mincemeat',
        'it looks nothing like cs art style',
        'start playing tinwhistle',
        'everyone quit except people from 2015 tyvm',
        'you will all be studied in a lab',
        'nmaking skins is so boring',
        'please all pursue your dreams',
        'this guy annoys me',
        'you are all spiritually fat',
        'post process andys can not cope',
        '🫵🤣🫵', #point at user emoji
        '👉💀👈',
        'slime_21.png',

    ]


    if message.content == 'motivate':
        response = random.choice(slime_quotes)
        if ".png" in response:
            await message.reply(file=discord.File(response))
        else:
            await message.reply(response)


client.run(TOKEN)