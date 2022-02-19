import discord, asyncio, datetime, pytz, random

client = discord.Client()

message_one = ['왜!','왜 불러!','왜 불렀엉!','뭐야!']
message_two = ['헿','흥!','난 이 서버에서 제일 귀여워!','와타시가 이치반 카와이!!']
message_three = ['미르가 제일제일 죠아요!','자는거 zzz','책 좋아아><','사이다!!','레몬...']
message_four = ['벌래...','다리 6개 달린거 ㅠㅠ','공부!','거미...','가지 우욱']
message_five = ['혹시 섹스 중독...?','섹스','야한거 안대...','떽뜨','그렇게 좋아..?','누구랑 그렇게 할거야?','나도 하고ㅅ..(퍽퍽)읍읍']

@client.event
async def on_ready(): # 봇이 실행시 한번 실행
    print("파이썬의 내장 함수를 출력하는 터미널에서 실행\n")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("무우봇아~"))

@client.event
async def on_message(message):
    if message.content == "무우야!":
        choiceList = random.choice(message_one)
        await message.channel.send (choiceList)
        print("{}이 '무우야!' 명령어 사용\n".format(message.author))

    elif message.content == "무우 바보!":
        await message.channel.send ("{}도 바보야!".format(message.author.mention))
        print("{}이 '무우 바보' 명령어 사용\n".format(message.author))


    elif message.content == "귀여운 무우!":
        choiceList = random.choice(message_two)
        await message.channel.send (choiceList)
        print("{}이 '귀여운 무우' 명령어 사용\n".format(message.author))

    elif message.content == "좋아하는거!":
        choiceList = random.choice(message_three)
        await message.channel.send (choiceList)
        print("{}이 '좋아하는거!' 명령어 사용\n".format(message.author))

    elif message.content == "싫어하는거!":
        choiceList = random.choice(message_four)
        await message.channel.send (choiceList)
        print("{}이 '싫어하는거!' 명령어 사용\n".format(message.author))  
        
    elif message.content == "섹스":
        choiceList = random.choice(message_five)
        await message.channel.send (choiceList)
        print("{}이 '섹스!' 명령어 사용\n".format(message.author))      
    

    elif message.content == "헤으응":
        await message.channel.send ("(경멸)")
        print("{}이 '헤으응' 명령어 사용\n".format(message.author))

    elif message.content == "띵킹" or message.content == "thinking":
        await message.channel.send ("띵킹하지 말라고 히잉...")
        print("{}이 '띵킹' 명령어 사용\n".format(message.author))

    elif message.content == "무우봇아~":
        await message.channel.send ("{} | {}, DM을 확인 해주세요!".format(message.author, message.author.mention))
        await message.author.send ("{} | {}, [무우봇 사용 설명서] 봇 사용방에서 무우봇아! 를 쳐보세요".format(message.author, message.author.mention))
        print("{}이 '무우봇아~' 명령어 사용\n".format(message.author))

    elif message.content == "ㅅㅂ":
        await message.channel.send ("바르고 고운말 써야징!")
        print("{}이 'ㅅㅂ' 명령어 사용\n".format(message.author))
    
    elif message.content == "애미":
        await message.channel.purge(limit=1)
        print("{}이 '애미' 명령어 사용\n".format(message.author))

    elif message.content == "ㅎㅇ":
        await message.channel.send ("{}도 안뇽".format(message.author.mention))
        print("{}이 'ㅎㅇ' 명령어 사용\n".format(message.author))
        
    elif message.content == "ㅁㄴㅇㄹ":
        await message.channel.send ("그만써...")
        print("{}이 'ㅁㄴㅇㄹ' 명령어 사용\n".format(message.author))
        
    elif message.content == "미르!":
        await message.channel.send ("무우꺼래요 건들면 무우가 물어요")
        print("{}이 '미르!' 명령어 사용\n".format(message.author))  

    elif message.content == "키리!":
        await message.channel.send ("헤으응")
        print("{}이 '키리!' 명령어 사용\n".format(message.author))    

    elif message.content == "엘풍!":
        await message.channel.send ("성남사는 칭구..?")
        print("{}이 '엘풍!' 명령어 사용\n".format(message.author))      

    elif message.content == "네코!":
        await message.channel.send ("2D랑 야스하는 미친넘")
        print("{}이 '네코!' 명령어 사용\n".format(message.author))

    elif message.content == "도핑!":
        await message.channel.send ("플심하는 중학생")
        print("{}이 '도핑!' 명령어 사용\n".format(message.author))

    elif message.content == "테귤희!":
        await message.channel.send ("귤희야 복숭아 줄게 귤줘")
        print("{}이 '테귤희!' 명령어 사용\n".format(message.author))      

    elif message.content == "아이스!":
        await message.channel.send ("대장대장 근데 왜 대장인지는 몰?루")
        print("{}이 '아이스!' 명령어 사용\n".format(message.author))  

    elif message.content == "마코!":
        await message.channel.send ("땅꼬마,꼬맹이,꼬꼬마")
        print("{}이 '마코!' 명령어 사용\n".format(message.author))        

    elif message.content == "릴리프!":
        await message.channel.send ("형아다형아다형아다!")
        print("{}이 '릴리프!' 명령어 사용\n".format(message.author))

    elif message.content == "네모!":
        await message.channel.send ("존경하는 인생선배(?), 부자형아, 멋진 어른")
        print("{}이 '네모!' 명령어 사용\n".format(message.author)) 
        
    elif message.content == "수빈!":
        await message.channel.send ("법을 사랑하는듯 하다.. 처음왔을때보다 잘 놀아서 뿌듯")
        print("{}이 '수빈!' 명령어 사용\n".format(message.author)) 

    elif message.content == "기신!":
        await message.channel.send ("귀신이 아니구 기신!!")
        print("{}이 '기신!' 명령어 사용\n".format(message.author))     
    
    elif message.content == "천령!":
        await message.channel.send ("천령천령??")
        print("{}이 '천령!' 명령어 사용\n".format(message.author))      

    elif message.content == "프라소!":
        await message.channel.send ("똑똑한 문과형아")
        print("{}이 '프라소!' 명령어 사용\n".format(message.author)) 
     
    elif message.content == "버그!":
        await message.channel.send ("진짜 버그는 싫지만 얘는 괜찮아")
        print("{}이 '버그!' 명령어 사용\n".format(message.author))
    
    elif message.content == "알럽파!":
        await message.channel.send ("얘 분신이 자꾸 나한테 막말했엉 히잉...")
        print("{}이 '알럽파!' 명령어 사용\n".format(message.author))
    
    elif message.content == "솜뭉치!":
        await message.channel.send ("그저 귀여운 솜뭉탱이")
        print("{}이 '솜뭉치!' 명령어 사용\n".format(message.author))
    
    elif message.content == "샤르!":
        await message.channel.send ("귀여운 고양이인가요??")
        print("{}이 '샤르!' 명령어 사용\n".format(message.author)) 
    
    elif message.content == "벤블!":
        await message.channel.send ("신경쓰이는 착한 애")
        print("{}이 '벤블!' 명령어 사용\n".format(message.author))
    
    elif message.content == "민!":
        await message.channel.send ("무서운 형아 스스로 군대를 가려하다 하다니...")
        print("{}이 '민!' 명령어 사용\n".format(message.author))
    
    elif message.content == "닉추!":
        await message.channel.send ("그림그리는 17쨜 여고생 하와와")
        print("{}이 '민!' 명령어 사용\n".format(message.author))
        
   
    
    
    
    elif message.content == "?":
        await message.channel.send ("어쩌라고")
        print("{}이 '?' 명령어 사용\n".format(message.author))
    elif message.content == "ㅋ":
        await message.channel.send ("웃어?")
        print("{}이 'ㅋ' 명령어 사용\n".format(message.author))
    elif message.content == "ㅎ":
        await message.channel.send ("뭐가 그렇게 웃긴데")
        print("{}이 'ㅎ' 명령어 사용\n".format(message.author))
    elif message.content == "너 밴":
        await message.channel.send ("내 본체가 섭장인데..?")
        print("{}이 '너 밴' 명령어 사용\n".format(message.author))
    elif message.content == "바본듯":
        await message.channel.send ("너 이를거야... ")
        print("{}이 '바본듯' 명령어 사용\n".format(message.author))
    elif message.content == "ㅗㅗ":
        await message.channel.send ("와 인성봐")
        print("{}이 'ㅗㅗ' 명령어 사용\n".format(message.author))
    elif message.content == "바보":
        await message.channel.send ("뭐래")
        print("{}이 '바보' 명령어 사용\n".format(message.author))
    elif message.content == "인성":
        await message.channel.send ("아 너인성이 더럽다고?")
        print("{}이 '인성' 명령어 사용\n".format(message.author))
    elif message.content == "아 너인성이 더럽다고?":
        await message.channel.send ("잘 알겠어")
        print("{}이 '아 너인성이 더럽다고?' 명령어 사용\n".format(message.author))
    elif message.content == "ㅈㄹ":
        await message.channel.send ("ㅈ까 시발")
        print("{}이 'ㅈㄹ' 명령어 사용\n".format(message.author))
    elif message.content == "수듄":
        await message.channel.send ("지는...")
        print("{}이 '수듄' 명령어 사용\n".format(message.author))
    elif message.content == "이잉":
        await message.channel.send ("아 꼴도보기 싫은 이잉")
        print("{}이 '이잉' 명령어 사용\n".format(message.author))
    elif message.content == "※전원이 켜졌습니다.":
        await message.channel.send ("안녕")
        print("{}이 '※전원이 켜졌습니다.' 명령어 사용\n".format(message.author))
    elif message.content == "컴퓨터의 힘":
        await message.channel.send ("그래봤자 코드덩어리")
        print("{}이 '컴퓨터의 힘' 명령어 사용\n".format(message.author))
    elif message.content == "왜 저럴까?":
        await message.channel.send ("너때문에")
        print("{}이 '왜 저럴까?' 명령어 사용\n".format(message.author))
    elif message.content == "특.이.점.이.도.래.했.노.":
        await message.channel.send ("너 일베 논란생길듯..?")
        print("{}이 '특.이.점.이.도.래.했.노.' 명령어 사용\n".format(message.author))
    elif message.content == "ㅖㅖ 잘 알겠습니다":
        await message.channel.send ("아 은근 기분 더럽네")
        print("{}이 'ㅖㅖ 잘 알겠습니다' 명령어 사용\n".format(message.author))
    elif message.content == "뭐해?":
        await message.channel.send ("너 생각")
        print("{}이 '뭐해?' 명령어 사용\n".format(message.author))
    elif message.content == "역시 주방세제는 만능이야!":
        await message.channel.send ("주방세제는 역시 퐁퐁!")
        print("{}이 '역시 주방세제는 만능이야' 명령어 사용\n".format(message.author))


    elif message.content == "무우봇아!": 
        embed = discord.Embed(title="무우봇", description="대표 명령어",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)

        embed.add_field(name="무우봇아~", value="무우봇에게서 DM이 옵니다", inline=False)
        embed.add_field(name="무우야!", value="답장 해줄거에요", inline=False)

        embed.add_field(name="좋아하는거!", value="무우가 좋아하는걸 알려드려요", inline=False)
        embed.add_field(name="싫어하는거!", value="무우가 싫어하는걸 알려드려요", inline=False)

        embed.add_field(name="귀여운 무우!", value="무우가 좋아하는 말이에요", inline=False)
        embed.add_field(name="무우 바보!", value="흥!", inline=False)

        embed.set_footer(text="Bot Made by. 장무우", icon_url="https://media.discordapp.net/attachments/859831545220562956/866345191212580874/1-001.png?width=613&height=613")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/859831545220562956/866344959485280266/KakaoTalk_20210717_124146667.jpg")
        await message.channel.send (embed=embed)
        print("{}이 '무우봇아!' 명령어 사용\n".format(message.author))

    if message.content.startswith ("청소!"):
        m = (message.author.guild_permissions.administrator)

        if m is True:
            amount = message.content[4:]
            await message.channel.purge(limit=1)
            await message.channel.purge(limit=int(amount))

            embed = discord.Embed(title="메시지 삭제 확인", description="채팅 {}개가\n관리자 {}님께서 보기 싫으시데요!".format(amount, message.author), color=0x000000)
            embed.set_footer(text="Bot Made by. 무우", icon_url="https://media.discordapp.net/attachments/859831545220562956/866345191212580874/1-001.png?width=613&height=613")
            await message.channel.send(embed=embed)
        
        elif m is False:
            await message.channel.purge(limit=1)
            await message.channel.send("{}넌 이거 못쓰지롱".format(message.author.mention))


client.run('OTAyMTk3OTA4OTA3MTA2MzY0.YXa7Rw.4x1LZa-jTQqJmfdZhXEXH-kwZss')  
