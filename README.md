# DiscordActivatedDeadman-sSwitch
deadman's switch that encrypts files with password if you dont type a command in discord for some time

functional discord bot that when run starts a timer and if you dont message the password in a discord server it encrypts a file/folder with a password with pyAesCrypt

Bot commands:
 
 -ping : tells the bot's ping
 -clear : clears last 5 messages by default, if you want to clear more messages do: -clear [number of lines you want to clear]
 -time : tells time left to enter password
 -l [password] : is used to login and reset the timer

How to edit:

set password to type in discord:
hash your password with the password_hashing.py tool and copy hash at line 37 in discord_bot.py

set time until files are encrypted:
modify hours= value at line 20 and 135


setup:
download all imported libraries (discord, discord.ext, hashlib, pyAesCrypt)
put your discord bot token at line 74
