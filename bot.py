import os, re, dotenv, discord
from discord import option, ApplicationContext as Context, Message

bot = discord.Bot()

@bot.command()
@discord.option("target", description="l'accusé·e", type=discord.SlashCommandOptionType.user)
@discord.option("reason", description="la raison du cancel", type=discord.SlashCommandOptionType.string)
async def cancel(ctx, target, reason):
    await ctx.respond(f"target: {target.avatar}, reason={reason}")

@bot.event
async def on_ready():
    print(f"logged in as {bot.user}")

dotenv.load_dotenv()
bot.run(os.getenv("DISCORD_TOKEN"))
