screen scr_math101_tutorial:

    modal True tag scr_math101_tutorial
    imagebutton:
        idle "math_tutorial_full"
        hover "math_tutorial_full"
        action Hide("scr_math101_tutorial")

screen scr_math101_cheats_left:
    text "{font=Redressed.ttf}{color=#2b2b2b}[math_cheats_left]{/color}{/font}" xpos 0.785 ypos 0.835

label math101_test1:
hide screen phone_screen
$ math_cheat = False
$ math_cheats_left = 1 + mathCheatBoost
scene math1_test1 with dissolve
show text "{color=#000000}{i}\nIn this example, the test follows a numerical pattern.{/i}{/color}" at top
$ renpy.pause()
show text "{color=#000000}{i}\nThe correct answer is {b}d{/b}.{/i}{/color}" at top
$ renpy.pause()
scene math1_test2 with dissolve
show text "{color=#000000}{i}\nTests can also consist of patterns.{/i}{/color}" at top
$ renpy.pause()
show text "{color=#000000}{i}\nIn this test, the correct answer is {b}b{/b}.{/i}{/color}" at top
$ renpy.pause()
show text "{color=#000000}{i}\nLet's begin!{/i}{/color}" at top
$ renpy.pause()
show screen scr_math101_cheats_left
$ myZorder = 1
$ mathTestScore = 0

show math1_test3 zorder myZorder:
    size (config.screen_width, config.screen_height)
$ ui.imagebutton("math_choice", "math_choice_hover", clicked=ui.returns("choice_a"), xpos=1020, ypos=330)
$ ui.imagebutton("math_choice", "math_choice_hover", clicked=ui.returns("choice_b"), xpos=1320, ypos=330)
$ ui.imagebutton("math_choice", "math_choice_hover", clicked=ui.returns("choice_c"), xpos=1020, ypos=630)
$ ui.imagebutton("math_choice", "math_choice_hover", clicked=ui.returns("choice_d"), xpos=1320, ypos=630)
if math_cheats_left >  0:
    $ ui.imagebutton("math_cheat", "math_cheat_hover", clicked=ui.returns("CHEAT"), xpos=1030, ypos=870)
$ result = ui.interact()
if result == "choice_c":
    $ mathTestScore += 1
elif result == "CHEAT":
    $ mathTestScore += 1
    $ math_cheats_left -= 1
    $ math_cheat = True
$ renpy.block_rollback()

show math1_test4 zorder myZorder:
    size (config.screen_width, config.screen_height)
hide math1_test3
$ ui.imagebutton("math_choice", "math_choice_hover", clicked=ui.returns("choice_a"), xpos=1020, ypos=330)
$ ui.imagebutton("math_choice", "math_choice_hover", clicked=ui.returns("choice_b"), xpos=1320, ypos=330)
$ ui.imagebutton("math_choice", "math_choice_hover", clicked=ui.returns("choice_c"), xpos=1020, ypos=630)
$ ui.imagebutton("math_choice", "math_choice_hover", clicked=ui.returns("choice_d"), xpos=1320, ypos=630)
if math_cheats_left >  0:
    $ ui.imagebutton("math_cheat", "math_cheat_hover", clicked=ui.returns("CHEAT"), xpos=1030, ypos=870)
$ result = ui.interact()
if result == "choice_b":
    $ mathTestScore += 1
elif result == "CHEAT":
    $ mathTestScore += 1
    $ math_cheats_left -= 1
    $ math_cheat = True
$ renpy.block_rollback()

show math1_test5 zorder myZorder:
    size (config.screen_width, config.screen_height)
hide math1_test4
$ ui.imagebutton("math_choice", "math_choice_hover", clicked=ui.returns("choice_a"), xpos=1020, ypos=330)
$ ui.imagebutton("math_choice", "math_choice_hover", clicked=ui.returns("choice_b"), xpos=1320, ypos=330)
$ ui.imagebutton("math_choice", "math_choice_hover", clicked=ui.returns("choice_c"), xpos=1020, ypos=630)
$ ui.imagebutton("math_choice", "math_choice_hover", clicked=ui.returns("choice_d"), xpos=1320, ypos=630)
if math_cheats_left >  0:
    $ ui.imagebutton("math_cheat", "math_cheat_hover", clicked=ui.returns("CHEAT"), xpos=1030, ypos=870)
$ result = ui.interact()
if result == "choice_d":
    $ mathTestScore += 1
elif result == "CHEAT":
    $ mathTestScore += 1
    $ math_cheats_left -= 1
    $ math_cheat = True
$ renpy.block_rollback()

show math1_test6 zorder myZorder:
    size (config.screen_width, config.screen_height)
hide math1_test5
$ ui.imagebutton("math_choice", "math_choice_hover", clicked=ui.returns("choice_a"), xpos=1020, ypos=330)
$ ui.imagebutton("math_choice", "math_choice_hover", clicked=ui.returns("choice_b"), xpos=1320, ypos=330)
$ ui.imagebutton("math_choice", "math_choice_hover", clicked=ui.returns("choice_c"), xpos=1020, ypos=630)
$ ui.imagebutton("math_choice", "math_choice_hover", clicked=ui.returns("choice_d"), xpos=1320, ypos=630)
if math_cheats_left >  0:
    $ ui.imagebutton("math_cheat", "math_cheat_hover", clicked=ui.returns("CHEAT"), xpos=1030, ypos=870)
$ result = ui.interact()
if result == "choice_a":
    $ mathTestScore += 1
elif result == "CHEAT":
    $ mathTestScore += 1
    $ math_cheats_left -= 1
    $ math_cheat = True
$ renpy.block_rollback()

show math1_test7 zorder myZorder:
    size (config.screen_width, config.screen_height)
hide math1_test6
$ ui.imagebutton("math_choice", "math_choice_hover", clicked=ui.returns("choice_a"), xpos=1020, ypos=330)
$ ui.imagebutton("math_choice", "math_choice_hover", clicked=ui.returns("choice_b"), xpos=1320, ypos=330)
$ ui.imagebutton("math_choice", "math_choice_hover", clicked=ui.returns("choice_c"), xpos=1020, ypos=630)
$ ui.imagebutton("math_choice", "math_choice_hover", clicked=ui.returns("choice_d"), xpos=1320, ypos=630)
if math_cheats_left >  0:
    $ ui.imagebutton("math_cheat", "math_cheat_hover", clicked=ui.returns("CHEAT"), xpos=1030, ypos=870)
$ result = ui.interact()
if result == "choice_d":
    $ mathTestScore += 1
elif result == "CHEAT":
    $ mathTestScore += 1
    $ math_cheats_left -= 1
    $ math_cheat = True
$ renpy.block_rollback()

show math1_test8 zorder myZorder:
    size (config.screen_width, config.screen_height)
hide math1_test7
$ ui.imagebutton("math_choice", "math_choice_hover", clicked=ui.returns("choice_a"), xpos=1020, ypos=330)
$ ui.imagebutton("math_choice", "math_choice_hover", clicked=ui.returns("choice_b"), xpos=1320, ypos=330)
$ ui.imagebutton("math_choice", "math_choice_hover", clicked=ui.returns("choice_c"), xpos=1020, ypos=630)
$ ui.imagebutton("math_choice", "math_choice_hover", clicked=ui.returns("choice_d"), xpos=1320, ypos=630)
if math_cheats_left >  0:
    $ ui.imagebutton("math_cheat", "math_cheat_hover", clicked=ui.returns("CHEAT"), xpos=1030, ypos=870)
$ result = ui.interact()
if result == "choice_c":
    $ mathTestScore += 1
elif result == "CHEAT":
    $ mathTestScore += 1
    $ math_cheats_left -= 1
    $ math_cheat = True
$ renpy.block_rollback()
scene desk_bg with dissolve
if mathTestScore == 6:
    $ maxedMath += 1
$ mathResult = int(100 * mathTestScore / 6)
$ mathVar = 90 - mathBoost
$ mathVar2 = 70 - mathBoost
hide screen scr_math101_cheats_left
$ ui.imagebutton("classes_you_scored", "classes_you_scored", clicked=ui.returns("NULL"), xalign=0.48, yalign=0.3)

if mathTestScore == 6:
    $ ui.imagebutton("classes_perfect", "classes_perfect", clicked=ui.returns("NULL"), xalign=0.49, yalign=0.14)
elif mathResult + bonusPercentageMath >= 90 - mathBoost:
    $ ui.imagebutton("classes_great", "classes_great", clicked=ui.returns("NULL"), xalign=0.49, yalign=0.14)
elif mathResult + bonusPercentageMath >= 70 - mathBoost:
    $ ui.imagebutton("classes_good", "classes_good", clicked=ui.returns("NULL"), xalign=0.49, yalign=0.14)
elif True:
    $ ui.imagebutton("classes_fail", "classes_fail", clicked=ui.returns("NULL"), xalign=0.49, yalign=0.14)

show text "{font=bradhitc.ttf}{color=#2b2b2b}{size=+50}[mathResult] + {color=#26ef4b}[bonusPercentageMath]{/color}%{/size}{/color}{/font}":
    yalign 0.4

if mathResult + bonusPercentageMath >= 90 - mathBoost:
    $ passedMath += 1
    if not persistent.ep1_card7:
        $ chat_new_rewards = True
        $ persistent.rew_josy_unlocked += 1
        $ persistent.ep1_card7 = True
        $ calcRenders()
        $ ui.imagebutton("classes_special_render", "classes_special_render", clicked=ui.returns("NULL"), xalign=0.48, yalign=0.6)
    if nerdNotes:
        $ ui.imagebutton("classes_nerd_notes", "classes_nerd_notes", clicked=ui.returns("NULL"), xalign=0.48, yalign=0.8)
        $ mny(1)
    if math_cheat:
        $ ui.imagebutton("classes_with_cheating", "classes_with_cheating", clicked=ui.returns("NULL"), xalign=0.48, yalign=0.7)
        $ dk(1)
    elif True:
        $ ui.imagebutton("classes_without_cheating", "classes_without_cheating", clicked=ui.returns("NULL"), xalign=0.48, yalign=0.7)
        $ dk(-1)
elif mathResult + bonusPercentageMath >= 70 - mathBoost:
    $ passedMath += 1
    if nerdNotes:
        $ ui.imagebutton("classes_nerd_notes", "classes_nerd_notes", clicked=ui.returns("NULL"), xalign=0.48, yalign=0.8)
        $ mny(1)
    if math_cheat:
        $ ui.imagebutton("classes_with_cheating", "classes_with_cheating", clicked=ui.returns("NULL"), xalign=0.48, yalign=0.7)
        $ dk(1)
    elif True:
        $ ui.imagebutton("classes_without_cheating", "classes_without_cheating", clicked=ui.returns("NULL"), xalign=0.48, yalign=0.7)
        $ dk(-1)
elif True:
    if steamAchievements and not config.console and not config.developer:
        $ achievement.grant("FISFORFAILURE")
        init:
            $ achievement.register("FISFORFAILURE")
        $ achievement.Sync()
    $ ui.imagebutton("classes_failed_test", "classes_failed_test", clicked=ui.returns("NULL"), xalign=0.48, yalign=0.7)
    $ failedMath += 1
if steamAchievements and mathResult + bonusPercentageMath >= 70 - mathBoost and not config.console and not config.developer:
    if math_cheat:
        $ achievement.grant("NOTSOHONORABLESTUDENT")
        init:
            $ achievement.register("NOTSOHONORABLESTUDENT")
    elif True:
        $ achievement.grant("HONORABLESTUDENT")
        init:
            $ achievement.register("HONORABLESTUDENT")
    $ achievement.Sync()
$ bonusPercentageMath = 0
$ renpy.pause()
hide text
if tutorials:
    scene black with fade
    show text "{i}You can buy items to lower the limit for getting lewd renders and to increase your cheating skill. By studying you can make the Math tests easier to pass.{/i}"
    $ renpy.pause()
show screen phone_screen
jump ep1_after_math_test
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
