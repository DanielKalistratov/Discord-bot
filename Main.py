import discord
import json
import secrets
import youtube_dl
from discord import Member
from discord.ext import commands
import os
from discord.ext.commands import bot
from dotenv import load_dotenv
import random
import time
import asyncio

Token = "OTc4MzE4NDc2ODI3NTgyNDc1.Gc0MTA.GZKbVvmrzei_W7SUuTfP8azYuBCvGF4ypNVePs"

client = discord.Client()

client = commands.Bot(command_prefix='!')

# Damit er online ist
@client.event
async def on_ready():
    print("online")
    client.loop.create_task(status_task())


#für seinen Status
async def status_task():
    while True:
        await client.change_presence(activity=discord.Game('Unser eigener Bratans Bot'), status=discord.Status.online)
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game('!help'), status=discord.Status.online)
        await asyncio.sleep(10)


# userinfo
@client.command()
async def userinfo(ctx, member:discord.Member=None):
    if member:
        embed = discord.Embed(title=f"Nutzerinfo von {member}",timestamp=ctx.message.created_at, color=0x22a7f0)
        embed.add_field(name="Name:", value=f"{member.mention}")
        embed.add_field(name="Server beigetreten:", value=f"{member.joined_at.strftime('%d/%m/%Y')}")
        embed.add_field(name="Discord beigetreten:", value=f"{member.created_at.strftime('%d/%m/%Y')}")
        if len(member.roles) > 1:
            rollen = ' '.join([r.mention for r in member.roles][1:])
        embed.add_field(name="Rollen [{}]".format(len(member.roles)-1), value=rollen, inline=True)
        embed.add_field(name="Höchster Rolle:", value=member.top_role.mention, inline=True)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Anfrage von - {member.name}", icon_url=member.avatar_url)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title=f"Nutzerinfo von {ctx.author}", color=0x22a7f0)
        embed.add_field(name="Name:", value=f"{ctx.author.mention}")
        embed.add_field(name="Server beigetreten:", value=f"{ctx.author.joined_at.strftime('%d/%m/%Y')}")
        embed.add_field(name="Discord beigetreten:", value=f"{ctx.author.created_at.strftime('%d/%m/%Y')}")
        if len(ctx.author.roles) > 1:
            rollen = ' '.join([r.mention for r in ctx.author.roles][1:])
        embed.add_field(name="Rollen [{}]".format(len(ctx.author.roles)-1), value=rollen, inline=True)
        embed.add_field(name="Höchster Rolle:", value=ctx.author.top_role.mention, inline=True)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.set_footer(text=f"Anfrage von - {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
d





client.run(Token)

