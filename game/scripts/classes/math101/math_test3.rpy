label math101_test3:
hide screen phone_screen
$ math_cheat = False
$ math_cheats_left = 1 + mathCheatBoost
show screen scr_math101_cheats_left
$ myZorder = 1
$ mathTestScore = 0
$ math_questions = 10
$ math_answers = ["b","a","a","b","c","d","b","d","a","d"]
$ math_test_name = "images/classes/math101/test03/math03_test%d.jpg"
$ count = 1

while count<11:
    show expression (math_test_name % count) zorder myZorder:
        size (config.screen_width, config.screen_height)
    $ ui.imagebutton("math_choice", "math_choice_hover", clicked=ui.returns("a"), xpos=1020, ypos=330)
    $ ui.imagebutton("math_choice", "math_choice_hover", clicked=ui.returns("b"), xpos=1320, ypos=330)
    $ ui.imagebutton("math_choice", "math_choice_hover", clicked=ui.returns("c"), xpos=1020, ypos=630)
    $ ui.imagebutton("math_choice", "math_choice_hover", clicked=ui.returns("d"), xpos=1320, ypos=630)
    if math_cheats_left >  0:
        $ ui.imagebutton("math_cheat", "math_cheat_hover", clicked=ui.returns("CHEAT"), xpos=1030, ypos=870)
    $ ui.imagebutton("classes_view_tutorial_idle", "classes_view_tutorial_hover", clicked=ui.returns("TUTORIAL"), xpos=1400, ypos=120)
    $ result = ui.interact()
    if result == math_answers[count-1]:
        $ mathTestScore += 1
    elif result == "CHEAT":
        $ mathTestScore += 1
        $ math_cheats_left -= 1
        $ math_cheat = True
    elif result == "TUTORIAL":
        show screen scr_math101_tutorial
        $ count -= 1
    $ count += 1
    $ renpy.block_rollback()

scene desk_bg with dissolve
if mathTestScore == 10:
    $ maxedMath += 1
$ mathResult = int(100 * mathTestScore / math_questions)
$ mathVar = 90 - mathBoost
$ mathVar2 = 50 - mathBoost


if mathTestScore == 10:
    $ ui.imagebutton("classes_perfect", "classes_perfect", clicked=ui.returns("NULL"), xalign=0.49, yalign=0.14)
elif mathResult + bonusPercentageMath >= 90 - mathBoost:
    $ ui.imagebutton("classes_great", "classes_great", clicked=ui.returns("NULL"), xalign=0.49, yalign=0.14)
elif mathResult + bonusPercentageMath >= 70 - mathBoost:
    $ ui.imagebutton("classes_good", "classes_good", clicked=ui.returns("NULL"), xalign=0.49, yalign=0.14)
elif True:
    $ ui.imagebutton("classes_fail", "classes_fail", clicked=ui.returns("NULL"), xalign=0.49, yalign=0.14)

hide screen scr_math101_cheats_left
show text "{font=bradhitc.ttf}{color=#2b2b2b}{size=+50}[mathResult] + {color=#26ef4b}[bonusPercentageMath]{/color}%{/size}{/color}{/font}":
    yalign 0.4
if mathResult + bonusPercentageMath >= 90 - mathBoost:
    $ passedMath += 1
    if not persistent.ep3_card6:
        $ chat_new_rewards = True
        $ persistent.rew_jade_unlocked += 1
        $ persistent.ep3_card6 = True
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
show screen phone_screen
jump ep3_after_math_test
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
