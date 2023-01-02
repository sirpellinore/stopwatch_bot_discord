import time
import discord

def time_convert(sec):
    hours = sec // 3600
    mins = (sec - (hours * 3600))//60
    sec = sec - hours * 3600 - mins * 60
    str = "{0}:{1}:{2}".format(int(hours),int(mins),sec)
    return str

"""function that never got used
accumulated_time=0

def stopwatch(start_time):
    end_time = time.time()
    time_lapsed = end_time - start_time
    accumulated_time += time_lapsed
    time_info = ["Time elapsed:",time_convert(time_lapsed),"Accumulated time:",time_convert(accumulated_time)]
    return time_info """

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

"""function that never got used
def has_space(str):
    for i in range(len(str)):
        if str[i] == ' ':
            bool = True
            break
        else:
            bool = False
    return bool"""



intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)



""" make stopwatch bot speak """

"""
@client.event
async def on_ready():
    channel_info = client.get_channel(1054253491238993940)
    await channel_info.send("Hello. I am the only bot on the server")
    await channel_info.send("Using me is easy! There are 3 commands!")
    await channel_info.send("The commands are 1) !activateStopwatch")
    await channel_info.send("2) !deactivateStopwatch and 3) !calculateTime")
    await channel_info.send("C1 does exactly what it says! It activates the stopwatch!")
    await channel_info.send("C2 deactivates the stopwatch!")
    await channel_info.send("C3 is a little tricky. You have to type...")
    await channel_info.send("!calculateTime followed a space, then the number that the stopwatch sent when you activated it, then another space, and finally the number the stopwatch sent when you deactivated it")
    await channel_info.send("Like this:")
    await channel_info.send("!calculateTime 123 345")
    await channel_info.send("That is honestly all there is to using the stopwatch bot! Have fun with it!!")"""

""" make stopwatch bot respond to commands"""


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

    


client.run('MTA1NDExODgzNjEyNDc3ODUyNg.Gs9MTZ.k04iEY3gM8P9E9GkO_mXtgi6nVAKeGGCirNAhY')