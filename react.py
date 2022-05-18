import discord
from discord.ext import commands
from core.classes import Cog_Extension

class React(Cog_Extension):
    
    @commands.Cog.listener()
    async def on_message(self,msg):
        replyDict ={

            '礦渣':'OK YOU WIN',
            '134tc':'勇嘎感瓦徐',
            '腳點':'. Italian 鍾岳停腳點滑鼠',
        
        }
        reply = replyDict[ msg.content ]
        if reply is not None:
            await msg.channel.send(reply)

def setup(bot):
    bot.add_cog(React(bot))