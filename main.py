import os
import discord
from discord.ext import commands
import asyncio 
import logging
import random 
from colorama import init
from colorama import Fore, Style
import requests
import json
import datetime
import random
import threading
import random
import time
import threading

init()
os.system("cls" or "clear")

token = input('{}\n[>] {} ТОКЕН ВАШЕ АККАУНТА DISCORD: {}'.format(Fore.RESET, Fore.LIGHTYELLOW_EX, Fore.RESET))
prefix = input('{}\n[>] {} ПРЕФИКС: {}'.format(Fore.RESET, Fore.LIGHTYELLOW_EX, Fore.RESET))
client = commands.Bot(command_prefix=prefix, case_insensitive=True,
                      self_bot=True)

client.remove_command('help')
header = {"Authorization": f'Bot {token}'}
os.system('cls' if os.name == 'nt' else 'clear')
os.system('cls' if os.name == 'nt' else 'clear')

intents = discord.Intents.all()
intents.members = True

@client.event
async def on_ready():
    print('------')
    print('{}\n[>] {} Запуск программы копирования... {}'.format(Fore.RESET, Fore.LIGHTYELLOW_EX, Fore.RESET))
    print('{}\n[>] {} Запуск произошёл успешно! {}'.format(Fore.RESET, Fore.LIGHTYELLOW_EX, Fore.RESET))
    print('{}\n[>] {} Команда копирования:{} {}copyserver\n'.format(Fore.RESET, Fore.LIGHTYELLOW_EX, Fore.RESET, prefix))
    print('     - Ваш ник: ' + client.user.name)
    print('     - Ваш ID: ' + str(client.user.id))
    print('{}\n[>] {} Создатель: GamerPTS {}'.format(Fore.RESET, Fore.LIGHTYELLOW_EX, Fore.RESET))
    print('\n------\n')


@client.command()
async def copyserver(ctx): 
    await ctx.message.delete()
    wow = await client.create_guild(f'backup-{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in client.guilds:
        if f'backup-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
            print(ctx.guild.roles)
    for role in ctx.guild.roles[::-1]:
        if role.name != "@everyone":
            try:
                await wow.create_role(name=role.name, color=role.color, permissions=role.permissions, hoist=role.hoist, mentionable=role.mentionable)
                print(f"Created new role : {role.name}")
            except:
                break

client.run(token, bot=False)
