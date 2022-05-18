import discord
from discord.ext import commands
import json
import random
import os 

with open('setting.json','r', encoding = 'utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.default()
intents.members = True

class CustomHelpCommand(commands.HelpCommand):
    def helpcmd():
        embed=discord.Embed(title="指令如下:", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley", color=0xffb029)
        embed.set_author(name="PvpForOrange", url="https://www.youtube.com/channel/UCfD_Lijbf2IDXIH89iqqqwg", icon_url="https://i.ibb.co/1Zgyxp8/orange.png")
        embed.set_thumbnail(url="https://i.ibb.co/1Zgyxp8/orange.png")
        embed.add_field(name="^help", value="顯示此表單", inline=False)
        embed.add_field(name="^ping", value="顯示此機器人現在的延遲", inline=True)
        embed.add_field(name="^lol" , value = "隨機發送一些圖片", inline=False)
        embed.set_footer(text="叫柳橙不要偷懶快發影片")



bot = commands.Bot(command_prefix='^',intents=intents,help_commands=CustomHelpCommand())

@bot.event
async def on_ready():
    print(">>bot is online<<")

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done.')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Un-Loaded {extension} done.')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Re-Loaded {extension} done.')


for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')



#@bot.event
#async def on_member_join(member):
#   channel = bot.get_channel(908371250726973470)
#   await channel.send(f'{member} join!')

#@bot.event
#async def on_member_remove(member):
#    channel = bot.get_channel(908371250726973470)
#    await channel.send(f'{member} leave!')
if __name__ == "__main__":
    bot.run(jdata['Token'])