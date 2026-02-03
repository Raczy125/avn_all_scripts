label ep1_freeroam_maya_label:
$ freeRoamID = 3
$ firstTimeFreeRoam = True
$ found_money = False
$ studied = False
label ep1_maya_freeroam_label:
scene ep1_maya_freeroam_bg with fade
label ep1_maya_freeroam_label_nofx:
$ currentFreeRoamLabel = "ep1_maya_freeroam_label"
if firstTimeFreeRoam:
    $ firstTimeFreeRoam = False
    show white_screen with dissolve
    $ current_task = "Bond with Maya and go to bed."
    $ chat_new_tasks = True
    show text "{font=collegiate.ttf}{size=+40}{color=#fe961b}Task:{/color} Bond with Maya and go to bed.{/size}{/font}":
        ypos 0.825
        xpos 0.5
    $ renpy.pause()
    hide text
    hide white_screen

if not ep1_maya_talk:
    $ ui.imagebutton("ep2_maya_freeroam_bg_maya_idle", "ep2_maya_freeroam_bg_maya_hover", clicked=ui.returns("maya_talk"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("fr_ep1_dad", "fr_ep1_go_right", clicked=ui.returns("go_right"), xpos=1690, ypos=250)
$ ui.imagebutton("fr_ep1_dad", "fr_ep1_go_left", clicked=ui.returns("go_left"), xpos=20, ypos=250)
$ ui.imagebutton("ep3_maya_freeroam_bg_desk_idle", "ep3_maya_freeroam_bg_desk_hover", clicked=ui.returns("go_up"), xpos=0, ypos=0, focus_mask=True)
$ result = ui.interact()

if result == "maya_talk":
    jump ep1_maya_freeroam_talk_label
elif result == "go_right":
    jump ep1_maya_freeroam_right_label
elif result == "go_left":
    jump ep1_maya_freeroam_left_label
elif result == "go_up":
    jump ep1_maya_freeroam_up_label

label ep1_maya_freeroam_talk_label:
$ guideSuggestedPage = 43
$ ep1_maya_talk = True
scene ep1_frmdorm1 with dissolve
mc "Hey...I didn't realize that you and Derek are siblings."
scene ep1_frmdorm2 with dissolve
my "Yeah, I was going to tell you that back in class."
my "We're twins."
scene ep1_frmdorm1b with dissolve
menu:
    "Joke" if True:
        $ RPmaya += 1
        $ dk(-1)
        if dtype > 0:
            mc "..."
            mc "So, you have a...penis?"
            scene ep1_frmdorm4 with dissolve
            my "Haha! You're an idiot!"
        elif True:
            mc "When it comes to looks, I know who got the better part of that deal."
            scene ep1_frmdorm3 with dissolve
            my "Yeah, Derek's a real looker."
            scene ep1_frmdorm1b with dissolve
            mc "No, I meant-"
            scene ep1_frmdorm4 with dissolve
            my "I'm joking, stupid."
            mc "Oh, haha."
    "Really?" if True:
        mc "Twins? Really?"
        scene ep1_frmdorm2 with dissolve
        my "Yup."
scene ep1_frmdorm1b with dissolve
mc "I would never have guessed that you were twins..."
scene ep1_frmdorm2 with dissolve
my "Yeah...well..."
my "We are very unalike."
scene ep1_frmdorm1b with dissolve
if dtype > 0:
    mc "No shit..."
elif True:
    mc "Very..."
mc "So, that's why you put up with him?"
scene ep1_frmdorm5 with dissolve
my "Well, not only because of that..."
my "Say what you want about my brother..."
my "...but he didn't give up on me."
scene ep1_frmdorm6 with dissolve
mc "Who gave up on you?"
scene ep1_frmdorm7 with dissolve
my "Please, forget that I said that..."
my "Maybe I'll tell you someday, but yeah...not today."
scene ep1_maya_freeroam_bg with dissolve
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
jump ep1_maya_freeroam_label_nofx


label ep1_maya_freeroam_right_label:
$ currentFreeRoamLabel = "ep1_maya_freeroam_right_label"
scene ep1_maya_freeroam_bg2b
$ ui.imagebutton("ep1_maya_freeroam_bg2b_notes_idle", "ep1_maya_freeroam_bg2b_notes_hover", clicked=ui.returns("examine"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep1_maya_freeroam_bg2b_closet_idle", "ep1_maya_freeroam_bg2b_closet_hover", clicked=ui.returns("closet"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep1_hallway2_shower", "fr_ep1_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=850)
$ result = ui.interact()
if result == "go_down":
    scene ep1_maya_freeroam_bg
    jump ep1_maya_freeroam_label_nofx
elif result == "examine":
    jump ep1_maya_freeroam_notes_label
elif result == "closet":
    if persistent.ep1_card17:
        scene ep1_maya_freeroam_bg2 with dissolve
    elif True:
        scene ep1_maya_freeroam_bg2_card with dissolve
    my "Erm...that's my closet, [name]."
    my "I know I told you to make yourself at home, but please let me have some privacy."
    mc "I'm sorry..."
    scene ep1_maya_freeroam_bg2b with dissolve
    jump ep1_maya_freeroam_right_label

label ep1_maya_freeroam_notes_label:
$ currentFreeRoamLabel = "ep1_maya_freeroam_notes_label"
if found_money:
    scene ep1_maya_freeroam_bg7
elif True:
    scene ep1_maya_freeroam_bg7_money
$ ui.imagebutton("ep1_hallway2_shower", "fr_ep1_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=850)
if not found_money:
    $ ui.imagebutton("fr_money_maya_ep1", "fr_money_maya_ep1_hover", clicked=ui.returns("money"), xpos=1062, ypos=0)
$ result = ui.interact()
if result == "go_down":
    jump ep1_maya_freeroam_right_label
elif result == "money":
    $ mny(dollar)
    $ found_money = True
    show screen moneymsg
    scene ep1_maya_freeroam_bg7 with dissolve
    $ renpy.pause(3)
    hide screen moneymsg
    jump ep1_maya_freeroam_notes_label

label ep1_maya_freeroam_left_label:
scene ep1_maya_freeroam_bg3
label ep1_maya_freeroam_left_label_nofx:
$ currentFreeRoamLabel = "ep1_maya_freeroam_left_label"
$ ui.imagebutton("fr_ep1_dad", "fr_ep1_go_right", clicked=ui.returns("go_right"), xpos=1690, ypos=250)
$ ui.imagebutton("ep1_maya_freeroam_bg3b_desk_idle", "ep1_maya_freeroam_bg3b_desk_hover", clicked=ui.returns("examine"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep1_maya_freeroam_bg3_bed_idle", "ep1_maya_freeroam_bg3_bed_hover", clicked=ui.returns("bed"), xpos=0, ypos=0, focus_mask=True)
$ result = ui.interact()
if result == "go_right":
    scene ep1_maya_freeroam_bg
    jump ep1_maya_freeroam_label_nofx
elif result == "examine":
    jump ep1_maya_freeroam_dresser_label
elif result == "bed":
    if current_task != "Go to bed.":
        mc "(I should chat a bit with Maya before I go to bed...)"
        jump ep1_maya_freeroam_left_label_nofx
    menu:
        "End the day" if True:
            jump ep1_maya_freeroam_sleep_label
        "Stay up a little bit longer" if True:
            jump ep1_maya_freeroam_left_label_nofx
label ep1_maya_freeroam_up_label:
$ currentFreeRoamLabel = "ep1_maya_freeroam_up_label"
scene ep1_maya_freeroam_bg5
if minigames:
    $ ui.imagebutton("ep1_maya_freeroam_bg5_desk_idle", "ep1_maya_freeroam_bg5_desk_hover", clicked=ui.returns("study"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep1_hallway2_shower", "fr_ep1_go_up", clicked=ui.returns("go_up"), xpos=0, ypos=20)
$ ui.imagebutton("ep1_hallway2_shower", "fr_ep1_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=850)
$ result = ui.interact()
if result == "go_down":
    scene ep1_maya_freeroam_bg
    jump ep1_maya_freeroam_label_nofx
elif result == "go_up":
    jump ep1_maya_freeroam_up2_label
elif result == "study":
    $ renpy.block_rollback()
    if studied:
        mc "(I already studied...)"
        mc "(That's enough for tonight.)"
        jump ep1_maya_freeroam_up_label
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
    jump ep1_maya_freeroam_up_label

label ep1_maya_freeroam_up2_label:
$ currentFreeRoamLabel = "ep1_maya_freeroam_up2_label"
if not persistent.ep1_card11:
    scene ep1_maya_freeroam_bg6_card
elif True:
    scene ep1_maya_freeroam_bg6
$ ui.imagebutton("ep1_hallway2_shower", "fr_ep1_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=850)
if not persistent.ep1_card11:
    $ ui.imagebutton("fr_ep1_hidden_11", "fr_ep1_hidden_11_hover", clicked=ui.returns("hidden_card"), xpos=1364, ypos=72)
$ result = ui.interact()
if result == "go_down":
    jump ep1_maya_freeroam_up_label
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep1_card11 = True
    $ persistent.rew_josy_unlocked += 1
    $ chat_new_rewards = True
    $ calcRenders()
    scene ep1_maya_freeroam_bg6 with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep1_maya_freeroam_up2_label

label ep1_maya_freeroam_dresser_label:
$ currentFreeRoamLabel = "ep1_maya_freeroam_dresser_label"
if not persistent.ep1_card12:
    scene ep1_maya_freeroam_bg4_card
elif True:
    scene ep1_maya_freeroam_bg4
$ ui.imagebutton("ep1_hallway2_shower", "fr_ep1_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=900)
if not persistent.ep1_card12:
    $ ui.imagebutton("fr_ep1_card12", "fr_ep1_card12_hover", clicked=ui.returns("hidden_card"), xpos=936, ypos=760)
$ result = ui.interact()
if result == "go_down":
    jump ep1_maya_freeroam_left_label
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep1_card12 = True
    $ persistent.rew_riona_unlocked += 1
    $ chat_new_rewards = True
    $ calcRenders()
    scene ep1_maya_freeroam_bg4 with dissolve
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    jump ep1_maya_freeroam_dresser_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
