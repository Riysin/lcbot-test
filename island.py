import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json','r', encoding = 'utf8') as jfile:
    jdata = json.load(jfile)

class Island(Cog_Extension):
   

    @commands.command()
    async def 隕石(self,ctx):
        pic = discord.File('C:\\Users\\Orange\\Desktop\\pics\\face\\unknown.png')
        await ctx.send(file = pic)

    @commands.command()
    async def jigsawrush(self,ctx):
        pic = discord.File('C:\\Users\\Orange\\Desktop\\pics\\face\\jigsaw_rush.png')
        await ctx.send(file = pic)

    @commands.command()
    async def partygames(self,ctx):
        random_pic = random.choice(jdata['pg_gif'])
        await ctx.send(random_pic)

    @commands.command()
    async def brotherteam(self,ctx):
        pic = discord.File('C:\\Users\\Orange\\Desktop\\pics\\face\\3.png')
        await ctx.send(file = pic)

    @commands.command()
    async def IceCream(self,ctx):
        pic = discord.File('C:\\Users\\Orange\\Desktop\\pics\\face\\ice.png')
        await ctx.send(file = pic)

def setup(bot):
    bot.add_cog(Island(bot))