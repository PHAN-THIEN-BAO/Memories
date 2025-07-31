define a = ("???") 
define b = ("Stranger")
define c = ("Kid's voice")
define d = ("[name]")
define e = ("Little girl")
define f = ("Lin")
define g = ("A statue")
define h = ("Kale")
define i = ("Lina")
define k = ("God")
define l = ("Author")
define m = ("Mother")

label start:
    "{i}{b}Use headphones to have a good experiment.{/b}{/i}"
    "....."
    "...."
    "..."
    ".."
    "."
    a "..."
    a "?"
    a "???"
    a 'Where am I?'
    
    scene hospital 

    play music "audio/DIE_MUSIC.mp3"
    queue music "audio/DIE_MUSIC.mp3"
    "Open your eyes, you realize you are standing in the cold windy wasteland"
    "In front of your eyes is an old hospital"
    "It's dilapidated and scary like stepping out of a creepy myth."
    "Suddenly, a cold feeling runs down your spine."
    "Turning around, you see a person"
    "Due to the distance, the person looks blurry, almost invisible."

    scene outside

    menu Strangers_or_Hospital: 
        "What should I do now?"
        "Approach him":
            jump Approach

        "Ignore him":
            "I go to the hospital, like it draws me in."
            jump Go_To_Hospital

label Approach:

    scene outside

    "You make a gentle gesture like waving."
    "Come closer and clearly see his face"
    "He looks dull, tired, but it's familiar somehow"
    "His eyes look at you like you are his target"
    "... he holds a knife in right hand ... "
    
    show bodypng
    a "!?"
    a "..."
    hide bodypng

    menu Run_or_Courious:
    
        "..."
        "Continue to approach him":
    
            jump Die

        "RUN!!!":
            "My cognitive understand this case is unsafe." 
            "I immediately ran away." 
            "Somehow, I ran to the hospital."
            jump Go_To_Hospital

label Die:

    "You worry when suddenly appearing somewhere, you still approach strangers trying to ask for help."
    "When you are close, you are violently attacked by that stranger."
    show bodypng
    "His face looked like he was about to cry, it's like he's venting his anger to attack you."
    "He crying..."
    a "..."
    a "... pitiful ..."
    b "Goodbye,..."
    b "... Kale"
    b "..."
    "..."
    hide bodypng
    jump Game_Over

label Game_Over: 

    "..." 
    "Thanks for playing, love you O◡O!!!"
    return

label Go_To_Hospital:

    scene hospital

    "Stand in the hospital yard."
    "Your feelings are unclear."
    "You not afraid this old building."
    "Besides, you feel like you are home."

    menu Try_To_Enter_The_Building:
        "You try to find the way to enter the hospital."
        "Try to open the main gate.":
            jump Can_not_enter

        "Look around.":
            jump Go_Or_Back

label Go_Or_Back:

    scene hospital

    "Look to the right, you see a small subtle path."


    menu Path_Or_Stranger:

        "What should you do?"
        "Follow the path.":
            jump Window

        "Back to the stranger.":
            jump Tomb

label Can_not_enter:
        "You can not open the gate. Some things block inside."
        a "Hm... Should I look around?"
        jump Try_To_Enter_The_Building

label Tomb:

        scene 2nd

        "You back to the place where the stranger was stay."
        "It's cemetery area."
        "You note the footprin."
        "Front of it is a tomb with a teddybear."

        scene bear

        "Suddenly, you cry."
        a "Lina..."
        "You turnback the hospital."
        jump Go_Or_Back

label Window:
    "You decide to follow the path."
    "At the end of this small path."
    "You find the window that still open."

    scene cua_sau

    "You note the left window."

    scene cua_so_sau

    menu Inside_Or_Not:
        a "Should I go inside or not?"
        "Enter the hospital":
            jump Enter_Hospital
            
        "Go back.":
            jump Try_To_Enter_The_Building


label Enter_Hospital:
    scene room 1
    "You jumped inside, the surrounding atmosphere suddenly changed."
    "Hot and humid, the room was cluttered but had a once-tidy look."
    "I had to be tough on myself to continues."
    "A nonsense voice ran through my thoughts."

    play sound "audio/smile.mp3"

    "{b}“Ant, Auto, Absorb, Anomaly, Alternate, A…”{/b}"
    a "What?"
    a "A taboo?"
    "You thoughts."

label now_u_in_room:
    scene room 1

    menu Jumpout_Or_Continues:

        a "What should I do now?"
        "Try to open the room door.":
            jump Dark_Hallway

        "Look around.":
            jump Flashlight

        "Back to outside.":
            jump Inside_Or_Not

label Dark_Hallway:

    scene dark_lobby

    a "Maybe this is the hallway" 
    "You are iffy because it is too dark." 
    jump now_u_in_room

label Flashlight:
    scene pick_up_flash_light
    "You found the flashlight"
    jump Room_With_Light

label Room_With_Light:
    "You pick up the flashlight."
    a "What next?"
    scene room 1
    menu Now_You_Have_Light:
        "Try to open the room door.":
            jump Hallway
        "Back to outside.":
            jump Someone_Lock_The_Door

label Someone_Lock_The_Door:
    "The window locked."
    a "What the...?"
    jump Now_You_Have_Light

label Hallway:
    scene lobby
    "Now you at the hallway."
    "At the end of hallway is toilet and stair."

    menu Toilet_Or_Stair:
        a "Where should I go now?"
        "Toilet.":
            jump Toilet

        "Go up stair.":
            jump Stair

label Toilet:
    scene tolet
    "You walk slowly to ensure you don't come faced something unexpected."
    "Somehow, you believe that you would meet some things (someone?) scary."
    
    scene mirror_face
    "You see your self in the mirror."
    "A wretched face tired of life."
    "Look at yourself, you feel angry."

    menu Stupid_Or_Not:
        "..."
        "Hit the mirror.":
            
            jump Stupid 

        "Forget it.":
            jump Paper

label Stupid:
    
    play sound "audio/broken.mp3"

    "You decide to broke it."
    a "OUCH!!!"
    "The mirror doesn't broke."
    "You hurt yourself."
    "{s}Idiot •_•{/s}"
    jump Paper

label Paper:

    scene toilet paper

    "You found a paper."
    a "{b}Ball, Beauty, Bureaucracy,...{/b}"
    a "Hm...?"
    a "I know this paper!"
    a "I..."
    a "...can't remember anythings."
    "Suddenly you hear the sound flushing from the toilet behind."

    scene toilet

    menu Run_Or_Curious:

        "Someone hide there."
        
        "Look carefully":
            jump Die_By_PEBU

        "RUN!!!!!!!":
            jump Stair

label Die_By_PEBU:

    scene son

    play sound "audio/PeBU.mp3"
    "That creature jump to you."
    jump Game_Over

label Stair:

    scene stair

    "You go to the stair."
    "A piece of paper lying on the stairs."
    "{b}Cognitive, Complementary, Constraint, Concentration, Co...{/b}"
    scene black
    a "!"
    a "!!!"
    c "Brother... See you soon."

    play sound "audio/smile.mp3"
    
    a "AHH!!!"

    scene stair 

    a "Someone..."
    a "...waiting..."
    menu Up_Or_Not:
        "What should I..."
        "Continues.":
            jump Someone_Cry
        "Go back.":
            jump Spider 

label Spider:

    play sound "audio/spi.mp3"
    play sound "audio/spi.mp3"

    "A spider noise on your head."
    menu Look_Or_No:
        "!?"
        "Look up.":
            jump ChoLam
        "Ignore it.":
            jump Someone_Cry

label ChoLam:

    play sound "audio/spi.mp3"

    scene lam-senpai
    a "!?"
    scene lam
    play sound "audio/lamscream.mp3"   
    "AHHHHHHHHHHHHHHHHHH!!!"
    jump Game_Over

label Someone_Cry:

    scene lau_1

    play sound "audio/crying.mp3"

    "You hear a kid's voice."
    "That child is crying."
    "The voice come from no where and started suddenly."
    a "What wrong with this hospital?"
    c "Brother..."
    c "... where are you ..."
    c "...hic hic."
    a "I'm here Li..."
    a "!?"

    menu Scare_Or_Not:
        a "!?"
        "Run away.":
            jump You_Kill_Yourself
        "Run away.":
            jump You_Kill_Yourself
        "Run away.":
            jump You_Kill_Yourself
        "Run away.":
            jump You_Kill_Yourself
        "Run away.":
            jump You_Kill_Yourself
        "Find where the voice come from.":
            jump The_Room_Next_To_You

label You_Kill_Yourself:
    "You fell from the stairs."
    "You see someone..."
    b "..."
    jump Game_Over

label The_Room_Next_To_You:
    play sound "audio/crying.mp3"
    "You walk to the end of the corridor, turn right, enter the 4th room."
    "You have no idea why you know exactly where the voice comes from."
    a "..."
    "You found a girl who was crying."
    scene cry
    a "Hello?"
    "You try to pat her shoulder."
    "You can not touch her."
    scene sister_room
    show linsock
    e "!"
    a "!!!"
    e "Kale?"
    e "Kale, is that you?"
    hide linsock
    show linsad
    a "Kale? Who? I'm..."
 
    e "?"
    e "..."
    e "......."
    e "........."
    hide linsad
    show linnomal

    e "Sorry, I just misunderstanding."
    e "What can I call you?" 

    $ name = renpy.input("Type a name:")
    $ name = name.strip()
    if name == "":
        $ name = "Traveller"
    if name == "Kale":
        $ name = "####"

    d "... %(name)s"
    hide linnomal
    show linhappy
    f "%(name)s, I'm Lin, nice to meet you."
    hide linhappy 
    menu Talk1:
        "What should you do now?"
        "Talk.":
            jump Request1a
        "Leave she alone.":
            jump Request1b

label Request1a:
    d "By the way, just momment go, why did you cry?"
    show linsad
    f "..."
    f "I have a request, I need your help."
    d "?"
    hide linsad
    menu Accept_Or_Not:
        "What would you said?"
        "Accept.":
            jump Canteen
        "Refuse.":
            jump Canteen

label Request1b:
    d "Well, I have to go now."
    "You turn around."
    show linsock
    f "Wait!!! I have a little problem, I need your help. "
    hide linsad
    show linsad
    f "... please."
    hide linsad
    jump Canteen

label Canteen:
    d "..."
    "You decide to help her."
    d "(Well, I have no choice. I have many things to ask her.)"
    d "Pleasure to help."
    show linhappy
    f "Thanks K..."
    f "I mean thanks %(name)s."
    f "I lost a teddybear, the last time I hold it is in canteen."
    hide linhappy
    d "I unerstand."

label Talk_Or_Canteen:

        scene sister_room

        menu What:
            "..."
            "Talk.":
                jump About_Teddy
            "Leave the room.":
                jump Find_Canteen

label About_Teddy:
    show linhappy
    d "That teddy is your favourie one?"
    f "Yes, that is a only one I have."
    f "At my 7th birthday, ma and brother make it for me."
    hide linhappy
    f "(Handmade?)"

    jump No_More_Asking

label No_More_Asking:

    menu CanteenNow:

        "Leave the room.":
            jump Find_Canteen

label Find_Canteen:
    scene lau_1
    menu Look_Around_Or_GO_Down:
        f "Where should I go now?"
        "Back to Lin's room.":
            jump Talk_Or_Canteen
        "Go around.":
            jump Nothing_Around
        "Down to ground floor.":
            jump Ground_Flood

label Nothing_Around:
    "You go around"
    "An invisible wall blocks the way, you cannot enter anyroom else."
    jump Look_Around_Or_GO_Down

label Ground_Flood:

    scene lobby

    menu Find_Teddy_Bear:
        d "Where is the canteen?"
        "Toilet.":
            jump Die_By_Twin
        "Turn left.":
            jump Library_Room1
        "Turn right.":
            jump Canteen_Room1

label Die_By_Twin:

    play sound "audio/toan_scare.mp3"

    scene toan

    d "AHHHH!!!!"

    jump Game_Over

label Library_Room1:
    "It's library."
    "The door is looked."
    jump Find_Teddy_Bear

label Canteen_Room1:

    scene lobby

    "You look around."
    "The hallway is dirty because of moss on the wall."
    d "(Hm? It was tidy since I entered this place, doesn't it?)"
    "You entered the canteen."

    scene canteen

    "A messy room with tables and chairs."
    "You found a paper."

    menu Find_Teddy_Or_Puzzle:
        " "
        "Find teddy bear.":
            jump Ted 
        "Find something else.":
            jump Text_Math

label Ted:
    "You found a box."

    scene safe

    menu Un_Or_No:
        d "A chest?"
        "Try to unlock it":
            jump No_Open
        "Not now.":
            jump No_Open

label No_Open:
    "You need a password."
    jump Text_Math

label Text_Math:
    scene canteen
    "You found a text"
    menu Ques1:
        "7x^2-14x+7=0"
        "x = 1":
            jump Ques2
        "x = 2":
            jump Ques1
        "x = 3":
            jump Ques1

label Ques2:
    menu Ques_2:
        "cos x = sin 35. x = ?"
        "x = 45":
            jump Ques2
        "x = 55":
            jump Ques3
        "x = 65":
            jump Ques2

label Ques3:

    menu Ques_3:

        "The sun's rays make an angle of 40 with the ground and the tower's shadow on the ground is 20 m long. Calculate the height of the tower."
        "x = 24":
            jump Ques3
        "x = 13":
            jump Ques3
        "x = 17":
            jump Finish

label Finish:

    d "1, 55 ,17"
    
    menu Finish_Math_Exam:

        d "What should I do now?"

        "Find teddy bear.":
            jump Pass1
        "Go out.":
            jump Die_By_PEBU

label Pass1:

    "You found a chest."

    menu ENNNNN:

        "What is the password?"
        "17155":
            jump Pass1
        "55171":
            jump Pass1
        "15517":
            jump GOTIT
        "17551":
            jump Pass1
        "11755":
            jump Pass1

label GOTIT:

    "You successful unlock the box."
    show teddies
    "You got a Teddy Bear."

    menu Give_It_Back:
        "What do you want to do next?"
        "Back to Lin.":
            jump Lin_Teddy
        "Rest.":
            jump Die_By_Spi

label Die_By_Spi:

    play sound "audio/spi.mp3"

    "Something on your head."
    "You look up"

    scene lam-senpai

    play sound "audio/lamscream.mp3"

    d "{b}{i}AHHHHHHHHHHHHHH!!!{/i}{/b}"

    scene lam

    jump Game_Over

label Lin_Teddy:

    scene sister_room

    "You back to Lin's room."
    d "I found your Teddy, Lin!"
    show linhappy
    f "You're back."
    f "Thanks %(name)s!"
    hide linhappy
    show linsad
    f "..."
    f "My family is not a well-being or rich."
    f "I have a brother older than me by 4 years."
    f "We grew up together, he loves me very much, and so do I."
    f "People always say that poverty always goes with bad luck."
    f "When I was 7, I found out that I had leukemia."
    f "Ma was already struggling to raise two children, now it's even harder."
    f "I can't go to school because of a serious illness."
    f "The only thing that makes me happy is that my brother visits me every day."
    f "On my 7th birthday, ma and brother made this one for me."
    "You feel like your heart missed a beat."
    d "..."
    f "..."
    d "Why you tell me this?"
    f "..."
    d "Um... Never mind..."
    d "Your story... just..."
    d "(...to familiar)"
    d "...too sad."
    f "Kal..."
    f "%(name)s, can I ask for one more favor?"
    d "?"
    d "..."
    d "Sure."
    hide linsad
    show linhappy
    f "Really?"
    "You give her a gentle smile."
    d "Um!"
    f "There are one fairy tale book at the library, the one with a big flower on the cover is mine."
    d "Hm?"
    d "The library was locked, wasn't it?"
    hide linhappy
    show linnomal
    f "Locked?"
    f "No, the library is always open to make sure that our patients always have something to read."
    hide linnomal
    d "?"
    d "Understood."
    d "I go for now."
    "You turn back."
    show linhappy
    f "Thanks, brother..."
    hide linhappy
    d "Hm???"
    "You look at Lin, she smile."
    d "(Maybe it's just my imagination)."

    jump Go_Lib

label Go_Lib:

    scene lobby

    menu Hum:
        d "Where is library?"
        "Turn left.":
            jump Library_Room2
        "Turn right.":
            jump Canteen_Room2

label Canteen_Room2:
    "It's canteen."
    "The door locked."
    d "Hm?"
    "You turn back."
    jump Go_Lib

label Library_Room2:
    "You come library."

    scene library_view

    d "Countless spider web..."
    "You note the book with a flower on the cover"
    d "Is that Lin's book?"
    "You found the book easily."
    d "It's time to give it back to Lin."

    scene library_out1

    "A creepy statue blocking the door."
    g "What comes after yesterday but prior to tomorrow?"
    d "!?"
    "Your cannot feel your legs."
    play sound "audio/ToanMD.mp3"
    "You can't utterance any word."
    g "What comes after yesterday but prior to tomorrow?"
    d "!?"

    play sound "audio/ToanMD.mp3"

    menu Answer_My_Questions:
        
        "You calm yourself so you can make a sound."
        "Morning?":
            jump Pye
        "Prior to today?":
            jump Que2
        "Future?":
            jump Pye
        "I don't know!":
            jump Pye

label Que2:
    play sound "audio/ToanMD.mp3"
    menu num2:
        "In what ways can effective leadership facilitate team collaboration and productivity?"
        "Goal clarity?":
            jump Que3
        "Shirk responsibility?":
            jump Pye
        "On time?":
            jump Pye
        "Patience?":
            jump Pye

label Pye:

    scene toan 

    jump Die_By_Twin

label Que3:
    menu hy:
        "A group of events that happen in a particular order, one following the other, and are often repeated?"
        "Cycle?":
            jump Gone
        "Excess?":
            jump Pye
        "Potency?":
            jump Pye
        "Adherent?":
            jump Pye

label Gone:
    d "..."
    d "What is that thing...?"
    "You back to Lin's room."

    scene sister_room

    "You found that Lin hold a paper with some random words."
    show linhappy
    f "You get my book back!"
    "Lin take a book and let the paper flew."
    "You pick up the paper."
    "Distinction, Dedicated, Decay,... Die."
    "You ask Lin"

    menu Ask_Sth:
        "You decide to ask Lin"
        "About the monster.":
            jump Lin_ans1
        "About the paper.":
            jump Lin_ans2

label Lin_ans1:
    hide linhappy
    d "There a weird statue with 2 heads at the library."
    d "What is that things?"
    d "Why you don't mention about that creature?"
    show linmad
    f "Statue? 2 heads? Creature? What are you talking about?"
    f "There are no anything like you say in this hospital!"
    d "!?"
    hide linmad
    show linsad
    "Lin got scared, she about to cry."
    hide linsad
    d "..."
    jump Q2a

label Lin_ans2:
    d "You are the one who wrote these papers?"
    "Lin was startled"
    f "No, my brother wrote it."
    f "I was say before."
    f "I can not go to school because my illness."
    f "My brother who very smart, write and teach vocabulary for me."
    d "Your brother? Die? He teached this word for you?"
    f "..."
    hide linhappy
    show linsad
    f "No, I wrote that one."
    f "One day, my brother had to move to city for university."
    f "Ma more focus on working."
    f "I realize one thing."
    f "I'm a burden."
    f "I thought ma and brother will happy."
    f "Few day later..."
    f "I died..."
    hide linsad
    d "HM!?"

    jump Q2b

label Q2a:
    menu nest:
        "What's next?"
        "About the paper.":
            jump last1
        "No more.":
            jump Lin_End

label last1:
    d "You are the one who wrote these papers?"
    "Lin was startled"
    f "No, my brother wrote it."
    f "I was say before."
    f "I can not go to school because my illness."
    f "My brother who very smart, write and teach vocabulary for me."
    d "Your brother? Die? He teached this word for you?"
    f "..."
    hide linhappy
    show linsad
    f "No, I wrote that one."
    f "One day, my brother had to move to city for university."
    f "Ma more focus on working."
    f "I realize one thing."
    f "I'm a burden."
    f "I thought ma and brother will happy."
    f "Few day later..."
    f "I died..."
    hide linsad
    d "HM!?"
    jump Lin_End

label Q2b:
    menu mext:
        "What's next?"
        "About the monster.":
            jump last2
        "No more.":
            jump Lin_End        

label last2:
    d "You are the one who wrote these papers?"
    "Lin was startled"
    f "No, my brother wrote it."
    f "I was say before."
    f "I can not go to school because my illness."
    f "My brother who very smart, write and teach vocabulary for me."
    d "Your brother? Die? He teached this word for you?"
    f "..."
    hide linhappy
    show linsad
    f "No, I wrote that one."
    f "One day, my brother had to move to city for university."
    f "Ma more focus on working."
    f "I realize one thing."
    f "I'm a burden."
    f "I thought ma and brother will happy."
    f "Few day later..."
    f "I died..."
    hide linsad
    d "HM!?"
    jump Lin_End

label Lin_End:
    show linmad
    i "Brother... Why you don't accept the truth?" 
    i "Why you don't accept that I already die?" 
    i "Why you acting that you don't realize me?"
    i "..."
    i "Brother Kale..."
    i "What happen to you?"
    i "Why you look so lifeless?"
    i "Why you don't smile?"
    hide linmad
    show linsad
    i "Why..."
    i "... you don't happy when I dead?"
    i "..."
    hide linsad
    h "..."
    h "......"
    h "........."
    h "Bastard Bob..." 
    h "... he always steals my food every time he sees me, if I refuse he will hit me."
    h "Dumb twins Dave and Dive always steal and hide my books..." 
    h "...I had to answer many dumb questions to get it back..." 
    h "...if I answer wrong, they will tear my books."
    h "Damn Nie always push to make me fall."
    show linsad
    i "So... those monster that you faced is your trauma?"
    i "...brother..."
    hide linsad
    h "The university like a hell. No one on my side..."
    h "...but I still suffer, waiting for the day I come home and hold you tight..."
    h "And what I got?"
    h "Lina, you're gone..."
    show linmad
    i "..."
    i "KALE!"
    i "You must go back!"
    i "You know that you have no more time!"
    hide linmad
    "The dimension started to collapse."

    scene fade2

    show linsad

    i "Think for ma!"
    i "Don't leave she alone."
    i "Don't follow my footstep!"
    i "Kale..."
    i "Save our mama..."
    i "...please..."
    hide linsad
    menu Die_Or_Live:
        h "I..."
        "Refuse to return.":
            jump BroSisDie
        "Accept to return.":
            jump ByeLine
        "(Donate to rescue both.)":
            jump Qr

label Qr:

    scene qr

    k "Your kindness will save many lives."
    "..."
    ".."
    "."
    "..."
    l "Money cannot bring those who already dead back to life..." 
    l "...But it can save those people who are near to death {s}and us, who create this game. Love you <3.{/s}"
    jump Die_Or_Live

label BroSisDie:
    h "No..."
    h "I can not suffer anymore."
    h "Mother will have a chance to have new families."
    h "Lina..."
    show linsad
    i "..."
    i "Um... you are right!"
    hide linsad
    jump Game_Over

label ByeLine:
    h "..."
    h "I will miss you..."
    show linhappy
    i "Um... goodbye brother..."
    i "Tell ma that I am sorry and dont need to remember me anymore."
    i "{i}I love you both.{/s}"
    h "Me too, Lina...{size=10}"
    hide linhappy
    jump No_Memmories

label No_Memmories:
    scene wake_up
    m "{b} KALE !!! {/b}{size=70}"
    m "Thanks godness... you are back!"
    h "..."
    h "?"
    menu LastHope:
        "What can reverse patient health?"
        "Money.":
            jump LOST
        "Emotion.":
            jump NOLOST

label LOST:

    scene wake_up_haha

    h "Excuse me miss..."
    h "But..."
    h "... who are you?"
    h "and... who am I?"
    m "..."
    "The end..."
    return

label NOLOST:  

    scene wake_up_haha     

    h "Ma..."
    h "I was dreaming a dream."
    h "I trapped in that dream."
    h "Dark and hopeless."
    m "Kale?"
    "You smile."
    h "But you know what?"
    h "Lin was there..."
    "..."
    "The end~"