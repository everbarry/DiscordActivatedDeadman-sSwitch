# Discord bot for deadman's switch

import discord                                                                               # For discord bot interface
from discord.ext import commands
import hashlib                                                             # To hash inputted password and verify hashes
from time import *
import threading                                                        # To run main(), timer() and the bot in parallel
import datetime                                                                                            # For timer()
import pyAesCrypt                                                                        # To encrypt files in payload()
import os

###################################### Functions ######################################################


# Timer function
def timer():
    global time_left
    global time_out
    time_out = False
    time_left = datetime.timedelta(hours=24)                                                             # Set here time
    while time_left >= datetime.timedelta(seconds=1):
        time_left -= datetime.timedelta(seconds=1)
        sleep(1)
    if time_left <= datetime.timedelta(seconds=1):
        time_out = True
        print("Time over")
        return True


# Threading settings to run timer on background
timer_thread = threading.Thread(target=timer)
timer_thread.start()


# Authentication function
def auth(password):
    hash = b"putyourhashinhere"                 # Set password hash
    hashed_pwd = hashlib.sha512(password.encode("utf-8")).hexdigest().encode("utf-8")
    if hashed_pwd == hash:
        return True
    else:
        return False


# Payload from original deadman's switch
def FirePayload(filePath, encryptPass):
    print("Deadman don't talk")
    bufferSize = 64 * 1024                                                     # encryption/decryption buffer size - 64K
    pyAesCrypt.encryptFile(filePath, (filePath+'.aes'), encryptPass, bufferSize)                               # encrypt
    # secure_delete.secure_random_seed_init()                     # Secure delete module available for Windows and Linux
    # secure_delete.secure_delete(filePath)
    os.remove(filePath)                          # Deletes path of file, DOES NOT ACTUALLY OVERRWRITE/SECURE-DELETE FILE
    print("SWITCH ACTIVATED - LOCKDOWN MODE ENTERED")
    exit()

# Main function to setup encryption

def main():
    global time_out
    filePath = input("Insert file path: ")
    encryptPass = input("Insert pass to decrypt: ")
    while timer():                                                                     # Check when timer runs out
        print("Main got timeout true")
        FirePayload(filePath, encryptPass)


# Threading settings to run setup on background
main_thread = threading.Thread(target=main)

################################ DISCORD-BOT Section ###################################################################

client = commands.Bot(command_prefix='-')

token = 'putyourtokeninhere'           # Put your discord bot login token in here


# bot set up
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Admin Check'))
    main_thread.start()
    print("Bot is ready")


# someone enters server
@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')


# someone leaves server
@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')


# ping command
@client.command()
async def ping(ctx):
    await ctx.send(f'Command activated {round(client.latency * 1000)}ms')


# error handler
@client.event
async def on_command_error(ctx):
    await ctx.send("Error")
    print("User error")
    pass


# clear command
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


# time left before destruction
@client.command()
async def time(ctx):
    global time_left
    await ctx.send(f'Time remaining before Self-destruction: {time_left}')


# deactivate command
@client.command()
async def l(ctx, *, pwd):
    global time_out
    password = f'{pwd}'
    auth(password)
    if auth(password):
        if time_out is False:
            await ctx.channel.purge(limit=1)
            await ctx.send(f'Switch reset')
            global time_left
            time_left = datetime.timedelta(hours=24)              # Set here time
        else:
            await ctx.send(f'Too late... ')
    else:
        await ctx.send(f'Wrong code, Impostor')
        await ctx.channel.purge(limit=200)



client.run(token)
