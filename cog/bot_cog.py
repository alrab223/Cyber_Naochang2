import asyncio
import json
import os
import random
import re
import datetime
import subprocess
import shutil
import glob
import sqlite3
from contextlib import closing

import discord
import MeCab
import requests
from dotenv import load_dotenv
from discord.ext import commands  # Bot Commands Frameworkのインポート
from googletrans import Translator
from pykakasi import kakasi
from src import colla,wiki_search
from src import picture_download as pd
load_dotenv()
# コグとして用いるクラスを定義。
class Main(commands.Cog):


   def __init__(self, bot):
      self.bot = bot
      self.tweet_wait = False
      with open("json/picture.json", "r") as f:
         self.colla_num=json.load(f) 
      

   @commands.command("goodbye")
   async def disconnect(self, ctx):
      """botを切ります"""
      await ctx.send("また会いましょう")
      await self.bot.logout()

   @commands.command()
   async def birthday(self, ctx, idol: str):
      """アイドル名を入れると誕生日を出力します"""
      with open("text/birthday.txt","r")as f:
           target=f.readline()
           while target:
               if idol in target:
                   answer=target.split(" - ")
                   break
               else:
                   target=f.readline()
           await ctx.send(answer[0])
  
   @commands.command("ナオビーム")
   async def logs(self, ctx,num:int):
      logs=[]
      if ctx.author.id!=425142865073799180:
           await ctx.send("あなたにこのコマンドは使えません")
           return
      async for log in ctx.channel.history(limit=num):
         logs.append(log)
      await ctx.channel.delete_messages(logs)
   
   @commands.command("リネーム")
   async def rename(self, ctx, name: str):
      guild=self.bot.get_guild(566227588054253569)
      for member in guild.members:
         if member.id==660877225863938079:
            await member.edit(nick=name)
            break
   
   @commands.command("参加日取得")
   async def member_join(self, ctx):
      guild=self.bot.get_guild(566227588054253569)
      members = guild.members
      with (sqlite3.connect("db/bot_data.db")) as conn:
         c = conn.cursor()
         for member in members:
            times = member.joined_at + datetime.timedelta(hours=9)
            data=[member.id,times.year,times.month,times.day]
            c.execute(f'insert into user_join (id,year,month,day) values (?,?,?,?)',data)
         conn.commit()
   
   
   @commands.command("教えて奈緒")
   async def wiki(self, ctx, word: str):
       """wikipediaを調べます。引数(単語)"""
       await ctx.send(wiki_search.wikipediaSearch(word))

   @commands.command()
   async def gold(self, ctx):
      """所持まゆげを調べます"""
      with (sqlite3.connect("db/bot_data.db")) as conn:
         c = conn.cursor()
      c.execute(f'select gold from userdata where id={ctx.author.id}')
      gold = c.fetchall()[0][0]
      await ctx.send(f"{gold}まゆげ")
   
   @commands.command("データ登録n")
   async def regist(self, ctx):
      with open("db/bot_id.json", "r") as f:
         dic = json.load(f)

      with (sqlite3.connect("db/bot_data.db")) as conn:
         c = conn.cursor()
         for i in dic:
            coin=dic[str(i)]["24_hours"]
            c.execute(f'update userdata set mayuge_coin={coin} where id={i}')
         conn.commit()
 
   
   @commands.command("vc通知")
   @commands.dm_only()
   async def vc_news(self, ctx,num:str):
      with (sqlite3.connect("db/bot_data.db")) as conn:
         c = conn.cursor()
         if num == "オフ":
            c.execute(f'update userdata set vc_notification=0 where id={ctx.author.id}')
            await ctx.send(ctx.author.mention+"通知を解除しました")
         else:
            c.execute(f'update vc_notification_setting set members={num},vc_notification=1 where id={ctx.author.id}')
            await ctx.send(f"参加人数{num}以上で通知します")
         conn.commit()
      
      
          
   @commands.command()
   async def rainbow(self, ctx):
       await ctx.message.delete()
       ch_webhooks = await ctx.channel.webhooks()
       webhook = discord.utils.get(ch_webhooks, name="naochang")
       await webhook.send(content=":heart: :orange_heart: :yellow_heart: :green_heart: :blue_heart: :purple_heart:",
               username=ctx.author.display_name,
               avatar_url=ctx.author.avatar_url_as(format="png"))
   
   @commands.command()
   async def rainbow2(self, ctx):
       emoji=""
       await ctx.message.delete()
       ch_webhooks = await ctx.channel.webhooks()
       webhook = discord.utils.get(ch_webhooks, name="naochang")
       with open("json/emoji.json", "r")as f:
           dic=json.load(f)
       for i in dic["rainbow_art"]:
          emoji += str(self.bot.get_emoji(int(i)))
       await webhook.send(content=emoji,
               username=ctx.author.display_name,
               avatar_url=ctx.author.avatar_url_as(format="png"))
   
   @commands.command()
   async def rainbow3(self, ctx):
      emoji=""
      await ctx.message.delete()
      ch_webhooks = await ctx.channel.webhooks()
      webhook = discord.utils.get(ch_webhooks, name="naochang")
      with open("json/emoji.json", "r")as f:
          dic = json.load(f)
      text=dic["rainbow_art"]
      for i in range(7):
          for i in text:
              emoji += str(self.bot.get_emoji(int(i)))
          emoji += "\n"
          pop = text.pop(0)
          text.append(pop)
          
      
      await webhook.send(content=emoji,
              username=ctx.author.display_name,
              avatar_url=ctx.author.avatar_url_as(format="png"))
   
            
   @commands.command("送金")
   async def send_money(self, ctx, user_id: int, money: int):
      """まゆげを誰かに送金できます.引数(ユーザーid,金額)"""
      with (sqlite3.connect("db/bot_data.db")) as conn:
         c = conn.cursor()
         sql = c.execute(f'select gold from userdata where id={ctx.author.id} or id={user_id}')
         gold=[]
         for row in sql:
            gold.append(row[0])
         if gold[0]<money:
            await ctx.send("まゆげが足りません")
            return
         else:
            gold[0]-=money
            gold[1] += money
            conn.commit()
      me=self.bot.get_user(user_id)
      await ctx.send(me.mention+f"に{money}まゆげ送金しました")

   @commands.Cog.listener()
   async def on_member_join(self,member):
      dm_channel = await member.create_dm()
      with open("text/introduce.txt","r")as f:
          text = f.read()
      await dm_channel.send(member.mention)
      await dm_channel.send(text)
      with (sqlite3.connect("db/bot_data.db")) as conn:
         c = conn.cursor()
         data=[member.id,10000,None,0,0,10]
         c.execute(f'insert into userdata (id, gold, birthday,naosuki,vc_notification,mayuge_coin) values (?,?,?,?,?,?)',data)
         conn.commit()
   @commands.command()#メンバー登録
   async def member(self, ctx):
      with (sqlite3.connect("db/bot_data.db")) as conn:
         c = conn.cursor()
         
         guild=self.bot.get_guild(658856326541213708)
         for member in guild.members:
            if member.bot or c.execute(f"select* from userdata where id={member.id}")!=None:
               pass
            else:
               data=[member.id,10000,None,0,0,10]
               c.execute(f'insert into userdata (id, gold, birthday,naosuki,vc_notification,mayuge_coin) values (?,?,?,?,?,?)',data)
               conn.commit()
   
   @commands.command()#メンバー登録
   async def check(self, ctx):
       emoji = await ctx.guild.fetch_emojis()
       for i in emoji:
           print(i)

   @commands.Cog.listener()
   async def on_reaction_add(self, reaction, user):
      print(reaction.emoji)
      if reaction.count==1:
         if reaction.emoji =="🇺🇸":
              translator = Translator()
              trans_en = translator.translate(reaction.message.content, src='ja', dest='en')
              await reaction.message.channel.send(trans_en.text)
         elif reaction.emoji =="🇯🇵":
             translator = Translator()
             lang=translator.detect(reaction.message.content)
             trans_en = translator.translate(reaction.message.content, src=lang.lang, dest='ja')
             await reaction.message.channel.send(trans_en.text)
         elif reaction.emoji =="🇮🇹":
             translator = Translator()
             trans_en = translator.translate(reaction.message.content, src='ja', dest='it')
             await reaction.message.channel.send(trans_en.text)
              
   @commands.Cog.listener()
   async def on_message(self, message):
      if message.author.bot:
         return
      pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
      text: list = re.findall(pattern, message.content)
      ch_list: list = ["kami_ch", "ya_ch", "na_ch", "o_ch"]
      channels: list = []
      for i in ch_list:
         channels.append(self.bot.get_channel(int(os.environ.get(i))))
      if message.channel.id==channels[0].id or message.channel.id==channels[1].id or message.channel.id==channels[2].id or message.channel.id==channels[3].id:
         for channel in channels:
            async for log in channel.history(limit=40):    
               url_list:list = re.findall(pattern,log.content)
               if set(text) & set(url_list) and message.id!=log.id:
                  msg=await message.channel.send(f"{message.author.mention}{channel.name}に同じURLがもう貼られてるよ！")
                  await asyncio.sleep(10)
                  await msg.delete()
                  return
                  
      if message.attachments:
         if message.content in self.colla_num:
            pd.download_img(message.attachments[0].url, "picture/colla/image.png")
            colla.colla_maker(self.colla_num[message.content])
            await message.delete()
            await message.channel.send(file=discord.File("picture/colla/new.png"))

         elif message.content=="切り抜き":
            #if ctx.author.id!=425142865073799180:
            pd.download_img(message.attachments[0].url, "picture/colla/image.png")
            response = requests.post(
              'https://api.remove.bg/v1.0/removebg',
              files={'image_file': open('picture/colla/image.png', 'rb')},
              data={'size': 'auto'},
              headers={'X-Api-Key':os.environ.get("removebg_api")},
            )
            if response.status_code == requests.codes.ok:
               with open('picture/colla/no-bg.png', 'wb') as out:
                  out.write(response.content)
            else:
               print("Error:", response.status_code, response.text)
            await message.delete()
            await message.channel.send(file=discord.File("picture/colla/no-bg.png"))         
      
      if "!random" in message.content:
          text=message.content.split("!random")
          num=random.randint(0,100)
          await message.channel.send(text[0] + str(num) + text[1])
      if message.content.startswith("https://discordapp.com/channels/566227588054253569"):
         text=message.content.split("566227588054253569/")[1]
         text=text.split("/")
         channel = self.bot.get_channel(int(text[0]))
         messages=await channel.fetch_message(int(text[1]))
         
         if messages.attachments:
               embed = discord.Embed(title="引用元",description=messages.content)
               embed.set_image(url=messages.attachments[0].url)
               
               embed.set_author(name=messages.author.display_name,icon_url=messages.author.avatar_url)
         else:
               embed = discord.Embed(title="引用元",description=messages.content)
               
               embed.set_author(name=messages.author.display_name,icon_url=messages.author.avatar_url)
         await message.channel.send(embed=embed)

      if "なおはじ" in message.content:
         emoji = ["<:na:681866058055024801>","<:o_:681866075935211555>","<:ha:681866087402700829>","<:ji:681866097858969677>"]
         for i in emoji:
            await message.add_reaction(i)
      if "ｶﾐﾔﾅｵ" in message.content:
         emoji = ["<a:kamiya:714088347924168714>","<a:unnamed:714091501646381058>",\
         "<a:Nao_Loading_5:714091475444432917>","<a:nao:714091488899891200>",\
         "<a:1478254807_tHGkQDRV:714091363360047205>","<a:1478254807_4CbzcReG:714091384411389952>",]
         for i in emoji:
            await message.add_reaction(i)
      if "なおすき" in message.content:
          with open("json/naosuki_count.json","r") as f:
              dic = json.load(f)
          dic["count"] += 1
          with open("json/naosuki_count.json", "w") as f:
             json.dump(dic,f,indent=3)
            



def setup(bot):
    bot.add_cog(Main(bot)) # TestCogにBotを渡してインスタンス化し、Botにコグとして登録する。