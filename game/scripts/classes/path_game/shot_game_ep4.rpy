
screen ep4_random_screen_start:

    modal True tag ep4_random_screen_start
    imagebutton:
        focus_mask True
        idle Transform(pathStartVar)
        hover Transform(pathStartVar)
        hovered (Hide("ep4_random_screen_start"), Show("ep4_random_screen"))
        action NullAction()
        xpos 0
        ypos 0
screen ep4_random_screen:

    modal True tag ep4_hand_screen
    timer 10 action [Hide('ep4_random_screen'), Hide(pathVar), SetVariable("shotFail", shotFail+1), Play("sfx1", "sound_effects/fail.mp3", loop = False),Jump(pathMainLabel)]
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
        hovered (Hide("ep4_random_screen"), Hide(pathVar),SetVariable("shotFail", shotFail+1), Play("sfx1", "sound_effects/fail.mp3", loop = False),Jump(pathMainLabel))
        action NullAction()
        xpos 0
        ypos 0
    imagebutton:
        focus_mask True
        idle Transform(pathGoalVar)
        hover Transform(pathGoalVar)
        hovered (Hide("ep4_random_screen"),SetVariable("shotWon", shotWon+1), Hide(pathVar), Play("sfx1", "sound_effects/win.mp3", loop = False), Jump(pathMainLabel))
        action NullAction()
        xpos 0
        ypos 0

label ep4_shot_game_label:
$ shotFail = 0
$ shotWon = 0
$ _game_menu_screen = None
$ pathRandomArray = ["ep2_path1_start", "ep2_path1_goal", "ep2_path1_nozone_fix", "ep2_path1", "ep2_path2_start", "ep2_path2_goal", "ep2_path2_nozone_fix", "ep2_path2","ep2_path3_start", "ep2_path3_goal", "ep2_path3_nozone_fix", "ep2_path3", "ep2_path4_start", "ep2_path4_goal", "ep2_path4_nozone_fix", "ep2_path4", "ep3_path1_start", "ep3_path1_goal", "ep3_path1_nozone_fix", "ep3_path1", "ep3_path2_start", "ep3_path2_goal", "ep3_path2_nozone_fix", "ep3_path2","ep3_path3_start", "ep3_path3_goal", "ep3_path3_nozone_fix", "ep3_path3", "ep3_path4_start", "ep3_path4_goal", "ep3_path4_nozone_fix", "ep3_path4","ep2_path5_start", "ep2_path5_goal", "ep2_path5_nozone_fix", "ep2_path5","ep2_path6_start", "ep2_path6_goal", "ep2_path6_nozone_fix", "ep2_path6"]
$ pathIntArray = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
$ renpy.random.shuffle(pathIntArray)
$ pathInt = 0
$ pathMainLabel = "ep4_shot_game_loop_label"
$ renpy.block_rollback()
hide screen phone_screen

label ep4_shot_game_loop_label:
if shotFail + shotWon == 5:
    if shotFail < 3:
        jump ep4_shot_game_won_label
    elif True:
        jump ep4_shot_game_lost_label

scene ep4_derek_beer2 with dissolve
show screen shot_text_screen
$ renpy.pause()
hide screen shot_text_screen
scene ep4_derek_beer1 with dissolve
$ pathStartVar = pathRandomArray[pathIntArray[pathInt]*4]
$ pathGoalVar = pathRandomArray[pathIntArray[pathInt]*4 + 1]
$ pathNoZoneVar = pathRandomArray[pathIntArray[pathInt]*4 + 2]
$ pathLabel = "ep4_shot_game_loop_label"
$ pathVar = pathRandomArray[pathIntArray[pathInt]*4 + 3]
$ pathInt += 1

label ep4_shot_game_loop_label_nofx:
$ renpy.block_rollback()
show screen ep4_random_screen_start
$ renpy.pause()
jump ep4_shot_game_loop_label_nofx

label ep4_shot_game_won_label:
$ renpy.block_rollback()
hide screen ep4_random_screen_start
hide screen ep4_random_screen
if shotFail == 0:
    $ maxedPaths += 1
    if not persistent.ep4_card15 or not persistent.ep4_card16:
        if not persistent.ep4_card15:
            $ persistent.ep4_card15 = True
            $ persistent.rew_sage_unlocked += 1
            $ calcRenders()
        if not persistent.ep4_card16:
            $ persistent.ep4_card16 = True
            $ persistent.rew_camila_unlocked += 1
            $ calcRenders()
        $ chat_new_rewards = True
        show screen srmsg
        $ renpy.pause(3)
        hide screen srmsg
elif shotFail < 3 and not persistent.ep4_card15:
    $ persistent.ep4_card15 = True
    $ persistent.rew_sage_unlocked += 1
    $ chat_new_rewards = True
    $ calcRenders()
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
show screen phone_screen
$ _game_menu_screen = "save"
if steamAchievements and maxedPaths == 4 and not config.console and not config.developer:
    $ achievement.grant("DRINKDRINKDRINK")
    init:
        $ achievement.register("DRINKDRINKDRINK")
    $ achievement.Sync()
jump ep4_sat_morning_label2

label ep4_shot_game_lost_label:
$ renpy.block_rollback()
hide screen ep4_random_screen_start
hide screen ep4_random_screen
show screen phone_screen
$ _game_menu_screen = "save"
jump ep4_sat_morning_label2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
