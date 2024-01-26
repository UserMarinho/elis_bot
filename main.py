import discord
from discord.ext import commands
from keys import token_bot
from generate_response import generate_response
from generate_image import generate_image
from keep_alive import keep_alive
keep_alive()
TOKEN = token_bot['TOKEN']

# configuração do bot
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='E!', intents=intents)

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

# comandos
@bot.command()
async def c_list(ctx: commands.Context):
  embed = discord.Embed(title='LISTA DE COMANDOS:',
  description=
'''E!say -> para fazer o bot digitar o que você digitar
E!avatar ->  para vizualizar a foto de perfil do amiguinho
E!ask -> para fazer uma pergunta para mim''',
  color=discord.Color.purple())
  await ctx.send(embed = embed)

@bot.command()
async def say(ctx: commands.Context, *, msg):
  try:
    await ctx.message.delete()
    await ctx.send(msg)
  except:
    pass

@bot.command()
async def avatar(ctx: commands.Context, member: discord.Member):
  try:
    avatar = member.avatar
    embed = discord.Embed(title=f'{member.display_name}', color=member.color)
    embed.set_image(url=avatar)
    await ctx.message.reply(embed=embed)
  except:
    pass

@bot.command()
async def ask(ctx: commands.Context, *, msg: str):
  try:
    channel = bot.get_channel(1198089267897978910)
    if ctx.message.channel != channel:
      await ctx.message.reply(f'Para fazer perguntas, vá ao canal {channel.mention}.')
      return
    response = generate_response(msg)
    await ctx.message.reply(response)
  except:
    pass

@bot.command()
async def crt_image(ctx: commands.Context, *, msg: str):
  try:
    image_url = generate_image(msg)
    embed = discord.Embed(title=f'Imagem solicitada:\n', color=discord.Color.blue())
    embed.set_image(url=image_url)
    await ctx.message.reply(embed=embed)
  except:
    await ctx.message.reply('Não foi possível gerar a imagem.')

# bot sendo executado
bot.run(TOKEN)
