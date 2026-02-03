


screen scr_english101_test4:
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
    timer 0.01 repeat True action If(e_time > 0, true=SetVariable('e_time', e_time - 0.01), false=[Hide('scr_english101_test4'), Jump(timer_jump)])
    bar value e_time range timer_range xalign 0.76 yalign 0.17 xmaximum 320 at alpha_dissolve:
        style "english_bar_style"

label english101_test4:
hide screen scr_stats
$ renpy.block_rollback()
show screen scr_english101_test4
$ myZorder = 1
$ englishTestScore = 0

$ e_time = 170
$ timer_range = 170
$ timer_jump = 'english101_test4_result'

$ letter_N = False
$ letter_O = False
$ letter_S2 = False
$ letter_S = False
$ letter_E = False
$ letter_L = False
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
$ english_cheat_array = ["sos","son","one","leo","eon","sons","sole","ones","nose","noel","loss","lose","lone","less","lens","eons","loses","noses","noels","soles","lesson"]
$ english_cheat_counter = 5
if englishCheatBoost == 1:
    $ english_cheat_counter = 7
elif englishCheatBoost == 2:
    $ english_cheat_counter = 8
elif englishCheatBoost == 3:
    $ english_cheat_counter = 10

$ english_current_score = "{color=#2b2b2b}0{/color}"
$ engVar = 90 - englishBoost
$ engVar2 = 50 - englishBoost


$ wordSOS = False
$ wordSON = False
$ wordONE = False
$ wordLEO = False
$ wordEON = False

$ wordSONS = False
$ wordSOLE = False
$ wordONES = False
$ wordNOSE = False
$ wordNOEL = False
$ wordLOSS = False
$ wordLOSE = False
$ wordLONE = False
$ wordLESS = False
$ wordLENS = False
$ wordEONS = False

$ wordLOSES = False
$ wordNOELS = False
$ wordNOSES = False
$ wordSOLES = False

$ wordLESSON = False

show english_test_board zorder myZorder:
    size (config.screen_width, config.screen_height)
label english101_test4_loop:
$ ui.imagebutton("english_quiz_main_text", "english_quiz_main_text", clicked=ui.returns("NULL"), xpos=990, ypos=120)
if not letter_N:
    $ ui.imagebutton("letter_n", "letter_n_hover", clicked=ui.returns("N"), xpos=english_position_list[1], ypos=514)
elif True:
    $ ui.imagebutton("letter_blank", "letter_blank", clicked=ui.returns(""), xpos=english_position_list[1], ypos=514)
if not letter_O:
    $ ui.imagebutton("letter_o", "letter_o_hover", clicked=ui.returns("O"), xpos=english_position_list[0], ypos=514)
elif True:
    $ ui.imagebutton("letter_blank", "letter_blank", clicked=ui.returns(""), xpos=english_position_list[0], ypos=514)
if not letter_S2:
    $ ui.imagebutton("letter_s", "letter_s_hover", clicked=ui.returns("S2"), xpos=english_position_list[2], ypos=514)
elif True:
    $ ui.imagebutton("letter_blank", "letter_blank", clicked=ui.returns(""), xpos=english_position_list[2], ypos=514)
if not letter_S:
    $ ui.imagebutton("letter_s", "letter_s_hover", clicked=ui.returns("S"), xpos=english_position_list[3], ypos=514)
elif True:
    $ ui.imagebutton("letter_blank", "letter_blank", clicked=ui.returns(""), xpos=english_position_list[3], ypos=514)
if not letter_E:
    $ ui.imagebutton("letter_e", "letter_e_hover", clicked=ui.returns("E"), xpos=english_position_list[4], ypos=514)
elif True:
    $ ui.imagebutton("letter_blank", "letter_blank", clicked=ui.returns(""), xpos=english_position_list[4], ypos=514)
if not letter_L:
    $ ui.imagebutton("letter_l", "letter_l_hover", clicked=ui.returns("L"), xpos=english_position_list[5], ypos=514)
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


if result == "L":
    $ letter_L = True
    $ wordToTest += "l"
if result == "E":
    $ letter_E = True
    $ wordToTest += "e"
if result == "S":
    $ letter_S = True
    $ wordToTest += "s"
if result == "S2":
    $ letter_S2 = True
    $ wordToTest += "s"
if result == "N":
    $ letter_N = True
    $ wordToTest += "n"
if result == "O":
    $ letter_O = True
    $ wordToTest += "o"
if result == "OK":
    jump english101_test4_ok
if result == "SHUFFLE":
    jump english101_test4_shuffle
if result == "CHEAT":
    if not english_cheat:
        $ ui.imagebutton("english_quiz_main_text", "english_quiz_main_text", clicked=ui.returns("NULL"), xpos=990, ypos=120)
        $ ui.imagebutton("classes_cheat_test_bg", "classes_cheat_test_bg", clicked=ui.returns("NULL"), xpos=960, ypos=350)
        $ ui.imagebutton("math_cheat", "math_cheat_hover", clicked=ui.returns("yes"), xpos=1070, ypos=500)
        $ ui.imagebutton("math_cheat", "math_cheat_hover", clicked=ui.returns("no"), xpos=1325, ypos=500)
        $ ui.imagebutton("classes_view_tutorial_idle", "classes_view_tutorial_hover", clicked=ui.returns("NULL"), xpos=1045, ypos=885)
        $ result = ui.interact()
        if result == "yes":
            $ renpy.block_rollback()
            $ english_cheat = True
            jump english101_test4_cheat
        elif True:
            jump english101_test4_ok
    elif True:
        jump english101_test4_ok
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
        jump english101_test4_result
    elif True:
        jump english101_test4_ok
if result == "TUTORIAL":
    show screen scr_english101_tutorial

jump english101_test4_loop

label english101_test4_cheat:
$ wordToTest = english_cheat_array[renpy.random.randint(0, 20)]
$ cheatingNow = True
$ scoredPoint = False

label english101_test4_ok:
$ scoredPoint = True
if wordToTest == "sos" and not wordSOS:
    $ englishTestScore += 1
    $ threeLetterPoints += 1
    $ wordSOS = True
    $ threeLetterWords += "sos "
elif wordToTest == "son" and not wordSON:
    $ englishTestScore += 1
    $ threeLetterPoints += 1
    $ wordSON = True
    $ threeLetterWords += "son "
elif wordToTest == "one" and not wordONE:
    $ englishTestScore += 1
    $ threeLetterPoints += 1
    $ wordONE = True
    $ threeLetterWords += "one "
elif wordToTest == "leo" and not wordLEO:
    $ englishTestScore += 1
    $ threeLetterPoints += 1
    $ wordLEO = True
    $ threeLetterWords += "leo "
elif wordToTest == "eon" and not wordEON:
    $ englishTestScore += 1
    $ threeLetterPoints += 1
    $ wordEON = True
    $ threeLetterWords += "eon "
elif wordToTest == "sons" and not wordSONS:
    $ englishTestScore += 1
    $ fourLetterPoints += 1
    $ wordSONS = True
    $ fourLetterWords += "sons "
elif wordToTest == "sole" and not wordSOLE:
    $ englishTestScore += 1
    $ fourLetterPoints += 1
    $ wordSOLE = True
    $ fourLetterWords += "sole "
elif wordToTest == "ones" and not wordONES:
    $ englishTestScore += 1
    $ fourLetterPoints += 1
    $ wordONES = True
    $ fourLetterWords += "ones "
elif wordToTest == "nose" and not wordNOSE:
    $ englishTestScore += 1
    $ fourLetterPoints += 1
    $ wordNOSE = True
    $ fourLetterWords += "nose "
elif wordToTest == "noel" and not wordNOEL:
    $ englishTestScore += 1
    $ fourLetterPoints += 1
    $ wordNOEL = True
    $ fourLetterWords += "noel "
elif wordToTest == "loss" and not wordLOSS:
    $ englishTestScore += 1
    $ fourLetterPoints += 1
    $ wordLOSS = True
    $ fourLetterWords += "loss "
elif wordToTest == "lose" and not wordLOSE:
    $ englishTestScore += 1
    $ fourLetterPoints += 1
    $ wordLOSE = True
    $ fourLetterWords += "lose "
elif wordToTest == "lone" and not wordLONE:
    $ englishTestScore += 1
    $ fourLetterPoints += 1
    $ wordLONE = True
    $ fourLetterWords += "lone "
elif wordToTest == "less" and not wordLESS:
    $ englishTestScore += 1
    $ fourLetterPoints += 1
    $ wordLESS = True
    $ fourLetterWords += "less "
elif wordToTest == "lens" and not wordLENS:
    $ englishTestScore += 1
    $ fourLetterPoints += 1
    $ wordLENS = True
    $ fourLetterWords += "lens "
elif wordToTest == "eons" and not wordEONS:
    $ englishTestScore += 1
    $ fourLetterPoints += 1
    $ wordEONS = True
    $ fourLetterWords += "eons "
elif wordToTest == "loses" and not wordLOSES:
    $ englishTestScore += 1
    $ fiveLetterPoints += 1
    $ wordLOSES = True
    $ fiveLetterWords += "loses "
elif wordToTest == "noses" and not wordNOSES:
    $ englishTestScore += 1
    $ fiveLetterPoints += 1
    $ wordNOSES = True
    $ fiveLetterWords += "noses "
elif wordToTest == "noels" and not wordNOELS:
    $ englishTestScore += 1
    $ fiveLetterPoints += 1
    $ wordNOELS = True
    $ fiveLetterWords += "noels "
elif wordToTest == "soles" and not wordSOLES:
    $ englishTestScore += 1
    $ fiveLetterPoints += 1
    $ wordSOLES = True
    $ fiveLetterWords += "soles "
elif wordToTest == "lesson" and not wordLESSON:
    $ englishTestScore += 1
    $ sixLetterPoints += 1
    $ wordLESSON = True
    $ sixLetterWords += "lesson "
elif True:
    $ scoredPoint = False

if cheatingNow and scoredPoint:
    $ english_cheat_counter-=1
    $ cheatingNow = False
$ scoredPoint = False

if english_cheat_counter == 0:
    $ english_cheat_done = True
if english_cheat and not english_cheat_done and englishTestScore < 21:
    jump english101_test4_cheat

$ percent3 = int(100 * threeLetterPoints / 5)
$ percent4 = int(100 * fourLetterPoints / 11)
$ percent5 = int(100 * fiveLetterPoints / 4)
$ percent6 = int(100 * sixLetterPoints / 1)

$ wordToTest = ""
$ letter_L = False
$ letter_E = False
$ letter_S = False
$ letter_S2 = False
$ letter_O = False
$ letter_N = False
show screen scr_english101_test4
$ english_current_score = int(100 * englishTestScore / 21) + bonusPercentageEnglish
if english_current_score >= engVar:
    $ english_current_score = "{color=#00a647}"+str(english_current_score)+"{/color}"
elif english_current_score >= engVar2:
    $ english_current_score = "{color=#00a0e6}"+str(english_current_score)+"{/color}"
elif True:
    $ english_current_score = "{color=#2b2b2b}"+str(english_current_score)+"{/color}"
if englishTestScore == 21:
    $ maxedEnglish += 1
    jump english101_test4_result
jump english101_test4_loop

label english101_test4_shuffle:
$ renpy.random.shuffle(english_position_list)
jump english101_test4_loop

label english101_test4_result:
$ renpy.block_rollback()
hide screen scr_english101_test4
scene desk_bg with dissolve
$ englishResult = int(100 * englishTestScore / 21)


if englishTestScore == 21:
    $ ui.imagebutton("classes_perfect", "classes_perfect", clicked=ui.returns("NULL"), xalign=0.49, yalign=0.14)
elif englishResult + bonusPercentageEnglish >= 90- englishBoost:
    $ ui.imagebutton("classes_great", "classes_great", clicked=ui.returns("NULL"), xalign=0.49, yalign=0.14)
elif englishResult + bonusPercentageEnglish >= 70 - englishBoost:
    $ ui.imagebutton("classes_good", "classes_good", clicked=ui.returns("NULL"), xalign=0.49, yalign=0.14)
elif True:
    $ ui.imagebutton("classes_fail", "classes_fail", clicked=ui.returns("NULL"), xalign=0.49, yalign=0.14)

show text "{font=bradhitc.ttf}{color=#2b2b2b}{size=+50}[englishResult] + {color=#26ef4b}[bonusPercentageEnglish]{/color}%{/size}{/color}{/font}":
    yalign 0.4
stop music fadeout 3
if englishResult + bonusPercentageEnglish >= 90- englishBoost:
    $ passedEnglish += 1
    if not persistent.ep4_card2:
        $ chat_new_rewards = True
        $ persistent.rew_camila_unlocked += 1
        $ persistent.ep4_card2 = True
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
if steamAchievements and not config.console and not config.developer and maxedEnglish == 4:
    $ achievement.grant("JUMBLEMASTER")
    init:
        $ achievement.register("JUMBLEMASTER")
$ achievement.Sync()

$ bonusPercentageEnglish = 0
$ renpy.pause()
hide text
show screen phone_screen
jump ep4_after_english_test
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
