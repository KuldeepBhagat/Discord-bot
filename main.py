import discord
from discord.ext import commands
from download import download_image
import asyncio
from newsapi import NewsApiClient
from googleapiclient.discovery import build
import torrent

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(commands.when_mentioned_or('!'), intents=intents)

class Myhelp(commands.MinimalHelpCommand):
    async def send_page(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            emby = discord.Embed(description=page)
            await destination.send(embed=emby)

bot.help_command = Myhelp()

#--------------------------------------------------Default Errors------------------------------------------#
async def member_not_found(ctx):
    emby = discord.Embed(title="Input Error", description="Please specify a username or id", color=0x00ff00)
    await ctx.send(embed=emby)
async def missing_perms(ctx):
    emby = discord.Embed(title="Permission Error", description="You don't have permission to use this command.", color=0x00ff00)
    await ctx.send(embed=emby)
async def wrong_user(ctx,arg):
    emby = discord.Embed(title="User Error", description=f"I don't have powers to {arg} this user.", color=0x00ff00)
    await ctx.send(embed=emby)


#--------------------------------------------------Fun Commands----------------------------------------------#
@bot.command(name = 'rimage', aliases=['ri']) # Image Downloading feature
async def rimage(ctx, number=1):
    url = download_image(number)
    for link in url:
        await ctx.send(link)

news_api = "32a810dc939a46b0aa36a50062567064"
youtube_api = "AIzaSyCzcPI8M4G9C47yV8CVtfQyVL9iLgABkyA"

@bot.command(name='newsh', aliases=['nh'])
async def newsh(ctx, country='in', category=None, page_size=5):
    News = NewsApiClient(api_key=news_api)
    headlines = News.get_top_headlines(country=country, category=category, page_size=page_size)
    for article in headlines['articles']:
        emby = discord.Embed(title=article['title'], url=article['url'],
                             description=f"Author: {article['author']}\nDate: {article['publishedAt']}", color=0x0000FF)
        await ctx.send(embed=emby)
@bot.command(name='newse', aliases=['ne'])
async def newse(ctx, *, query=None, language='en'):
    News = NewsApiClient(api_key=news_api)
    Everything = News.get_everything(q=query, page_size=10, language=language)
    for article in Everything['articles']:
        emby = discord.Embed(title=article['title'], url=article['url'],
                             description=article['description'])
        emby.set_author(name=article['author'])
        emby.set_image(url=article['urlToImage'])
        emby.set_footer(text=f"{article['source']} Date: {article["publishedAt"]}")
        emby.add_field(name="Content", value=article['content'], inline=False)
        await ctx.send(embed=emby)

@bot.command(name='youtube', aliases=['yt'])
async def youtube(ctx, *, query=None):
    youtubeClient = build("youtube", "v3", developerKey=youtube_api)
    request = youtubeClient.search().list(part='snippet', q=query, maxResults=1)
    response = request.execute()

    video_id = response['items'][0]['id']['videoId']
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    await ctx.send(video_url)

@bot.command(name='pirate', aliases=['p'])
async def pirate(ctx, query, page=1):

    page1 = torrent.PirateBay(query)
    title1 = page1.extract_title()
    magnet1 = page1.extract_magnet()
    page_address1 = page1.extract_page()

    if page == 1:
        for i in range(10):
            seed, leech, no_files, size, type, date, user = page1.extract_info(page_address1[i])
            emby = discord.Embed(title=title1[i], url=page_address1[i], description=f"{magnet1[i]}", color=0x0000FF)
            emby.add_field(name="Number of Files: ", value=no_files)
            emby.add_field(name="Type: ", value=type)
            emby.add_field(name="Size: ", value=size)
            emby.add_field(name="Added by: ", value=user)
            emby.set_footer(text=f"Seed and Leech: [{seed},{leech}] {date}")
            await ctx.send(embed=emby)
        return

    elif page == 2:
        for i in range(10, 20):
            seed, leech, no_files, size, type, date, user = page1.extract_info(page_address1[i])
            emby = discord.Embed(title=title1[i], url=page_address1[i], description=f"{magnet1[i]}", color=0x0000FF)
            emby.add_field(name="Number of Files: ", value=no_files)
            emby.add_field(name="Type: ", value=type)
            emby.add_field(name="Size: ", value=size)
            emby.add_field(name="Added by: ", value=user)
            emby.set_footer(text=f"Seed and Leech: [{seed},{leech}] {date}")
            await ctx.send(embed=emby)
        return
        
    elif page == 3:
        for i in range(20, 30):
            seed, leech, no_files, size, type, date, user = page1.extract_info(page_address1[i])
            emby = discord.Embed(title=title1[i], url=page_address1[i], description=f"{magnet1[i]}", color=0x0000FF)
            emby.add_field(name="Number of Files: ", value=no_files)
            emby.add_field(name="Type: ", value=type)
            emby.add_field(name="Size: ", value=size)
            emby.add_field(name="Added by: ", value=user)
            emby.set_footer(text=f"Seed and Leech: [{seed},{leech}] {date}")
            await ctx.send(embed=emby)
        return
    
    elif page == 4:
        for i in range(30, 40):
            seed, leech, no_files, size, type, date, user = page1.extract_info(page_address1[i])
            emby = discord.Embed(title=title1[i], url=page_address1[i], description=f"{magnet1[i]}", color=0x0000FF)
            emby.add_field(name="Number of Files: ", value=no_files)
            emby.add_field(name="Type: ", value=type)
            emby.add_field(name="Size: ", value=size)
            emby.add_field(name="Added by: ", value=user)
            emby.set_footer(text=f"Seed and Leech: [{seed},{leech}] {date}")
            await ctx.send(embed=emby)
        return
    
    elif page == 5:
        for i in range(40, 50):
            seed, leech, no_files, size, type, date, user = page1.extract_info(page_address1[i])
            emby = discord.Embed(title=title1[i], url=page_address1[i], description=f"{magnet1[i]}", color=0x0000FF)
            emby.add_field(name="Number of Files: ", value=no_files)
            emby.add_field(name="Type: ", value=type)
            emby.add_field(name="Size: ", value=size)
            emby.add_field(name="Added by: ", value=user)
            emby.set_footer(text=f"Seed and Leech: [{seed},{leech}] {date}")
            await ctx.send(embed=emby)
        return
    

    page2 = torrent.PirateBay(query, page_number=2)
    title2 = page2.extract_title()
    magnet2 = page2.extract_magnet()
    page_address2 = page2.extract_page()
    if page == 6:
        for i in range(10):
            seed, leech, no_files, size, type, date, user = page2.extract_info(page_address2[i])
            emby = discord.Embed(title=title2[i], url=page_address2[i], description=f"{magnet2[i]}", color=0x0000FF)
            emby.add_field(name="Number of Files: ", value=no_files)
            emby.add_field(name="Type: ", value=type)
            emby.add_field(name="Size: ", value=size)
            emby.add_field(name="Added by: ", value=user)
            emby.set_footer(text=f"Seed and Leech: [{seed},{leech}] {date}")
            await ctx.send(embed=emby)
        return
    
    if page == 7:
        for i in range(10, 20):
            seed, leech, no_files, size, type, date, user = page2.extract_info(page_address2[i])
            emby = discord.Embed(title=title2[i], url=page_address2[i], description=f"{magnet2[i]}", color=0x0000FF)
            emby.add_field(name="Number of Files: ", value=no_files)
            emby.add_field(name="Type: ", value=type)
            emby.add_field(name="Size: ", value=size)
            emby.add_field(name="Added by: ", value=user)
            emby.set_footer(text=f"Seed and Leech: [{seed},{leech}] {date}")
            await ctx.send(embed=emby)
        return
    
    if page == 8:
        for i in range(20, 30):
            seed, leech, no_files, size, type, date, user = page2.extract_info(page_address2[i])
            emby = discord.Embed(title=title2[i], url=page_address2[i], description=f"{magnet2[i]}", color=0x0000FF)
            emby.add_field(name="Number of Files: ", value=no_files)
            emby.add_field(name="Type: ", value=type)
            emby.add_field(name="Size: ", value=size)
            emby.add_field(name="Added by: ", value=user)
            emby.set_footer(text=f"Seed and Leech: [{seed},{leech}] {date}")
            await ctx.send(embed=emby)
        return
    
    if page == 9:
        for i in range(30, 40):
            seed, leech, no_files, size, type, date, user = page2.extract_info(page_address2[i])
            emby = discord.Embed(title=title2[i], url=page_address2[i], description=f"{magnet2[i]}", color=0x0000FF)
            emby.add_field(name="Number of Files: ", value=no_files)
            emby.add_field(name="Type: ", value=type)
            emby.add_field(name="Size: ", value=size)
            emby.add_field(name="Added by: ", value=user)
            emby.set_footer(text=f"Seed and Leech: [{seed},{leech}] {date}")
            await ctx.send(embed=emby)
        return
    
    if page == 10:
        for i in range(40, 50):
            seed, leech, no_files, size, type, date, user = page2.extract_info(page_address2[i])
            emby = discord.Embed(title=title2[i], url=page_address2[i], description=f"{magnet2[i]}", color=0x0000FF)
            emby.add_field(name="Number of Files: ", value=no_files)
            emby.add_field(name="Type: ", value=type)
            emby.add_field(name="Size: ", value=size)
            emby.add_field(name="Added by: ", value=user)
            emby.set_footer(text=f"Seed and Leech: [{seed},{leech}] {date}")
            await ctx.send(embed=emby)
        return
    
@bot.command(name='nyaa')
async def nyaa(ctx, query, page_no=1):
    page1 = torrent.nyaa(query, page_number=1)
    magnet1, torrent1 = page1.extract_mag_and_tor()
    title1, type1 = page1.extract_title_and_type()
    size1, date1, seed1, leech1, no_of_down1 = page1.extract_info()
    site1 = page1.extract_page()
    if page_no == 1:
        for i in range(15):
            emby = discord.Embed(title=title1[i], url=site1[i], description=magnet1[i], color=0x0000FF)
            emby.add_field(name='Torrent: ', value=torrent1[i])
            emby.add_field(name='Size: ', value=size1[i])
            emby.add_field(name='Type: ', value=type1[i])
            emby.add_field(name='Number of download: ', value=no_of_down1[i])
            emby.set_footer(text=f"Seed and Leech: [{seed1[i]},{leech1[i]}] date: {date1[i]}")
            await ctx.send(embed=emby)
        return
    
    if page_no == 2:
        for i in range(15, 30):
            emby = discord.Embed(title=title1[i], url=site1[i], description=magnet1[i], color=0x0000FF)
            emby.add_field(name='Torrent: ', value=torrent1[i])
            emby.add_field(name='Size: ', value=size1[i])
            emby.add_field(name='Type: ', value=type1[i])
            emby.add_field(name='Number of download: ', value=no_of_down1[i])
            emby.set_footer(text=f"Seed and Leech: [{seed1[i]},{leech1[i]}] date: {date1[i]}")
            await ctx.send(embed=emby)
        return
    
    if page_no == 3:
        for i in range(30, 45):
            emby = discord.Embed(title=title1[i], url=site1[i], description=magnet1[i], color=0x0000FF)
            emby.add_field(name='Torrent: ', value=torrent1[i])
            emby.add_field(name='Size: ', value=size1[i])
            emby.add_field(name='Type: ', value=type1[i])
            emby.add_field(name='Number of download: ', value=no_of_down1[i])
            emby.set_footer(text=f"Seed and Leech: [{seed1[i]},{leech1[i]}] date: {date1[i]}")
            await ctx.send(embed=emby)
        return
    
    if page_no == 4:
        for i in range(45, 60):
            emby = discord.Embed(title=title1[i], url=site1[i], description=magnet1[i], color=0x0000FF)
            emby.add_field(name='Torrent: ', value=torrent1[i])
            emby.add_field(name='Size: ', value=size1[i])
            emby.add_field(name='Type: ', value=type1[i])
            emby.add_field(name='Number of download: ', value=no_of_down1[i])
            emby.set_footer(text=f"Seed and Leech: [{seed1[i]},{leech1[i]}] date: {date1[i]}")
            await ctx.send(embed=emby)
        return
    
    if page_no == 5:
        for i in range(60, 75):
            emby = discord.Embed(title=title1[i], url=site1[i], description=magnet1[i], color=0x0000FF)
            emby.add_field(name='Torrent: ', value=torrent1[i])
            emby.add_field(name='Size: ', value=size1[i])
            emby.add_field(name='Type: ', value=type1[i])
            emby.add_field(name='Number of download: ', value=no_of_down1[i])
            emby.set_footer(text=f"Seed and Leech: [{seed1[i]},{leech1[i]}] date: {date1[i]}")
            await ctx.send(embed=emby)
        return
    
    page1 = torrent.nyaa(query, page_number=2)
    magnet1, torrent1 = page1.extract_mag_and_tor()
    title1, type1 = page1.extract_title_and_type()
    size1, date1, seed1, leech1, no_of_down1 = page1.extract_info()
    site1 = page1.extract_page()

    if page_no == 6:
        for i in range(15):
            emby = discord.Embed(title=title1[i], url=site1[i], description=magnet1[i], color=0x0000FF)
            emby.add_field(name='Torrent: ', value=torrent1[i])
            emby.add_field(name='Size: ', value=size1[i])
            emby.add_field(name='Type: ', value=type1[i])
            emby.add_field(name='Number of download: ', value=no_of_down1[i])
            emby.set_footer(text=f"Seed and Leech: [{seed1[i]},{leech1[i]}] date: {date1[i]}")
            await ctx.send(embed=emby)
        return
    
    if page_no == 7:
        for i in range(15, 30):
            emby = discord.Embed(title=title1[i], url=site1[i], description=magnet1[i], color=0x0000FF)
            emby.add_field(name='Torrent: ', value=torrent1[i])
            emby.add_field(name='Size: ', value=size1[i])
            emby.add_field(name='Type: ', value=type1[i])
            emby.add_field(name='Number of download: ', value=no_of_down1[i])
            emby.set_footer(text=f"Seed and Leech: [{seed1[i]},{leech1[i]}] date: {date1[i]}")
            await ctx.send(embed=emby)
        return
    
    if page_no == 8:
        for i in range(30, 45):
            emby = discord.Embed(title=title1[i], url=site1[i], description=magnet1[i], color=0x0000FF)
            emby.add_field(name='Torrent: ', value=torrent1[i])
            emby.add_field(name='Size: ', value=size1[i])
            emby.add_field(name='Type: ', value=type1[i])
            emby.add_field(name='Number of download: ', value=no_of_down1[i])
            emby.set_footer(text=f"Seed and Leech: [{seed1[i]},{leech1[i]}] date: {date1[i]}")
            await ctx.send(embed=emby)
        return
    
    if page_no == 9:
        for i in range(45, 60):
            emby = discord.Embed(title=title1[i], url=site1[i], description=magnet1[i], color=0x0000FF)
            emby.add_field(name='Torrent: ', value=torrent1[i])
            emby.add_field(name='Size: ', value=size1[i])
            emby.add_field(name='Type: ', value=type1[i])
            emby.add_field(name='Number of download: ', value=no_of_down1[i])
            emby.set_footer(text=f"Seed and Leech: [{seed1[i]},{leech1[i]}] date: {date1[i]}")
            await ctx.send(embed=emby)
        return
    
    if page_no == 10:
        for i in range(60, 75):
            emby = discord.Embed(title=title1[i], url=site1[i], description=magnet1[i], color=0x0000FF)
            emby.add_field(name='Torrent: ', value=torrent1[i])
            emby.add_field(name='Size: ', value=size1[i])
            emby.add_field(name='Type: ', value=type1[i])
            emby.add_field(name='Number of download: ', value=no_of_down1[i])
            emby.set_footer(text=f"Seed and Leech: [{seed1[i]},{leech1[i]}] date: {date1[i]}")
            await ctx.send(embed=emby)
        return

#--------------------------------------------------Moderation Commands----------------------------------------#


@bot.command() 
@commands.has_guild_permissions(ban_members=True)
async def ban(ctx, member: discord.Member=None, reason=None):
    if member.top_role > ctx.me.top_role:
        await wrong_user(ctx, 'ban')
        return
    await member.ban(reason=reason)
    emby = discord.Embed(title="Bot Action",description=f"{member} has been banned. \nReason: {reason}" ,color=0xff0000)
    await ctx.send(embed=emby)
@ban.error
async def ban_error(ctx, error):                                      # ban
    if isinstance(error, commands.errors.MemberNotFound):
        await member_not_found(ctx)
    if isinstance(error, commands.errors.MissingPermissions):
        await missing_perms(ctx)

@bot.command()
@commands.has_guild_permissions(kick_members=True)
async def kick(ctx, member: discord.Member=None, reason=None):        # Kick
    if member.top_role > ctx.me.top_role:
        await wrong_user(ctx, 'kick')
        return
    await member.kick(reason=reason)
    emby = discord.Embed(title="Bot Action",description=f"{member} has been kicked. \nReason: {reason}" ,color=0xff0000)
    await ctx.send(embed=emby)
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.errors.MemberNotFound):
        await member_not_found(ctx)
    if isinstance(error, commands.errors.MissingPermissions):
        await missing_perms(ctx)

@bot.command()
@commands.has_guild_permissions(manage_roles=True)
async def mute(ctx, member: discord.Member=None,time: int = 0, unit: str="s", reason=None):     # Mute
    if member.top_role > ctx.me.top_role:
        await wrong_user(ctx, 'mute')
        return
    mute_role = discord.utils.get(ctx.guild.roles, name = 'muted')
    if mute_role in member.roles:
        emby = discord.Embed(title="Error", description="User is already muted", color=0x00ff00)
        await ctx.send(embed=emby)
        return
    units = {"s": 1, "m": 60, "h": 3600, "d": 86400}
    mute_time = time*units[unit]
    if time == 0:
        await member.add_roles(mute_role, reason=reason)
        emby = discord.Embed(title="Muted", description=f"{member} is muted", color=0xff0000)
        await ctx.send(embed=emby)
    else:
        await member.add_roles(mute_role, reason=reason)
        emby = discord.Embed(title="Muted", description=f"{member} has been muted for {time}{unit}", color=0xff0000)
        await ctx.send(embed=emby)
        await asyncio.sleep(mute_time)
        await member.remove_roles(mute_role, reason="Mute Expired")
@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.errors.MemberNotFound):
        await member_not_found(ctx)
    if isinstance(error, commands.errors.MissingPermissions):
        await missing_perms(ctx)
@bot.command()
@commands.has_guild_permissions(manage_roles=True)                                     # Un_mute
async def unmute(ctx, member: discord.Member):
    mute_role = discord.utils.get(ctx.guild.roles, name= "muted")
    await member.remove_roles(mute_role)
    emby = discord.Embed(title="UnMuted", description=f"{member} has been unmuted", color=0xff0000)
    await ctx.send(embed=emby)
@unmute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.errors.MemberNotFound):
        await member_not_found(ctx)
    if isinstance(error, commands.errors.MissingPermissions):
        await missing_perms(ctx)

@bot.command()
@commands.has_guild_permissions(manage_channels=True)
async def clear(ctx, number=1):                                                          # Clear
    msg = []
    async for message in ctx.message.channel.history(limit=number):
        msg.append(message)
    await ctx.message.channel.delete_messages(msg)
async def c_error(ctx, error):
    if isinstance(error, commands.errors.MissingPermissions):
        await missing_perms(ctx)

bot.run('bot token')
