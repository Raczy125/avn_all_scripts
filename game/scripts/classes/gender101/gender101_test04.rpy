label gender101_test4:
if minigames:
    $ tmpMenu = quick_menu
    $ quick_menu = 0
    hide screen phone_screen
    $ genderPoints = 0
    $ gender_cheat = False
    $ gender_cheats_left = 1 + genderCheatBoost
play music "music/ep1/radio_martini.mp3"
scene gender101_fem04_listen with dissolve
mc "Go... Talk to me."
scene gender101_fem04_talk with dissolve
stu "What?"
scene gender101_fem04_listen with dissolve
if affinity == "DIK":
    mc "I know how these things go by now. Tell me about you and your fucking problems!"
elif True:
    mc "I know how these things go by now. Tell me about you and your problems!"
stu "..."
mc "What's your name?"
scene gender101_fem04_talk with dissolve
stu "Karen."
scene gender101_fem04_listen with dissolve
mc "..."
mc "That's it?"
scene gender101_fem04_talk with dissolve
stu "That's my given name."
scene gender101_fem04_listen with dissolve
mc "Ok, what else do you got?"
scene gender101_fem04_talk with dissolve
stu "Ah... I don't know what to say."
stu "I thought we were going to discuss feminism..."
stu "My full name is Karen Rebecca Johnson. I'm 19 years and 2 months old. I signed up for this class to get extra credits."
stu "I...have a social anxiety disorder and I don't handle stress or yelling well. I hate conflicts. You seem upset..."
stu "You're not going to yell at me, are you?"
scene gender101_fem04_listen with dissolve
mc "No! Of course not. What else?"
scene gender101_fem04_talk with dissolve
stu "Ah... I like classical music and arts. I don't like hip hop, it's too noisy for me. My ears are very sensitive, you see."
stu "When I was 7 years old, I got my first hearing aid. Kids made fun of me for it."
scene gender101_fem04_listen with dissolve
mc "That sucks... I know what it's like to be bullied, too."
scene gender101_fem04_talk with dissolve
stu "Are you sure you aren't upset?"
scene gender101_fem04_listen with dissolve
mc "I'm fine!"
scene gender101_fem04_talk2 with dissolve
stu "Aaaahhh! I want to become a librarian when I graduate. Libraries don't have a high noise level. I heard that it was somewhere around 44 dB."
stu "My mom wanted me to become a veterinarian like her mom, but I'm allergic to dogs and they bark so loud. I can't stand them and I'm afraid of cows."
stu "Currently, I take Gender Studies, History and Latin."
stu "I'm at the end of my second year here, so I'm almost done now."
$ renpy.block_rollback()
scene gender101_fem04_maya with dissolve
my "You can't keep avoiding me like this. Please, you have to listen!"
scene gender101_fem04_maya1 with dissolve
if minigames:
    mc "No. Right now, I'm listening to..."
    show screen scr_gender101_cheats_left
    menu:
        "Susan Karen Johansen" if True:
            $ guessedName = "Susan"
            mc "...Susan Karen Johansen."
        "Karen Rebecca Johnson" if True:
            $ guessedName = "Karen"
            $ genderPoints += 1
            mc "...Karen Rebecca Johnson."
        "Hearing aid girl" if True:
            $ dk(1)
            $ guessedName = "hearing aid girl"
            mc "...hearing aid girl, over here!"
        "Karen Rebecca Johansen" if True:
            $ guessedName = "Rebecca"
            mc "...Karen Rebecca Johansen."
        "{color=#ffffff}Cheat{/color}" if gender_cheats_left > 0:
            $ gender_cheats_left -= 1
            $ gender_cheat = True
            $ genderPoints += 1
            mc "...this lovely girl."
            $ guessedName = "you"
elif True:
    mc "No. Right now I'm listening to Karen Rebecca Johnson."
if minigames:
    hide screen scr_gender101_cheats_left
    $ renpy.block_rollback()
    mc "She's so nice and she doesn't like..."
    show screen scr_gender101_cheats_left
    menu:
        "Classical music or dogs" if True:
            mc "...classical music or dogs."
        "Conflicts or dogs" if True:
            $ genderPoints += 1
            mc "...conflicts or dogs."
        "Hearing aids or librarians" if True:
            mc "...hearing aids or librarians!"
        "Latin or dogs" if True:
            mc "...Latin or dogs."
        "{color=#ffffff}Cheat{/color}" if gender_cheats_left > 0:
            $ gender_cheats_left -= 1
            $ gender_cheat = True
            $ genderPoints += 1
            mc "...you know what, that's personal. Right, [guessedName]?"
    hide screen scr_gender101_cheats_left
    $ renpy.block_rollback()
elif True:
    mc "She's so nice and she doesn't like conflicts or dogs."
if minigames:
    mc "And she got her first hearing aid when she was..."
    show screen scr_gender101_cheats_left
    menu:
        "2 years" if True:
            mc "...2 years young."
        "7 months" if True:
            mc "...7 months. Such a poor baby!"
        "5 years" if True:
            mc "...5 years young."
        "7 years" if True:
            $ genderPoints += 1
            mc "...7 years young."
        "{color=#ffffff}Cheat{/color}" if gender_cheats_left > 0:
            $ gender_cheats_left -= 1
            $ gender_cheat = True
            $ genderPoints += 1
            mc "...way too young. Right, [guessedName]?"
    hide screen scr_gender101_cheats_left
    $ renpy.block_rollback()
elif True:
    mc "And she got her first hearing aid when she was 7 years young."
scene gender101_fem04_mayab with dissolve
my "Is this your plan? To avoid me?"
scene gender101_fem04_maya2 with dissolve
mc "You hurt me, Maya... I'm tired of all the lies and secrets."
stu "Um...I..."
scene gender101_fem04_maya1
mc "Not now, [guessedName]."
if minigames:
    mc "We can talk about your fear of..."
    show screen scr_gender101_cheats_left
    menu:
        "Cows" if True:
            $ genderPoints += 1
            mc "...cows later!"
        "Dogs" if True:
            mc "...dogs later!"
        "Hip hop" if True:
            mc "...hip hop later!"
        "Librarians" if True:
            mc "...librarians later!"
        "{color=#ffffff}Cheat{/color}" if gender_cheats_left > 0:
            $ gender_cheats_left -= 1
            $ gender_cheat = True
            $ genderPoints += 1
            mc "...the horrible things in this world, later!"
    hide screen scr_gender101_cheats_left
    $ renpy.block_rollback()
elif True:
    mc "We can talk about your fear of cows later!"
if minigames:
    mc "And also, about how you want to be a..."
    show screen scr_gender101_cheats_left
    menu:
        "Librarian" if True:
            $ genderPoints += 1
            mc "...librarian when you graduate."
        "Veterinarian" if True:
            mc "...veterinarian when you graduate."
        "Hip hop artist" if True:
            mc "...hip hop artist when you graduate."
        "Dog" if True:
            mc "...dog when you graduate."
        "{color=#ffffff}Cheat{/color}" if gender_cheats_left > 0:
            $ gender_cheats_left -= 1
            $ gender_cheat = True
            $ genderPoints += 1
            mc "...person that matters when you graduate."
    hide screen scr_gender101_cheats_left
    $ renpy.block_rollback()
elif True:
    mc "And also, about how you want to be a librarian when you graduate."
if minigames:
    mc "Even though someone in your life wanted you to be a veterinarian..."
    mc "...and that person was..."
    show screen scr_gender101_cheats_left
    menu:
        "Your mom" if True:
            $ genderPoints += 1
            mc "...your mom."
        "Your grandmother" if True:
            mc "...your grandmother."
        "Your dad" if True:
            mc "...your dad."
        "Your dog" if True:
            mc "...your dog."
        "{color=#ffffff}Cheat{/color}" if gender_cheats_left > 0:
            $ gender_cheats_left -= 1
            $ gender_cheat = True
            $ genderPoints += 1
            mc "...someone you love."
    hide screen scr_gender101_cheats_left
    $ renpy.block_rollback()
elif True:
    mc "Even though your mom wanted you to be a veterinarian."
scene gender101_fem04_maya4 with dissolve
my "Is this what you talk about during class?"
scene gender101_fem04_maya2 with dissolve
mc "Maybe."
scene gender101_fem04_mayab with dissolve
my "I'm sorry I hurt you! I never meant to do that!"
if ep3_acceptedJade:
    scene gender101_fem04_maya5a with dissolve
    ja "(Hm?)"
    scene gender101_fem04_mayab with dissolve
my "Can you please just give me one final chance? Please?"
my "I...don't want this to end like this."
scene gender101_fem04_maya5b with dissolve
mc "..."
scene gender101_fem04_maya5
mc "Don't you go anywhere, [guessedName]."
if not minigames:
    stop music fadeout 3
    mc "You're 19 years and 2 months old, you'll survive some discomfort."
    jump ep4_after_gender_test4_label

mc "You're..."
show screen scr_gender101_cheats_left
menu:
    "18 years old" if True:
        mc "...18 years old, you'll survive some discomfort."
    "19 years old" if True:
        mc "...19 years old, you'll survive some discomfort."
    "18 years and 2 months" if True:
        mc "...18 years and 2 months old, you'll survive some discomfort."
    "19 years and 2 months" if True:
        $ genderPoints += 1
        mc "...19 years and 2 months old, you'll survive some discomfort."
    "{color=#ffffff}Cheat{/color}" if gender_cheats_left > 0:
        $ gender_cheats_left -= 1
        $ gender_cheat = True
        $ genderPoints += 1
        mc "...a grown woman, you'll survive some discomfort."
hide screen scr_gender101_cheats_left
$ renpy.block_rollback()
mc "You've been at B&R for..."
show screen scr_gender101_cheats_left
menu:
    "Six months" if True:
        mc "...six months now, you know what college is like."
    "Three years" if True:
        mc "...three years now, you know what college is like."
    "Two years" if True:
        $ genderPoints += 1
        mc "...two years now, you know what college is like."
    "A year" if True:
        mc "...a year now, you know what college is like."
    "{color=#ffffff}Cheat{/color}" if gender_cheats_left > 0:
        $ gender_cheats_left -= 1
        $ gender_cheat = True
        $ genderPoints += 1
        mc "...a long time now, you know what college is like."
hide screen scr_gender101_cheats_left
$ renpy.block_rollback()
mc "And we're not screaming at you. Our noise level is way below that of a library, which is..."
show screen scr_gender101_cheats_left
menu:
    "34 dB" if True:
        mc "34 dB."
    "40 dB" if True:
        mc "40 dB."
    "44 dB" if True:
        $ genderPoints += 1
        mc "44 dB."
    "50 dB" if True:
        mc "50 dB."
    "{color=#ffffff}Cheat{/color}" if gender_cheats_left > 0:
        $ gender_cheats_left -= 1
        $ gender_cheat = True
        $ genderPoints += 1
        mc "...a reasonable noise level for you."
hide screen scr_gender101_cheats_left
$ renpy.block_rollback()
mc "This will soon be over and you can go back to studying..."
show screen scr_gender101_cheats_left
menu:
    "History and Latin" if True:
        $ genderPoints += 1
        mc "History and Latin."
    "English and Math" if True:
        mc "English and Math."
    "Latin and classical music" if True:
        mc "Latin and classical music."
    "History and Science" if True:
        mc "History and Science."
    "{color=#ffffff}Cheat{/color}" if gender_cheats_left > 0:
        $ gender_cheats_left -= 1
        $ gender_cheat = True
        $ genderPoints += 1
        mc "...the courses you have enrolled in."
hide screen scr_gender101_cheats_left
$ renpy.block_rollback()
$ renpy.block_rollback()
$ genderResult = int(100 * genderPoints / 10)
$ genderVar = 90 - genderBoost
$ genderVar2 = 50 - genderBoost
if genderPoints == 10:
    $ maxedGender += 1
stop music fadeout 3
if genderResult + bonusPercentageGender >= 90 - genderBoost:
    scene gender101_class4_result1b with dissolve
    $ passedGender += 1
    if not persistent.ep4_card19:
        $ chat_new_rewards = True
        $ persistent.rew_mixed_unlocked += 1
        $ persistent.ep4_card19 = True
        $ calcRenders()
    if nerdNotes:
        $ mny(1)
        if gender_cheat:
            show text "{color=#000000}{size=+50}You scored [genderResult] + {color=#26ef4b}[bonusPercentageGender]{/color}%!\nYou unlocked a special render!\nYou got +{color=#fe9416}{size=-1}{font=collegiate.ttf}DIK{/font}{/size}{/color} from cheating.\nYou got {color=#36ca2b}${/color} from taking notes for the nerds.{/size}{/color}"
            $ dk(1)
        elif True:
            show text "{color=#000000}{size=+50}You scored [genderResult] + {color=#26ef4b}[bonusPercentageGender]{/color}%!\nYou unlocked a special render!\nYou got -{color=#fe9416}{size=-1}{font=collegiate.ttf}DIK{/font}{/size}{/color} from passing without cheating.\nYou got {color=#36ca2b}${/color} from taking notes for the nerds.{/size}{/color}"
            $ dk(-1)
    elif True:
        if gender_cheat:
            show text "{color=#000000}{size=+50}You scored [genderResult] + {color=#26ef4b}[bonusPercentageGender]{/color}%!\nYou unlocked a special render!\nYou got +{color=#fe9416}{size=-1}{font=collegiate.ttf}DIK{/font}{/size}{/color} from cheating.{/size}{/color}"
            $ dk(1)
        elif True:
            show text "{color=#000000}{size=+50}You scored [genderResult] + {color=#26ef4b}[bonusPercentageGender]{/color}%!\nYou unlocked a special render!\nYou got -{color=#fe9416}{size=-1}{font=collegiate.ttf}DIK{/font}{/size}{/color} from passing without cheating.{/size}{/color}"
            $ dk(-1)
    $ renpy.pause()
elif genderResult + bonusPercentageGender >= 70 - genderBoost:
    scene gender101_class4_result1b with dissolve
    $ passedGender += 1
    if nerdNotes:
        $ mny(1)
        if gender_cheat:
            show text "{color=#000000}{size=+50}You scored [genderResult] + {color=#26ef4b}[bonusPercentageGender]{/color}%!\nYou got +{color=#fe9416}{size=-1}{font=collegiate.ttf}DIK{/font}{/size}{/color} from cheating.\nYou got {color=#36ca2b}${/color} from taking notes for the nerds.{/size}{/color}"
            $ dk(1)
        elif True:
            show text "{color=#000000}{size=+50}You scored [genderResult] + {color=#26ef4b}[bonusPercentageGender]{/color}%!\nYou got -{color=#fe9416}{size=-1}{font=collegiate.ttf}DIK{/font}{/size}{/color} from passing without cheating.\nYou got {color=#36ca2b}${/color} from taking notes for the nerds.{/size}{/color}"
            $ dk(-1)
    elif True:
        if gender_cheat:
            show text "{color=#000000}{size=+50}You scored [genderResult] + {color=#26ef4b}[bonusPercentageGender]{/color}%!\nYou got +{color=#fe9416}{size=-1}{font=collegiate.ttf}DIK{/font}{/size}{/color} from cheating.{/size}{/color}"
            $ dk(1)
        elif True:
            show text "{color=#000000}{size=+50}You scored [genderResult] + {color=#26ef4b}[bonusPercentageGender]{/color}%!\nYou got -{color=#fe9416}{size=-1}{font=collegiate.ttf}DIK{/font}{/size}{/color} from passing without cheating.{/size}{/color}"
            $ dk(-1)
    $ renpy.pause()
elif True:
    if steamAchievements and not config.console and not config.developer:
        $ achievement.grant("FISFORFAILURE")
        init:
            $ achievement.register("FISFORFAILURE")
        $ achievement.Sync()
    scene gender101_class4_result1b with dissolve
    $ failedGender += 1
    show text "{color=#000000}{size=+50}You scored [genderResult] + {color=#26ef4b}[bonusPercentageGender]{/color}%!\nYou failed the test!{/size}{/color}"
    $ renpy.pause()
scene gender101_class4_result1 with dissolve
stu "..."
if steamAchievements and genderResult + bonusPercentageGender >= 70 - genderBoost and not config.console and not config.developer:
    if gender_cheat:
        $ achievement.grant("NOTSOHONORABLESTUDENT")
        init:
            $ achievement.register("NOTSOHONORABLESTUDENT")
    elif True:
        $ achievement.grant("HONORABLESTUDENT")
        init:
            $ achievement.register("HONORABLESTUDENT")
    $ achievement.Sync()
if steamAchievements and not config.console and not config.developer and maxedGender == 3:
    $ achievement.grant("FEMINIST")
    init:
        $ achievement.register("FEMINIST")
$ achievement.Sync()
$ bonusPercentageGender = 0
hide screen gender_score_bg_scr
show screen phone_screen
if minigames:
    $ quick_menu = tmpMenu
jump ep4_after_gender_test4_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
