# bot.py
# bot.py
import os
import random

import discord
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


class myclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            print(f"Syncing command tree")
            self.synced = True
        else:
            print(f"Bot is ready!")


client = myclient()

tree = app_commands.CommandTree(client)



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
    'hello everyone please switch to rust workshop',
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
    '/home/container/slimebot/slime_21.png',
    'that is the dumbest thing i have ever seen',
    'quickly everyone update all your skins to validate',
    'remesh makes my pc explode everytime',
    'Anyone holding out inside info from me will pay the ultimate price',
    'you have a full set of teeth because you are not british',
    'they will surley pick me',
    'i hate using substance so much',
    'its like workshop but you can smell the other workshopers',
    'few understand',
    'you have exposed yourself you fool it was a test',
    'you are so interesting'
]




@tree.command(name="motivate")
@app_commands.checks.cooldown(1, 300, key=lambda i: (i.user.id))
async def motivate(interaction: discord.Integration):
    response = random.choice(slime_quotes)
    if ".png" in response:
        try:
            await interaction.response.send_message(file=discord.File(response), content="<https://www.youtube.com/watch?v=dQw4w9WgXcQ>")
        except Exception as e:
            print(e)
    else:
        await interaction.response.send_message(f"{interaction.user.mention} {response}")


@tree.error
async def on_app_command_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    if isinstance(error, app_commands.CommandOnCooldown):
        await interaction.response.send_message(f"{error} to redeem more motivation", ephemeral=True)
    else: raise error

client.run(TOKEN)