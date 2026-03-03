import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

WELCOME_CHANNEL_ID = 1478328986013667338

intents = discord.Intents.default()
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user} aktif!")


@bot.event
async def on_member_join(member: discord.Member):

    channel = bot.get_channel(WELCOME_CHANNEL_ID)
    if not channel:
        return

    embed = discord.Embed(
        title=f"👋 Hoş geldin, {member.name}!",
        description="**Atlas Projects** ailesine katıldığın için mutluyuz.",
        color=discord.Color.blurple()
    )

    embed.set_thumbnail(url=member.display_avatar.url)

    embed.add_field(
        name="🌐 Hizmetlerimiz",
        value=(
            "• Web sitesi yazılım & geliştirme\n"
            "• E-ticaret sistemleri\n"
            "• Özel Discord bot geliştirme\n"
            "• FiveM & Minecraft çözümleri"
        ),
        inline=False
    )

    embed.add_field(
        name="🚀 Deneyim",
        value="10+ yıl tecrübe • 200+ sunucu • 3000+ sipariş",
        inline=False
    )

    embed.set_footer(text=f"{member.guild.name} • Atlas Projects")

    await channel.send(
        content=f"🎉 {member.mention} aramıza katıldı!",
        embed=embed
    )


bot.run(TOKEN)
