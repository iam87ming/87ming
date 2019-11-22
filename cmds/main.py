import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import datetime

with open('setting.json', 'r', encoding='utf8')as jfile:
    jdata = json.load(jfile)


class Main(Cog_Extension):
    
    @commands.command ()
    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}(ms)')

    @commands.command()
    async def hi(self,ctx):
        await ctx.send('HI你老母,芝士漢堡!')

    @commands.command()
    async def em(self,ctx):
        embed=discord.Embed(title="about", url="https://giphy.com/gifs/swaps4-xULW8io3Em6y3lrIYM", description="about the bot", color=0x00ff80, timestamp=datetime.datetime.utcnow())
        embed.set_author(name="Bot is shit", url="https://giphy.com/gifs/poputepipikku-EtFNtaj8sQKuA", icon_url="https://media.giphy.com/media/EtFNtaj8sQKuA/giphy.gif")
        embed.set_thumbnail(url="https://media.giphy.com/media/xULW8io3Em6y3lrIYM/giphy.gif")
        embed.add_field(name="屌", value="87", inline=False)
        embed.add_field(name="你", value="ming", inline=True)
        embed.add_field(name="老", value="love", inline=False)
        embed.add_field(name="母", value="001", inline=True)
        embed.set_footer(text="Hi your ass")
        await ctx.send(embed=embed)

    @commands.command()
    async def sayd(self,ctx, *,msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def clean(self,ctx,num:int):
        await ctx.channel.purge(limit=num+1)

def setup(bot):
    bot.add_cog(Main(bot))
