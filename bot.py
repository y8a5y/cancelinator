import os, dotenv, discord
from discord import option, ApplicationContext as Context, Message
from src.cancel_utils import generate_response, edit_avatar

bot = discord.Bot()

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
    response_msg = generate_response(ctx.author.id, target.id, reason)
    avatar_file = discord.File(edit_avatar(target.avatar), filename="canceled.png")

    await ctx.respond(
        content=response_msg,
        file=avatar_file,
    )

@bot.event
async def on_ready():
    print(f"logged in as {bot.user}")

dotenv.load_dotenv() # loads .env file, if any
bot.run(os.getenv("DISCORD_TOKEN"))
