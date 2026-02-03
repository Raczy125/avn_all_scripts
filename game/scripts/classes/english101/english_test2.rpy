


screen scr_english101_test2:
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
    timer 0.01 repeat True action If(e_time > 0, true=SetVariable('e_time', e_time - 0.01), false=[Hide('scr_english101_test2'), Jump(timer_jump)])
    bar value e_time range timer_range xalign 0.76 yalign 0.17 xmaximum 320 at alpha_dissolve:
        style "english_bar_style"

label english101_test2:
hide screen scr_stats
$ renpy.block_rollback()
show screen scr_english101_test2
$ myZorder = 1
$ englishTestScore = 0

$ e_time = 170
$ timer_range = 170
$ timer_jump = 'english101_test2_result'

$ letter_E = False
$ letter_E2 = False
$ letter_R = False
$ letter_P = False
$ letter_S = False
$ letter_H = False
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
$ english_cheat_array = ["she","see","rep","per","pee","her","seer","seep","reps","peer","hers","here","spree","sheer","sheep","peers","herpes","sphere"]
$ english_cheat_counter = 4
if englishCheatBoost == 1:
    $ english_cheat_counter = 6
elif englishCheatBoost == 2:
    $ english_cheat_counter = 7
if englishCheatBoost == 3:
    $ english_cheat_counter = 9
$ english_current_score = 0
$ engVar = 90 - englishBoost
$ engVar2 = 50 - englishBoost


$ wordShe = False
$ wordSee = False
$ wordRep = False
$ wordPer = False
$ wordPee = False
$ wordHer = False

$ wordSeer = False
$ wordSeep = False
$ wordReps = False
$ wordPeer = False
$ wordHers = False
$ wordHere = False

$ wordSpree = False
$ wordSheer = False
$ wordSheep = False
$ wordPeers = False

$ wordHerpes = False
$ wordSphere = False

show english_test_board zorder myZorder:
    size (config.screen_width, config.screen_height)
label english101_test2_loop:
    $ ui.imagebutton("english_quiz_main_text", "english_quiz_main_text", clicked=ui.returns("NULL"), xpos=990, ypos=120)
if not letter_E:
    $ ui.imagebutton("letter_e", "letter_e_hover", clicked=ui.returns("E"), xpos=english_position_list[0], ypos=514)
elif True:
    $ ui.imagebutton("letter_blank", "letter_blank", clicked=ui.returns(""), xpos=english_position_list[0], ypos=514)
if not letter_E2:
    $ ui.imagebutton("letter_e", "letter_e_hover", clicked=ui.returns("E2"), xpos=english_position_list[1], ypos=514)
elif True:
    $ ui.imagebutton("letter_blank", "letter_blank", clicked=ui.returns(""), xpos=english_position_list[1], ypos=514)
if not letter_R:
    $ ui.imagebutton("letter_r", "letter_r_hover", clicked=ui.returns("R"), xpos=english_position_list[2], ypos=514)
elif True:
    $ ui.imagebutton("letter_blank", "letter_blank", clicked=ui.returns(""), xpos=english_position_list[2], ypos=514)
if not letter_P:
    $ ui.imagebutton("letter_p", "letter_p_hover", clicked=ui.returns("P"), xpos=english_position_list[3], ypos=514)
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

if result == "E":
    $ letter_E = True
    $ wordToTest += "e"
if result == "E2":
    $ letter_E2 = True
    $ wordToTest += "e"
if result == "R":
    $ letter_R = True
    $ wordToTest += "r"
if result == "P":
    $ letter_P = True
    $ wordToTest += "p"
if result == "H":
    $ letter_H = True
    $ wordToTest += "h"
if result == "S":
    $ letter_S = True
    $ wordToTest += "s"
if result == "OK":
    jump english101_test2_ok
if result == "SHUFFLE":
    jump english101_test2_shuffle
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
            jump english101_test2_cheat
        elif True:
            jump english101_test2_ok
    elif True:
        jump english101_test2_ok
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
        jump english101_test2_result
    elif True:
        jump english101_test2_ok
if result == "TUTORIAL":
    show screen scr_english101_tutorial


jump english101_test2_loop

label english101_test2_cheat:
$ wordToTest = english_cheat_array[renpy.random.randint(0, 17)]
$ cheatingNow = True
$ scoredPoint = False
label english101_test2_ok:
if wordToTest == "she" and not wordShe:
    $ englishTestScore += 1
    $ threeLetterPoints += 1
    $ wordShe = True
    $ threeLetterWords += "she "
    $ scoredPoint = True
elif wordToTest == "see" and not wordSee:
    $ englishTestScore += 1
    $ threeLetterPoints += 1
    $ wordSee = True
    $ threeLetterWords += "see "
    $ scoredPoint = True
elif wordToTest == "rep" and not wordRep:
    $ englishTestScore += 1
    $ threeLetterPoints += 1
    $ wordRep = True
    $ threeLetterWords += "rep "
    $ scoredPoint = True
elif wordToTest == "per" and not wordPer:
    $ englishTestScore += 1
    $ threeLetterPoints += 1
    $ wordPer = True
    $ threeLetterWords += "per "
    $ scoredPoint = True
elif wordToTest == "pee" and not wordPee:
    $ englishTestScore += 1
    $ threeLetterPoints += 1
    $ wordPee = True
    $ threeLetterWords += "pee "
    $ scoredPoint = True
elif wordToTest == "her" and not wordHer:
    $ englishTestScore += 1
    $ threeLetterPoints += 1
    $ wordHer = True
    $ threeLetterWords += "her "
    $ scoredPoint = True
elif wordToTest == "seer" and not wordSeer:
    $ englishTestScore += 1
    $ fourLetterPoints += 1
    $ wordSeer = True
    $ fourLetterWords += "seer "
    $ scoredPoint = True
elif wordToTest == "seep" and not wordSeep:
    $ englishTestScore += 1
    $ fourLetterPoints += 1
    $ wordSeep = True
    $ fourLetterWords += "seep "
    $ scoredPoint = True
elif wordToTest == "reps" and not wordReps:
    $ englishTestScore += 1
    $ fourLetterPoints += 1
    $ wordReps = True
    $ fourLetterWords += "reps "
    $ scoredPoint = True
elif wordToTest == "peer" and not wordPeer:
    $ englishTestScore += 1
    $ fourLetterPoints += 1
    $ wordPeer = True
    $ fourLetterWords += "peer "
    $ scoredPoint = True
elif wordToTest == "hers" and not wordHers:
    $ englishTestScore += 1
    $ fourLetterPoints += 1
    $ wordHers = True
    $ fourLetterWords += "hers "
    $ scoredPoint = True
elif wordToTest == "here" and not wordHere:
    $ englishTestScore += 1
    $ fourLetterPoints += 1
    $ wordHere = True
    $ fourLetterWords += "here "
    $ scoredPoint = True
elif wordToTest == "spree" and not wordSpree:
    $ englishTestScore += 1
    $ fiveLetterPoints += 1
    $ wordSpree = True
    $ fiveLetterWords += "spree "
    $ scoredPoint = True
elif wordToTest == "sheer" and not wordSheer:
    $ englishTestScore += 1
    $ fiveLetterPoints += 1
    $ wordSheer = True
    $ fiveLetterWords += "sheer "
    $ scoredPoint = True
elif wordToTest == "sheep" and not wordSheep:
    $ englishTestScore += 1
    $ fiveLetterPoints += 1
    $ wordSheep = True
    $ fiveLetterWords += "sheep "
    $ scoredPoint = True
elif wordToTest == "peers" and not wordPeers:
    $ englishTestScore += 1
    $ fiveLetterPoints += 1
    $ wordPeers = True
    $ fiveLetterWords += "peers "
    $ scoredPoint = True
elif wordToTest == "herpes" and not wordHerpes:
    $ englishTestScore += 1
    $ sixLetterPoints += 1
    $ wordHerpes = True
    $ sixLetterWords += "herpes "
    $ scoredPoint = True
elif wordToTest == "sphere" and not wordSphere:
    $ englishTestScore += 1
    $ sixLetterPoints += 1
    $ wordSphere = True
    $ sixLetterWords += "sphere "
    $ scoredPoint = True
if cheatingNow and scoredPoint:
    $ english_cheat_counter-=1
    $ cheatingNow = False
$ scoredPoint = False
if english_cheat_counter == 0:
    $ english_cheat_done = True
if english_cheat and not english_cheat_done and englishTestScore < 18:
    jump english101_test2_cheat

$ percent3 = int(100 * threeLetterPoints / 6)
$ percent4 = int(100 * fourLetterPoints / 6)
$ percent5 = int(100 * fiveLetterPoints / 4)
$ percent6 = int(100 * sixLetterPoints / 2)

$ wordToTest = ""
$ letter_S = False
$ letter_P = False
$ letter_E = False
$ letter_E2 = False
$ letter_R = False
$ letter_H = False
show screen scr_english101_test2
$ english_current_score = int(100 * englishTestScore / 18) + bonusPercentageEnglish
if english_current_score >= engVar:
    $ english_current_score = "{color=#0e8c02}"+str(english_current_score)+"{/color}"
elif english_current_score >= engVar2:
    $ english_current_score = "{color=#0f55aa}"+str(english_current_score)+"{/color}"
if englishTestScore == 18:
    $ maxedEnglish += 1
    jump english101_test2_result
jump english101_test2_loop

label english101_test2_shuffle:
$ renpy.random.shuffle(english_position_list)
jump english101_test2_loop

label english101_test2_result:
$ renpy.block_rollback()
hide screen scr_english101_test2
scene desk_bg with dissolve
$ englishResult = int(100 * englishTestScore / 18)


if englishTestScore == 18:
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
    if not persistent.ep2_card5:
        $ chat_new_rewards = True
        $ persistent.rew_cathy_unlocked += 1
        $ persistent.ep2_card5 = True
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
jump ep2_after_english_test
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
