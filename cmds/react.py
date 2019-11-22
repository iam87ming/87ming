import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json', 'r', encoding='utf8')as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):

    @commands.command()
    async def crycat(self, ctx):
     random_crycat = random.choice(jdata['crycat'])
     crycat = discord.File(random_crycat)
     await ctx.send(file=crycat)

    @commands.command()
    async def jojo(self, ctx):
     random_jojo = random.choice(jdata['url_jojo'])
     await ctx.send(random_jojo)

    @commands.command()
    async def ming(self, ctx):
     random_ming= random.choice(jdata['87ming'])
     ming = discord.File(random_ming)
     await ctx.send(file=ming)

def setup(bot):
    bot.add_cog(React(bot))   

