import os, re, dotenv, discord, requests
from PIL import Image
from io import BytesIO
from discord import option, ApplicationContext as Context, Message

bot = discord.Bot()

@bot.command()
@discord.option("target", description="l'accusé·e", type=discord.SlashCommandOptionType.user)
@discord.option("reason", description="la raison du cancel", type=discord.SlashCommandOptionType.string)
async def cancel(ctx, target, reason):
    img = Image.open(requests.get(target.avatar, stream=True).raw)
    img = img.resize((256,256))
    img = img.transpose(Image.FLIP_LEFT_RIGHT)

    bytes = BytesIO()
    img.save(bytes, format="PNG")
    bytes.seek(0)

    await ctx.respond(f"raison : {reason}, type: {type(bytes)}", file=discord.File(bytes, filename="target.png"))

@bot.event
async def on_ready():
    print(f"logged in as {bot.user}")

dotenv.load_dotenv()
bot.run(os.getenv("DISCORD_TOKEN"))
