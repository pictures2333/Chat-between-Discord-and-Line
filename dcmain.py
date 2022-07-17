import discord, json, requests
from discord.ext import commands, tasks
from discord import Webhook
import aiohttp, asyncio, os

with open('request.json', 'r', encoding = 'utf-8') as f:
    d1 = json.load(f)
d1['type'] = "Response"
d1['content'] = "Success"
d1['header'] = "None"
d1['url'] = "None"
d1['avatar'] = "None"
d1['sticker'] = [0, 0]
d1['event'] = "None"
dumpdata = json.dumps(d1, ensure_ascii = False)
with open(f'request.json', 'w', encoding = 'utf-8') as f:
    f.write(dumpdata)

with open('settings.json', 'r', encoding = 'utf-8') as f:
    d2 = json.load(f)

bot = commands.Bot(prefix = d2["DiscordBotPrefix"], intents = discord.Intents.all())

@bot.event
async def on_ready():
    print('Connecting...')
    await asyncio.sleep(1)
    if d2['DiscordWebhookUrl'] == "":
        print('Generating a webhook, please wait...')
        channel = bot.get_channel(d2["DiscordChannelID"])
        webhook = await channel.create_webhook(name = "Line to Discord")
        d2['DiscordWebhookUrl'] = webhook.url
        dumpdata = json.dumps(d2, ensure_ascii = False)
        with open(f'settings.json', 'w', encoding = 'utf-8') as f:
            f.write(dumpdata)
    print('Generated.')

@tasks.loop(seconds = 0.1)
async def myLoop():
    channel = bot.get_channel(d2["DiscordChannelID"])
    with open('request.json', 'r', encoding = 'utf-8') as f:
        d1 = json.load(f)
    #print(d1['event'])
    if d1['type'] == "LinePost":
        if d1['event'] == "textmsg":
            async with aiohttp.ClientSession() as session:  
                webhook = Webhook.from_url(d2['DiscordWebhookUrl'], session=session)
                await webhook.send(content=d1['content'], username=d1['header'], avatar_url=d1['avatar'])
            d1['type'] = "Response"
            d1['content'] = "Success"
            d1['header'] = "None"
            d1['url'] = "None"
            d1['avatar'] = "None"
            d1['sticker'] = [0, 0]
            d1['event'] = "None"
            dumpdata = json.dumps(d1, ensure_ascii = False)
            with open(f'request.json', 'w', encoding = 'utf-8') as f:
                f.write(dumpdata)
        elif d1['event'] == "sticker":
            async with aiohttp.ClientSession() as session:  
                webhook = Webhook.from_url(d2['DiscordWebhookUrl'], session=session)
                await webhook.send(content=f"<LINE STICKER PACKAGEID={d1['sticker'][0]} STICKERID={d1['sticker'][1]}>", username=d1['header'], avatar_url=d1['avatar'])
            d1['type'] = "Response"
            d1['content'] = "Success"
            d1['header'] = "None"
            d1['avatar'] = "None"
            d1['url'] = "None"
            d1['sticker'] = [0, 0]
            d1['event'] = "None"
            dumpdata = json.dumps(d1, ensure_ascii = False)
            with open(f'request.json', 'w', encoding = 'utf-8') as f:
                f.write(dumpdata)
        elif d1['event'] == "image":
            turl = d1['url']
            avatar = d1['avatar']
            header = d1['header']
            d1['type'] = "Response"
            d1['content'] = "Success"
            d1['header'] = "None"
            d1['avatar'] = "None"
            d1['url'] = "None"
            d1['sticker'] = [0, 0]
            d1['event'] = "None"
            dumpdata = json.dumps(d1, ensure_ascii = False)
            with open(f'request.json', 'w', encoding = 'utf-8') as f:
                f.write(dumpdata)
            async with aiohttp.ClientSession() as session:  
                webhook = Webhook.from_url(d2['DiscordWebhookUrl'], session=session)
                File = discord.File(turl)
                await webhook.send(file = File, username=header, avatar_url=avatar)
            #print(f"{d2['LineWebhookUrl']}/pimage/?msg={msg.attachments[0].url}")
            #requests.get(f"{d2['LineWebhookUrl']}/pimage/?msg={msg.attachments[0].url}")
            os.remove(turl)
        elif d1['event'] == "image":
            turl = d1['url']
            avatar = d1['avatar']
            header = d1['header']
            d1['type'] = "Response"
            d1['content'] = "Success"
            d1['header'] = "None"
            d1['avatar'] = "None"
            d1['url'] = "None"
            d1['sticker'] = [0, 0]
            d1['event'] = "None"
            dumpdata = json.dumps(d1, ensure_ascii = False)
            with open(f'request.json', 'w', encoding = 'utf-8') as f:
                f.write(dumpdata)
            async with aiohttp.ClientSession() as session:  
                webhook = Webhook.from_url(d2['DiscordWebhookUrl'], session=session)
                File = discord.File(turl)
                await webhook.send(file = File, username=header, avatar_url=avatar)
            #print(f"{d2['LineWebhookUrl']}/pimage/?msg={msg.attachments[0].url}")
            #requests.get(f"{d2['LineWebhookUrl']}/pimage/?msg={msg.attachments[0].url}")
            os.remove(turl)
        elif d1['event'] == "image":
            turl = d1['url']
            avatar = d1['avatar']
            header = d1['header']
            d1['type'] = "Response"
            d1['content'] = "Success"
            d1['header'] = "None"
            d1['avatar'] = "None"
            d1['url'] = "None"
            d1['sticker'] = [0, 0]
            d1['event'] = "None"
            dumpdata = json.dumps(d1, ensure_ascii = False)
            with open(f'request.json', 'w', encoding = 'utf-8') as f:
                f.write(dumpdata)
            async with aiohttp.ClientSession() as session:  
                webhook = Webhook.from_url(d2['DiscordWebhookUrl'], session=session)
                File = discord.File(turl)
                await webhook.send(file = File, username=header, avatar_url=avatar)
            #print(f"{d2['LineWebhookUrl']}/pimage/?msg={msg.attachments[0].url}")
            #requests.get(f"{d2['LineWebhookUrl']}/pimage/?msg={msg.attachments[0].url}")
            os.remove(turl)
        elif d1['event'] == "image":
            turl = d1['url']
            avatar = d1['avatar']
            header = d1['header']
            d1['type'] = "Response"
            d1['content'] = "Success"
            d1['header'] = "None"
            d1['avatar'] = "None"
            d1['url'] = "None"
            d1['sticker'] = [0, 0]
            d1['event'] = "None"
            dumpdata = json.dumps(d1, ensure_ascii = False)
            with open(f'request.json', 'w', encoding = 'utf-8') as f:
                f.write(dumpdata)
            async with aiohttp.ClientSession() as session:  
                webhook = Webhook.from_url(d2['DiscordWebhookUrl'], session=session)
                File = discord.File(turl)
                await webhook.send(file = File, username=header, avatar_url=avatar)
            #print(f"{d2['LineWebhookUrl']}/pimage/?msg={msg.attachments[0].url}")
            #requests.get(f"{d2['LineWebhookUrl']}/pimage/?msg={msg.attachments[0].url}")
            os.remove(turl)
        elif d1['event'] == "video":
            turl = d1['url']
            avatar = d1['avatar']
            header = d1['header']
            d1['type'] = "Response"
            d1['content'] = "Success"
            d1['header'] = "None"
            d1['avatar'] = "None"
            d1['url'] = "None"
            d1['sticker'] = [0, 0]
            d1['event'] = "None"
            dumpdata = json.dumps(d1, ensure_ascii = False)
            with open(f'request.json', 'w', encoding = 'utf-8') as f:
                f.write(dumpdata)
            async with aiohttp.ClientSession() as session:  
                webhook = Webhook.from_url(d2['DiscordWebhookUrl'], session=session)
                File = discord.File(turl)
                await webhook.send(file = File, username=header, avatar_url=avatar)
            #print(f"{d2['LineWebhookUrl']}/pimage/?msg={msg.attachments[0].url}")
            #requests.get(f"{d2['LineWebhookUrl']}/pimage/?msg={msg.attachments[0].url}")
            os.remove(turl)
        elif d1['event'] == "audio":
            turl = d1['url']
            avatar = d1['avatar']
            header = d1['header']
            d1['type'] = "Response"
            d1['content'] = "Success"
            d1['header'] = "None"
            d1['avatar'] = "None"
            d1['url'] = "None"
            d1['sticker'] = [0, 0]
            d1['event'] = "None"
            dumpdata = json.dumps(d1, ensure_ascii = False)
            with open(f'request.json', 'w', encoding = 'utf-8') as f:
                f.write(dumpdata)
            async with aiohttp.ClientSession() as session:  
                webhook = Webhook.from_url(d2['DiscordWebhookUrl'], session=session)
                File = discord.File(turl)
                await webhook.send(file = File, username=header, avatar_url=avatar)
            #print(f"{d2['LineWebhookUrl']}/pimage/?msg={msg.attachments[0].url}")
            #requests.get(f"{d2['LineWebhookUrl']}/pimage/?msg={msg.attachments[0].url}")
            os.remove(turl)
myLoop.start()

@bot.event
async def on_message(message):
    print(message.content)
    if not("[Line/" in message.author.name):
        attas = ""
        atts = []
        for at in message.attachments:
            atts.append(at.url)
        if len(atts) != 0:
            attas += "Attachments:\n"
            for attass in atts:
                attas += f"{attass}\n"
         
        msgem = ""
        embeds = []
        for em in message.embeds:
            embeds.append(em.url)
        if len(embeds) != 0:
            msgem += "Embeds:\n"
            for emm in embeds:
                msgem += f"{emm}\n"
        
        msgsti = ""
        stickers = []
        for sti in message.stickers:
            stickers.append(sti.url)
        if len(stickers) != 0:
            msgsti += "Stickers:\n"
            for emm in stickers:
                msgsti += f"{emm}\n"
        requests.get(f"{d2['LineWebhookUrl']}/push_function/?msg=[Discord:{message.guild.name}/{str(message.author.name)}]{str(message.content)}\n\n{attas}\n{msgem}\n{msgsti}")

bot.run(d2["DiscordBotToken"])