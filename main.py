import discord
from discord.ext import commands
from discord.utils import get
import asyncio
from itertools import cycle
import os
from dotenv import load_dotenv

import platform

print(f"Running on: {platform.sys.version}")

load_dotenv()
TOKEN = os.environ['TOKEN']
BOT_PREFIX = '!'

bot = commands.Bot(command_prefix=BOT_PREFIX)

audio_list = ["a1.mp3", "a3.mp3"]
cycled_audio = cycle(audio_list)

delay_duration = {"a1.mp3": 0.6319047619047619,
                  "a3.mp3": 2.072380952380952,
                  }



@bot.event
async def on_ready():
    print("Logged in as: " + bot.user.name + "\n")
    activity = discord.Game(name="!microwave")
    await bot.change_presence(status=discord.Status.idle, activity=activity)


async def join(ctx):
    try:
        channel = ctx.message.author.voice.channel
    except AttributeError:
        await ctx.send(f"{ctx.message.author.mention} You need to join voice channel to use this command")
        return

    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        await channel.connect()


async def leave(ctx):
    # channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        # print(f"The bot has left {channel}")
    else:
        # print("Bot was told to leave voice channel, but was not in one")
        pass


@bot.command(pass_context=True, aliases=['mw', 'mcw'])
@commands.cooldown(1, 2.5, commands.BucketType.guild)
async def microwave(ctx):
    await join(ctx)

    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice is None:
        return
    audio_file = next(cycled_audio)

    voice.play(discord.FFmpegPCMAudio(audio_file))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.4

    await asyncio.sleep(delay_duration[audio_file])

    await voice.disconnect()


if __name__ == "__main__":
    bot.run(TOKEN)
