import asyncio
import discord
import re
import os
import requests
import bs4
from bs4 import BeautifulSoup
from discord.ext import commands
from urllib3 import request
from urllib.request import Request
from urllib.request import urlopen
import urllib.request
import random
import pymysql

random.seed(a=None)

client = discord.Client()

token = "NjEyNTgyMTg1MTY5MzIxOTg3.XVmyiQ.JMk8TBwU7ly3DbHAqgwM5Zmofg0"

'''
def is_me(m):
    return m.author == client.user
@bot.command(pass_context = True)
async def c(ctx):
    if commands.content.startswith('$c'):
        await ctx.client.purge_from(ctx.message.channel, check=is_me)
'''

@client.event
async def on_ready():
    print("다음으로 로그인합니다.")
    print(client.user.name)
    print(client.user.id)
    print("=============")
    game = discord.Game(name="행복아 도와줘")
    await client.change_presence(status = discord.Status.idle, activity=game)

@client.event
async def on_message(message):

    if message.author.bot:
        return None

    channel = message.channel
    id = message.author.id

    if message.content =='행복아 도와줘':
        embed = discord.Embed(title="명령어 목록입니다.", description="행복아 도와줘 = 도움말 \n행복아 부탁해 @닉네임 \nsushi(초밥)/chicken(치킨)/fky(fuckyou)/tle(틀니)/blt(블러드트레일)/zuzac(주작)\n\n행복아 실검\n\n-틀- / 사랑해 @태그/ 슬개 / 수고 / 나만운없어 / 고마워 @태그 / 축하해 @태그\n\n틀니지수 @닉네임 /국밥지수 @닉네임 /탈모지수 @닉네임 \n\n롤전적 롤닉네임 \n\n포츈쿠키 @닉네임\n\n마법의 행복이님 \n\n$추가 명령어 추가하고싶은 채팅 = 명령어를 치면 추가하고 싶은 채팅을 출력합니다!\n\n삭제 명령어 = 추가된 명령어가 삭제됩니다.\n\n", color =0x00ff00)
        embed.set_footer(text = "명령어는 지속적으로 추가될 예정입니다.")
        await channel.send(embed=embed)
    
    if message.content.startswith('롤전적 '):
        Name = message.content[3:len(message.content)]
        req = requests.get("https://www.op.gg/summoner/userName="+Name)
        html = req.text
        opgg = BeautifulSoup(html,"html.parser")

        Rank1 = str(opgg.find_all('div',{'class':'TierRank'}))
        Rank2 = str(Rank1)[23:-7]
   

        lp1 = str(opgg.find_all('span',{'class':'LeaguePoints'}))

        lp2 = str(lp1)[28:-8]
        lp3 = lp2.strip()

        lol = '티어 : ' + Rank2+ '\n점수 : '+ lp3
        embed = discord.Embed(title = Name + "님의 전적입니다.",description = lol, color=0x00ff00)
        await channel.send(embed = embed)

    
    if message.content.startswith('행복아 부탁해 '):            
        userid = re.findall(r'\d+',message.content)
        userid = userid[0]
        userid = str(userid)
        if message.content[8:].startswith('<@'):
            #await channel.send('<@'+userid+">:sushi:")
    
            if message.content[-6:].startswith(" sushi"):
                await channel.send('<@'+userid+"> :sushi:")
            elif message.content[-6:].startswith(" pizza"):
                await channel.send('<@'+userid+"> :pizza:")
            elif message.content[-8:].startswith(" chicken"):
                await channel.send('<@'+userid+"> :poultry_leg: ")
            elif message.content[-4:].startswith(" fky"):
                await channel.send('<@'+userid+"> :middle_finger: ")
            elif message.content[-6:].startswith(" zuzac"):
                await channel.send('<@'+userid+"> <:zuzac:359257073055170561>")
            elif message.content[-4:].startswith(" tle"):
                await channel.send('<@'+userid+"> <:tle:396604664990269440>")
            elif message.content[-4:].startswith(" blt"):
                await channel.send('<@'+userid+"> <:bloodtrail:352805698498854913>")
    
    if message.content.startswith('축하해 '):
        randomemjic = random.randint(1,20)
        userid1 = re.findall(r'\d+',message.content)
        userid1 = userid1[0]
        userid1 = str(userid1)
        
        if message.content[4:].startswith('<@'):
            await channel.send('<@'+userid1+">"+randomemjic*':tada:')

        elif message.content.startswith(''):
            await channel.send(randomemjic*':tada:')

    if message.content.startswith('고마워 ') :
        randomemjit = random.randint(1,20)
        userid2 = re.findall(r'\d+', message.content)
        userid2 = userid2[0]
        userid2 = str(userid2)
        
        if message.content[4:].startswith('<@'):
            await channel.send('<@'+userid2+">"+randomemjit*':blush:')
        if message.content[3:].startswith('<@'):
            await channel.send('<@'+userid2+">"+randomemjit*':blush:')
    
    if message.content =='후' or message.content == '하':
        await channel.send("<:simuruk:488370573001621514> :dash:")

    if message.content.startswith('선넘네'):
        embed = discord.Embed()
        embed.set_image(url = 'https://cdn.discordapp.com/attachments/287230035155222540/620418841725370420/image0.jpg')
        await channel.send(embed = embed)
    


    if message.content.startswith('탈모지수 '):
        talid = message.content
        talid2 = talid.split(' ')
        
        del talid2[0]
        
        print(talid2)
        talidrange = len(talid2)
        
        
        
        for qwe in range(0,talidrange):
            randomemojitle = random.choice([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,20])
            useridtal = re.findall(r'\d+', talid2[qwe])
            print(useridtal)
            
            print(qwe)
            print(talidrange)
            useridtal = useridtal[0]
            
            useridtal = str(useridtal)
            print(useridtal)
            
            await channel.send('<@'+useridtal+">님의 탈모지수"+randomemojitle*"<:talmo:452778889668984842>"+"\n")

    if message.content.startswith('국밥지수 '):
        pigid = message.content
        pigid2 = pigid.split(' ')
        
        del pigid2[0]
        
        print(pigid2)
        pigidrange = len(pigid2)
        
        
        
        for qwe in range(0,pigidrange):
            randomemojitle = random.choice([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,20])
            useridpig = re.findall(r'\d+', pigid2[qwe])
            print(useridpig)
            
            print(qwe)
            print(pigidrange)
            useridpig = useridpig[0]
            
            useridpig = str(useridpig)
            print(useridpig)
            
            await channel.send('<@'+useridpig+"> 님은 "+randomemojitle*"<:gb:616571362533703690>"+"그릇"+"\n")

    if message.content.startswith('사랑해 ') :
        randomemjih = random.randint(1,20)
        userid3 = re.findall(r'\d+',message.content)
        userid3 = userid3[0]
        userid3 = str(userid3)
        
        if message.content[4:].startswith('<@'):
            await channel.send('<@'+userid3+">"+randomemjih*':heart:')
    
    if message.content.startswith('<:sad:355710026993893377>'):
        randomemji1s = random.randint(1,10)
        await channel.send(randomemji1s*'<:sad:355710026993893377>')
    
    if message.content.startswith('시바'):
        randomemji1d = random.randint(1,10)
        await channel.send(randomemji1d*'<:siba:449362867230081026>')

    if message.content.startswith('수고') or message.content.startswith('고생'):
        randomemji1bl = random.randint(1,10)
        await channel.send(randomemji1bl*':blush:')

    if message.content.startswith('나만운없어'):
        randomemji1z = random.randint(1,10)
        await channel.send(randomemji1z*"<:zuzac:359257073055170561>")
    
    if message.content.startswith('행복아 실검'):
        r = requests.get("https://www.naver.com")
        html2 = r.text
        naver = BeautifulSoup(html2,"html.parser")

        realtime_part2 = realtime_part1.find('ul',{'class':'ah_l'})
        realtime_part3 = realtime_part2.find_all('li')

        embed = discord.Embed(
            title='네이버 실시간 검색어',
            description='실시간 검색어',
            colour = discord.Colour.green()
        )
        for i in range(0,5):
            realtime_part4 = realtime_part3[i]
            realtime_part5 = str(realtime_part4.find('span',{'class':"ah_k"}))
            realtime_part6 = str(realtime_part5[18:-7])
            realtime_part6.replace(" ",'+')
            realtime_part = realtime_part6.replace(' ', '+')
            realurl = 'https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query='+realtime_part
            print(realtime_part)
            embed.add_field(name=str(i+1)+'위', value='\n'+'[%s](<%s>)'%(realtime_part, realurl), inline=False)
        await channel.send(embed=embed)


    if message.content.startswith('행복아 짖어'):
        await channel.send('냥')
    
    #소라고동
    if message.content.startswith('마법의 행복이님'):
        mabub = random.choice(["안돼", "하지마", "그래", "제발그러지마",])
        await channel.send(mabub)

    #포츈쿠키
    if message.content.startswith('포츈쿠키 '):
        useridlucky = re.findall(r'\d+', message.content)
        useridlucky = useridlucky[0]
        useridlucky = str(useridlucky)
        luckypc = str(random.randint(1,100))
        lucky = random.choice(["길가다 백원 주울 확률"+luckypc+"%증가!!", "우산 안들고 나왔는데 비 안올 확률 "+luckypc+"% 증가!!", "오늘 상사가 덜지랄할 확률 "+luckypc+"%증가!!", "핸드폰 떨어뜨려도 안깨질확률 "+luckypc+"%증가!!", "핸드폰 충전 안한줄 알았는데 되어있음!!", "자기가 원하던 스팀게임"+luckypc+"년 안에 세일!!", "길가다 아주 귀여운 고양이를 만날 확률"+luckypc+"% 증가!!", "요번달 은행 저축이자 "+luckypc+"원 더 들어옴!!", "천천히 걸어 나갔는데 버스가 딱 맞춰서 올 확률"+luckypc+"% 증가!!", "버스 탔는데 좋은 자리가 날 확률 "+luckypc+"% 증가!!","편의점에서 사려던것 2+1 할 확률"+luckypc+"% 증가!!"],)
        if message.content[5:].startswith('<@'):

            await channel.send('<@'+useridlucky+'>님의 포츈쿠키!\n'+lucky)

    if message.content.startswith('$추가'):
        conn = pymysql.connect(host='', user='TT', password='',db='Happy',charset = 'utf8mb4')
        cmdmessage = message.content
        cmdmsgsp = cmdmessage.split()
        del cmdmsgsp[0]
        #cmdmsgsp[1] = str(cmdmsgsp[1])
        curs = conn.cursor()
        sql = "INSERT INTO test1(cmd,emoji) value (%s, %s)"
        print(sql)
        curs.execute(sql, (cmdmsgsp[0],cmdmsgsp[1]))
        conn.commit()
        conn.close()
        await channel.send("추가되었습니다!")
    b = message.content
    qasw = 0

    qwer = pymysql.connect(host='', user='TT', password='',db='Happy',charset = 'utf8mb4')
    try:
        cursor = qwer.cursor()
        sql1 = "select *from test1"
        cursor.execute(sql1)
        result = str(cursor.fetchall())
    finally:

        qwer.close()

    a = result.replace("(","")
    a = a.replace("'","")
    a = str(a.replace(")",""))
    a = str(a.replace(" ",""))
    a = a.split(',')
    if b in a: #이모지에 있는거 입력하면 다음 cmd 거가 나옴 고쳐야함
        print('포함')
        while(1): # 난리나는 이유 : 멀 쳐넣든 0부터 시작하는데 게다가 맞는다? 바로 출력해버림 / 해결
            
            if b == a[qasw]:
                v = a[qasw+1]
                print(v)
                if 'https' in v:
                    embed = discord.Embed()
                    embed.set_image(url = v)
                    
                    await channel.send(embed=embed)
                    break
                await channel.send(v)
                break
            qasw = qasw+1
    qasw = 0        
    
    if message.content.startswith('삭제'):
        conn = pymysql.connect(host='', user='TT', password='',db='Happy',charset = 'utf8mb4')
        cmdmessage = message.content
        cmdmsgsp = cmdmessage.split()
        del cmdmsgsp[0]
        curs = conn.cursor()
        sql = "delete from test1 where cmd = '"+cmdmsgsp[0]+"'"
        curs.execute(sql)
        conn.commit()
        conn.close()
        await channel.send("삭제되었습니다!")

    '''
    if message.content=="명령어 확인":
        qwer = pymysql.connect(host='localhost', user='TT', password='QLXK-clzls!2',db='Happy',charset = 'utf8mb4')
        try:
            cursor = qwer.cursor()
            sql1 = "select *from test1"
            cursor.execute(sql1)
            result = str(cursor.fetchall())
        finally:

            qwer.close()
        for i in result:
            await channel.send(result)
    '''   


    '''
    
    if message.content.startswith('$이미지'):
        Text = ""
        learn = message.content.split(" ")
        vrsize = len(learn)
        vrsize = int(vrsize)
        for vv in(range(1, vrsize)):
            Text = Text + " " + learn[vv]
        print(Text.strip())

        randonNum = random.randrange(0,40)

        location = Text
        enc_location = urllib.parse.quote(location)
        hdr = {'User-Agent' : 'Mozilla/5.0','referer':'https://www.google.co.kr'}
        url = 'https://www.google.co.kr/search?hl=ko&tbm=isch&source=hp&biw=1460&bih=659&ei=rK1cXdewKqu4mAXMvKjYDA&q=' + enc_location
        req = Request(url, headers=hdr)
        html4 = urllib.request.urlopen(req)
        im = bs4.BeautifulSoup(html4, "html.parser")
        print(im)

        imgfind1 =im.find('div',attrs={'class':'rg_bx rg_di rg_ed'}) 
                                          
        imgfind2 = imgfind1.find('a',attrs={'class':'rg_1'})

        embed = discord.Embed(
            colour=discord.Colur.Yellow()
            )
        embed.set_image(url=imgfind2)
        await channel.send(embed = embed)
        



    if message.content.startswith('$clear'):
        await client.delete_message(message)   

'''
'''
    if message.content.startswith("행복아 음악"):
            mumsg = message.content.split(" ")
            try:
                muurl = mumsg[1]
                muurl2 = re.match('(https?://)?(www.\)?((youtube\.(com))/watch\?v=([-\w]+)|youtube\.be/([-w]+))',mumsg)
                if muurl1 == None:
                    await channel.send('url을 제대로 입력해 주세요')
                    return
            except IndentationError:
                await channel.send('url을 제대로 입력해 주세요')
                return
            
            muchannel = message.author.voice.voice_channel
            musever = message.server
            void_client = client.voice_client_in(server)

            if 
'''

client.run(token)
