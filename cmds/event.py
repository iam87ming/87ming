import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json', 'r', encoding='utf8')as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self,member):  
      channel = self.bot.get_channel(int(jdata['Shit']))
      await channel.send(f'{member}join this group for what 7 啊屌你啦!')
 
    @commands.Cog.listener()
    async def on_member_remove(self,member):
      channel = self.bot.get_channel(int(jdata['Shit']))
      await channel.send(f'{member}我屌你老母啦leave what 7!')

    @commands.Cog.listener()
    async def on_message(self,msg):
      keyword = ['ming','87ming','001','boss']
      if msg.content in keyword  and msg.author != self.bot.user:
         await msg.channel.send('I love 001 !')
      gg = ['hi','Hi','Hello','Good morning']
      if msg.content in gg  and msg.author != self.bot.user:
         await msg.channel.send('HI你老母,芝士漢堡!')

        


        

def setup(bot):
    bot.add_cog(Event(bot))  