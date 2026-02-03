label ep1_freeroam_movie_maya_label:
$ phone_chat_josy = 2
$ chat_josy_state = "h1"
$ newMessageIntJosy = len(chat_josy_history)
$ phone_chat_josy_new = True
$ phone_chat_derek = 1
$ chat_derek_state = "h1"
$ newMessageIntDerek = len(chat_derek_history)
$ phone_chat_derek_new = True

$ freeRoamID = 4
$ firstTimeFreeRoam = True
$ found_money = False
$ studied = False
$ game_money_available = True
if persistent.ep1_card13:
    $ brawler_render_available = False
elif True:
    $ brawler_render_available = True
$ brawler_money_available = True
$ brawler_skillpoint_available = True
$ loopMusic = True
$ queueChanCallback()

if minigames:
    $ phone_call_magnar = "shop_magnar_phone_call"
    $ phone_call_derek = "shop_derek_phone_call"
if number_quinn:
    $ phone_call_quinn = "shop_quinn_phone_call"
$ phone_call_enabled = True

label ep1_maya3_freeroam_label:
scene ep1_maya3_freeroam_bg with fade
label ep1_maya3_freeroam_label_nofx:
scene ep1_maya3_freeroam_bg
$ phone_call_enabled = True
$ currentFreeRoamLabel = "ep1_maya3_freeroam_label_nofx"
if firstTimeFreeRoam:
    hide screen phone_screen
    $ firstTimeFreeRoam = False
    show white_screen with dissolve
    $ current_task = "Talk to Maya"
    $ chat_new_tasks = True
    show text "{font=collegiate.ttf}{size=+40}{color=#fe961b}Task:{/color} Talk to Maya.{/size}{/font}":
        ypos 0.825
        xpos 0.5
    $ renpy.pause()
    hide text
    hide white_screen
    show screen phone_screen
    $ ui.imagebutton("phone_btn_alert", "phone_btn_alert", clicked=ui.returns("OK"), xalign=0.02, yalign=0.02)
    if notifications:
        play sound "sound_effects/message.mp3"
    $ renpy.pause(2)

$ ui.imagebutton("ep1_maya3_freeroam_bg_maya_idle", "ep1_maya3_freeroam_bg_maya_hover", clicked=ui.returns("maya_talk"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_ep1_dad", "fr_ep1_go_right", clicked=ui.returns("go_right"), xpos=1690, ypos=250)
$ ui.imagebutton("fr_ep1_dad", "fr_ep1_go_left", clicked=ui.returns("go_left"), xpos=20, ypos=250)
$ ui.imagebutton("ep1_maya3_freeroam_bg_desk_idle", "ep1_maya3_freeroam_bg_desk_hover", clicked=ui.returns("go_up"), xpos=0, ypos=0, focus_mask=True)
$ result = ui.interact()

if result == "maya_talk":
    menu:
        "End free roam" if True:
            stop music fadeout 3
            $ renpy.block_rollback()
            $ phone_call_enabled = False
            $ chat_new_tasks = False
            $ loopMusic = False
            $ renpy.pause(3)
            play music "music/ep1/trow.mp3"
            $ phone_clear_jump_label = "ep1_maya_movie_label"
            jump clear_phone_chat
        "Not yet" if True:
            jump ep1_maya3_freeroam_label_nofx
elif result == "go_right":
    jump ep1_maya3_freeroam_right_label
elif result == "go_left":
    jump ep1_maya3_freeroam_left_label
elif result == "go_up":
    jump ep1_maya3_freeroam_up_label

label ep1_maya3_freeroam_right_label:
$ currentFreeRoamLabel = "ep1_maya3_freeroam_right_label"
$ phone_call_enabled = True
scene ep1_maya3_freeroam_bg2b
$ ui.imagebutton("ep1_hallway2_shower", "fr_ep1_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=850)
$ ui.imagebutton("ep1_maya3_freeroam_bg2b_notes_idle", "ep1_maya3_freeroam_bg2b_notes_hover", clicked=ui.returns("examine"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep1_maya3_freeroam_bg2b_door_idle", "ep1_maya3_freeroam_bg2b_door_hover", clicked=ui.returns("closet"), xpos=0, ypos=0, focus_mask=True)
$ result = ui.interact()
if result == "go_down":
    scene ep1_maya3_freeroam_bg
    jump ep1_maya3_freeroam_label_nofx
elif result == "examine":
    jump ep1_maya3_freeroam_notes_label
elif result == "closet":
    if persistent.ep1_card17:
        scene ep1_maya3_freeroam_bg2 with dissolve
    elif True:
        scene ep1_maya3_freeroam_bg2_card with dissolve
    my "Erm...that's my closet, [name]."
    my "I know I told you to make yourself at home, but please let me have some privacy."
    mc "I'm sorry..."
    scene ep1_maya3_freeroam_bg2b with dissolve
    jump ep1_maya3_freeroam_right_label

label ep1_maya3_freeroam_notes_label:
$ currentFreeRoamLabel = "ep1_maya3_freeroam_notes_label"
$ phone_call_enabled = True
if found_money:
    scene ep1_maya3_freeroam_bg7
elif True:
    scene ep1_maya3_freeroam_bg7_money
$ ui.imagebutton("ep1_hallway2_shower", "fr_ep1_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=850)
if not found_money:
    $ ui.imagebutton("fr_money_maya_ep1", "fr_money_maya_ep1_hover", clicked=ui.returns("money"), xpos=1062, ypos=0)
$ result = ui.interact()
if result == "go_down":
    jump ep1_maya3_freeroam_right_label
elif result == "money":
    $ mny(dollar)
    $ found_money = True
    show screen moneymsg
    scene ep1_maya3_freeroam_bg7 with dissolve
    $ renpy.pause(3)
    hide screen moneymsg
    jump ep1_maya3_freeroam_notes_label

label ep1_maya3_freeroam_left_label:
scene ep1_maya3_freeroam_bg3
label ep1_maya3_freeroam_left_label_nofx:
$ currentFreeRoamLabel = "ep1_maya3_freeroam_left_label"
$ phone_call_enabled = True
$ ui.imagebutton("fr_ep1_dad", "fr_ep1_go_right", clicked=ui.returns("go_right"), xpos=1690, ypos=250)
$ ui.imagebutton("ep1_maya3_freeroam_bg3_idle", "ep1_maya3_freeroam_bg3_hover", clicked=ui.returns("examine"), xpos=0, ypos=0, focus_mask=True)
$ result = ui.interact()
if result == "go_right":
    scene ep1_maya3_freeroam_bg
    jump ep1_maya3_freeroam_label_nofx
elif result == "examine":
    jump ep1_maya3_freeroam_dresser_label
label ep1_maya3_freeroam_up_label:
$ currentFreeRoamLabel = "ep1_maya3_freeroam_up_label"
$ phone_call_enabled = True
scene ep1_maya3_freeroam_bg5
if minigames:
    $ ui.imagebutton("ep1_maya3_freeroam_bg5_idle", "ep1_maya3_freeroam_bg5_hover", clicked=ui.returns("study"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep1_hallway2_shower", "fr_ep1_go_up", clicked=ui.returns("go_up"), xpos=0, ypos=20)
$ ui.imagebutton("ep1_hallway2_shower", "fr_ep1_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=850)
$ result = ui.interact()
if result == "go_down":
    scene ep1_maya3_freeroam_bg
    jump ep1_maya3_freeroam_label_nofx
elif result == "go_up":
    jump ep1_maya3_freeroam_up2_label
elif result == "study":
    $ renpy.block_rollback()
    if studied:
        mc "(I already studied...)"
        mc "(That's enough for tonight.)"
        jump ep1_maya3_freeroam_up_label
    $ studied = True
    mc "Maya, can I borrow your desk to study for a bit?"
    my "Yeah, go ahead."
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
    mc "(That will do for tonight.)"
    jump ep1_maya3_freeroam_up_label

label ep1_maya3_freeroam_up2_label:
$ currentFreeRoamLabel = "ep1_maya3_freeroam_up2_label"
$ phone_call_enabled = True
if not persistent.ep1_card11:
    scene ep1_maya3_freeroam_bg6_card
elif True:
    scene ep1_maya3_freeroam_bg6
$ ui.imagebutton("ep1_hallway2_shower", "fr_ep1_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=850)
if not persistent.ep1_card11:
    $ ui.imagebutton("fr_ep1_hidden_11", "fr_ep1_hidden_11_hover", clicked=ui.returns("hidden_card"), xpos=1364, ypos=72)
$ result = ui.interact()
if result == "go_down":
    jump ep1_maya3_freeroam_up_label
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep1_card11 = True
    $ persistent.rew_josy_unlocked += 1
    $ chat_new_rewards = True
    $ calcRenders()
    scene ep1_maya3_freeroam_bg6 with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep1_maya3_freeroam_up2_label

label ep1_maya3_freeroam_dresser_label:
$ currentFreeRoamLabel = "ep1_maya3_freeroam_dresser_label"
$ phone_call_enabled = True
if not persistent.ep1_card12:
    scene ep1_maya3_freeroam_bg4_card
elif True:
    scene ep1_maya3_freeroam_bg4
$ ui.imagebutton("ep1_hallway2_shower", "fr_ep1_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=900)
if not persistent.ep1_card12:
    $ ui.imagebutton("fr_ep1_card12", "fr_ep1_card12_hover", clicked=ui.returns("hidden_card"), xpos=936, ypos=760)
$ result = ui.interact()
if result == "go_down":
    jump ep1_maya3_freeroam_left_label
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep1_card12 = True
    $ persistent.rew_riona_unlocked += 1
    $ chat_new_rewards = True
    $ calcRenders()
    scene ep1_maya3_freeroam_bg4 with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep1_maya3_freeroam_dresser_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
