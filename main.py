import discord
from discord.ext import commands
import os
import random
from keep_alive import keep_alive
keep_alive()
TOKEN = os.environ['key']

# configuração do bot
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='E!', intents=intents)

# eventos
@bot.event
async def on_ready():
  print('Elis online')

@bot.event
async def on_member_join(member: discord.Member):
  if member.bot:
    return
  else:
    try:
      channel = bot.get_channel(757649361248190546)
      rules_channel = bot.get_channel(817079518979293205)
      await channel.send(f'Olá {member.mention}! Leia as {rules_channel.mention} e seja bem viado!')
    except:
      pass

@bot.event
async def on_member_update(before: discord.Member, after: discord.Member):
  member = after
  if member.bot:
    return
  try:
    channel = bot.get_channel(757649361248190546)
    reactions = [
    'preferia seu perfil como era antes',
    'seu perfil ta bem mais bonitinho agora',
    'seu perfil sofreu um downgradekkkkkk',
    'achei seu perfil agora meio meh'
    ]
    r = random.randint(0, len(reactions))
    await channel.send(f'{member.mention} {reactions[r]}')
  except:
    pass

# comandos
@bot.command()
async def c_list(ctx: commands.Context):
  embed = discord.Embed(title='LISTA DE COMANDOS:',
  description=
'''E!say -> para fazer o bot digitar o que você digitar
E!avatar ->  para vizualizar a foto de perfil do amiguinho''',
  color=discord.Color.purple())
  await ctx.send(embed = embed)

@bot.command()
async def say(ctx: commands.Context, *, msg):
  await ctx.message.delete()
  await ctx.send(msg)

@bot.command()
async def avatar(ctx: commands.Context, member: discord.Member):
  avatar = member.avatar
  embed = discord.Embed(title=f'{member.display_name}', color=member.color)
  embed.set_image(url=avatar)
  await ctx.send(embed=embed)

# bot sendo executado
bot.run(TOKEN)
