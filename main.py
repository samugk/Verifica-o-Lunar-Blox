import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot conectado com sucesso como {bot.user}!")

if __name__ == "__main__":
    if TOKEN:
        bot.run(TOKEN)
    else:
        print("Erro: DISCORD_TOKEN não foi encontrado no .env!")