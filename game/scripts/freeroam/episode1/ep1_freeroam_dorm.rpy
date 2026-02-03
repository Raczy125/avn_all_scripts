label ep1_freeroam_dorm_label:
$ freeRoamID = 2
$ bios_isabella = True
$ bios_name_isabella = True
$ bios_history_isabella = "I met Isabella today. She doesn't talk much. Maybe that's why she's a librarian?\n\n"
$ chat_new_bios = True
$ game_money_available = True
if persistent.ep1_card16:
    $ brawler_render_available = False
elif True:
    $ brawler_render_available = True
$ brawler_money_available = True
$ brawler_skillpoint_available = True
scene d1_evening with wipeleft
$ loopMusic = True
$ queueChanCallback()
mc "(Let's hope he's in a better mood now.)"
menu:
    "Say hey" if True:
        if dtype > 0:
            mc "What's up, Troy? Doing good?"
        elif True:
            mc "Hi, Troy!"
        scene d1_evening2 with dissolve
        troy "Shut up."
        menu:
            "Think a bad thought" if True:
                $ dk(1)
                mc "(Moody cunt...)"
            "Ignore him" if True:
                $ dk(-1)
                mc "(Apparently not.)"
    "Ignore him" if True:
        if dtype > 0:
            mc "(Meh...fuck him.)"
        elif True:
            mc "(Looks like he's calmed down a bit.)"

scene d1_evening1 with dissolve
mc "(I still have some time to fuck around before it's bedtime.)"
mc "(What do I want to do?)"
scene d1_evening2b with dissolve
mc "(Maybe play the guitar?)"
if minigames:
    scene d1_evening3 with dissolve
    mc "(Study for a while?)"
scene d1_evening1 with dissolve
mc "(I could call Josy...)"
mc "(...or just walk around and see what's what.)"
$ phone_call_josy = "fr_ep1_call_josy"
if minigames:
    $ phone_call_magnar = "shop_magnar_phone_call"
$ phone_chat_dad = 1
$ chat_dad_state = "h1"
$ phone_chat_dad_new = True
label ep1_freeroam_mc_dorm:
if not persistent.ep1_card5:
    scene d1_evening_bg_card with fade
elif True:
    scene d1_evening_bg with fade
label ep1_freeroam_mc_dorm_nofx:
if not persistent.ep1_card5:
    scene d1_evening_bg_card
elif True:
    scene d1_evening_bg
$ currentFreeRoamLabel = "ep1_freeroam_mc_dorm_nofx"
$ phone_call_enabled = True
if firstTimeFreeRoamMCDormEp1:
    hide screen phone_screen
    $ firstTimeFreeRoamMCDormEp1 = False
    show white_screen with dissolve
    $ current_task = "Call Josy and go to bed."
    $ chat_new_tasks = True
    show text "{font=collegiate.ttf}{size=+40}{color=#fe961b}Task:{/color} Call Josy and go to bed.{/size}{/font}":
        ypos 0.825
        xpos 0.5
    $ ui.imagebutton("invisible_viewport", "invisible_viewport", clicked=ui.returns("OK"), xpos=0, ypos=0)
    $ result = ui.interact()
    if result == "OK":
        hide text "{font=collegiate.ttf}{size=+40}{color=#fe961b}Task:{/color} Call Josy and go to bed.{/size}{/font}"
        hide white_screen with dissolve
    $ updateDikScore()
    show screen scoremsg
    $ renpy.pause(2)
    hide screen scoremsg
    show screen phone_screen
    $ ui.imagebutton("phone_btn_alert", "phone_btn_alert", clicked=ui.returns("OK"), xalign=0.02, yalign=0.02)
    if notifications:
        play sound "sound_effects/message.mp3"
    $ renpy.pause(2)

$ ui.imagebutton("d1_evening_bg_troy_idle", "d1_evening_bg_troy_hover", clicked=ui.returns("fr_ep1_troy"), xpos=0, ypos=0, focus_mask=True)
if not ep1_played_guitar:
    $ ui.imagebutton("d1_evening_bg_guitar_idle", "d1_evening_bg_guitar_hover", clicked=ui.returns("fr_ep1_guitar"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("d1_evening_bg_bed_idle", "d1_evening_bg_bed_hover", clicked=ui.returns("fr_ep1_bed_dorm"), xpos=0, ypos=0, focus_mask=True)
if minigames:
    $ ui.imagebutton("d1_evening_bg_desk_idle", "d1_evening_bg_desk_hover", clicked=ui.returns("fr_ep1_mc_desk"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("arrow_invis", "fr_ep1_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840)
if not persistent.ep1_card5:
    $ ui.imagebutton("fr_ep1_hidden5", "fr_ep1_hidden5_hover", clicked=ui.returns("fr_ep1_hidden5"), xpos=773, ypos=439)

$ result = ui.interact()

if result == "go_down":
    $ renpy.block_rollback()
    jump fr_ep1_mc_dorm_hall_label
elif result == "fr_ep1_mc_desk":
    $ renpy.block_rollback()
    $ phone_call_enabled = False
    scene fr_ep1_desk_study with dissolve
    if ep1_studied_d1:
        mc "(I already studied...)"
        mc "(That's enough for tonight.)"
        jump ep1_freeroam_mc_dorm
    $ ep1_studied_d1 = True
    mc "(I guess I can study some English...)"
    mc "(It would make it easier to pass the next test.)"
    mc "(...or I could prepare for tomorrow's math test.)"
    menu:
        "Study English" if True:
            $ bonusPercentageEnglish += 10
            "+10%% score on your next English test.\nYour total bonus for the next test is [bonusPercentageEnglish]%%."
        "Study Math" if True:
            $ bonusPercentageMath += 10
            "+10%% score on your next Math test.\nYour total bonus for the next test is [bonusPercentageMath]%%."
    mc "(That will do for tonight.)"
    jump ep1_freeroam_mc_dorm
elif result == "fr_ep1_troy":
    $ renpy.block_rollback()
    $ phone_call_enabled = False
    if ep1_troy_talk:
        if dtype > 0:
            mc "Nope, I'm not talking to that dick again."
        elif True:
            mc "No, I gave it a shot. I'm not doing that again."
        jump ep1_freeroam_mc_dorm_nofx
    $ ep1_troy_talk = True
    scene fr_ep1_troy_listen with dissolve
    mc "So...Troy..."
    troy "..."
    scene fr_ep1_troy_listen with dissolve
    mc "You seem dead set on hating me."
    mc "Any way I can change your mind?"
    scene fr_ep1_troy_talk1 with dissolve
    troy "I don't know what you think you're doing right now but stop it."
    troy "I don't want to be your friend."
    scene fr_ep1_troy_listen with dissolve
    mc "We don't have to be friends, but we should at least be able to tolerate each other when we're living together."
    mc "Don't you think?"
    scene fr_ep1_troy_talk1 with dissolve
    troy "If that's so, then shut the fuck up and stop bothering me."
    troy "I can tolerate that."
    $ bios_history_troy += "I tried to talk with Troy again. It went as expected.\n\n"
    $ bios_name_troy = True
    $ chat_new_bios = True
    jump ep1_freeroam_mc_dorm
elif result == "fr_ep1_guitar":
    $ renpy.block_rollback()
    $ phone_call_enabled = False
    $ ep1_played_guitar = True
    scene fr_ep1_guitar with dissolve
    $ loopMusic = False
    stop music fadeout 3
    mc "(What would I do without you? You make this new place feel like home...)"
    mc "(How did that song go? It's been a while...)"
    play music "music/ep1/apra_hyde.mp3"
    scene fr_ep1_guitar1 with dissolve
    $ renpy.pause()
    scene fr_ep1_guitar2 with dissolve
    troy "..."
    scene fr_ep1_guitar1b with dissolve
    $ renpy.pause()
    scene fr_ep1_guitar3 with dissolve
    troy "That sounds pretty sweet..."
    scene fr_ep1_guitar2 with dissolve
    mc "Thanks..."
    scene fr_ep1_guitar3 with dissolve
    troy "You wrote that?"
    scene fr_ep1_guitar2 with dissolve
    mc "No, my dad played this song on the radio when I was twelve."
    mc "I..."
    mc "Forget it; it's stupid."
    scene fr_ep1_guitar4 with dissolve
    troy "It probably is."
    scene fr_ep1_guitar1 with dissolve
    mc "(Couldn't leave me feeling good about myself, huh?)"
    show text "Click to continue" with dissolve:
        xpos 0.5
        ypos 0.9
    $ renpy.pause(2)
    hide text "Click to continue" with dissolve
    $ renpy.pause()
    scene fr_ep1_guitar with dissolve
    stop music
    mc "(Ok, that's enough for now.)"
    $ loopMusic = True
    $ queueChanCallback()
    if not persistent.ep1_card5:
        scene d1_evening_bg_card with dissolve
    elif True:
        scene d1_evening_bg with dissolve
    $ bios_history_troy += "Troy seemed to like it when I played the guitar.\n\n"
    $ bios_name_troy = True
    $ chat_new_bios = True
    jump ep1_freeroam_mc_dorm_nofx
elif result == "fr_ep1_hidden5":
    $ renpy.block_rollback()
    $ phone_call_enabled = False
    $ persistent.ep1_card5 = True
    $ persistent.rew_josy_unlocked += 1
    $ chat_new_rewards = True
    $ calcRenders()
    scene d1_evening_bg with dissolve
    hide screen phone_screen
    show screen srmsg
    $ renpy.pause(4)
    hide screen srmsg
    show screen phone_screen
    jump ep1_freeroam_mc_dorm_nofx
elif result == "fr_ep1_bed_dorm":
    if not ep1_called_josy:
        mc "(I should call Josy before I go to bed...)"
        jump ep1_freeroam_mc_dorm_nofx
    $ phone_call_enabled = False
    menu:
        "End the day" if True:
            $ renpy.block_rollback()
        "Stay up a little bit longer" if True:
            jump ep1_freeroam_mc_dorm_nofx
    scene d1_bedtime with dissolve
    mc "(That's it for today...)"
    $ loopMusic = False
    stop music fadeout 5
    mc "(...it's been interesting.)"
    mc "(Not at all like I would have imagined it.)"
    scene d1_bedtime2 with Fade(1.5, 1, 0.5)
    $ renpy.sound.play("sound_effects/footsteps_indoors.mp3", channel="sfx1", loop=False)
    "*{i}Footsteps{/i}*"
    $ renpy.sound.play("sound_effects/door_close.mp3", channel="sfx2", loop=False)
    "*{i}Door closes{/i}*"
    scene d1_bedtime3 with dissolve
    mc "(Huh?)"
    scene d1_bedtime4 with dissolve
    mc "(Troy? Where's he going?)"
    scene d1_bedtime2 with dissolve
    mc "(Meh. I'm too tired...)"
    mc "(...besides, I really don't care.)"
    $ phone_clear_jump_label = "ep1_college_day2_label"
    jump clear_phone_chat

label fr_ep1_call_josy:
hide screen phone_menu
$ renpy.block_rollback()
$ phone_call_enabled = False
$ phone_call_josy = "NONE"
$ ep1_called_josy = True
$ loopMusic = False
stop music fadeout 3
scene fr_ep1_josy with dissolve
mc "(...)"
mc "(Should I call her?)"
play music "music/ep1/art_nouveau.mp3"
mc "(I...shouldn't.)"
mc "(It's better if I just erase her number...maybe?)"
mc "(One phone call can't hurt...)"
scene fr_ep1_josy1 with dissolve
play sound "sound_effects/cellphone.mp3"
"*{i}Cellphone rings{/i}*"
mc "(No fucking way!)"
scene d1_evening2 with dissolve
troy "Hey, take it outside!"
mc "Yeah, yeah..."
scene fr_ep1_josy3 with dissolve
mc "Josy?"
scene fr_ep1_josy4 with dissolve
js "[name]? Hi!"
scene fr_ep1_josy3 with dissolve
mc "Hey...how are you?"
scene fr_ep1_josy4b with dissolve
js "Hey! That was my line!"
js "I'm great, but enough about me..."
js "How's college?"
scene fr_ep1_josy3 with dissolve
mc "It's...ok."
scene fr_ep1_josy4b with dissolve
js "Just ok? Did you meet a lot of new fun people yet?"
play sound "sound_effects/door_slam.mp3"
scene fr_ep1_josy5 with hpunch
troy "HEY SHITHEAD! GO AWAY! I CAN STILL HEAR YOU!"
scene fr_ep1_josy8 with dissolve
mc "Some interesting ones, indeed."
menu:
    "Why are you calling?" if True:
        mc "So, why did you call?"
        scene fr_ep1_josy9 with dissolve
        js "Oh, well I..."
        scene fr_ep1_josy9b with dissolve
        js "I saw this ad on self-defense on TV and thought about you."
        js "I know...it's stupid..."
        js "But...I kind of miss you..."
    "I was about to call you" if True:
        mc "It's funny; I was actually about to call you."
        scene fr_ep1_josy4b with dissolve
        js "Haha! No way!"
        scene fr_ep1_josy8b with dissolve
        mc "Yeah, I was standing here holding the phone when you called."
        scene fr_ep1_josy11 with dissolve
        js "What a coincidence! So, why were you almost calling me?"
        js "Do you miss me or what?"
        scene fr_ep1_josy12 with dissolve
        menu:
            "I miss you" if True:
                mc "Yeah...I miss you, Josy."
                scene fr_ep1_josy13 with dissolve
                $ RPjosy += 1
                js "Oh!"
                js "..."
                js "I miss you too."
            "Just checking in" if True:
                mc "I just wanted to check how you were doing."
                scene fr_ep1_josy9 with dissolve
                js "Oh, ok."
scene fr_ep1_josy8b with dissolve
mc "Did you hear anything about the waitlist yet?"
scene fr_ep1_josy9 with dissolve
js "No, that's kind of why I called, too."
js "I think I will cut my losses already and just move on."
js "I'm actually thinking of quitting my job and moving to the east coast..."
js "Maybe start working in a mall or do volunteer work, I don't know..."
scene fr_ep1_josy8 with dissolve
menu:
    "What about your boyfriend?" if True:
        mc "What about your boyfriend?"
        scene fr_ep1_josy9 with dissolve
        js "Erm...listen...I..."
    "What about me?" if True:
        mc "That far away?"
        mc "..."
        mc "What about me?"
        scene fr_ep1_josy9 with dissolve
        js "I...erm..."
scene fr_ep1_josy9b with dissolve
js "..."
js "Sorry, this was a stupid idea."
js "I shouldn't have called you."
scene fr_ep1_josy8 with dissolve
mc "Hey, don't hang up..."
mc "Can I come to see you soon?"
scene fr_ep1_josy9 with dissolve
js "Soon? You just left..."
scene fr_ep1_josy8 with dissolve
mc "Yeah, I did. But you saying that you're about to move even further away..."
mc "...it feels weird."
scene fr_ep1_josy9 with dissolve
js "I just...feel like I need to get away for a while."
js "It's been tough lately..."
scene fr_ep1_josy8 with dissolve
mc "How about I come back home this weekend?"
scene fr_ep1_josy20 with dissolve
js "This weekend? It's your first weekend in college!"
js "You should be partying!"
js "Would you give that up for me?"
scene fr_ep1_josy8b with dissolve
if dtype < 1:
    $ RPjosy += 1
    mc "In a heartbeat."
elif True:
    mc "It's no problem."
scene fr_ep1_josy13 with dissolve
js "Ok. See you Saturday...or Sunday?"
mc "I'll let you know."
js "Bye..."
scene fr_ep1_josy23 with dissolve
js "(What am I doing?)"
$ loopMusic = True
$ queueChanCallback()
$ bios_history_josy += "Josy called me today. She said she's going to move away and give up on going to college. I told her that I will come home this weekend to see her again. I must talk her out of it....I can't lose her.\n\n"
$ bios_name_josy = True
$ chat_new_bios = True
scene fr_ep1_mc_dorm_hall_b with fade
show white_screen with dissolve
$ current_task = "Go to bed."
$ chat_new_tasks = True
show text "{font=collegiate.ttf}{size=+40}{color=#fe961b}Task:{/color} Go to bed.{/size}{/font}":
    ypos 0.825
    xpos 0.5
$ ui.imagebutton("invisible_viewport", "invisible_viewport", clicked=ui.returns("OK"), xpos=0, ypos=0)
$ result = ui.interact()
if result == "OK":
    hide text "{font=collegiate.ttf}{size=+40}{color=#fe961b}Task:{/color} Go to bed.{/size}{/font}"
    hide white_screen with dissolve
$ renpy.block_rollback()
jump fr_ep1_mc_dorm_hall_label_nofx

label fr_ep1_mc_dorm_hall_label:
scene fr_ep1_mc_dorm_hall_b with dissolve
label fr_ep1_mc_dorm_hall_label_nofx:
scene fr_ep1_mc_dorm_hall_b
$ currentFreeRoamLabel = "fr_ep1_mc_dorm_hall_label_nofx"
$ renpy.block_rollback()
$ phone_call_enabled = True
$ ui.imagebutton("fr_go_up_small_idle", "fr_go_up_small_hover", clicked=ui.returns("fr_ep1_hallw"), xpos=850, ypos=220)
$ ui.imagebutton("fr_ep1_mc_dorm_hall_b_door_idle", "fr_ep1_mc_dorm_hall_b_door_hover", clicked=ui.returns("fr_ep1_dorm"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_ep1_mc_dorm_hall_b_derek_idle", "fr_ep1_mc_dorm_hall_b_derek_hover", clicked=ui.returns("fr_ep1_derek"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
$ guideSuggestedPage = 37
if result == "fr_ep1_dorm":
    jump ep1_freeroam_mc_dorm
elif result == "fr_ep1_hallw":
    jump fr_ep1_mc_dorm_hall2_label
elif result == "fr_ep1_derek":
    $ renpy.block_rollback()
    $ phone_call_enabled = False
    $ loopMusic = False
    stop music fadeout 3
    play music "music/ep1/energetic.mp3"
    if not ep1_fr_talked_to_derek:
        $ ep1_fr_talked_to_derek = True
        scene fr_ep1_derek_1 with dissolve
        if assman:
            de "Hey hey! Ass man! What's up!?"
        elif True:
            de "Hey dude! What's up!?"
        menu:
            "High five" if True:
                play sound "sound_effects/slap.mp3"
                scene fr_ep1_derek_1c with hpunch
                de "All right!"
                $ RPderek += 1
            "Low five" if True:
                $ dk(1)
                play sound "sound_effects/hit.mp3"
                scene fr_ep1_derek_1b with vpunch
                de "Ooowww!"
                scene fr_ep1_derek_2 with dissolve
                de "Hehe! You got me!"
        scene fr_ep1_derek_3 with dissolve
        de "So, what are you up to?"
        scene fr_ep1_derek_4 with dissolve
        mc "Not much, just walking around trying to figure this place out."
        mc "How about you?"
        scene fr_ep1_derek_5 with dissolve
        de "I'm trying to find out who's really in charge of this place."
        scene fr_ep1_derek_4 with dissolve
        mc "What do you mean?"
        scene fr_ep1_derek_5 with dissolve
        de "Well, rumor has it that there's more to this place than what it appears to be."
        de "I'm trying to find out who's calling the shots and how to get in on the action."
        scene fr_ep1_derek_4 with dissolve
        mc "That doesn't really explain anything..."
        mc "Calling the shots on what? What action?"
        scene fr_ep1_derek_6 with dissolve
        de "Open your eyes, I think you'd see that there's something weird going on if you just look hard enough."
        de "I mean, how can the HOTs afford to pay tuition for the freshies?"
        de "Why do the security guards treat some people differently?"
        scene fr_ep1_derek_7 with dissolve
        menu:
            "Joke around" if True:
                $ RPderek += 1
                if dtype > 0:
                    scene fr_ep1_derek_8 with dissolve
                    mc "Hm..."
                    de "What are you doing?"
                    scene fr_ep1_derek_7 with dissolve
                    mc "I was looking for your tinfoil hat, where did you last see it?"
                    scene fr_ep1_derek_3 with dissolve
                    de "Haha! Fuck off! I'm not bullshitting you!"
                elif True:
                    mc "Maybe because they are wearing clothes while you walk around half-naked."
                    mc "Seriously, do you even have a spare T-shirt? I can give you one of mine."
                    scene fr_ep1_derek_3 with dissolve
                    de "Haha! Fuck off! I'm not bullshitting you!"
            "Ignore him" if True:
                mc "If you say so. Good luck with that!"
                scene fr_ep1_derek_3 with dissolve
                de "Thanks!"
        de "But enough about that..."
        de "How did the English test go?"
        scene fr_ep1_derek_4 with dissolve
        if not minigames:
            mc "I did ok."
        elif failedEnglish == 0 and english_cheat:
            mc "I'm sure I passed it...with some tricks..."
        elif failedEnglish == 0:
            mc "Pretty good. I'm sure I passed it."
        elif True:
            mc "Not so good. I'm pretty sure I failed."
        scene fr_ep1_derek_5b with dissolve
        if english_cheat:
            de "I could spot you cheating from where I was sitting, dude."
            de "You need to get smarter with that."
        elif True:
            de "Tests don't have to be that hard, you know."
        de "If you want, I can give you some pointers to \"pass\" tests easier."
        scene fr_ep1_derek_4 with dissolve
        mc "Why are you saying it like that?"
        scene fr_ep1_derek_3 with dissolve
        de "Like how?"
        scene fr_ep1_derek_4 with dissolve
        mc "Oh, you mean you want to teach me how to cheat."
        scene fr_ep1_derek_5c with dissolve
        de "Cheat? ME!? HAHA! Well, I'd never-"
        scene fr_ep1_derek_10 with dissolve
        de "Look, dude, trust me. I have some pointers for you..."
        de "...not for free, of course; a dude gotta eat."
        scene fr_ep1_derek_4 with dissolve
        if not minigames:
            stop music fadeout 3
            mc "Thanks, but I don't need any help with that."
            scene fr_ep1_derek_10 with dissolve
            de "Ok, that's cool."
            $ loopMusic = True
            $ queueChanCallback()
            $ bios_history_derek += "Derek thinks there's something fishy going on around here and wants to get in on it.\n\nHe offered to sell me tricks that I can use to cheat on tests.\n\n"
            $ bios_name_derek = True
            $ chat_new_bios = True
            jump fr_ep1_mc_dorm_hall_label

        if tutorials:
            show white_screen with dissolve
            show text "{color=#ffffff}Derek sells items that make the mini-games easier to pass through cheating. The items are permanent bonuses. How the cheating is carried out depends on the mini-game.{/color}" zorder 2 with dissolve:
                ypos 0.825
            $ renpy.pause()
            show text "{color=#ffffff}As an example, increasing your cheating level in English will reveal more words when you cheat and in Math you may cheat one extra time per level of the booster.{/color}" zorder 2 with dissolve:
                ypos 0.825
            $ renpy.pause()
            hide text
    elif True:
        if minigames:
            scene fr_ep1_derek_5b with dissolve
            de "Hey! So, what will it be?"
        elif True:
            scene fr_ep1_derek_5b with dissolve
            de "Let me know if you change your mind."
            jump fr_ep1_mc_dorm_hall_label

    scene fr_ep1_derek_4 with dissolve
    $ afterDerekShopLabel = "d1_de_afterloop"
    $ talkDerekShopLabel = "d1_de_talk"
    $ listenDerekShopLabel = "d1_de_listen"
    show screen moneymsg
    show screen derek_shop_screen
    label d1_de_loop:
    $ renpy.pause()
    jump d1_de_loop
    label d1_de_talk:
    scene fr_ep1_derek_cheat with dissolve
    de "Hehe, say no more, so here's what you have to do...{w=3}{nw}"
    jump d1_de_listen
    label d1_de_listen:
    scene fr_ep1_derek_4 with dissolve
    jump d1_de_loop
    label d1_de_afterloop:

    scene fr_ep1_derek_5b with dissolve
    stop music fadeout 3
    de "Just hit me up if you want to buy something."
    $ loopMusic = True
    $ queueChanCallback()
    jump fr_ep1_mc_dorm_hall_label

label fr_ep1_mc_dorm_hall2_label:
$ currentFreeRoamLabel = "fr_ep1_mc_dorm_hall2_label"
$ renpy.block_rollback()
$ phone_call_enabled = True
if not ep1_fr_quinn and not ep1_bought_student_soda:
    scene fr_ep1_mc_dorm_hall2_b with dissolve
    stu "Come on! You stupid machine!"
    $ ui.imagebutton("fr_ep1_mc_dorm_hall2_b_idle", "fr_ep1_mc_dorm_hall2_b_hover", clicked=ui.returns("fr_ep1_student"), xpos=0, ypos=0, focus_mask=True)
elif True:
    scene fr_ep1_mc_dorm_hall2_b2 with dissolve
$ ui.imagebutton("arrow_invis", "fr_ep1_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840)
$ ui.imagebutton("fr_go_up_small_idle", "fr_go_up_small_hover", clicked=ui.returns("BATHROOM"), xpos=850, ypos=150)

$ result = ui.interact()

if result == "go_down":
    jump fr_ep1_mc_dorm_hall_label
elif result == "fr_ep1_student":
    $ phone_call_enabled = False
    scene fr_ep1_student with dissolve
    mc "I hate when that happens."
    scene fr_ep1_student1 with dissolve
    stu "When what happens?"
    scene fr_ep1_student with dissolve
    mc "When it steals your money."
    scene fr_ep1_student1 with dissolve
    stu "Yeah, that's not what this is."
    scene fr_ep1_student with dissolve
    show screen moneymsg
    menu:
        "Buy him a soda {color=#36ca2b}${/color}" if money > 0:
            $ ep1_bought_student_soda = True
            $ dk(-1)
            $ mny(-1)
            mc "I'll buy a soda for you."
            hide screen moneymsg
            scene fr_ep1_student4 with dissolve
            mc "Here you go."
            scene fr_ep1_student5 with dissolve
            stu "Really? Thanks man!"
            stu "Now I only need some chips and I'm in business."
            jump fr_ep1_mc_dorm_hall2_label
        "Leave" if True:
            hide screen moneymsg
            if dtype > 0:
                mc "Good luck with the petty theft, then."
            elif True:
                mc "Best of luck to whatever it is you're doing, then."
            scene fr_ep1_student1 with dissolve
            stu "Thanks!"
            jump fr_ep1_mc_dorm_hall2_label
elif result == "BATHROOM":
    if not ep1_fr_quinn:
        $ phone_call_enabled = False
        $ renpy.block_rollback()
        $ ep1_fr_quinn = True
        scene fr_ep1_dorm_quinn with dissolve
        qu "Camila and Maya, I think."
        scene fr_ep1_dorm_quinnb with dissolve
        ri "If you say so, Quinn."
        scene fr_ep1_dorm_quinn1 with dissolve
        qu "..."
        scene fr_ep1_dorm_quinn2 with dissolve
        ri "Yeah, I know."
        ri "But you have to admit it was easier last year."
        scene fr_ep1_dorm_quinn3 with dissolve
        qu "That was because of you, Riona."
        scene fr_ep1_dorm_quinn4 with dissolve
        $ renpy.pause()
        scene fr_ep1_dorm_quinn4b with dissolve
        ri "Fuck, I'm bored."
        ri "Wanna get your groove on?"
        scene fr_ep1_dorm_quinn5 with dissolve
        qu "Shh. These hallways have ears."
        qu "Follow me."
        scene fr_ep1_dorm_quinn6 with dissolve
        $ renpy.pause()
        $ bios_quinn = True
        $ bios_riona = True
        $ bios_history_quinn = "What did Quinn and Riona do in that bathroom?\n\n"
        $ bios_history_riona = "What did Quinn and Riona do in that bathroom?\n\n"
        $ bios_name_quinn = True
        $ bios_name_riona = True
        $ chat_new_bios = True
    jump fr_ep1_bathroom_label

label fr_ep1_bathroom_label:
$ currentFreeRoamLabel = "fr_ep1_bathroom_label"
$ phone_call_enabled = True
$ renpy.block_rollback()
scene fr_ep1_mc_dorm_bathroom with dissolve
if firstTimeBathroom:
    uk "*{i}Whistles{/i}*"
    mc "(Someone's in here...)"
    $ firstTimeBathroom = False
$ ui.imagebutton("fr_ep1_mc_dorm_bathroom_idle", "fr_ep1_mc_dorm_bathroom_hover", clicked=ui.returns("STALL"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("arrow_invis", "fr_ep1_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840)
$ result = ui.interact()
if result == "go_down":
    jump fr_ep1_mc_dorm_hall2_label
elif result == "STALL":
    jump fr_ep1_dorm_stall_label

label fr_ep1_dorm_stall_label:
$ renpy.block_rollback()
if not persistent.ep1_card6:
    scene fr_ep1_mc_dorm_stall_card with dissolve
elif True:
    scene fr_ep1_mc_dorm_stall with dissolve
label fr_ep1_dorm_stall_label_nofx:
$ currentFreeRoamLabel = "fr_ep1_dorm_stall_label"
$ phone_call_enabled = True
$ ui.imagebutton("arrow_invis", "fr_ep1_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840)
if not persistent.ep1_card6:
    $ ui.imagebutton("fr_ep1_hidden6", "fr_ep1_hidden6_hover", clicked=ui.returns("fr_ep1_hidden6"), xpos=856, ypos=662)
if not ep1_saw_glory_hole:
    $ ui.imagebutton("fr_ep1_mc_dorm_stall_idle", "fr_ep1_mc_dorm_stall_hover", clicked=ui.returns("HOLE"), xpos=0, ypos=0, focus_mask=True)

$ result = ui.interact()
if result == "fr_ep1_hidden6":
    $ renpy.block_rollback()
    $ phone_call_enabled = False
    $ persistent.ep1_card6 = True
    $ persistent.rew_riona_unlocked += 1
    $ chat_new_rewards = True
    $ calcRenders()
    scene fr_ep1_mc_dorm_stall with dissolve
    hide screen phone_screen
    show screen srmsg
    $ renpy.pause(4)
    hide screen srmsg
    show screen phone_screen
    jump fr_ep1_dorm_stall_label_nofx
elif result == "go_down":
    jump fr_ep1_bathroom_label
elif result == "HOLE":
    $ phone_call_enabled = False
    $ ep1_saw_glory_hole = True
    scene fr_ep1_mc_dorm_stall1 with dissolve
    mc "(What the fuck is this!? A glory hole?)"
    mc "(Someone's on the other side...)"
    mc "(Yeah, no way I'm eating anything that comes through that hole.)"
    mc "(There's a faded number written on the wall. I think it says {color=#00ff00}3{/color}...but it could be an {color=#00ff00}8{/color}, too.)"
    jump fr_ep1_dorm_stall_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
