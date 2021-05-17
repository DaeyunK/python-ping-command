#pip install discord
#pip install commands
import discord
from discord.ext import commands

app = commands.Bot(command_prefix='-', case_insensitive=True, help_command=None)

@app.command()
async def 핑(ctx):
        embed = discord.Embed(title=f"퐁 , 지연속도(ms) :  {app.latency} ms")
        await ctx.send(embed=embed)

#명령어 : -핑

app.run("TOKEN")
