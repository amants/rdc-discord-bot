import discord
from dotenv import dotenv_values

# Load .env file for secret bot code
env_vars = dotenv_values(".env")

# Define the discord client class
class MyClient(discord.Client):

    # Callback when the bot is initialized
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    # Callback when a message is sent in any channel
    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run(env_vars["BOT_TOKEN"])