import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True
intents.members = True  

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is online! Logged in as {bot.user}")

@bot.command()
async def play(ctx, *, opponent: str = None):
    if opponent is None:
        await ctx.send("Please mention your opponent. Example: !play @opponent")
        return

    if opponent.startswith("<@") and opponent.endswith(">"):
        opponent = opponent.replace("<", "").replace(">", "").replace("@", "").replace("!", "")
        
    try:
        opponent_member = ctx.guild.get_member(int(opponent))
    except (ValueError, TypeError):
        await ctx.send("Invalid mention or user not found.")
        return

    if opponent_member is None:
        await ctx.send("Could not find the mentioned user.")
        return

    print(f"Opponent Member: {opponent_member}")

    if ctx.author == opponent_member:
        await ctx.send("You cannot challenge yourself!")
        return

    if opponent_member.bot:
        await ctx.send("You cannot challenge another bot!")
        return

    # Game logic for Rock, Paper, Scissors, Lizard, Spock
    choices = ["ROCK", "PAPER", "SCISSORS", "LIZARD", "SPOCK"]
    author_choice = random.choice(choices)
    opponent_choice = random.choice(choices)

    await ctx.send(f"{ctx.author.mention} chooses *{author_choice}*!")
    await ctx.send(f"{opponent_member.mention} chooses *{opponent_choice}*!")


    rules = {
        "ROCK": ["SCISSORS", "LIZARD"],
        "PAPER": ["ROCK", "SPOCK"],
        "SCISSORS": ["PAPER", "LIZARD"],
        "LIZARD": ["PAPER", "SPOCK"],
        "SPOCK": ["ROCK", "SCISSORS"],
    }

    if author_choice == opponent_choice:
        await ctx.send("It's a tie!")
    elif opponent_choice in rules[author_choice]:
        await ctx.send(f"{ctx.author.mention} says: *I WON!*")
    else:
        await ctx.send(f"{opponent_member.mention} says: *I WON!*")

bot.run("MTMxMjEwMDczNjY2NjE3NzU2Ng.GePMTG.G4Wxi-ISUng-qKYbX0ydhjh85LHC7LlnHME4LA")