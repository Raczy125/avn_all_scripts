


screen scr_english101_test3:
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
    timer 0.01 repeat True action If(e_time > 0, true=SetVariable('e_time', e_time - 0.01), false=[Hide('scr_english101_test3'), Jump(timer_jump)])
    bar value e_time range timer_range xalign 0.76 yalign 0.17 xmaximum 320 at alpha_dissolve:
        style "english_bar_style"

label english101_test3:
hide screen scr_stats
$ renpy.block_rollback()
show screen scr_english101_test3
$ myZorder = 1
$ englishTestScore = 0

$ e_time = 170
$ timer_range = 170
$ timer_jump = 'english101_test3_result'

$ letter_A = False
$ letter_C = False
$ letter_T = False
$ letter_I = False
$ letter_N = False
$ letter_G = False
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
$ english_cheat_array = ["act","tin","gin","git","nag","tag","tic","nit","tan","cat","can","ant","gait","cant","tang","ting","inca","gnat","gain","anti","agin","giant","antic","actin","acing","acting"]
$ english_cheat_counter = 5
if englishCheatBoost == 1:
    $ english_cheat_counter = 9
elif englishCheatBoost == 2:
    $ english_cheat_counter = 10
elif englishCheatBoost == 3:
    $ english_cheat_counter = 12

$ english_current_score = "{color=#2b2b2b}0{/color}"
$ engVar = 90 - englishBoost
$ engVar2 = 50 - englishBoost


$ wordACT = False
$ wordTIN = False
$ wordGIN = False
$ wordGIT = False
$ wordNAG = False
$ wordTAG = False
$ wordTAN = False
$ wordCAT = False
$ wordCAN = False
$ wordANT = False
$ wordTIC = False
$ wordNIT = False

$ wordTANG = False
$ wordGAIT = False
$ wordCANT = False
$ wordTING = False
$ wordINCA = False
$ wordGNAT = False
$ wordGAIN = False
$ wordANTI = False
$ wordAGIN = False

$ wordGIANT = False
$ wordANTIC = False
$ wordACTIN = False
$ wordACING = False

$ wordACTING = False

show english_test_board zorder myZorder:
    size (config.screen_width, config.screen_height)
label english101_test3_loop:
$ ui.imagebutton("english_quiz_main_text", "english_quiz_main_text", clicked=ui.returns("NULL"), xpos=990, ypos=120)
if not letter_A:
    $ ui.imagebutton("letter_a", "letter_a_hover", clicked=ui.returns("A"), xpos=english_position_list[1], ypos=514)
elif True:
    $ ui.imagebutton("letter_blank", "letter_blank", clicked=ui.returns(""), xpos=english_position_list[1], ypos=514)
if not letter_C:
    $ ui.imagebutton("letter_c", "letter_c_hover", clicked=ui.returns("C"), xpos=english_position_list[0], ypos=514)
elif True:
    $ ui.imagebutton("letter_blank", "letter_blank", clicked=ui.returns(""), xpos=english_position_list[0], ypos=514)
if not letter_T:
    $ ui.imagebutton("letter_t", "letter_t_hover", clicked=ui.returns("T"), xpos=english_position_list[2], ypos=514)
elif True:
    $ ui.imagebutton("letter_blank", "letter_blank", clicked=ui.returns(""), xpos=english_position_list[2], ypos=514)
if not letter_I:
    $ ui.imagebutton("letter_i", "letter_i_hover", clicked=ui.returns("I"), xpos=english_position_list[3], ypos=514)
elif True:
    $ ui.imagebutton("letter_blank", "letter_blank", clicked=ui.returns(""), xpos=english_position_list[3], ypos=514)
if not letter_N:
    $ ui.imagebutton("letter_n", "letter_n_hover", clicked=ui.returns("N"), xpos=english_position_list[4], ypos=514)
elif True:
    $ ui.imagebutton("letter_blank", "letter_blank", clicked=ui.returns(""), xpos=english_position_list[4], ypos=514)
if not letter_G:
    $ ui.imagebutton("letter_g", "letter_g_hover", clicked=ui.returns("G"), xpos=english_position_list[5], ypos=514)
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

if result == "A":
    $ letter_A = True
    $ wordToTest += "a"
if result == "C":
    $ letter_C = True
    $ wordToTest += "c"
if result == "T":
    $ letter_T = True
    $ wordToTest += "t"
if result == "I":
    $ letter_I = True
    $ wordToTest += "i"
if result == "N":
    $ letter_N = True
    $ wordToTest += "n"
if result == "G":
    $ letter_G = True
    $ wordToTest += "g"
if result == "OK":
    jump english101_test3_ok
if result == "SHUFFLE":
    jump english101_test3_shuffle
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
            jump english101_test3_cheat
        elif True:
            jump english101_test3_ok
    elif True:
        jump english101_test3_ok
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
        jump english101_test3_result
    elif True:
        jump english101_test3_ok
if result == "TUTORIAL":
    show screen scr_english101_tutorial

jump english101_test3_loop

label english101_test3_cheat:
$ wordToTest = english_cheat_array[renpy.random.randint(0, 25)]
$ cheatingNow = True
$ scoredPoint = False

label english101_test3_ok:
$ scoredPoint = True
if wordToTest == "act" and not wordACT:
    $ englishTestScore += 1
    $ threeLetterPoints += 1
    $ wordACT = True
    $ threeLetterWords += "act "
elif wordToTest == "tin" and not wordTIN:
    $ englishTestScore += 1
    $ threeLetterPoints += 1
    $ wordTIN = True
    $ threeLetterWords += "tin "
elif wordToTest == "tic" and not wordTIC:
    $ englishTestScore += 1
    $ threeLetterPoints += 1
    $ wordTIC = True
    $ threeLetterWords += "tic "
elif wordToTest == "nit" and not wordNIT:
    $ englishTestScore += 1
    $ threeLetterPoints += 1
    $ wordNIT = True
    $ threeLetterWords += "nit "
elif wordToTest == "gin" and not wordGIN:
    $ englishTestScore += 1
    $ threeLetterPoints += 1
    $ wordGIN = True
    $ threeLetterWords += "gin "
elif wordToTest == "git" and not wordGIT:
    $ englishTestScore += 1
    $ threeLetterPoints += 1
    $ wordGIT = True
    $ threeLetterWords += "git "
elif wordToTest == "nag" and not wordNAG:
    $ englishTestScore += 1
    $ threeLetterPoints += 1
    $ wordNAG = True
    $ threeLetterWords += "nag "
elif wordToTest == "tag" and not wordTAG:
    $ englishTestScore += 1
    $ threeLetterPoints += 1
    $ wordTAG = True
    $ threeLetterWords += "tag "
elif wordToTest == "tan" and not wordTAN:
    $ englishTestScore += 1
    $ threeLetterPoints += 1
    $ wordTAN = True
    $ threeLetterWords += "tan "
elif wordToTest == "cat" and not wordCAT:
    $ englishTestScore += 1
    $ threeLetterPoints += 1
    $ wordCAT = True
    $ threeLetterWords += "cat "
elif wordToTest == "can" and not wordCAN:
    $ englishTestScore += 1
    $ threeLetterPoints += 1
    $ wordCAN = True
    $ threeLetterWords += "can "
elif wordToTest == "ant" and not wordANT:
    $ englishTestScore += 1
    $ threeLetterPoints += 1
    $ wordANT = True
    $ threeLetterWords += "ant "
elif wordToTest == "ting" and not wordTING:
    $ englishTestScore += 1
    $ fourLetterPoints += 1
    $ wordTING = True
    $ fourLetterWords += "ting "
elif wordToTest == "tang" and not wordTANG:
    $ englishTestScore += 1
    $ fourLetterPoints += 1
    $ wordTANG = True
    $ fourLetterWords += "tang "
elif wordToTest == "gait" and not wordGAIT:
    $ englishTestScore += 1
    $ fourLetterPoints += 1
    $ wordGAIT = True
    $ fourLetterWords += "gait "
elif wordToTest == "cant" and not wordCANT:
    $ englishTestScore += 1
    $ fourLetterPoints += 1
    $ wordCANT = True
    $ fourLetterWords += "cant "
elif wordToTest == "inca" and not wordINCA:
    $ englishTestScore += 1
    $ fourLetterPoints += 1
    $ wordINCA = True
    $ fourLetterWords += "inca "
elif wordToTest == "gnat" and not wordGNAT:
    $ englishTestScore += 1
    $ fourLetterPoints += 1
    $ wordGNAT = True
    $ fourLetterWords += "gnat "
elif wordToTest == "gain" and not wordGAIN:
    $ englishTestScore += 1
    $ fourLetterPoints += 1
    $ wordGAIN = True
    $ fourLetterWords += "gain "
elif wordToTest == "anti" and not wordANTI:
    $ englishTestScore += 1
    $ fourLetterPoints += 1
    $ wordANTI = True
    $ fourLetterWords += "anti "
elif wordToTest == "agin" and not wordAGIN:
    $ englishTestScore += 1
    $ fourLetterPoints += 1
    $ wordAGIN = True
    $ fourLetterWords += "agin "
elif wordToTest == "giant" and not wordGIANT:
    $ englishTestScore += 1
    $ fiveLetterPoints += 1
    $ wordGIANT = True
    $ fiveLetterWords += "giant "
elif wordToTest == "antic" and not wordANTIC:
    $ englishTestScore += 1
    $ fiveLetterPoints += 1
    $ wordANTIC = True
    $ fiveLetterWords += "antic "
elif wordToTest == "actin" and not wordACTIN:
    $ englishTestScore += 1
    $ fiveLetterPoints += 1
    $ wordACTIN = True
    $ fiveLetterWords += "actin "
elif wordToTest == "acing" and not wordACING:
    $ englishTestScore += 1
    $ fiveLetterPoints += 1
    $ wordACING = True
    $ fiveLetterWords += "acing "
elif wordToTest == "acting" and not wordACTING:
    $ englishTestScore += 1
    $ sixLetterPoints += 1
    $ wordACTING = True
    $ sixLetterWords += "acting "
elif True:
    $ scoredPoint = False

if cheatingNow and scoredPoint:
    $ english_cheat_counter-=1
    $ cheatingNow = False
$ scoredPoint = False

if english_cheat_counter == 0:
    $ english_cheat_done = True
if english_cheat and not english_cheat_done and englishTestScore < 26:
    jump english101_test3_cheat

$ percent3 = int(100 * threeLetterPoints / 12)
$ percent4 = int(100 * fourLetterPoints / 9)
$ percent5 = int(100 * fiveLetterPoints / 4)
$ percent6 = int(100 * sixLetterPoints / 1)

$ wordToTest = ""
$ letter_A = False
$ letter_C = False
$ letter_T = False
$ letter_I = False
$ letter_N = False
$ letter_G = False
show screen scr_english101_test3
$ english_current_score = int(100 * englishTestScore / 26) + bonusPercentageEnglish
if english_current_score >= engVar:
    $ english_current_score = "{color=#00a647}"+str(english_current_score)+"{/color}"
elif english_current_score >= engVar2:
    $ english_current_score = "{color=#00a0e6}"+str(english_current_score)+"{/color}"
elif True:
    $ english_current_score = "{color=#2b2b2b}"+str(english_current_score)+"{/color}"
if englishTestScore == 26:
    $ maxedEnglish += 1
    jump english101_test3_result
jump english101_test3_loop

label english101_test3_shuffle:
$ renpy.random.shuffle(english_position_list)
jump english101_test3_loop

label english101_test3_result:
$ renpy.block_rollback()
hide screen scr_english101_test3
scene desk_bg with dissolve
$ englishResult = int(100 * englishTestScore / 26)


if englishTestScore == 26:
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
    if not persistent.ep3_card9:
        $ chat_new_rewards = True
        $ persistent.rew_isa_unlocked += 1
        $ persistent.ep3_card9 = True
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
show screen phone_screen
jump ep3_after_english_test
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
