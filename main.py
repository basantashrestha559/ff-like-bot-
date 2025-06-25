import discord
from discord.ext import commands
import requests
import os

# Use your actual API key
API_KEY = "Prabin9001"
BASE_URL = "https://likes.api.freefireofficial.com/api/sg/"

# Discord bot token (will be set from Render environment)
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN", "your_discord_bot_token_here")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot is online as {bot.user}")

@bot.command()
async def like(ctx, uid):
    try:
        url = f"{BASE_URL}{uid}?key={API_KEY}"
        res = requests.get(url)
        data = res.json()
        before = data.get("likes_before", "N/A")
        after = data.get("likes_after", "N/A")
        await ctx.send(f"👍 UID: {uid}\nBefore: {before} Likes\nAfter: {after} Likes")
    except Exception as e:
        await ctx.send(f"❌ Error: {e}")

bot.run(DISCORD_TOKEN)
