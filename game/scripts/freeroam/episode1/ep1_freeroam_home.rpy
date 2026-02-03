label ep1_freeroam_home_label:
if persistent.ep1_card15:
    $ brawler_render_available = False
$ phone_chat_josy = 1
$ chat_josy_state = "1"
$ phone_chat_josy_new = True
$ loopMusic = True
$ queueChanCallback()
$ updateDikScore()
label ep1_freeroam_kitchen_label:
if not persistent.ep1_card1:
    scene d0_kitchen_bg_card with fade
elif True:
    scene d0_kitchen_bg with fade
label ep1_freeroam_kitchen_label_nofx:
if not persistent.ep1_card1:
    scene d0_kitchen_bg_card
elif True:
    scene d0_kitchen_bg
$ currentFreeRoamLabel = "ep1_freeroam_kitchen_label_nofx"
if firstTimeFreeRoam:
    $ firstTimeFreeRoam = False
    $ bios_name_josy = True
    $ bios_name_dad = True
    $ bios_name_mc = True
    $ bios_name_steve = True
    if tutorials:
        show white_screen with dissolve
        show text "{color=#ffffff}During the game, there will be events where you can explore certain areas. Think of it as free roam.{/color}" zorder 2 with dissolve:
            ypos 0.825
        $ renpy.pause()
        hide text
        show text "{color=#ffffff}These events always state tasks you must complete to advance the story. During free roam events you can find special renders and money if you look hard enough.{/color}" zorder 2 with dissolve:
            ypos 0.825
        $ renpy.pause()
        hide text
        show text "{color=#ffffff}View your unlocked special renders in the Rewards app on your phone.{/color}" zorder 2 with dissolve:
            ypos 0.825
        $ renpy.pause()
        hide text
        show screen scoremsg
        show text "{color=#ffffff}Your {size=+3}{size=+3}{color=#ffb052}{font=collegiate.ttf}DIK{/font}{/color}{/size}{/size} score has changed as a result of your choices.\nCheck the Stats app on your phone to view your score.{/color}" zorder 2 with dissolve:
            ypos 0.825
        $ renpy.pause()
        hide screen scoremsg
        hide text
        show text "{color=#ffffff}Your phone is accessible by clicking the phone button in the upper left corner of the screen.{/color}" zorder 2 with dissolve:
            ypos 0.825
        $ ui.imagebutton("phone_btn_alert", "phone_btn_alert", clicked=ui.returns("OK"), xalign=0.02, yalign=0.02)
        if notifications:
            play sound "sound_effects/message.mp3"
        $ renpy.pause()
        hide text
        show text "{color=#ffffff}You can also access your phone and close any menus in it by middle-clicking your mouse.{/color}" zorder 2 with dissolve:
            ypos 0.825
        $ renpy.pause()
        hide text
        show text "{color=#ffffff}Your phone is continuously updated throughout the game. If you forget some important choice you made, you can read about it in the Bios app.{/color}" zorder 2 with dissolve:
            ypos 0.825
        $ renpy.pause()
        hide text
        show text "{color=#ffffff}During free roam you can change music using your phone or by clicking\nthe skip song button in the upper right corner of the screen.{/color}" zorder 2 with dissolve:
            ypos 0.825
        $ ui.imagebutton("skip_song_button_hover", "skip_song_button_hover", clicked=ui.returns("OK"), xalign=0.99, yalign=0.01)
        $ renpy.pause()
        hide text
        hide white_screen
    elif True:
        show screen scoremsg
        $ renpy.pause(2)
        hide screen scoremsg
    mc "(Ugh... It was a good sparring session, but I fucking reek...)"
    mc "(I can't meet Josy smelling like this.)"
    show white_screen with dissolve
    $ current_task = "Prepare for your date."
    $ chat_new_tasks = True
    show text "{font=collegiate.ttf}{size=+40}{color=#fe961b}Task:{/color} Prepare for your date.{/size}{/font}":
        ypos 0.825
        xpos 0.5
    $ ui.imagebutton("invisible_viewport", "invisible_viewport", clicked=ui.returns("OK"), xpos=0, ypos=0)
    $ result = ui.interact()
    if result == "OK":
        hide text "{font=collegiate.ttf}{size=+40}{color=#fe961b}Task:{/color} Prepare for your date.{/size}{/font}"
        hide white_screen with dissolve
    $ phone_call_enabled = True
    show screen phone_screen
$ ui.imagebutton("arrow_invis", "fr_ep1_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840)
if not ep1_dad_college and not ep1_dad_women:
    $ ui.imagebutton("d0_kitchen_bg_dad_idle", "d0_kitchen_bg_dad_hover", clicked=ui.returns("fr_ep1_dad"), xpos=0, ypos=0, focus_mask=True)
if not persistent.ep1_card1:
    $ ui.imagebutton("fr_ep1_hidden1", "fr_ep1_hidden1_hover", clicked=ui.returns("fr_ep1_hidden1"), xpos=1300, ypos=614)
$ ui.imagebutton("d0_kitchen_bg_stove_idle", "d0_kitchen_bg_stove_hover", clicked=ui.returns("fr_ep1_stove"), xpos=0, ypos=0, focus_mask=True)
$ result = ui.interact()

if result == "go_down":
    jump fr_ep1_hall_label
elif result == "fr_ep1_stove":
    $ phone_call_enabled = False
    mc "(Haha. I still laugh when I see that industrial stove...)"
    mc "(I can't believe dad actually brought that home after renovating that restaurant...)"
    mc "(The number {color=#00ff00}1{/color} is carved on the side of the stove.)"
    $ phone_call_enabled = True
    jump ep1_freeroam_kitchen_label_nofx
elif result == "fr_ep1_dad":
    $ phone_call_enabled = False
    stop music fadeout 3
    $ loopMusic = False
    scene fr_ep1_dad_talk with dissolve
    dad "Getting ready for tonight?"
    play music "music/ep1/someways.mp3"
    scene fr_ep1_dad_listen with dissolve
    mc "Yeah...tonight's the night."
    scene fr_ep1_dad_talk with dissolve
    dad "You can do it, son."
    label ep1_fr_dad_label:
    scene fr_ep1_dad_listen with dissolve
    menu:
        "College" if not ep1_dad_college:
            $ ep1_dad_college = True
            mc "Are you going to be ok on your own when I move out and start college?"
            scene fr_ep1_dad_talk2 with dissolve
            dad "Of course! I'm going to miss having you around, but I knew that this day would come sooner or later."
            scene fr_ep1_dad_listen with dissolve
            mc "I feel weird leaving you here alone."
            scene fr_ep1_dad_talk with dissolve
            dad "Don't say that. I have the guys at work; I'm not really alone."
            scene fr_ep1_dad_talk2 with dissolve
            dad "Although, I could come to stay with you in your dorm if that would make you feel better?"
            scene fr_ep1_dad_listen with dissolve
            mc "Haha! I'll pass on that offer, thanks."
            jump ep1_fr_dad_label
        "Women" if not ep1_dad_women:
            $ ep1_dad_women = True
            mc "Dad...were you popular with women growing up?"
            scene fr_ep1_dad_talk2 with dissolve
            dad "Hehe, I had my fair share before I met your mom. I can't deny that."
            scene fr_ep1_dad_talkc with dissolve
            dad "Some serious relationships and some...not so serious ones."
            dad "If I could go back and give myself advice, though..."
            dad "It would be to never second guess my gut feeling."
            scene fr_ep1_dad_talk3 with dissolve
            dad "...that would have saved me some...grief."
            scene fr_ep1_dad_talk with dissolve
            dad "Oh! And I would also have told myself to always use a condom."
            scene fr_ep1_dad_listen with dissolve
            mc "...thanks, dad."
            scene fr_ep1_dad_talk4 with dissolve
            dad "No, I didn't mean..."
            dad "Don't mind me, son, I was just rambling."
            dad "I must be tired tonight."
            jump ep1_fr_dad_label
        "Leave" if True:
            mc "I got to go, dad."
            scene fr_ep1_dad_talk with dissolve
            dad "Go ahead, son. You're going to be late for your date."
    $ phone_call_enabled = True
    $ loopMusic = True
    $ queueChanCallback()
    jump ep1_freeroam_kitchen_label
elif result == "fr_ep1_hidden1":
    $ renpy.block_rollback()
    $ persistent.ep1_card1 = True
    $ persistent.rew_josy_unlocked += 1
    $ chat_new_rewards = True
    $ calcRenders()
    scene d0_kitchen_bg with dissolve
    hide screen phone_screen
    show screen srmsg
    $ renpy.pause(4)
    hide screen srmsg
    show screen phone_screen
    jump ep1_freeroam_kitchen_label_nofx

label fr_ep1_hall_label:
scene d0_hall_bg with dissolve
label fr_ep1_hall_label_nofx:
scene d0_hall_bg
$ currentFreeRoamLabel = "fr_ep1_hall_label_nofx"
$ renpy.block_rollback()
$ ui.imagebutton("arrow_invis", "fr_ep1_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840)
$ ui.imagebutton("d0_hall_bg_right_idle", "d0_hall_bg_right_hover", clicked=ui.returns("fr_ep1_room"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("d0_hall_bg_left_idle", "d0_hall_bg_left_hover", clicked=ui.returns("fr_ep1_bathroom"), xpos=0, ypos=0, focus_mask=True)
$ result = ui.interact()

if result == "go_down":
    jump ep1_freeroam_kitchen_label
elif result == "fr_ep1_room":
    jump ep1_freeroam_room_label
elif result == "fr_ep1_bathroom":
    jump ep1_freeroam_bathroom_label

label ep1_freeroam_bathroom_label:
$ renpy.block_rollback()
if not persistent.ep1_card2:
    scene d0_bathroom_bg_card with fade
elif True:
    scene d0_bathroom_bg with fade
if firstTimeShower:
    $ phone_call_enabled = False
    $ firstTimeShower = False
    mc "(Dad did a really good job renovating the bathroom.)"
    mc "(Sure, it's mostly bits and pieces he got a hold on for free from work, but man...)"
    mc "(He's so talented...)"
    mc "(...if he only could afford to fix the rest of the house.)"
    mc "(That would make him so happy...)"
    $ phone_call_enabled = True
label ep1_freeroam_bathroom_label_nofx:
if not persistent.ep1_card2:
    scene d0_bathroom_bg_card
elif True:
    scene d0_bathroom_bg
$ currentFreeRoamLabel = "ep1_freeroam_bathroom_label_nofx"
$ renpy.block_rollback()
$ ui.imagebutton("arrow_invis", "fr_ep1_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840)
$ ui.imagebutton("d0_bathroom_bg_toilet_idle", "d0_bathroom_bg_toilet_hover", clicked=ui.returns("fr_ep1_toilet"), xpos=0, ypos=0, focus_mask=True)
if not ep1_showered:
    $ ui.imagebutton("d0_bathroom_bg_shower_idle", "d0_bathroom_bg_shower_hover", clicked=ui.returns("fr_ep1_shower"), xpos=0, ypos=0, focus_mask=True)
if not persistent.ep1_card2:
    $ ui.imagebutton("fr_ep1_hidden2", "fr_ep1_hidden2_hover", clicked=ui.returns("fr_ep1_hidden2"), xpos=695, ypos=466)

$ result = ui.interact()
if result == "go_down":
    $ renpy.block_rollback()
    jump fr_ep1_hall_label
elif result == "fr_ep1_toilet":
    $ phone_call_enabled = False
    mc "(That ugly toilet, though...)"
    $ phone_call_enabled = True
    jump ep1_freeroam_bathroom_label_nofx
elif result == "fr_ep1_shower":
    $ phone_call_enabled = False
    $ renpy.block_rollback()
    $ loopMusic = False
    stop music fadeout 3
    $ ep1_showered = True
    mc "(I have plenty of time to grab a long shower.)"
    $ renpy.music.set_volume(1, delay=0, channel="sfx1")
    $ renpy.sound.play("sound_effects/shower.mp3", channel="sfx1", loop=True)
    play music "music/ep1/slow_day_blues.mp3"
    scene fr_ep1_shower with wipeleft
    mc "(I can't wait to meet Josy tonight...)"
    mc "(I wonder what she'll say...)"
    scene fr_ep1_shower_thought
    js "You're in love with me? Are you high?"
    scene fr_ep1_shower_thought2
    js "HAHAHA! That's just sad!"
    scene fr_ep1_shower_thought3
    js "Erm...ok...I got to go..."
    scene fr_ep1_shower_thought4
    js "You're in love with me?"
    scene fr_ep1_shower_thought4b with dissolve
    js "Well, why don't you fuck me right here, then?"
    js "Yes, that's right... I want your dick inside me, [mc_josy]."
    scene fr_ep1_shower_thought4d with dissolve
    js "I've been a naughty girl..."
    scene fr_ep1_shower_thought5
    stop music
    $ renpy.music.stop(channel="sfx1", fadeout=0)
    $ renpy.sound.play("sound_effects/shower_low.mp3", channel="sfx1", loop=True)
    play sound "sound_effects/door_knock.mp3"
    dad "*{i}Door knocking{/i}* Son, are you almost done?"
    scene fr_ep1_shower_thought6 with dissolve
    mc "Take my cock, Josy!"
    scene fr_ep1_shower_thought5b with dissolve
    dad "What's that, son?"
    scene fr_ep1_shower_thought6 with dissolve
    mc "Yes, I'm coming- Shit! I'm almost done, dad!"
    scene fr_ep1_shower_thought5c with dissolve
    dad "Save some hot water for me, will you?"
    scene fr_ep1_shower_thought7 with dissolve
    $ renpy.music.stop(channel="sfx1", fadeout=5)
    mc "(There goes that moment...)"
    mc "(Time to get changed, I guess.)"
    $ loopMusic = True
    $ queueChanCallback()
    $ phone_call_enabled = True
    jump ep1_freeroam_bathroom_label
elif result == "fr_ep1_hidden2":
    $ renpy.block_rollback()
    $ persistent.ep1_card2 = True
    $ persistent.rew_riona_unlocked += 1
    $ chat_new_rewards = True
    $ calcRenders()
    scene d0_bathroom_bg with dissolve
    hide screen phone_screen
    show screen srmsg
    $ renpy.pause(4)
    hide screen srmsg
    show screen phone_screen
    jump ep1_freeroam_bathroom_label_nofx

label ep1_freeroam_room_label:
$ renpy.block_rollback()
if not persistent.ep1_card3:
    scene ep1_fr_room_bg_card with fade
elif True:
    scene ep1_fr_room_bg with fade
label ep1_freeroam_room_label_nofx:
$ currentFreeRoamLabel = "ep1_freeroam_room_label_nofx"
if not persistent.ep1_card3:
    scene ep1_fr_room_bg_card
elif True:
    scene ep1_fr_room_bg
$ renpy.block_rollback()
$ ui.imagebutton("ep1_fr_room_bg_door_idle", "ep1_fr_room_bg_door_hover", clicked=ui.returns("fr_ep1_hall3"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep1_fr_room_bg_desk_idle", "ep1_fr_room_bg_desk_hover", clicked=ui.returns("fr_ep1_closet"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep1_fr_room_bg_guitar_idle", "ep1_fr_room_bg_guitar_hover", clicked=ui.returns("fr_ep1_guitar"), xpos=0, ypos=0, focus_mask=True)
if not persistent.ep1_card3:
    $ ui.imagebutton("fr_ep1_hidden3", "fr_ep1_hidden3_hover", clicked=ui.returns("fr_ep1_hidden3"), xpos=1610, ypos=593)
$ result = ui.interact()

if result == "fr_ep1_hall3":
    $ renpy.block_rollback()
    jump fr_ep1_hall_label
elif result == "fr_ep1_guitar":
    $ phone_call_enabled = False
    $ renpy.block_rollback()
    mc "(My dad got me that guitar for my 12th birthday. I've loved it ever since.)"
    mc "(I have no idea where he got the money for it...)"
    scene ep1_fr_guitar_play with dissolve
    $ loopMusic = False
    stop music fadeout 3
    mc "(It must have cost him a fortune.)"
    mc "(It's the most valuable thing I own, for more reasons than one.)"
    play music "music/ep1/trow.mp3"
    scene ep1_fr_guitar_play_dyn with dissolve
    $ renpy.pause(8)
    show text "Click to continue" with dissolve:
        xpos 0.5
        ypos 0.9
    $ renpy.pause(2)
    hide text "Click to continue" with dissolve
    $ renpy.pause()
    stop music
    scene ep1_fr_guitar_play with dissolve
    mc "(I love music so much...)"
    if not persistent.ep1_card3:
        scene ep1_fr_room_bg_card with dissolve
    elif True:
        scene ep1_fr_room_bg with dissolve
    $ loopMusic = True
    $ queueChanCallback()
    $ phone_call_enabled = True
    jump ep1_freeroam_room_label_nofx
elif result == "fr_ep1_closet":
    $ phone_call_enabled = False
    $ renpy.block_rollback()
    if not ep1_showered:
        mc "(I fucking stink, I can't go on a date smelling like this...)"
        mc "(I need to grab a shower first.)"
        $ phone_call_enabled = True
        jump ep1_freeroam_room_label_nofx
    menu:
        "Get dressed" if True:
            scene fr_ep1_clothes with dissolve
        "I'm not ready yet" if True:
            $ phone_call_enabled = True
            jump ep1_freeroam_room_label_nofx
    stop music fadeout 3
    $ loopMusic = False
    mc "(Perfect...)"
    mc "(Time to go and pick up Josy.)"
    $ phone_clear_jump_label = "ep1_date_label"
    jump clear_phone_chat
elif result == "fr_ep1_hidden3":
    $ renpy.block_rollback()
    $ persistent.ep1_card3 = True
    $ persistent.rew_josy_unlocked += 1
    $ chat_new_rewards = True
    $ calcRenders()
    scene ep1_fr_room_bg with dissolve
    hide screen phone_screen
    show screen srmsg
    $ renpy.pause(4)
    hide screen srmsg
    show screen phone_screen
    jump ep1_freeroam_room_label_nofx
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
