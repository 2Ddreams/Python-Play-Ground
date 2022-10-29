import discord
import random


TOKEN = "OTc5NzMxMjU5OTA1NDQxODMy.Gbnp6p.Q4xk3W5Y5IU0rq6MDz83wK2JdheAm8kldfVEyQ"

client = discord.Client()

# Loggin In
@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

# Message Logging
@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f"({username}) [{channel}]: {user_message} ")
    print("------------------------------------------------------------------------------------------------")

    if message.author == client.user:
        return


    # Chat Bot (bot-test-ground)
    if message.channel.name == "bot-test-ground":
        if user_message.lower() == "hello":
            await message.channel.send(f"Hello {username}!")
            return
        elif user_message.lower() == "bye":
            await message.channel.send(f"See you later {username}!") 
        
    # Accessable Everywhere
    if user_message.lower() == "!anywhere":
            await message.channel.send(f"This can be used anywhere!")
            return
    if user_message.lower() == "!random":
        response = f"This is your random number {random.randrange(10)}" 
        await message.channel.send(response)


    # Character Information
    if message.channel.name == "character-information":
        await message.channel.send(f"https://u.gg/lol/champions/{user_message.lower()}/build")
        



client.run(TOKEN)