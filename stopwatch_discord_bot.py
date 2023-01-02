import time
import discord

def time_convert(sec):
    hours = sec // 3600
    mins = (sec - (hours * 3600))//60
    sec = sec - hours * 3600 - mins * 60
    str = "{0}:{1}:{2}".format(int(hours),int(mins),sec)
    return str

def convert_list_into_string(list):
    string = ""
    for element in list:
        string = string + element + " "
    return string


def print_up_to_space(str):
    index = str.find(' ')
    str = str[:index]
    return str

def print_after_space(str):
    index = str.find(' ')
    str = str[index+1:]
    return str


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)



@client.event
async def on_message(message):
    
    if message.author == client.user:
        return


    if message.content.startswith("calculate:"):
        numbers = message.content[11:]
        firstNumber = print_up_to_space(numbers)
        secondNumber = print_after_space(numbers)
        time_lapsed = float(secondNumber) - float(firstNumber)
        time_lapsed = int(time_lapsed)
        msg = time_convert(time_lapsed)
        await message.channel.send(msg)
    else:
        time_info = time.time()
        msg = "{}".format(time_info)
        await message.channel.send(msg)

    


client.run(token)
