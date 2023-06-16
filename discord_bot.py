import discord
import time



intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.content.startswith('!travel'):
        await message.channel.send('Chwila...')

    if message.content.startswith('!info'):
        await message.channel.send('Zamiast spacji używaj znaku podłogi. Przykładowo: Wierzbowa_41 lub Stadion_Miejski')

    # Sprawdź, czy wiadomość zaczyna się od !travel i zawiera dwa argumenty oddzielone spacją
    if message.content.startswith('!travel'):
        args = message.content.split(' ')
        if len(args) == 3:
            arg1 = args[1]
            arg2 = args[2]
            print(arg1)
            print(arg2)
            from response import travel_response
            response = travel_response(arg1,arg2)
            await message.channel.send(response)


        if len(args) > 3:
            await message.channel.send('Wystąpił bład. Spróbuj ponownie lub użyj komendy !info w celu uzyskania informacji')

    if message.content.startswith('!travel_next'):
        args = message.content.split(' ')
        if len(args) == 3:
            arg1 = args[1]
            arg2 = args[2]
            print(arg1)
            print(arg2)
            from response_next import travel_response
            response = travel_response(arg1,arg2)
            await message.channel.send(response)


TOKEN = 'YOUR_TOKEN_CODE'
client.run('YOUR_TOKEN_CODE')

while True:
    pass









