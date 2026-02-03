label ep1_start_label:
if steamConfig:
    $ state = "ep1_steam"
elif True:
    $ state = "ep1"
window hide
call rpc from _call_rpc_5
stop music fadeout 5
scene black with fade
$ randInt = renpy.random.randint(0, 9)
show screen keymap_screen
$ brawler_question = True
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)

show text "{i}There are mini-games in this game.\nThe mini-games are optional but they offer you rewards such as special renders and money to spend.{/i}"
$ renpy.pause()
hide text
show text "{i}If you choose to skip mini-games, you may miss out on minor special events that happen during, or as a result of, the mini-game.{/i}"
$ renpy.pause()
hide text
show text "{i}Special renders won from mini-games can still be acquired in other ways.{/i}"
$ renpy.pause()
hide text
show text "{i}Do you want to skip mini-games?{/i}"
menu:
    "Play mini-games" if True:
        hide text
        $ dollar = 1
        $ minigames = True
        show text "{i}Done! You will always have to play the mini-games.\nIf you change your mind, you must restart the game.{/i}"
        $ renpy.pause()
        hide text
    "Skip all mini-games" if True:
        hide text
        $ dollar = 2
        $ minigames = False
        show text "{i}You will never be asked to play a mini-game during this playthrough again.\nIf you change your mind, you must restart the game.{/i}"
        $ renpy.pause()
        hide text
        show text "{i}To compensate for the loss of money, from not playing mini-games, you'll get double the money tokens from finding in-game money.{/i}"
        $ renpy.pause()
        hide text

play music "music/ep1/apra_hyde.mp3" fadein 3
"Family."
"My dad once told me that a family is more than blood relations."
"Being related doesn't necessarily make you family."
"Family are the people who support you in your choices."
"Family will help you grow."
"Family doesn't give up on you in times of need."
"Family are the ones who love you for you..."
"...whoever that may be."
"Even if you lose your family..."
"...or if your family loses you."
"Don't stop."
"Find new ones to love and somewhere else to call home."

scene d_intro with fade:
    linear 30 zoom 1.02
"That's me and my dad."
"We took that photo the day I got my driver's license."
"He was so happy that it looks like he is trying to swallow a coat hanger."
"Back then, it was just me and him."
"My mother died shortly after giving birth to me."
"It's a shame that I never got to meet her."
"I would have loved hearing stories from her past and truly getting to know her."
"Sure, my dad told me stories growing up...but his memory sucked."
"He would always forget the punchline. Not surprising, since he would talk so long before reaching the point where the punchline was supposed to be."
"Either way, I was happy back then. We didn't have much, we...erm..."
"...we had enough."
"We had each other."
"As for now?"
stop music fadeout 3
"Let me tell you what happened."

$ guideSuggestedPage = 27
scene d0_intro with Fade(1.5,1,0.5)
play music "music/ep1/windswept.mp3"
js "Haha! You're so silly!"
js "You wanna know something...?"
js "I've always had a crush on you..."
scene d0_intro1 with dissolve
js "What?"
js "You've been in love with me all this time, too?"
scene d0_intro2 with dissolve
js "You're so sweet..."
scene d0_intro3 with dissolve
js "Come closer..."
scene d0_intro4 with dissolve
js "I wanna feel your soft lips pressed against mine..."
js "Kiss me..."

play sound "sound_effects/shove.mp3"
stop music
scene d0_intro5 with hpunch
$ renpy.pause()
play music "music/ep1/roadtrip.mp3"
scene d0_intro5b with dissolve
cl "Hey, fuckface!"
cl "I said, stop daydreaming and get back to work!"
scene d0_intro5c with dissolve
mc "My name is not fuckface!"
mc "It's..."
label getPlayerName:
$ name = renpy.input("What is your name?", length=15)
$ name = name.strip()
if name == "":
    jump getPlayerName
$ tmpname = name
$ persistent.name = name
$ mc_josy = name
$ mc_maya = name
$ mc_sage = name
$ mc_isabella = name
$ mc_jill = name
$ mc_quinn = "pervert"
$ mc_riona = name
$ mc_jade = name
$ mc_cathy = name
$ mc_camila = name
if persistent.mc_josy == None:
    $ persistent.mc_josy = name
if persistent.mc_maya == None:
    $ persistent.mc_maya = name
if persistent.mc_sage == None:
    $ persistent.mc_sage = name
if persistent.mc_isabella == None:
    $ persistent.mc_isabella = name
if persistent.mc_jill == None:
    $ persistent.mc_jill = name
if persistent.mc_quinn == None:
    $ persistent.mc_quinn = name
if persistent.mc_riona == None:
    $ persistent.mc_riona = name
if persistent.mc_jade == None:
    $ persistent.mc_jade = name
if persistent.mc_cathy == None:
    $ persistent.mc_cathy = name
if persistent.mc_camila == None:
    $ persistent.mc_camila = name

if name == "fuckface" or name == "Fuckface":
    mc "Oh, wait...it is..."
elif True:
    mc "...[name]!"
scene d0_intro5d with dissolve
cl "Whatever! Get back to work, or I'll tell my dad, ok!?"
if tutorials:
    show white_screen with dissolve
    show screen majorChoiceScale
    show text "{color=#ffffff}During the game, your choices will affect a {size=+3}{size=+3}{color=#ffb052}{font=collegiate.ttf}DIK{/font}{/color}{/size}{/size} score.\nGenerally, nice reactions will decrease your {size=+3}{color=#ffb052}{font=collegiate.ttf}DIK{/font}{/color}{/size} score and vice versa.\nThe {size=+3}{color=#ffb052}{font=collegiate.ttf}DIK{/font}{/color}{/size} score will affect how characters perceive you and unlock certain actions, events and even lewd scenes.{/color}" zorder 2 with dissolve:
        ypos 0.83
    $ renpy.pause()
    hide text
    show text "{color=#ffffff}Having a high or low {size=+3}{color=#ffb052}{font=collegiate.ttf}DIK{/font}{/color}{/size} score may also lock certain actions, events or lewd scenes.\nThe girls will respond differently to how you treat them and who you are based on the {size=+3}{color=#ffb052}{font=collegiate.ttf}DIK{/font}{/color}{/size} score.\nThe score is updated at specific checkpoints during the game; you will be notified when this happens.{/color}" zorder 2 with dissolve:
        ypos 0.83
    $ renpy.pause()
    hide text
    hide screen majorChoiceScale
    hide white_screen with dissolve
menu:
    "Get mad" if True:
        mc "(You fucking cunt...)"
        $ dk(1)
    "Shrug it off" if True:
        mc "(Typical Steve...)"
        $ dk(-1)

scene d0_intro8b with dissolve
mc "(Josy...)"
mc "(I've been in love with her since I first saw her two months ago.)"
mc "(If it wasn't for her, I never would have stayed at this crappy summer job.)"
scene d0_intro8c with dissolve
mc "(She's so beautiful...)"
mc "(I could watch her smile all day long...)"

scene d0_intro9 with dissolve
cl "Hey Josephine..."
cl "What are you doing later?"
scene d0_intro10 with dissolve
js "It's Josy..."
js "...and that's none of your business, Steve."
scene d0_intro9 with dissolve
st "Come on, Josephine. Don't be like that."
st "I was thinking we could get together and maybe take a ride in my Ford Mustang."
menu:
    "Think a bad thought" if True:
        $ dk(1)
        mc "(You mean your {b}dad's{/b} Ford Mustang...)"
    "Ignore it" if True:
        $ dk(-1)
        mc "(Josy would never go for someone like Steve...)"
        mc "(She's not that kind of a girl.)"
scene d0_intro10 with dissolve
js "How many times do I have to turn you down before you take a hint?"
js "I'm not interested!"
scene d0_intro9 with dissolve
st "You're interested; you just don't know it yet."
stop music fadeout 3
st "Live a little, won't ya?"
scene d0_intro11 with vpunch
play sound "sound_effects/slap.mp3"
$ renpy.pause()
scene d0_intro12 with vpunch
play sound "sound_effects/slap.mp3"
js "Fuck off!"

play music "music/ep1/golden_alley.mp3"
scene d0_lunchroom with fade
mc "So, Josy..."
mc "I was wondering if you'd like to hang out sometime..."
mc "...maybe we could take a stroll along the river and get to know each other better?"
scene d0_lunchroom1 with dissolve
mc "Nah! Too corny."
scene d0_lunchroom with dissolve
mc "Hey, Josy!"
mc "Is that a new top?"
mc "You look radiant today!"
mc "...was that better?"
scene d0_lunchroom2 with dissolve
mc "Hey, Josy!"
js "Hey, [name]."
mc "(!!!)"
scene d0_lunchroom4 with dissolve
mc "Oh! Ah..."
mc "Is that a new top?"
scene d0_lunchroom5 with dissolve
js "Erm...these are my work clothes."
scene d0_lunchroom6 with dissolve
mc "I mean, you look like a radiator today."
js "Like a what?"
mc "Shit...no, I mean..."
scene d0_lunchroom9 with dissolve
bs "Josephine?"
js "Yes, boss?"
bs "Did you finish restocking the apple sauce in aisle 9?"
js "Steve told me he would do it."
bs "*{i}Sigh{/i}*"
bs "Fine."
scene d0_lunchroom9b with dissolve
bs "Hm..."
scene d0_lunchroom9c with dissolve
bs "Why does this frame keep tilting?"
scene d0_lunchroom9d with dissolve
mc "*{i}Whispers{/i}* I know why."
scene d0_lunchroom9e with dissolve
js "You do?"
scene d0_lunchroom9f with dissolve
mc "Yeah. I use that picture to make Tina laugh when we have our lunch breaks together."
scene d0_lunchroom9g with dissolve
js "Ok, now you have to show me!"
scene d0_lunchroom9j with dissolve
mc "Hi! I'm Steve! When I'm not busy stocking the shelves in my dad's store, I'm postponing going to the barber."
js "HAHA! That is SO funny!"
mc "How about this one?"
menu:
    "Nasty joke" if True:
        $ dk(1)
        $ RPjosy += 1
        scene d0_lunchroom9i with dissolve
        mc "\nHey, Josephine! What's pink, brown, and fits like a glove?"
        js "\nHaha! No! That's enough!"
    "Corny joke" if True:
        $ dk(-1)
        scene d0_lunchroom9h with dissolve
        mc "Hey, Josephine. I call you Josephine, because you-so-fine."
        js "Oh my god! CRINGE!!!"
scene d0_lunchroom9k with dissolve
js "Haha, that was so good, [name]!"
mc "Thanks! I'm glad you liked it."
scene d0_lunchroom9l with dissolve
mc "Employee of the month...pff..."
js "He's such an ass..."
mc "He looks like one, too."
js "Are you thinking what I'm thinking?"
mc "What?"
scene d0_lunchroom9m with dissolve
mc "Oh, wow!"
menu:
    "Draw dicks" if True:
        $ bios_history_steve = "I drew dicks on Steve's employee of the month picture.\n\n"
        $ RPjosy += 1
        $ dk(2)
        $ stevePainting = 2
        scene d0_lunchroom9n with dissolve
        mc "I'm not the best at drawing, but I think I can convey the message..."
        scene d0_lunchroom9n2 with dissolve
        mc "There!"
        js "Hahaha! I meant you should draw a funny face or something..."
        mc "Oh..."
    "Draw a funny face" if True:
        $ bios_history_steve = "I drew a funny face on Steve's employee of the month picture.\n\n"
        $ RPjosy += 1
        $ dk(1)
        $ stevePainting = 1
        scene d0_lunchroom9n with dissolve
        mc "It will be hard to make this picture uglier, but I can try."
        scene d0_lunchroom9n3 with dissolve
        js "That's perfect! That's just what I see when I look at him."
        mc "Yeah, I think I nailed it."
    "Don't draw" if True:
        $ bios_history_steve = "I resisted the urge to draw something on Steve's employee of the month picture.\n\n"
        $ dk(-2)
        $ stevePainting = 0
        scene d0_lunchroom9l with dissolve
        mc "Sorry... I don't think it's a good idea."
        js "Fine, I just thought it would be fun."

scene d0_lunchroom14 with fade
js "Whatcha reading?"
scene d0_lunchroom15 with dissolve
mc "Oh, this?"
mc "It's just a pamphlet...for college."
scene d0_lunchroom16 with dissolve
js "Oh! Burgmeister & Royce!"
js "Did you apply too?"
scene d0_lunchroom17 with dissolve
mc "Yeah, I did."
mc "But I don't think I got accepted..."
mc "Everyone I know already got their letter of acceptance in the mail."
mc "Right now, I'm just waiting for something to happen, I guess."
scene d0_lunchroom17b with dissolve
js "I know that feeling. I got put on the waiting list."
js "It sucks because I really wanna go!"
js "I know people who go there already, and even my moron stepbrother got accepted!"
scene d0_lunchroom18 with dissolve
mc "Maybe people will drop off and a spot opens up for you?"
scene d0_lunchroom17b with dissolve
js "I'm number 14 in line..."
scene d0_lunchroom18 with dissolve
mc "That sucks... It must be a popular degree."
scene d0_lunchroom20 with dissolve
js "Yeah, it's for a business degree. My dad really wanted me to go, since he went there too."
scene d0_lunchroom17c with dissolve
js "He was so happy when my stepbrother got accepted."
js "And he's not going there to study..."
js "He's just there for the frat life and parties."
js "I'm pretty sure that he cheated his way through high school..."
scene d0_lunchroom20 with dissolve
js "What about you?"
scene d0_lunchroom17 with dissolve
mc "I guess I'm going for a little bit of both."
mc "I don't really know what I want to be...but science is pretty cool, so I think I'm going for a bachelor's degree."
scene d0_lunchroom24 with dissolve
js "You think?"
scene d0_lunchroom17 with dissolve
mc "Well...I haven't really figured it out yet, but I will eventually."
mc "In the first couple of years, the classes are more or less the same for most students, with the general education classes and all."
mc "It probably doesn't matter, though..."
mc "With my luck, I'll have to stay at this place until I retire."
scene d0_lunchroom42 with dissolve
js "That makes two of us, then."
js "Hey..."
js "When do you quit work today?"
scene d0_lunchroom17 with dissolve
mc "At 4 p.m."
scene d0_lunchroom42c with dissolve
js "Sweet! Me too!"
js "My dad was going to pick me up but he texted me saying he has to work overtime."
js "He has some big client meeting or something..."
js "Can you give me a ride home?"
scene d0_lunchroom24b with dissolve
mc "Sure...but I ride a bike."
scene d0_lunchroom42 with dissolve
js "Oh, that will be awesome!"
scene d0_lunchroom42c with dissolve
stop music fadeout 3
js "My break is over."
js "Talk to you later, [name]."

play music "music/ep1/never_give_up.mp3"
scene d0_goinghome with Fade(1.5, 1, 0.5)
js "There you are!"
js "I've been waiting for you."
scene d0_goinghome1 with dissolve
mc "Sorry for being late."
mc "Steve forced me to clean the grill."
scene d0_goinghome with dissolve
js "No problemo."
js "Where's your ride?"
scene d0_goinghome3 with dissolve
mc "You're standing next to it."
scene d0_goinghome4 with dissolve
js "Hahaha!"
mc "What's wrong?"
scene d0_goinghome6 with dissolve
js "Sorry, [name]!"
js "When you said bike, I thought you meant a motorcycle."
scene d0_goinghome7 with dissolve
mc "Oh..."
mc "Well, this is what I ride."
scene d0_goinghome7b with dissolve
js "Well, hop on and give me a lift, then."
scene d0_goinghome9 with dissolve
mc "Are you ready?"
scene d0_goinghome10 with dissolve
js "Yeah. Don't do a wheelie now."
mc "Don't worry; I won't."
scene d0_goinghome12 with dissolve
js "Ok, that was a joke, but sure."
scene d0_goinghome12a with dissolve
$ renpy.pause()

scene d0_goinghome12b with fade
mc "(The way she's holding her arms around me...)"
mc "(...it feels like the warmest hug.)"
scene d0_goinghome13 with dissolve
mc "(She smells so good.)"
mc "(Just like strawberries.)"
mc "Are you comfortable back there?"
scene d0_goinghome16 with dissolve
js "Yes, I'm fine, thanks."
js "We can switch if it's too tiresome for you."
scene d0_goinghome13 with dissolve
mc "No, I'm good."
scene d0_goinghome17b with dissolve
js "I bet you give chicks rides home all the time on this thing."
scene d0_goinghome17 with dissolve
mc "No, not really."
scene d0_goinghome17b with dissolve
js "So, [name]. We haven't really talked much to each other before."
js "Besides work stuff, I mean."
scene d0_goinghome17 with dissolve
mc "Yeah, I've meant to talk more to you but never found the right opportunity for it."
scene d0_goinghome17b with dissolve
js "What are you saying? We've been working together for almost two months now!"
js "Are you a shy guy or something?"
scene d0_goinghome17 with dissolve
mc "No, not really. But you're always talking to others at work."
mc "I don't want to interrupt..."
mc "...besides, I generally like to listen more than I like to talk."
$ guideSuggestedPage = 28
scene d0_goinghome18 with dissolve
js "Haha, yeah, I tend to talk a lot."
js "Some people find it annoying."
scene d0_goinghome17 with dissolve
menu:
    "I don't mind it" if True:
        mc "I don't mind it. Talk all you want."
    "I really like it" if True:
        $ RPjosy += 1
        mc "Well, I really like that about you."
        mc "You're very easy-going; I guess that's why people are drawn to you."
        scene d0_goinghome20 with dissolve
        js "(He's really sweet.)"
        scene d0_goinghome17b with dissolve
        js "Thanks."

scene d0_goinghome26 with fade
js "This is me."
mc "Ok."
scene d0_goinghome27 with dissolve
js "So...thanks for the ride, [name]."
scene d0_goinghome28 with dissolve
mc "You're welcome."
js "..."
mc "..."
mc "So..."
mc "See you tomorrow?"
scene d0_goinghome29 with dissolve
js "All right..."
js "Bye."
stop music fadeout 5
scene d0_goinghome30 with dissolve
menu:
    "Check out her ass" if True:
        $ dk(1)
        scene d0_goinghome31 with dissolve
        $ renpy.pause()
    "Check out her boobs" if True:
        $ dk(1)
        scene d0_goinghome32 with dissolve
        $ renpy.pause()
    "Leave" if True:
        $ dk(-1)

scene d0_goinghome33 with dissolve
play music "music/patched/track_previous.mp3"
mc "(...)"
mc "(Oh no...)"
mc "(Was that a cue for me to kiss her?)"
mc "(I'm such a loser!)"

scene dik_title at transformTop2
$ renpy.pause(8)
show title_ol with dissolve
$ renpy.pause()
hide title_ol with dissolve
stop music fadeout 7
scene black with dissolve
show screen ep6_title_screen
$ renpy.pause(5)
scene d0_home with fade
mc "Dad! I'm home."
scene d0_home1 with dissolve
play music "music/ep1/golden_alley.mp3"
dad "Hey, son."
dad "You're home later than usual."
scene d0_home2b with dissolve
mc "Yeah, I was giving Josy a ride home on my bike."
scene d0_home2 with dissolve
dad "I didn't realize I raised such a charmer."
scene d0_home2b with dissolve
menu:
    "Get annoyed" if True:
        $ dk(1)
        mc "Stop it, dad..."
    "Humor him" if True:
        $ dk(-1)
        mc "The apple doesn't fall far from the tree."
scene d0_home3 with dissolve
dad "I'm proud of you, son, and I know your mother would have been, too."
scene d0_home3b with dissolve
mc "Thanks, dad."
scene d0_home5 with dissolve
mc "What's this?"
dad "Open it."
scene d0_home6 with dissolve
mc "Dear [name]...your application was..."
mc "...you are hereby accepted..."
mc "I GOT IN!"
scene d0_home7 with dissolve
dad "You did!?"
mc "Dad, I got accepted to college!!!"
scene d0_home9 with dissolve
dad "This calls for a celebration!"
scene d0_home10 with dissolve
dad "My son...a college freshman."
dad "How does that feel?"
mc "It's just unimaginable!"
scene d0_home12 with dissolve
dad "Son, I want you to take the jar from the closet."
dad "It's yours."
scene d0_home13 with dissolve
mc "No, dad. That's not my money."
scene d0_home14 with dissolve
dad "Stop it! I know that I can't afford to pay for your tuition, but at least let me help you with as much as I can."
show screen moneymsg
if tutorials:
    show white_screen with dissolve
    show text "{color=#ffffff}This game uses a simplistic money system.\nYou can carry up to five ({color=#36ca2b}$$$$${/color}) money tokens; this is your pocket money.{/color}" zorder 2 with dissolve:
        ypos 0.825
    $ renpy.pause()
    hide text
    show text "{color=#ffffff}Money is used to purchase items on special occasions and useful during certain events.\nMoney can be earned through various actions during the game. Spend your pocket money wisely.{/color}" zorder 2 with dissolve:
        ypos 0.825
    $ renpy.pause()
    hide text
scene d0_home13 with dissolve
$ money = 0
$ earnedMoney = 0
$ spentMoney = 0
menu:
    "Accept money" if True:
        $ bios_history_dad = "Dad gave me money from his personal savings.\n\n"
        $ acceptedMoneyFromDad = True
        $ mny(1)
        "{i}Received {color=#36ca2b}${/color}{/i}"
        mc "Thank you, dad!"
        mc "I love you."
        hide screen moneymsg
        scene d0_home16 with dissolve
        dad "I love you too, son."
        scene d0_home13 with dissolve
    "Ask for more money" if True:
        $ bios_history_dad = "Dad gave me money from his personal savings and I even got some more when I asked him.\n\n"
        $ dk(1)
        $ acceptedMoneyFromDad = True
        mc "Didn't you get your paycheck today?"
        scene d0_home16b with dissolve
        dad "Oh, yeah. I did..."
        dad "I think I can throw in a little bit extra for you."
        $ mny(2)
        "{i}Received {color=#36ca2b}$${/color}{/i}"
        scene d0_home16 with dissolve
        dad "I love you, son."
        scene d0_home13 with dissolve
        hide screen moneymsg
    "Reject money" if True:
        $ bios_history_dad = "Dad tried to give me money from his personal savings, but that's his money, he earned that.\n\n"
        $ dk(-1)
        $ acceptedMoneyFromDad = False
        mc "I'm sorry, dad, but no."
        hide screen moneymsg
        mc "I can't accept this. I'll take a student loan and will find a way to earn some extra pocket money."
        scene d0_home16 with dissolve
        dad "I love you, son."
        dad "You make me so proud."
        scene d0_home13 with dissolve
        mc "I love you too, dad."
$ bios_name_dad = True
mc "It will feel great to tell my boss I'm quitting tomorrow."
scene d0_home12 with dissolve
dad "I bet he will miss having you as an employee, son."
stop music

$ guideSuggestedPage = 29
scene d0_boss2
bs "Great! That saves me the trouble of firing you."
scene d0_boss2b with dissolve
mc "Oh..."
play music "music/ep1/someways.mp3"
scene d0_boss3 with dissolve
bs "College, huh?"
scene d0_boss3b with dissolve
mc "Yeah, I start on Monday."
scene d0_boss with dissolve
bs "What!? Already? You're supposed to give me two weeks' notice."
scene d0_bossb with dissolve
mc "Yeah...I know. But I didn't think I would be accepted and I got the letter of acceptance yesterday."
scene d0_boss with dissolve
bs "Mhm..."
scene d0_bossb with dissolve
mc "So, what about my pay slip?"
scene d0_boss with dissolve
bs "Well, the way I see it..."
bs "I think it's only fair that you get less than agreed upon."
scene d0_bossb with dissolve
menu:
    "Push him for more" if True:
        $ dk(1)
        mc "That's not fair at all. I'm pretty sure it's illegal, too."
        scene d0_boss with dissolve
        if stevePainting > 0:
            bs "Vandalizing company property is also illegal, buddy. I saw what you did to Steve's photo on the security cam."
            bs "You know what? I changed my mind. I'm keeping your pay as compensation for the damages."
        elif True:
            bs "Fine, I'll meet you halfway. That's me being generous, ok?"
            $ mny(2)
            show screen moneymsg
            "{i}Received {color=#36ca2b}$${/color}{/i}"
            hide screen moneymsg
    "Accept less" if True:
        $ dk(-1)
        show screen moneymsg
        mc "Ok, that's fair."
        $ mny(1)
        scene d0_boss with dissolve
        "{i}Received {color=#36ca2b}${/color}{/i}"
        bs "That's only because I'm generous. Make sure you remember that."
        hide screen moneymsg
stop music fadeout 3
bs "Wash your clothes and return them to me by the end of the week."

play music "music/ep1/winter_sunshine.mp3"
scene d0_js with wipeleft
mc "Hi, Josy."
js "Hey, [name]!"
js "Everything good?"
scene d0_js2 with dissolve
mc "It's better than good, actually."
mc "I got my letter of acceptance yesterday!"
scene d0_js3 with dissolve
js "You did!? Wow, that's awesome!"
scene d0_js3b with dissolve
js "Congratulations!!!"
js "I'm so jealous!"
scene d0_js4 with dissolve
js "So, you're leaving me here, huh?"
scene d0_js4b with dissolve
menu:
    "Yes, sorry" if True:
        mc "Yeah... I'm sorry for that..."
        scene d0_js6 with dissolve
        js "Hey, don't feel sorry for me."
        js "I only need 13 people to decline, and I'm golden."
        scene d0_js4b with dissolve
        mc "Haha! I'm glad that you're staying positive."
        scene d0_js6b with dissolve
    "I can stay if you want" if True:
        mc "I can stay if you want..."
        scene d0_js7 with dissolve
        js "Are you crazy? You got in!"
        js "Go chase your dream!"
        scene d0_js6b with dissolve
js "But I will miss you."
if dtype < 0:
    scene d0_js8 with dissolve
    "*{i}Smack{/i}*"
scene d0_js9 with dissolve
mc "I'll come back and visit once in a while, you know."
mc "I mean, it's not far from here, and my dad still lives here."
scene d0_js10 with dissolve
js "I'd love that..."
js "When are you leaving?"
scene d0_js9 with dissolve
mc "I start on Monday."
scene d0_js10 with dissolve
js "No way! This Monday?"
scene d0_js9 with dissolve
mc "Yeah, afraid so."
scene d0_js12b with dissolve
js "Hey, I know!"
js "We should do something fun this weekend!"
js "You know, to celebrate!"
scene d0_js13 with dissolve
mc "Well, all right. What do you have in mind?"
scene d0_js10 with dissolve
js "Pick me up tomorrow night on that {i}sweet ride{/i} of yours, and I'll show you!"
scene d0_js9 with dissolve
menu:
    "Ok" if True:
        mc "Ok. I will."
    "It's a date!" if True:
        $ RPjosy += 1
        mc "It's a date!"
        scene d0_js16 with dissolve
        js "Haha..."
stop music fadeout 3
scene d0_js17 with dissolve
st "Back to work, Josy."
play music "music/ep1/roadtrip.mp3"
if stevePainting >0:
    scene d0_js17b with dissolve
    st "So, you think you're pretty funny, huh?"
    scene d0_js17c with dissolve
    menu:
        "Trigger him" if True:
            $ dk(1)
            mc "I've been known to tell a joke or two."
            mc "Knock knock."
            scene d0_js17d with dissolve
            st "Fuck you!"
            scene d0_js17c with dissolve
            mc "You're supposed to say \"Who's there?\", Steve. Didn't your imaginary friends teach you that one?"
        "What do you mean?" if True:
            $ dk(-1)
            mc "What do you mean?"
    scene d0_js17d2 with dissolve
    if stevePainting == 2:
        st "Drawing dicks on my face is not funny, you asshole!"
        scene d0_js17c with dissolve
        mc "I strongly disagree."
        scene d0_js17d2 with dissolve
    elif True:
        st "Why the fuck did you draw on my picture!?"
    st "I earned that award!"
    scene d0_js18 with dissolve
    st "Dad just told me that you're quitting."
    st "Thank fuck for that. I knew this job was too hard for you."
    scene d0_js19 with dissolve
    mc "Not really. I can't work here and go to B&R."
elif True:
    scene d0_js18 with dissolve
    st "Dad just told me that you're quitting."
    st "That was the best news I've heard in a long time."
    scene d0_js19 with dissolve
    mc "Well, I can't work here and go to B&R."
scene d0_js18 with dissolve
st "*{i}Snorts{/i}* B&R, the poor man's college."
scene d0_js19 with dissolve
mc "What are you talking about? It's not a bad college."
scene d0_js18 with dissolve
st "Aside from that preppy, silver spoon in their asses frat house..."
st "...yeah, people who go there are trash."
scene d0_js19 with dissolve
menu:
    "Retort" if True:
        $ dk(1)
        mc "You're one to talk!"
        mc "If it wasn't for your dad, you and your 50's haircut would be picking up litter in the park for a living."
        scene d0_js17d2 with dissolve
        st "Watch your mouth!"
        scene d0_js19 with dissolve
        mc "Or what? Will you have your dad fire me?"
        mc "Oh, wait... That's right, I already quit."
        scene d0_js22b with dissolve
        st "I'll be the owner of this place one day, you know!"
        stop music fadeout 10
        st "Remember that when you come crawling back."
        scene d0_js22c with dissolve
        mc "Good luck with the family business, Steve. Call me when you do something without daddy's help."
    "Ignore him" if True:
        $ dk(-1)
        mc "Whatever, Steve. Enjoy working here."
        scene d0_js22b with dissolve
        stop music fadeout 10
        st "I'll be the owner of this place one day, you know!"
        st "Remember that when you come crawling back."
$ bios_history_steve += "Steve tried to pick a fight with me when he heard that I was quitting my job.\n\n"
play music "music/ep1/food_chain_short.mp3"
play sound "sound_effects/hit.mp3"
scene d0_fight0 with vpunch
$ renpy.pause(0.5)
play sound "sound_effects/hit.mp3"
scene d0_fight1 with vpunch
$ renpy.pause(0.5)
play sound "sound_effects/hit.mp3"
scene d0_fight0 with vpunch
$ renpy.pause(0.5)
scene d0_fight2 with dissolve
dad "Great! Don't stop now!"
dad "High kick!"
play sound "sound_effects/hit.mp3"
scene d0_fight3 with vpunch
$ renpy.pause(0.5)
dad "Perfect!"
scene d0_fight2 with dissolve
dad "Flurry!"
play sound "sound_effects/hit.mp3"
scene d0_fight0 with vpunch
$ renpy.pause(0.5)
play sound "sound_effects/hit.mp3"
scene d0_fight1 with vpunch
$ renpy.pause(0.5)
play sound "sound_effects/hit.mp3"
scene d0_fight0 with vpunch
$ renpy.pause(0.5)
scene d0_fight3b with dissolve
stop music fadeout 10
dad "Great, son! That will do for today."
scene d0_fight4 with dissolve
dad "So, how did it go with your boss?"
scene d0_fight5 with dissolve
play music "music/ep1/never_give_up.mp3"
mc "It went ok. It could've gone better, but I'm done with that place now."
scene d0_fight5b with dissolve
dad "The next step in your life is a big one, son."
dad "As I never went to college, I can't imagine how exciting this must feel for you."
scene d0_fight6 with dissolve
mc "Yeah..."
dad "Something the matter?"
scene d0_fight8 with dissolve
mc "Well, there's this girl...Josy."
mc "I have a crush on her, and now I'm moving away from here."
mc "I feel pretty bad about it."
scene d0_fight9 with dissolve
dad "Uh-huh. I see."
dad "Let me tell you something I've learned."
scene d0_fight10 with dissolve
dad "As you know, I already worked in construction when I met your mom."
dad "Her dad, who was filthy rich, hired me to help him build a hotel."
scene d0_fight11 with fade
dad "Your mom was a very beautiful woman. I was 24, and she had just turned 18."
dad "Her dad disapproved of me being with his daughter. In his eyes, I was of a lower class."
scene d0_fight12 with dissolve
dad "Your mother didn't see it that way. She looked past all that, and we fell in love."
scene d0_fight13 with dissolve
dad "To her father's dismay, he couldn't get her to stop seeing me."
dad "But he knew that once the hotel was built, there was no reason for me to stay and work in that town."
scene d0_fight14 with dissolve
dad "And when that day came, I left. I had to make a living after all."
dad "So, with a heavy heart, I left Lynette."
scene d0_fight15 with dissolve
dad "But before doing so, I gave her the best kiss I ever could have given her."
scene d0_fight16 with dissolve
dad "To me...that was it."
dad "The last time I would ever gaze upon her."
scene black with fade
dad "But your mom, stubborn as a mule, didn't give up that easily."
scene d0_fight18 with dissolve
dad "It took her three days to run away from home and track me down."
dad "No...wait...five days?"
dad "Hm...maybe it was something along the lines of a week?"
mc "Are you seriously asking {b}me{/b} that?"
dad "No, well, it was something like that."
dad "Either way...where was I?"
dad "Oh yeah!"
dad "She didn't want her dad's life or his money..."
dad "She wanted me."
scene d0_fight10 with dissolve
dad "If something's meant to be, it will happen, son."
dad "But make sure that you give it your best try and that you leave without regrets."
dad "Because regrets can come back to haunt you later in life."
scene d0_fight8 with dissolve
mc "I regret never meeting mom."
scene d0_fight21 with dissolve
dad "Hey now, you can't regret things out of your control."
dad "And you did meet her briefly before she passed away."
scene d0_fight10 with dissolve
dad "She said \"He's so beautiful\". Those were her exact words about you."
stop music fadeout 10
dad "Tell Josy how you feel, son. That's my advice."
dad "Don't keep your emotions locked up."
$ guideSuggestedPage = 30
jump ep1_freeroam_home_label

label ep1_date_label:
$ current_task = "None"
$ chat_new_tasks = False
$ renpy.block_rollback()
scene d0_date with Fade(1.5, 1, 0.5)
play music "music/ep1/scrapbook.mp3"
mc "(I wonder what Josy has planned for us.)"
mc "(It sure feels like a date...)"
mc "(A Saturday night, starry sky...)"
mc "(This is my only shot if I want to make a move on her.)"
scene d0_date_1 with dissolve
js "Hey [name]!"
mc "Hi Josy!"
js "Were you too scared to ring the doorbell, or what?"
scene d0_date_2 with dissolve
mc "Oh, sorry. I thought we were supposed to meet out here."
scene d0_date_3 with dissolve
js "Haha, it's ok."
if ep1_josy_chat1_state > 0:
    scene d0_date_2 with dissolve
    mc "I see that you found something to wear."
    scene d0_date_3 with dissolve
    js "Yeah, I did."
    scene d0_date_2 with dissolve
    if ep1_josy_chat1_state == 2:
        menu:
            "I like it" if True:
                $ RPjosy += 1
                if dtype > 0:
                    mc "You look hot in it."
                elif True:
                    mc "I like it! You look very pretty."
                scene d0_date_4 with hpunch
                js "Stop it..."
                scene d0_date_3 with dissolve
            "It's better than wearing nothing." if True:
                $ RPjosy += 1
                mc "It's better than wearing nothing."
                scene d0_date_3 with dissolve
                js "Still thinking about that, huh?"
            "Let's go" if True:
                mc "Ok, let's go."
                scene d0_date_3 with dissolve
    elif True:
        menu:
            "I like it" if True:
                $ RPjosy += 1
                if dtype > 0:
                    mc "You look hot in it."
                elif True:
                    mc "I like it! You look very pretty."
                scene d0_date_4 with hpunch
                js "Stop it..."
                scene d0_date_3 with dissolve
            "Let's go" if True:
                mc "Ok, let's go."
                scene d0_date_3 with dissolve
$ guideSuggestedPage = 31
js "Scoot forward and make space for my cute butt."
scene d0_date_2 with dissolve

menu:
    "Flirt with her" if True:
        if dtype > 0:
            $ bios_history_josy = "I flirted with Josy, but I think she took it the wrong way.\n\n"
            $ bios_name_josy = True
            $ chat_new_bios = True
            mc "I think you meant cute and sexy butt."
            scene d0_date_4b with dissolve
            js "[name]... Really?"
            $ RPjosy -= 1
            js "You sound like Steve."
        elif True:
            $ bios_history_josy = "I flirted with Josy and I think she liked it.\n\n"
            $ bios_name_josy = True
            $ RPjosy += 1
            $ chat_new_bios = True
            mc "It is very cute."
            scene d0_date_4 with hpunch
            js "Haha, [name]..."
    "Don't push your luck" if True:
        mc "Ok."

scene d0_date_5 with fade
mc "Where am I taking us?"
scene d0_date_6 with dissolve
js "Just a bit further..."
js "You see that road to the right over there? Go that way."
scene d0_date_5 with dissolve
stop music fadeout 5
mc "I think that's a dead end."
scene d0_date_6 with dissolve
js "Trust me; it's the right way."

scene d0_date_7 with fade
$ renpy.sound.play("sound_effects/crickets.mp3", channel="sfx1", loop=True)
js "Here we are!"
play music "music/ep1/windswept.mp3"

menu:
    "Check her out ({color=#ffffff}{size=-1}{font=collegiate.ttf}DIK{/font}{/size}{/color} or {color=#ffffff}{size=-1}{font=collegiate.ttf}CHICK{/font}{/size}{/color})" if dtype != 0:
        if dik > 5:
            scene d0_date_7b with dissolve
        elif True:
            scene d0_date_7c with dissolve
        $ renpy.pause()
    "Don't push your luck" if True:
        $ renpy.pause(0.2)

scene d0_date_7 with dissolve
if dik > 5:
    mc "This is a pretty cool place!"
elif True:
    mc "Such a beautiful place."
scene d0_date_8 with dissolve
js "Yes! This is my little sanctuary."
js "I've never seen anyone come here before."
js "I found this place one day when I was out running and got lost."
js "Since then, I have come here once in a while to think."
scene d0_date_8b with dissolve
mc "What do you think about?"
scene d0_date_8 with dissolve
js "You know, about life and the future."
scene d0_date_10 with dissolve
js "Come, sit with me."
scene d0_date_10a with dissolve
js "I'm gonna try to let you do the talking for a while."
js "Otherwise, I'll just blabber on."
scene d0_date_10aa with dissolve
js "Did you like working at the minimart this summer?"
mc "It was all right. The pay was decent."
scene d0_date_10b with dissolve
js "Yeah, I guess you're going to need it if you're going to B&R."
scene d0_date_10c with dissolve
mc "Sure, but I'm taking a student loan, just like most students."
mc "Aren't you?"
scene d0_date_10d with dissolve
js "No, my dad has saved up for my tuition."
js "Didn't your parents do the same?"
scene d0_date_10g with dissolve
mc "My mom passed away shortly after I was born, so it's just been me and my dad."
scene d0_date_10h with dissolve
js "Oh, I'm so sorry!"
scene d0_date_10g with dissolve
mc "Don't worry; you couldn't have known that."
scene d0_date_10i with dissolve
mc "He takes very good care of me, but no...he can't afford my college tuition."
scene d0_date_10j with dissolve
mc "But it doesn't matter. I love my dad."
mc "He's taught me everything I know..."
mc "...well, it's mostly \"man stuff\", like carpentry and martial arts."
scene d0_date_10k with dissolve
js "Haha! \"Man stuff\"? Listen to you."
js "I know someone who would hate you for saying that."
js "Women know about that, too, you know."
scene d0_date_10l with dissolve
mc "I didn't mean it that way. Of course, women know about it..."
mc "...all I'm saying is that my dad teaches me what he knows, and it's often of that nature."
scene d0_date_10k with dissolve
js "The man stuff nature?"
scene d0_date_10l with dissolve
mc "Haha, sorry. I don't know how to describe it differently."
mc "I try to teach myself stuff too. For instance, I've been playing guitar since I was twelve years old."
scene d0_date_10k with dissolve
js "Oh, I'd love to hear you play for me sometime!"
scene d0_date_10l with dissolve
mc "Yeah, maybe..."
mc "So, you know a lot about carpentry and martial arts, then?"
scene d0_date_10m with dissolve
js "Haha, no! I didn't mean that {b}I{/b} knew about it."
js "But I guess it could be fun to take a self-defense class or something."
scene d0_date_10l with dissolve
mc "Hey, I can teach you that!"
scene d0_date_10o with dissolve
js "Really?"
scene d0_date_10p with dissolve
mc "Stand up. We can start small."
js "Haha, ok!"
scene d0_date_10q with dissolve
mc "Put your palms up like this."
js "Uh-huh."
mc "Now, strike with your left-hand palm against mine."
play sound "sound_effects/hit.mp3"
scene d0_date_10s with vpunch
js "Ah!!!"
scene d0_date_10t with dissolve
mc "Are you ok!?"
js "Hahaha! Sorry, I slipped!"
js "Did I hurt you?"
mc "Haha, no, I'm fine."
if dtype < 1:
    scene d0_date_10u2 with dissolve
    $ RPjosy += 1
    mc "Here, let me help you up."
scene d0_date_10v with dissolve
mc "Yeah, this isn't the best place to teach you this."
mc "Let's sit down again instead."
scene d0_date_11c with dissolve
js "Say cheese!"
mc "Oh, ok. Cheese!"
scene white
play sound "sound_effects/camera_shutter.mp3"
$ renpy.pause(0.5)
scene d0_date_11c with dissolve
js "Haha! Thanks."
scene d0_date_11 with dissolve
js "I can send it to you later."
js "But now..."
js "...I got us something for tonight."
scene d0_date_11b with dissolve
js "Tada!"
mc "Oh wow, you got booze?"
js "Haha, yup! I told you that I wanted to celebrate with you!"
scene d0_date_12b with dissolve
mc "Where did you even get this?"
scene d0_date_12c with dissolve
js "I swiped it from my dad's cabinet."
scene d0_date_12b with dissolve
mc "Let me guess. You're hoping he will blame your brother for it?"
scene d0_date_12c with dissolve
js "Haha, maybe."
scene d0_date_13 with dissolve
$ renpy.pause()
scene d0_date_14 with dissolve
js "Here, have a sip!"
if dtype < 0:
    mc "It's pure vodka!"
    js "Haha, I know."
scene d0_date_15 with dissolve
$ renpy.pause()
scene d0_date_16 with dissolve
stop music fadeout 5
mc "That's some strong stuff!"
js "Haha, yeah!"

label ep1_josy_lewd:
if _in_replay:
    hide screen phone_screen
    if persistent.name == None:
        $ name = "MC"
    elif True:
        $ name = persistent.name
play music "music/ep1/lonely.mp3"
scene d0_date_17 with Fade(1.5, 1, 0.5)
mc "It's so nice of you to do this for me. I really appreciate it!"
scene d0_date_18 with dissolve
js "I really wish we did this back when we started working together and not during your last weekend here."
mc "Yeah, me too."
scene d0_date_20 with dissolve
js "I'm starting to get kind of tipsy over here."
mc "We should've bought some sodas to mix the vodka with."
scene d0_date_22 with dissolve
js "Haha, you're cute."
mc "(Did I say something?)"
scene d0_date_23 with dissolve
mc "(Oh, ok...)"
mc "(Wow, she's really hugging me tightly.)"
scene d0_date_23b with dissolve
mc "(There's that wonderful smell of strawberries again...)"
mc "(This is it, [name]. It's now or never.)"
mc "(I'm just gonna put it out there.)"
mc "Josy?"
scene d0_date_24 with dissolve
js "Yeah?"
scene d0_date_23b with dissolve
mc "I know this may sound a bit weird, but I just have to say it..."
mc "This summer, working with you has been really awesome."
mc "Even though I haven't really shown it..."
mc "...I've had a crush on you since the start of this summer."
scene d0_date_26b with dissolve
js "You have?"
mc "Yeah, I just wanted to tell you, so I don't regret it later on."
scene d0_date_28 with dissolve
js "[name]... That's so sweet..."
scene d0_date_29 with dissolve
$ renpy.pause()
image anim_josy_kiss_01_ep1 = Movie(channel="anim_josy_kiss_01_ep1", play="images/movies/ep1/anim_josy_kiss_01_ep1.webm")
scene anim_josy_kiss_01_ep1 with dissolve:
    size (config.screen_width, config.screen_height)
pause
image anim_josy_kiss_02_ep1 = Movie(channel="anim_josy_kiss_02_ep1", play="images/movies/ep1/anim_josy_kiss_02_ep1.webm")
scene anim_josy_kiss_02_ep1 with dissolve:
    size (config.screen_width, config.screen_height)
pause
if _in_replay:
    if persistent.ep1_josy_lewd_full or persistent.ep1_josy_lewd_chick:
        image anim_josy_kiss_03_ep1 = Movie(channel="anim_josy_kiss_03_ep1", play="images/movies/ep1/anim_josy_kiss_03_ep1.webm")
        scene anim_josy_kiss_03_ep1 with dissolve:
            size (config.screen_width, config.screen_height)
        pause
    if persistent.ep1_josy_lewd_full or persistent.ep1_josy_lewd_dik:
        image anim_josy_kiss_04_ep1 = Movie(channel="anim_josy_kiss_04_ep1", play="images/movies/ep1/anim_josy_kiss_04_ep1.webm")
        scene anim_josy_kiss_04_ep1 with dissolve:
            size (config.screen_width, config.screen_height)
        pause
elif True:
    if dik < -5:
        image anim_josy_kiss_03_ep1 = Movie(channel="anim_josy_kiss_03_ep1", play="images/movies/ep1/anim_josy_kiss_03_ep1.webm")
        scene anim_josy_kiss_03_ep1 with dissolve:
            size (config.screen_width, config.screen_height)
        pause
    elif dik > 5:
        image anim_josy_kiss_04_ep1 = Movie(channel="anim_josy_kiss_04_ep1", play="images/movies/ep1/anim_josy_kiss_04_ep1.webm")
        scene anim_josy_kiss_04_ep1 with dissolve:
            size (config.screen_width, config.screen_height)
        pause
scene d0_date_30 with dissolve
mc "I've wanted to do that for so long, Josy..."
$ renpy.end_replay()
if dtype > 0:
    $ persistent.ep1_josy_lewd_dik = True
elif True:
    $ persistent.ep1_josy_lewd_chick = True
if persistent.ep1_josy_lewd_dik and persistent.ep1_josy_lewd_chick:
    $ persistent.ep1_josy_lewd_full = True
$ calcScenes()
js "[name]... I'm sorry..."
js "I shouldn't have done that..."
mc "What? Why?"
scene d0_date_32 with dissolve
js "I'm already in a relationship..."
scene d0_date_33 with dissolve
mc "You're what?"
scene d0_date_30 with dissolve
js "I'm so sorry..."
js "It's complicated..."
js "I didn't mean for {i}this{/i} to happen..."
scene d0_date_32 with dissolve
js "But you're so..."
scene d0_date_33 with dissolve
js "..."
scene d0_date_30 with dissolve
js "I've had a crush on you too."
mc "Really? Wow..."
mc "That's great!"
scene d0_date_32 with dissolve
js "It's not great, [name]..."
js "By doing this right now, I'm cheating..."
scene d0_date_38 with dissolve
js "Fuck... I gotta go..."
js "Please... Take me home..."
scene d0_date_38b with dissolve
js "..."
mc "Are you cold?"
scene d0_date_38c with dissolve
js "Just a tad..."
mc "Here..."
$ renpy.music.stop(channel="sfx1", fadeout=3)

scene d0_date_39 with fade
mc "(She's holding me even tighter than she did before...)"
mc "(I can't believe this is happening...)"
mc "(We have crushes on each other...)"
mc "(...but we still can't be together.)"
scene d0_date_40 with dissolve
mc "(She must be in an unhappy relationship to do something like this...)"
mc "(Maybe it's for the best, though?)"
mc "(I'm still leaving for college, and she is likely staying here.)"
mc "(...)"
mc "(Even so, it still hurts.)"
mc "(At least I don't have to regret never telling her how I feel.)"
scene d0_date_41 with Fade(1.5, 1, 0.5)
mc "Thanks for the night, Josy..."
mc "I guess this is where we say farewell."
scene d0_date_42 with dissolve
js "Farewell? You're still coming back to visit, right?"
scene d0_date_43 with dissolve
mc "I just thought...with what happened and all..."
mc "Maybe it's just best to leave it like this?"
scene d0_date_44 with dissolve
js "Ok..."
js "What about your sweatshirt?"
mc "You can keep it."
js "..."
js "Farewell, then."
scene d0_date_45 with dissolve
mc "(Fuck...)"
mc "(This doesn't feel very good.)"
mc "(Will this huge pain in my chest go away already.)"
js "[name]!!!"
scene d0_date_46 with dissolve
js "Wait!"
scene d0_date_48 with dissolve
js "It's goodbye."
js "Do you understand me?"
js "Goodbye...not farewell..."
scene d0_date_49 with dissolve
mc "Goodbye, it is."
$ bios_history_josy += "I went out on a date with Josy. It started out great, but after we made out I learned that she's in a relationship and was cheating by being with me. That hurt like hell to hear...\n\n"
$ bios_name_josy = True
$ chat_new_bios = True

scene d0_after_date with Fade(1.5, 1, 0.5)
mc "(She's in a relationship...?)"
mc "(I should've known. She's way too perfect to be single.)"
mc "(Why did she lead me on, though?)"
scene d0_after_date1 with dissolve
mc "(She's been so forward with me...hugging me...)"
mc "(...kissing my cheek.)"
mc "(I feel like such an idiot.)"
mc "(Not farewell...?)"
mc "(What am I supposed to do with that?)"
mc "(Am I supposed to cling to hope?)"
scene d0_after_date2 with dissolve
mc "(...or maybe just distance myself?)"
stop music fadeout 10
mc "(I'm going away to college...how much more can I distance myself from her?)"
mc "(I'm going away...and her boyfriend is not.)"
mc "(Fuck... I need to find a way to get over her...)"

scene black with Fade(1.5, 1, 0.5)
image ep1_bg_scroll:
    "images/ep1/car/car_scrolling_bg.jpg"
    xalign 0.0
    linear 1 xalign 1.0
    repeat
show black zorder 3
show ep1_bg_scroll zorder 1
show d1_drive zorder 2
hide black
play music "music/ep1/someways.mp3"
dad "The first day of college..."
dad "I wonder what that feels like..."
dad "How does it feel, son?"
hide d1_drive
show d1_drive1 zorder 2
menu:
    "I feel excited" if True:
        mc "I feel pretty excited, dad."
        hide d1_drive1
        show d1_drive zorder 2
        dad "That's the spirit!"
    "I'm nervous" if True:
        mc "I'm kind of nervous..."
        hide d1_drive1
        show d1_drive zorder 2
        dad "I'm sure you'll be fine."
hide d1_drive
show d1_drive1 zorder 2
mc "You really didn't have to rent a car for this..."
mc "I would have been fine taking the train."
hide d1_drive1
show d1_drive zorder 2
dad "Nonsense! This is a big day for both of us!"
hide d1_drive
show d1_drive4 zorder 2
dad "Now, I've heard what college is like."
dad "There will be a lot of...uh...temptations that you'll face as a freshman."
dad "I just want you to know that it's ok to say no, son."
hide d1_drive4
show d1_drive5 zorder 2
mc "Do you mean to say no to drinking alcohol?"
hide d1_drive5
show d1_drive zorder 2
dad "Well, you're a grown man now."
dad "Alcohol won't kill you..."
dad "...unless you overdo it, of course."
dad "But it's not just alcohol that may be tempting you."
hide d1_drive
show d1_drive4 zorder 2
dad "You might come in contact with drugs."
dad "I want you to be safe, son."
hide d1_drive4
show d1_drive5 zorder 2
mc "Don't worry, dad. I don't have any interest in doing drugs."
mc "I'm going to college to educate myself."
hide d1_drive5
show d1_drive4 zorder 2
dad "Also..."
dad "I know that I haven't really talked to you about the birds and the bees yet..."
hide d1_drive4
show d1_drive5 zorder 2
mc "You don't have to, dad."
mc "I'm well aware of how that works."
hide d1_drive5
show d1_drive4 zorder 2
dad "Please know that there's no shame in putting on a condom."
hide d1_drive4
show d1_drive5 zorder 2
mc "I know, dad!"
hide d1_drive5
show d1_drive zorder 2
dad "Hey... I know that your date didn't go as you hoped it would."
dad "But, chin up! Heartbreak is a natural thing."

scene d1_drive13 with fade:
    linear 10 zoom 1.1
dad "Here we are."
dad "Burgmeister & Royce."
dad "It sounds so fancy!"
mc "It's not that big of a college, dad."
dad "Ah! An elitist college, then!"
scene d1_drive16 with dissolve
dad "Take care, son!"
dad "Don't forget to call."
scene d1_drive17 with dissolve
mc "Thanks, dad! I won't forget."
scene d1_drive16 with dissolve
dad "Come, give your old man a hug."
scene d1_drive19 with dissolve
jc "GAY ALERT!!!"
scene d1_drive20 with dissolve
jc "Why don't you grab his dick while you're at it!?"

scene d1_college with wipeleft
mc "Excuse me..."
scene d1_college1 with dissolve
rc "Hi, how may I help you?"
scene d1_college2 with dissolve
mc "I'm a freshman...I have no clue where I'm supposed to be."
scene d1_college1 with dissolve
rc "ID, please."
scene d1_college3 with dissolve
rc "You're late, you know?"
scene d1_college4 with dissolve
mc "Am I?"
scene d1_college3 with dissolve
rc "Yeah, you were supposed to be here one hour ago."
scene d1_college4 with dissolve
mc "So...what should I do?"
scene d1_college1 with dissolve
rc "Today is orientation; freshmen are walking around campus, visiting the different fraternities and the sorority."
rc "I suggest that you find your dorm quickly and then join the campus tour."
rc "I take it that you've already signed up for a B&R ID online?"
scene d1_college2 with dissolve
mc "I have."
scene d1_college10 with dissolve
rc "That's great."
rc "Here's the key to your shared dorm, you're in the eastern wing. The dorm number is 66."
stop music fadeout 5
scene d1_college2 with dissolve

menu:
    "Thank her" if True:
        $ dk(-1)
        mc "Thank you!"
        scene d1_college1 with dissolve
        rc "You're most welcome."
    "Just leave" if True:
        $ dk(1)
        scene d1_college1 with dissolve
        rc "...you're welcome."

play music "music/ep1/funk_rock.mp3"
scene d1_dorm0 with fade
mc "(Is this the right corridor?)"
mc "(Everything looks the same here...)"
mc "(Would it be the worst thing to put up comprehensible signs?)"
scene d1_dorm with dissolve
mc "(Dorm 66...this is it.)"
mc "(Hah. That's cute.)"
scene d1_dormc with dissolve
troy "Hey hey hey! You can't just barge in here!"
troy "Who the fuck are you!?"
scene d1_dorm1 with dissolve

menu:
    "Be confident" if True:
        $ dk(1)
        mc "Settle down. This is my dorm, too."
        scene d1_dorm2 with dissolve
    "Be friendly" if True:
        $ dk(-1)
        mc "Hi, I'm [name]."
        mc "I believe I'm your dorm buddy."
        scene d1_dorm2 with dissolve
        troy "Not another one! I fucking told them yesterday..."
troy "I don't want to share this dorm!"
troy "Find somewhere else to sleep."
scene d1_dorm1 with dissolve
mc "I don't think it works that way..."
scene d1_dormc with dissolve
troy "Hey, shithead!"
troy "I'm not going to live here with you."
scene d1_dorm1 with dissolve
$ guideSuggestedPage = 32
menu:
    "Be rude" if True:
        $ dk(1)
        mc "Well, then maybe you should leave. Because I'm not."
    "Be friendly" if True:
        $ dk(-1)
        mc "Come on, don't be like that."
        mc "I'm sure we can get along."

scene d1_dorm5 with dissolve
troy "Fucking morons are running this place."
scene d1_dorm6 with dissolve
troy "If I have to share this dorm with you, here's the deal..."
troy "You're allowed to sleep on that bed."
troy "But daytime, when I'm in here, you're not."
troy "Got it!?"
mc "I guess."
scene d1_dorm9 with dissolve
troy "Good. Now drop your shit off and get out before I change my mind."
scene d1_dorm9b with dissolve
mc "Can we start over and try to get along?"
mc "I could use someone to help me find the campus tour group."
scene d1_dorm9b2 with dissolve
stop music fadeout 5
troy "Oh, you could?"
play sound "sound_effects/door_slam.mp3"
scene d1_dorm with hpunch
mc "..."

$ bios_troy = True
$ bios_history_troy = "I just met Troy and he's an asshole. It will be difficult to share a dorm with someone who doesn't want me there.\n\n"
$ bios_name_troy = True
$ chat_new_bios = True
mc "(What a shitty start this has been...)"

play music "music/ep1/fresh_air.mp3"
scene d1_corridor with fade
mc "(Where did everybody go?)"
mc "(Should I go back to the reception and ask for help?)"
scene d1_corridor1 with dissolve
mc "Ah!!!"
scene d1_corridor2 with hpunch
mc "Dammit..."
uk "Haha. Do you need a hand?"
scene maya_intro at transformTop with fade
$ renpy.pause()
scene d1_corridor3 with dissolve
mc "Oh, hi..."
menu:
    "Sure" if True:
        mc "Sure."
        scene d1_corridor4 with dissolve
        menu:
            "Check her panties ({color=#ffffff}{size=-1}{font=collegiate.ttf}DIK{/font}{/size}{/color})" if dtype > 0:
                $ bios_history_maya = "I met Maya today while I was lying on the floor; she offered to help me get back up.\nWhile helping me up I got a good look at her panties, she noticed and didn't seem to like it.\n\n"
                $ bios_name_maya = True
                $ chat_new_bios = True
                $ RPmaya -= 1
                $ dk(1)
                scene d1_corridor4b with dissolve
                mc "(Holy shit...)"
                scene d1_corridor4c with dissolve
                uk "Hey..."
                mc "Sorry..."
            "Check her out" if True:
                $ bios_history_maya = "I met Maya today while I was lying on the floor; she offered to help me get back up.\nWhile helping me up I kind of checked her out, she noticed and seemed flattered.\n\n"
                $ bios_name_maya = True
                $ chat_new_bios = True
                $ RPmaya += 1
                scene d1_corridor4d with dissolve
                mc "(Yum...)"
            "Don't push your luck" if True:
                $ dk(-1)
                $ bios_history_maya = "I met Maya today while I was lying on the floor; she helped me get back up.\n\n"
                $ bios_name_maya = True
                $ chat_new_bios = True
    "No thanks" if True:
        $ bios_history_maya = "I met Maya today while I was lying on the floor; she offered to help me get back up but I declined.\n\n"
        $ bios_name_maya = True
        $ chat_new_bios = True
        mc "No thanks."
scene d1_corridor5 with dissolve
uk "That was quite a fall. Are you ok?"
scene d1_corridor7 with dissolve
mc "Yeah, I was too busy figuring out where I was going."
scene d1_corridor9 with dissolve
uk "Ah, that must mean that you're a freshman?"
scene d1_corridor7 with dissolve
mc "Yeah, that's right. I'm [name], by the way."
scene d1_corridor8 with dissolve
my "Cool. I'm Maya."
scene d1_corridor9 with dissolve
my "So, what are you doing in here?"
my "Today's orientation day!"
scene d1_corridor10 with dissolve
mc "Yeah, I know...but I arrived too late and missed the tour."
scene d1_corridor11 with dissolve
my "Well, that sucks."
scene d1_corridor10 with dissolve
mc "Yeah..."
scene d1_corridor9 with dissolve
my "Shit, now I feel bad for you."
my "How about I show you around, instead?"
scene d1_corridor10 with dissolve
mc "Would you do that?"
scene d1_corridor15 with dissolve
my "Sure, follow me."
scene d1_corridor16 with dissolve
mc "I take it you're not a freshman yourself?"
scene d1_corridor17 with dissolve
my "Actually, I am. But I'm also a local, so I've been here at high school events."
my "It's not a big campus, really."
scene d1_corridor18 with dissolve
mc "What are you going to study?"
scene d1_corridor19 with dissolve
my "I've applied for a social work degree."
scene d1_corridor18 with dissolve
mc "Ok...I don't really know what that means."
scene d1_corridor19 with dissolve
my "Hah, that's ok."
my "Besides, I think most freshmen have the same general education classes the first year anyway."
scene d1_corridor18 with dissolve
mc "The selection was pretty poor..."
stop music fadeout 5
scene d1_corridor20 with dissolve
my "That's small colleges for you."

play music "music/ep1/dont_count_on_me.mp3"
scene d1_campus with fade
my "How much do you know about this place?"
mc "I know the history of the campus, but not much else."
my "Cool. So, on this campus, we have four fraternities and one sorority; the rest of the students live in co-ed dorms."
scene d1_campus3 with dissolve
my "There's the nerd fraternity, the tri-betas..."
mc "The nerds?"
my "Yeah, I know it's kind of insensitive, but they're very smart."
scene d1_campus3b with dissolve
my "I think they take pride in being called nerds, too."
my "Anyway, they don't have a house. They just hang around the library most of the time."
my "Not having a house helps a lot with their expenses, too."
scene d1_campus4 with dissolve
my "Over there, you have the rich kids' club, \"the preps\", or whatever you want to call them."
my "They go by the acronym Alpha Nu Omega."
mc "Alpha and Omega...that's clever. Is it a biblical fraternity?"
my "Haha, no way. I think it means that they put themselves first and last, with no room for others."
scene d1_campus4b with dissolve:
    linear 10 zoom 1.02
my "That guy over there is Tybalt, their fraternity president."
my "Every year, his family donates a lot of money to B&R. It's always a big deal in the local newspapers."
$ bios_tybalt = True
$ bios_name_tybalt = True
$ chat_new_bios = True

scene d1_campus5 with dissolve
my "Then we have the jocks, the tri-alphas."
my "A bunch of meatheads in that house."
scene d1_campus5b with dissolve
my "Unless you're a jock..."
my "...you should probably stay away from them."
my "They get nasty."
mc "Noted."
scene d1_campus6 with dissolve
my "That house over there is the only sorority on campus."
my "The Eta Omicron Tau or HOT for short."
my "The jocks and the HOTs have a long history; they usually party together."
scene d1_campus6b2 with dissolve
mc "What are they like?"
scene d1_campus6b3 with dissolve
my "A bunch of sluts, if you ask me."
scene d1_campus6b4 with dissolve
my "Well, we all have our vices, and I'm still gonna pledge their house."
scene d1_campus6b with dissolve
mc "Huh? It sounds like you don't like them. Why would you want to pledge?"
scene d1_campus6c with dissolve
my "It's kind of unofficial, but rumor has it that they pay for your entire tuition if you fit their criteria."
scene d1_campus6d with dissolve

menu:
    "Really?" if True:
        mc "Wow, are you serious?"
        scene d1_campus6c with dissolve
        my "Yeah, I really need that money."
    "Tell a joke" if True:
        $ RPmaya += 1
        mc "Can I pledge, too?"
        scene d1_campus6d2 with dissolve
        my "Haha! I'd like to see you try!"
        scene d1_campus6c with dissolve
        my "I really need that money..."
my "My dad was going to pay for my tuition, but he gave me an ultimatum that I..."
scene d1_campus6e with dissolve
my "You know what...? We just met."
scene d1_campus6d with dissolve
mc "It's ok. I understand."
mc "It's common to take student loans, though."
scene d1_campus6g with dissolve
my "Yeah, I'm doing that, but it's not that simple... I need that money."
$ bios_history_maya += "Maya said she wants to pledge the HOTs. Apparently they offer to pay the tuition for their sorority sisters. She seems to have some sort of issues with her dad.\n\n"
$ bios_name_maya = True
$ chat_new_bios = True

scene d1_campus7 with dissolve
mc "You mentioned there being four fraternities...which is the fourth one?"
scene d1_campus6d2 with dissolve
my "Oh right! I almost forgot about them."
my "It's a new frat house, called the DIKs. It's right over there."
scene d1_campus9 with dissolve
mc "Delta Iota Kappa?"
my "Yeah, you got it."
my "They have only been around for a couple of years, and their name goes hand in hand with their personalities."
mc "That's a huge mansion, though!"
my "Yeah, I have no clue how they can afford that place. You'll have to ask them about it."
scene d1_campus6d2 with dissolve
my "So...that's about it."
my "Are you thinking of pledging a frat house?"
scene d1_campus7 with dissolve
mc "I'm not sure... I didn't really think about it before coming here."
scene d1_campus6g with dissolve
my "Yeah, I hear ya."
my "You can do like the rest and just stay in your shared dorm."
scene d1_campus7 with dissolve
mc "Yeah... I'd rather not."
mc "My dorm...guy...doesn't like me."
scene d1_campus6d2 with dissolve
my "Haha! Damn, [name]."
my "You've barely been here an hour and are already making enemies?"
scene d1_campus7 with dissolve
mc "Yeah..."

scene d1_campus16 with dissolve
my "Well, you can consider me a friend at least."
scene d1_campus17 with dissolve

menu:
    "Cool" if True:
        mc "Cool."
    "Compliment her" if True:
        $ bios_history_maya += "I complimented Maya, she liked it.\n\n"
        $ bios_name_maya = True
        $ chat_new_bios = True
        $ RPmaya += 1
        $ dk(-1)
        mc "I really appreciate that, Maya."
        mc "You seem like a fun person."
scene d1_campus18 with dissolve
my "Oh, look! I think I see the tour guide by the entrance! I think you should go tag along and meet some new people."
scene d1_campus7 with dissolve
mc "What about you?"
scene d1_campus16 with dissolve
my "I'll join you for the first class after lunch. I need to chat with the HOTs."

scene d1_campus17 with dissolve
menu:
    "Hug her ({color=#ffffff}{size=-1}{font=collegiate.ttf}CHICK{/font}{/size}{/color})" if dtype < 0:
        $ bios_history_maya += "I hugged Maya, she liked it.\n\n"
        $ bios_name_maya = True
        $ chat_new_bios = True
        $ RPmaya += 1
        scene d1_campus20b with dissolve
        mc "Thank you for the help."
        my "Aw! You're welcome!"
    "Bye" if True:
        mc "Bye, Maya."
scene d1_campus20 with dissolve
$ bios_maya = True
$ bios_name_maya = True
$ chat_new_bios = True
my "Later!"
scene d1_tour with wiperight
ca "Professors Castor Burgmeister and Sigmond Royce founded this college in 1921."
ca "Their vision was that everyone can become who they want to be."
scene d1_tourb with dissolve
ca "Much like the students before you and the students to come, you will learn to love it here at B&R!"
ca "So, see each day as a new opportunity and study hard to fulfill your dreams."
stop music fadeout 5
ca "Any questions?"
scene d1_tour1 with dissolve
ca "Yes, you again...the shirtless one..."
play music "music/ep1/energetic.mp3"
scene d1_tour5 with dissolve
de "When does this tour get interesting?"
scene d1_tour3 with dissolve
ca "Young man, you are free to leave if you don't wish to hear about the campus history."
scene d1_tour5 with dissolve
de "It just seems so weird that you would spend all this time talking about some dead dudes..."
de "...when you could tell us where to buy liquor and where the best parties are at."
scene d1_tour3 with dissolve
ca "Alcohol is strictly forbidden on campus grounds!"
scene d1_tour5 with dissolve
de "Define campus grounds."
scene d1_tour5b with dissolve
ca "This is campus grounds. Where you live and study."
scene d1_tour5c with dissolve
de "You really should put that in the brochure."
de "I feel cheated."
scene d1_tour6 with dissolve
de "Don't you feel cheated?"
scene d1_tour3 with dissolve
ca "If we find you in possession of alcohol or narcotics on campus grounds, there will be repercussions."
de "Narcotics, too!?"
stop music fadeout 3
scene d1_tour7b with dissolve
$ bios_derek = True
$ bios_cathy = True
$ bios_name_derek = True
$ bios_name_cathy = True
$ chat_new_bios = True
ca "And we're walking!"

play music "music/ep1/art_nouveau.mp3"
scene d1_tour8 with wipeleft
ca "In this building you'll find each lecture hall and classroom; there are maps on the walls if you ever get lost."
mc "(The maps suck...)"
ca "And this college is filled with helpful students."
play sound "sound_effects/hit.mp3"
scene d1_tour9 with hpunch
$ renpy.pause()
scene d1_tour9b with dissolve
dw "Eat shit, Cathy!"
scene d1_tour10 with dissolve
sec "Stop right there!"
scene d1_tour11 with dissolve
ca "Ah, yes. Our campus security is always vigilant and close by to help you if you need it."
scene d1_tour12 with wiperight
$ renpy.sound.set_volume(0.7,channel='sfx1')
$ renpy.sound.play("sound_effects/cafeteria.mp3", channel="sfx1", loop=True)
ca "Here is the campus cafeteria."
ca "Most students come here to buy their lunch or afternoon snack."
scene d1_tour13 with dissolve
ca "And that is the end of our tour."
ca "Just in time for lunch."
ca "I suggest that you eat your lunch here and then we'll meet up in classroom 5K, at 1 p.m."
$ guideSuggestedPage = 33
scene d1_lunch with dissolve
mc "(Students already seem to be bonding.)"
mc "(I hate this...)"
mc "(I'm not good at initiating chats with new people...)"
mc "(Maybe I'll sit down over there.)"
scene d1_lunch1b with dissolve
mc "(This food looks disgusting...)"
mc "(It's like someone put minimal effort into making it...)"
scene d1_lunch2 with dissolve
$ renpy.pause()
scene d1_lunch2b with dissolve

menu:
    "Introduce yourself" if True:
        $ introducedSage = True
        $ dk(-1)
        mc "Hi! I'm [name]."
    "Say nothing" if True:
        $ introducedSage = False
        mc "..."

stop music fadeout 3
scene d1_lunch3 with dissolve
sa "..."
$ renpy.sound.stop(channel="sfx1", fadeout=None)
play music "music/ep1/food_chain_short.mp3"
scene d1_lunch4 with vpunch
ch "What the fuck, Sage!"
ch "I wasn't done talking to you!"
mc "(Whoa, that's a huge dude.)"
scene d1_lunch5 with dissolve
sa "For the last time, Chad..."
sa "FUCK OFF!!!"
menu:
    "Intervene" if True:
        $ intervenedChad = True
        $ RPjocks -= 1
        $ RPsage += 1
        scene d1_lunch7 with dissolve
        if dtype > 0:
            mc "Hey, juicehead! Let go of her."
        elif True:
            mc "Hey, let go of her! You're hurting her."
        scene d1_lunch8 with dissolve
        ch "This doesn't concern you."
        menu:
            "Shove him ({color=#ffffff}{size=-1}{font=collegiate.ttf}DIK{/font}{/size}{/color})" if dtype > 0:
                $ dk(1)
                $ bios_history_chad = "I shoved Chad to defend Sage.\n\n"
                $ bios_name_chad = True
                $ chat_new_bios = True
                play sound "sound_effects/shove.mp3"
                scene d1_lunch9c with vpunch
                $ renpy.pause()
                jc "FRESHY FIGHT!"
                scene d1_lunch10d with dissolve
                ch "WHAT THE FUCK!?"
            "Call security" if True:
                $ dk(-1)
                $ bios_history_chad = "I called campus security on Chad to defend Sage.\n\n"
                $ bios_name_chad = True
                $ chat_new_bios = True
                mc "Hey, security!"
        scene d1_lunch9b with dissolve
        sec "What is going on here?"
        if dtype>0:
            mc "Ask this asshole that question?"
        elif True:
            mc "Ask this guy that question?"
        scene d1_lunch10 with dissolve
        ch "Pff..."
    "Keep quiet" if True:
        $ bios_history_chad = "I didn't intervene when Chad argued with Sage.\n\n"
        $ bios_name_chad = True
        $ chat_new_bios = True
        $ intervenedChad = False
        mc "..."
        scene d1_lunch9 with dissolve
        sec "What is going on here?"
        scene d1_lunch10b with dissolve
        ch "Pff..."
stop music fadeout 3
scene d1_lunch11 with dissolve
sa "..."
$ renpy.sound.set_volume(0.7,channel='sfx1')
$ renpy.sound.play("sound_effects/cafeteria.mp3", channel="sfx1", loop=True)
play music "music/ep1/funk_rock.mp3"

if intervenedChad:
    scene d1_lunch11b with dissolve
    if introducedSage:
        sa "Thanks, [name]."
    elif True:
        sa "Thanks..."
elif True:
    mc "Are you ok?"
    scene d1_lunch11c with dissolve
    sa "Found your voice?"
    scene d1_lunch11b with dissolve
    sa "...I'm fine."
scene d1_lunch11 with dissolve
mc "Sage, huh?"

menu:
    "Joke about her name" if True:
        $ dk(1)
        mc "As in the herb or the color?"
        scene d1_lunch11d with dissolve
        sa "Ugh..."
        scene d1_lunch11 with dissolve
        mc "Just trying to cheer you up..."
    "Pretty name" if True:
        $ dk(-1)
        mc "That's a pretty name."

if not introducedSage:
    mc "I'm [name]."
mc "What was that about?"
scene d1_lunch14 with dissolve
sa "Just a stupid argument with my even stupider boyfriend."
scene d1_lunch14b with dissolve
sa "He thinks he's so fucking smart that he can hide that he's cheating on me!"
scene d1_lunch15 with dissolve
sa "I fucking found the panties in his gym bag!"
sa "And he told me that he bought them for me."
sa "Can you believe that?"
scene d1_lunch11 with dissolve
menu:
    "Maybe he did?" if True:
        mc "Maybe he's telling the truth?"
        scene d1_lunch11c with dissolve
        sa "New panties don't reek of perfume."
        mc "Oh..."
    "That's bullshit" if True:
        $ dk(-1)
        mc "It does sound like a bullshit story."
scene d1_lunch11d with dissolve
sa "He's so full of shit."
scene d1_lunch11 with dissolve
$ bios_history_sage = "I met Sage today. She seems to have relationship issues with her jock boyfriend Chad.\n\n"
$ bios_name_sage = True
$ chat_new_bios = True

menu:
    "Tell a joke" if True:
        if dtype > 0:
            mc "And steroids. Evidently, they shrink both dick and brains."
            scene d1_lunch17b with dissolve
            sa "Haha..."
            $ RPsage += 1
            $ bios_history_sage += "I told her a joke and she laughed.\n\n"
            $ bios_name_sage = True
            $ chat_new_bios = True
        elif True:
            mc "Full of shit? Well, he does smell worse than the lunch at this place."
            scene d1_lunch17c
            ll "RUDE!!!"
            $ ep1_insulted_cafeteria_worker = True
            $ bios_history_sage += "I told her a joke but ended up insulting the cafeteria workers.\n\n"
            $ bios_history_beth += "I told Sage a joke but ended up insulting Beth.\n\n"
            $ bios_name_sage = True
            $ chat_new_bios = True
    "Don't push it" if True:
        $ renpy.pause(0.2)
$ guideSuggestedPage = 34
scene d1_lunch11 with dissolve
menu:
    "Why do you date him?" if True:
        mc "Then why do you date him?"
        scene d1_lunch19 with dissolve
        sa "Mind your own fucking business."
        if dtype > 0:
            scene d1_lunch19b with dissolve
            mc "Drop that fucking attitude; I was only caring."
            scene d1_lunch11 with dissolve
            sa "..."
            scene d1_lunch19d with dissolve
            sa "Sorry."
            scene d1_lunch11 with dissolve
            $ RPsage += 1
            $ bios_history_sage += "I was dominant with her when she got offended. She liked that.\n\n"
            $ bios_name_sage = True
            $ chat_new_bios = True
        elif True:
            $ RPsage -= 1
            $ bios_history_sage += "She got offended when I asked her about Chad.\n\n"
            $ bios_name_sage = True
            $ chat_new_bios = True
            scene d1_lunch11 with dissolve
    "Don't inquire" if True:
        scene d1_lunch11 with dissolve
sa "..."
scene d1_lunch19d with dissolve
sa "I haven't seen you around before. So, what are you? A freshman?"
scene d1_lunch11 with dissolve
mc "What gave it away?"
scene d1_lunch19d with dissolve
sa "You sit here and eat all alone, but you don't look like someone who would."
scene d1_lunch11 with dissolve
menu:
    "That's superficial" if True:
        $ RPsage -= 1
        $ bios_history_sage += "She got offended when I called her superficial.\n\n"
        $ bios_name_sage = True
        $ chat_new_bios = True
        mc "That's very superficial."
        scene d1_lunch11d with dissolve
        sa "Whatever."
        scene d1_lunch23 with dissolve
    "No friends yet" if True:
        mc "Yeah, I haven't made any friends yet."
        scene d1_lunch23 with dissolve
        sa "Well, that sucks."
sa "Which frat are you pledging?"
scene d1_lunch23b with dissolve
mc "Oh...I don't know if I will pledge."
scene d1_lunch23c with dissolve
sa "Come on, you gotta pledge!"
sa "You're going to miss out on a lot of parties otherwise."
scene d1_lunch23b with dissolve
mc "Well, I came here to study."
scene d1_lunch11d with dissolve
sa "Ugh. Then you should pledge the tri-betas; that's all they do."
scene d1_lunch11 with dissolve
mc "(Hm...it could be worth checking them out at least.)"
mc "Since you seem to like parties..."
mc "I'm guessing you're in the Eta Omicron Tau sorority."
scene d1_lunch31 with dissolve
sa "In it? I'm the sorority president."
sa "You do know that we just call it HOT, right?"
scene d1_lunch11 with dissolve
mc "Ok..."
scene d1_lunch33 with dissolve
$ bios_chad = True
$ bios_sage = True
$ bios_name_sage = True
$ bios_name_chad = True
$ chat_new_bios = True

if intervenedChad:
    sa "I gotta run. Thanks for the help back there."
elif True:
    sa "I gotta run. Bye."

menu:
    "Check her out" if True:
        $ dk(1)
        stop music fadeout 3
        scene d1_lunch33b with dissolve
        if dtype > 0:
            mc "(Nice ass...)"
        elif True:
            mc "(She's very pretty.)"
    "Don't push your luck" if True:
        $ dk(-1)
        stop music fadeout 3

scene d1_derek1 with dissolve
de "Holy fuck!"
play music "music/ep1/energetic.mp3"
scene d1_derek2 with dissolve
de "Hey, bro! Did you see the tits on that one?"
scene d1_derek2b with dissolve

$ bios_history_derek = "Derek seems to be a party guy. Dude seems to have lost his shirt somewhere.\n\n"
$ bios_name_derek = True
$ chat_new_bios = True
menu:
    "Banter" if True:
        $ dk(1)
        $ assman = True
        mc "Tits? I was looking at her ass."
        scene d1_derek4 with dissolve
        de "Aha! An ass man."
        de "I would never have guessed."
        $ bios_history_derek += "Derek started calling me ass man, today... I don't know if I like that nickname.\n\n"
        $ bios_name_derek = True
        $ chat_new_bios = True
    "Defend her" if True:
        $ dk(-1)
        $ assman = False
        mc "That's pretty rude, dude."
        scene d1_derek4b with dissolve
        de "Thanks!"
scene d1_derek2b with dissolve
mc "..."
mc "Where's your shirt?"
scene d1_derek6 with dissolve
de "I know! Right?"
de "I probably lost it."
scene d1_derek2 with dissolve
if intervenedChad:
    de "You almost gave it to that jock, huh?"
elif True:
    de "Man, I gotta say I wished for you to stand up to that Belgian Blue lookin' motherfucker."
scene d1_derek2b with dissolve
if intervenedChad:
    mc "Yeah...almost."
    scene d1_derek2 with dissolve
    de "He would have crushed you, though."
    scene d1_derek2b with dissolve
elif True:
    mc "Did you see the size of him?"
mc "I know how to fight, but I really don't want to make enemies."
scene d1_derek7 with dissolve
de "Come on, don't say that! Beating up a jock would grant you instant access to join the DIKs!"
scene d1_derek8 with dissolve
mc "Yeah, I don't think I want to join the DIKs."
scene d1_derek9 with dissolve
de "Dude, are you crazy!? I just talked to some students..."
de "The DIKs is where it's at, bro! They throw the best parties, and lately, they've been partying a lot with the HOTs."
scene d1_derek8 with dissolve
mc "Really? I thought the HOTs were tri-alpha's sorority."
scene d1_derek9 with dissolve
de "And that's why you would have gotten that golden ticket to the DIKs by beating that jock up."
scene d1_derek8 with dissolve
mc "Well, if you wanna be in that fraternity so much, why don't you beat up a jock?"
scene d1_derek7 with dissolve
de "Dude...look at me. I'm not a fighter."
de "I'm a lover and a gentleman."
scene d1_derek13 with dissolve
de "Holy fuck! Would you look at the milk machines on that one!"
scene d1_derek_jade1 with dissolve
$ renpy.pause()
scene d1_derek_jade with dissolve
de "What do you say, bro!?"
menu:
    "Just my type" if True:
        $ bios_history_derek += "I told him that I like busty women.\n\n"
        $ bios_name_derek = True
        $ chat_new_bios = True
        $ preferredmilf = 0
        scene d1_derek_jade2 with dissolve
        if dtype > 0:
            mc "Yeah, that's just how I like them."
            de "{i}Them{/i} as in titties or women?"
            mc "Why not both?"
            if assman:
                de "Haha! So, you're not just an ass man, then?"
            elif True:
                de "Haha!"
        elif True:
            mc "She sure is beautiful."
    "I prefer Cathy" if True:
        $ bios_history_derek += "I told him that I prefer women like Cathy.\n\n"
        $ bios_name_derek = True
        $ chat_new_bios = True
        scene d1_derek_cathy with dissolve
        $ preferredmilf = 1
        if dtype > 0:
            mc "Nah, milfs like Cathy are much more my style."
            if assman:
                de "An ass man and a dyke lover, huh?"
                mc "Haha, fuck you!"
        elif True:
            mc "For older women, I'd prefer someone like Cathy."
            de "Flat and boring, huh? Got it."
scene d1_derek10 with dissolve
de "Anyway, so you're not planning on pledging the DIKs?"
de "Think about it! Their parties are next level!"
scene d1_derek8 with dissolve
mc "Well, as I said to Sage just now, I came here to study, not to party."
scene d1_derek10b with dissolve
de "Oh yeah. Sure, sure. Me too."
scene d1_derek8 with dissolve
mc "Really?"
scene d1_derek10b with dissolve
de "No."
de "I'm just here for the pussy."
scene d1_derek8 with dissolve
mc "At least you're honest."
scene d1_derek14 with dissolve
$ number_derek = True
de "Here take my number."
de "Hit me up if you change your mind!"
$ renpy.sound.stop(channel="sfx1", fadeout=3)
stop music fadeout 3
if assman:
    de "See ya later, ass man!"
elif True:
    de "See ya later, dude!"
$ bios_history_derek += "Derek wants me to pledge the DIKs with him.\n\n"
$ bios_name_derek = True
$ chat_new_bios = True

play music "music/ep1/someways.mp3"
scene d1_class with wipeleft
de "So, you're going to do it or what?"
scene d1_class_b with dissolve
my "In your dreams!"
$ renpy.sound.set_volume(1.0,channel='sfx1')
scene d1_class_c with dissolve
de "Aw, come on! Why not?"
scene d1_class_b with dissolve
my "Just because I'm pledging, I'm not going to hook you up with HOT chicks."
scene d1_class_c with dissolve
de "Not cool. Not cool at all."
scene d1_class_e with dissolve
de "Hey, bro. Don't try your luck with that one. Total cockblock."
menu:
    "Get mad" if True:
        $ bios_history_derek += "I called Derek out when he called Maya a cockblock.\n\n"
        $ bios_name_derek = True
        $ chat_new_bios = True
        $ RPderek -= 1
        scene d1_class_g with dissolve
        mc "Don't fucking talk about her like that!"
        de "Bro...relax. It's cool."
        scene d1_class_i with dissolve
    "Ignore him" if True:
        scene d1_class_i with dissolve
$ guideSuggestedPage = 35
menu:
    "Check her out" if True:
        $ dk(1)
        $ RPmaya -= 1
        scene d1_class_j2 with dissolve
        $ renpy.pause()
        scene d1_class_j3 with dissolve
        $ bios_history_maya += "Maya caught me staring at her panties... I'm sure she didn't appreciate that.\n\n"
        $ chat_new_bios = True
        my "Hey, [name]..."
        scene d1_class_j4 with dissolve
        mc "Hey!"
    "Say hi" if True:
        $ dk(-1)
        mc "Hey, Maya. Thanks again for the tour."
        scene d1_class_j with dissolve
        my "No sweat."
        scene d1_class_l with dissolve

mc "What have you been up to?"
scene d1_class_j with dissolve
my "I went to the HOTs and chatted with Quinn about pledging."
my "She wasn't totally against it."
my "So, now I'll have to wait for her to call on me."
scene d1_class_l with dissolve
mc "Who's Quinn?"
scene d1_class_j with dissolve
my "The vice president of HOT. A total hardass."
scene d1_class_l with dissolve
mc "I see you've met Derek..."
scene d1_class_n with dissolve
my "Haha, met him? No, we-"
ca "Simmer down, students. It's time to start."
$ bios_history_derek += "Maya and Derek seem to have a history.\n\n"
$ bios_history_maya += "Maya and Derek seem to have a history.\n\n"
$ bios_name_derek = True
$ bios_name_maya = True
$ chat_new_bios = True
scene d1_class_j with dissolve
my "Let's chat later, ok?"
scene d1_class_p with dissolve
ca "Welcome to your first class."
ca "During your freshman year, there are a lot of courses that we recommend you take."
ca "Most courses are general education courses and, well...our selection is...limited."
$ englishPresented = True
show screen skillmsg
ca "For the English credits, most students sign up for this class, named \"Writing and Communication\"..."
ca "...and for the mathematics credits, \"Gen. Ed. Mathematics\" is the most common choice."
ca "In both of which, I'm the teacher."
hide screen skillmsg
scene d1_class1bb with dissolve
ca "If you haven't signed up for all classes yet, I'd recommend you all to do it this week."
ca "But today, we're here to start mastering the English language in writing and communication."
scene d1_class2 with dissolve
ca "As a standard, I start each freshman year with a couple of tests."
de "BOOH!!!"
scene d1_class1bb with dissolve
ca "Now, now. Don't be scared."
ca "These tests will not count toward your final grades."
ca "They're just tests that will show me what level you all are on."
scene d1_class2 with dissolve
ca "You may begin."
$ bios_history_cathy = "Cathy is going to be my English and Math teacher.\n\n"
$ bios_name_cathy = True
$ chat_new_bios = True


if not minigames:
    scene black with Fade(1.5, 1, 0.5)
    jump ep1_after_english_test
if tutorials:
    scene english_tutorial1 with wipeleft
    $ renpy.pause()
    scene english_tutorial2 with dissolve
    $ renpy.pause()
    scene english_tutorial3 with dissolve
    $ renpy.pause()
elif True:
    stop music fadeout 3
    $ renpy.pause(3)
play music "music/ep3/sing_along_with_jim.mp3"
scene english_test_board
jump english101_test1
label ep1_after_english_test:
$ renpy.block_rollback()
if minigames:
    scene d1_class2 with wiperight
    stop music fadeout 3
elif True:
    scene d1_class2 with fade
ca "Pencils down, class."
ca "Please turn in your tests."
scene d1_class1bb with dissolve
if minigames:
    play music "music/ep1/someways.mp3"
ca "We're done for today."
ca "Please spend the remainder of the day getting acquainted with each other."
ca "For those of you who are taking Gen. Ed. Mathematics, we'll meet here again tomorrow morning."
ca "Class dismissed."
scene d1_class8 with dissolve
mc "Hey, Maya. How did it go?"
my "I think it went all right."
my "So, what are you up to?"
scene d1_class9 with dissolve
mc "I'm going to check out the tri-beta fraternity."
mc "Wanna come with me?"
scene d1_class10 with dissolve
my "Sorry, I can't. I need to call my boyfriend."
menu:
    "Ask about boyfriend" if True:
        mc "Oh, you have a boyfriend?"
        scene d1_class13 with dissolve
        my "Yes. I gotta go."
    "Leave it alone" if True:
        mc "Ok, have fun."
mc "(That was weird...)"
$ bios_history_maya += "Maya told me she has a boyfriend. Everyone seems to be spoken for around here...\n\n"
$ bios_name_maya = True
$ chat_new_bios = True
stop music fadeout 3
scene d1_tribeta with fade
mc "(If I recall correctly, the library is this way...)"
scene d1_tribetab with dissolve
dw "Hey, Chad, there he is!"
an "So, what are you going to do?"
if intervenedChad:
    play music "music/ep1/credits.mp3"
    play sound "sound_effects/hit.mp3"
    scene d1_tribetac with hpunch
    jcs "Hahaha!"
    scene d1_tribetad with dissolve
    mc "Hey, what the hell!?"
    ch "You got a problem there, tattletale?"
    an "Hehe. Yeah!"
    scene d1_tribeta3 with dissolve
    ch "Shut up, Anthony!"
    scene d1_tribeta3b with dissolve
    menu:
        "Mock him" if True:
            $ dk(1)
            $ RPjocks -= 1
            mc "Tattletale? What are you? In kindergarten?"
            scene d1_tribeta4 with dissolve
            an "No, in college!"
            ch "..."
            scene d1_tribeta7 with dissolve
            ch "It seems to me like you're trying to make a move on my girl."
        "Calm him down" if True:
            $ dk(-1)
            mc "Relax, I have no beef with you."
            scene d1_tribeta7 with dissolve
            ch "Really? No beef, he says!"
            ch "Because it seems to me like you're trying to make a move on my girl."
    $ guideSuggestedPage = 36
    scene d1_tribeta3b with dissolve
    mc "Who? Sage? You've got it all wrong."
    scene d1_tribeta7 with dissolve
    ch "You do know that campus security can't always be around to save your pretty little ass?"
    scene d1_tribeta3b with dissolve
    menu:
        "Mock him" if True:
            $ dk(1)
            $ RPjocks -= 1
            mc "Do you think I have a pretty little ass? How gay are you?"
            scene d1_tribeta11 with dissolve
            an "Hehe. That sounded pretty gay to me."
            play sound "sound_effects/hit.mp3"
            scene d1_tribeta12 with hpunch
            mc "(Holy shit!)"
            scene d1_tribeta13 with dissolve
        "Calm him down" if True:
            $ dk(-1)
            mc "Come on; I'm not looking for a fight."
            scene d1_tribeta7 with dissolve
elif True:
    play music "music/ep1/credits.mp3"
    play sound "sound_effects/hit.mp3"
    scene d1_tribetac with hpunch
    jcs "Hahaha!"
    scene d1_tribetad with dissolve
    mc "Hey, what the hell!?"
    ch "You got a problem there, Prince Charming?"
    an "Hehe. Yeah! We got a fucking Romeo or something over here."
    scene d1_tribeta3 with dissolve
    ch "Shut up, Anthony!"
    scene d1_tribeta3b with dissolve
    menu:
        "Mock him" if True:
            $ dk(1)
            $ RPjocks -= 1
            mc "Did I charm your panties off?"
            scene d1_tribeta4 with dissolve
            an "Chad doesn't wear panties."
            ch "..."
            scene d1_tribeta7 with dissolve
            ch "It seems to me like you're trying to make a move on my girl."
        "Calm him down" if True:
            $ dk(-1)
            mc "Relax, I have no beef with you."
            scene d1_tribeta7 with dissolve
            ch "Really? No beef, he says!"
            ch "Because it seems to me like you're trying to make a move on my girl."
    scene d1_tribeta3b with dissolve
    mc "Who? Sage? You've got it all wrong."
    $ guideSuggestedPage = 36
    scene d1_tribeta7 with dissolve
    ch "That's not what Dawe told me. Apparently, you were getting ready to fuck her right there in the cafeteria."
    scene d1_tribeta3b with dissolve
    menu:
        "Mock him" if True:
            $ dk(1)
            $ RPjocks -= 1
            mc "Funny how that is. I could've sworn that it was you trying to fuck her up."
            scene d1_tribeta11 with dissolve
            an "Hehe. That's kind of funny."
            play sound "sound_effects/hit.mp3"
            scene d1_tribeta12 with hpunch
            mc "(Holy shit!)"
            scene d1_tribeta13 with dissolve
        "Calm him down" if True:
            $ dk(-1)
            mc "Come on; I'm not looking for a fight."
            scene d1_tribeta7 with dissolve
ch "I'll be watching you, freshy."
scene d1_tribeta_sage with dissolve
ch "Stay the fuck away from Sage!"
scene d1_tribeta14 with dissolve
ch "Dawe, here, will show you what happens when you mess with the tri-alphas."
mc "Huh?"
play sound "sound_effects/wedgie.mp3"
scene d1_tribeta15 with vpunch
dw "Take this, bitch!"
dw "Hehehe!"
$ bios_anthony = True
$ bios_dawe = True
$ bios_name_anthony = True
$ bios_name_dawe = True
if RPjocks < 0:
    $ bios_history_chad += "I got into an argument with the jocks over Sage. I didn't get off to a good start with them.\n\n"
elif True:
    $ bios_history_chad += "I got into an argument with the jocks over Sage. I managed to keep my cool.\n\n"
$ bios_history_dawe = "Dawe's an ass. He gave me a wedgie today. I'll remember this.\n\n"
$ bios_history_anthony = "It's a wonder that this guy got accepted to college, he seems to be a new kind of stupid.\n\n"
$ bios_name_chad = True
$ chat_new_bios = True

scene d1_tribeta16 with dissolve
stop music fadeout 5
mc "(Fucking jocks!)"

uk "Hey! Stop that! You bullies!"
play music "music/ep1/they_say.mp3"
scene d1_tribeta17 with dissolve

uk "Are you hurt?"
mc "No, I'm-"
scene d1_tribeta19
ty "Jill, we're going to be late."

ji "Give me a second, Tybalt."
scene d1_tribeta21 with dissolve
mc "I'm ok. Thanks."
mc "This is not the first time in my life I got a wedgie. Haha."
mc "But it's the first time in my adult life."
scene d1_tribeta18 with dissolve

ji "Argh! I can't stand bullies. Some boys never grow up."
scene d1_tribeta22 with dissolve
menu:
    "Compliment her" if True:
        if dtype < 1:
            $ RPjill += 1
            mc "So, Jill... That's a pretty name."
            scene d1_tribeta23 with dissolve

            ji "Thanks. And you are...?"
            scene d1_tribeta22 with dissolve
            mc "[name]."
        elif True:
            $ RPjill -= 1
            mc "Jill, huh. I'm [name]."
            mc "You're pretty hot."
            scene d1_tribeta23b with dissolve

            ji "Erm...ok."
    "Introduce yourself" if True:
        mc "I'll be fine, Jill. I'm [name], by the way."
scene d1_tribeta22b with dissolve

ji "I think you got some dirt on your clothes."
scene d1_tribeta22 with dissolve
mc "Ah... Well, nothing that some good old saliva won't get rid of."
scene d1_tribeta22d with dissolve

ji "Haha! Euw!"
scene d1_tribeta21b with dissolve

ji "I'm glad you're not hurt."
scene d1_tribeta24 with dissolve
ty "Jill, what's the hold-up?"
scene d1_tribeta24b with dissolve

ji "Oh! This is Tybalt. Tybalt, this is-"
scene d1_tribeta24c with dissolve
ty "We're going to be late for our economics lecture, and I want to exchange some words with you before that."
scene d1_tribeta24d with dissolve

ji "Sorry, [name]. I have to go."
scene d1_tribeta24e with dissolve
mc "That's ok. I need to go dislodge something from my ass anyway."
mc "(Why did I say that...?)"
scene d1_tribeta24f with dissolve

ji "Hahaha!"
scene d1_tribeta24g with dissolve

ji "Stay safe, [name]."
scene d1_tribeta24h with dissolve
stop music fadeout 3
mc "(What a beauty...)"
play music "music/ep1/your_smile.mp3"
$ bios_name_jill = True
$ bios_name_tybalt = True
$ bios_jill = True
$ bios_history_jill = "I met Jill today. She was upset to see the jocks bully me.\n\n"
$ bios_history_tybalt = "Tybalt totally ignored me when I was talking to Jill. Was it because of me or Jill?\n\n"
$ chat_new_bios = True

scene d1_tribeta25 with dissolve
mg "Oh, the wedgie. If ass cracks could get callouses, mine would be hard as marble by now."
mg "I feel for you. I really do."
mc "I'll be fine..."
scene d1_tribeta25b with dissolve
mc "Hey, you... You wouldn't happen to know someone who can tell me more about the tri-betas."
scene d1_tribeta25c with dissolve
mg "Why would I know about that? Because of my glasses?"
mc "..."
scene d1_tribeta25c2 with dissolve
mg "Just pulling your leg."
mg "You're in luck. I'm the current tri-beta president."
mg "The name's Magnar."
scene d1_tribeta25c3 with dissolve
mc "[name]."
scene d1_tribeta25c2 with dissolve
mg "Are you thinking of pledging our friendly fraternity?"
scene d1_tribeta25c3 with dissolve
mc "I don't know, to be honest."
mc "I wasn't really going to pledge any fraternity, but I didn't want to say no before checking them out."
scene d1_tribeta25c2 with dissolve
stop music fadeout 3
mg "Mhm. Follow me."
scene d1_tribeta25d with wiperight
$ renpy.sound.play("sound_effects/library_ambience.mp3", channel="sfx1", loop=True)
mg "This is the campus library. Where we tri-betas usually spend our free time."
mg "It's pretty small, but within these walls, you'll find a vast amount of knowledge."
scene d1_tribeta26 with dissolve
mg "Please, be seated."
scene d1_tribeta27 with dissolve
mg "To join our fraternity, you must love to study, but it must also show on your grades."
mg "Tell me, how did you do in high school?"
scene d1_tribeta27b with dissolve
mc "I did ok. Look, I'm not the smartest guy, but I got into college here."
scene d1_tribeta27 with dissolve
mg "Yeah, sorry. That's not enough to qualify you."
mg "I don't want to insinuate that you're stupid, but we do have a reputation to keep."
scene d1_tribeta30 with dissolve
mg "But it doesn't mean that you're not allowed to come here and study with us."
mg "We'll gladly provide our services...for a price."
mc "A price?"
scene d1_tribeta31b with dissolve
mg "Sally, would you mind giving us a moment?"
scene d1_tribeta31c with dissolve
$ renpy.pause()
scene d1_tribeta30b with dissolve
mg "Even if you're a snooty prep, college is expensive for all fraternities and sororities..."
mg "All I'm saying is that we can share a few study techniques and notes with you if you pay us."
mg "That will make classes a lot easier for you."
if not minigames:
    scene d1_tribeta30b2 with dissolve
    mc "Thanks, but I'm not interested."
    jump d1_mg_afterloop
if tutorials:
    scene d1_tribeta30b2 with dissolve
    show white_screen with dissolve
    show text "{color=#ffffff}Magnar sells items that make the mini-games easier to pass. The items are permanent bonuses. You can buy boosters that lower the requirement to pass a test and get lewd renders by 5% per level.{/color}" zorder 2 with dissolve:
        ypos 0.825
    $ renpy.pause()
    hide text
scene d1_tribeta30b2 with dissolve
mc "I'm actually in need of money, too."
scene d1_tribeta30b with dissolve
mg "Hm..."
mg "I guess that we could use someone to take notes for us during class."
mg "I'll tell you what. If you pay me {color=#36ca2b}$$${/color}, I'll let you earn money from passing classes."
scene d1_tribeta30b2 with dissolve
$ afterMagnarShopLabel = "d1_mg_afterloop"
$ talkMagnarShopLabel = "d1_mg_talk"
$ listenMagnarShopLabel = "d1_mg_listen"
show screen moneymsg
show screen magnar_shop_screen
label d1_mg_loop:
$ renpy.pause()
jump d1_mg_loop
label d1_mg_talk:
scene d1_tribeta30b with dissolve
mg "Thank you!{w=2}{nw}"
jump d1_mg_listen
label d1_mg_listen:
scene d1_tribeta30b2 with dissolve
jump d1_mg_loop
label d1_mg_afterloop:
scene d1_tribeta30b with dissolve
if minigames:
    mg "Here, take my number."
    mg "Call me if you want to buy something in the future, pal."
elif True:
    mg "All right..."
    mg "Here, take my number."
    mg "Just in case you would change your mind."
$ number_magnar = True

scene d1_tribeta33 with dissolve
stop music fadeout 10
mg "Well, this was fun, [name]. I hope I'll be seeing you around."
mg "I need to make haste. We are playing Dungeons and Gremlins this evening."
$ bios_magnar = True
$ bios_history_magnar = "Magnar's a nice guy, maybe a tad arrogant. It's weird that people around here like to flaunt that they are smart. Where I come from, that got you beat up.\n\n"
$ bios_history_magnar += "Magnar offered to sell me tests and to teach me study techniques. I can call him to buy his services.\n\n"
$ bios_name_magnar = True
$ bios_sally = True
$ bios_name_sally = True
$ chat_new_bios = True
$ renpy.music.stop(channel="sfx1", fadeout=3)
mg "Come, I'll walk you out."

scene d1_tribeta34 with dissolve
play music "music/ep1/apra_hyde.mp3"
mc "Who is that?"
mg "Ah! I see that you've spotted {i}the Ice Queen{/i}."
mg "She's our librarian."
scene d1_tribeta44 with dissolve
mc "The Ice Queen?"
mg "Oh. You're not familiar with role-playing games, are you?"
mg "Well, think of her as the protector of knowledge."
mg "For keeping our books and territory safe, I applaud her..."
scene d1_tribeta45 with dissolve
mg "...but I applaud her in silence."
mg "She has no tolerance for shenanigans, and if you don't keep quiet, she will scold you."
scene d1_tribeta46 with dissolve
mg "Good afternoon, Isabella."
isa "..."
scene d1_tribeta47 with dissolve
mc "I should probably get a library card to check out books, right?"
scene d1_tribeta47b with dissolve
mg "Yeah..."
mg "Very smart idea. Go ahead."
scene d1_tribeta49 with dissolve
mg "*{i}Snickers{/i}*"
mc "(Pff... The Ice Queen? That's pretty mean.)"
scene d1_isa1 with dissolve
mc "Hi!"
menu:
    "Tell a joke" if True:
        if dtype < 1:
            mc "What did the librarian say to the student?"
            scene d1_isa2 with dissolve

            isa "Shhh!"
            scene d1_isa1 with dissolve
            mc "Oh, so you've heard that one already?"
            isa "..."
            mc "Sorry..."
            mc "I'm really here to apply for a library card."
        elif True:
            $ RPisabella -= 1
            mc "Hey Isabella! Are you a book? Because I would like to check you out."
            scene d1_isa3 with dissolve
            $ renpy.pause()
            jump d1_thrown_out
    "Ask about library card" if True:
        mc "I would like to apply for a library card."
mc "..."
mc "Can you help me with that?"
scene d1_isa4 with dissolve

isa "No."
scene d1_isa4b with dissolve
mc "..."
mc "Ok..."
mc "How does this work, then? I'm guessing I need a library card to check out books, right?"
scene d1_isa4c with dissolve

isa "You use your student ID."
scene d1_isa4b with dissolve
mc "Oh, I haven't got one of those yet."
mc "I think I'll get mine later this week."
mc "..."
mc "So...erm...I..."
stop music fadeout 3
mc "Nice chatting with you."
jump d1_not_thrown_out

label d1_thrown_out:
stop music
play sound "sound_effects/shove.mp3"
scene d1_after_library with hpunch
$ renpy.pause()
scene d1_after_library1 with dissolve
mc "That wasn't really what I thought would happen."

label d1_not_thrown_out:
$ guideSuggestedPage = 37
jump ep1_freeroam_dorm_label

label ep1_college_day2_label:
$ current_task = "None"
$ chat_new_tasks = False
$ bios_history_troy += "Troy left the dorm in the middle of the night. He's up to something.\n\n"
$ bios_name_troy = True
$ chat_new_bios = True
if preferredmilf == 0:
    label ep1_jade_lewd:
    if _in_replay:
        hide screen phone_screen
        if persistent.name == None:
            $ name = "MC"
        elif True:
            $ name = persistent.name
        if persistent.mc_jade == None:
            $ mc_jade = name
        elif True:
            $ mc_jade = persistent.mc_jade
        if persistent.jade == None:
            $ jade = "Jade"
        elif True:
            $ jade = persistent.jade
    play music "music/ep1/slow_day_blues.mp3"
    scene ep1_jade_dream2 with Fade(1.5, 1, 0.5)
    ja "Hey, [mc_jade]..."
    scene ep1_jade_dream3 with dissolve
    mc "OH MY GOD! Who are you!?"
    scene ep1_jade_dream2 with dissolve
    ja "Come on; you overheard my name in the cafeteria...I'm Jade."
    scene ep1_jade_dream with dissolve
    mc "Oh, yeah...but what are you doing?"
    scene ep1_jade_dream1 with dissolve
    ja "Take a look around, [mc_jade]...you're dreaming."
    ja "That means you can do whatever you want...without any consequences..."
    mc "I can?"
    scene ep1_jade_dream2 with dissolve
    ja "Well, that's kind of why I'm kneeling here squeezing my big tits around your huge hard cock, [mc_jade]."
    ja "Let's not waste any more time...you might wake up."
    image anim_jade_boobjob1_ep1 = Movie(channel="anim_jade_boobjob1_ep1", play="images/movies/ep1/anim_jade_boobjob1_ep1.webm")
    scene anim_jade_boobjob1_ep1 with dissolve:
        size (config.screen_width, config.screen_height)
    ja "Here we go..."
    ja "Your cock feels so good between my tits, [mc_jade]..."
    mc "Oh [jade], your tits are so soft..."
    ja "I can squeeze them tighter if you want..."
    mc "No, [jade], this is perfect."
    pause
    image anim_jade_boobjob2_ep1 = Movie(channel="anim_jade_boobjob2_ep1", play="images/movies/ep1/anim_jade_boobjob2_ep1.webm")
    scene anim_jade_boobjob2_ep1 with dissolve:
        size (config.screen_width, config.screen_height)
    pause
    ja "Tell me...do you prefer tits or asses?"
    menu:
        "Tits" if True:
            mc "Oh, definitely tits, [jade]."
            ja "Mhm...that's good to know..."
        "Asses" if True:
            mc "Asses, [jade]. No question about it."
            ja "Really? So, you don't like my tits, then?"
            mc "No, I didn't say that."
            ja "Haha, I'm just teasing you, [mc_jade]..."
    image anim_jade_boobjob1_ep1 = Movie(channel="anim_jade_boobjob1_ep1", play="images/movies/ep1/anim_jade_boobjob1_ep1.webm")
    scene anim_jade_boobjob1_ep1 with dissolve:
        size (config.screen_width, config.screen_height)
    pause
    ja "Would you like me to do something else? I can do anything you want, you know..."
    mc "Wow...anything?"
    ja "Sure. I'm yours to fuck however you wish..."
    ja "...the only thing you can't do, though, is to-"
    $ persistent.ep1_jade_dream1 = True
    $ renpy.end_replay()
    $ calcScenes()
    stop music
    scene ep1_jade_dream_troy
    troy "Wake up!"
    $ bios_history_jade += "I had a sexy dream about Jade...\n\n"
elif True:
    label ep1_cathy_lewd:
    if _in_replay:
        hide screen phone_screen
        if persistent.name == None:
            $ name = "MC"
        elif True:
            $ name = persistent.name
        if persistent.mc_cathy == None:
            $ mc_cathy = name
        elif True:
            $ mc_cathy = persistent.mc_cathy
        if persistent.cathy == None:
            $ cathy = "Cathy"
        elif True:
            $ cathy = persistent.cathy
    play music "music/ep1/slow_day_blues.mp3"
    scene ep1_d2_wake with Fade(1.5, 1, 0.5)
    ca "You did so well on your test, [mc_cathy]."
    if failedEnglish != 0:
        mc "What? But I failed the test..."
    ca "I can't believe you know so much..."
    if failedEnglish != 0:
        mc "Oh, ok...this is a dream..."
    ca "I kind of feel like you should be the one teaching me things."
    scene ep1_d2_wake1 with dissolve
    ca "Would you like to teach me how to pronounce words like onomatopoeia?"
    scene ep1_d2_wake2 with dissolve
    ca "Whoops! I already knew that word..."
    scene ep1_d2_wake3 with dissolve
    ca "What about sarcoidosis?"
    scene ep1_d2_wake2 with dissolve
    ca "Oh, silly me! Again!"
    scene ep1_d2_wake3b with dissolve
    ca "Well, I'm sure that there are other ways..."
    ca "...in which you can wake me up."
    scene ep1_d2_wake4 with dissolve
    ca "Can you wake me up?"
    $ persistent.ep1_cathy_dream1 = True
    $ renpy.end_replay()
    $ calcScenes()
    scene ep1_d2_wake5
    stop music
    troy "Wake up!"
    $ bios_history_cathy += "I had a sexy dream about Cathy.\n\n"
    $ bios_name_cathy = True
    $ chat_new_bios = True
$ guideSuggestedPage = 38
scene ep1_d2_wake6 with hpunch
mc "AHHH!!!"
scene ep1_d2_wake7 with dissolve
troy "What the fuck's the matter with you?"
play music "music/ep1/someways.mp3"
scene ep1_d2_wake8 with dissolve
mc "Oh, nothing..."
mc "What do you want?"
scene ep1_d2_wake7 with dissolve
troy "You need to leave; I'm getting company."
scene ep1_d2_wake8 with dissolve
mc "What? Now?"
scene ep1_d2_wake7 with dissolve
troy "Yes, now! Get out! Don't you have classes to go to or something?"

scene ep1_d2_wake8 with dissolve
menu:
    "Fine" if True:
        $ dk(-1)
        mc "Fine. Give me a second, will you?"
    "Don't you?" if True:
        $ dk(1)
        mc "Don't you?"
play sound "sound_effects/shove.mp3"
scene ep1_d2_wake11 with hpunch
mc "Dude!"
play sound "sound_effects/door_slam.mp3"
scene d1_dorm with hpunch
if dtype > 0:
    mc "(I'm going to fucking snap soon...)"
elif True:
    mc "(This is not sustainable...)"
scene ep1_d2_sage with wipeleft
sa "Hey, it's you again!"
scene ep1_d2_sage1 with dissolve
mc "Hey..."
menu:
    "Sage, was it?" if True:
        $ dk(-1)
        $ ep1_blank_on_name = False
        mc "Sage, was it?"
        scene ep1_d2_sage2 with dissolve
        sa "Right."
    "I'm blanking on your name" if True:
        $ dk(1)
        $ ep1_blank_on_name = True
        mc "I'm blanking on your name."
        scene ep1_d2_sage2b with dissolve
        sa "It's Sage! Fucking learn to listen."
        scene ep1_d2_sage2 with dissolve
$ guideSuggestedPage = 39
sa "You hate Chad, right?"
scene ep1_d2_sage1 with dissolve
menu:
    "Yes" if True:
        if dtype > 0:
            $ RPsage += 1
            mc "Who? Chad? Oh! You mean Mr. Juicebox!"
            scene ep1_d2_sage2c with dissolve
            sa "Mr. Juicebox?"
            scene ep1_d2_sage6 with dissolve
            mc "Yeah, you know, because he's juiced up and kind of looks like a juice box when he walks."
            sa "HAHA! You're fucking mean!"
            $ bios_history_sage += "Sage liked my mean joke.\n\n"
            $ bios_name_sage = True
            $ chat_new_bios = True
            scene ep1_d2_sage2 with dissolve
            sa "I like that."
        elif True:
            mc "With a burning passion."
            scene ep1_d2_sage2 with dissolve
            sa "Good!"
    "No" if True:
        mc "No, I don't hate him."
        scene ep1_d2_sage2 with dissolve
        sa "Yes, you do."
sa "I saw what the jocks did to you yesterday."
scene ep1_d2_sage1 with dissolve
mc "That was nothing."
scene ep1_d2_sage2d with dissolve
sa "Nothing? Not even my G-strings go that high up."
menu:
    "Let me check ({color=#ffffff}Huge {size=-1}{font=collegiate.ttf}DIK{/font}{/size}{/color})" if dtype > 1:
        $ RPsage += 1
        scene ep1_d2_sage_ass with dissolve
        mc "Really? Let me check."
        mc "Hm...hard to tell from here."
        scene ep1_d2_sage_ass1 with dissolve
        sa "Hah. Stop it!"
    "If you say so" if True:
        mc "If you say so."
scene ep1_d2_sage2 with dissolve
sa "I have a proposition for you."
scene ep1_d2_sage1 with dissolve
mc "What's it about?"
scene ep1_d2_sage2 with dissolve
sa "It's simple, really. I want you to find out who Chad's been fucking behind my back."
scene ep1_d2_sage1 with dissolve
menu:
    "What's in it for me?" if True:
        $ dk(1)
        mc "What's in it for me?"
    "No way" if True:
        $ dk(-1)
        if dtype > 0:
            mc "Fat chance. Take care of your own dirty business. I'm not your errand boy."
        elif True:
            mc "Nope, not gonna happen. I'm not getting involved in your love life."
scene ep1_d2_sage2 with dissolve
sa "Well..."
sa "If you scratch my back, I'll scratch yours."
mc "(What is she getting at?)"
scene ep1_d2_sage1 with dissolve
mc "Yeah, I don't know..."
scene ep1_d2_sage14 with dissolve
sa "Think about it."
if ep1_blank_on_name:
    sa "Talk to you later...erm..."
    sa "Sorry, \"I'm blanking on your name\"."
elif True:
    sa "Talk to you later...[name], was it?"
scene ep1_d2_sage15 with dissolve
$ bios_history_sage += "Sage proposed that I help her find out who Chad is fucking behind her back. If I accept, she said I would be rewarded somehow.\n\n"
$ bios_name_sage = True
$ chat_new_bios = True
mc "(This girl is trouble...)"
if dtype > 0:
    mc "(I think I like trouble.)"
scene ep1_d2_math with wipeleft
ca "Good morning, class. Are we ready for a math test today?"
scene ep1_d2_math_de1 with dissolve
de "Yes, I stayed up all night studying for it."
scene ep1_d2_math1 with dissolve
ca "(He's such a smartass.)"
scene ep1_d2_math with dissolve
stop music fadeout 3
ca "Best of luck to you! You may begin."
if not minigames:
    scene black with Fade(1.5, 1, 0.5)
    jump ep1_after_math_test
scene desk_bg with wipeleft
play music "music/ep3/sing_along_with_jim.mp3"
if tutorials:
    scene desk_bg_tut with dissolve
    $ renpy.pause()
    scene desk_bg_tut1 with dissolve
    $ renpy.pause()
    scene desk_bg_tut2 with dissolve
    $ renpy.pause()
jump math101_test1

label ep1_after_math_test:
$ renpy.block_rollback()
if minigames:
    scene ep1_d2_math with wiperight
    stop music fadeout 3
elif True:
    scene ep1_d2_math with fade
ca "Pencils down, class."
ca "Please turn in your tests."
scene ep1_d2_math2 with dissolve
play music "music/ep1/art_nouveau.mp3"
ca "That wasn't so bad, was it?"
ca "Tomorrow, there will be no more tests. I promise."
ca "Instead, we'll start having lectures."
scene ep1_d2_math with dissolve
ca "Don't forget to sign up for other classes online, students."
scene ep1_d2_math3 with dissolve
mc "Hey, Maya. Did you sign up for any class yet?"
scene ep1_d2_math4 with dissolve
my "Yeah, I did. Gender Studies 101."
my "How about you?"
scene ep1_d2_math5 with dissolve
mc "No, nothing yet."
mc "So...gender studies, huh? What's that about?"
scene ep1_d2_math4 with dissolve
my "Well, it's a-"
scene ep1_d2_math6
if assman:
    de "It's a fucking feminist class, ass man."
    my "Ass man?"
elif True:
    de "It's a fucking feminist class, bro."
de "Trust me; it's bullshit."
scene ep1_d2_math7 with dissolve
my "Shut up, Derek. It's not bullshit!"
scene ep1_d2_math8 with dissolve
my "*{i}Psst{/i}* It's easy credits."
scene ep1_d2_math9 with dissolve
de "Easy credits? For real?"
scene ep1_d2_math10b with dissolve
my "Yeah, if you're into that sort of stuff."
scene ep1_d2_math11 with dissolve
de "Define stuff."
scene ep1_d2_math10 with dissolve
my "Women's rights."
scene ep1_d2_math12
de "Nope."
scene ep1_d2_math10 with dissolve
my "Gender equality."
scene ep1_d2_math12
de "Couldn't care less."
scene ep1_d2_math10 with dissolve
my "Vaginas."
scene ep1_d2_math12
de "No-"
scene ep1_d2_math13 with dissolve
de "Yes!"
scene ep1_d2_math14 with dissolve
my "That was a test. You just failed."
scene ep1_d2_math15 with dissolve
de "So, no vaginas?"
scene ep1_d2_math10b with dissolve
my "Well, probably some vaginas..."
scene ep1_d2_math17 with dissolve
my "Wait, why are we discussing vaginas?"
my "No, Derek, I don't think it's a class for you."
scene ep1_d2_math18 with dissolve
de "Yeah, whatever."
scene ep1_d2_math19 with dissolve
my "You, on the other hand... Are you up for it?"
scene ep1_d2_math20 with dissolve
mc "I don't think it's for me either..."
scene ep1_d2_math19 with dissolve
my "Come on! It will be fun!"
my "If you don't like it, you can just sit there and pretend to listen."
scene ep1_d2_math22 with dissolve
my "Like I said...easy credits."
my "Plus, it will look good on your resume."
scene ep1_d2_math20 with dissolve
$ genderPresented = True
show screen skillmsg
mc "Ok, what the hell. I can give it a shot."
hide screen skillmsg
$ bios_history_maya += "Maya convinced me to sign up for Gender Studies.\n\n"
$ bios_name_maya = True
$ chat_new_bios = True
scene ep1_d2_math19 with dissolve
my "Wanna eat lunch together?"
scene ep1_d2_math20 with dissolve
mc "Sure...but tell me..."
mc "Is there anything else to eat around here besides cafeteria food?"
scene ep1_d2_math19 with dissolve
my "Ah, you want to eat healthier too!"
stop music fadeout 3
my "We'll have to go outside of campus."
my "Are you up for it?"
scene ep1_d2_math20 with dissolve
mc "Lead the way."
$ guideSuggestedPage = 40
play music "music/ep1/golden_alley.mp3"
$ renpy.sound.play("sound_effects/cafeteria.mp3", channel="sfx1", loop=True)
scene ep1_cafe_maya with wipeleft
my "Oh, I've been there. It's very close!"
scene ep1_cafe_maya1 with dissolve
mc "Yeah, it's just 30 minutes by train."
mc "I will probably go back and visit my dad a lot."
scene ep1_cafe_maya2 with dissolve
my "..."
mc "How about you? You said you're a local."
mc "Do you live close by?"
scene ep1_cafe_maya2b with dissolve
my "I live on campus, stupid."
scene ep1_cafe_maya2 with dissolve
mc "Well, I kind of meant your parents."
scene ep1_cafe_maya2c with dissolve
my "They live uptown; it's not far from here."
scene ep1_cafe_maya2 with dissolve
mc "(Hm...her tone has changed...)"
if dtype < 1:
    mc "(This is probably a sensitive issue...)"
elif True:
    mc "(I wonder why...)"
scene ep1_cafe_maya6 with dissolve
my "Enough family talk. Let me see what kind of person you really are!"
scene ep1_cafe_maya7 with dissolve
mc "Erm...ok? What do you have in mind?"
scene ep1_cafe_maya6 with dissolve
my "I'll ask you a few questions, and after that, I'm going to figure you out."
scene ep1_cafe_maya7 with dissolve
mc "I've never done such a thing before...but all right."
mc "Fire away."
scene ep1_cafe_maya6 with dissolve
my "Which do you prefer...being indoors or outdoors?"
scene ep1_cafe_maya7 with dissolve
menu:
    "Indoors" if True:
        $ ep1_maya_question_indoors = True
        mc "I'm an indoors kind of guy."
    "Outdoors" if True:
        $ ep1_maya_question_indoors = False
        mc "Easy, definitely outdoors."
scene ep1_cafe_maya8 with dissolve
my "Interesting..."
scene ep1_cafe_maya6 with dissolve
my "Which sounds nicer...?"
my "Cuddling up with a blanket or taking a bubble bath?"
scene ep1_cafe_maya7 with dissolve
menu:
    "Cuddling with a blanket" if True:
        $ ep1_maya_question_blanket = True
        $ ep1_maya_question_bath = False
        mc "Cuddling up with a blanket sounds nicer...but I'm not sure I would do that by myself."
    "Bubble bath" if True:
        $ ep1_maya_question_blanket = False
        $ ep1_maya_question_bath = True
        mc "I'd have to say bubble baths...is that weird?"
        scene ep1_cafe_maya8 with dissolve
        my "I'm asking the questions here. You just answer them."
    "Neither" if True:
        $ ep1_maya_question_blanket = False
        $ ep1_maya_question_bath = False
        mc "Nope, neither of those are for me."
scene ep1_cafe_maya9 with dissolve
my "Do you drink alcohol?"
scene ep1_cafe_maya7 with dissolve
mc "Yeah, it happens."
mc "But I haven't partied a lot in my life...yet."
scene ep1_cafe_maya9 with dissolve
my "Would you rather spend a night with friends getting drunk at a party or at home with a bottle of wine?"
scene ep1_cafe_maya7 with dissolve
menu:
    "At a party" if True:
        $ ep1_maya_question_party = True
        mc "At a party, of course!"
    "At home" if True:
        $ ep1_maya_question_party = False
        mc "I wouldn't be against partying, but I'd prefer just staying home chatting and casually drinking with them."
scene ep1_cafe_maya9 with dissolve
my "Do you keep your promises?"
scene ep1_cafe_maya10 with dissolve
mc "I think I do..."
scene ep1_cafe_maya9 with dissolve
my "So, if I asked you to promise me something..."
my "...would you?"
scene ep1_cafe_maya10 with dissolve
mc "For you? Sure."
scene ep1_cafe_maya9 with dissolve
my "Ok. Can you promise me to always be honest with me and to never lie?"
scene ep1_cafe_maya11 with dissolve
mc "I can do that."
scene ep1_cafe_maya9 with dissolve
my "Really? Say it!"
scene ep1_cafe_maya11 with dissolve
mc "I promise!"
mc "Why wouldn't I be able to? I can be 100%% honest with you."
scene ep1_cafe_maya6 with dissolve
my "Do you masturbate?"
scene ep1_cafe_maya11 with dissolve
mc "Ok, maybe 99%% honest with you."
scene ep1_cafe_maya11b with dissolve
my "Haha! Come on, you promised!"
scene ep1_cafe_maya11 with dissolve
mc "I thought you meant honesty like telling you if you looked fat in a dress or something."
mc "Not something so personal."
scene ep1_cafe_maya11c with dissolve
my "Yeah, sorry. I don't think I can trust you."
scene ep1_cafe_maya11 with dissolve
mc "I can be 100%% honest, but then you would have to be that way too!"
scene ep1_cafe_maya11c with dissolve
my "If you can prove to me that you are...yeah! I could do that."
my "But you would REALLY have to prove it."
scene ep1_cafe_maya11 with dissolve
mc "Fine. Yes, I masturbate. Who doesn't?"
scene ep1_cafe_maya11c with dissolve
my "I don't."
scene ep1_cafe_maya11 with dissolve
mc "What!?"
scene ep1_cafe_maya11c with dissolve
my "Yeah, there must be something seriously wrong with you."
scene ep1_cafe_maya11b with dissolve
mc "Ok, now you're just fucking with me."
my "Hahaha!"
mc "What about you?"
scene ep1_cafe_maya9 with dissolve
my "Nuh-uh! I'm still asking the questions here, remember?"
my "How many relationships have you been in?"
scene ep1_cafe_maya11 with dissolve
mc "...just one. Listen, I don't want to talk about that."
scene ep1_cafe_maya11d with dissolve
my "Ended poorly, huh?"
scene ep1_cafe_maya11 with dissolve
mc "Don't they all?"
scene ep1_cafe_maya11d with dissolve
my "I wouldn't know."
scene ep1_cafe_maya11c with dissolve
my "Ok, I'm not gonna push you on that, for now."
my "How many girls have you slept with?"
scene ep1_cafe_maya11 with dissolve
mc "Wow, you're really going all-in on personal questions..."
scene ep1_cafe_maya11d with dissolve
my "Ok, don't answer that. I'll stop."
scene ep1_cafe_maya with dissolve
my "Wow, time really flies chatting with you!"
scene ep1_cafe_maya24 with dissolve
my "Come, let's leave."
show screen moneymsg
menu:
    "Pay for her meal ({color=#36ca2b}${/color})" if money > 0:
        $ bios_history_maya += "I had a nice afternoon with Maya, I paid for her lunch.\n\n"
        $ ep1_maya_question_money = True
        $ money -= 1
        $ RPmaya += 1
        mc "Hey, keep that. It's my treat."
        hide screen moneymsg
        my "Are you sure?"
        mc "Yeah, I want to."
        scene ep1_cafe_maya25 with dissolve
        my "Thank you so much!"
    "Don't pay for her meal" if True:
        $ bios_history_maya += "I had a nice afternoon with Maya.\n\n"
        hide screen moneymsg
        $ ep1_maya_question_money = False
        $ renpy.pause(0.5)
$ bios_name_maya = True
$ chat_new_bios = True
scene ep1_cafe_maya26 with dissolve
my "Remember what I said in the beginning?"
scene ep1_cafe_maya27 with dissolve
mc "Beginning of what?"
scene ep1_cafe_maya26 with dissolve
my "That I thought that I could figure you out."
scene ep1_cafe_maya27 with dissolve
mc "Ah, yeah."
scene ep1_cafe_maya26 with dissolve
my "I just did."
scene ep1_cafe_maya27 with dissolve
mc "And?"
scene ep1_cafe_maya28 with dissolve
my "I'm not telling you."
scene ep1_cafe_maya27 with dissolve
mc "I don't know if that's good or bad..."
scene ep1_cafe_maya28 with dissolve
my "You're..."
my "...different."
$ renpy.sound.stop(channel="sfx1", fadeout=3)
scene ep1_cafe_maya27 with dissolve
stop music fadeout 3
mc "That doesn't make it any clearer."
scene ep1_cafe_maya30 with hpunch
my "I'm different too."

scene ep1_troy_fight with Fade(1.5,1,0.5)
play music "music/ep1/food_chain.mp3"
mc "Hey. Safe to come in?"
troy "..."
mc "(What happened here...?)"
scene ep1_troy_fight1 with dissolve
mc "Are you ok?"
troy "Leave me alone."
scene ep1_troy_fight2 with dissolve
mc "Hey...where's my guitar?"
scene ep1_troy_fight1 with dissolve
troy "..."
troy "It's gone."
mc "SAY WHAT!?"
scene ep1_troy_fight4 with dissolve
troy "There was nothing I could do."
scene ep1_troy_fight5 with dissolve
mc "Are you fucking kidding me!? That's MY guitar!"
mc "Who the FUCK stole it!?"
play sound "sound_effects/shove.mp3"
scene ep1_troy_fight6 with vpunch
troy "Fuck off! I told you to leave me alone...you...you dick!"
scene ep1_troy_fight7 with dissolve
mc "TELL ME WHO STOLE IT!"
scene ep1_troy_fight8 with dissolve
troy "Some fucking jocks stormed in and took it, ok!?"
scene ep1_troy_fight7 with dissolve
mc "And you just let them do that!?"
scene ep1_troy_fight8 with dissolve
troy "You think I wanted this!?"
scene ep1_troy_fight7 with dissolve
mc "You're a fucking asshole!!"
play sound "sound_effects/shove.mp3"
scene ep1_troy_fight6 with vpunch
troy "Get the fuck out!!! There's no fucking way that you're staying here anymore!"
if tutorials:
    show white_screen with dissolve
    show screen majorChoiceScale
    show text "{color=#ffffff}During the game, you will encounter major choices. These choices will shape your character with time.\nIf the choice you make is considered to be a {size=+3}{color=#ffb052}{font=collegiate.ttf}DIK{/font}{/color}{/size} choice, one bar will be removed from the {size=+3}{color=#ffb052}{font=collegiate.ttf}CHICK{/font}{/color}{/size} side; vice versa.{/color}" zorder 2 with dissolve:
        ypos 0.825
    $ renpy.pause()
    show text "{color=#ffffff}After making several major {size=+3}{color=#ffb052}{font=collegiate.ttf}DIK{/font}{/color}{/size} or {size=+3}{color=#ffb052}{font=collegiate.ttf}CHICK{/font}{/color}{/size} choices you will be unable to progress on the opposite side past a certain point.\nBeware, eventually you may be forced to make good or bad decisions as a result of how you shaped your character.{/color}" zorder 2 with dissolve:
        ypos 0.825
    $ renpy.pause()
    hide text
    hide white_screen with dissolve
elif True:
    show screen majorChoiceScale
label makeChoice:
    menu:
        "Beat him up" if True:
            $ bios_history_troy += "Because of Troy, my guitar got stolen. I lost my temper and punched him.\n\n"
            $ ep1_beat_up_troy = True
            $ bios_name_troy = True
            $ addCPenalty()
            $ renpy.pause(1)
            hide screen majorChoiceScale
            play sound "sound_effects/hit.mp3"
            scene ep1_troy_fight13 with hpunch
            $ renpy.pause()
            if minigames:
                $ brawlerStoryFight = "troy"
                $ brawlerStoryFightLabel = "ep1_after_troy_fight"
                jump app_brawler_label
                label ep1_after_troy_fight:
                $ sports_opponent_idx = 0
                $ brawlerStoryFight = ""
                $ brawlerStoryFightLabel = ""
                if ep1_beat_up_troy_won and brawler_difficulty == 3 and steamAchievements:
                    if not config.console and not config.developer:
                        $ achievement.grant("DORMMATEBEATDOWN")
                        init:
                            $ achievement.register("DORMMATEBEATDOWN")
                        $ achievement.Sync()
            elif True:
                $ ep1_beat_up_troy_won = True
            if ep1_beat_up_troy_won:
                $ bios_history_mc += "I beat Troy up.\n\n"
                $ bios_name_mc = True
                $ chat_new_bios = True
                play sound "sound_effects/whoosh.mp3"
                scene ep1_troy_fight14 with dissolve
                $ renpy.pause(0.5)
                play sound "sound_effects/hit.mp3"
                scene ep1_troy_fight13 with hpunch
                $ renpy.pause(0.5)
                scene ep1_troy_fight16 with dissolve
                mc "THIS IS FAR FROM FUCKING OVER, TROY!"
                stop music fadeout 3
                scene ep1_troy_fight17b with dissolve
                mc "I'LL GET YOU FOR THIS!!!"
                troy "..."
            elif True:
                $ bios_history_mc += "I tried to beat Troy up.\n\n"
                $ bios_name_mc = True
                $ chat_new_bios = True
                play sound "sound_effects/hit.mp3"
                scene ep1_troy_fight14b with dissolve
                $ renpy.pause(0.5)
                scene ep1_troy_fight16b with dissolve
                troy "I SAID GET THE FUCK OUT!!!"
                scene ep1_troy_fight17b with dissolve
                stop music fadeout 3
                mc "I'LL FUCKING GET YOU FOR THIS!!!"
                troy "..."
        "Storm out" if True:
            $ bios_history_mc += "I was angry, but I didn't beat Troy up.\n\n"
            $ bios_history_troy += "Because of Troy, my guitar got stolen. I stormed out screaming when he told me.\n\n"
            $ ep1_beat_up_troy = False
            $ bios_name_mc = True
            $ bios_name_troy = True
            $ chat_new_bios = True
            $ addDPenalty()
            $ renpy.pause(1)
            hide screen majorChoiceScale
            stop music fadeout 3
            scene ep1_troy_fight17b with dissolve
            mc "I'LL GET YOU FOR THIS, TROY!"
            troy "..."
play music "music/ep1/unknown_power.mp3"
scene ep1_reception with fade
mc "Hey, reception lady! Wait! I need help!"
scene ep1_reception1 with dissolve
rc "I'm going home for the day; you can come back tomorrow morning."
scene ep1_reception1b with dissolve
mc "This is urgent! I need somewhere else to stay!"
mc "I got into a huge fight with my dorm mate, and there's just no way I can stay there any longer!"
scene ep1_reception1 with dissolve
rc "Oh, I'm afraid it's not that simple. There's a whole process behind changing dorms that-"
scene ep1_reception1b with dissolve
mc "Please! This is an emergency!"
scene ep1_reception1 with dissolve
rc "Calm down. There's nothing that can be done for you at the moment."
rc "Try to get along with your dorm mate or maybe stay with a friend until we can get you a new dorm."
scene ep1_reception1b with dissolve
mc "Really? That's all you can do!?"
scene ep1_reception1 with dissolve
rc "For now...yes."
rc "Or...you could try talking to the different fraternities and see if they will help you."
scene ep1_reception7 with dissolve
mc "(The fraternities...really?)"
mc "(The nerds don't have a house...)"
mc "(The jocks? Yeah, right...)"
stop music fadeout 5
mc "(The preps? Good luck getting close to that mansion...)"
mc "(...)"
mc "(The DIKs.)"

play music "music/ep1/my_heart.mp3"
scene ep1_diks with wiperight
dikc "CHUG! CHUG! CHUG!"
dikc "YEAH!!!"
scene ep1_diks1 with dissolve
rs "Ladies and not-so-gentlemen!"
rs "The winner is the reigning Massive DIK..."
rs "TOMMY!!!"
play sound "sound_effects/burp.mp3"
tm "*{i}BURP{/i}*!!!"
scene ep1_diks4 with dissolve
tm "Fucking learn how to drink, Jacob!"
scene ep1_diks4b with dissolve
jac "Man, fuck you. You probably were breastfed beer as a kid."
scene ep1_diks4c with dissolve
tm "Get fucked! I get more tits in my mouth these days than I did back then."
scene ep1_diks5 with dissolve
tm "Hey! Hold the fuck up! Who's that!?"
tm "Is that a jock!?"
scene ep1_diks6 with dissolve
mc "Erm...hi, the door was open and I-"
scene ep1_diks6b with dissolve
rs "Hm...doesn't look like a jock to me."
scene ep1_diks6c with dissolve
if intervenedChad:
    $ RPdiks += 1
    jac "Nah! That's no jock!"
    jac "This is the freshy I was telling you about."
    jac "He almost gave it to Chad in the cafeteria!"
    scene ep1_diks9b with dissolve
    hg "Wow!"
    tm "Almost, huh? That doesn't cut it."
    scene ep1_diks10 with dissolve
    rs "Dude, come on! It's not like you would have tried to go head-to-head with Chad."
elif True:
    jac "No, this is the freshy who got a wedgie from Dawe!"
    scene ep1_diks9c with dissolve
    hg "Haha!"
    tm "Haha! Dawe's such a fucking cunt!"
scene ep1_diks11 with dissolve
rs "Hey! Who are you?"
mc "[name]."
rs "How do you feel about the jocks?"
scene ep1_diks6 with dissolve
menu:
    "I don't hate them" if True:
        $ RPdiks -= 1
        mc "I don't hate them, but they did steal something very valuable from me."
        scene ep1_diks9b with dissolve
        tm "This fucking guy..."
        tm "He's either stupid or a jock...or both."
        scene ep1_diks10 with dissolve
        rs "Hm...maybe he's not been enlightened."
        scene ep1_diks9b with dissolve
        tm "Pff..."
    "I hate them" if True:
        $ RPdiks += 1
        if dtype > 0:
            mc "I hate the fucking jocks!"
        elif True:
            mc "I don't like them at all."
        mc "They stole something very valuable from me..."
scene ep1_diks6b with dissolve
rs "Yeah. He's not a jock...right?"
scene ep1_diks6 with dissolve
if dtype > 0:
    mc "I may have the physique for it, but no, I'm not a jock."
elif True:
    mc "No, I'm just me."
    scene ep1_diks30 with dissolve
    tm "How cute!"
scene ep1_diks17 with dissolve
ri "Yeah, he's not a jock."
ri "This guy was hitting on Sage before."
$ guideSuggestedPage = 41
ri "No jock would be stupid enough to do that."
scene ep1_diks6 with dissolve
menu:
    "Play along" if True:
        $ ep1_played_along = True
        $ RPdiks += 1
        mc "Yeah, that's right."
        scene ep1_diks18 with dissolve
        rs "HAHA! This guy is fucking DIK material!"
        scene ep1_diks21 with dissolve
    "Deny" if True:
        $ ep1_played_along = False
        mc "No, that's just not true!"
        scene ep1_diks6b with dissolve
        rs "Yeah, I don't know what to make of this guy."
        scene ep1_diks6 with dissolve
mc "Here's the deal, I came here looking for some place to stay."
if ep1_beat_up_troy:
    mc "I got into a fight with my dorm mate, and I can't stay there anymore."
elif True:
    mc "I got into an argument with my dorm mate, and I can't stay there anymore."
scene ep1_diks11 with dissolve
rs "Who's your dorm mate?"
scene ep1_diks6 with dissolve
if dtype > 0:
    mc "Some fucking asshole named Troy."
elif True:
    mc "Just some guy named Troy."
scene ep1_diks6c with dissolve
jac "Long black hair?"
mc "Yeah."
scene ep1_diks18 with dissolve
if not ep1_played_along:
    rs "See? This guy is DIK material!"
elif True:
    rs "That fucking seals the deal for me!"
rs "That's another jock he's got issues with!"
scene ep1_diks21 with dissolve
mc "Wait, Troy's not a jock."
scene ep1_diks6c with dissolve
jac "Former jock. He got kicked out."
scene ep1_diks18 with dissolve
rs "That's just semantics! A jock's a fucking jock!"
scene ep1_diks21b with dissolve
tm "Yeah, I don't know. I say we test him."
scene ep1_diks21c with dissolve
rs "You want to pledge our house, yes?"
scene ep1_diks21 with dissolve
mc "If that would get me a place to stay, then yes."
scene ep1_diks27 with dissolve
tm "Rusty...he must be tested."
scene ep1_diks18 with dissolve
rs "Gah, this is tough. But rules are rules!"
rs "A test it is."
scene ep1_diks21 with dissolve
mc "What do I have to do?"
scene ep1_diks30 with dissolve
tm "Oh, it's really simple."
tm "You need to bring us one small item from the HOTs, and we'll consider your pledge."
mc "An item?"
scene ep1_diks6c with dissolve
jac "A pair of panties, dude. We've all done it."
jac "Think of it as an...initiation."
if dtype > 0:
    scene ep1_diks32 with dissolve
    mc "Hey, you! How about you give me yours, and this will be all over?"
    tm "Hah! No way it's that simple."
scene ep1_diks30 with dissolve
tm "How you go about and do it, that's up to you."
tm "But you must enter their house and leave with a pair of panties. Those are the rules."
if dtype > 0:
    mc "Fine, I'll be back in a minute."
elif True:
    mc "Ok...I'll try..."
stop music fadeout 3
scene ep1_diks36 with dissolve
tm "Hey. Fresh bait on the hook."

jump ep1_freeroam_hots_label

label ep1_raid_panties_label:
scene ep1_panties with dissolve
$ renpy.block_rollback()
stop music fadeout 5
mc "(Yes! These will do perfectly!)"
cam "Why do I have to do that?"
mc "(Shit! Someone's coming.)"
scene ep1_panties1 with dissolve
play music "music/ep1/funk_rock.mp3"
mc "(I'll hide in here...)"
qu "Think of it as a rite of passage or an initiation. Something we all do at least once."
scene ep1_panties3 with dissolve
cam "If that's really the case...I'll do it."
qu "Good girl."
scene ep1_panties4 with dissolve
mc "(Holy shit! What an ass...)"
mc "(I can't believe this...if they see me, I'm totally screwed.)"
qu "Just follow the instructions we give you, and you'll be fine."
scene ep1_panties5 with dissolve
qu "Huh!? Is somebody in there?"

menu:
    "Stay quiet" if True:
        mc "..."
        qu "You in the booth! Speak up!"
    "Act like a girl" if True:
        mc "*{i}High voice{/i}* It's just me, girls."
        qu "And who would that be?"
        mc "Erm...Suzanne?"
scene ep1_panties6 with dissolve
qu "What do we have here? A fucking perv!"
mc "Please, I can explain!"
scene ep1_panties7 with dissolve
qu "Yeah, go ahead and explain why you're standing here holding a pair of panties with a hard-on."
mc "Oh shit..."
scene ep1_panties6 with dissolve
qu "Please. I'm all ears."
scene ep1_panties8 with dissolve
qu "Were you enjoying yourself watching Camila getting naked in front of you?"
qu "She's got a nice ass, huh?"

menu:
    "Agree" if True:
        $ dk(1)
        mc "Yeah, her ass is amazing."
    "Try to leave" if True:
        $ dk(-1)
        mc "I'm so sorry; I'm leaving."
        scene ep1_panties9 with dissolve
        qu "Whoa! Whoa! Not so fast there, [mc_quinn]!"
scene ep1_panties10 with dissolve
qu "Show us what you hide in those shorts."
qu "Strip!"
scene ep1_panties12 with dissolve
mc "Why would I do that?"
scene ep1_panties11 with dissolve
qu "Strip, [mc_quinn], or I'll make sure that everyone hears about how you snuck into our showers trying to wank to us being naked!"
scene ep1_panties12 with dissolve
mc "Come on, that's not the truth!"
scene ep1_panties11 with dissolve
stop music fadeout 3
qu "It will be. Strip!"
play sound "sound_effects/clothes.mp3"
label ep1_quinn_lewd:
if _in_replay:
    hide screen phone_screen
    if persistent.name == None:
        $ name = "MC"
    elif True:
        $ name = persistent.name
    if persistent.mc_quinn == None:
        $ mc_quinn = "pervert"
    elif True:
        $ mc_quinn = persistent.mc_quinn
    if persistent.quinn == None:
        $ quinn = "Quinn"
    elif True:
        $ quinn = persistent.quinn
scene ep1_panties10 with dissolve
hide screen phone_screen
mc "Fine! There! You've seen me too now. Can I leave?"
qu "Camila. Come over here."
play music "music/ep1/slow_day_blues.mp3"
scene ep1_panties13 with dissolve
qu "Show him the goods."
scene ep1_panties14 with dissolve
mc "Wait, what?"
scene ep1_panties15 with dissolve
mc "Oh my god..."
scene ep1_panties16 with dissolve
qu "See? I knew it. You are getting off to watching Camila naked."
qu "Look at that hard cock!"
scene ep1_panties17 with dissolve
qu "I bet this is what you really came to see..."
image anim_quinn_kiss_ep1 = Movie(channel="anim_quinn_kiss_ep1", play="images/movies/ep1/anim_quinn_kiss_ep1.webm")
scene anim_quinn_kiss_ep1 with dissolve:
    size (config.screen_width, config.screen_height)
pause
menu:
    "Get involved" if True:
        $ ep1_lewd_camila_quinn = True
        $ dk(1)
        scene ep1_panties18 with dissolve
        mc "Yeah, that looks really nice..."
        scene ep1_panties19 with dissolve
        qu "Grab his cock, Camila."
        qu "Give this pervert what he really came for."
        image anim_camila_hj_ep1 = Movie(channel="anim_camila_hj_ep1", play="images/movies/ep1/anim_camila_hj_ep1.webm")
        scene anim_camila_hj_ep1 with dissolve:
            size (config.screen_width, config.screen_height)
        qu "Mmm...that's it. Can you feel how his cock is pulsating in your hand?"
        qu "I bet this guy's a virgin."
        qu "Coming in here trying to jack off to little girls. That's fucking disgusting!"
        mc "(Wow...I've never gotten a handjob from two girls before...)"
        mc "(This feels amazing. The way Camila is gripping my cock while Quinn is stroking the head...)"
        pause
        image anim_quinn_kiss_ep1 = Movie(channel="anim_quinn_kiss_ep1", play="images/movies/ep1/anim_quinn_kiss_ep1.webm")
        scene anim_quinn_kiss_ep1 with dissolve:
            size (config.screen_width, config.screen_height)
        mc "(They're really going at it... Fuck, this is just too hot...)"
        pause
        image anim_quinn_kiss2_ep1 = Movie(channel="anim_quinn_kiss2_ep1", play="images/movies/ep1/anim_quinn_kiss2_ep1.webm")
        scene anim_quinn_kiss2_ep1 with dissolve:
            size (config.screen_width, config.screen_height)
        pause
        image anim_camila_hj_ep1 = Movie(channel="anim_camila_hj_ep1", play="images/movies/ep1/anim_camila_hj_ep1.webm")
        scene anim_camila_hj_ep1 with dissolve:
            size (config.screen_width, config.screen_height)
        qu "Keep going, Camila... He isn't twitching yet."
        qu "That means he's not ready to cum."
        qu "Keep massaging that pervert's cock."
        pause
        image anim_camile_ass_ep1 = Movie(channel="anim_camile_ass_ep1", play="images/movies/ep1/anim_camile_ass_ep1.webm")
        scene anim_camile_ass_ep1 with dissolve:
            size (config.screen_width, config.screen_height)
        mc "(She has the softest ass I've ever felt...)"
        pause
        cam "Quinn, he's touching my ass..."
        qu "I fucking told you that he's a pervert!"
        scene ep1_panties19b with dissolve
        qu "Hey! Did I say you could touch her, you pervy little cunt!?"
        scene ep1_panties19c with dissolve
        mc "Come on; I thought we were having fun..."
        if _in_replay and not persistent.ep1_quinn_full:
            scene ep1_panties_leaving1 with hpunch
            qu "PERVERT! SOMEBODY CALL SECURITY!!!"
            $ renpy.end_replay()
        elif dtype < 2 and not _in_replay:
            $ persistent.ep1_quinn = True
            $ calcScenes()
            stop music
            play sound "sound_effects/shove.mp3"
            scene ep1_panties_leaving1 with hpunch
            qu "PERVERT! SOMEBODY CALL SECURITY!!!"
            play music "music/ep4/driving_rock.mp3"
            jump ep1_after_raid_label
        scene ep1_panties19d with dissolve
        qu "Fun, huh?"
        qu "Heh, I like your confidence."
        scene ep1_panties22 with dissolve
        qu "But you're in no position to be calling the shots here."
        qu "Do you understand?"
        mc "*{i}Muffled voice{/i}* Mhm."
        qu "Camila. You know what to do."
        scene ep1_panties20 with dissolve
        qu "Jack him off."
        scene ep1_panties21 with dissolve
        qu "Let me know when the fucker starts twitching."
        image anim_cam_hj_ep1 = Movie(channel="anim_cam_hj_ep1", play="images/movies/ep1/anim_cam_hj_ep1.webm")
        scene anim_cam_hj_ep1 with dissolve:
            size (config.screen_width, config.screen_height)
        qu "Do you like that, [mc_quinn]?"
        qu "Do you like the way her soft hands rub your cock?"
        pause
        scene ep1_panties22 with dissolve
        qu "What's that? You want to watch her jerking you off?"
        qu "That's not going to happen, you little shit!"
        image anim_quinn_lick_ep1 = Movie(channel="anim_quinn_lick_ep1", play="images/movies/ep1/anim_quinn_lick_ep1.webm")
        scene anim_quinn_lick_ep1 with dissolve:
            size (config.screen_width, config.screen_height)
        qu "Mmm... You taste good..."
        pause
        scene ep1_panties22 with dissolve
        qu "How's it going, Camila? Is he twitching yet?"
        image anim_cam_hj_ep1 = Movie(channel="anim_cam_hj_ep1", play="images/movies/ep1/anim_cam_hj_ep1.webm")
        scene anim_cam_hj_ep1 with dissolve:
            size (config.screen_width, config.screen_height)
        cam "No...nothing yet."
        pause
        scene ep1_panties22 with dissolve
        qu "Put it in another gear, then."
        scene ep1_panties23 with dissolve
        cam "You mean faster?"
        qu "No. Use your mouth and hands."
        image anim_cam_bj_ep1 = Movie(channel="anim_cam_bj_ep1", play="images/movies/ep1/anim_cam_bj_ep1.webm")
        scene anim_cam_bj_ep1 with dissolve:
            size (config.screen_width, config.screen_height)
        cam "*{i}Mphff...{/i}*"
        qu "That's it, girl. Suck that dick."
        qu "You should see this, [mc_quinn]. She's really doing a fine job handling that cock."
        qu "I can tell that she's done this many times before. Haven't you, Camila?"
        cam "*{i}Mphff...{/i}*"
        pause
        image anim_quinn_lick_ep1 = Movie(channel="anim_quinn_lick_ep1", play="images/movies/ep1/anim_quinn_lick_ep1.webm")
        scene anim_quinn_lick_ep1 with dissolve:
            size (config.screen_width, config.screen_height)
        qu "You like having two warm tongues against your body, [mc_quinn]?"
        pause
        image anim_cam_bj_var_ep1 = Movie(channel="anim_cam_bj_var_ep1", play="images/movies/ep1/anim_cam_bj_var_ep1.webm")
        scene anim_cam_bj_var_ep1 with dissolve:
            size (config.screen_width, config.screen_height)
        qu "Looks like she's enjoying that cock..."
        qu "She's such a slut. Aren't you Camila?"
        cam "*{i}Mphff...{/i}*"
        pause
        image anim_cam_bj_ep1 = Movie(channel="anim_camila_bj_ep1", play="images/movies/ep1/anim_cam_bj_ep1.webm")
        scene anim_cam_bj_ep1 with dissolve:
            size (config.screen_width, config.screen_height)
        qu "Hm...he isn't getting closer..."
        pause
        qu "What if he got to look into your eyes, Camila? Is this what you wanna see, you fucking pervert?"
        image anim_cam_bj_long_ep1 = Movie(channel="anim_cam_bj_long_ep1", play="images/movies/ep1/anim_cam_bj_long_ep1.webm")
        scene anim_cam_bj_long_ep1 with dissolve:
            size (config.screen_width, config.screen_height)
        pause
        qu "Wow, she's good at that!"
        qu "I didn't know a freshy could suck cock that well..."
        qu "You'll be a sorority sister in no time, Camila."
        qu "Hm...what was that? I think the pervert here twitched when I called her sister."
        qu "What's wrong with you?"
        mc "*{i}Mphff...{/i}*"
        qu "Let's try that again..."
        qu "Do you like when Sister Camila is sucking your cock?"
        pause
        qu "Oh! Now he's twitching for sure!"
        scene ep1_panties26 with dissolve
        qu "Camila! Stop it!"
        scene ep1_panties27 with dissolve
        stop music fadeout 3
        qu "Here, take your fucking panties!"
        qu "And get the fuck out of here!"
        play music "music/ep4/driving_rock.mp3"
        mc "Huh? But what about my clothes?"
        play sound "sound_effects/shove.mp3"
        scene ep1_panties_leaving1 with hpunch
        qu "PERVERT! SOMEBODY CALL SECURITY!!!"
        $ persistent.ep1_quinn = True
        $ persistent.ep1_quinn_full = True
        $ renpy.end_replay()
        $ calcScenes()
        jump ep1_after_raid_label
    "Leave" if True:
        $ renpy.end_replay()
        $ ep1_lewd_camila_quinn = False
        $ dk(-1)
        mc "Nope, sorry. I'm leaving."
        scene ep1_panties_leaving with dissolve
        qu "Leave the clothes."
        play music "music/ep4/driving_rock.mp3"
        mc "What!?"
        play sound "sound_effects/shove.mp3"
        scene ep1_panties_leaving1 with hpunch
        qu "PERVERT! SOMEBODY CALL SECURITY!!!"
        jump ep1_after_raid_label

label ep1_after_raid_label:
play sound "sound_effects/door_slam.mp3"
scene ep1_raid2e with hpunch
play sound "sound_effects/door_lock.mp3"
mc "(FUCK! FUCK! FUCK!)"
scene ep1_panties_leaving3 with dissolve
hg "AHHH!!!"
mc "I'M SO SORRY! FUCK!"
scene ep1_panties_leaving3b with dissolve
hg "OH MY GOD! PERVERT!"
mc "NO, I'M REALLY NOT!"
mc "SORRY!"
scene ep1_panties_leaving4 with dissolve
hg "Hahaha!"
$ bios_camila = True
$ bios_quinn = True
if ep1_lewd_camila_quinn:
    if dtype >= 2:
        $ bios_history_camila = "Camila gave me a handjob and a blowjob... If Quinn just would have let me finish, it would have been amazing.\n\n"
    elif True:
        $ bios_history_camila = "Camila gave me a handjob... If Quinn just would have let me finish, it would have been amazing.\n\n"
    $ bios_history_quinn += "Quinn played me like a fiddle. I really thought I was going to fuck her and Camila in that bathroom...\nShe stole my clothes and the key to my dorm.\n\n"
elif True:
    $ bios_history_camila = "I saw Camila naked today. She has a great body.\n\n"
    $ bios_history_quinn += "I left as fast as I could when Quinn and Camila confronted me. She stole my clothes and the key to my dorm.\n\n"
$ bios_name_camila = True
$ bios_name_quinn = True
$ chat_new_bios = True
$ current_task = "None"
$ chat_new_tasks = False

scene ep1_panties_leaving5 with fade
mc "(I'm fucking freezing...)"
mc "(I got the panties...they have to let me in!)"
play sound "sound_effects/door_bang.mp3"
scene ep1_panties_leaving7 with hpunch
mc "Hey!!! Open up!"
scene ep1_panties_leaving8 with dissolve
tm "Haha! What the fuck is this!?"
scene ep1_panties_leaving9 with dissolve
mc "Here, I got you the panties!"
mc "Can I come in? I'm freezing my balls off out here!"
scene ep1_panties_leaving10 with dissolve
tm "HAHA! DIKS! RUSTY!"
tm "Come! You've got to see this!"
scene ep1_panties_leaving11 with dissolve
rs "Hey, what's-"
scene ep1_panties_leaving12 with dissolve
rs "...up."
jac "Oh, hell naw."
dikc "Ding dong!"
scene ep1_panties_leaving13 with dissolve
mc "Hey, guys! I did what you told me; please let me in."
scene ep1_panties_leaving14 with dissolve
rs "Well, the house is really for DIKs only, but since you got the panties, I guess-"
scene ep1_panties_leaving15
tm "No! Stop it right there, Rusty. You got the first part right."
tm "This is a DIKs only house, and this guy's neither a DIK, a pledge, or a hot girl."
tm "He may stand there naked with panties, but that cock sticking out between his legs is what's wrong with that."
$ guideSuggestedPage = 42
scene ep1_panties_leaving13 with dissolve
menu:
    "Joke around" if True:
        if dtype > 0:
            $ RPdiks += 1
            scene ep1_panties_leaving17 with dissolve
            mc "Look! Problem solved! Let me in!"
            dikc "HAHA! You like him better now, Tommy?"
            scene ep1_panties_leaving17d with dissolve
            tm "Fuck off! That's just fucking weird..."
        elif True:
            mc "Come on; it's just a dick. We all have them."
    "Get angry" if True:
        mc "For fuck's sake, guys, let me in! I can't walk around buck naked on campus with nowhere to go!"

scene ep1_panties_leaving18 with dissolve
tm "Thanks for the panties! We'll be in touch!"
rs "Sorry, dude... DIK code, you know."
mc "Can I at least get something to wear?"
play sound "sound_effects/door_slam.mp3"
scene ep1_panties_leaving19 with hpunch
$ bios_tommy = True
$ bios_rusty = True
$ bios_jacob = True
$ bios_heather = True
$ bios_name_heather = True
$ bios_nick = True
$ bios_name_nick = True
$ bios_johnboy = True
$ bios_name_johnboy = True
$ bios_elena = True
$ bios_name_elena = True
$ bios_history_tommy += "Tommy left me standing naked outside with nowhere to go.\n\n"
$ bios_history_rusty += "Rusty told me that DIK code prohibited him from helping me.\n\n"
$ bios_history_jacob += "I have no clue who this guy is yet.\n\n"
$ bios_name_tommy = True
$ bios_name_rusty = True
$ bios_name_jacob = True
$ chat_new_bios = True
mc "(I fucking hate college!)"
mc "(What the fuck am I supposed to do now?)"
scene ep1_panties_leaving20 with wipeleft
stop music fadeout 5
mc "(Troy has my other clothes... Quinn has my keys and phone...)"
mc "(I'm screwed...)"
scene ep1_panties_leaving21 with dissolve
mc "(Maybe I just should call for a security guard?)"
mc "(If I only could find one...)"
$ renpy.sound.play("sound_effects/footsteps_outside.mp3", channel="sfx1", loop=False)
"*{i}Footsteps{/i}*"
scene ep1_panties_leaving21b
play sound "sound_effects/car_beep.mp3"
$ renpy.pause(0.5)
scene ep1_panties_leaving21
mc "(Someone's coming! Shit...)"
play music "music/ep1/fresh_air.mp3"
scene ep1_panties_leaving22 with dissolve
mc "(Oh, it's the librarian...what was her name again?)"
mc "(Oh, yeah! Isabella!)"
mc "*{i}Psst{/i}*"
mc "Isabella?"
scene ep1_panties_leaving23 with dissolve

isa "Who's there?"
scene ep1_panties_leaving23b with dissolve
mc "Don't be alarmed...I don't want you to see me like this, but I need your help."
scene ep1_panties_leaving23 with dissolve

isa "What? Who is this?"
scene ep1_panties_leaving26
mc "NO, DON'T!"
scene ep1_panties_leaving27 with dissolve

isa "What the hell, boy! Are you out of your mind!?"
mc "Ouch! Ouch!!!"

isa "Why are you walking around naked outside!?"
scene ep1_panties_leaving29 with dissolve
mc "Please, help me! A HOT girl took my clothes and threw me outside of their sorority house, naked."
mc "My keys were in my pants, and I can't get back to my dorm..."
scene ep1_panties_leaving27 with dissolve

isa "What!?"
scene ep1_panties_leaving29 with dissolve
mc "Please...help me..."
scene ep1_panties_leaving31 with dissolve

isa "Here..."

stop music fadeout 3
isa "Cover yourself up and follow me."
mc "Thank you!"

scene ep1_bella_library with fade

isa "There's no one here at this hour."
mc "Oh, good."
scene ep1_bella_library2 with dissolve

isa "But don't get too comfortable. I'm not interested in seeing your penis again."
scene ep1_bella_library3 with dissolve
menu:
    "Tease her" if True:
        $ dk(1)
        mc "So, you did see it before, huh?"
        $ RPisabella -= 1
        $ bios_history_isabella += "She didn't appreciate my penis joke...\n\n"
        $ bios_name_isabella = True
        $ chat_new_bios = True
        scene ep1_bella_library3b with dissolve
        $ renpy.pause()
    "Don't tease her" if True:
        $ dk(-1)
        $ RPisabella += 1
        mc "Understood."
scene ep1_bella_library4 with dissolve

isa "There's a lost and found back here."

isa "I'm not sure if they will fit, but it's better than wearing nothing."
mc "Really? How do people lose their clothes in here?"
scene ep1_bella_library4b with dissolve

isa "...said the boy standing naked in front of me."
scene ep1_bella_library5 with dissolve
mc "Thank you."

isa "TOWEL!"
scene ep1_bella_library7 with dissolve
mc "Sorry!"
scene ep1_bella_library10 with dissolve
mc "Thank you for the clothes...really..."
mc "..."
mc "Bye..."
scene ep1_bella_library11 with dissolve

isa "Not so fast. Where do you think you're going?"
scene ep1_bella_library12 with dissolve
mc "I thought I would try getting back to my dorm now."
scene ep1_bella_library12b with dissolve

isa "Where are your manners, boy?"
scene ep1_bella_library12 with dissolve
mc "Look, I said I'm sorry and thanked you. What else can I do?"
scene ep1_bella_library15 with dissolve

isa "Over there! Sit!"
scene ep1_bella_library12 with dissolve
mc "Hey, I don't like how you boss me arou-"
scene ep1_bella_library15

isa "NOW!"
scene ep1_bella_library17 with dissolve
mc "..."
scene ep1_bella_library18 with dissolve

isa "Start from the beginning."
scene ep1_bella_library17 with dissolve
mc "The beginning of what?"
scene ep1_bella_library18b with dissolve

isa "Tell me why you ended up in that bush naked, boy."
scene ep1_bella_library17 with dissolve
menu:
    "Stop calling me boy" if True:
        mc "Can you stop calling me boy!? I'm a grown man!"
        scene ep1_bella_library18b with dissolve

        isa "A grown man, you say? Does a grown man sneak into young girls' dorms?"
        scene ep1_bella_library17 with dissolve
        mc "That's not what I was doing in there!"
        scene ep1_bella_library23 with dissolve

        isa "Then tell me what you were doing in there...BOY!"
    "Don't call her out" if True:
        mc "Ok..."
scene ep1_bella_library17 with dissolve
mc "Look, I share a dorm with this asshole named Troy."
mc "I was trying to get along but, thanks to him, the jocks stole my guitar..."
mc "...my father got me that guitar *{i}sobs{/i}*...and now it's gone..."
scene ep1_bella_library18 with dissolve

isa "It's ok. Go on."
scene ep1_bella_library17 with dissolve
mc "I had a falling out with him, and there's just no way I can live with him anymore."
mc "I figured that I could move into a frat house to get away from him."
mc "The tri-betas don't have a house, the jocks hate me, and I'm way too poor to ever be able to join the preppy frat, so I was left with the DIKs."
mc "It was my only option."
mc "They said I would get in if I went to the HOT sorority and stole a pair of panties from them."
scene ep1_bella_library23 with dissolve

isa "You what!?"
mc "Hey, at least let me explain before you scold me!"
scene ep1_bella_library23b with dissolve
isa "..."
scene ep1_bella_library18 with dissolve

isa "Go on."
scene ep1_bella_library17 with dissolve
mc "So, I found the panties and was about to get out of there..."
mc "...but these two girls came into the showers, and I had to hide."
mc "They found me and..."
mc "The details don't matter; they stole my clothes and kicked me out, holding a pair of panties."
scene ep1_bella_library18 with dissolve

isa "They stole your clothes?"
scene ep1_bella_library17 with dissolve
mc "Yes! I'm telling you the truth! I had to walk around campus naked, trying to get back to the DIKs."
mc "And when I got there, they laughed in my face...they even took the panties from me."
mc "There! Go ahead and scold me again!"
scene ep1_bella_library18b with dissolve

isa "Are you some kind of a pervert?"
scene ep1_bella_library17 with dissolve
mc "Great! I'm a pervert. Again!"
scene ep1_bella_library23 with dissolve

isa "What's wrong with you, boy? Didn't your mother ever teach you that you don't go sneaking around in women's showers?"
scene ep1_bella_library23b with dissolve
mc "No!!! She-"
mc "..."
mc "My mother passed away as I was born."
scene ep1_bella_library23c with dissolve
mc "It's just been me and my dad."
mc "And he didn't tell me that..."
mc "...explicitly."
scene ep1_bella_library36 with dissolve

isa "Oh...I...erm..."
isa "..."
scene ep1_bella_library37b with dissolve

isa "Yes, well, that would make quite a difference."
scene ep1_bella_library37 with dissolve
mc "Well, there's not much I can do about that."
scene ep1_bella_library37b with dissolve

isa "You may leave."
scene ep1_bella_library37 with dissolve
mc "Fine..."
scene ep1_bella_library40 with dissolve

isa "That shirt is too small for you."
scene ep1_bella_library41 with dissolve
mc "..."
stop music fadeout 10
mc "Thank you...Isabella."
mc "I'm [name], by the way."
$ bios_history_isabella += "I got to talk more to Isabella today. She helped me get clothes after standing naked outside. She scolded me for my actions, but something tells me that she cared about me more than she let on.\n\n"
$ bios_name_isabella = True
$ chat_new_bios = True
scene ep1_bella_library42 with dissolve
$ renpy.pause()

scene ep1_dorm_aftermath with fade
mc "..."
mc "(Yeah...there's no way I'm going to get back in.)"
play music "music/ep1/your_smile.mp3"
mc "(If I had my phone, I could have called someone...)"
mc "(...you know what?)"
mc "(Fuck this place, I'm going home.)"
scene ep1_dorm_aftermath2 with fade
mc "(I'm not going to stay here. It's obvious that no one gives a fuck about me.)"
mc "(College sucks!)"
mc "(Dad...he'll understand...)"
scene ep1_dorm_aftermath4
mc "(FUCK! My wallet was in my pants!)"
scene ep1_dorm_aftermath5 with dissolve
mc "(NO! I'm so fucking stupid!)"
play sound "sound_effects/running_gravel.mp3"
scene ep1_dorm_aftermath6 with dissolve
sec "Hey, you! Have you seen a naked guy running around here?"
mc "*{i}Gulp{/i}*"
mc "No...or...maybe he went into the parking lot?"
sec "Dammit!"
play sound "sound_effects/bushes.mp3"
scene ep1_dorm_aftermath8 with dissolve
uk "Is he gone?"
play sound "sound_effects/bushes.mp3"
scene ep1_dorm_aftermath10 with dissolve
mc "Huh?"
de "That was a close one."
play sound "sound_effects/bushes.mp3"
scene ep1_dorm_aftermath11 with dissolve
mc "Wait...you're the naked guy?"
de "Yeah! Fucking Quinn stole my clothes!"
scene ep1_dorm_aftermath13 with dissolve
mc "No way! Mine too!"
de "Haha! No way!"
mc "You want some clothes? I have my bag right here."
scene ep1_dorm_aftermath15 with dissolve
de "Nah, I'm good."
de "She fooled both of us, huh?"
scene ep1_dorm_aftermath17 with dissolve
mc "Looks like it..."
scene ep1_dorm_aftermath18 with dissolve
de "Don't worry! We'll get her back."
de "What's up with the bag? Going somewhere?"
scene ep1_dorm_aftermath17 with dissolve
mc "Actually...I was going home."
mc "I've had enough of this place..."
scene ep1_dorm_aftermath18 with dissolve
de "Are you crazy? You're giving up? You just got here!"
scene ep1_dorm_aftermath17 with dissolve
mc "Yeah, but it feels like everyone's against me."
mc "Quinn tricked me, the DIKs fucked me over, the jocks hate me, and I got into a fight with my dorm mate..."
mc "...my former dorm mate, I should say."
scene ep1_dorm_aftermath18 with dissolve
de "So what? You were naked, everyone hates you, and you have no place to stay."
de "That's some cool fucking stories in the making there, bro!"
de "That's the real college experience if you ask me!"
scene ep1_dorm_aftermath23 with dissolve
de "And not everyone hates you. I like you!"
mc "I'd feel much more comfortable if you put on some clothes..."
my "What the fuck are you two doing!?"
scene ep1_dorm_aftermath25 with dissolve
de "Hey! Sis! Come join us!"
my "No way! I'm going!"
mc "Wait, what!? Sis?"
scene ep1_dorm_aftermath25c with dissolve
de "Didn't she tell you?"
mc "...no."
scene ep1_dorm_aftermath25 with dissolve
de "[name] needs your help!"
scene ep1_dorm_aftermath25c with dissolve
mc "*{i}Whispers{/i}*What are you doing?"
de "*{i}Whispers{/i}*Trust me."
scene ep1_dorm_aftermath29 with dissolve
my "Help with what?"
scene ep1_dorm_aftermath25 with dissolve
de "Did that exchange student show up yet, or are you still living alone?"
scene ep1_dorm_aftermath29 with dissolve
my "No, not yet. Why?"
scene ep1_dorm_aftermath25 with dissolve
de "Awesome!"
play sound "sound_effects/shove.mp3"
scene ep1_dorm_aftermath32 with vpunch
de "Meet your new roommate!"
scene ep1_dorm_aftermath31 with dissolve
my "My new what?"
scene ep1_dorm_aftermath33 with dissolve
de "He needs a place to stay, and you need someone to share your dorm with!"
scene ep1_dorm_aftermath31 with dissolve
my "No, I don't {b}need{/b} someone to share my dorm with."
my "You can share your dorm with him!"
scene ep1_dorm_aftermath35 with dissolve
de "Come on! You fucking owe me, and you know it!"
scene ep1_dorm_aftermath36 with dissolve
my "This again?"
scene ep1_dorm_aftermath35 with dissolve
de "After this, we're even."
scene ep1_dorm_aftermath36 with dissolve
my "Only for one night..."
scene ep1_dorm_aftermath35 with dissolve
de "For one night!?"
scene ep1_dorm_aftermath38
de "No way!"
scene ep1_dorm_aftermath36b
my "Put some fucking clothes on, Derek!!!"
scene ep1_dorm_aftermath39 with dissolve
mc "I'll take it."
scene ep1_dorm_aftermath40 with dissolve
my "Deal!"
scene ep1_dorm_aftermath41 with dissolve
de "Dude! I would have gotten you months!"
scene ep1_dorm_aftermath40b with dissolve
my "The deal is done, Derek."
scene ep1_dorm_aftermath40c with dissolve
stop music fadeout 3
my "Ok, [name]. Follow me. I can sneak you in through the window."

scene ep1_maya_dorm with wiperight
mc "Hngh..."
scene ep1_maya_dorm1 with dissolve
mc "There! Thanks!"
my "Hahaha!"
mc "Why are you laughing?"
play music "music/ep1/trow.mp3"
scene ep1_maya_dorm3 with dissolve
my "I was just fucking with you about the window. No one cares if you go through the door."
scene ep1_maya_dorm4 with dissolve
menu:
    "Laugh" if True:
        $ dk(-1)
        $ RPmaya += 1
        mc "Oh, haha!"
    "Get annoyed" if True:
        $ dk(1)
        mc "That's not funny! That's just mean."
scene ep1_maya_dorm5 with dissolve
my "Sorry."
play sound "sound_effects/switch.mp3"
scene ep1_maya_dorm5b
my "Anyway, welcome to my dorm."
scene ep1_maya_dorm6 with dissolve
mc "This dorm is a lot nicer than my old one."
scene ep1_maya_dorm7 with dissolve
my "Make yourself at home..."
my "You know...for the night."
$ guideSuggestedPage = 43
$ bios_history_derek +="Derek was tricked by Quinn too. He convinced Maya to share her dorm with me.\n\nI found out that Derek and Maya are siblings.\n\n"
$ bios_history_maya +="Maya agreed to share her dorm with me for the night. Derek called in a favor that she owed him.\n\nI found out that Derek and Maya are siblings.\n\n"
$ bios_name_derek = True
$ bios_name_maya = True
$ chat_new_bios = True
jump ep1_freeroam_maya_label

label ep1_maya_freeroam_sleep_label:
$ renpy.block_rollback()
$ phone_call_enabled = False
$ chat_new_tasks = False
$ loopMusic = False
stop music fadeout 3

scene ep1_frmdorm_sleep with dissolve
my "Wanna go to bed?"
scene ep1_frmdorm_sleepb with dissolve
play music "music/ep1/fresh_air.mp3"
menu:
    "Sure" if True:
        mc "Sure, I'm pretty tired..."
    "Together?" if True:
        if dtype > 0:
            $ dk(1)
            mc "Together with you? Of course."
            scene ep1_frmdorm_sleep2 with dissolve
            my "You really need to work on your flirting skills. That just comes off as sleazy."
        elif True:
            $ dk(-1)
            mc "What? Not together, right?"
            scene ep1_frmdorm_sleep3 with dissolve
            my "Haha! No, stupid."
        scene ep1_frmdorm_sleep4 with dissolve
        my "To clarify, I'm sleeping over there..."
        scene ep1_frmdorm_sleep5 with dissolve
        my "And you're sleeping all the way over there."
        mc "Haha, ok."
scene ep1_maya_dorm5b with dissolve
$ renpy.pause(0.5)
play sound "sound_effects/switch.mp3"
scene ep1_maya_dorm5
$ renpy.pause(2)
scene ep1_frmdorm_sleep7 with dissolve
my "Now turn around and close your eyes."
scene ep1_frmdorm_sleep7b with dissolve
mc "What for?"
scene ep1_frmdorm_sleep7 with dissolve
my "Because I need to change, and I don't need you staring at me."
if dtype > 0:
    scene ep1_frmdorm_sleep7b with dissolve
    mc "You're no fun..."
elif True:
    $ RPmaya += 1
    scene ep1_frmdorm_sleep7b with dissolve
    mc "Is that what you think of me? That I would stare?"
    scene ep1_frmdorm_sleep12b with dissolve
    my "No...I..."
    my "Sorry. You've been nothing but nice."
    my "I just meant that I would be more comfortable that way."
    scene ep1_frmdorm_sleep12 with dissolve
    mc "Of course, I'll turn around."

scene ep1_frmdorm_sleep15 with dissolve
menu:
    "Sneak a peek ({color=#ffffff}{size=-1}{font=collegiate.ttf}DIK{/font}{/size}{/color})" if dtype > 0:
        scene ep1_frmdorm_sleep16 with dissolve
        mc "(Fuck me...)"
        scene ep1_frmdorm_sleep17 with dissolve
        $ renpy.pause()
        menu:
            "Closer look at ass" if True:
                scene ep1_frmdorm_sleep17c with dissolve
                $ renpy.pause()
                scene ep1_frmdorm_sleep17b with dissolve
                $ renpy.pause()
            "Closer look at tits" if True:
                scene ep1_frmdorm_sleep17d with dissolve
                $ renpy.pause()
                scene ep1_frmdorm_sleep17e with dissolve
                $ renpy.pause()
        scene ep1_frmdorm_sleep15 with dissolve
        mc "(Ok...that's enough...)"
        my "Ok! I'm ready."
    "Wait until she's done" if True:
        my "Ok! I'm ready."
$ guideSuggestedPage = 44
scene ep1_frmdorm_sleep18 with dissolve
menu:
    "Compliment her" if True:
        if dtype > 0:
            mc "You look hot in that."
            scene ep1_frmdorm_sleep18b with dissolve
            my "Thanks. I guess."
            scene ep1_frmdorm_sleep18 with dissolve
        elif True:
            $ RPmaya += 1
            mc "That's very beautiful on you."
            scene ep1_frmdorm_sleep18c with dissolve
            my "[name]..."
            scene ep1_frmdorm_sleep18 with dissolve
    "Don't compliment her" if True:
        mc "Great!"
mc "My turn!"

scene ep1_frmdorm_sleep18d with dissolve
my "Haha, all right."
scene ep1_frmdorm_sleep18 with dissolve
menu:
    "Ask her to turn around" if True:
        mc "I think it's your turn to turn around, Maya..."
        if dtype > 0:
            scene ep1_frmdorm_sleep20b with dissolve
            my "Now who's the fun one?"
        elif True:
            scene ep1_frmdorm_sleep20c with dissolve
            my "Oh, of course!"
        scene ep1_frmdorm_sleep21 with dissolve
        menu:
            "Check her out" if True:
                scene ep1_frmdorm_sleep21b with dissolve
                $ renpy.pause()
            "Don't risk it" if True:
                $ renpy.pause(0.5)
        play sound "sound_effects/clothes.mp3"
    "Undress while she looks" if True:
        play sound "sound_effects/clothes.mp3"
        scene ep1_frmdorm_sleep22 with dissolve
        my "Haha! Whoa!"
        my "I thought you would ask me to turn around!"
        scene ep1_frmdorm_sleep23 with dissolve
        if dtype > 0:
            mc "It's ok. I'm not ashamed of my body."
        elif True:
            mc "Oh... Well, it doesn't matter to me."
        scene ep1_frmdorm_sleep24 with dissolve
        my "Haha, you'll have to teach me how to be that comfortable with myself some time."
        if dtype < 0:
            $ RPmaya += 1
            scene ep1_frmdorm_sleep25 with dissolve
            mc "Well, you should feel comfortable with your body."
            mc "You're beautiful."
            scene ep1_frmdorm_sleep26 with dissolve
            my "[name]..."
scene ep1_frmdorm_sleep27 with dissolve
my "Good night, [name]."
mc "Good night. Thank you for letting me stay here tonight."
my "No worries. Hope you'll dream sweet dreams."
scene ep1_frmdorm_sleep29 with dissolve
stop music fadeout 3
mc "(I hope so too...)"
scene black with fade
$ phone_clear_jump_label = "ep1_sleep_after_maya_freeroam_label"
jump clear_phone_chat

label ep1_sleep_after_maya_freeroam_label:
if preferredmilf == 0:
    label ep1_jade_lewd2:
    if _in_replay:
        $ currentEpisode = 1
        $ preferredmilf = 0
        if persistent.name == None:
            $ name = "MC"
        elif True:
            $ name = persistent.name
        if persistent.mc_jade == None:
            $ mc_jade = name
        elif True:
            $ mc_jade = persistent.mc_jade
        if persistent.jade == None:
            $ jade = "Jade"
        elif True:
            $ jade = persistent.jade
    hide screen phone_screen
    play music "music/ep1/slow_day_blues.mp3"
    scene ep1_jade_dream2 with Fade(1.5, 1, 0.5)
    ja "Hey, [mc_jade]..."
    scene ep1_jade_dream3 with dissolve
    mc "Oh! Jade! It's you again..."
    scene ep1_jade_dream2 with dissolve
    ja "Yeah, it's me again...why did you leave me so early last time?"
    scene ep1_jade_dream with dissolve
    mc "I had to wake up..."
    mc "...but not this time, though!"
    scene ep1_jade_dream1 with dissolve
    ja "Is that so? Let's take it from the beginning, then..."
    scene ep1_jade_dream2 with dissolve
    ja "Because [jade] is here for you now, [mc_jade]..."
    ja "Let me take care of you..."
    image anim_jade_boobjob1_ep1b = Movie(channel="anim_jade_boobjob1_ep1", play="images/movies/ep1/anim_jade_boobjob1_ep1.webm")
    scene anim_jade_boobjob1_ep1b with dissolve:
        size (config.screen_width, config.screen_height)
    ja "Did you miss my soft breasts, [mc_jade]?"
    mc "Mmm...I did..."
    pause
    image anim_jade_boobjob2_ep1b = Movie(channel="anim_jade_boobjob2_ep1", play="images/movies/ep1/anim_jade_boobjob2_ep1.webm")
    scene anim_jade_boobjob2_ep1b with dissolve:
        size (config.screen_width, config.screen_height)
    pause
    ja "Your cock is so hard, [mc_jade]..."
    image anim_jade_boobjob1_ep1c = Movie(channel="anim_jade_boobjob1_ep1", play="images/movies/ep1/anim_jade_boobjob1_ep1.webm")
    scene anim_jade_boobjob1_ep1c with dissolve:
        size (config.screen_width, config.screen_height)
    pause
    ja "What's the matter, [mc_jade]?"
    ja "You look a bit skeptical..."
    ja "Are you good?"
    mc "..."
    mc "Yes! I think I am good this time!"
    scene ep1_jade_dream5 with dissolve
    ja "That's great to hear..."
    ja "Because all I want right now..."
    ja "Is you [mc_jade]..."
    scene ep1_jade_dream_6 with dissolve
    ja "...and to have that big fat cock between your legs rubbing against my wet pussy."
    ja "Mmm...can you feel how warm my pussy is against your dick?"
    mc "Yeah...I almost wished you didn't have panties for this..."
    scene ep1_jade_dream5 with dissolve
    ja "I can arrange that...it's a dream after all..."
    scene ep1_jade_dream7 with dissolve
    ja "Mmm...good choice..."
    ja "This feels so much better."
    scene ep1_jade_dream8 with dissolve
    mc "Wow, you're squeezing it just right, [jade]..."
    scene ep1_jade_dream9 with dissolve
    ja "You're loving this, aren't you?"
    mc "Yes, [jade]..."
    scene ep1_jade_dream10 with dissolve
    ja "So...what are you waiting for?"
    mc "What?"
    scene ep1_jade_dream11 with dissolve
    ja "Get your hips moving..."
    ja "It's time to get you off for real, [mc_jade]..."
    image anim_jade_assjob1_ep1b = Movie(channel="anim_jade_assjob2_ep1b", play="images/movies/ep1/anim_jade_assjob1_ep1.webm")
    scene anim_jade_assjob1_ep1b with dissolve:
        size (config.screen_width, config.screen_height)
    pause
    ja "Oh, yes!!! Just like that!"
    image anim_jade_assjob2_ep2b = Movie(channel="anim_jade_assjob2_ep2b", play="images/movies/ep1/anim_jade_assjob2_ep1.webm")
    scene anim_jade_assjob2_ep2b with dissolve:
        size (config.screen_width, config.screen_height)
    pause
    ja "I'm soaking wet, [mc_jade]..."
    ja "Keep moving those hips..."
    ja "I might actually be able to cum..."
    image anim_jade_assjob3_ep3b = Movie(channel="anim_jade_assjob3b_ep1", play="images/movies/ep1/anim_jade_assjob3_ep1.webm")
    scene anim_jade_assjob3_ep3b with dissolve:
        size (config.screen_width, config.screen_height)
    pause
    ja "...no man has ever made me cum..."
    mc "Really?"
    ja "..."
    ja "Sure."
    image anim_jade_assjob4_ep1 = Movie(channel="anim_jade_assjob4_ep1", play="images/movies/ep1/anim_jade_assjob4_ep1.webm")
    scene anim_jade_assjob4_ep1 with dissolve:
        size (config.screen_width, config.screen_height)
    pause
    ja "Feel how my huge tits bounce on your chest..."
    mc "Your tits are so big and soft, [jade]."
    image anim_jade_assjob5_ep1 = Movie(channel="anim_jade_assjob5_ep1", play="images/movies/ep1/anim_jade_assjob5_ep1.webm")
    scene anim_jade_assjob5_ep1 with dissolve:
        size (config.screen_width, config.screen_height)
    pause
    ja "And your cock is so big and hard, [mc_jade]."
    ja "Are you getting close?"
    mc "I don't know...maybe..."
    ja "Take as long as you need..."
    $ currentSexLabel = "ep1_jade_lewd2b"
    $ lewd_jade_phase = 1
    jump jade_sex_scene_loop
    label ep1_jade_lewd2b:
    ja "Mmm...that was amazing, [mc_jade]!"
    stop music fadeout 3
    ja "I'll see you soon again, in your dreams..."
    $ persistent.ep1_jade_dream2 = True
    $ renpy.end_replay()
    $ calcScenes()
    $ bios_history_jade += "I had another sexy dream about Jade. This time it ended much better than the first one.\n\n"
    $ bios_name_jade = True
    $ chat_new_bios = True
elif True:
    label ep1_cathy_lewd2:
    if _in_replay:
        $ currentEpisode = 1
        $ preferredmilf = 1
        if persistent.name == None:
            $ name = "MC"
        elif True:
            $ name = persistent.name
        if persistent.mc_cathy == None:
            $ mc_cathy = name
        elif True:
            $ mc_cathy = persistent.mc_cathy
        if persistent.cathy == None:
            $ cathy = "Cathy"
        elif True:
            $ cathy = persistent.cathy
    hide screen phone_screen
    play music "music/ep1/slow_day_blues.mp3"
    scene ep1_d2_wakeb with Fade(1.5, 1, 0.5)
    ca "You really don't know shit!"
    ca "Can't you spell the word endocytosis?"
    if failedEnglish == 0:
        mc "But I do know how to spell it!"
        mc "Oh...yeah, this is another dream..."
    scene ep1_d2_wake1b with dissolve
    ca "I feel like I should be teaching you how to spell simpler words."
    ca "What about ball? B-A-L-L!"
    scene ep1_d2_wake2b with dissolve
    ca "Hello! It's a noun! Something you can play with."
    scene ep1_d2_wake1b with dissolve
    ca "No, not your BALLS!"
    scene ep1_d2_wake3b2 with dissolve
    ca "Would you want that? For me to play with your balls?"
    ca "With your dick, too!?"
    ca "If that's what it will take for you to stay awake in class...FINE!"
    image anim_cathy_hj_ep1 = Movie(channel="anim_cathy_hj_ep1", play="images/movies/ep1/anim_cathy_hj_ep1.webm")
    scene anim_cathy_hj_ep1 with dissolve:
        size (config.screen_width, config.screen_height)
    ca "This is ridiculous. Never have I had a student as bad as you!"
    pause
    image anim_cathy_hj2_ep1 = Movie(channel="anim_cathy_hj2_ep1", play="images/movies/ep1/anim_cathy_hj2_ep1.webm")
    scene anim_cathy_hj2_ep1 with dissolve:
        size (config.screen_width, config.screen_height)
    ca "I seem to have gotten your attention now, haven't I?"
    ca "Oh yes! I definitely have your full attention!"
    pause
    scene ep1_d2_wake3b3 with dissolve
    ca "Are you going to behave in class, [mc_cathy]? Or will I have to do this every day!?"
    image anim_cathy_hj_ep1 = Movie(channel="anim_cathy_hj_ep1", play="images/movies/ep1/anim_cathy_hj_ep1.webm")
    scene anim_cathy_hj_ep1 with dissolve:
        size (config.screen_width, config.screen_height)
    ca "You like this, don't you?"
    ca "Having your teacher jack you off?"
    mc "Yes, [cathy]..."
    pause
    scene ep1_d2_wake3b4 with dissolve
    ca "All that cum in your cock must be making you stupid!"
    image anim_cathy_hj3_ep1 = Movie(channel="anim_cathy_hj3_ep1", play="images/movies/ep1/anim_cathy_hj3_ep1.webm")
    scene anim_cathy_hj3_ep1 with dissolve:
        size (config.screen_width, config.screen_height)
    ca "I'll get all of it out for you..."
    ca "...every single drop..."
    mc "Faster, [cathy]...please..."
    pause
    image anim_cathy_hj_fast_ep1 = Movie(channel="anim_cathy_hj_fast_ep1", play="images/movies/ep1/anim_cathy_hj_fast_ep1.webm")
    scene anim_cathy_hj_fast_ep1 with dissolve:
        size (config.screen_width, config.screen_height)
    ca "Faster, he says... Who do you think you are?"
    pause
    image anim_cathy_hj2_fast_ep1 = Movie(channel="anim_cathy_hj2_fast_ep1", play="images/movies/ep1/anim_cathy_hj2_fast_ep1.webm")
    scene anim_cathy_hj2_fast_ep1 with dissolve:
        size (config.screen_width, config.screen_height)
    ca "I'm the one in charge here, [mc_cathy]."
    pause
    scene ep1_d2_wake3b6 with dissolve
    ca "Did you hear what I just said?"
    mc "Yes, [cathy]...please don't stop now..."
    image anim_cathy_hj3_fast_ep1 = Movie(channel="anim_cathy_hj3_fast_ep1", play="images/movies/ep1/anim_cathy_hj3_fast_ep1.webm")
    scene anim_cathy_hj3_fast_ep1 with dissolve:
        size (config.screen_width, config.screen_height)
    pause
    ca "Are you going to cum soon or what!?"
    $ currentSexLabel = "ep1_cathy_lewd2b"
    $ lewd_cathy_phase = 1
    jump cathy_sex_scene_loop
    label ep1_cathy_lewd2b:
    ca "About time! I hope that you will stay awake in class from now on..."
    stop music fadeout 3
    ca "...or I will have to come visit you in your dreams again."
    $ persistent.ep1_cathy_dream2 = True
    $ renpy.end_replay()
    $ calcScenes()
    $ bios_history_cathy += "I had another sexy dream about Cathy. This time it ended much better than the first one.\n\n"
    $ bios_name_cathy = True
    $ chat_new_bios = True

scene black with fade
my "Erm...good morning, [name]."
play music "music/ep1/winter_sunshine.mp3"
scene ep1_maya_morning with fade
mc "*{i}Yawns{/i}* Good morning..."
my "So...uh...did you sleep well?"
mc "Yeah, I slept really well."
scene ep1_maya_morning1 with dissolve
my "Did you dream about...anything in particular?"
scene ep1_maya_morning2b with dissolve
mc "Erm...why do you ask?"
scene ep1_maya_morning3
mc "Oh, shit!"
scene ep1_maya_morning with dissolve
mc "Sorry! I don't know what to say..."
my "Don't worry. These things happen."
scene ep1_maya_morning1 with dissolve
my "Listen, I'm going out for a run before classes."
my "It was nice having a roommate for the evening."
scene ep1_maya_morning4 with dissolve
mc "Thank you for letting me stay here, Maya."
my "No worries."
my "I hope that everything gets sorted for you today."
scene ep1_maya_morning5 with dissolve
stop music fadeout 3
mc "(Me too.)"
mc "(And I know just where to start.)"

scene ep1_quinn_confront with wiperight
play music "music/ep1/classicals_breakbeat.mp3"
mc "Hey!!! Quinn!"
scene ep1_quinn_confront1 with dissolve
qu "What's up, perv boy?"
qu "I almost didn't recognize you with clothes."
scene ep1_quinn_confront2 with dissolve
menu:
    "Hostile approach" if True:
        $ dk(1)
        mc "Stop fucking with me! Give me back my clothes, wallet and phone!"
    "Calm approach" if True:
        $ dk(-1)
        mc "Speaking of clothes. Can I have mine back? My phone and wallet were in there."
scene ep1_quinn_confront1 with dissolve
qu "Oh, yeah! That's right; there was a phone in there."
qu "Who's Josy?"
scene ep1_quinn_confront2 with dissolve
mc "What?"
scene ep1_quinn_confront3 with dissolve
qu "She called last night; we ended up chatting."
scene ep1_quinn_confront5b with dissolve
mc "Bullshit."
scene ep1_quinn_confront5 with dissolve
qu "Hah! You should have heard the quaver in her voice when she thought I was your booty call."
scene ep1_quinn_confront5b with dissolve
menu:
    "Hostile approach" if True:
        $ dk(1)
        scene ep1_quinn_confront6 with dissolve
        mc "Not funny! Give it back!"
        scene ep1_quinn_confront6b with dissolve
        qu "Oh! Perv boy got some anger issues. I like it."
    "Calm approach" if True:
        $ dk(-1)
        mc "Ok, you had your fun. Please, give it back now."
scene ep1_quinn_confront5 with dissolve
qu "You'll have to talk with Sage. I got bored with it."
scene ep1_quinn_confront8 with dissolve
stop music fadeout 3
qu "Go on in. I'm sure you're familiar with our house already, pervert."
$ bios_history_quinn += "Quinn gave my belongings to Sage.\n\n"
$ bios_name_quinn = True
$ chat_new_bios = True

play music "music/ep1/funk_rock.mp3"
scene ep1_quinn_confront9 with dissolve
mc "Sage!"
scene ep1_quinn_confront10 with dissolve
sa "Ah! I knew you would come, eventually."
sa "Follow me."
scene ep1_quinn_confront11 with dissolve
sa "Ok, we can talk in here."
sa "So, did you think about my proposition, yet?"
scene ep1_quinn_confront12 with dissolve
mc "That's not why I'm here."
mc "Give me my belongings back."
scene ep1_quinn_confront12b with dissolve
sa "Your belongings?"
scene ep1_quinn_confront12c with dissolve
mc "Yes! My clothes, wallet and phone..."
scene ep1_quinn_confront24 with dissolve
mc "...AND MY GUITAR!"
scene ep1_quinn_confront12 with dissolve
mc "You're the one who stole it!!!"
scene ep1_quinn_confront17 with dissolve
sa "Hey! Calm the fuck down!"
sa "That's my guitar. It was a gift."
scene ep1_quinn_confront18 with dissolve
mc "A gift? What!?"
mc "Just... Please. Give it back to me."
scene ep1_quinn_confront18b with dissolve
sa "What's it worth to you?"
scene ep1_quinn_confront18 with dissolve
mc "What?"
scene ep1_quinn_confront18b with dissolve
sa "Will you spy on Chad for me?"
scene ep1_quinn_confront18 with dissolve
mc "..."
mc "Ok... I will help you with Chad. Can I have it back?"
scene ep1_quinn_confront22 with dissolve
sa "Proof first. Guitar later."
scene ep1_quinn_confront12 with dissolve
mc "Please, Sage... I need it."
mc "My dad bought that for my 12th birthday..."
mc "I don't think you understand how much it means to me..."
sa "..."
scene ep1_quinn_confront12b with dissolve
sa "You still promise to help me?"
scene ep1_quinn_confront12 with dissolve
mc "I do."
scene ep1_quinn_confront12b with dissolve
sa "Ok... Take it."
scene ep1_quinn_confront12 with dissolve
mc "What about the rest of my stuff?"
scene ep1_quinn_confront15 with dissolve
sa "Sure..."
menu:
    "Look closer" if True:
        $ dk(1)
        scene ep1_quinn_confront15b with dissolve
        $ renpy.pause()
    "Don't risk it" if True:
        $ dk(-1)
scene ep1_quinn_confront15c with dissolve
sa "Here. I didn't know they were yours."
$ updateDikScore()
show screen scoremsg
$ ui.imagebutton("phone_btn_alert", "phone_btn_alert", clicked=ui.returns("OK"), xalign=0.02, yalign=0.02)
if notifications:
    play sound "sound_effects/message.mp3"
$ renpy.pause(2)
hide screen scoremsg
show screen phone_screen
sa "Quinn gave them to me, saying that she confiscated them from a pervert..."
scene ep1_quinn_confront12c with dissolve
mc "That was me."
scene ep1_quinn_confront12b with dissolve
sa "You're the pervert?"
scene ep1_quinn_confront12 with dissolve
mc "I'm not a pervert!"
scene ep1_quinn_confront29 with dissolve
sa "Hey..."
mc "What?"
scene ep1_quinn_confront30 with dissolve
stop music fadeout 3
sa "Call me when you know more about the bitch Chad is fucking."
$ bios_history_sage += "Sage had my guitar, but she gave it back to me. She wants me to find proof on who Chad is fucking behind her back.\n\n"
$ number_sage = True
$ bios_name_sage = True
$ chat_new_bios = True

scene ep1_quinn_confront31 with dissolve
play music "music/ep1/classicals_breakbeat.mp3"
qu "Wow, she gave you your things back? She must really like you."
if dtype >  0:
    mc "Fuck you."
elif True:
    mc "..."
scene ep1_quinn_confront32 with dissolve
qu "Hey, hold up."
mc "What is it?"
scene ep1_quinn_confront34b with dissolve
qu "I'm not going to say I'm sorry, because I'm not. What you did was a fucking scumbag thing to do."
mc "But I-"
scene ep1_quinn_confront35 with dissolve
qu "Shh!"
scene ep1_quinn_confront34 with dissolve
qu "I like to fuck with people. Some like that, some don't."
qu "So, no harsh feelings?"
scene ep1_quinn_confront36 with dissolve
menu:
    "No harsh feelings" if True:
        $ dk(-1)
        mc "No harsh feelings..."
    "Don't accept apology" if True:
        $ dk(1)
        mc "You'll have to do better than that."
scene ep1_quinn_confront34 with dissolve
qu "You're a single guy, right?"
scene ep1_quinn_confront36 with dissolve
mc "What if I am?"
scene ep1_quinn_confront39 with dissolve
$ guideSuggestedPage = 45
qu "Yeah, you're a single guy."
qu "Do you get laid a lot?"
scene ep1_quinn_confront36 with dissolve
menu:
    "Yes" if True:
        $ dk(1)
        if dtype > 1:
            mc "Of course. You interested?"
            scene ep1_quinn_confront34 with dissolve
            qu "Hah. Maybe."
        elif True:
            mc "Yes, I do."
            scene ep1_quinn_confront34b with dissolve
            qu "That was a lie."
    "No" if True:
        $ dk(-1)
        mc "No, I don't."
        scene ep1_quinn_confront34b with dissolve
        qu "Really? Not even gonna lie about it?"
    "None of your business" if True:
        mc "That's really none of your business."
        scene ep1_quinn_confront34b with dissolve
        qu "Ok, that's a no."
        qu "And it's kind of my business..."
scene ep1_quinn_confront40 with dissolve
qu "What if I told you that there was a way for you to {i}have some fun{/i} in a noncommittal way?"
scene ep1_quinn_confront41 with dissolve
mc "What are you getting at?"
scene ep1_quinn_confront42 with dissolve
qu "I'm saying that I...erm..."
scene ep1_quinn_confront40 with dissolve
qu "Let's say you're hungry, but you don't want to cook the food yourself. What would you do?"
scene ep1_quinn_confront41 with dissolve
mc "Go buy food or order take out."
scene ep1_quinn_confront43 with dissolve
qu "Ah! Exactly. Take out."
qu "What I'm saying is that you can think of me as a {i}fast-food restaurant{/i}."
qu "Just call me and order some food and I'll get it for you."
scene ep1_quinn_confront40 with dissolve
qu "My menu, for the time being, consists of {i}Japanese{/i} or {i}Spicy{/i} food."
qu "It costs a bit, but most customers are very satisfied."
qu "Catch my drift?"
scene ep1_quinn_confront41 with dissolve
mc "I think I do."
scene ep1_quinn_confront40 with dissolve
qu "So? You want the number to my restaurant or not?"
scene ep1_quinn_confront36 with dissolve
show screen majorChoiceScale
menu:
    "Accept her offer" if True:
        $ bios_history_mc += "I accepted Quinn's offer to buy \"food\" from her.\n\n"
        $ bios_history_quinn += "I accepted Quinn's offer to buy \"food\" from her.\n\n"
        $ bios_name_quinn = True
        $ chat_new_bios = True
        $ ep1_accepted_quinn_offer = True
        $ addCPenalty()
        $ renpy.pause(1)
        mc "Sure."
        hide screen majorChoiceScale
        scene ep1_quinn_confront46 with dissolve
        qu "Here you go."
        $ number_quinn = True
        qu "FYI. You pick up your food in the corner booth of the bathroom next to dorms 72 and 73."
    "Reject her offer" if True:
        $ bios_history_mc += "I rejected Quinn's offer to buy sexual favors through her.\n\n"
        $ bios_history_quinn += "I rejected Quinn's offer to buy sexual favors through her.\n\n"
        $ ep1_accepted_quinn_offer = False
        $ bios_name_quinn = True
        $ chat_new_bios = True
        $ addDPenalty()
        $ renpy.pause(1)
        mc "No, I don't pay for sex, Quinn! What the hell is the matter with you!?"
        hide screen majorChoiceScale
scene ep1_quinn_confront47 with dissolve
stop music fadeout 3
qu "Bye, pervert!"

scene ep1_lib_thank0 with wiperight
$ renpy.sound.play("sound_effects/library_ambience.mp3", channel="sfx1", loop=True)
sb "Well, that settles it. Friday night it is."
sb "If you don't mind, you can bring a bottle of wine."
if preferredmilf == 0:
    mc "(Jade...)"
    mc "*{i}Gulp{/i}*"
scene ep1_lib_thank1 with dissolve
sb "Ah, enough chatting. We're keeping you from customers."
scene ep1_lib_thank2 with dissolve
sb "Hey there, sport."
menu:
    "Say hey" if True:
        $ dk(-1)
        mc "Hi."
    "Retort" if True:
        $ dk(1)
        if dtype > 0:
            mc "What's up, gramps?"
        elif True:
            mc "Sport? I'm not a kid, mister."
        scene ep1_lib_thank3 with dissolve
        sb "Ah..."
$ bios_burke = True
$ bios_history_burke = "I saw him chat with Jade and Isabella.\n\n"
$ bios_history_jade = "Call me crazy, but I think Jade checked me out in the library!\n\n"
$ bios_name_burke = True
$ bios_jade = True
$ bios_name_jade = True
$ chat_new_bios = True
scene ep1_lib_thank4 with dissolve

isa "Yes?"
scene ep1_lib_thank5 with dissolve
menu:
    "Joke" if True:
        mc "That's not how you start a conversation."
        scene ep1_lib_thank6 with dissolve
        mc "Where are your manners, woman?"
        mc "...you know..."
        mc "...because you told me that yesterday, remember?"
    "Say hey" if True:
        mc "Hi, Isabella."
scene ep1_lib_thank4 with dissolve

isa "What do you need?"
scene ep1_lib_thank5 with dissolve
mc "I don't need anything, really."
mc "I came to thank you for helping me yesterday and to say that I'm sorry for the way I behaved."
mc "I got my belongings back..."
scene ep1_lib_thank4 with dissolve

isa "Ok. Anything else?"
scene ep1_lib_thank5 with dissolve
mc "No...I...ah..."
mc "..."
mc "No. Nothing else."
mc "Bye, Isabella."
scene ep1_lib_thank6b with dissolve
mc "(It doesn't feel like she accepted my apology...)"
mc "(Maybe I can help her around here somehow?)"
scene ep1_lib_thank7 with dissolve
mc "(That book cart is full.)"
scene ep1_lib_thank8 with wiperight
if dtype > 0:
    mc "(Back into the shelves you go...)"
elif True:
    mc "(The good old Dewey Decimal system...)"
scene ep1_lib_thank8b with dissolve
mc "(The myth of the male orgasm...)"
mc "(Who would write this, let alone read it?)"
scene ep1_lib_thank10 with wiperight
mc "(There. All done.)"
scene ep1_lib_thank11 with dissolve
mc "(Hey...isn't that Jill?)"
mc "(She's here all alone? This could be my chance to talk to her some more.)"
scene ep1_lib_thank12 with dissolve
mc "Hey! Jill, was it? Mind if I sit down?"
scene ep1_lib_thank12b with dissolve

ji "Please, go ahead."
scene ep1_lib_thank14 with dissolve
if dtype > 0:
    mc "Are you reading?"
    scene ep1_lib_thank15 with dissolve

    ji "Yeah, that's mostly what people do in a library."
elif True:
    $ RPjill += 1
    mc "I don't want to bother you if you're busy studying."
    scene ep1_lib_thank15 with dissolve

    ji "It's fine. Really. Although..."
scene ep1_lib_thank16 with dissolve

ji "We're not supposed to be talking in here, you know."
scene ep1_lib_thank14 with dissolve
mc "Oh, it's cool. Me and Isabella are friends now. I'm sure she doesn't mind us chatting."
scene ep1_lib_thank16 with dissolve

ji "Is that so?"
scene ep1_lib_thank14 with dissolve
mc "Yup."
scene ep1_lib_thank16b with dissolve

ji "If you really were friends, you would know that she prefers to be called Bella and that she absolutely still would mind you talking in here..."

ji "...friend or not."
scene ep1_lib_thank14 with dissolve
mc "Oh... So, you're her friend, then."
scene ep1_lib_thank16 with dissolve

ji "Yup."
scene ep1_lib_thank14 with dissolve
if dtype > 0:
    mc "Ok. I'll leave you to it."
elif True:
    mc "Ok. I'm sorry. I'll leave you to it."
scene ep1_lib_thank15 with dissolve

ji "Wait. You don't have to go."

ji "I'm sure she won't mind, as long as we keep our voices down."
scene ep1_lib_thank14 with dissolve
mc "*{i}Inaudible whisper{/i}*"

scene ep1_lib_thank15 with dissolve

ji "What?"
scene ep1_lib_thank14 with dissolve
menu:
    "Whisper again" if True:
        mc "*{i}Inaudible whisper{/i}*"
        scene ep1_lib_thank15 with dissolve
        $ guideSuggestedPage = 46
        ji "Come sit down over here. I can't hear you."
    "Sit down closer to her" if True:
        mc "Let me sit closer to you so you can hear me."
        scene ep1_lib_thank19 with dissolve
        $ guideSuggestedPage = 46
        ji "Smooth move..."
        scene ep1_lib_thank19b with dissolve
        menu:
            "Thanks" if True:
                $ RPjill -= 1
                mc "Thanks."
            "It wasn't a move" if True:
                mc "Oh, that wasn't a move."

scene ep1_lib_thank21 with dissolve
mc "Do you come here often?"
scene ep1_lib_thank22 with dissolve

ji "As a matter of fact, I do. This is the only place where I get to be truly alone."
scene ep1_lib_thank21 with dissolve
mc "And here I am ruining that moment for you."
scene ep1_lib_thank22b with dissolve

ji "I didn't mean it like that."

ji "How can I explain it?"
ji "..."

ji "Ah, never mind. I just like this place a lot."

ji "It's much more cozy and comfortable than the library in the Alpha Nu Omega mansion, too."
scene ep1_lib_thank21 with dissolve
mc "Wow, they even have their own library in there?"
scene ep1_lib_thank22 with dissolve

ji "Yeah."
scene ep1_lib_thank22c with dissolve

ji "So...I hope you've been doing okay since last time."
scene ep1_lib_thank21 with dissolve
mc "Ah, I'm guessing you're alluding to the wedgie?"
mc "There've been some minor wardrobe malfunctions, but overall...I'm ok."
scene ep1_lib_thank22 with dissolve

ji "You seem to take it pretty well..."
scene ep1_lib_thank22c with dissolve

ji "I don't want to pry, but...that's not the first time you've dealt with bullies, huh?"
scene ep1_lib_thank21 with dissolve
mc "Erm...I-"
scene ep1_lib_thank25 with dissolve
mc "H-Hey Bella!"
scene ep1_lib_thank26 with dissolve

isa "Bella?"
scene ep1_lib_thank26b with dissolve

isa "What did you tell him?"

ji "Just that friends call you Bella."
scene ep1_lib_thank26c with dissolve

isa "You know that a library is for reading and studying, [name]."

isa "Not for hitting on girls."

ji "Bella!"
scene ep1_lib_thank31 with dissolve
if dtype > 0:
    mc "Gah. You seem to have a personal vendetta with me. I'm leaving..."
elif True:
    mc "All right... I'm leaving."
mc "Bye, Jill."

ji "I...ah...bye."
$ bios_history_isabella +="I tried apologizing to Bella, but she doesn't seem to like me at all.\n\n"
$ bios_history_jill +="I got a chance to talk more to Jill. She's really nice...and a friend of Bella....which is kind of weird.\n\n"
$ bios_name_jill = True
$ bios_name_isabella = True
$ chat_new_bios = True

scene ep1_lib_thank33 with dissolve

ji "That was kind of rude."
scene ep1_lib_thank34 with dissolve

isa "Trust me. I know that boy. You should stay away from him."
scene ep1_lib_thank33 with dissolve

ji "What? Why?"
scene ep1_lib_thank34 with dissolve

isa "Let's just say that he has a habit of getting into trouble."
scene ep1_lib_thank35 with dissolve

ji "More trouble?"
scene ep1_lib_thank36 with dissolve

isa "What do you mean {b}more{/b} trouble!? What trouble do you know of!?"
scene ep1_lib_thank35 with dissolve

ji "I saw him get bullied by the tri-alphas yesterday."

ji "They were ganging up on him and pulled his underwear up."
scene ep1_lib_thank37 with dissolve

isa "Oh..."
scene ep1_lib_thank35 with dissolve

ji "Yeah, I couldn't help but feel sorry for him."
scene ep1_lib_thank37 with dissolve

isa "Where you're coming from...I understand."
scene ep1_lib_thank35b with dissolve

ji "Also, I don't think he's such a bad guy."

ji "I saw him spend like 10 minutes putting books from your cart back into their shelves."
scene ep1_lib_thank37c with dissolve
$ renpy.pause()
scene ep1_lib_thank37b with dissolve
isa "..."
scene ep1_lib_thank35b with dissolve

ji "And he's been nothing but nice to me."
scene ep1_lib_thank34 with dissolve

isa "Is there something going on between the two of you?"
scene ep1_lib_thank33 with dissolve

ji "What? No! I just..."

ji "We've barely talked to each other..."
scene ep1_lib_thank35b with dissolve

ji "...but I have to admit that it's nice to socialize with someone who doesn't talk about their successful parents or economics every single minute."
scene ep1_lib_thank37 with dissolve

isa "Just...be careful, Jill. You know I want what's best for you."
scene ep1_lib_thank42 with dissolve

ji "I know, Bella. I love you for that."
scene ep1_lib_thank43 with dissolve

ji "So, you think I shouldn't socialize with him?"
$ renpy.music.stop(channel="sfx1", fadeout=3)
scene ep1_lib_thank44 with dissolve
isa "..."

play music "music/ep1/golden_alley.mp3"
scene ep1_mdorm with wipeleft
mc "Hey! Where have you been?"
scene ep1_mdorm3 with dissolve
my "Out...doing stuff..."
my "Wait...why are you still here?"
scene ep1_mdorm2 with dissolve
mc "I was thinking that maybe...just maybe..."
mc "...you would let me stay here until I find another dorm?"
scene ep1_mdorm3 with dissolve
my "Wow...really?"
scene ep1_mdorm8b with dissolve
mc "Listen, I went to the reception earlier, but it's not simple to change dorms all of a sudden."
mc "There's this big process behind it..."
scene ep1_mdorm4 with dissolve
my "Well, fuck it. It's not like I was going to let you live outdoors anyway."
scene ep1_mdorm5 with dissolve
mc "Really!?"
scene ep1_mdorm4 with dissolve
my "Yes, but only until you find yourself another place to stay!"
my "Or until I get a new dorm mate."
scene ep1_mdorm5 with dissolve
mc "About that, why don't I ask them if I can just share this dorm with you?"
scene ep1_mdorm8 with dissolve
my "You didn't tell them that, did you!?"
scene ep1_mdorm8b with dissolve
mc "That your dorm mate is a no-show? No, I didn't."
scene ep1_mdorm10 with dissolve
my "*{i}Phew{/i}* Good!"
my "It's just that I hit the jackpot for once, and I don't want to lose the privilege of having my own room here."
scene ep1_mdorm10b with dissolve
mc "Anyway...thanks! I'll try not to annoy you."
scene ep1_mdorm10 with dissolve
my "Don't worry. You're cool."
my "You got your phone back yet?"
scene ep1_mdorm10b with dissolve
mc "Yeah, I did!"
scene ep1_mdorm15 with dissolve
my "You should take my number in case you get locked out or something."
$ number_maya = True
jump ep1_freeroam_movie_maya_label
label ep1_maya_movie_label:
scene fr_ep1_movie with dissolve

menu:
    "Sneak a peek ({color=#ffffff}{size=-1}{font=collegiate.ttf}DIK{/font}{/size}{/color})" if dtype > 0:
        scene fr_ep1_movieb with dissolve
        mc "(Damn, that's sexy...)"
        if assman:
            mc "(Derek's right...I am the ass man.)"
        scene fr_ep1_movie with dissolve
    "Ask her what she's doing" if True:
        $ renpy.pause(0.5)
mc "What are you up to?"
my "Just watching a movie."
mc "On your phone?"
scene fr_ep1_movie2 with dissolve
my "Yeah, do you see a TV in here?"
scene fr_ep1_movie2b with dissolve
mc "It's just that the screen is so small."
scene fr_ep1_movie2 with dissolve
my "You get used to it. Besides, I couldn't give up watching movies."
scene fr_ep1_movie2b with dissolve
mc "Ah, so you're a movie buff then?"
scene fr_ep1_movie3 with dissolve
my "Big time! How about you?"
scene fr_ep1_movie2b with dissolve
mc "No, growing up, we didn't have..."
mc "No, I'm not into movies."
scene fr_ep1_movie4 with dissolve
my "What was that first part?"
scene fr_ep1_movie2b with dissolve
mc "I was going to say that we didn't have a TV when I grew up..."
mc "...but I stopped because it's both personal and embarrassing..."
scene fr_ep1_movie2 with dissolve
my "You don't have to feel embarrassed about that."
my "Look at me! I don't have a TV now."
scene fr_ep1_movie2b with dissolve
mc "Yeah..."
scene fr_ep1_movie2 with dissolve
my "Hey, I'm glad you told me."
scene fr_ep1_movie3 with dissolve
my "Maybe you're a movie nerd too. You just don't know it yet."
scene fr_ep1_movie2b with dissolve
mc "Haha, maybe."
scene fr_ep1_movie8 with dissolve
my "Come."
scene fr_ep1_movie9 with dissolve
mc "What?"
scene fr_ep1_movie8 with dissolve
my "Lie next to me, stupid. We can watch it together."
scene fr_ep1_movie9 with dissolve
mc "Oh, ok."
scene fr_ep1_movie10 with dissolve
$ guideSuggestedPage = 47
mc "(Her vanilla perfume smells amazing on her...)"
menu:
    "Look closer" if True:
        $ dk(1)
        scene fr_ep1_movie10b with dissolve
        if dtype > 0:
            mc "(Fuck me...)"
        elif True:
            mc "(I shouldn't be looking...but I just can't resist.)"
        scene fr_ep1_movie10 with dissolve
    "Don't look closer" if True:
        $ dk(-1)
        $ renpy.pause(0.5)
mc "What are we watching?"
my "An old horror movie called \"The Secret in His Closet\"."
my "It's one of my all-time favorites!"
my "It's about this older man living alone who has a routine of always going into his closet every night."
scene fr_ep1_movie12 with dissolve
mc "Into it?"
scene fr_ep1_movie11b with dissolve
my "Yeah! The kids next door watch him through their bedroom window every night and become obsessed with it."
my "Like, why would he go into a closet?"
my "So, they sneak into his house when he leaves to run an errand and try to find out what's in there."
scene fr_ep1_movie12 with dissolve
mc "That sounds really interesting."
stop music fadeout 3
scene fr_ep1_movie11b with dissolve
my "Yeah, let's watch! I'm not going to spoil what happens for you."
play music "music/ep1/lost_souls.mp3"
scene fr_ep1_movie13 with fade
mc "(This movie is fucking scary!)"
kid "Jonathan! Hide! He's coming back home!"
mc "(Oh shit!)"
scene fr_ep1_movie14 with dissolve
my "Are you ok there, [name]?"
scene fr_ep1_movie15 with dissolve
mc "Yeah, I just haven't watched a lot of scary movies..."
scene fr_ep1_movie14 with dissolve
my "It's the best feeling, huh?"
scene fr_ep1_movie13 with dissolve
kid "Quick! Hide under the bed!"
scene fr_ep1_movie13b with dissolve
kid "NO!!!! JONATHAN!!!"
scene black
my "Hey! You're missing the best part!"
scene fr_ep1_movie15 with dissolve
mc "Sorry, it's just too scary for me."
scene fr_ep1_movie14 with dissolve
my "Aw..."
my "Here, hold the phone."
scene fr_ep1_movie15 with dissolve
stop music fadeout 3
mc "How is that going to help?"
scene fr_ep1_movie17 with dissolve
mc "(Oh...)"
play music "music/ep1/windswept.mp3"
mc "What are you doing?"
scene fr_ep1_movie19 with dissolve
my "I'm comforting you."
my "Feeling better?"
scene fr_ep1_movie17 with dissolve
mc "Yeah..."
scene fr_ep1_movie21 with dissolve
mc "(Why is she doing this?)"
mc "(Maybe she likes me?)"
scene fr_ep1_movie21b with dissolve
mc "(Oh my God... Those are the strings of her panties I feel...)"
scene fr_ep1_movie21c with dissolve
mc "(She doesn't mind that I have my hand here?)"
my "This part is so scary!"
mc "(She has the softest skin...)"
scene fr_ep1_movie21 with dissolve
menu:
    "Smell her hair" if True:
        scene fr_ep1_movie24 with dissolve
        mc "*{i}Inhales deeply{/i}*"
        scene fr_ep1_movie25 with dissolve
        my "Are you...smelling my hair?"
        scene fr_ep1_movie26 with dissolve
        if dtype > 0:
            $ RPmaya-=1
            mc "Yeah, you smell good."
            scene fr_ep1_movie26b with dissolve
            my "Please, stop that..."
        elif True:
            mc "No...I was just breathing. This is so scary!"
            scene fr_ep1_movie27 with dissolve
            my "Yeah!"
    "Don't risk it" if True:
        $ dk(-1)

scene fr_ep1_movie28 with dissolve
mc "(She has her leg over mine! How am I supposed to focus now?)"
scene fr_ep1_movie29 with dissolve
my "Wow, your heart is beating like really fast!"
my "I had no idea that you were this scared."
scene fr_ep1_movie30 with dissolve
mc "Yeah, this is horrifying."
scene fr_ep1_movie27 with dissolve
my "Aw..."
scene fr_ep1_movie32 with dissolve
mc "(She moved it even higher up!)"
mc "(Fuck! I'm going to get a boner from this...not good...)"
menu:
    "Push her leg down" if True:
        $ RPmaya += 1
        scene fr_ep1_movie30 with dissolve
        mc "Maya...your leg is a bit too high up..."
        scene fr_ep1_movie33 with dissolve
        my "Oh! I wasn't touching...you know?"
        scene fr_ep1_movie30 with dissolve
        mc "No, it's fine."
        scene fr_ep1_movie27 with dissolve
        my "Ok. Thanks for telling me."
    "Linger longer" if True:
        scene fr_ep1_movie31 with dissolve
        my "(Hm...I think my thigh is touching his dick...)"
        scene fr_ep1_movie36 with dissolve
        my "(Why isn't he saying anything?)"
        scene fr_ep1_movie31b with dissolve
        if dtype > 0:
            mc "(Damn...)"
        elif True:
            mc "(Phew...)"
scene fr_ep1_movie30 with dissolve
mc "Maybe this is weird to ask but..."
mc "...didn't you say that you have a boyfriend?"
scene fr_ep1_movie29 with dissolve
my "Erm...yeah...I..."
my "Why?"
scene fr_ep1_movie30 with dissolve
mc "I just think that it's a bit weird lying like this with you if that's the case..."
scene fr_ep1_movie33 with dissolve
my "Well...it's...complicated...I..."
my "Can you keep a secret?"
scene fr_ep1_movie30 with dissolve
mc "Yes, of course."
scene fr_ep1_movie33 with dissolve
my "...and promise me that you won't ask any more questions if I tell you this?"
scene fr_ep1_movie30 with dissolve
mc "Sure..."
scene fr_ep1_movie33 with dissolve
my "I don't have a boyfriend."
my "I tell guys I have a boyfriend because I'm not interested in attracting them."
my "It may sound weird...but that's the only way that seems to work."
scene fr_ep1_movie30 with dissolve
mc "Ok, so you don't want me to be attracted to you?"
scene fr_ep1_movie26b with dissolve
my "Hey...you promised not to ask any more questions..."
my "..."
scene fr_ep1_movie33 with dissolve
my "...but yeah..."
my "...it would probably be for the best if you weren't."
scene fr_ep1_movie21 with dissolve
menu:
    "Too late for that" if True:
        $ bios_history_maya += "I had a movie night with Maya. I told her I'm attracted to her.\n\n"
        $ bios_name_maya = True
        $ chat_new_bios = True
        $ ep1_maya_attracted = True
        $ RPmaya+=1
        mc "..."
        mc "I think it's too late for that."
        scene fr_ep1_movie25 with dissolve
        my "Oh..."
        scene fr_ep1_movie26 with dissolve
        if dtype > 0:
            mc "Yeah..."
            scene fr_ep1_movie27 with dissolve
            my "Let's focus on the movie instead..."
        elif True:
            mc "But don't worry...I'll be respectful."
            scene fr_ep1_movie27 with dissolve
            my "Thank you, [name]..."
    "Ok. I'll try." if True:
        $ bios_history_maya += "I had a movie night with Maya.\n\n"
        $ bios_name_maya = True
        $ chat_new_bios = True
        $ ep1_maya_attracted = False
        mc "Ok, I'll try."

scene fr_ep1_movie36b with Fade(1.5,1,0.5)
my "Tell me! Did you like the movie?"
scene fr_ep1_movie37 with dissolve
menu:
    "I liked it" if True:
        if dtype > 0:
            mc "Yeah. It was scary, but I liked it."
            scene fr_ep1_movie36b with dissolve
            my "Right!?"
        elif True:
            $ RPmaya += 1
            mc "It was scary, but watching it with you made it fun."
            scene fr_ep1_movie36b with dissolve
            my "Yeah, this was really nice."
    "It wasn't for me" if True:
        mc "No...that movie wasn't for me at all."
        mc "It was way too scary!"
        scene fr_ep1_movie36b with dissolve
        my "Haha, you're cute."
my "Maybe next time we can watch something more lighthearted?"
scene fr_ep1_movie37 with dissolve
mc "I'd love that."
scene fr_ep1_movie40 with dissolve
my "Now, unless you wanna sleep in my bed, get out."
scene fr_ep1_movie37 with dissolve
menu:
    "Thanks for the movie" if True:
        stop music fadeout 3
        mc "Thanks for the movie, Maya."
    "Was that an offer?" if True:
        mc "Was that an offer?"
        scene fr_ep1_movie36b with dissolve
        stop music fadeout 3
        my "Haha, no, it was a joke, stupid."
$ guideSuggestedPage = 48
scene ep1_gender with Fade(1.5,1,0.5)
play music "music/ep1/dont_count_on_me.mp3"
mc "(Gender Studies 101...this will be interesting...)"
mc "(Wow, there's a lot of girls in this class...)"
mc "(Derek's going to regret that he didn't sign up for-)"
scene ep1_gender1
if assman:
    de "ASS MAN! OVER HERE!"
elif True:
    de "BRO! OVER HERE!"
mc "(...oh.)"
scene ep1_gender2 with dissolve
de "I'm loving this class, bro!"
de "Look at all the girls!"
de "Sure, some look like peacocks that escaped from the zoo-"
play sound "sound_effects/table_slam.mp3"
scene ep1_gender2b with vpunch
fem "Oh my God! You did not just say that!!!"
scene ep1_gender3 with dissolve
de "But there are several who actually are packing some serious front and back load."
scene ep1_gender3b with dissolve
de "NO WAY! That's our teacher!"
scene ep1_gender4 with dissolve
de "Mrs. Milk machine!"
if preferredmilf == 0:
    de "She's the one you found hotter than Cathy, right!?"
scene ep1_gender4b with dissolve
mc "*{i}Whispers{/i}*Dude, chill! She can hear you."
de "Seriously! Look at her!"
ja "(Hm...well, this is a first.)"
ja "(It should be interesting having boys in this class...)"
scene ep1_gender5 with dissolve
ja "(If they are here for the right reasons that is...)"
scene ep1_gender6 with dissolve
ja "(Hmph...bummer.)"
scene ep1_gender8 with dissolve
ja "(*{i}Sigh{/i}* I should've doubled up on espresso for this...)"
ja "(Every year, it's the same group of girls...)"
scene ep1_gender9 with dissolve
ja "(I wonder why feminism always attracts the most hardcore women.)"
ja "(There are rarely any girls here who understand what it's really about.)"
scene ep1_gender10
my "Derek!? No...don't tell me you signed up."
de "You weren't lying about the vaginas, Maya!"
scene ep1_gender12 with dissolve
my "Give me strength..."
mc "Hey, Maya."
scene ep1_gender13 with dissolve
my "Hey, [name]."
scene ep1_gender14 with dissolve
ja "Ok, my clock is on the dot. Let us begin."
ja "Welcome to Gender Studies 101. I'm Dr. Jade-"
de "Females can be doctors?"
fem "Hey, shut up!"
scene ep1_gender16 with dissolve
ja "During this course, we will learn about gender equality, feminism, sexism..."
ja "...and the difference between sex and gender."
scene ep1_gender17
de "Maya, you didn't tell me there will be sex talk, too!"
fem "Shh!"
scene ep1_gender18 with dissolve
ja "You two."
ja "I'm happy to see two male students in my class."
ja "That's a first-time occurrence."
scene ep1_gender20 with dissolve
de "You're welcome!"
fem "Ugh..."
scene ep1_gender18 with dissolve
ja "I'm going to have to ask you to put on at least a t-shirt next time, though."
de "...fine."
ja "But, I'm curious, why did you sign up for this class?"
ja "What was it that piqued your interests?"
scene ep1_gender20 with dissolve
de "Easy credits and vagin-"
scene ep1_gender22
my "No!"
scene ep1_gender23 with dissolve
ja "How about you?"
scene ep1_gender24 with dissolve
menu:
    "Easy credits and vaginas ({color=#ffffff}Huge {size=-1}{font=collegiate.ttf}DIK{/font}{/size}{/color})" if dtype > 1:
        $ dk(1)
        mc "Easy credits and vaginas."
        $ RPmaya -= 1
        $ RPderek += 1
        scene ep1_gender17 with dissolve
        de "That's what I was going to say!"
        scene ep1_gender24b with dissolve
        ja "Hmph."
    "Learn more about women" if True:
        $ dk(-1)
        $ RPmaya += 1
        if dtype > 0:
            mc "You know...to learn more about women and their issues."
            scene ep1_gender23 with dissolve
            ja "Welcome to the class...?"
            scene ep1_gender24 with dissolve
            mc "[name]."
        elif True:
            mc "I would like to learn more about women's struggles in real life and the real meaning of feminism."
            scene ep1_gender24c with dissolve
            ja "(What the...?)"
            ja "The real meaning of feminism? A very interesting point!"
            scene ep1_gender23 with dissolve
            ja "Welcome to the class...?"
            scene ep1_gender24 with dissolve
            mc "[name]."
            scene ep1_gender23 with dissolve
            $ ep1_jade_pleased = True
            ja "Welcome, [name]."
    "Nothing special" if True:
        mc "Nothing special, really."
        scene ep1_gender23 with dissolve
        ja "Well, hopefully, you'll be more motivated soon."

scene ep1_gender14 with dissolve
ja "These classes will consist of a lot of topical discussions, and participation in the discussions is mandatory."
ja "I would like you all to find someone you don't know in here and get to know each other better."
if not minigames:
    jump ep1_after_gender_test1
scene ep1_gender30 with dissolve
stop music fadeout 3
stu "Hey, do you wanna pair up?"
mc "Sure..."
jump gender101_test1
label ep1_after_gender_test1:
if minigames:
    scene ep1_gender31 with wiperight
    play music "music/ep1/dont_count_on_me.mp3"
elif True:
    scene ep1_gender31 with Fade(1.5, 1, 0.5)
fem "Why are you even here!? You're like the worst person I've ever met!"
scene ep1_gender32 with dissolve
de "Not a PERSON! It's called a MAN, Wendy!"
de "Men have penises; women have vaginas."
de "What the fuck does X-gender even mean!?"
de "What do its genitals look like!?"
scene ep1_gender34 with dissolve
fem "I HATE YOU!"
scene ep1_gender35 with dissolve
de "Women...am I right?"
$ bios_jade = True
$ bios_history_jade += "Dr. Jade teaches Gender Studies 101.\n\n"
$ bios_name_jade = True
$ bios_history_derek += "Even though Derek and Maya are twins, they are very unalike. The Gender Studies class proved that.\n\n"
$ bios_name_derek = True
$ bios_dany = True
$ bios_name_dany = True
$ bios_wendy = True
$ bios_name_wendy = True
$ bios_minny = True
$ bios_name_minny = True
$ chat_new_bios = True

scene ep1_gender36
my "I don't know about you, but I just can't sit with him in that class."
my "I know I said it's easy credits, but I also want to learn something from it."
scene ep1_gender37 with dissolve
if dtype > 0:
    mc "I know, but I gotta admit that he's pretty fun to be around."
elif True:
    $ RPmaya += 1
    mc "I don't blame you."
scene ep1_gender38 with dissolve
my "Ok...I'll see you later. Don't wait up; I'll probably be very late tonight."
scene ep1_gender39 with dissolve
mc "Where are you going?"
scene ep1_gender38 with dissolve
my "Home to shower and change..."
my "Then...you know...pledge stuff..."
scene ep1_gender39 with dissolve
mc "Oh, so Quinn got back to you?"
scene ep1_gender38 with dissolve
my "Yeah..."
scene ep1_gender39 with dissolve
mc "I get it... Well, good luck."
stop music fadeout 3

$ guideSuggestedPage = 49
jump ep1_freeroam_maya_dorm_label

label ep1_ending_scene:
stop music fadeout 3
scene ep1_end0 with fade
mc "(This is weird...)"
mc "(Why hasn't she come back home yet? It's getting very late.)"
scene ep1_end1 with dissolve
play sound "sound_effects/dial_tone.mp3"
mc "(Hm...)"
mc "(Nope. No answer...)"
scene ep1_end2 with dissolve
mc "(Nothing else I can do.)"
mc "(She told me not to wait up...)"
mc "(...)"
mc "(Bedtime it is.)"
scene ep1_ending0 with fade
play sound "sound_effects/door_lock.mp3"
$ renpy.pause(0.5)
$ renpy.sound.play("sound_effects/door_close.mp3", channel="sfx2", loop=False)
$ renpy.pause()
scene ep1_ending0b with dissolve
my "(Yup...he's asleep...)"
label ep1_maya_lewd:
if _in_replay:
    hide screen phone_screen
    if persistent.name == None:
        $ name = "MC"
    elif True:
        $ name = persistent.name
    if persistent.mc_maya == None:
        $ mc_maya = name
    elif True:
        $ mc_maya = persistent.mc_maya
    if persistent.maya == None:
        $ maya = "Maya"
    elif True:
        $ maya = persistent.maya
scene ep1_ending0 with dissolve
play sound "sound_effects/clothes.mp3"
$ renpy.pause()
play music "music/ep1/windswept.mp3"
scene ep1_ending1 with dissolve
$ renpy.pause()
scene ep1_ending2 with dissolve
my "(You can do this, Maya...)"
scene ep1_ending3 with dissolve
$ renpy.pause()
scene ep1_ending4 with dissolve
my "(Wait...)"
my "(...why is it hard?)"
scene ep1_ending5 with dissolve
my "(Holy fuck! It's huge!)"
my "*{i}Gulp{/i}*"
scene ep1_ending6 with dissolve
my "(Ok... Careful now...)"
my "(This feels so wrong...)"
scene ep1_ending7 with dissolve
my "(Am I really doing this?)"
scene ep1_ending6b with dissolve
$ renpy.pause()
scene ep1_ending7 with dissolve
my "(This feels...weird...)"
my "(But his skin is so warm...)"
my "(That's kind of nice...)"
scene ep1_ending8 with dissolve
my "(Who are you kidding, Maya? All you're feeling right now is that hard thing poking you...)"
my "(It's kind of like my dildo...I guess...but...)"
my "(Huh! Is he waking up? No turning back now.)"
scene ep1_ending10 with dissolve
mc "Huh, [maya]? What are you-"
scene ep1_ending11 with dissolve
my "Shh!"
my "*{i}Whispers{/i}* Don't say a word."
scene ep1_ending13 with dissolve
mc "(Is this another dream, or is she really lying on top of me...)"
mc "(Shit...she's pressing herself against my dick...)"
scene ep1_ending14 with dissolve
mc "(Oh my God! That's her nipple...)"
mc "(Damn, my mouth is all dry...)"
mc "(I guess I can put my hand here...)"
scene ep1_ending15 with dissolve
mc "(Her ass is both firm and soft at the same time.)"
my "(Is he pushing me harder down...)"
my "(Damn...I'm getting that tingling feeling...)"
my "*{i}Softly moans{/i}*"
image anim_maya_grind2_ep1 = Movie(channel="anim_maya_grind2_ep1", play="images/movies/ep1/anim_maya_grind2_ep1.webm")
scene anim_maya_grind2_ep1 with dissolve:
    size (config.screen_width, config.screen_height)
my "(Ok, let's begin...)"
my "Hngh..."
my "(Am I doing it too hard?)"
mc "Mmm..."
my "(No...he seems to like it...)"
pause
image anim_maya_grind_ep1 = Movie(channel="anim_maya_grind_ep1", play="images/movies/ep1/anim_maya_grind_ep1.webm")
scene anim_maya_grind_ep1 with dissolve:
    size (config.screen_width, config.screen_height)
my "(It feels...kind of nice...)"
my "(No, it doesn't! Stop it...)"
my "(It's wrong...)"
pause
scene ep1_ending13 with dissolve
my "*{i}Breathes heavily{/i}*"
my "(Shit...I'm starting to get hot...)"
my "(I can feel his warm breath against my face...)"
scene ep1_ending16 with dissolve
my "(No...)"
my "(This is better...I think...)"
image anim_maya_grind3_ep1 = Movie(channel="anim_maya_grind3_ep1", play="images/movies/ep1/anim_maya_grind3_ep1.webm")
scene anim_maya_grind3_ep1 with dissolve:
    size (config.screen_width, config.screen_height)
mc "(Oh fuck...her body's fucking amazing...)"
mc "(Look at those hips moving...)"
pause
image anim_maya_grind_closer_ep1 = Movie(channel="anim_maya_grind_closer_ep1", play="images/movies/ep1/anim_maya_grind_closer_ep1.webm")
scene anim_maya_grind_closer_ep1 with dissolve:
    size (config.screen_width, config.screen_height)
my "*{i}Softly moans{/i}* Oh...[mc_maya]..."
mc "[maya]..."
my "(Oh no...)"
image anim_maya_grind3b_ep1 = Movie(channel="anim_maya_grind3b_ep1", play="images/movies/ep1/anim_maya_grind3b_ep1.webm")
scene anim_maya_grind3b_ep1 with dissolve:
    size (config.screen_width, config.screen_height)
my "(I'm...enjoying this?)"
my "(No! Stop thinking about it.)"
my "(Focus! It's almost over now...)"
pause

image anim_maya_grind_long_ep1 = Movie(channel="anim_maya_grind_long_ep1", play="images/movies/ep1/anim_maya_grind_long_ep1.webm")
scene anim_maya_grind_long_ep1 with dissolve:
    size (config.screen_width, config.screen_height)
my "*{i}Moans{/i}*"
my "(I'm so fucking hot right now...)"
mc "(Damn, she has the angle just right...)"
mc "(Her warm pussy is grinding so tightly against the head of my dick...)"
my "(Fuck, I'm so wet....this wasn't supposed to happen.)"
pause

if _in_replay:
    menu:
        "Massage her clit" if persistent.ep1_maya_dik:
            image anim_maya_clit_ep1 = Movie(channel="anim_maya_clit_ep1", play="images/movies/ep1/anim_maya_clit_ep1.webm")
            scene anim_maya_clit_ep1 with dissolve:
                size (config.screen_width, config.screen_height)
            my "*{i}Moans loudly{/i}*"
            my "(OH FUCK!)"
            my "(What's he doing!? This...this...)"
            my "*{i}Moans loudly{/i}* Oh, [mc_maya]!"
            pause
        "Kiss her" if persistent.ep1_maya_chick:
            image anim_maya_kiss_ep1 = Movie(channel="anim_maya_kiss_ep1", play="images/movies/ep1/anim_maya_kiss_ep1.webm")
            scene anim_maya_kiss_ep1 with dissolve:
                size (config.screen_width, config.screen_height)
            my "(Shit! He's kissing me...)"
            my "(God...his lips are so soft...)"
            my "(Just...a little bit longer...)"
            pause
elif True:
    if dtype > 0:
        $ ep1_kissed_maya = False
        image anim_maya_clit_ep1 = Movie(channel="anim_maya_clit_ep1", play="images/movies/ep1/anim_maya_clit_ep1.webm")
        scene anim_maya_clit_ep1 with dissolve:
            size (config.screen_width, config.screen_height)
        my "*{i}Moans loudly{/i}*"
        my "(OH FUCK!)"
        my "(What's he doing!? This...this...)"
        my "*{i}Moans loudly{/i}* Oh, [mc_maya]!"
        pause
    elif True:
        $ ep1_kissed_maya = True
        image anim_maya_kiss_ep1 = Movie(channel="anim_maya_kiss_ep1", play="images/movies/ep1/anim_maya_kiss_ep1.webm")
        scene anim_maya_kiss_ep1 with dissolve:
            size (config.screen_width, config.screen_height)
        my "(Shit! He's kissing me...)"
        my "(God...his lips are so soft...)"
        my "(Maybe if I close my eyes and pretend that he's- NO!)"
        my "(Just...a little bit longer...)"

scene ep1_ending_shock with dissolve
if _in_replay:
    mc "[maya]... Take your panties off..."
    $ renpy.end_replay()
elif dtype > 0:
    mc "[maya]... Take your panties off..."
    $ persistent.ep1_maya_dik = True
    $ ep1_dik_end = True
elif True:
    mc "[maya]... What are we doing?"
    $ ep1_dik_end = False
    $ persistent.ep1_maya_chick = True
if persistent.ep1_maya_dik and persistent.ep1_maya_chick:
    $ persistent.ep1_maya_full = True
$ calcScenes()
hide screen phone_screen
stop music
play sound "sound_effects/zap.mp3"
scene ep1_ending_shock1 with hpunch
$ renpy.pause(0.5)
scene black
$ renpy.pause(2)
$ updateDikScore()

if steamAchievements and persistent.vault1 and not config.console and not config.developer:
    $ achievement.grant("VAULTLOOTER1")
    init:
        $ achievement.register("VAULTLOOTER1")
    $ achievement.Sync()
if steamAchievements and persistent.vault1 and persistent.vault2 and persistent.vault3 and persistent.vault4 and not config.console and not config.developer:
    $ achievement.grant("VAULTLOOTER")
    init:
        $ achievement.register("VAULTLOOTER")
    $ achievement.Sync()
if steamAchievements and preferredmilf == 0 and not config.console and not config.developer:
    $ achievement.grant("MILKMACHINE")
    init:
        $ achievement.register("MILKMACHINE")
    $ achievement.Sync()
if steamAchievements and preferredmilf == 1 and not config.console and not config.developer:
    $ achievement.grant("FLATANDBORING")
    init:
        $ achievement.register("FLATANDBORING")
    $ achievement.Sync()
if steamAchievements and not config.console and not config.developer:
    $ achievement.grant("EPISODE1")
    init:
        $ achievement.register("EPISODE1")
    $ achievement.Sync()
if persistent.current_episode == 1:
    scene ep1_episode_end
    play music "music/patched/track_previous.mp3"
    $ renpy.pause()
elif True:
    scene ep1_episode_endb
    $ renpy.pause()
scene black with fade
play music "music/ep1/unknown_power.mp3"
show screen scoremsg
$ calcRenders()
$ renpy.pause(2)
hide screen scoremsg

$ episodeIsEnding = True
show screen endingScreen
show screen majorChoiceScale
$ renpy.pause()
$ episodeIsEnding = False
hide screen endingScreen
hide screen majorChoiceScale

if RPjosy >= 0:
    $ josyScore = RPjosy / 10.0
elif True:
    $ josyScore = RPjosy / 1.0
if RPmaya >= 0:
    $ mayaScore = RPmaya / 15.0
elif True:
    $ mayaScore = RPmaya / 3.0
if RPsage >=0:
    $ sageScore = RPsage / 6.0
elif True:
    $ sageScore = RPsage / 2.0
if RPisabella >= 0:
    $ isabellaScore = RPisabella / 1.0
elif True:
    $ isabellaScore = RPisabella / 2.0
if RPjill >= 0:
    $ jillScore = RPjill / 2.0
elif True:
    $ jillScore = RPjill / 2.0
$ episodeContLabel = "ep1EndLabel"

jump ep1_report_jill_label
$ renpy.pause()
label ep1EndLabel:
stop music fadeout 3
$ renpy.pause(2)
$ persistent.tutorials = True
scene black with dissolve
if not persistent.pet_app_unlocked:
    $ persistent.pet_app_unlocked = True
    show phone_app_pet_new:
        xalign 0.5
        yalign 0.4
    show text "Congratulations! You just unlocked the Pet names app on your phone.\nThis app lets you give the girls pet names and have them call you pet names, too."
    $ renpy.pause()
    show text "This feature will remain unlocked if you decide to restart the game."
    $ renpy.pause()

$ bios_history_maya += "Unbelievable! Maya woke me up in the middle of the night and started grinding on my cock. Why did she do that?\n\n"
$ bios_name_maya = True
$ chat_new_bios = True
$ guideSuggestedPage = 51
if renpy.loadable("update2.rpyc"):
    jump startUpdate2
elif True:
    jump endOfVersion

label endOfVersion:
scene black
show spr_bg
show spr_mid
show spr_top
show massive_diks
$ renpy.pause()
hide massive_diks
show acknowledgements
$ renpy.pause()
hide acknowledgements
show music_credits
$ renpy.pause()
hide music_credits
show version_end
$ renpy.pause()
hide version_end
scene episode2_polls
$ renpy.pause()
scene patreon_promo
$ renpy.pause()
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
