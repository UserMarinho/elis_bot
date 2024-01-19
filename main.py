import discord
from discord.ext import commands
import os
import random
import openai
from keep_alive import keep_alive
keep_alive()
TOKEN = os.environ['key']
openai.api_key = os.environ['openai_key']

# configuração do bot
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='E!', intents=intents)

# integração com o OpenAi
def generate_response(message):
  msg = [{'role': 'user', 'content': message}]
  response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=msg,
    max_tokens=1024,
    temperature=1
  )
  response_return = response.choices[0].message.content
  return response_return

# eventos
@bot.event
async def on_ready():
  print('Elis online')

@bot.event
async def on_member_join(member: discord.Member):
  try:
    channel = bot.get_channel(817084528719036466)
    rules_channel = bot.get_channel(817079518979293205)
    embed = discord.Embed(title=f'Olá {member.mention}!', description=f'Leia as {rules_channel.mention} e seja bem viado!', color=discord.Color.green())
    embed.set_thumbnail(url=member.avatar)
    embed.set_image(url='https://media1.tenor.com/m/-lFV17DHQEsAAAAC/qxwaii-rem.gif')
    await channel.send(embed=embed)
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

@bot.command()
async def ask(ctx: commands.Context, *, msg: str):
  response = generate_response(msg)
  await ctx.send(response)

# bot sendo executado
bot.run(TOKEN)
