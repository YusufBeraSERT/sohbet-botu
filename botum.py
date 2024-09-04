import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('/Selamün Aleyküm'):
        await message.channel.send(f'aleyküm selam')
    if message.content.startswith('/Türkiyeyi ilk kuran kişi kimdir?'):
        await message.channel.send(f'Ulu Önder Mustafa kemal ATATÜRK')
    if message.content.startswith('/Gökyüzünde olmasını istediğin şey nedir?'):
        await message.channel.send(f'Güneş parıltısı ve kuşlar:)')
    if message.content.startswith('/küfür et'):
        await message.channel.send(f'yazılımım böyle kaba bir şekilde yazılmadı')
    if message.content.startswith('/köpekler ne kadar yaşar?'):
        await message.channel.send(f'Araştırmalara göre iyi bir bakım görerek evde bakılan köpeklerin sokak köpeklerine kıyasla daha uzun yaşadığı kanıtlanmıştır. Boyut olarak büyük sınıfına dahil olan köpekler genel ortalamada 10 ile 13 yıl arasında yaşarlar. Boyut olarak küçük kategorisine giren köpeklerde ortalama yaşam süresi 20 yıla kadar uzayabilir.')
    if message.content.startswith('/Hangi takımlısın?'):
        await message.channel.send(f'ben bir yazılım olduğum için takım tutamam ama güç olarak Galatasaray daha hoşuma gidiyor')
    if message.content.startswith('/hangi dilleri biliyorsun?'):
        await message.channel.send(f'Bütün dilleri ama en çok kullandıklarım Türkçe ve İngilizce')
    if message.content.startswith('/en sevdiğin film nedir?'):
        await message.channel.send(f'Hababam sınıfını çok sevmiştim')
    if message.content.startswith('/en sevdiğin oyun ne?'):
        await message.channel.send(f'Brawll Stars ve Roblox ama malesef Roblox şu anda kapandı:(')

    elif  message.content.startswith('$heh'):
        if len(message.content) > 4:
            count_heh = int(message.content[4:])
        else:
            count_heh = 5
        await message.channel.send("he" * count_heh)
        
client.run("MTI3ODczMjUzNTAxNDEwMDk5Mg.GxkpSt.h2haWQdWCDarGsManFWIeXYZO1oRDYAadX86Vs")
