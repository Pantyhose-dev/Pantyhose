Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import scapy.all as scapy
... import discord
... from discord.ext import commands
... 
... # Replace with your Discord bot token
... BOT_TOKEN = 'your_discord_bot_token'
... 
... # Replace with your Discord channel ID
... CHANNEL_ID = 1206140464906895360
... 
... intents = discord.Intents.default()
... intents.messages = True
... intents.guilds = True
... 
... bot = commands.Bot(command_prefix='!', intents=intents)
... 
... @bot.event
... async def on_ready():
...     print(f'Logged in as {bot.user}')
... 
... async def send_packet_info(channel, packet):
...     packet_info = f"Captured Packet:\n{packet.summary()}"
...     await channel.send(packet_info)
... 
... def packet_callback(packet):
...     if packet.haslayer(scapy.IP):
...         asyncio.run_coroutine_threadsafe(send_packet_info(bot.get_channel(CHANNEL_ID), packet), bot.loop)
... 
... def start_sniffer():
...     scapy.sniff(prn=packet_callback, store=0)
... 
... @bot.command()
... async def start(ctx):
...     await ctx.send("Starting packet sniffer...")
...     start_sniffer()
... 
... @bot.command()
... async def stop(ctx):
...     await ctx.send("Stopping packet sniffer...")
...     scapy.sniff(prn=packet_callback, store=0, stop_filter=lambda x: False)
... 
