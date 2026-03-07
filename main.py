import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# =========================
# ENV LOAD
# =========================
load_dotenv()
TOKEN = os.getenv("TOKEN")

WELCOME_CHANNEL_ID = 1479868699463913789

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
        description="**PRX | Prime Raiders** ailesine katıldığın için mutluyuz. Biz bir e-spor takımıyız ve seni takımımızda görmek için sabırsızlanıyoruz!",
        color=discord.Color.blurple()
    )

    # Üye avatarı (solda)
    embed.set_thumbnail(url=member.display_avatar.url)

    embed.add_field(
        name="🌐 Takım Olanaklarımız",
        value=(
            "• Profesyonel e-spor deneyimi\n"
            "• Düzenli turnuvalar ve antrenmanlar\n"
            "• Özel Discord topluluğu\n"
            "• Takım koçluğu & rehberlik"
        ),
        inline=False
    )

    embed.add_field(
        name="🚀 Başarılarımız",
        value="10+ yıl e-spor tecrübesi • 200+ turnuva • 3000+ aktif oyuncu",
        inline=False
    )

    embed.set_footer(
        text=f"{member.guild.name} • PRX | Prime Raiders"
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
            content=(
                f"👋 {member.name}, {member.guild.name} sunucusuna hoş geldin! "
                "PRX ekibi seni rekabetçi oyunlarda ve turnuvalarda görmek için sabırsızlanıyor!"
            ),
            embed=embed
        )
    except discord.Forbidden:
        print(f"{member} DM kapalı.")

# =========================
# RUN BOT
# =========================
bot.run(TOKEN)
