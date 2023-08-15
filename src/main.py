import discord
from discord.ext import commands

import os
from dotenv import load_dotenv

import requests

load_dotenv()

discord_api_key = os.getenv("DISCORD_TOKEN")
bluealliance_api_key = os.getenv("BLUEALLIANCE_API_KEY")