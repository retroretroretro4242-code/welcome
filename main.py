import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# =========================
# ENV LOAD
# =========================
load_dotenv()
TOKEN = os.getenv("TOKEN")

WELCOME_CHANNEL_ID = 1478328986013667338

# =========================
# BOT INTENTS
# =========================
intents = discord.Intents.default()
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

# =========================
# READY EVENT
# =========================
@bot.event
async def on_ready():
    print(f"{bot.user} aktif!")

# =========================
# MEMBER JOIN EVENT
# =========================
@bot.event
async def on_member_join(member: discord.Member):

    embed = discord.Embed(
        title=f"👋 Hoş geldin, {member.name}!",
        description="**Atlas Projects** ailesine katıldığın için mutluyuz.",
        color=discord.Color.blurple()
    )

    # Üye avatarı (solda)
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

    embed.set_footer(
        text=f"{member.guild.name} • Atlas Projects"
    )

    # =========================
    # KANALA MESAJ
    # =========================
    channel = bot.get_channel(WELCOME_CHANNEL_ID)

    if channel:
        await channel.send(
            content=f"🎉 {member.mention} aramıza katıldı!",
            embed=embed
        )

    # =========================
    # DM MESAJI
    # =========================
    try:
        await member.send(
            content=f"👋 {member.name}, {member.guild.name} sunucusuna hoş geldin!",
            embed=embed
        )
    except discord.Forbidden:
        print(f"{member} DM kapalı.")

# =========================
# RUN BOT
# =========================
bot.run(TOKEN)
