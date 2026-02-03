label ep4_night_talk_sage_label:
scene ep4_night_talk_sage with Fade(1.5,1.5,1.5)
sa "I'm not fully awake yet."
sa "What happened?"
scene ep4_night_talk_sage2 with dissolve
mc "..."
scene ep4_night_talk_sage with dissolve
sa "Look, if you expect me to let you stay in our sorority, you need to tell me what's up."
sa "Why did you come here?"
scene ep4_night_talk_sage2 with dissolve
mc "I didn't know where else to go. You were the first one who came to mind."
scene ep4_night_talk_sage5 with dissolve
sa "Ok? That doesn't explain anything. Why are you sad?"
scene ep4_night_talk_sage2 with dissolve
mc "I...feel betrayed."
scene ep4_night_talk_sage5 with dissolve
sa "Betrayed? By who?"
scene ep4_night_talk_sage2 with dissolve
mc "My roommate...Maya. My former roommate, I should say."
mc "I can't tell you any details...I promised."
scene ep4_night_talk_sage5 with dissolve
sa "Keep it vague, then. You gotta give me something."
scene ep4_night_talk_sage2 with dissolve
mc "She lied to me...or kept something from me..."
mc "And I just can't stay with her anymore. Besides, me staying there with her wasn't really legal in the first place..."
mc "I got into a fight with my first roommate and ended up staying at her place."
mc "She got a new roommate now. So...I need a place to stay."
scene ep4_night_talk_sage with dissolve
sa "What about the DIKs? Can't they cut you some slack?"
sa "I mean, you're a maggot. You're gonna be a DIK in like a week, right?"
scene ep4_night_talk_sage2 with dissolve
mc "I've tried that before. It's not gonna work."
scene ep4_night_talk_sage13 with dissolve
sa "Ok... So...uh..."
sa "Get comfortable. I'm gonna go find a mattress for you."
scene ep4_night_talk_sage14 with dissolve
stop music fadeout 3
mc "*{i}Sigh{/i}*"
mc "(I can't believe what happened back there...)"
jump ep4_flashback_label

label ep4_night_talk2_sage_label:
play music "music/ep3/guitar_gentle.mp3"
scene ep4_night_talk2_sage with fade
sa "Here's your mattress."
scene ep4_night_talk2_sage1 with dissolve
mc "Thanks... I could have helped you get it."
sa "Really? I thought you were here because you need {b}my{/b} help."
scene ep4_night_talk2_sage3 with dissolve
sa "Sorry... I'm dead tired right now."
sa "I'm a bit bitchy when I'm tired."
sa "We'll continue this in the morning, ok?"
mc "Sure...."
play sound "sound_effects/shove.mp3"
scene ep4_night_talk2_sage5 with vpunch
sa "*{i}Yawns{/i}* Good night."
mc "Good night, Sage."
scene ep4_night_talk2_sage5b with dissolve
mc "(...)"
mc "(I have no clue what I'm going to do now...)"
mc "(Thank you, Sage...)"
mc "(I'm glad I have someone like you here.)"
play sound "sound_effects/slap.mp3"
scene ep4_night_talk2_sage6 with vpunch
mc "Ouch! Hey..."
scene ep4_night_talk2_sage7 with dissolve
sa "*{i}Snores{/i}*"
mc "(Haha...ok, that's pretty damn cute.)"
mc "(Fuck... That would have counted as the third slap...)"
mc "(Meh... I have other problems to worry about.)"
stop music fadeout 2

$ bios_history_sage += "After fighting with Josy and Maya, I went to stay with Sage.\n\n"
$ bios_name_sage = True
$ bios_history_mc += "After fighting with Josy and Maya, I went to stay with Sage.\n\n"
$ bios_name_mc = True
$ chat_new_bios = True
label ep4_morning_talk_sage_label:
scene ep4_morning_talk_sage with Fade(2,2,2)
play music "music/ep4/inspiring_acoustic.mp3"
mc "..."
mc "Morning..."
scene ep4_morning_talk_sage1 with dissolve
sa "Hey. Good morning."
scene ep4_morning_talk_sage2 with dissolve
mc "What time is it?"
scene ep4_morning_talk_sage1 with dissolve
sa "It's 6 a.m."
scene ep4_morning_talk_sage2 with dissolve
mc "Seriously? Are you always up this early?"
scene ep4_morning_talk_sage5 with dissolve
sa "No, just sometimes. I had some HOT business to plan for and I woke up an hour ago, restless."
sa "I couldn't sleep well."
scene ep4_morning_talk_sage4 with dissolve
mc "Oh... Sorry if I ruined your beauty sleep."
scene ep4_morning_talk_sage5 with dissolve
sa "Don't worry. It's not because of you."
sa "I've had a lot on my plate lately."
scene ep4_morning_talk_sage4 with dissolve
mc "Being a president must mean a lot of work."
scene ep4_morning_talk_sage5 with dissolve
sa "Yeah, it is. Especially when it comes to the economy. You know, collecting fees from sisters, finding ways to earn money for the HOTs..."
sa "I'm so fucking thankful to have Quinn to help me out."
scene ep4_morning_talk_sage4 with dissolve
mc "Quinn?"
mc "..."
mc "How is she helping you out?"
scene ep4_morning_talk_sage5 with dissolve
$ guideSuggestedPage = 89
sa "She's amazing, really! I don't even have to ask her for most of the things."
sa "She just knows what needs to be done and then she does it."
scene ep4_morning_talk_sage4 with dissolve
menu:
    "That's nice" if True:
        mc "Nice to have someone to help you run things, I guess."
        mc "It's kind of like what Tommy is to Rusty."
        scene ep4_morning_talk_sage9 with dissolve
        sa "Yeah, definitely. That's what a vice president should be like."
        sa "Not like Dawe. Well...his family gym's been sponsoring the tri-alphas for years, but other than that, he leaves everything to Chad."
        sa "Well...{i}left{/i} everything to Chad, I guess."
    "And you like that?" if True:
        mc "She does your job without asking first? And you like that?"
        scene ep4_morning_talk_sage9 with dissolve
        sa "It's not really my job, the HOTs are a team."
        sa "And I like when she helps out...most of the time."
        sa "I mean, there have been some questionable choices in the past."
        sa "But she's the vice president and I'd rather have her doing something than nothing, like Dawe..."
        sa "And we always talk it out in private if there's an issue."
scene ep4_morning_talk_sage4 with dissolve
mc "I didn't realize that you and Quinn were close."
scene ep4_morning_talk_sage5 with dissolve
sa "I'm close with all sisters. But for Quinn..."
sa "What can I say? She was my daughter and she grew on me."
sa "Besides, after next year, the HOTs need someone to fill my shoes."
scene ep4_morning_talk_sage4 with dissolve
mc "You're quitting?"
scene ep4_morning_talk_sage9 with dissolve
sa "It's called graduating and yes..."
sa "I'm graduating next year."
scene ep4_morning_talk_sage4 with dissolve
mc "I see."
scene ep4_morning_talk_sage10 with dissolve
sa "Now... What are we going to do about you?"
scene ep4_morning_talk_sage11 with dissolve
mc "What do you mean?"
scene ep4_morning_talk_sage10 with dissolve
sa "Having a dude staying in a sorority...that's breaking all kinds of rules."
scene ep4_morning_talk_sage11 with dissolve
mc "You can't do anything about that?"
scene ep4_morning_talk_sage10 with dissolve
sa "I...like you."
sa "And I know the feeling of looking for a place to belong."
sa "Stay with me until you get your shit sorted, but get it sorted fast so us girls don't get into trouble."
scene ep4_morning_talk_sage11 with dissolve
mc "Thank you so much."
mc "I'll find a way to repay you."
scene ep4_morning_talk_sage10 with dissolve
sa "You teach me how to play guitar and we'll call it even. Sound good?"
scene ep4_morning_talk_sage11 with dissolve
mc "Yeah, absolutely!"
scene ep4_morning_talk_sage15 with dissolve
sa "Hey..."
sa "Join me for breakfast."
$ bios_history_sage += "Sage and Quinn seem to be close friends.\n\n"
$ bios_name_sage = True
$ bios_history_quinn += "Sage and Quinn seem to be close friends.\n\n"
$ bios_history_quinn += "Sage was Quinn's mother when she joined the HOTs.\n\n"
$ bios_name_quinn = True
$ chat_new_bios = True
scene ep4_morning_talk_sage16 with wipeleft
sa "Say, you're a freshman..."
sa "Would you happen to know two students named Ashley and Lily?"
scene ep4_morning_talk_sage17 with dissolve
mc "I really stink with names..."
mc "Ashley...Ashley..."
menu:
    "Tall girl, blonde hair?" if True:
        mc "Oh! Tall girl, blonde hair?"
        scene ep4_morning_talk_sage16b with dissolve
        sa "Hm...no..."
    "Short girl, red hair?" if True:
        mc "Oh! Short girl, reddish hair?"
        scene ep4_morning_talk_sage16 with dissolve
        sa "Yeah, that's her."
        $ RPsage += 1
scene ep4_morning_talk_sage17 with dissolve
mc "And Lily...um..."
menu:
    "The Pink Rose" if True:
        mc "She works at The Pink Rose, right?"
        scene ep4_morning_talk_sage16b with dissolve
        sa "You know her that way, huh?"
        $ RPsage -= 1
    "The DIKs know her" if True:
        $ RPsage += 1
        mc "...she's a DIK recommendation, right?"
        scene ep4_morning_talk_sage16 with dissolve
        sa "I'm impressed. You're not so clueless."
    "I don't know her" if True:
        $ ep4_knowLily = False
        mc "I don't know her."
        scene ep4_morning_talk_sage16b with dissolve
        sa "All right."
scene ep4_morning_talk_sage17 with dissolve
mc "Are they new HOTs?"
scene ep4_morning_talk_sage16 with dissolve
sa "They might be, but I'll leave that decision to Quinn."
sa "You know...to test her with these sorts of tasks."
scene ep4_morning_talk_sage21 with dissolve
sa "Speaking of Quinn..."
sa "She mentioned you."
scene ep4_morning_talk_sage22 with dissolve
mc "She did?"
scene ep4_morning_talk_sage21 with dissolve
sa "Yeah. Do you like her or something?"
scene ep4_morning_talk_sage22 with dissolve
menu:
    "Yes" if True:
        $ ep4_likeQuinn = True
        mc "Yeah, I like her. She's...fun."
    "No" if True:
        $ ep4_likeQuinn = False
        mc "No. I really don't like Quinn."
    "How do you mean?" if True:
        mc "Like her? How do you mean?"
        scene ep4_morning_talk_sage21 with dissolve
        sa "You know... Like her, like her."
        scene ep4_morning_talk_sage22 with dissolve
        menu:
            "Yes" if True:
                $ ep4_likeQuinn = True
                mc "Well...yeah, I like her. You know, she's fun."
            "No" if True:
                $ ep4_likeQuinn = False
                mc "No, definitely not in that way."
if ep4_likeQuinn:
    $ bios_history_sage += "Sage asked me if I liked Quinn, I told her I did.\n\n"
elif True:
    $ bios_history_sage += "Sage asked me if I liked Quinn, I told her I didn't.\n\n"
$ bios_name_sage = True
$ chat_new_bios = True
scene ep4_morning_talk_sage24 with dissolve
sa "Interesting..."
mc "Why?"
scene ep4_morning_talk_sage21 with dissolve
sa "I think she likes you."
scene ep4_morning_talk_sage22 with dissolve
mc "Quinn? Haha, no way!"
scene ep4_morning_talk_sage21 with dissolve
sa "She didn't say it, but you pick up on the little things, you know?"
sa "She generally doesn't talk about guys that much, but, fuck me, she's been ranting a lot about you."
sa "I figured that you either got under her skin or that she likes you."
scene ep4_morning_talk_sage22 with dissolve
mc "It's probably the first one."
scene ep4_morning_talk_sage24 with dissolve
sa "It could be..."
sa "Although, no one really gets under her skin."
scene ep4_morning_talk_sage24b with dissolve
sa "But... Nah, forget it."
scene ep4_morning_talk_sage22 with dissolve
mc "Tell me."
scene ep4_morning_talk_sage21 with dissolve
sa "She seems to think that you're trying to ruin her fun. But the way she says it..."
sa "It's kind of like a cat chasing a mouse."
sa "Half of it is play and the other half is serious."
sa "What I'm trying to say is...chat her up if you're interested."
scene ep4_morning_talk_sage22 with dissolve
menu:
    "I'll think about it" if True:
        mc "I'll think about it."
    "Decline" if True:
        if dtype > 0:
            mc "Hell no. That's a hard pass."
        elif True:
            mc "No, thanks."
    "I'm more interested in you" if True:
        mc "I'm more interested in you..."
        $ guideSuggestedPage = 90
        scene ep4_morning_talk_sage24 with dissolve
        sa "Sorry... I'm taken. You know that."
        menu:
            "We almost fucked" if True:
                $ RPsage -= 1
                mc "You're taken? We almost fucked, if you remember."
                scene ep4_morning_talk_sage24b with dissolve
                sa "That wasn't about relationships. It was just about sex."
                sa "I was mad and horny. As I recall, you were ok with that."
                sa "If you want me to be your fuck buddy, you can't mix in emotions."
                scene ep4_morning_talk_sage24 with dissolve
                mc "Ok..."
                $ bios_history_sage += "Sage doesn't like it when I bring up the topic of relationships while talking about us.\n\n"
                $ bios_name_sage = True
                $ chat_new_bios = True
            "I was just saying" if True:
                mc "Yeah, I was just saying that I'm more interested in you than Quinn."
                mc "Nothing wrong with that."
                scene ep4_morning_talk_sage21 with dissolve
                sa "Fine."
$ guideSuggestedPage = 90
scene ep4_morning_talk_sage22 with dissolve
mc "About me staying here..."
mc "What will you tell the others?"
scene ep4_morning_talk_sage21 with dissolve
sa "In my experience, it's better to be upfront with all sisters."
sa "Rumors aren't good for anyone, and I'm not going to let them think I'm trying to hide you from them."
scene ep4_morning_talk_sage35 with dissolve
el "[name]? {i}Who{/i} are you doing here?"
scene ep4_morning_talk_sage36 with dissolve
menu:
    "Sage" if True:
        mc "Sage, of course."
        scene ep4_morning_talk_sage38 with dissolve
        el "Yeah, right."
        scene ep4_morning_talk_sage39 with dissolve
        sa "[name] is just fucking around. It's nothing like that."
    "No one" if True:
        mc "No one."
        scene ep4_morning_talk_sage38 with dissolve
        el "I don't believe you. It's probably Arieth."
        scene ep4_morning_talk_sage39 with dissolve
        sa "Very funny, Elena. It's nothing like that."
    "You interested?" if True:
        $ ep4_toldElenaInterested = True
        mc "Maybe you. Are you interested?"
        scene ep4_morning_talk_sage38 with dissolve
        el "Fat chance. But I'll tell John Boy that you asked that."
        scene ep4_morning_talk_sage39 with dissolve
        sa "[name] is just trying to be funny. It's nothing like that."
        $ bios_history_elena += "I made a joke about wanting to fuck Elena to her face, she told me she was going to tell John Boy about it.\n\n"
        $ bios_name_elena = True
        $ chat_new_bios = True
scene ep4_morning_talk_sage40 with dissolve
ml "Nothing like what?"
sar "Morning sisters...and someone's one-night stand."
sar "Where the fuck is Arieth?"
scene ep4_morning_talk_sage41 with dissolve
sa "Don't get any ideas. [name] is going to stay with me for a while."
sa "He's here because he had some roommate trouble."
scene ep4_morning_talk_sage42 with dissolve
ri "Roommate trouble? Again? Was it Troy this time, too?"
sa "No, it was Maya."
scene ep4_morning_talk_sage44 with dissolve
qu "What's that I hear? Haha!"
qu "A lover's spat between Ken doll and Barbie?"
scene ep4_morning_talk_sage45 with dissolve
menu:
    "Eat shit" if True:
        $ RPsage -= 1
        mc "Eat shit, Quinn."
        scene ep4_morning_talk_sage46 with dissolve
        sa "[name]! Don't talk to my sister like that."
        scene ep4_morning_talk_sage47 with dissolve
        qu "Haha! It's ok, Sage. Sweethearts have many names for each other..."
        if ep3_fuckedRionaQuinn:
            qu "Isn't that right, [mc_quinn]?"
            if mc_quinn != "pervert":
                scene ep4_morning_talk_sage48 with dissolve
                sa "..."
                scene ep4_morning_talk_sage47 with dissolve
        elif True:
            qu "Isn't that right, pervert?"
        $ bios_history_sage += "I insulted Quinn in front of Sage, she didn't like it.\n\n"
        $ bios_name_sage = True
        $ chat_new_bios = True
    "That joke is getting old" if True:
        mc "Very funny, Quinn. That's getting old, don't you think?"

        scene ep4_morning_talk_sage47 with dissolve
        qu "Which part of it? Me insinuating that you two are dolls that I can play with or that Maya looks like a bimbo?"
        scene ep4_morning_talk_sage45 with dissolve
        menu:
            "Mock her" if True:
                mc "Hey, I'd take a bimbo over a half-shaven rodent any day."
                scene ep4_morning_talk_sage46c with dissolve
                qu "Whatever..."
                scene ep4_morning_talk_sage47 with dissolve
            "Recite the HOT code" if True:
                mc "That doesn't sound like \"Don't turn on each other\" to me."
                scene ep4_morning_talk_sage46c with dissolve
                qu "Cute, but that code is reserved for real sisters."
                scene ep4_morning_talk_sage47 with dissolve
    "Say nothing" if True:
        $ renpy.pause(0.5)
        scene ep4_morning_talk_sage47 with dissolve
qu "Speaking of Maya... I have some mother-daughter time on my schedule."
scene ep4_morning_talk_sage49b with dissolve
qu "*{i}Whispers{/i}* We need to talk after that. Dawe dropped by and it's not good."
scene ep4_morning_talk_sage51 with dissolve
sa "Don't forget about Lily and Ashley."
qu "I got it!"
scene ep4_morning_talk_sage52 with dissolve
ml "Sage? What's this rumor about Chad getting kicked out of the jocks? Is it true?"
sar "Yeah? I saw it on Rooster!"
scene ep4_morning_talk_sage53 with dissolve
sa "We'll see."
scene ep4_morning_talk_sage52 with dissolve
ml "So, it's not true?"
scene ep4_morning_talk_sage53 with dissolve
sa "He's made some stupid decisions lately. I'm looking into it."
sa "It doesn't look very good."
scene ep4_morning_talk_sage54 with dissolve
sar "Your buddies will be happy to hear that, huh?"
scene ep4_morning_talk_sage55 with dissolve
menu:
    "Leave me out of this" if True:
        mc "Leave me out of this."
    "He deserved it" if True:
        mc "He got what he deserved and more."
scene ep4_morning_talk_sage56 with dissolve
ml "I find it very interesting that they say it was your fault."
if ep3_chad_fight_won:
    ml "Impressive how you managed to beat him up and get him in trouble for it..."
elif True:
    ml "Chad beating you up so hard he almost got expelled..."
    scene ep4_morning_talk_sage55 with dissolve
    mc "How's that my fault?"
scene ep4_morning_talk_sage53 with dissolve
sa "Melanie, be nice to our guest."
scene ep4_morning_talk_sage56 with dissolve
ml "It's just a rumor, of course."
scene ep4_morning_talk_sage55 with dissolve
mc "Stop getting your news from rumors."
scene ep4_morning_talk_sage62 with dissolve
sa "All right, I need to go find Mona. Talk to you later."
scene ep4_morning_talk_sage63 with dissolve
mc "Hey, can I use the shower?"
scene ep4_morning_talk_sage64 with dissolve
stop music fadeout 5
sa "Feel like home."
scene ep4_morning_talk_sage64b with dissolve
sa "Sisters...be nice to him."

label ep4_melanie_lewd_label:
$ guideSuggestedPage = 91
scene ep4_melanie_lewd with wipeleft
mc "(I remember this place...)"
mc "(I can't believe I'm stripping naked in here again.)"
scene ep4_melanie_lewd1 with dissolve
menu:
    "Call out" if True:
        mc "Hey, there's no one in here, right?"
        mc "..."
        mc "(Ok, I'm good.)"
    "Don't call out" if True:
        mc "(Shower time...)"
$ renpy.sound.play("sound_effects/shower.mp3", channel="sfx2", loop=True)
scene ep4_melanie_lewd2 with dissolve
mc "(These showers are tiny...)"
mc "(...but a lot cleaner than the co-ed showers.)"
scene ep4_melanie_lewd3 with dissolve
"Haha! Right?"
scene ep4_melanie_lewd4 with dissolve
mc "(Oh...)"
menu:
    "Warn them" if True:
        mc "Girls? I'm in the shower."
        play sound "sound_effects/shower_curtain.mp3"
        scene ep4_melanie_lewd5 with hpunch
        sar "Yep, sure looks like it."
        ml "Haha! Was that an invite?"
        scene ep4_melanie_lewd6 with dissolve
        menu:
            "Ask for privacy" if True:
                play sound "sound_effects/shower_curtain.mp3"
                scene ep4_melanie_lewd7 with hpunch
                mc "Fuck! Can I get some privacy?"
                ml "Where's the fun in that?"
                sar "Prude!"
                scene ep4_melanie_lewd12 with dissolve
                sar "I fail to understand why Sage would let you stay here, [name]."
                ml "Yeah! What did you do to earn that?"
                menu:
                    "I teach her to play guitar" if True:
                        mc "I teach her how to play the guitar and I needed her help."
                        sar "So, it's a trade?"
                        mc "No... Call it karma."
                        ml "It's just weird. It's the first time this has happened during my time here."
                        sar "It's not! Remember Dawe staying here with Arieth?"
                        ml "Oh, yeah!"
                        mc "What happened?"
                        sar "Long story short, it's ok for a guy to stay the night if he's a one-night stand..."
                        sar "...and Arieth thinks that fucking the same guy three nights in a row counts as three one-night stands."
                        ml "Hahaha! She's hilarious."
                    "None of your business" if True:
                        $ dk(1)
                        mc "That's none of your business."
                        sar "So, that's it? You're gonna be all Mr. Privacy while you're staying here?"
                        ml "Boring..."
            "Be confident ({color=#ffffff}{size=-1}{font=collegiate.ttf}DIK{/font}{/size} or {size=-1}Neutral{/size} affinity{/color})" if not affinity == "CHICK":
                scene ep4_melanie_lewd9 with dissolve
                mc "Yeah, whatever."
                sar "So... You're just gonna continue showering?"
                mc "Yeah? Why? Were you looking for another reaction?"
                scene ep4_melanie_lewd9b with dissolve
                sar "Quinn mentioned you were weird..."
                sar "Living up to that pervert rumor, huh?"
                scene ep4_melanie_lewd9 with dissolve
                mc "I'm the pervert? You're the ones standing there staring at my dick."
                mc "Now, either join or get out."
                scene ep4_melanie_lewd11 with dissolve
                sar "So stupid...right, Mel?"
                ml "Yeah... Really...stupid."
                jump ep4_melanie_lewd_label2
    "Don't warn them" if True:
        scene ep4_melanie_lewd12 with dissolve
        sar "You're going to the DIKs tomorrow, right?"
        ml "Yeah, you too?"
        sar "Yeah, what else would I do on a Friday?"
        scene ep4_melanie_lewd12b with dissolve
        ml "You could stay here waiting for Sage's fuck buddy to come."
        mc "(They know about that!?)"
        if ep2_fuckHOT:
            sar "I already fucked him once. That's enough for me."
            ml "You didn't enjoy it?"
            sar "I enjoy my thumb more."
            ml "He really was that small?"
            sar "Yeah! Tiniest cock I ever saw."
            ml "I thought that was just a rumor..."
            sar "You felt his cock with your foot; how come you didn't notice that?"
            ml "I was drunk as fuck."
        elif True:
            sar "Him? No fucking way! There are a bunch of rumors going around about him."
            ml "Like what?"
            sar "For one, I hear he has a tiny dick."
            ml "Are we talking \"Dawe tiny\"?"
            sar "Oh, definitely!"
        mc "(What the fuck is this!?)"
        scene ep4_melanie_lewd12 with dissolve
        sar "You know what else I heard about him?"
        ml "What?"
        sar "That he really doesn't get when someone is fucking with him."
        mc "(Huh?)"
        ml "We know you're in there, [name]."
        mc "That wasn't funny."
        sar "Hahah! I disagree!"
scene ep4_melanie_lewd13 with dissolve
sar "This guy showers longer than a girl."
stop music fadeout 3
ml "Hahaha!"
$ renpy.music.stop(channel="sfx2", fadeout=3)
mc "..."
jump ep4_jmq_label

label ep4_melanie_lewd_label2:
if _in_replay:
    hide screen phone_screen
    if persistent.name == None:
        $ name = "MC"
    elif True:
        $ name = persistent.name
    $ ep2_fuckHOT = True
scene ep4_melanie_lewd2 with dissolve
$ renpy.pause()
play sound "sound_effects/shower_curtain.mp3"
play music "music/ep3/some_obsession.mp3"
scene ep4_melanie_lewd14 with dissolve
mc "Hey...?"
scene ep4_melanie_lewd15 with dissolve
ml "*{i}Whispers{/i}* Shh..."
ml "*{i}Whispers{/i}* I hope you don't mind some company."
menu:
    "Leave" if not _in_replay:
        $ dk(-2)
        $ ep4_fuckedMelanie = False
        stop music fadeout 3
        scene ep4_melanie_lewd16 with dissolve
        $ renpy.music.stop(channel="sfx2", fadeout=3)
        mc "Nope, not interested."
        jump ep4_jmq_label
    "Go for it" if True:
        $ dk(2)
        $ ep4_fuckedMelanie = True
        mc "(It's not like it matters who I fuck anymore...)"
scene ep4_melanie_lewd17 with dissolve
mc "Not at all..."
scene ep4_melanie_lewd18 with dissolve
ml "*{i}Whispers{/i}* Try to stay quiet..."
scene ep4_melanie_lewd19 with dissolve
sar "Hey, [name]?"
mc "Yeah?"
scene anim_ml_bj_ep4 with dissolve
sar "I fail to understand why Sage would let you stay here."
$ guideSuggestedPage = 92
menu:
    "I teach her to play guitar" if True:
        mc "Hngh..."
        mc "I...uh...teach her how to play the guitar and I needed her help."
        sar "So, it's a trade?"
        mc "No... Call it kaaaaarma."
        sar "What?"
        mc "Karma!"
    "None of your business" if True:
        $ dk(1)
        mc "That's none of....hngh...your business."
        sar "Come on... If you're going to stay here, you could share some info with us."
pause
scene anim_ml_bj2_ep4 with dissolve
mc "*{i}Whispers{/i}* Fuck, it feels great, Melanie."
ml "*{i}Whispers{/i}* It's Mel. *{i}Schlurp{/i}*"
pause
scene ep4_melanie_lewd20 with dissolve
ml "*{i}Whispers{/i}* Come on... Give it to me."
scene ep4_melanie_lewd21 with dissolve
mc "(Shit...this is really hot.)"
menu:
    "Assjob" if True:
        scene anim_ml_assjob_ep4 with dissolve
        pause
        sar "Mel? My conditioner is empty, do you have any in yours?"
        ml "Yes...yes..."
        sar "Then pass it here!"
        ml "No! It's empty...sorry!"
        sar "Never mind then..."
        scene anim_ml_assjob2_ep4 with dissolve
    "Thighjob" if True:
        scene anim_ml_thighjob_ep4 with dissolve
        pause
        sar "Mel? My conditioner is empty, do you have any in yours?"
        ml "Yes...yes..."
        sar "Then pass it here!"
        ml "No! It's empty...sorry!"
        sar "Never mind then..."
        scene anim_ml_thighjob2_ep4 with dissolve
ml "*{i}Muffled moan{/i}*"
pause
menu:
    "Vaginal" if True:
        scene ep4_melanie_lewd23 with dissolve
        ml "Mmmm... Yes..."
        sar "What's that?"
        scene anim_ml_doggy_ep4 with dissolve
        ml "*{i}Moans{/i}* Oh, God... I...uh..."
        pause
        scene anim_ml_doggy2_ep4 with dissolve
        ml "I...hngh...um...nothing!"
        sar "What!?"
        pause
        scene anim_ml_doggy2b_ep4 with dissolve
        ml "Don't stop..."
        pause
        play sound "sound_effects/shower_curtain.mp3"
        scene ep4_melanie_lewd24 with hpunch
    "Anal" if True:
        scene ep4_melanie_lewd22 with dissolve
        ml "Shit...wrong hole!"
        ml "What are you serious?"
        sar "What happened?"
        scene anim_ml_anal_ep4 with dissolve
        ml "Hngh... Nothing! I uh...fuck..."
        pause
        scene anim_ml_doggy2_ep4 with dissolve
        sar "What!?"
        ml "My...hngh...conditioner is empty."
        sar "You just said that."
        pause
        scene anim_ml_anal2_ep4 with dissolve
        ml "You're stretching my asshole..."
        play sound "sound_effects/shower_curtain.mp3"
        scene ep4_melanie_lewd24 with hpunch
sar "What!? You sneaky slut!"
sar "Are you two for real?"
scene ep4_melanie_lewd26 with dissolve
ml "Hey! Have you ever heard of privacy?"
scene ep4_melanie_lewd27 with dissolve
sar "You're such a slut!"
scene ep4_melanie_lewd28 with dissolve
sar "Haha! And you, too!"
sar "What are you waiting for? Go on."
scene ep4_melanie_lewd30 with dissolve
mc "You wanna watch us fuck?"
ml "Just shut up and fuck me already."
scene anim_ml_doggy3_ep4 with dissolve
if ep2_fuckHOT:
    ml "You already had your fun with him."
ml "I'm not gonna share him with you, you know that?"
sar "Greedy!"
pause
scene anim_ml_sar_mast_ep4 with dissolve
sar "*{i}Moans{/i}* Fuck!"
ml "Haha! Are you getting off to us?"
sar "Don't mind me, just keep fucking him."
pause
scene anim_ml_doggy3_ep4 with dissolve
$ tmpInt = 0
label ep4_mel_loop_label:
menu:
    "Doggystyle" if tmpInt != 4:
        $ tmpInt = 4
        scene anim_ml_doggy6_ep4 with dissolve
        pause
        jump ep4_mel_loop_label
    "Doggystyle (anal)" if tmpInt != 5:
        $ tmpInt = 5
        scene anim_ml_doggy7_ep4 with dissolve
        sar "Yes...fuck her asshole..."
        sar "You fucking like that, don't you?"
        ml "Yes! Fuck! YES!!!"
        pause
        jump ep4_mel_loop_label
    "Lift her leg up" if tmpInt != 1:
        $ tmpInt = 1
        scene anim_ml_doggy5_ep4 with dissolve
        sar "Wow, You two are really going at it!"
        ml "Faster! Faster! Don't you dare fucking stop!"
        sar "This is so fucking hot..."
        pause
        jump ep4_mel_loop_label
    "Spank her" if tmpInt != 2:
        $ tmpInt = 2
        scene bg anim_ml_spank_ep4 movie with dissolve
        ml "Ahhh!"
        sar "Yes! Spank the shit out of her!"
        sar "That's so hot!!! HARDER!"
        ml "AHHHH!!! YES!"
        pause
        jump ep4_mel_loop_label
    "Have Sarah help" if tmpInt != 3:
        $ tmpInt = 3
        scene anim_sar_rub_ep4 with dissolve
        sar "Here let me help you get off..."
        ml "*{i}Moans{/i}* Yes!!!"
        sar "Keep fucking her, [name]."
        pause
        scene anim_sar_rub2_ep4 with dissolve
        sar "Let's make her cum together!"
        pause
        ml "Ahhh!!! I'm cumming!!!"
        scene ep4_melanie_lewd31 with hpunch
        $ renpy.pause(0.5)
        scene ep4_melanie_lewd31 with hpunch
        $ renpy.pause(0.5)
        scene ep4_melanie_lewd31 with hpunch
        ml "FUCK!!! YES!!!"
        ml "Wow..."
        jump ep4_mel_loop_label
    "Cum" if True:
        mc "Hey, get ready! I'm cumming!"
        menu:
            "Inside (vaginal)" if True:
                scene anim_ml_doggy6_ep4 with dissolve
                ml "Fill me up, [name]! I want your load inside my pussy!"
                pause
                scene ep4_melanie_lewd32 with hpunch
                $ renpy.pause(0.5)
                scene ep4_melanie_lewd32 with hpunch
                $ renpy.pause(0.5)
                scene ep4_melanie_lewd32 with hpunch
                mc "Ahh!!!"
                scene ep4_melanie_lewd33 with dissolve
                sar "You let him cum inside you!? You're such a whore!"
                if ep2_fuckHOT:
                    ml "I'm the whore? HAHA! You told me you let him do that to you, too!"
                    sar "Hahah!"
                ml "Fuck me... That was so good!"
            "Inside (anal)" if True:
                scene anim_ml_doggy7_ep4 with dissolve
                ml "Just shoot it into me, [name]! Fill me up!"
                pause
                scene ep4_melanie_lewd34 with hpunch
                $ renpy.pause(0.5)
                scene ep4_melanie_lewd34 with hpunch
                $ renpy.pause(0.5)
                scene ep4_melanie_lewd34 with hpunch
                mc "Ahh!!!"
                scene ep4_melanie_lewd35 with dissolve
                sar "That's some really hot shit!"
                ml "*{i}Breathes heavily{/i}* Yeah..."
                ml "Did you enjoy the show?"
                sar "Fuck yes, I did..."
            "Face" if True:
                scene anim_ml_bj_ep4 with dissolve
                sar "Cum all over her pretty, slutty face!"
                scene anim_ml_cum_ep4 with dissolve
                mc "Ahhhh!!!"
                pause
                scene ep4_melanie_lewd36 with dissolve
                sar "Wow, you guys are kinky as fuck!"
                sar "I love it!"
                ml "Shit...that was the biggest dick I ever had..."
stop music fadeout 5
scene ep4_melanie_lewd37 with dissolve
$ renpy.music.stop(channel="sfx2", fadeout=3)
sar "I'm starting to think it's not so bad having a dude live here with us."
$ renpy.end_replay()
$ persistent.ep4_lewd_melanie = True
$ calcScenes()
$ bios_history_melanie += "I fucked Melanie while showering at the HOTs. Sarah watched us and masturbated to it. There seems to be some sort of friendly competition between the two.\n\n"
$ bios_name_melanie = True
$ bios_history_sarah += "Sarah masturbated to me and Melanie fucking in the shower. There seems to be some sort of friendly competition between the two.\n\n"
$ bios_name_sarah = True
$ chat_new_bios = True
jump ep4_jmq_label

label ep4_afternoon_sage_label:
scene ep4_afternoon_sage with wipeleft
play music "music/ep4/inspiring_acoustic.mp3"
sa "Hey...what's that?"
scene ep4_afternoon_sage1 with dissolve
mc "It's my beer for one of the Hell Week tasks."
mc "I need to finish it before Saturday night."
scene ep4_afternoon_sage2 with dissolve
sa "You're gonna be drunk while staying with me?"
scene ep4_afternoon_sage3 with dissolve
mc "No, just a bit tipsy...although...if I get drunk, I may be able to finish early."
mc "Is that a problem?"
scene ep4_afternoon_sage2 with dissolve
sa "No, go for it. No one here would care."
sa "We're having movie night tonight if you wanna join us."
scene ep4_afternoon_sage3 with dissolve
mc "Hmm..."
mc "I don't know. We're not gonna watch horror movies, right?"
scene ep4_afternoon_sage6 with dissolve
sa "Haha! If you're scared, I'll let you hold my hand."
scene ep4_afternoon_sage7 with dissolve
mc "It's not that. I have some memories I don't want to revisit at the moment..."
scene ep4_afternoon_sage8 with dissolve
sa "Don't fret; it's not a horror movie. It's just some stupid comedy."
sa "It's one of those things we do together once in a while as a group."
scene ep4_afternoon_sage9 with dissolve
mc "Oh...um..."
mc "The pledges aren't going to come, right?"
scene ep4_afternoon_sage10 with dissolve
sa "Actually, they will. Why do you ask?"
scene ep4_afternoon_sage9 with dissolve
mc "I'd rather not see Maya tonight. That's all."
scene ep4_afternoon_sage10 with dissolve
sa "We can probably make it just HOTs tonight."
sa "I'm gonna go check if I can set it up."
jump ep4_sage_freeroam_label

label ep4_movienight_notsage_label:
play music "music/ep4/merry_bay.mp3"
scene ep4_movienight_ns with wipeleft
mc "Hey!"
sa "You came!"
scene ep4_movienight_ns1 with dissolve
mc "Yeah, I felt like it."
mc "I'm up for anything that will take my mind off Maya."
scene ep4_movienight_ns2 with dissolve
sa "About that..."
sa "I'm sorry, but I couldn't cancel."
scene ep4_movienight_ns3 with dissolve
mc "What? Oh no..."
scene ep4_movienight with dissolve
jump ep4_movienight_label2

label ep4_movienight_label:
scene ep4_movienight with fade
label ep4_movienight_label2:
$ ep4_SageMovieEvent = True
qu "Are we ready to get this night started, sisters?"
qu "I brought some new daughters to present to you."
scene ep4_movienight3 with dissolve
sa "Hey... You're ok."
sa "You're with me."
mc "Ok..."
scene ep4_movienight5 with dissolve
qu "Not these ones, though! You already know Camila, Mona and...Maya. Right, [name]?"
scene ep4_movienight6 with dissolve
if not ep3_choseSage:
    mc "(What does she know...?)"
elif True:
    $ renpy.pause()
scene ep4_movienight7 with dissolve
qu "Now let me present our newest recruits!"
scene ep4_movienight8 with dissolve
qu "A welcome to the fiery semi-redhead, Ashley."
qu "You might recognize her from a party or two. I don't know what took her so long to pledge, but here she is."
scene ep4_movienight9 with dissolve
qu "This year we're adding a petite blonde to our roster. Give it up for Lily!"
qu "Apparently, she knows how to dance and would likely have smashed in the CUM-petition."
scene ep4_movienight10 with dissolve
ly "Tsk. I only dance for losers at work."
scene ep4_movienight11 with dissolve
qu "I'm sure you recognize some of those losers on campus."
scene ep4_movienight10 with dissolve
ly "Sorry, but I don't dance and tell."
scene ep4_movienight12 with dissolve
sa "Welcome, daughters."
scene ep4_movienight13 with dissolve
qu "Wait a bit, Sage. I'm not done yet."
qu "I found a last-minute recruit!"
qu "And let me tell you...this one is a really good one..."
scene ep4_movienight15 with dissolve
qu "Vice President Tommy's li'l sister, Josy!"
mc "(And there she is...)"
scene ep4_movienight16 with dissolve
he "What!? For real?"
he "You're Tommy's sister? We're practically sisters-in-law!"
js "Stepsister."
scene ep4_movienight18 with dissolve
sa "Hey, you look pale. Did you drink too much already?"
scene ep4_movienight19 with dissolve
mc "No, I just want to leave."
scene ep4_movienight22 with dissolve
stop music fadeout 3
sa "Ok! Movie time! We've waited long enough for you to get here."
scene ep4_movienight25 with fade
play music "music/ep2/jingle.mp3"
mc "..."
scene ep4_movienight26 with dissolve
$ renpy.pause()
scene ep4_movienight27 with dissolve
sa "*{i}Whispers{/i}* Did you see this movie before?"
scene ep4_movienight28 with dissolve
mc "*{i}Whispers{/i}* What? No..."
scene ep4_movienight27 with dissolve
sa "Ok. It just looks to me like you're more interested in watching Maya and Josy, for some reason."
scene ep4_movienight28 with dissolve
mc "..."
scene ep4_movienight31 with dissolve
sa "Cheer up. I don't like you like this."
scene ep4_movienight32 with dissolve
mc "I can't just magically cheer up. I feel like shit."
scene ep4_movienight33 with dissolve
sa "Welcome to the club."
sa "But you're wrong. It's possible."
sa "You've cheered me up in the past...multiple times."
sa "Although, I think most would bat an eye if we did what we did last time, right now."
scene ep4_movienight34 with dissolve
mc "Haha... Yeah, me too."
scene ep4_movienight33 with dissolve
sa "Let's play a game."
scene ep4_movienight34 with dissolve
mc "Don't you want to watch the movie?"
scene ep4_movienight33 with dissolve
sa "Fuck the movie. I'm bored."
sa "Besides, it looks like Arieth is the only one being entertained by it."
scene ep4_movienight36
ar "HAHAHAH!"
scene ep4_movienight34 with dissolve
mc "What game?"
scene ep4_movienight33 with dissolve
sa "Every time that Arieth laughs, you must drink."
scene ep4_movienight37b with dissolve
mc "Drink what?"
scene ep4_movienight53a with dissolve
mc "Where did that come from?"
scene ep4_movienight53 with dissolve
sa "Haha! Here."
scene ep4_movienight54 with dissolve
mc "What is it?"
scene ep4_movienight53 with dissolve
sa "Something stronger than beer."
scene ep4_movienight54 with dissolve
if dtype > 0:
    mc "I'm not looking to get fucked up...and I'm already buzzed."
elif True:
    mc "I'm not looking to get drunk...and I'm already tipsy."
scene ep4_movienight53 with dissolve
sa "Just share it with me."
$ guideSuggestedPage = 106
sa "It will make the movie so much better."
scene ep4_movienight54 with dissolve
menu:
    "Drink" if True:
        $ ep4_sage_drink = True
        scene ep4_movienight57b with dissolve
        sa "That's it."
        scene ep4_movienight36
        ar "HAHAHA! She fell right on her ass!"
        scene ep4_movienight57b with dissolve
        sa "Hahaha!"
        sa "You don't know what you just agreed to."
        $ bios_history_sage += "During the HOTs' movie night, Sage and I played a drinking game together.\n\n"
        $ bios_name_sage = True
        $ chat_new_bios = True
    "Don't drink" if True:
        $ ep4_sage_drink = False
        mc "Pass..."
        scene ep4_movienight58 with dissolve
        sa "Ok."
        $ bios_history_sage += "I didn't play Sage's drinking game during the HOTs' movie night.\n\n"
        $ bios_name_sage = True
        $ chat_new_bios = True
        jump ep4_movienight2_label

scene ep4_movienight38 with fade
sa "Hahah! It's so stupid."
mc "The bottle is almost empty. Hahaha!"
scene ep4_movienight38b with dissolve
ar "Shh!"
scene ep4_movienight38c with dissolve
sa "*{i}Whispers{/i}* Shh! Hahaha..."
play sound "sound_effects/slap.mp3"
scene ep4_movienight38c2 with vpunch
he "Stop it!"
qu "Hahaha!"
scene ep4_movienight38d with dissolve
sa "Hey, wanna play another game?"
scene ep4_movienight38e with dissolve
mc "Sure."
scene ep4_movienight38d with dissolve
sa "Look at all the HOTs in front of you."
scene ep4_movienight25 with dissolve
mc "Yeah?"
sa "Rate their asses."
mc "Are you serious?"
sa "Yeah. Tell me the ugliest and the hottest one."
mc "Oh wow..."

mc "The ugliest ass..."
label ep4_ass_loop2_label:
menu:
    "Look at their asses" if True:
        scene ep4_movienight_elena_ass with dissolve
        mc "(Elena...hm...)"
        scene ep4_movienight_sarah_ass with dissolve
        mc "(Sarah's ass...hm...)"
        scene ep4_movienight_melanie_ass with dissolve
        mc "(Melanie...)"
        scene ep4_movienight_riona_ass with dissolve
        mc "(Riona... There's a lot of asses to choose from...)"
        scene ep4_movienight_quinn_ass with dissolve
        mc "(Quinn's ass...)"
        scene ep4_movienight_mona_ass with dissolve
        mc "(Mona...)"
        scene ep4_movienight_camila_ass with dissolve
        mc "(Camila has a big one...)"
        scene ep4_movienight_ashley_ass with dissolve
        mc "(Ashley...hm...)"
        scene ep4_movienight_lily_ass with dissolve
        mc "(Lily's ass is pretty fit...)"
        scene ep4_movienight_heather_ass with dissolve
        mc "(Heather...)"
        scene ep4_movienight25 with dissolve
        jump ep4_ass_loop2_label
    "Ready to decide" if True:
        mc "Hm... Ok, the ugliest ass..."
menu:
    "Elena" if True:
        $ ep4_ugliest_ass = "Elena"
        scene ep4_movienight_elena_ass with dissolve
        mc "Elena. Yeah...that's not for me."
        $ bios_history_sage += "I told Sage that I think Elena has the ugliest ass of the HOTs.\n\n"
        $ bios_name_sage = True
        $ chat_new_bios = True
    "Sarah" if True:
        $ ep4_ugliest_ass = "Sarah"
        scene ep4_movienight_sarah_ass with dissolve
        mc "Sarah, it doesn't really stand out to me."
        $ bios_history_sage += "I told Sage that I think Sarah has the ugliest ass out of the HOTs.\n\n"
        $ bios_name_sage = True
        $ chat_new_bios = True
    "Melanie" if True:
        $ ep4_ugliest_ass = "Melanie"
        scene ep4_movienight_melanie_ass with dissolve
        mc "Melanie. It lacks shape."
        $ bios_history_sage += "I told Sage that I think Melanie has the ugliest ass out of the HOTs.\n\n"
        $ bios_name_sage = True
        $ chat_new_bios = True
    "Riona" if True:
        $ ep4_ugliest_ass = "Riona"
        scene ep4_movienight_riona_ass with dissolve
        mc "Riona. That ass does nothing for me."
        $ bios_history_sage += "I told Sage that I think Riona has the ugliest ass out of the HOTs.\n\n"
        $ bios_name_sage = True
        $ chat_new_bios = True
    "Quinn" if True:
        $ ep4_ugliest_ass = "Quinn"
        scene ep4_movienight_quinn_ass with dissolve
        mc "Quinn. Her ass sucks."
        $ bios_history_sage += "I told Sage that I think Quinn has the ugliest ass out of the HOTs.\n\n"
        $ bios_name_sage = True
        $ chat_new_bios = True
    "Mona" if True:
        $ ep4_ugliest_ass = "Mona"
        scene ep4_movienight_mona_ass with dissolve
        mc "Mona. Too plain."
        $ bios_history_sage += "I told Sage that I think Mona has the ugliest ass out of the HOTs.\n\n"
        $ bios_name_sage = True
        $ chat_new_bios = True
    "Camila" if True:
        $ ep4_ugliest_ass = "Camila"
        scene ep4_movienight_camila_ass with dissolve
        mc "Camila. It's way too big for me."
        $ bios_history_sage += "I told Sage that I think Camila has the ugliest ass out of the HOTs.\n\n"
        $ bios_name_sage = True
        $ chat_new_bios = True
    "Ashley" if True:
        $ ep4_ugliest_ass = "Ashley"
        scene ep4_movienight_ashley_ass with dissolve
        mc "Ashley. It's too flat."
        $ bios_history_sage += "I told Sage that I think Ashley has the ugliest ass out of the HOTs.\n\n"
        $ bios_name_sage = True
        $ chat_new_bios = True
    "Lily" if True:
        $ ep4_ugliest_ass = "Lily"
        scene ep4_movienight_lily_ass with dissolve
        mc "Lily. That's a bony ass."
        $ bios_history_sage += "I told Sage that I think Lily has the ugliest ass out of the HOTs.\n\n"
        $ bios_name_sage = True
        $ chat_new_bios = True
    "Heather" if True:
        $ ep4_ugliest_ass = "Heather"
        scene ep4_movienight_heather_ass with dissolve
        mc "Heather. It just looks a bit odd."
        $ bios_history_sage += "I told Sage that I think Heather has the ugliest ass out of the HOTs.\n\n"
        $ bios_name_sage = True
        $ chat_new_bios = True
    "I like all of them" if True:
        $ dk(-1)
        $ ep4_ugliest_ass = "All"
        scene ep4_movienight38e with dissolve
        mc "Honestly, I like all of them."
        scene ep4_movienight38e2 with dissolve
        sa "Booh."
        $ bios_history_sage += "I couldn't pick whose ass is the ugliest out of the HOTs.\n\n"
        $ bios_name_sage = True
        $ chat_new_bios = True
scene ep4_movienight38d with dissolve
sa "What about the hottest ass?"
label ep4_ass_loop_label:
scene ep4_movienight25 with dissolve
menu:
    "Look at their asses" if True:
        if not ep4_ugliest_ass == "Elena":
            scene ep4_movienight_elena_ass with dissolve
            mc "(Elena...hm...)"
        if not ep4_ugliest_ass == "Sarah":
            scene ep4_movienight_sarah_ass with dissolve
            mc "(Sarah's ass...hm...)"
        if not ep4_ugliest_ass == "Melanie":
            scene ep4_movienight_melanie_ass with dissolve
            mc "(Melanie...)"
        if not ep4_ugliest_ass == "Riona":
            scene ep4_movienight_riona_ass with dissolve
            mc "(Riona... There's a lot of asses to choose from...)"
        if not ep4_ugliest_ass == "Quinn":
            scene ep4_movienight_quinn_ass with dissolve
            mc "(Quinn's ass...)"
        if not ep4_ugliest_ass == "Mona":
            scene ep4_movienight_mona_ass with dissolve
            mc "(Mona...)"
        if not ep4_ugliest_ass == "Camila":
            scene ep4_movienight_camila_ass with dissolve
            mc "(Camila has a big one...)"
        if not ep4_ugliest_ass == "Ashley":
            scene ep4_movienight_ashley_ass with dissolve
            mc "(Ashley...hm...)"
        if not ep4_ugliest_ass == "Lily":
            scene ep4_movienight_lily_ass with dissolve
            mc "(Lily's ass is pretty fit...)"
        if not ep4_ugliest_ass == "Heather":
            scene ep4_movienight_heather_ass with dissolve
            mc "(Heather...)"
        jump ep4_ass_loop_label
    "Ready to decide" if True:
        mc "Hm... Ok, the hottest ass..."
menu:
    "Elena" if not ep4_ugliest_ass == "Elena":
        $ ep4_hottest_ass = "Elena"
        scene ep4_movienight_elena_ass with dissolve
        mc "Elena. Neat and petite."
        $ bios_history_sage += "I told Sage that I think Elena has the hottest ass out of the HOTs.\n\n"
        $ bios_name_sage = True
        $ chat_new_bios = True
    "Sarah" if not ep4_ugliest_ass == "Sarah":
        $ ep4_hottest_ass = "Sarah"
        scene ep4_movienight_sarah_ass with dissolve
        mc "Sarah. Yeah, definitely Sarah."
        $ bios_history_sage += "I told Sage that I think Sarah has the hottest ass out of the HOTs.\n\n"
        $ bios_name_sage = True
        $ chat_new_bios = True
    "Melanie" if not ep4_ugliest_ass == "Melanie":
        $ ep4_hottest_ass = "Melanie"
        scene ep4_movienight_melanie_ass with dissolve
        mc "Melanie. I love her skin."
        $ bios_history_sage += "I told Sage that I think Melanie has the hottest ass out of the HOTs.\n\n"
        $ bios_name_sage = True
        $ chat_new_bios = True
    "Riona" if not ep4_ugliest_ass == "Riona":
        $ ep4_hottest_ass = "Riona"
        scene ep4_movienight_riona_ass with dissolve
        mc "Riona, not even a fair competition."
        $ bios_history_sage += "I told Sage that I think Riona has the hottest ass out of the HOTs.\n\n"
        $ bios_name_sage = True
        $ chat_new_bios = True
    "Quinn" if not ep4_ugliest_ass == "Quinn":
        $ ep4_hottest_ass = "Quinn"
        scene ep4_movienight_quinn_ass with dissolve
        mc "Quinn. Her ass is the best."
        $ bios_history_sage += "I told Sage that I think Quinn has the hottest ass out of the HOTs.\n\n"
        $ bios_name_sage = True
        $ chat_new_bios = True
    "Mona" if not ep4_ugliest_ass == "Mona":
        $ ep4_hottest_ass = "Mona"
        scene ep4_movienight_mona_ass with dissolve
        mc "Mona. There's just something special about it."
        $ bios_history_sage += "I told Sage that I think Mona has the hottest ass out of the HOTs.\n\n"
        $ bios_name_sage = True
        $ chat_new_bios = True
    "Camila" if not ep4_ugliest_ass == "Camila":
        $ ep4_hottest_ass = "Camila"
        scene ep4_movienight_camila_ass with dissolve
        mc "Camila. It's huge and feels so soft...I think."
        $ bios_history_sage += "I told Sage that I think Camila has the hottest ass out of the HOTs.\n\n"
        $ bios_name_sage = True
        $ chat_new_bios = True
    "Ashley" if not ep4_ugliest_ass == "Ashley":
        $ ep4_hottest_ass = "Ashley"
        scene ep4_movienight_ashley_ass with dissolve
        mc "Ashley. She looks great in a jeans skirt."
        $ bios_history_sage += "I told Sage that I think Ashley has the hottest ass out of the HOTs.\n\n"
        $ bios_name_sage = True
        $ chat_new_bios = True
    "Lily" if not ep4_ugliest_ass == "Lily":
        $ ep4_hottest_ass = "Lily"
        scene ep4_movienight_lily_ass with dissolve
        mc "Lily. Her ass is so hot."
        $ bios_history_sage += "I told Sage that I think Lily has the hottest ass out of the HOTs.\n\n"
        $ bios_name_sage = True
        $ chat_new_bios = True
    "Heather" if not ep4_ugliest_ass == "Heather":
        $ ep4_hottest_ass = "Heather"
        scene ep4_movienight_heather_ass with dissolve
        mc "Heather. It looks so soft."
        $ bios_history_sage += "I told Sage that I think Heather has the hottest ass out of the HOTs.\n\n"
        $ bios_name_sage = True
        $ chat_new_bios = True
    "I don't wanna play" if True:
        $ dk(-1)
        $ ep4_hottest_ass = "None"
        mc "I don't wanna play this game."
        sa "Chill. It's just a game."
        $ bios_history_sage += "I couldn't pick one ass as the hottest out of the HOTs.\n\n"
        $ bios_name_sage = True
        $ chat_new_bios = True

scene ep4_movienight26 with dissolve
$ renpy.pause()
scene ep4_movienight38d with dissolve
sa "Hey... I thought it would serve as a good distraction."
scene ep4_movienight26 with dissolve
mc "Yeah..."
sa "Hey..."
scene ep4_movienight42 with dissolve
menu:
    "Hold her hand" if True:
        $ ep4_hold_sage_hand = True
        scene ep4_movienight43 with dissolve
        $ renpy.pause()
        scene ep4_movienight45 with dissolve
        sa "*{i}Whispers{/i}* Here. It would be pretty bad if they saw this."
        scene ep4_movienight47 with dissolve
        menu:
            "Put hand inside panties" if True:
                $ ep4_sage_horny = True
                scene ep4_movienight49 with dissolve
                sa "*{i}Whispers{/i}* You're lucky we have a blanket."
                scene ep4_movienight50 with dissolve
                sa "*{i}Whispers{/i}* Hngn... This is seriously a bad idea."
                scene ep4_movienight52 with dissolve
                $ renpy.pause()
                scene ep4_movienight50 with dissolve
                sa "*{i}Whispers{/i}* Are you trying to turn me on?"
                mc "*{i}Whispers{/i}* Is it working?"
                "*{i}Wet sounds{/i}*"
                sa "*{i}Whispers{/i}* You don't feel that?"
                scene ep4_movienight52 with dissolve
                sa "*{i}Whispers{/i}* Hngn..."
                scene ep4_movienight51 with dissolve
                sa "*{i}Whispers{/i}* Ok, stop that now..."
                sa "*{i}Whispers{/i}* I can't wait until this movie is over."
                sa "*{i}Whispers{/i}* I'm going to take you back to my room and let you fuck me senseless."
                $ bios_history_sage += "During the movie night, I held Sage's hand and touched her pussy. She got really horny from it.\n\n"
                $ bios_name_sage = True
                $ chat_new_bios = True
            "Just hold her hand" if True:
                scene ep4_movienight48 with dissolve
                $ renpy.pause()
                $ bios_history_sage += "During the movie night, I held Sage's hand.\n\n"
                $ bios_name_sage = True
                $ chat_new_bios = True
    "Don't hold her hand" if True:
        $ RPsage -= 1
        $ ep4_hold_sage_hand = False
        mc "I'm good..."
        scene ep4_movienight38e2 with dissolve
        sa "*{i}Sigh{/i}* Suit yourself. I'm trying here, you know."
        $ bios_history_sage += "I didn't hold Sage's hand during the movie night. She didn't like that.\n\n"
        $ bios_name_sage = True
        $ chat_new_bios = True

label ep4_movienight2_label:
scene ep4_movienight59 with fade
qu "That movie was shit!"
he "Worst crap I ever saw!"
scene ep4_movienight60 with dissolve
ml "Thanks for the movie night, I'm gonna go crash."
sar "Same."
if ep4_sage_horny:
    scene ep4_movienight61 with dissolve
    sa "Come! Let's brush our teeth together!"
    scene ep4_movienight63 with dissolve
    $ renpy.pause()
    jump ep4_sage_brush_label
elif True:
    if ep3_choseSage:
        scene ep4_movienight64 with dissolve
        stop music fadeout 5
        sa "Hey. Let's go."
        scene ep4_movienight66 with dissolve
        $ renpy.pause()
        jump ep4_friday_math_label
    elif True:
        scene ep4_movienight66 with dissolve
        stop music fadeout 5
        mc "Thanks for the movie night, I'm gonna head out."
        sa "Anytime..."
        jump ep4_friday_math_label


label ep4_sage_brush_label:
scene ep4_sage_brush with dissolve
sa "You're drunk."
mc "Right back at you."
sa "I hate brushing my teeth when I'm drunk."
mc "Why's that?"
scene ep4_sage_brush1 with dissolve
sa "There's just something about toothpaste and alcohol that tastes weird together."
sa "Just like orange juice and toothpaste."
scene ep4_sage_brush1b with dissolve
mc "I don't think toothpaste and anything are supposed to taste good together."
scene ep4_sage_brush1 with dissolve
sa "Haha, true."
scene ep4_sage_brush with dissolve
mc "I just realized something..."
mc "There's no way to look attractive while brushing your teeth."
scene ep4_sage_brush1 with dissolve
sa "Of course, there is."
scene ep4_sage_brush1b with dissolve
mc "Really? How?"
scene ep4_sage_brush2 with dissolve
sa "How about this?"
mc "Yeah, but that doesn't work for me."
scene ep4_sage_brush1 with dissolve
$ guideSuggestedPage = 107
sa "Haha, yeah, don't do that."
menu:
    "Do it" if True:
        $ RPsage += 1
        scene ep4_sage_brush4 with dissolve
        sa "Haha! NO! Stop that! HAHA!"
        sa "You're so stupid!"
        $ bios_history_sage += "Sage liked it when I was being goofy while brushing our teeth.\n\n"
        $ bios_name_sage = True
        $ chat_new_bios = True
    "Don't do it" if True:
        $ renpy.pause(0.5)
scene ep4_sage_brush5 with dissolve
sa "How about this?"
mc "Again...hot...but that won't work for me either."
scene ep4_sage_brush6 with dissolve
sa "What about now? Now you're attractive by association."
mc "Yeah!"
mc "This is really not practical, though."
scene ep4_sage_brush8 with dissolve
sa "*{i}Spits{/i}*"
menu:
    "Grab her ass" if True:
        $ dk(1)
        scene ep4_sage_brush9 with dissolve
        sa "Hey... Not in here."
        mc "Are you kidding? Your tits were hanging out; how's this any different?"
        scene ep4_sage_brush10b with dissolve
        sa "Hanging?"
        scene ep4_sage_brush10c with dissolve
        mc "You know what I mean."
        scene ep4_sage_brush10b with dissolve
        sa "Well, you're wrong! My breasts were..."
        scene ep4_sage_brush10d with dissolve
        sa "Ok, I'm too drunk to think of another word for hanging..."
    "Don't grab her ass" if True:
        $ dk(-1)
        scene ep4_sage_brush10b with dissolve
        sa "How gay are you?"
        scene ep4_sage_brush10c with dissolve
        mc "What?"
        scene ep4_sage_brush10b with dissolve
        sa "Why didn't you grab my ass just now?"
        scene ep4_sage_brush10c with dissolve
        mc "Did you want me to do that?"
        scene ep4_sage_brush10d with dissolve
        sa "No, but I expected you to."
if ep3_choseSage:
    stop music fadeout 3
    sa "Anyway...let's go to bed."
elif True:
    sa "Anyway...let's go to bed."
    stop music fadeout 3
    sa "I'm gonna put out a mattress for you, so you can stay the night after I'm done with you."

label ep4_sage_sex_label:
if _in_replay:
    hide screen phone_screen
    if persistent.name == None:
        $ name = "MC"
    elif True:
        $ name = persistent.name
    if persistent.mc_sage == None:
        $ mc_sage = name
    elif True:
        $ mc_sage = persistent.mc_sage
    if persistent.sage == None:
        $ sage = "Sage"
    elif True:
        $ sage = persistent.sage
    if persistent.ep4_lewd_sage_full:
        $ ep3_choseSage = True
    elif True:
        $ ep3_choseSage = False
    $ ep2QuinnSawYouAndSage = True
play music "music/ep4/jack_the_lumberer.mp3"
$ ep4_fuckedSage = True
scene ep4_sage_sex with dissolve
sa "Are you ready?"
scene ep4_sage_sexb with dissolve
mc "For what?"
scene ep4_sage_sex with dissolve
sa "For what? Haha... You know exactly what I mean."
scene ep4_sage_sexd with dissolve
$ renpy.pause()
scene ep4_sage_sexe with dissolve
mc "Are we going all the way this time?"
sa "Yeah, that whiskey made me really horny!"
sa "But we better keep the volume down, so the girls don't overhear us."
scene ep4_sage_sexd with dissolve
$ renpy.pause()
scene ep4_sage_sex1 with dissolve
mc "It's sexy being quiet and sneaking around."
scene ep4_sage_sex2 with dissolve
sa "You like that sort of sex? The forbidden kind?"
scene ep4_sage_sex1 with dissolve
mc "Forbidden?"
scene ep4_sage_sex2 with dissolve
sa "Maybe forbidden isn't the right word, but you know..."
sa "...when you fuck and there's a risk someone will catch you and there will be consequences if they do."
sa "Do you like that?"
scene ep4_sage_sex1 with dissolve
menu:
    "Yes" if True:
        $ ep4_sageLikeDaringSex = True
        mc "Yeah, that's very hot. Like public sex and whatnot?"
        scene ep4_sage_sex2 with dissolve
        sa "Yeah! Exactly!"
    "No" if True:
        $ ep4_sageLikeDaringSex = False
        mc "Nah, I'm more into doing it in private."
        scene ep4_sage_sex2 with dissolve
        sa "That can be fun too, but it lacks that extra spice."

scene ep4_sage_sex1 with dissolve
mc "You're weird. You wanna hide me, but almost getting caught turns you on?"
scene ep4_sage_sex8 with dissolve
sa "Never had a dirty little secret before?"
scene ep4_sage_sex9 with dissolve
mc "Not really. But when I had sex with my first...um...girlfriend..."
mc "...we had some risky sex."
scene ep4_sage_sex8 with dissolve
sa "Mmm... Tell me about it!"
scene ep4_sage_sex9 with dissolve
mc "We used to fuck when her parents were home."
scene ep4_sage_sex8 with dissolve
sa "Did they ever catch you?"
scene ep4_sage_sex9 with dissolve
mc "No. Though, I have a feeling they overheard but never said anything about it."
scene ep4_sage_sex12 with dissolve
sa "What about fucking outdoors?"
scene ep4_sage_sex9 with dissolve
mc "No, I've never done that. Unless you count a treehouse as outdoors..."
scene ep4_sage_sex14 with dissolve
play sound "sound_effects/footsteps_indoors.mp3"
"*{i}Footsteps{/i}*"
scene ep4_sage_sex8 with dissolve
sa "*{i}Whispers{/i}* Ok, for real... We should stay quiet."
scene ep4_sage_sex9 with dissolve
if ep2QuinnSawYouAndSage:
    mc "*{i}Whispers{/i}* What's the big deal? Quinn already saw us once before."
    scene ep4_sage_sex8 with dissolve
    sa "*{i}Whispers{/i}* Yeah, but it's cool. I talked to her about it. I don't want anyone else to find out."

scene ep4_sage_sex14 with dissolve
"*{i}Chatter{/i}*"
scene ep4_sage_sex15 with dissolve
sa "*{i}Whispers{/i}* Remove those clothes and join me..."
scene ep4_sage_sex16 with dissolve
sa "*{i}Whispers{/i}* That's more like it..."
scene ep4_sage_sex16b with dissolve
sa "*{i}Whispers{/i}* Now, what do you want to do to me?"
scene ep4_sage_sex17 with dissolve
mc "*{i}Whispers{/i}* Turn around. I want to pick up from where we left off."
scene ep4_sage_sex18 with dissolve
mc "*{i}Whispers{/i}* You're really wet..."
sa "*{i}Whispers{/i}* Yeah, I get wet easily when I'm turned on."
scene anim_sage_finger_ep4 with dissolve
sa "Oh God... Hngn...*{i}Moans{/i}*"
mc "*{i}Whispers{/i}* Hey, what happened to staying silent?"
sa "*{i}Whispers{/i}* I'm trying to, but it feels so good..."
pause
sa "*{i}Moans{/i}*"
mc "*{i}Whispers{/i}* Bury your face in the pillow or something."
scene anim_sage_finger2_ep4 with dissolve
sa "*{i}Muffled moans{/i}*"
mc "*{i}Whispers{/i}* That's better. Do you like this?"
sa "Mhm..."
pause
mc "*{i}Whispers{/i}* Hey, [sage]? Are you gonna stay silent if we change position?"
sa "Mhm..."
label ep4_sage_sex_loop_label:
menu:
    "Thigh fuck" if True:
        scene anim_sage_thigh_ep4 with dissolve
        sa "*{i}Whispers{/i}* Yes... Rub your cock against my wet pussy, [mc_sage]..."
        pause
        sa "*{i}Whispers{/i}* Are you gonna put it inside me now?"
        jump ep4_sage_sex_loop_label
    "69" if True:
        scene anim_sage_69_ep4 with dissolve
        sa "*{i}Schlurp{/i}* Mmm..."
        pause
        if ep3_choseSage:
            scene anim_sage_692_ep4 with dissolve
        sa "*{i}Schlurp{/i}* This was a great idea... It's way better than the...hngh...pillow..."
        if ep3_choseSage:
            pause
        scene anim_sage_693_ep4 with dissolve
        mc "*{i}Whispers{/i}* Keep that pace, [sage]..."
        mc "*{i}Whispers{/i}* Fuck, you taste so good!"
        pause
        jump ep4_sage_sex_loop_label
    "Continue" if True:
        $ renpy.pause(0.5)

scene ep4_sage_sex19 with dissolve
sa "*{i}Whispers{/i}* Ok, stop teasing me... Put it in..."
mc "*{i}Whispers{/i}* Are you sure you won't moan loudly when I do it?"
sa "*{i}Whispers{/i}* It's not that big-"
scene ep4_sage_sex20 with hpunch
sa "OH GOOOD-"
scene ep4_sage_sex21 with hpunch
mc "*{i}Whispers{/i}* For fuck's sake, [sage]! You have to control it better if we're gonna do this your way."
mc "*{i}Whispers{/i}* I'm not gonna move my hips until you stop moaning like that."
scene anim_sage_thigh2_ep4 with dissolve
sa "*{i}Muffled moans{/i}* Give it to me! Give it!!!"
mc "*{i}Whispers{/i}* Hey, did I say you could move?"
sa "*{i}Muffled moans{/i}* Mmm... Yes!"
scene anim_sage_thigh3_ep4 with dissolve
mc "(She's doing all the work right now...wow...)"
mc "(She's thrusting her hips so hard against me.)"
pause
scene anim_sage_thigh2_ep4 with dissolve
sa "OH FUCK-"
scene ep4_sage_sex21 with hpunch
mc "*{i}Whispers{/i}* Ok, this is not keeping you quiet!"
scene ep4_sage_sex22 with hpunch
mc "*{i}Whispers{/i}* Back into the pillow you go."
scene ep4_sage_sex23 with dissolve
menu:
    "Tease her asshole" if True:
        scene ep4_sage_sex24 with dissolve
        sa "*{i}Whispers{/i}* Oh, wow, what are you doing?"
        mc "*{i}Whispers{/i}* It's just a finger."
        sa "*{i}Whispers{/i}* I know where this is going."
        sa "*{i}Whispers{/i}* You must be out of your mind if you think that you can put that big cock in my ass."
        mc "*{i}Whispers{/i}* Why? You don't like that?"
        sa "*{i}Whispers{/i}* I do, but there's no way a fucking pillow will keep me quiet."
        scene ep4_sage_sex25 with dissolve
        mc "*{i}Whispers{/i}* I hear you... Let's do this instead..."
    "Don't tease her" if True:
        scene ep4_sage_sex25 with dissolve
        mc "*{i}Whispers{/i}* Here we go..."

scene anim_sage_doggy_ep4 with dissolve
mc "*{i}Whispers{/i}* Wow... I'm fully inside you now, [sage]."
sa "*{i}Muffled moans{/i}*"
pause
scene anim_sage_doggy3_ep4 with dissolve
sa "*{i}Muffled moans{/i}* Don't stop... Don't...stop!"
pause
scene anim_sage_doggy2_ep4 with dissolve
mc "*{i}Whispers{/i}* Your ass jiggles so fucking good on my cock."
pause
mc "*{i}Whispers{/i}* Are you ok there?"
scene anim_sage_doggy3_ep4 with dissolve
pause
mc "*{i}Whispers{/i}* [sage]?"
sa "*{i}Muffled moans{/i}* I'm gonna..."
scene ep4_sage_sex26 with hpunch
sa "*{i}Muffled moans{/i}* CUUM!!!"
mc "*{i}Whispers{/i}* Wow! Just like that?"
scene ep4_sage_sex27 with dissolve
sa "*{i}Whispers{/i}* This is so damn hot, [mc_sage]..."
sa "*{i}Whispers{/i}* Ok... Phew! I'm good to go again..."
sa "*{i}Whispers{/i}* How do you want me?"
scene ep4_sage_sex28 with hpunch
sa "*{i}Whispers{/i}* Whoa! Haha! Are you being rough with me now?"
mc "*{i}Whispers{/i}* I have to compensate somehow for having to stay silent."
scene ep4_sage_sex29 with dissolve
sa "*{i}Whispers{/i}* Putting that pillow on my face now wouldn't be very sexy..."
sa "*{i}Whispers{/i}* How are you gonna solve it this time?"
scene ep4_sage_sex30 with dissolve
mc "*{i}Whispers{/i}* Open up..."
sa "*{i}Suck suck{/i}* Now I see what you're going for..."
scene anim_sage_miss_ep4 with dissolve
mc "*{i}Whispers{/i}* That should keep you quiet..."
sa "*{i}Suck suck{/i}* Mmm... Don't count on it..."
pause
scene anim_sage_miss2_ep4 with dissolve
sa "*{i}Suck suck{/i}* Fuck me good, [mc_sage]..."
sa "*{i}Suck suck{/i}* I know how much you've wanted my pussy...and right now, it's yours..."
pause
mc "Mmm... Fuck..."
scene ep4_sage_sex29 with dissolve
sa "*{i}Whispers{/i}* Look who's having a hard time staying quiet now?"
sa "*{i}Whispers{/i}* Let's reverse the roles, shall we?"
scene ep4_sage_sex31 with dissolve
mc "*{i}Whispers{/i}* Haha, really?"
mc "*{i}Whispers{/i}* Ok, I'll play along. How are you gonna keep me quiet?"
scene ep4_sage_sex31b with dissolve
sa "*{i}Whispers{/i}* Like this..."
scene anim_sage_ride3_ep4 with dissolve
sa "*{i}Moans softly{/i}*"
pause
scene anim_sage_ride2_ep4 with dissolve
sa "*{i}Whispers{/i}* See how that works..."
pause
if ep3_choseSage:
    sa "*{i}Whispers{/i}* Ok, I need it harder..."
    scene anim_sage_ride_ep4 with dissolve
    mc "*{i}Whispers{/i}* Shit... Wow... Hey!"
    sa "*{i}Whispers{/i}* Shut up! Mmm... Eat that pillow if you can't!"
    pause
mc "*{i}Whispers{/i}* It's hot how you take control like this."
sa "*{i}Whispers{/i}* Wanna see what else I can do?"
mc "*{i}Whispers{/i}* Mmm... Yeah, what's that?"
scene anim_sage_reverse_ep4 with dissolve
mc "*{i}Whispers{/i}* Ah, mixing it up... I love it."
sa "*{i}Whispers{/i}* And I love the reverse cowgirl..."
sa "*{i}Whispers{/i}* It's just like doggystyle, but I'm in control..."
pause
scene anim_sage_reverse2_ep4 with dissolve
pause
sa "*{i}Whispers{/i}* That's right... You just lie there..."
mc "*{i}Whispers{/i}* Take it easy...don't go too fast."
sa "*{i}Whispers{/i}* Oh really?"
scene anim_sage_reverse2b_ep4 with dissolve
sa "*{i}Whispers{/i}* I'm in charge now..."
pause
mc "*{i}Whispers{/i}* That's what you think."
scene anim_sage_reverse3_ep4 with vpunch
sa "*{i}Moans{/i}* Fuck!"
sa "*{i}Whispers{/i}* You fucker! Yes! Don't stop!"
if ep3_choseSage:
    pause
    scene anim_sage_reverse4_ep4 with dissolve
sa "*{i}Moans{/i}* Keep going! I'm gonna cum again!"
pause
scene ep4_sage_sex32 with hpunch
sa "*{i}Moans{/i}* Ahhh!!"
sa "*{i}Whispers{/i}* Shit... [mc_sage]... You can't keep doing this to me..."
sa "*{i}Breathes heavily{/i}*"
sa "*{i}Whispers{/i}* You're spoiling me..."
label ep4_sage_sex_loop2_label:
menu:
    "Thigh fuck" if True:
        scene anim_sage_thigh_ep4 with dissolve
        pause
        scene anim_sage_thigh2_ep4 with dissolve
        pause
        scene anim_sage_thigh3_ep4 with dissolve
        pause
        jump ep4_sage_sex_loop2_label
    "69" if True:
        scene anim_sage_69_ep4 with dissolve
        pause
        if ep3_choseSage:
            scene anim_sage_692_ep4 with dissolve
            pause
        scene anim_sage_693_ep4 with dissolve
        pause
        jump ep4_sage_sex_loop2_label
    "Doggystyle" if True:
        scene anim_sage_doggy_ep4 with dissolve
        pause
        scene anim_sage_doggy2_ep4 with dissolve
        pause
        scene anim_sage_doggy3_ep4 with dissolve
        pause
        jump ep4_sage_sex_loop2_label
    "Missionary" if True:
        scene anim_sage_miss_ep4 with dissolve
        pause
        scene anim_sage_miss2_ep4 with dissolve
        pause
        jump ep4_sage_sex_loop2_label
    "Cowgirl" if True:
        scene anim_sage_ride2_ep4 with dissolve
        pause
        scene anim_sage_ride3_ep4 with dissolve
        pause
        if ep3_choseSage:
            scene anim_sage_ride_ep4 with dissolve
            pause
        jump ep4_sage_sex_loop2_label
    "Reverse cowgirl" if True:
        scene anim_sage_reverse_ep4 with dissolve
        pause
        scene anim_sage_reverse2_ep4 with dissolve
        pause
        scene anim_sage_reverse2b_ep4 with dissolve
        pause
        scene anim_sage_reverse3_ep4 with dissolve
        pause
        if ep3_choseSage:
            scene anim_sage_reverse4_ep4 with dissolve
            pause
        jump ep4_sage_sex_loop2_label
    "Cum" if True:
        menu:
            "Inside pussy" if True:
                scene anim_sage_reverse3_ep4 with dissolve
                mc "*{i}Whispers{/i}* Hey, I'm close to cumming..."
                sa "Cum for me, [mc_sage]..."
                sa "Fill my slutty pussy with your cum..."
                pause
                scene ep4_sage_sex34b with hpunch
                $ renpy.pause(0.5)
                scene ep4_sage_sex34b with hpunch
                $ renpy.pause(0.5)
                scene ep4_sage_sex34b with hpunch
                mc "Hngn... Shit!!!"
                scene ep4_sage_sex35b with dissolve
                sa "*{i}Breathes heavily{/i}* That's it...nice... *{i}Phew{/i}*"
                stop music fadeout 3
            "Face" if True:
                mc "*{i}Whispers{/i}* Hey, I'm close to cumming..."
                scene ep4_sage_sex33 with dissolve
                sa "*{i}Whispers{/i}* Here... I know the final way of making me shut up."
                scene anim_sage_bj_ep4 with dissolve
                sa "*{i}Suck suck{/i}*"
                pause
                scene anim_sage_bj2_ep4 with dissolve
                sa "*{i}Suck suck{/i}* Cum for me, [mc_sage]..."
                sa "*{i}Suck suck{/i}* Fill my slutty mouth with your cum..."
                pause
                scene ep4_sage_sex34 with hpunch
                $ renpy.pause(0.5)
                scene ep4_sage_sex34 with hpunch
                $ renpy.pause(0.5)
                scene ep4_sage_sex34 with hpunch
                mc "Hngn..."
                scene ep4_sage_sex35 with dissolve
                sa "Mmm..."
                scene ep4_sage_sex36 with dissolve
                sa "*{i}Gulp{/i}*"
                stop music fadeout 3
$ renpy.end_replay()
$ persistent.ep4_lewd_sage = True
if ep3_choseSage:
    $ persistent.ep4_lewd_sage_full = True
$ calcScenes()
scene ep4_sage_sex16c with dissolve
sa "Hahah...wow..."
scene ep4_sage_sex17 with dissolve
mc "How hot was that?"
scene ep4_sage_sex16b with dissolve
sa "It was everything I needed right now..."
sa "I'm impressed."
scene ep4_sage_sex17 with dissolve
mc "Haha, well, I'm not. You couldn't keep quiet for shit."
mc "I'd be surprised if no one heard us."
scene ep4_sage_sex16b with dissolve
sa "Maybe Quinn heard us, but other than that, I think we're good."
sa "Hey..."
scene ep4_sage_sex17 with dissolve
mc "Yeah?"
scene ep4_sage_sex43 with dissolve
sa "Fuck buddies."
scene ep4_sage_sex44 with vpunch
mc "Fuck buddies..."
scene ep4_sage_sex17 with dissolve
mc "Is sleeping in your bed a part of the deal?"
if not ep3_choseSage:
    scene ep4_sage_sex16c with dissolve
    sa "If it was, I wouldn't have put out that mattress for you."
play sound "sound_effects/shove.mp3"
scene ep4_sage_sex46 with hpunch
if ep3_choseSage:
    sa "Nope!"
mc "Whoa!"
scene ep4_sage_sex47 with dissolve
sa "Hahaha!"
mc "Hahaha!"
$ bios_history_sage += "Sage and I are fuck buddies... I fucked her for real and it was so good!\n\n"
$ bios_name_sage = True
$ chat_new_bios = True
jump ep4_friday_math_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
