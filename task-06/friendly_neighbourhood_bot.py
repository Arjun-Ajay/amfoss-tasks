import discord
from discord.ext import commands
from dotenv import load_dotenv
import asyncio
import os
import mytexts

load_dotenv()
token=os.getenv("DISCORD_TOKEN")
orientation_channel_id=int(os.getenv("ORIENTATION_CHANNEL_ID"))
new_student_role_id=int(os.getenv("NEW_STUDENT_ROLE_ID"))
annoucnement_channel_id=int(os.getenv("ANNOUNCEMENT_CHANNEL_ID"))
Authorised_role=["Faculty","Administrator"]

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

FORBIDDEN_KEYWORDS=["villainous spam","unauthorized link","off-topic disruption","menacing threats"]

async def auto_delete(msg):
    time_in_secs=30 #CHANGE TO CONTROL THE TIME UNTIL DELETION (24hr - 86400sec)
    #print(msg.pinned)
    if msg.pinned==False:
        await asyncio.sleep(time_in_secs)
        await msg.delete()

bot = commands.Bot(command_prefix='??',description=mytexts.description,intents=intents)
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}.\nBot is now running")
    print('------------')
    print()
 

@bot.event
async def on_member_join(member):
    orientation_channel=bot.get_channel(orientation_channel_id)
    #print(type(orientation_channel_id))  #debugging id type
    #print(orientation_channel)           #confirming channel
    new_student_role=member.guild.get_role(new_student_role_id)

    await orientation_channel.send(f"Welcome to the server {member.mention} 🎉🎉.\nType '??help' to get started")
    await member.add_roles(new_student_role)


@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return
    
    for keyword in FORBIDDEN_KEYWORDS:
        if keyword in msg.content.lower(): 
            await msg.delete()
            await msg.channel.send(f"{msg.author.mention} - chaos-inducing messages and activities are not permitted on this server. You have been warned.")
            await msg.author.send("Keep all messages and activities on the server civil and respectful. " \
            "Our code of conduct promotes constructive communication to provide a safe environment for all members of the server.\n"\
            "Further violation of our code of conduct will result in a permanent ban from the server")
    await bot.process_commands(msg)


@bot.command()
@commands.has_any_role(*Authorised_role)
async def bugle(ctx,*,content:str):
    annoucement_channel=bot.get_channel(annoucnement_channel_id)
    announcement_msg=await annoucement_channel.send(f"OFFICIAL ANOUNCEMENT BY {ctx.author.mention}:\n\n{content}")
    await ctx.send(f"{ctx.author.mention} - Your announcement has been posted in the annoucement channel")
    print(announcement_msg.pinned)
    bot.loop.create_task(auto_delete(msg=announcement_msg))

@bugle.error
async def bugle_error(ctx,error):
    if isinstance(error, commands.MissingAnyRole):
        await ctx.send(f"{ctx.author.mention} - You do not have the permission to use this command.")


@bot.command()
async def wisdom(ctx,*,content:str):
    if content.lower()=="rules":
        await ctx.send(mytexts.RULES)
    elif content.lower()=="resources":
        await ctx.send(mytexts.RESOURCES)
    elif content.lower()=="contacts":
        await ctx.send(mytexts.CONTACTS)
    else:
        await ctx.send(f"{ctx.author.mention} - Invalid command usage. Use '??help' for more information")

#NOTE: Update command descriptions
#NOTE: Implement pinned msg persistance on #announcements
bot.run(token)