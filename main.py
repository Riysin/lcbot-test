import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json','r', encoding = 'utf8') as jfile:
    jdata = json.load(jfile)

class Main(Cog_Extension):

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} (ms)')

    @commands.command()
    async def lol(self,ctx):
        random_pic = random.choice(jdata['pic'])
        pic = discord.File(random_pic)
        await ctx.send(file = pic)

    @commands.command()
    async def welp(self,ctx):
        embed=discord.Embed(title="指令如下:", url="https://www.youtube.com/channel/UCfD_Lijbf2IDXIH89iqqqwg", color=0xffb029)
        embed.set_author(name="PvpForOrange", url="https://www.youtube.com/channel/UCfD_Lijbf2IDXIH89iqqqwg", icon_url="https://ibb.co/1Zgyxp8")
        embed.set_thumbnail(url="https://ibb.co/1Zgyxp8")
        embed.add_field(name="$welp", value="顯示此表單", inline=False)
        embed.add_field(name="$ping", value="顯示此機器人現在的延遲", inline=True)
        embed.add_field(name="$lol" , value = "隨機發送一些圖片", inline=False)
        embed.set_footer(text="叫柳橙不要偷懶快發影片")
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Main(bot))