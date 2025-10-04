import os, re, dotenv, discord, requests
from PIL import Image, ImageOps
from io import BytesIO
from discord import option, ApplicationContext as Context, Message

bot = discord.Bot()
overlay = Image.open(r"assets/cancel.png").convert("RGBA")

@bot.slash_command(
    name="cancel",
    description="Parce que même la liberté d'expression a ses limites."
)
@discord.option(
    name="qui",
    parameter_name="target",
    description="l'accusé·e",
    type=discord.SlashCommandOptionType.user
)
@discord.option(
    name="pourquoi",
    parameter_name="reason",
    description="la raison (totalement justifiée) du cancel (max 300 caractères)",
    type=str,
    max_length=300
)
async def cancel(ctx, target, reason):
    avatar = Image.open(requests.get(target.avatar, stream=True).raw)

    # L mode converts to greyscale
    # then back to RGBA so overlay doesn't get greyscaled
    avatar = avatar \
        .convert("L") \
        .convert("RGBA") \
        .resize((256, 256))

    avatar.paste(overlay, mask=overlay)

    # saving to bytes
    bytes = BytesIO()
    avatar.save(bytes, format="PNG")
    bytes.seek(0)

    if ctx.author.id == target.id:
        tag_msg = f"<@{ctx.author.id}> s'est auto-cancel."
    else:
        tag_msg = f"<@{ctx.author.id}> a cancel <@{target.id}>.",

    await ctx.respond(
        tag_msg + f"\nRaison invoquée : {reason}",
        file=discord.File(bytes, filename="canceled.png")
    )

@bot.event
async def on_ready():
    print(f"logged in as {bot.user}")

dotenv.load_dotenv() # loads .env file, if any
bot.run(os.getenv("DISCORD_TOKEN"))
