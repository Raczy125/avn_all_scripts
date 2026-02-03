label ep4_night_talk_bella_label:
scene ep4_night_talk_bella with Fade(1.5,1.5,1.5)
play sound "sound_effects/teapot.mp3"
$ renpy.pause()
scene ep4_night_talk_bella1 with dissolve
isa "Here you go."
mc "Thank you."
scene ep4_night_talk_bella3 with dissolve
$ renpy.pause()
scene ep4_night_talk_bella2 with dissolve
isa "Do you want to tell me what happened?"
scene ep4_night_talk_bella3 with dissolve
mc "No."
scene ep4_night_talk_bella2 with dissolve
isa "You look very upset."
scene ep4_night_talk_bella3 with dissolve
mc "..."
scene ep4_night_talk_bella2 with dissolve
isa "You're usually much more..."
isa "...annoying."
scene ep4_night_talk_bella3 with dissolve
mc "Thanks..."
scene ep4_night_talk_bella2 with dissolve
isa "It was a joke."
scene ep4_night_talk_bella3 with dissolve
mc "Sorry, I'm not in a joking mood."
isa "..."
scene ep4_night_talk_bella2 with dissolve
isa "We can just sit in silence if you want?"
scene ep4_night_talk_bella3 with dissolve
mc "..."
scene ep4_night_talk_bella6 with dissolve
isa "Come with me."
scene ep4_night_talk_bella7 with dissolve
isa "If we're going to sit in silence, we might as well be comfortable."
scene ep4_night_talk_bella8 with dissolve
isa "That doesn't look comfortable."
scene ep4_night_talk_bella9 with dissolve
isa "Come here. Lie down."
scene ep4_night_talk_bella10 with dissolve
$ renpy.pause()
scene ep4_night_talk_bella11 with dissolve
isa "You've been drinking."
scene ep4_night_talk_bella12 with dissolve
mc "Yes, but not a lot."
scene ep4_night_talk_bella10 with dissolve
$ renpy.pause()
scene ep4_night_talk_bella11 with dissolve
isa "Don't you think talking about it will make you feel better?"
scene ep4_night_talk_bella12 with dissolve
mc "It will just make me feel angry again."
scene ep4_night_talk_bella11 with dissolve
isa "Those feelings fade with time."
isa "Sometimes you need an ear to vent to."
isa "Surely there's a reason you came to my place instead of a friend?"
scene ep4_night_talk_bella12 with dissolve
mc "You've helped me a lot. I think that's why."
mc "And you're genuine. Harsh...but genuine."
mc "I need that. Someone who doesn't lie and keep secrets from me."
scene ep4_night_talk_bella10 with dissolve
isa "..."
scene ep4_night_talk_bella11 with dissolve
isa "What is it you need help with?"
isa "Is there another problem with your roommate?"
scene ep4_night_talk_bella12 with dissolve
mc "I changed dorms...but yeah...another roommate problem."
scene ep4_night_talk_bella11 with dissolve
isa "Did you get into another fight, like two nights before?"
scene ep4_night_talk_bella20 with dissolve
mc "How did you know about that?"
mc "Oh..."
mc "Jill..."
mc "No, it's nothing like that."
scene ep4_night_talk_bella20b with dissolve
mc "Can you promise not to tell anyone about this? Even Jill...?"
scene ep4_night_talk_bella20c with dissolve
isa "I promise."
scene ep4_night_talk_bella20b with dissolve
mc "Remember that girl I told you about over lunch?"
scene ep4_night_talk_bella20c with dissolve
isa "Which one? The ex or the crush?"
scene ep4_night_talk_bella20b with dissolve
mc "The crush..."
mc "It turns out she's my roommate's girlfriend."
scene ep4_night_talk_bella20c with dissolve
isa "And your roommate, is he your friend?"
scene ep4_night_talk_bella20b with dissolve
mc "She."
scene ep4_night_talk_bella26 with dissolve
isa "Oh..."
scene ep4_night_talk_bella20b with dissolve
mc "And yeah. She is my friend...and maybe something more...or...was something more."
mc "I don't know."
scene ep4_night_talk_bella20c with dissolve
stop music fadeout 3
isa "Start from the beginning. You know you want to."
jump ep4_flashback_label

label ep4_night_talk2_bella_label:
play music "music/ep3/guitar_gentle.mp3"
scene ep4_night_talk2_bella with fade
isa "..."
mc "..."
$ guideSuggestedPage = 92
scene ep4_night_talk2_bella1 with dissolve
mc "Did I overreact?"
scene ep4_night_talk2_bella2 with dissolve
isa "Do you feel like you overreacted?"
scene ep4_night_talk2_bella with dissolve
menu:
    "Yes" if True:
        $ ep4_overreacted = True
        scene ep4_night_talk2_bella1 with dissolve
        mc "Yeah, kinda..."
    "No" if True:
        $ ep4_overreacted = False
        scene ep4_night_talk2_bella1 with dissolve
        mc "No. It didn't feel good, but I feel like I did the right thing."
scene ep4_night_talk2_bella2 with dissolve
isa "Then there's your answer."
scene ep4_night_talk2_bella1 with dissolve
mc "What would you have done?"
scene ep4_night_talk2_bella6 with dissolve
isa "When you get older, you don't act the same way as you do at your age."
isa "If you asked me now, I wouldn't be stupid enough to put myself into a position where I dated multiple girls at once."
isa "Who do you think you are? Casanova?"
scene ep4_night_talk2_bella5 with dissolve
mc "Who's that?"
scene ep4_night_talk2_bella6b with dissolve
isa "Never mind..."
scene ep4_night_talk2_bella5 with dissolve
mc "What about teenage you? What would she have done?"
scene ep4_night_talk2_bella6 with dissolve
isa "I can't deny that she might have been in that situation if she ever had found two guys to fall for."
scene ep4_night_talk2_bella5 with dissolve
menu:
    "She didn't?" if True:
        mc "She didn't?"
        scene ep4_night_talk2_bella6 with dissolve
        isa "No. Just one."
    "Thanks" if True:
        mc "I get it. Thanks."
        scene ep4_night_talk2_bella6 with dissolve
isa "Give it a rest and when it's not so fresh, find a way to forgive your friends and move on."
isa "It's the healthy thing to do."
isa "It's time to get some rest."
scene ep4_night_talk2_bella5 with dissolve
mc "Please..."
mc "A little while longer."
scene ep4_night_talk2_bella11 with dissolve
$ renpy.pause()
scene ep4_night_talk2_bella12 with dissolve
isa "*{i}Smack{/i}*"
stop music fadeout 3
scene ep4_night_talk2_bella13 with dissolve
$ renpy.pause()
$ bios_history_isabella += "After fighting with Josy and Maya, I went to stay with Bella.\n\n"
$ bios_history_mc += "After fighting with Josy and Maya, I went to stay with Bella.\n\n"
$ bios_name_isabella = True
$ bios_name_mc = True
$ chat_new_bios = True

label ep4_morning_talk_bella_label:
scene ep4_morning_talk_bella with Fade(2,2,2)
play music "music/ep2/by_your_side.mp3"

mc "..."
mc "(Oh...?)"
menu:
    "Look at her tits" if True:
        $ dk(1)
        scene ep4_morning_talk_bella2 with dissolve
        mc "(Wow...)"
        scene ep4_morning_talk_bella with dissolve
    "Don't risk it" if True:
        $ renpy.pause(0.5)

menu:
    "Stroke her cheek" if True:
        scene ep4_morning_talk_bella4 with dissolve
        isa "What are you doing?"
        scene ep4_morning_talk_bella5 with dissolve
        mc "Oh... Good morning!"
        scene ep4_morning_talk_bella4 with dissolve
        isa "Answer my question."
        scene ep4_morning_talk_bella5 with dissolve
        mc "I...don't know. I felt like doing this."
        scene ep4_morning_talk_bella4 with dissolve
        isa "Get up."
    "Say good morning" if True:
        mc "Good morning, Bella."
        scene ep4_morning_talk_bella7 with dissolve
        isa "Morning."
        scene ep4_morning_talk_bella6 with dissolve
        isa "Oh... Get up."

scene ep4_morning_talk_bella8 with wipeleft
mc "I never saw that you had such a nice pool!"
scene ep4_morning_talk_bella9 with dissolve
isa "You miss a lot when you're drunk."
scene ep4_morning_talk_bella10 with dissolve
mc "Shit! That reminds me..."
mc "My beer! I'm supposed to drink ten per day!"
mc "I need to get it from Maya's dorm..."
mc "...or have Derek pick it up, maybe."
isa "..."
mc "What do you think?"
scene ep4_morning_talk_bella11 with dissolve
isa "I think that the combination of you and alcohol isn't going to work out if you want to stay under my roof."
scene ep4_morning_talk_bella12 with dissolve
mc "But...but..."
scene ep4_morning_talk_bella11 with dissolve
isa "But, but."
scene ep4_morning_talk_bella12 with dissolve
mc "I have to!"
scene ep4_morning_talk_bella11 with dissolve
isa "How are they monitoring your alcohol consumption?"
scene ep4_morning_talk_bella10 with dissolve
mc "Hm...they don't really bother to check it. They expect me to drink the beers in the cooler...that's about it."
scene ep4_morning_talk_bella11 with dissolve
isa "Then how about pouring out the beer and saving the empty bottles?"
scene ep4_morning_talk_bella12 with dissolve
mc "I can't do that... That's cheating."
mc "..."
mc "They wouldn't know that."
scene ep4_morning_talk_bella11 with dissolve
isa "Right. You know..."
isa "...unless I told them."
scene ep4_morning_talk_bella10 with dissolve
mc "You wouldn't!"
mc "..."
mc "Would you?"
scene ep4_morning_talk_bella11 with dissolve
isa "And I thought it was the beer..."
scene ep4_morning_talk_bella12 with dissolve
mc "What?"
scene ep4_morning_talk_bella11 with dissolve
isa "Nothing."
scene ep4_morning_talk_bella20 with dissolve
mc "Hey!"
isa "Yes?"
mc "Do you ever swim in the pool?"
isa "I do."
scene ep4_morning_talk_bella18 with dissolve
mc "Can I?"
isa "You just ate."
mc "So?"
isa "You don't go swimming after you just ate."
mc "Why is that?"
scene ep4_morning_talk_bella19 with dissolve
isa "Supposedly, you can get cramps."
scene ep4_morning_talk_bella18 with dissolve
mc "Hah, really? Who would have known?"
isa "You can swim after school."
mc "Cool! Will you join me?"
isa "Perhaps."
stop music fadeout 3
isa "Finish your breakfast. I don't want to be late."
jump ep4_jmq_label

label ep4_afternoon_bella_label:
scene ep4_afternoon_bella with wipeleft
play music "music/ep4/inspiring_acoustic.mp3"
mc "Honey! I'm home!"
scene ep4_afternoon_bella1 with dissolve
mc "Hey! Where are you going?"
scene ep4_afternoon_bella1b with dissolve
$ renpy.pause()
scene ep4_afternoon_bella15 at transformTop
mc "(Wow!)"
$ guideSuggestedPage = 99
scene ep4_afternoon_bella15b with dissolve
mc "(Holy hell!)"
scene ep4_afternoon_bella15c with dissolve
menu:
    "Compliment her" if True:
        if dtype > 0:
            $ RPisabella -= 1
            mc "You look so fucking hot, Bella."
            scene ep4_afternoon_bella17 with dissolve
            isa "Careful!"
        elif True:
            mc "You look breathtaking."
            scene ep4_afternoon_bella17 with dissolve
            isa "Breathtaking? What the hell is wrong with you?"
    "Don't compliment her" if True:
        $ renpy.pause(0.5)
scene ep4_afternoon_bella2 with dissolve
mc "Is it pool time?"
scene ep4_afternoon_bella3 with dissolve
isa "I thought you weren't going to drink those beers."
scene ep4_afternoon_bella2 with dissolve
mc "I haven't."
scene ep4_afternoon_bella3 with dissolve
isa "But you will."
scene ep4_afternoon_bella2 with dissolve
mc "It's just such a shame to let them go to waste."
scene ep4_afternoon_bella7 with dissolve
isa "Pass me one."
scene ep4_afternoon_bella8 with dissolve
mc "For real?"
scene ep4_afternoon_bella7 with dissolve
isa "If you don't mind."
scene ep4_afternoon_bella8 with dissolve
mc "Of course not!"
scene ep4_afternoon_bella9 with dissolve
$ renpy.pause()
play sound "sound_effects/bottle_open.mp3"
scene ep4_afternoon_bella10 with dissolve
mc "Nice..."
play sound "sound_effects/bottle_open.mp3"
scene ep4_afternoon_bella11 with dissolve
mc "Cheers!"
scene ep4_afternoon_bella12 with dissolve
isa "If you throw up in the pool, you're cleaning it."
mc "Deal! Let me go and get changed."
jump ep4_freeroam_bella_label

label ep4_bella_pool_label:
scene ep4_afternoon_bella18 with fade
play music "music/ep4/inspiring_acoustic.mp3"
mc "Hey! I'm back."
scene ep4_afternoon_bella19 with dissolve
isa "What are you waiting for? Go ahead and jump in the pool."
scene ep4_afternoon_bella18 with dissolve
mc "Will you join me?"
scene ep4_afternoon_bella19 with dissolve
isa "Not at the moment."
scene ep4_afternoon_bella18 with dissolve
mc "Then I can wait."
scene ep4_afternoon_bella23 with dissolve
mc "Sunbathing, huh?"
scene ep4_afternoon_bella24 with dissolve
isa "There aren't many more chances to get a tan before fall."
scene ep4_afternoon_bella23b with dissolve
mc "Is that sunblock I see over there?"
scene ep4_afternoon_bella24 with dissolve
$ guideSuggestedPage = 104
isa "Yes. And I already put it on, so keep it in your pants."
scene ep4_afternoon_bella23 with dissolve
menu:
    "You missed a spot" if True:
        mc "But you missed a spot..."
        scene ep4_afternoon_bella24 with dissolve
        isa "I don't think so."
    "I asked for me" if True:
        mc "I was really asking for me."
        scene ep4_afternoon_bella25 with dissolve
        isa "Oh... Do you want some?"
        mc "No, I'm good."
        scene ep4_afternoon_bella27 with dissolve
        isa "..."
scene ep4_afternoon_bella23 with dissolve
mc "I never got why people like to sunbathe..."
scene ep4_afternoon_bella24 with dissolve
isa "Do you understand the concept of a tan?"
scene ep4_afternoon_bella23 with dissolve
menu:
    "Lecture her" if True:
        $ ep4_lecturedBella = True
        mc "I understand it perfectly."
        mc "Do you understand that the sun irreversibly destroys collagen and gives you wrinkles?"
        scene ep4_afternoon_bella24 with dissolve
        isa "You're such a charmer."
        scene ep4_afternoon_bella23 with dissolve
    "Of course" if True:
        $ ep4_lecturedBella = False
        mc "Of course."
mc "I just don't understand why you have to lie still while doing it."
mc "You could be up and about, kick a ball around or you know...swim in the pool."
scene ep4_afternoon_bella32 with dissolve
isa "I'll tell you what. Let me just get 10 minutes on my back, and I'll join you for a swim."
$ guideSuggestedPage = 105
scene ep4_afternoon_bella33 with dissolve
menu:
    "Help her with the sunblock" if True:
        label ep4_bella_lewd_label:
        if _in_replay:
            hide screen phone_screen
            if persistent.name == None:
                $ name = "MC"
            elif True:
                $ name = persistent.name
            if persistent.mc_isabella == None:
                $ mc_isabella = name
            elif True:
                $ mc_isabella = persistent.mc_isabella
            if persistent.isabella == None:
                $ isabella = "Isabella"
            elif True:
                $ isabella = persistent.isabella
            $ ep4_lecturedBella = True
            scene ep4_afternoon_bella33 with dissolve
            play music "music/ep4/inspiring_acoustic.mp3"
        mc "You're not gonna put sunblock on your back?"
        scene ep4_afternoon_bella34 with dissolve
        if ep4_lecturedBella:
            isa "I should, right? Or I'll get those nasty back wrinkles from collagen destruction."
            scene ep4_afternoon_bella33 with dissolve
            mc "See? Now you get it!"
            scene ep4_afternoon_bella34 with dissolve
        isa "Maybe I already put it on?"
        scene ep4_afternoon_bella33 with dissolve
        mc "Hey... I get the hint."
        scene ep4_afternoon_bella36 with dissolve
        isa "Here. Only on my back, ok?"
        scene ep4_afternoon_bella37 with dissolve
        menu:
            "Arms" if True:
                scene anim_bella_arms_ep4 with dissolve
                mc "Gotta get some sunblock on those arms."
                isa "You don't have to narrate."
                mc "I know I don't have to; I just didn't want to take you by surprise."
                pause
                menu:
                    "Back" if True:
                        scene anim_bella_back_ep4 with dissolve
                        mc "Look at that, b-e-a-utiful."
                        isa "Are you done?"
                        menu:
                            "Ass" if True:
                                $ RPisabella -= 1
                                scene ep4_afternoon_bella40 with dissolve
                                isa "That's NOT my back!"
                                scene ep4_afternoon_bella41 with dissolve
                                isa "And you're done."
                                mc "Whoops..."
                                $ bios_history_isabella += "I helped Bella put on sunblock, but I got too hands-on with her.\n\n"
                                $ bios_name_isabella = True
                                $ chat_new_bios = True
                            "Done" if True:
                                $ RPisabella += 1
                                mc "Yeah... I'm done."
                                isa "Thank you."
                    "Ass" if True:
                        $ RPisabella -= 1
                        scene ep4_afternoon_bella40 with dissolve
                        isa "That's NOT my back!"
                        scene ep4_afternoon_bella41 with dissolve
                        isa "And you're done."
                        mc "Whoops..."
                        $ bios_history_isabella += "I helped Bella put on sunblock, but I got too hands-on with her.\n\n"
                        $ bios_name_isabella = True
                        $ chat_new_bios = True
            "Back" if True:
                scene anim_bella_back_ep4 with dissolve
                mc "Your back's going to need a lot of sunblock."
                isa "Lucky me."
                menu:
                    "Arms" if True:
                        scene anim_bella_arms_ep4 with dissolve
                        mc "Can't forget about those arms..."
                        isa "*{i}Exhales{/i}* Mmm..."
                        menu:
                            "Ass" if True:
                                $ RPisabella += 1
                                scene anim_bella_ass_ep4 with dissolve
                                isa "Hey..."
                                isa "..."
                                scene ep4_afternoon_bella41 with dissolve
                                isa "That's enough."
                                $ bios_history_isabella += "I helped Bella put on sunblock and I played a bit with her ass. I think she liked it...\n\n"
                                $ bios_name_isabella = True
                                $ chat_new_bios = True
                            "Done" if True:
                                $ RPisabella += 1
                                mc "Yeah... I'm done."
                                isa "Thank you."
                                $ bios_history_isabella += "I helped Bella put on sunblock and she liked it.\n\n"
                                $ bios_name_isabella = True
                                $ chat_new_bios = True
                    "Ass" if True:
                        $ RPisabella -= 1
                        scene ep4_afternoon_bella40 with dissolve
                        isa "That's NOT my back!"
                        scene ep4_afternoon_bella41 with dissolve
                        isa "And you're done."
                        mc "Whoops..."
                        $ bios_history_isabella += "I helped Bella put on sunblock, but I got too hands-on with her.\n\n"
                        $ bios_name_isabella = True
                        $ chat_new_bios = True
            "Ass" if True:
                $ RPisabella -= 1
                scene ep4_afternoon_bella40 with dissolve
                isa "That's NOT my back!"
                scene ep4_afternoon_bella41 with dissolve
                isa "And you're done."
                mc "Whoops..."
                $ bios_history_isabella += "I helped Bella put on sunblock, but I got too hands-on with her.\n\n"
                $ bios_name_isabella = True
                $ chat_new_bios = True
        scene ep4_afternoon_bella_mc with dissolve
        mc "Wanna do me next?"
        scene ep4_afternoon_bella_mc1 with dissolve
        isa "What did you just ask me?"
        scene ep4_afternoon_bella_mc with dissolve
        mc "My back... Will you put some sunblock on it?"
        scene ep4_afternoon_bella_mc3 with dissolve
        mc "This is life, Bella."
        scene ep4_afternoon_bella_mc5 with dissolve
        isa "..."
        scene ep4_afternoon_bella_mc3b with dissolve
        mc "Hey... Thank you for all of this."
        mc "Letting me stay here really helped me take my mind off things."
        scene ep4_afternoon_bella_mc7 with dissolve
        isa "It's not a hotel, you know?"
        scene ep4_afternoon_bella_mc3 with dissolve
        mc "Haha!"
        mc "Great! Then I don't have to pay you for the stay."
        scene ep4_afternoon_bella_mc7 with dissolve
        isa "Very funny."
        isa "Are you going to find a new dorm soon?"
        scene ep4_afternoon_bella_mc3b with dissolve
        mc "I hope that the DIKs will have a place for me to stay next week."
        mc "If I pass their tests that is."
        scene ep4_afternoon_bella_mc7 with dissolve
        isa "Good. You can stay here until then."
        scene ep4_afternoon_bella_mc12 with dissolve
        mc "I really appreciate that!"
        scene ep4_afternoon_bella_mc12b with dissolve
        $ renpy.pause()
        scene ep4_afternoon_bella_mc13 with dissolve
        isa "..."
        scene ep4_afternoon_bella_mc14 with dissolve
        $ renpy.pause()
    "Don't help her" if True:
        $ renpy.pause(0.5)

scene ep4_afternoon_bella_mc15 with dissolve
mc "Want another beer?"
scene ep4_afternoon_bella_mc17 with dissolve
mc "Jill told me that you two drink wine together. You know, wine tasting?"
scene ep4_afternoon_bella_mc18 with dissolve
isa "It happens."
scene ep4_afternoon_bella_mc17 with dissolve
mc "What's the deal with that?"
scene ep4_afternoon_bella_mc18 with dissolve
isa "With tasting wine?"
isa "We do it to discover new wines to enjoy."
scene ep4_afternoon_bella_mc21 with dissolve
mc "Ah. Ok..."
mc "Do you spit or swallow?"
scene ep4_afternoon_bella_mc22 with hpunch
isa "*{i}Coughs{/i}* What!?"
scene ep4_afternoon_bella_mc23 with dissolve
mc "The wine, I mean..."
mc "(She's got a dirty mind...)"
isa "Yeah, I got that."
isa "We swallow."
scene ep4_afternoon_bella_mc25 with dissolve
mc "Nice."
scene ep4_afternoon_bella_mc26 with dissolve
isa "The wine, I mean..."
scene ep4_afternoon_bella_mc25 with dissolve
mc "Hahah!"
scene ep4_afternoon_bella43 with dissolve
mc "Ok! Time's up! Let's go swimming."
scene ep4_afternoon_bella44 with dissolve
isa "After you."
play sound "sound_effects/water_splash.mp3"
$ renpy.sound.play("sound_effects/water_pool.mp3", channel="sfx1", loop=True)
scene ep4_afternoon_bella47 with vpunch
mc "The water is perfect! Jump in!"
scene ep4_afternoon_bella49 with dissolve
mc "Booh! That's not how you jump into a pool."
scene ep4_afternoon_bella50 with dissolve

isa "I don't want to get my hair wet."
scene ep4_afternoon_bella51 with dissolve
menu:
    "Splash her" if True:
        mc "Oh. That's too bad."
        play sound "sound_effects/water_splash.mp3"
        scene ep4_afternoon_bella52 with vpunch
        $ renpy.pause()
        scene ep4_afternoon_bella53 with dissolve
        isa "Hey! What did I just say?"
        scene ep4_afternoon_bella55 with dissolve
        mc "Hahaha!"
        isa "..."
        $ RPisabella += 1
        $ bios_history_isabella += "I splashed water on Bella in the pool for fun. I think she enjoyed it.\n\n"
        $ bios_name_isabella = True
        $ chat_new_bios = True
    "Don't splash her" if True:
        mc "Don't be like that! It will dry again."
scene ep4_afternoon_bella56 with dissolve
$ renpy.music.stop(channel="sfx1", fadeout=3)
mc "Do you ever just lie here floating like this?"
isa "No. Never."
mc "You should."
mc "It's very calming."
isa "I'm glad you feel calm."
mc "Yeah... Me too."
scene ep4_afternoon_bella57 with dissolve
mc "Oh. I must have drifted."
scene ep4_afternoon_bella58 with dissolve
mc "Sorry."
menu:
    "Take it further" if True:
        $ ep4_bella_lewd = True
    "Stop" if not _in_replay:
        $ ep4_bella_lewd = False
        scene ep4_afternoon_bella58b with dissolve
        $ renpy.pause()
        scene ep4_afternoon_bella58c with dissolve
        isa "I'm going to grab a shower."
        stop music fadeout 3
        mc "Go ahead, I want to swim some more."
        $ bios_history_isabella += "I didn't make a move on Bella in the pool.\n\n"
        $ bios_name_isabella = True
        $ chat_new_bios = True
        jump ep4_dinner_bella_label
stop music fadeout 3
scene ep4_afternoon_bella59 with dissolve
$ renpy.pause()
scene ep4_afternoon_bella60 with dissolve
mc "No..."
mc "I feel bad for kissing you yesterday."
mc "I'm not going to force it."
play music "music/ep4/all_of_the_pieces.mp3"
scene ep4_afternoon_bella61 with dissolve
isa "..."
mc "..."
scene ep4_afternoon_bella62 with dissolve
$ renpy.pause()
scene ep4_afternoon_bella61 with dissolve
mc "This...feels nice."
mc "I didn't think I needed a hug like this..."
isa "(I needed a hug like this...)"
isa "(Why can't I stop thinking these dirty thoughts about him...?)"
isa "(All these words that I'd never dare tell him...)"
isa "(It's adultery...isn't it?)"
isa "(Can I just decide to move on?)"
scene ep4_afternoon_bella62 with dissolve
isa "(What if James comes home?)"
isa "(Would he blame me if I did this?)"
isa "(After all this time?)"
isa "(I have forgiven him...)"
scene ep4_afternoon_bella61 with dissolve
isa "(It's just an urge, Bella...)"
isa "(It's like...like...like a sneeze!)"
isa "(You just need to hold it in...)"
scene ep4_afternoon_bella62 with dissolve
isa "(Who am I kidding...?)"
isa "(You can't hold a sneeze in...)"
scene ep4_afternoon_bella65 with dissolve
isa "(Not when the urge is this big...)"
isa "(I'm...going to do it...)"
isa "(I need to do it...)"
isa "(It's time to do it.)"
scene ep4_afternoon_bella61 with dissolve
mc "Bella... I think I'm getting-"
scene ep4_afternoon_bella65 with dissolve
isa "Shh..."
scene ep4_afternoon_bella66 with dissolve
$ renpy.pause()
scene ep4_afternoon_bella68 with dissolve
isa "*{i}Deep breath{/i}*"
scene ep4_afternoon_bella66 with dissolve
$ renpy.pause()
scene ep4_afternoon_bella67 with dissolve
$ renpy.pause()
scene ep4_afternoon_bella68 with dissolve
isa "*{i}Deep breath{/i}*"
scene anim_hj_bella_ep4 with dissolve
$ renpy.pause()
scene ep4_afternoon_bella68 with dissolve
isa "*{i}Deep breath{/i}*"
isa "(I'm doing it!)"
isa "(I'm really doing it!)"
scene anim_hj_bella_ep4 with dissolve
$ renpy.pause()
scene anim_kiss_bella_ep4 with dissolve
$ renpy.pause()
scene anim_hj_bella_ep4 with dissolve
$ renpy.pause()
scene ep4_afternoon_bella60 with dissolve
$ renpy.pause()
scene ep4_afternoon_bella70 with dissolve
mc "(Where's she going?)"
scene ep4_afternoon_bella71 with dissolve
$ renpy.pause()
scene ep4_afternoon_bella72 with dissolve
$ renpy.pause()
scene ep4_afternoon_bella73 with dissolve
$ renpy.pause()
scene ep4_afternoon_bella74 with dissolve
$ renpy.pause()
scene ep4_afternoon_bella75 with dissolve
$ renpy.pause()
scene ep4_afternoon_bella76 with dissolve
$ renpy.pause()
scene ep4_afternoon_bella76b with dissolve
$ renpy.pause()
scene ep4_afternoon_bella77 with dissolve
$ renpy.pause()
scene ep4_afternoon_bella78 with dissolve
$ renpy.pause()
scene ep4_afternoon_bella79 with dissolve
$ renpy.pause()
scene ep4_afternoon_bella80 with dissolve
$ renpy.pause()
scene ep4_afternoon_bella82 with dissolve
$ renpy.pause()
scene anim_hj2_bella_ep4 with dissolve
$ renpy.pause()
scene anim_hj3_bella_ep4 with dissolve
$ renpy.pause()
scene anim_tits_bella_ep4 with dissolve
$ renpy.pause()
label ep4_bella_loop_label:
menu:
    "Play with her tits" if True:
        scene anim_tits_bella_ep4 with dissolve
        $ renpy.pause()
        jump ep4_bella_loop_label
    "Handjob" if True:
        scene anim_hj2_bella_ep4 with dissolve
        $ renpy.pause()
        scene anim_hj3_bella_ep4 with dissolve
        $ renpy.pause()
        jump ep4_bella_loop_label
    "Squeeze her ass" if True:
        scene anim_squeeze_bella_ep4 with dissolve
        $ renpy.pause()
        jump ep4_bella_loop_label
    "Touch her face" if True:
        scene ep4_afternoon_bella90 with dissolve
        $ renpy.pause()
        scene anim_suck_bella_ep4 with dissolve
        $ renpy.pause()
        jump ep4_bella_loop_label
    "Cum" if True:
        mc "*Breathing intensifies*"
scene anim_hj4_bella_ep4 with dissolve
$ renpy.pause()
scene anim_cum_bella_ep4 with dissolve
$ renpy.pause()
scene ep4_afternoon_bella88 with dissolve
$ renpy.pause()
scene ep4_afternoon_bella89 with dissolve
$ renpy.pause()
stop music fadeout 3
scene ep4_afternoon_bella90 with dissolve
isa "..."
$ bios_history_isabella += "Bella and I shared a silent and sexual moment in the pool and in her shower. It was amazing!\n\n"
$ bios_name_isabella = True
$ chat_new_bios = True
$ renpy.end_replay()
$ persistent.ep4_lewd_bella = True
$ calcScenes()

label ep4_after_lewd_bella_label:
scene ep4_after_lewd_bella1 with Fade(2,1.5,2)
play music "music/ep2/journey_of_hope.mp3"
mc "..."
isa "..."
scene ep4_after_lewd_bella with dissolve
mc "Are we not gonna talk about what happened?"
scene ep4_after_lewd_bella1 with dissolve
isa "..."
mc "Ok..."
mc "Just an FYI...I really enjoyed it."
scene ep4_after_lewd_bella with dissolve
mc "But I'm sensing that you didn't...?"
scene ep4_after_lewd_bellab with dissolve
isa "It's not that simple."
scene ep4_after_lewd_bella5 with dissolve
mc "Um...I think it is."
mc "You either enjoy something or you don't..."
mc "...or you think it's meh."
mc "Was it meh?"
scene ep4_after_lewd_bellab with dissolve
isa "Eat your dinner."
scene ep4_after_lewd_bella5 with dissolve
mc "Fine...I'll stop."
jump ep4_dinner_bella_label2
label ep4_dinner_bella_label:
scene ep4_after_lewd_bella5 with fade
label ep4_dinner_bella_label2:
if not ep4_bella_lewd:
    play music "music/ep2/journey_of_hope.mp3"
mc "This is a nice tasting meal..."
mc "Those have been few and far between these days."
scene ep4_dinner_bella2 with dissolve
isa "What do you usually eat?"
scene ep4_after_lewd_bella5 with dissolve
mc "Cafeteria food, microwaved things, cold food, sandwiches..."
mc "That kind of food."
scene ep4_dinner_bella2 with dissolve
isa "There are kitchens at campus, why aren't you using them?"
scene ep4_after_lewd_bella5 with dissolve
mc "I'm not good at it."
mc "I mean, I know the basics, but I'm no cook."
mc "I'd probably set the whole place on fire and nobody would want that."
scene ep4_dinner_bella2 with dissolve
isa "No one is born a cook. Like everything in life, it takes practice."
scene ep4_dinner_bella7 with dissolve
mc "And interest..."
scene ep4_dinner_bella6 with dissolve
isa "That's true. Wouldn't you like to get better at it?"
scene ep4_dinner_bella7 with dissolve
mc "I guess."
mc "..."
mc "Could you teach me?"
scene ep4_dinner_bella6 with dissolve
isa "I suppose."
if ep4_wateringPoints > 8:
    $ RPisabella += 2
    $ ep4_wateringSatisfaction = "GREAT"
    scene ep4_dinner_bella6b with dissolve
    isa "By the way, I would like to thank you for watering my plants."
    isa "I was pleasantly surprised. You did a great job."
    if ep4_bellaDishes:
        $ RPisabella += 1
        isa "Also, thanks for the help with the dishes."
        $ bios_history_isabella += "Bella was really thankful for the help with watering her plants and doing her dishes.\n\n"
        $ bios_name_isabella = True
        $ chat_new_bios = True
    elif True:
        isa "Thank you."
        $ bios_history_isabella += "Bella was really thankful for the help with watering her plants.\n\n"
        $ bios_name_isabella = True
        $ chat_new_bios = True
    if not persistent.ep4_card13:
        $ renpy.block_rollback()
        $ persistent.ep4_card13 = True
        $ persistent.rew_sage_unlocked += 1
        $ chat_new_rewards = True
        $ calcRenders()
        show screen srmsg
        $ renpy.pause(3)
        hide screen srmsg
    scene ep4_dinner_bella7 with dissolve
    if ep2_helpedBellaKitchen or ep2_helpedBellaFrame1 or ep2_helpedBellaFrame2 or ep2_helpedBellaFrame3 or ep2_bellaStudy:
        mc "You're welcome. I figured I would do a better job helping you in a semi-sober state."
    elif True:
        mc "You're welcome."
elif ep4_wateringPoints > 4:
    $ RPisabella += 1
    $ ep4_wateringSatisfaction = "GOOD"
    scene ep4_dinner_bella6b with dissolve
    isa "By the way, I would like to thank you for watering my plants."
    isa "You did a good job."
    if ep4_bellaDishes:
        $ RPisabella += 1
        isa "Also, thanks for the help with the dishes."
    elif True:
        isa "Thank you."
    scene ep4_dinner_bella7 with dissolve
    if ep2_helpedBellaKitchen or ep2_helpedBellaFrame1 or ep2_helpedBellaFrame2 or ep2_helpedBellaFrame3 or ep2_bellaStudy:
        mc "You're welcome. I figured I would do a better job helping you in a semi-sober state."
    elif True:
        mc "You're welcome."
    $ bios_history_isabella += "Bella was thankful for the help with watering her plants and doing her dishes. It wasn't perfect, but she was happy about it.\n\n"
    $ bios_name_isabella = True
    $ chat_new_bios = True
elif ep4_wateringPoints <= 4 and ep4_plantsWatered > 4:
    $ RPisabella -= 1
    $ ep4_wateringSatisfaction = "POOR"
    isa "And while we're at it, I might as well show you how to water plants..."
    isa "...because I will have to replace several of them."
    isa "You watered them way too much."
    scene ep4_dinner_bella7 with dissolve
    mc "Whoops... I'm sorry."
    if ep2_helpedBellaKitchen or ep2_helpedBellaFrame1 or ep2_helpedBellaFrame2 or ep2_helpedBellaFrame3 or ep2_bellaStudy:
        mc "I thought I would do a better job helping you in a semi-sober state."
        mc "Apparently not."
    if ep4_bellaDishes:
        $ RPisabella += 1
        scene ep4_dinner_bella6 with dissolve
        isa "But thanks for the help with the dishes."
        $ bios_history_isabella += "Bella wasn't happy that I ruined her plants when I tried to water them... At least she liked that I helped her with the dishes.\n\n"
        $ bios_name_isabella = True
        $ chat_new_bios = True
    elif True:
        $ bios_history_isabella += "Bella wasn't happy that I ruined her plants when I tried to water them...\n\n"
        $ bios_name_isabella = True
        $ chat_new_bios = True

scene ep4_after_lewd_bella5 with dissolve
mc "Hey... I just remembered something..."
mc "You never told me about Derek's reputation."
scene ep4_dinner_bella2 with dissolve
isa "You really want to hear it?"
scene ep4_after_lewd_bella5 with dissolve
mc "Yeah, of course!"
scene ep4_dinner_bella2 with dissolve
isa "Ok..."
isa "They say that he's somewhat of a genius."
scene ep4_dinner_bella7 with dissolve
mc "..."
mc "Derek?"
scene ep4_dinner_bella6 with dissolve
isa "Yes."
scene ep4_dinner_bella7 with dissolve
mc "Shirtless Derek..."
mc "...with the dildo helmet?"
scene ep4_dinner_bella6 with dissolve
isa "That's Derek, all right."
scene ep4_after_lewd_bella5 with dissolve
mc "He's not a genius."
scene ep4_dinner_bella2 with dissolve
isa "Cathy was surprised, too."
isa "But he is passing her classes with flying colors."
scene ep4_after_lewd_bella5 with dissolve
mc "(Derek's cheating and they think he's a genius...)"
mc "(He really managed to fool them.)"
mc "Oh, good for him, then."
scene ep4_dinner_bella2 with dissolve
isa "Cathy cuts him some slack because of it."
scene ep4_dinner_bella7 with dissolve
mc "Jade doesn't."
scene ep4_dinner_bella6 with dissolve
isa "Well, she's a bit..."
isa "Never mind."
scene ep4_dinner_bella7 with dissolve
mc "Finish your sentence."
scene ep4_dinner_bella6c with dissolve
isa "\"Finish your sentence\"?"
scene ep4_dinner_bella7 with dissolve
mc "It sounds like something you would say to me."
if ep4_bella_lewd:
    mc "I think you're starting to rub me off."
    scene ep4_dinner_bella6c with dissolve
    isa "What?"
    mc "...r-rub off on me."
elif True:
    mc "I think you're starting to rub off on me."
scene ep4_dinner_bella2 with dissolve
isa "Fine."
isa "Jade's a bit uptight."
isa "She's not as nice as Cathy..."
isa "...when it comes to students."
scene ep4_after_lewd_bella5 with dissolve
menu:
    "She's nice to me" if True:
        mc "She's been nothing but nice to me."
        scene ep4_dinner_bella2 with dissolve
        isa "Well, you're no Derek."
    "Do you like her?" if True:
        mc "Do you like Jade? I picked up on something in your tone."
        scene ep4_dinner_bella2 with dissolve
        isa "Let's not get into it."
        scene ep4_after_lewd_bella5 with dissolve
        mc "That sounded like a no to me."
        scene ep4_dinner_bella2 with dissolve
        if ep4_bella_lewd:
            isa "Once again, eat your dinner."
        elif True:
            isa "Eat your dinner."
        $ bios_history_isabella += "Bella doesn't seem to like Jade...\n\n"
        $ bios_name_isabella = True
        $ chat_new_bios = True

scene ep4_dinner_bella6 with dissolve
isa "I spoke to Jill over lunch."
isa "I heard you're going out on a date tomorrow."
scene ep4_dinner_bella7 with dissolve
mc "Yeah, that's right. We are."
mc "Are you ok with that?"
scene ep4_dinner_bella6 with dissolve
isa "Of course. I wouldn't have said so to her otherwise."
if ep4_bella_lewd:
    scene ep4_dinner_bella7 with dissolve
    mc "Yeah, but...after what happened today, between us..."
    mc "Doesn't that make you change your mind?"
    isa "..."
    scene ep4_dinner_bella6d with dissolve
    mc "It's just that she's your best friend."
    mc "Doesn't that make you feel weird? It makes me feel weird."
    scene ep4_dinner_bella6 with dissolve
    isa "Go out on a date with her."
    isa "What happened this afternoon...it was a one-time thing."
    scene ep4_dinner_bella7 with dissolve
    mc "Was it really?"
    scene ep4_dinner_bella6 with dissolve
    isa "It's not something Jill should know about or prevent you two from dating."
    scene ep4_dinner_bella7 with dissolve
    menu:
        "Make a move on her" if True:
            $ RPisabella += 1
            mc "Ok...but for what it's worth, it wasn't a one-time thing for me."
            mc "I think I want more..."
            scene ep4_dinner_bella30j with dissolve
            isa "..."
        "If you say so" if True:
            mc "If you say so..."
    $ bios_history_isabella += "Even though I was physical with Bella, she doesn't seem to care that I'm dating Jill.\n\n"
    $ bios_name_isabella = True
    $ chat_new_bios = True
scene ep4_dinner_bella2 with dissolve
isa "How about tonight? Any plans?"
isa "I'm assuming that you're not going to stay home and study during your Hell Week."
scene ep4_after_lewd_bella5 with dissolve
if ep4_called_sage:
    mc "I was invited to a movie night, but I'm gonna study a bit before that."
    scene ep4_dinner_bella2 with dissolve
    isa "I see."
    isa "I'll lend you a spare key if you promise not to lose it."
    scene ep4_after_lewd_bella5 with dissolve
    stop music fadeout 3
    mc "It's tough to promise such a thing, but I'll try."
elif True:
    mc "That was actually my plan."
    mc "We don't have any Hell Week activities planned for tonight."
    mc "So, I figured I could have a date with my books over some beer."
    scene ep4_dinner_bella2 with dissolve
    stop music fadeout 3
    isa "All right. I'll do the same..."

label ep4_bella_study_label:
scene ep4_bella_study with fade
play music "music/ep4/relax.mp3"
if minigames:
    menu:
        "Study English" if True:
            $ bonusPercentageEnglish += 10
            "+10%% score on your next English test.\nYour total bonus for the next test is [bonusPercentageEnglish]%%."
        "Study Math" if True:
            $ bonusPercentageMath += 10
            "+10%% score on your next Math test.\nYour total bonus for the next test is [bonusPercentageMath]%%."
        "Study Gender Studies" if True:
            $ bonusPercentageGender += 10
            "+10%% score on your next Gender Studies test.\nYour total bonus for the next test is [bonusPercentageGender]%%."
mc "(This is boring...)"
mc "(The only thing I get from this is that I know I don't wanna work with any of these subjects in the future...)"
scene ep4_bella_study1bb with dissolve
mc "(I have no clue if Bella is enjoying herself...)"
mc "(Haha! She could probably be reading a comedy or a thriller and still look the same.)"
scene ep4_bella_study with dissolve
if minigames:
    menu:
        "Study English" if True:
            $ bonusPercentageEnglish += 10
            "+10%% score on your next English test.\nYour total bonus for the next test is [bonusPercentageEnglish]%%."
        "Study Math" if True:
            $ bonusPercentageMath += 10
            "+10%% score on your next Math test.\nYour total bonus for the next test is [bonusPercentageMath]%%."
        "Study Gender Studies" if True:
            $ bonusPercentageGender += 10
            "+10%% score on your next Gender Studies test.\nYour total bonus for the next test is [bonusPercentageGender]%%."
mc "(Study...study...study...)"
mc "(I wonder when the fun classes will start.)"
mc "(Probably next semester...)"
scene ep4_bella_study2b with dissolve
mc "(It would be cool to take a science class!)"
mc "(Oh, and what Jill recommended me...economics.)"
mc "(Although that doesn't sound much fun.)"
mc "(The last time I took advice from someone with choosing a class I ended up listening to girls ranting...)"
scene ep4_bella_study4c with dissolve
mc "(Hm...shouldn't she have more books than this?)"
isa "Something the matter?"
scene ep4_bella_study5b with dissolve
mc "Huh? No."
scene ep4_bella_study5c with dissolve
isa "You've been studying for a while now; it seems like your head's not in it anymore."
scene ep4_bella_study5b with dissolve
mc "I was just looking at your bookshelf and I find it weird that you don't have more books."
mc "I know you have more upstairs, but still... I was expecting there to be a lot more."
scene ep4_bella_study5c with dissolve
isa "Because I'm a librarian?"
scene ep4_bella_study5b with dissolve
mc "Yeah!"
scene ep4_bella_study5c with dissolve
isa "I don't bring the library home with me."
isa "I keep the books I love and get rid of the ones I know I won't read again."
isa "And I have some space for new ones that I haven't had the time to enjoy."
scene ep4_bella_study5b with dissolve
mc "You read a book more than once?"
scene ep4_bella_study5c with dissolve
isa "Do you find it weird that people watch the same movies or listen to the same songs over and over, too?"
scene ep4_bella_study5b with dissolve
mc "No, but reading just seems like a bigger chore to me."
scene ep4_bella_study5d with dissolve
isa "It depends on what you read."
isa "There are a lot of boring books..."
isa "Poorly written books..."
isa "Self-indulgent drivel."
scene ep4_bella_study5c with dissolve
isa "You have to sift through a lot to find what you like."
isa "Once you find a certain genre or author that speaks to you..."
isa "...you'll notice that there are so many you want to read that you didn't see before."
scene ep4_bella_study5b with dissolve
mc "All we do in school is reading."
mc "It gets tiresome, and my head always feels full afterward."
scene ep4_bella_study5c with dissolve
isa "When you read to learn, it's the learning part that takes its toll on you."
isa "Reading for enjoyment is different, but I understand where you're coming from."
isa "I rarely read novels when I went to college. It was mostly just class literature."
isa "The real passion for reading came to me later on in life."
scene ep4_bella_study5b with dissolve
mc "That's interesting. I have one passion in my life..."
mc "Music...and that's a big one."
if ep4_playedGuitar:
    $ RPisabella += 1
    scene ep4_bella_study5e with dissolve
    isa "I heard you play before."
    scene ep4_bella_study5f with dissolve
    mc "You did? I thought you were outside."
    scene ep4_bella_study5e with dissolve
    isa "I went inside for a glass of water and heard you play."
    isa "It was beautiful. I wouldn't mind hearing more of it."
    scene ep4_bella_study5f with dissolve
    mc "(That was a real compliment...)"
    mc "(Funny how it means a lot to hear that from her.)"
    mc "Thank you."
    $ bios_history_isabella += "Bella overheard when I played guitar in her house; she liked it.\n\n"
    $ bios_name_isabella = True
    $ chat_new_bios = True
if ep4_called_sage:
    mc "I should go get ready for the movie night."
    scene ep4_bella_study5e with dissolve
    isa "All right, I'll go get that spare key for you."
    stop music fadeout 3
    scene ep4_bella_study25 with dissolve
    $ renpy.pause()
    jump ep4_movienight_notsage_label
elif True:
    scene ep4_bella_study5e with dissolve
    isa "Are you feeling tired?"
    scene ep4_bella_study5f with dissolve
    mc "Yeah, I'm starting to."
    scene ep4_bella_study5e with dissolve
    isa "Let's go then. I'll help you turn the sofa into a bed."
    stop music fadeout 3
    scene ep4_bella_study25 with dissolve
    $ renpy.pause()
    jump ep4_friday_math_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
