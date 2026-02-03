
screen ep2_random_screen_start:

    modal True tag ep2_random_screen_start
    imagebutton:
        focus_mask True
        idle Transform(pathStartVar)
        hover Transform(pathStartVar)
        hovered (Hide("ep2_random_screen_start"), Show("ep2_random_screen"))
        action NullAction()
        xpos 0
        ypos 0
screen ep2_random_screen:

    modal True tag ep2_hand_screen
    timer 10 action [Hide('ep2_random_screen'), Hide(pathVar), SetVariable("shotFail", shotFail+1), Play("sfx1", "sound_effects/fail.mp3", loop = False),Jump(pathMainLabel)]
    imagebutton:
        focus_mask True
        idle Transform(pathVar)
        hover Transform(pathVar)
        action NullAction()
        xpos 0
        ypos 0
    imagebutton:
        focus_mask True
        idle Transform(pathNoZoneVar)
        hover Transform(pathNoZoneVar)
        hovered (Hide("ep2_random_screen"), Hide(pathVar),SetVariable("shotFail", shotFail+1), Play("sfx1", "sound_effects/fail.mp3", loop = False),Jump(pathMainLabel))
        action NullAction()
        xpos 0
        ypos 0
    imagebutton:
        focus_mask True
        idle Transform(pathGoalVar)
        hover Transform(pathGoalVar)
        hovered (Hide("ep2_random_screen"),SetVariable("shotWon", shotWon+1), Hide(pathVar), Play("sfx1", "sound_effects/win.mp3", loop = False), Jump(pathMainLabel))
        action NullAction()
        xpos 0
        ypos 0

label ep2_shot_game_label:
$ shotFail = 0
$ shotWon = 0
$ _game_menu_screen = None
$ pathRandomArray = ["ep2_path1_start", "ep2_path1_goal", "ep2_path1_nozone_fix", "ep2_path1", "ep2_path2_start", "ep2_path2_goal", "ep2_path2_nozone_fix", "ep2_path2","ep2_path3_start", "ep2_path3_goal", "ep2_path3_nozone_fix", "ep2_path3", "ep2_path4_start", "ep2_path4_goal", "ep2_path4_nozone_fix", "ep2_path4","ep2_path5_start", "ep2_path5_goal", "ep2_path5_nozone_fix", "ep2_path5","ep2_path6_start", "ep2_path6_goal", "ep2_path6_nozone_fix", "ep2_path6"]
$ pathIntArray = [0, 1, 2, 3, 4, 5]
$ renpy.random.shuffle(pathIntArray)
$ pathInt = 0
$ pathMainLabel = "ep2_shot_game_loop_label"
$ renpy.block_rollback()
hide screen phone_screen
$ ep2_hand_shot = True
$ ep2_mouth_shot = True
$ ep2_belly_shot = True

label ep2_shot_game_loop_label:
if ep2_hand_shot and ep2_mouth_shot and ep2_belly_shot:
    scene ep2_fri_shots3 with dissolve
elif ep2_hand_shot and ep2_mouth_shot:
    scene ep2_fri_shots5 with dissolve
    tm "YES!"
    scene ep2_fri_shots3_2nobelly with dissolve
elif ep2_hand_shot and ep2_belly_shot:
    scene ep2_fri_shots5 with dissolve
    rs "GO! GO! GO!"
    scene ep2_fri_shots3_2nomouth with dissolve
elif ep2_mouth_shot and ep2_belly_shot:
    scene ep2_fri_shots5 with dissolve
    rs "GO! GO! GO!"
    scene ep2_fri_shots3_2nohand with dissolve
elif ep2_mouth_shot:
    scene ep2_fri_shots5 with dissolve
    rs "Almost there now! Push!!"
    scene ep2_fri_shots3_1mouth with dissolve
elif ep2_belly_shot:
    scene ep2_fri_shots5 with dissolve
    rs "Almost there now! Push!!"
    scene ep2_fri_shots3_1belly with dissolve
elif ep2_hand_shot:
    scene ep2_fri_shots5 with dissolve
    rs "Almost there now! Push!!"
    scene ep2_fri_shots3_1hand with dissolve
elif True:
    if shotFail < 2:
        jump ep2_shot_game_won_label
    elif True:
        jump ep2_shot_game_lost_label
show screen shot_text_screen2
$ renpy.pause()
hide screen shot_text_screen2

if ep2_hand_shot:
    $ ui.imagebutton("ep2_hand_shot", "ep2_hand_shot_hover", clicked=ui.returns("HAND"), xpos=56, ypos=62)
if ep2_mouth_shot:
    $ ui.imagebutton("ep2_mouth_shot", "ep2_mouth_shot_hover", clicked=ui.returns("MOUTH"), xpos=576, ypos=274)
if ep2_belly_shot:
    $ ui.imagebutton("ep2_belly_shot", "ep2_belly_shot_hover", clicked=ui.returns("BELLY"), xpos=1609, ypos=543)
$ result = ui.interact()
$ renpy.block_rollback()

if result == "HAND":
    $ pathStartVar = pathRandomArray[pathIntArray[pathInt]*4]
    $ pathGoalVar = pathRandomArray[pathIntArray[pathInt]*4 + 1]
    $ pathNoZoneVar = pathRandomArray[pathIntArray[pathInt]*4 + 2]
    $ pathLabel = "ep2_shot_game_hand_loop_label"
    $ pathVar = pathRandomArray[pathIntArray[pathInt]*4 + 3]
    $ pathInt += 1
    $ ep2_hand_shot = False
    jump ep2_shot_game_hand_loop_label
elif result == "MOUTH":
    $ pathStartVar = pathRandomArray[pathIntArray[pathInt]*4]
    $ pathGoalVar = pathRandomArray[pathIntArray[pathInt]*4 + 1]
    $ pathNoZoneVar = pathRandomArray[pathIntArray[pathInt]*4 + 2]
    $ pathVar = pathRandomArray[pathIntArray[pathInt]*4 + 3]
    $ pathLabel = "ep2_shot_game_mouth_loop_label"
    $ pathInt += 1
    $ ep2_mouth_shot = False
    jump ep2_shot_game_mouth_loop_label
elif result == "BELLY":
    $ pathStartVar = pathRandomArray[pathIntArray[pathInt]*4]
    $ pathNoZoneVar = pathRandomArray[pathIntArray[pathInt]*4 + 2]
    $ pathGoalVar = pathRandomArray[pathIntArray[pathInt]*4 + 1]
    $ pathVar = pathRandomArray[pathIntArray[pathInt]*4 + 3]
    $ pathLabel = "ep2_shot_game_belly_loop_label"
    $ pathInt += 1
    $ ep2_belly_shot = False
    jump ep2_shot_game_belly_loop_label
elif True:
    jump ep2_shot_game_loop_label


label ep2_shot_game_hand_loop_label:
scene ep2_fri_shots3_hand with dissolve
label ep2_shot_game_hand_loop_label_nofx:
$ renpy.block_rollback()
show screen ep2_random_screen_start
$ renpy.pause()
jump ep2_shot_game_hand_loop_label_nofx

label ep2_shot_game_mouth_loop_label:
scene ep2_fri_shots3_mouth with dissolve
label ep2_shot_game_mouth_loop_label_nofx:
$ renpy.block_rollback()
show screen ep2_random_screen_start
$ renpy.pause()
jump ep2_shot_game_mouth_loop_label_nofx

label ep2_shot_game_belly_loop_label:
scene ep2_fri_shots3_belly with dissolve
label ep2_shot_game_belly_loop_label_nofx:
$ renpy.block_rollback()
show screen ep2_random_screen_start
$ renpy.pause()
jump ep2_shot_game_belly_loop_label_nofx


label ep2_shot_game_won_label:
$ renpy.block_rollback()
hide screen ep2_random_screen_start
hide screen ep2_random_screen
if shotFail == 0:
    $ maxedPaths = 1
    if not persistent.ep2_card17:
        $ persistent.ep2_card17 = True
        $ persistent.rew_mixed_unlocked += 1
        $ chat_new_rewards = True
        $ calcRenders()
        show screen srmsg
        $ renpy.pause(3)
        hide screen srmsg
$ ep2_shotWon = True
show screen phone_screen
$ _game_menu_screen = "save"
jump ep2_after_shot_game_label

label ep2_shot_game_lost_label:
$ renpy.block_rollback()
hide screen ep2_random_screen_start
hide screen ep2_random_screen

$ ep2_shotWon = False
show screen phone_screen
$ _game_menu_screen = "save"
jump ep2_after_shot_game_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
