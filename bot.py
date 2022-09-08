import discord
from discord.ext import tasks
from discord import *
import bs4
from Api import WezerApi
import discord
from discord.ext import tasks
import requests
import json
import a2s

client = discord.Client(intents=discord.Intents.all())

wapi = Api()

@tasks.loop(minutes=3)
async def update_status():
    status = wapi.get_status("IP", "PORT")


@client.event
async def on_ready():
    update_status.start()
    print('Ready!')


client.run("TOKEN")