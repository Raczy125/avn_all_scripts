label ep1_freeroam_maya_dorm_label:
$ phone_chat_josy = 3
$ chat_josy_state = "1"
$ phone_chat_josy_new = True
$ phone_chat_derek = 2
$ chat_derek_state = "h1"
$ newMessageIntDerek = len(chat_derek_history)
$ phone_chat_derek_new = True
$ phone_chat_sage = 1
$ chat_sage_state = "h1"
$ phone_chat_sage_new = True

$ freeRoamID = 5
$ firstTimeFreeRoam = True
$ game_money_available = True
if persistent.ep1_card18:
    $ brawler_render_available = False
elif True:
    $ brawler_render_available = True
$ brawler_money_available = True
$ brawler_skillpoint_available = True
$ studied = False
$ loopMusic = True
$ queueChanCallback()
$ found_money = False
if minigames:
    $ phone_call_magnar = "shop_magnar_phone_call"
    if number_derek:
        $ phone_call_derek = "shop_derek_phone_call"
if number_quinn:
    $ phone_call_quinn = "shop_quinn_phone_call"
$ phone_call_enabled = True
label ep1_maya2_freeroam_label:
scene ep1_nomaya_freeroam_bg with fade
label ep1_maya2_freeroam_label_nofx:
scene ep1_nomaya_freeroam_bg
$ currentFreeRoamLabel = "ep1_maya2_freeroam_label_nofx"
$ phone_call_enabled = True
if firstTimeFreeRoam:
    mc "(I've got the place all to myself...)"
    hide screen phone_screen
    $ firstTimeFreeRoam = False
    show white_screen with dissolve
    $ current_task = "Go to bed or explore (optional)."
    $ chat_new_tasks = True
    show text "{font=collegiate.ttf}{size=+40}{color=#fe961b}Task:{/color} Go to bed or explore.{/size}{/font}":
        ypos 0.825
        xpos 0.5
    $ renpy.pause()
    hide text
    hide white_screen
    $ updateDikScore()
    show screen scoremsg
    $ renpy.pause(2)
    hide screen scoremsg
    show screen phone_screen
    $ ui.imagebutton("phone_btn_alert", "phone_btn_alert", clicked=ui.returns("OK"), xalign=0.02, yalign=0.02)
    if notifications:
        play sound "sound_effects/message.mp3"
    $ renpy.pause(2)

$ ui.imagebutton("fr_ep1_dad", "fr_ep1_go_right", clicked=ui.returns("go_right"), xpos=1690, ypos=250)
$ ui.imagebutton("fr_ep1_dad", "fr_ep1_go_left", clicked=ui.returns("go_left"), xpos=20, ypos=250)
$ ui.imagebutton("ep3_maya_freeroam_bg_desk_idle", "ep3_maya_freeroam_bg_desk_hover", clicked=ui.returns("go_up"), xpos=0, ypos=0, focus_mask=True)
$ result = ui.interact()

if result == "go_right":
    jump ep1_maya2_freeroam_right_label
elif result == "go_left":
    jump ep1_maya2_freeroam_left_label
elif result == "go_up":
    jump ep1_maya2_freeroam_up_label

label ep1_maya2_freeroam_right_label:
$ currentFreeRoamLabel = "ep1_maya2_freeroam_right_label"
$ closet_open = False
$ phone_call_enabled = True
scene ep1_maya_freeroam_bg2b
label ep1_maya2_freeroam_right_label_nofx:
$ ui.imagebutton("arrow_invis", "fr_ep1_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840)
if closet_open:
    if not persistent.ep1_card17:
        $ ui.imagebutton("fr_ep1_hidden_18", "fr_ep1_hidden_18_hover", clicked=ui.returns("hidden_card"), xpos=625, ypos=916)
elif True:
    $ ui.imagebutton("ep1_maya_freeroam_bg2b_closet_idle", "ep1_maya_freeroam_bg2b_closet_hover", clicked=ui.returns("closet"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep1_maya_freeroam_bg2b_notes_idle", "ep1_maya_freeroam_bg2b_notes_hover", clicked=ui.returns("examine"), xpos=0, ypos=0, focus_mask=True)
$ result = ui.interact()
if result == "go_down":
    scene ep1_nomaya_freeroam_bg
    jump ep1_maya2_freeroam_label_nofx
elif result == "examine":
    jump ep1_maya2_freeroam_notes_label
elif result == "closet":
    $ closet_open = True
    if persistent.ep1_card17:
        scene ep1_maya_freeroam_bg2 with dissolve
    elif True:
        scene ep1_maya_freeroam_bg2_card with dissolve
    jump ep1_maya2_freeroam_right_label_nofx
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep1_card17 = True
    $ persistent.rew_mixed_unlocked += 1
    $ chat_new_rewards = True
    $ calcRenders()
    scene ep1_maya_freeroam_bg2 with dissolve
    hide screen phone_screen
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    show screen phone_screen
    jump ep1_maya2_freeroam_right_label_nofx

label ep1_maya2_freeroam_notes_label:
$ currentFreeRoamLabel = "ep1_maya2_freeroam_notes_label"
$ phone_call_enabled = True
if found_money:
    scene ep1_maya_freeroam_bg7
elif True:
    scene ep1_maya_freeroam_bg7_money
$ ui.imagebutton("arrow_invis", "fr_ep1_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840)
if not found_money:
    $ ui.imagebutton("fr_money_maya_ep1", "fr_money_maya_ep1_hover", clicked=ui.returns("money"), xpos=1062, ypos=0)
$ result = ui.interact()
if result == "go_down":
    jump ep1_maya2_freeroam_right_label
elif result == "money":
    $ mny(dollar)
    $ found_money = True
    show screen moneymsg
    scene ep1_maya_freeroam_bg7 with dissolve
    $ renpy.pause(3)
    hide screen moneymsg
    jump ep1_maya2_freeroam_notes_label

label ep1_maya2_freeroam_left_label:
scene ep1_maya_freeroam_bg3b
label ep1_maya2_freeroam_left_label_nofx:
$ currentFreeRoamLabel = "ep1_maya2_freeroam_left_label"
$ phone_call_enabled = True
$ ui.imagebutton("fr_ep1_dad", "fr_ep1_go_right", clicked=ui.returns("go_right"), xpos=1690, ypos=250)
$ ui.imagebutton("ep1_maya_freeroam_bg3b_desk_idle", "ep1_maya_freeroam_bg3b_desk_hover", clicked=ui.returns("examine"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep1_maya_freeroam_bg3_bed_idle", "ep1_maya_freeroam_bg3_bed_hover", clicked=ui.returns("bed"), xpos=0, ypos=0, focus_mask=True)
$ result = ui.interact()
if result == "go_right":
    scene ep1_nomaya_freeroam_bg
    jump ep1_maya2_freeroam_label_nofx
elif result == "examine":
    jump ep1_maya2_freeroam_dresser_label
elif result == "bed":
    $ phone_call_enabled = False
    menu:
        "End the day" if True:
            $ renpy.block_rollback()
            $ phone_call_enabled = False
            $ chat_new_tasks = False
            $ loopMusic = False
            stop music fadeout 3
            $ phone_clear_jump_label = "ep1_ending_scene"
            jump clear_phone_chat
        "Stay up a little bit longer" if True:
            jump ep1_maya2_freeroam_left_label_nofx

label ep1_maya2_freeroam_up_label:
$ currentFreeRoamLabel = "ep1_maya2_freeroam_up_label"
$ phone_call_enabled = True
scene ep1_maya_freeroam_bg5
if minigames:
    $ ui.imagebutton("ep1_maya_freeroam_bg5_desk_idle", "ep1_maya_freeroam_bg5_desk_hover", clicked=ui.returns("study"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep1_hallway2_shower", "fr_ep1_go_up", clicked=ui.returns("go_up"), xpos=0, ypos=20)
$ ui.imagebutton("arrow_invis", "fr_ep1_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840)
$ result = ui.interact()
if result == "go_down":
    scene ep1_nomaya_freeroam_bg
    jump ep1_maya2_freeroam_label_nofx
elif result == "go_up":
    jump ep1_maya2_freeroam_up2_label
elif result == "study":
    $ renpy.block_rollback()
    if studied:
        mc "(I already studied...)"
        mc "(That's enough for tonight.)"
        jump ep1_maya2_freeroam_up_label
    $ studied = True
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
    jump ep1_maya2_freeroam_up_label

label ep1_maya2_freeroam_up2_label:
$ currentFreeRoamLabel = "ep1_maya2_freeroam_up2_label"
$ phone_call_enabled = True
if not persistent.ep1_card11:
    scene ep1_maya_freeroam_bg6_card
elif True:
    scene ep1_maya_freeroam_bg6
$ ui.imagebutton("arrow_invis", "fr_ep1_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840)
if not persistent.ep1_card11:
    $ ui.imagebutton("fr_ep1_hidden_11", "fr_ep1_hidden_11_hover", clicked=ui.returns("hidden_card"), xpos=1364, ypos=72)
$ result = ui.interact()
if result == "go_down":
    jump ep1_maya2_freeroam_up_label
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep1_card11 = True
    $ persistent.rew_josy_unlocked += 1
    $ chat_new_rewards = True
    $ calcRenders()
    scene ep1_maya_freeroam_bg6 with dissolve
    hide screen phone_screen
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    show screen phone_screen
    jump ep1_maya2_freeroam_up2_label

label ep1_maya2_freeroam_dresser_label:
$ currentFreeRoamLabel = "ep1_maya2_freeroam_dresser_label"
$ phone_call_enabled = True
if not persistent.ep1_card12:
    scene ep1_maya_freeroam_bg4_card
elif True:
    scene ep1_maya_freeroam_bg4
$ ui.imagebutton("arrow_invis", "fr_ep1_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=900)
if not persistent.ep1_card12:
    $ ui.imagebutton("fr_ep1_card12", "fr_ep1_card12_hover", clicked=ui.returns("hidden_card"), xpos=936, ypos=760)
$ result = ui.interact()
if result == "go_down":
    jump ep1_maya2_freeroam_left_label
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep1_card12 = True
    $ persistent.rew_riona_unlocked += 1
    $ chat_new_rewards = True
    $ calcRenders()
    scene ep1_maya_freeroam_bg4 with dissolve
    hide screen phone_screen
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    show screen phone_screen
    jump ep1_maya2_freeroam_dresser_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
