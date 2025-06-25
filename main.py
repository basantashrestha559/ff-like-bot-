import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # ✅ This line is required!

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Logged in as {bot.user}')

@bot.command()
async def like(ctx, uid):
    await ctx.send(f"Sending like to UID: {uid}")
    # Example: API request logic can go here
    # requests.get(f"https://your-api.com/send-like?uid={uid}")

bot.run(os.getenv("TOKEN"))
