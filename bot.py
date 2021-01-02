import discord
from discord.ext import commands

client = commands.Bot(command_prefix=".")

f = open("rules.txt","r", encoding = "utf8")
rules =f.readlines()

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def rule(ctx,*,number):
    await ctx.send(rules[int(number)-1])

@client.command(aliases=['c'])
async def clear(ctx,amount=2):
    await ctx.channel.purge(limit = amount)

@client.command(aliases=['k'])
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member,*,reason= "No reason"):
    try:
        await member.send("You have been kicked from the server because "+reason)
    except:
        await ctx.send("Member has DM closed")
    await member.kick(reason=reason)

@client.command(aliases=['b'])
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member,*,reason= "No reason"):
    try:
            await member.send("You have been banned from the server because "+reason)
    except:
        await ctx.send("Member has DM closed")

    await member.ban(reason=reason)

client.run("BOT TOKEN HERE")
