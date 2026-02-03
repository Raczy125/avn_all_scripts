screen scr_english101_tutorial:

    modal True tag scr_english101_tutorial
    imagebutton:
        idle "english_tutorial_full"
        hover "english_tutorial_full"
        action Hide("scr_english101_tutorial")

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

init:
    $ timer_range = 0
    $ timer_jump = 0
    $ e_time= 0

init -5 python:

    style.english_bar_style = Style(style.default)
    style.english_bar_style.left_bar = Frame("gui/bar/left_var.png", 0, 0)
    style.english_bar_style.right_bar = Frame("gui/bar/right_var.png", 0, 0)
    style.english_bar_style.ymaximum = 20 




screen scr_english101_test1:
    text "{font=Audrey-Bold.otf}{size=-5}{color=#2b2b2b}Total score: [english_current_score]%{/color}{/size}{/font}" xpos 0.33 ypos 0.88
    text "{font=bradhitc.ttf}{color=#2b2b2b}[threeLetterWords]{/color}{/font}" xpos 0.185 ypos 0.25 xmaximum 0.2
    text "{font=bradhitc.ttf}{color=#2b2b2b}[percent3]%{/color}{/font}" xpos 0.35 ypos 0.213
    text "{font=bradhitc.ttf}{color=#2b2b2b}[fourLetterWords]{/color}{/font}" xpos 0.185 ypos 0.4343 xmaximum 0.2
    text "{font=bradhitc.ttf}{color=#2b2b2b}[percent4]%{/color}{/font}" xpos 0.35 ypos 0.3973
    text "{font=bradhitc.ttf}{color=#2b2b2b}[fiveLetterWords]{/color}{/font}" xpos 0.185 ypos 0.6160 xmaximum 0.2
    text "{font=bradhitc.ttf}{color=#2b2b2b}[percent5]%{/color}{/font}" xpos 0.35 ypos 0.579
    text "{font=bradhitc.ttf}{color=#2b2b2b}[sixLetterWords]{/color}{/font}" xpos 0.185 ypos 0.7990 xmaximum 0.2
    text "{font=bradhitc.ttf}{color=#2b2b2b}[percent6]%{/color}{/font}" xpos 0.35 ypos 0.762
    text "{font=bradhitc.ttf}{color=#2b2b2b}{size=+20}[wordToTest]{/size}{/color}{/font}" xpos 0.67 ypos 0.355
    timer 0.01 repeat True action If(e_time> 0, true=SetVariable('e_time', e_time- 0.01), false=[Hide('scr_english101_test1'), Jump(timer_jump)])
    bar value e_time range timer_range xalign 0.76 yalign 0.17 xmaximum 320 at alpha_dissolve:
        style "english_bar_style"

label english101_test1:
hide screen phone_screen
$ renpy.block_rollback()
show screen scr_english101_test1
$ myZorder = 1
$ englishTestScore = 0

$ e_time= 170
$ timer_range = 170
$ timer_jump = 'english101_test1_result'

$ letter_I = False
$ letter_G = False
$ letter_L = False
$ letter_T = False
$ letter_H = False
$ letter_S = False
$ english_position_list = [1040, 1134, 1228, 1322, 1416, 1510]
$ wordToTest = ""
$ threeLetterWords = ""
$ fourLetterWords = ""
$ fiveLetterWords = ""
$ sixLetterWords = ""
$ threeLetterPoints = 0
$ fourLetterPoints = 0
$ fiveLetterPoints = 0
$ sixLetterPoints = 0
$ percent3 = 0
$ percent4 = 0
$ percent5 = 0
$ percent6 = 0
$ english_cheat = False
$ english_cheat_done = False
$ cheatingNow = False
$ english_cheat_array = ["sit","lit","hit","his","git","its","this","slit","silt","sigh","shit","list","hits","gits","gist","hilt","gilt","hilts","sight","light","lights","slight"]
$ english_cheat_counter = 5
if englishCheatBoost == 1:
    $ english_cheat_counter = 7
elif englishCheatBoost == 2:
    $ english_cheat_counter = 9
if englishCheatBoost == 3:
    $ english_cheat_counter = 11
$ english_current_score = 0
$ engVar = 90 - englishBoost
$ engVar2 = 70 - englishBoost


$ wordSit = False
$ wordLit = False
$ wordHit = False
$ wordHis = False
$ wordGit = False
$ wordIts = False

$ wordThis = False
$ wordSlit = False
$ wordSilt = False
$ wordSigh = False
$ wordShit = False
$ wordList = False
$ wordHits = False
$ wordGits = False
$ wordGist = False
$ wordHilt = False
$ wordGilt = False

$ wordSight = False
$ wordLight = False
$ wordHilts = False

$ wordSlight = False
$ wordLights = False

show english_test_board zorder myZorder:
    size (config.screen_width, config.screen_height)
label english101_test1_loop:
$ ui.imagebutton("english_quiz_main_text", "english_quiz_main_text", clicked=ui.returns("NULL"), xpos=990, ypos=120)
if not letter_I:
    $ ui.imagebutton("letter_i", "letter_i_hover", clicked=ui.returns("I"), xpos=english_position_list[0], ypos=514)
elif True:
    $ ui.imagebutton("letter_blank", "letter_blank", clicked=ui.returns(""), xpos=english_position_list[0], ypos=514)
if not letter_G:
    $ ui.imagebutton("letter_g", "letter_g_hover", clicked=ui.returns("G"), xpos=english_position_list[1], ypos=514)
elif True:
    $ ui.imagebutton("letter_blank", "letter_blank", clicked=ui.returns(""), xpos=english_position_list[1], ypos=514)
if not letter_L:
    $ ui.imagebutton("letter_l", "letter_l_hover", clicked=ui.returns("L"), xpos=english_position_list[2], ypos=514)
elif True:
    $ ui.imagebutton("letter_blank", "letter_blank", clicked=ui.returns(""), xpos=english_position_list[2], ypos=514)
if not letter_T:
    $ ui.imagebutton("letter_t", "letter_t_hover", clicked=ui.returns("T"), xpos=english_position_list[3], ypos=514)
elif True:
    $ ui.imagebutton("letter_blank", "letter_blank", clicked=ui.returns(""), xpos=english_position_list[3], ypos=514)
if not letter_H:
    $ ui.imagebutton("letter_h", "letter_h_hover", clicked=ui.returns("H"), xpos=english_position_list[4], ypos=514)
elif True:
    $ ui.imagebutton("letter_blank", "letter_blank", clicked=ui.returns(""), xpos=english_position_list[4], ypos=514)
if not letter_S:
    $ ui.imagebutton("letter_s", "letter_s_hover", clicked=ui.returns("S"), xpos=english_position_list[5], ypos=514)
elif True:
    $ ui.imagebutton("letter_blank", "letter_blank", clicked=ui.returns(""), xpos=english_position_list[5], ypos=514)

$ ui.imagebutton("math_cheat", "math_cheat_hover", clicked=ui.returns("OK"), xpos=1165, ypos=605)
$ ui.imagebutton("math_cheat", "math_cheat_hover", clicked=ui.returns("SHUFFLE"), xpos=1325, ypos=735)
$ ui.imagebutton("math_cheat", "math_cheat_hover", clicked=ui.returns("QUIT"), xpos=1385, ypos=865)
$ ui.imagebutton("classes_view_tutorial_idle", "classes_view_tutorial_hover", clicked=ui.returns("TUTORIAL"), xpos=1045, ypos=885)

if not english_cheat:
    $ ui.imagebutton("math_cheat", "math_cheat_hover", clicked=ui.returns("CHEAT"), xpos=1030, ypos=735)
elif True:
    $ ui.imagebutton("math_cheated", "math_cheated", clicked=ui.returns("CHEAT"), xpos=1030, ypos=735)
$ result = ui.interact()


if result == "I":
    $ letter_I = True
    $ wordToTest += "i"
if result == "G":
    $ letter_G = True
    $ wordToTest += "g"
if result == "L":
    $ letter_L = True
    $ wordToTest += "l"
if result == "T":
    $ letter_T = True
    $ wordToTest += "t"
if result == "H":
    $ letter_H = True
    $ wordToTest += "h"
if result == "S":
    $ letter_S = True
    $ wordToTest += "s"
if result == "OK":
    jump english101_test1_ok
if result == "SHUFFLE":
    jump english101_test1_shuffle
if result == "CHEAT":
    if not english_cheat:
        $ wordToTest = ""
        $ ui.imagebutton("english_quiz_main_text", "english_quiz_main_text", clicked=ui.returns("NULL"), xpos=990, ypos=120)
        $ ui.imagebutton("classes_cheat_test_bg", "classes_cheat_test_bg", clicked=ui.returns("NULL"), xpos=960, ypos=350)
        $ ui.imagebutton("math_cheat", "math_cheat_hover", clicked=ui.returns("yes"), xpos=1070, ypos=500)
        $ ui.imagebutton("math_cheat", "math_cheat_hover", clicked=ui.returns("no"), xpos=1325, ypos=500)
        $ ui.imagebutton("classes_view_tutorial_idle", "classes_view_tutorial_hover", clicked=ui.returns("NULL"), xpos=1045, ypos=885)
        $ result = ui.interact()
        if result == "yes":
            $ renpy.block_rollback()
            $ english_cheat = True
            jump english101_test1_cheat
        elif True:
            jump english101_test1_ok
    elif True:
        jump english101_test1_ok

if result == "QUIT":
    $ ui.imagebutton("english_quiz_main_text", "english_quiz_main_text", clicked=ui.returns("NULL"), xpos=990, ypos=120)
    $ ui.imagebutton("classes_quit_test_bg", "classes_quit_test_bg", clicked=ui.returns("NULL"), xpos=960, ypos=350)
    $ ui.imagebutton("math_cheat", "math_cheat_hover", clicked=ui.returns("yes"), xpos=1070, ypos=500)
    $ ui.imagebutton("math_cheat", "math_cheat_hover", clicked=ui.returns("no"), xpos=1325, ypos=500)
    $ ui.imagebutton("classes_view_tutorial_idle", "classes_view_tutorial_hover", clicked=ui.returns("NULL"), xpos=1045, ypos=885)
    if english_cheat:
        $ ui.imagebutton("math_cheated", "math_cheated", clicked=ui.returns("NULL"), xpos=1030, ypos=735)
    $ result = ui.interact()
    if result == "yes":
        jump english101_test1_result
    elif True:
        jump english101_test1_ok
if result == "TUTORIAL":
    show screen scr_english101_tutorial

jump english101_test1_loop

label english101_test1_cheat:
$ wordToTest = english_cheat_array[renpy.random.randint(0, 21)]
$ cheatingNow = True
$ scoredPoint = False
label english101_test1_ok:
if wordToTest == "sit" and not wordSit:
    $ englishTestScore += 1
    $ threeLetterPoints += 1
    $ wordSit = True
    $ threeLetterWords += "sit "
    $ scoredPoint = True
elif wordToTest == "lit" and not wordLit:
    $ englishTestScore += 1
    $ threeLetterPoints += 1
    $ wordLit = True
    $ threeLetterWords += "lit "
    $ scoredPoint = True
elif wordToTest == "hit" and not wordHit:
    $ englishTestScore += 1
    $ threeLetterPoints += 1
    $ wordHit = True
    $ threeLetterWords += "hit "
    $ scoredPoint = True
elif wordToTest == "his" and not wordHis:
    $ englishTestScore += 1
    $ threeLetterPoints += 1
    $ wordHis = True
    $ threeLetterWords += "his "
    $ scoredPoint = True
elif wordToTest == "git" and not wordGit:
    $ englishTestScore += 1
    $ threeLetterPoints += 1
    $ wordGit = True
    $ threeLetterWords += "git "
    $ scoredPoint = True
elif wordToTest == "its" and not wordIts:
    $ englishTestScore += 1
    $ threeLetterPoints += 1
    $ wordIts = True
    $ threeLetterWords += "its "
    $ scoredPoint = True
elif wordToTest == "this" and not wordThis:
    $ englishTestScore += 1
    $ fourLetterPoints += 1
    $ wordThis = True
    $ fourLetterWords += "this "
    $ scoredPoint = True
elif wordToTest == "slit" and not wordSlit:
    $ englishTestScore += 1
    $ fourLetterPoints += 1
    $ wordSlit = True
    $ fourLetterWords += "slit "
    $ scoredPoint = True
elif wordToTest == "silt" and not wordSilt:
    $ englishTestScore += 1
    $ fourLetterPoints += 1
    $ wordSilt = True
    $ fourLetterWords += "silt "
    $ scoredPoint = True
elif wordToTest == "sigh" and not wordSigh:
    $ englishTestScore += 1
    $ fourLetterPoints += 1
    $ wordSigh = True
    $ fourLetterWords += "sigh "
    $ scoredPoint = True
elif wordToTest == "shit" and not wordShit:
    $ englishTestScore += 1
    $ fourLetterPoints += 1
    $ wordShit = True
    $ fourLetterWords += "shit "
    $ scoredPoint = True
elif wordToTest == "list" and not wordList:
    $ englishTestScore += 1
    $ fourLetterPoints += 1
    $ wordList = True
    $ fourLetterWords += "list "
    $ scoredPoint = True
elif wordToTest == "hits" and not wordHits:
    $ englishTestScore += 1
    $ fourLetterPoints += 1
    $ wordHits = True
    $ fourLetterWords += "hits "
    $ scoredPoint = True
elif wordToTest == "gits" and not wordGits:
    $ englishTestScore += 1
    $ fourLetterPoints += 1
    $ wordGits = True
    $ fourLetterWords += "gits "
    $ scoredPoint = True
elif wordToTest == "gist" and not wordGist:
    $ englishTestScore += 1
    $ fourLetterPoints += 1
    $ wordGist = True
    $ fourLetterWords += "gist "
    $ scoredPoint = True
elif wordToTest == "hilt" and not wordHilt:
    $ englishTestScore += 1
    $ fourLetterPoints += 1
    $ wordHilt = True
    $ fourLetterWords += "hilt "
    $ scoredPoint = True
elif wordToTest == "gilt" and not wordGilt:
    $ englishTestScore += 1
    $ fourLetterPoints += 1
    $ wordGilt = True
    $ fourLetterWords += "gilt "
    $ scoredPoint = True
elif wordToTest == "sight" and not wordSight:
    $ englishTestScore += 1
    $ fiveLetterPoints += 1
    $ wordSight = True
    $ fiveLetterWords += "sight "
    $ scoredPoint = True
elif wordToTest == "light" and not wordLight:
    $ englishTestScore += 1
    $ fiveLetterPoints += 1
    $ wordLight = True
    $ fiveLetterWords += "light "
    $ scoredPoint = True
elif wordToTest == "hilts" and not wordHilts:
    $ englishTestScore += 1
    $ fiveLetterPoints += 1
    $ wordHilts = True
    $ fiveLetterWords += "hilts "
    $ scoredPoint = True
elif wordToTest == "slight" and not wordSlight:
    $ englishTestScore += 1
    $ sixLetterPoints += 1
    $ wordSlight = True
    $ sixLetterWords += "slight "
    $ scoredPoint = True
elif wordToTest == "lights" and not wordLights:
    $ englishTestScore += 1
    $ sixLetterPoints += 1
    $ wordLights = True
    $ sixLetterWords += "lights "
    $ scoredPoint = True
if cheatingNow and scoredPoint:
    $ english_cheat_counter-=1
    $ cheatingNow = False
$ scoredPoint = False
if english_cheat_counter == 0:
    $ english_cheat_done = True
if english_cheat and not english_cheat_done and englishTestScore < 22:
    jump english101_test1_cheat

$ percent3 = int(100 * threeLetterPoints / 6)
$ percent4 = int(100 * fourLetterPoints / 11)
$ percent5 = int(100 * fiveLetterPoints / 3)
$ percent6 = int(100 * sixLetterPoints / 2)

$ wordToTest = ""
$ letter_I = False
$ letter_G = False
$ letter_L = False
$ letter_T = False
$ letter_H = False
$ letter_S = False
show screen scr_english101_test1
$ english_current_score = int(100 * englishTestScore / 22) + bonusPercentageEnglish
if english_current_score >= engVar:
    $ english_current_score = "{color=#0e8c02}"+str(english_current_score)+"{/color}"
elif english_current_score >= engVar2:
    $ english_current_score = "{color=#0f55aa}"+str(english_current_score)+"{/color}"
if englishTestScore == 22:
    $ maxedEnglish += 1
    jump english101_test1_result
jump english101_test1_loop

label english101_test1_shuffle:
$ renpy.random.shuffle(english_position_list)
jump english101_test1_loop

label english101_test1_result:
$ renpy.block_rollback()
hide screen scr_english101_test1
scene desk_bg with dissolve
$ englishResult = int(100 * englishTestScore / 22)

if englishTestScore == 22:
    $ ui.imagebutton("classes_perfect", "classes_perfect", clicked=ui.returns("NULL"), xalign=0.49, yalign=0.14)
elif englishResult + bonusPercentageEnglish >= 90- englishBoost:
    $ ui.imagebutton("classes_great", "classes_great", clicked=ui.returns("NULL"), xalign=0.49, yalign=0.14)
elif englishResult + bonusPercentageEnglish >= 70 - englishBoost:
    $ ui.imagebutton("classes_good", "classes_good", clicked=ui.returns("NULL"), xalign=0.49, yalign=0.14)
elif True:
    $ ui.imagebutton("classes_fail", "classes_fail", clicked=ui.returns("NULL"), xalign=0.49, yalign=0.14)

show text "{font=bradhitc.ttf}{color=#2b2b2b}{size=+50}[englishResult] + {color=#26ef4b}[bonusPercentageEnglish]{/color}%{/size}{/color}{/font}":
    yalign 0.4
if englishResult + bonusPercentageEnglish >= 90- englishBoost:
    $ passedEnglish += 1
    if not persistent.ep1_card4:
        $ chat_new_rewards = True
        $ persistent.rew_riona_unlocked += 1
        $ persistent.ep1_card4 = True
        $ calcRenders()
        $ ui.imagebutton("classes_special_render", "classes_special_render", clicked=ui.returns("NULL"), xalign=0.48, yalign=0.6)
    if nerdNotes:
        $ ui.imagebutton("classes_nerd_notes", "classes_nerd_notes", clicked=ui.returns("NULL"), xalign=0.48, yalign=0.8)
        $ mny(1)
    if english_cheat:
        $ ui.imagebutton("classes_with_cheating", "classes_with_cheating", clicked=ui.returns("NULL"), xalign=0.48, yalign=0.7)
        $ dk(1)
    elif True:
        $ ui.imagebutton("classes_without_cheating", "classes_without_cheating", clicked=ui.returns("NULL"), xalign=0.48, yalign=0.7)
        $ dk(-1)
elif englishResult + bonusPercentageEnglish >= 70 - englishBoost:
    $ passedEnglish += 1
    if nerdNotes:
        $ ui.imagebutton("classes_nerd_notes", "classes_nerd_notes", clicked=ui.returns("NULL"), xalign=0.48, yalign=0.8)
        $ mny(1)
    if english_cheat:
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
    $ failedEnglish += 1

if steamAchievements and englishResult + bonusPercentageEnglish >= 70 - englishBoost and not config.console and not config.developer:
    if english_cheat:
        $ achievement.grant("NOTSOHONORABLESTUDENT")
        init:
            $ achievement.register("NOTSOHONORABLESTUDENT")
    elif True:
        $ achievement.grant("HONORABLESTUDENT")
        init:
            $ achievement.register("HONORABLESTUDENT")
    $ achievement.Sync()
$ bonusPercentageEnglish = 0
$ renpy.pause()
hide text
if tutorials:
    scene black with fade
    show text "{i}You can buy items to lower the limit for getting lewd renders and to increase your cheating skill. By studying you can make the English tests easier to pass.{/i}"
    $ renpy.pause()
show screen phone_screen
jump ep1_after_english_test
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
