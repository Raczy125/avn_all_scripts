label gender101_test2:
$ tmpMenu = quick_menu
$ quick_menu = 0
hide screen phone_screen
$ genderPoints = 0
$ gender_cheat = False
$ gender_cheats_left = 1 + genderCheatBoost
play music "music/ep1/radio_martini.mp3"

scene gender101_fem02_listen with dissolve
$ renpy.block_rollback()
mc "Hey, there."
stu "..."
mc "So...um..."
if dtype>0:
    mc "What stuff do you like?"
elif True:
    mc "What's a topic that's close to your heart?"
scene gender101_fem02_talk with dissolve
stu "Why don't boys like me?"
mc "(Oh boy.)"
stu "I've only had five boyfriends in my life."
scene gender101_fem02_listen with dissolve
mc "Hey, five boyfriends! That's not bad."
scene gender101_fem02_talk with dissolve
stu "They were all imaginary."
scene gender101_fem02_listen with dissolve
mc "Oh..."
scene gender101_fem02_talk with dissolve
stu "I named them after my cats."
stu "Whiskers, Puss Puss, Mr. Paw, Pinkie and Lemons."
scene gender101_fem02_listen with dissolve
mc "Those are some weird names to have for imaginary boyfriends, don't you think?"
scene gender101_fem02_talk with dissolve
stu "You sound just like my mom! She's always nagging me."
stu "{i}Go clean your room, Linda!{/i}"
stu "{i}Remove the wrapping paper before you eat that burger, Linda!{/i}"
stu "I really love burgers..."
stu "...and chocolate milkshakes..."
stu "...and onion rings..."
stu "...but don't get me started on fries! I hate fries, they're too salty."
scene gender101_fem02_talk2 with dissolve
stu "I get so bloated from the salt, especially since I drink 3 bottles of orange soda every day."
stu "Excuse me; I meant diet orange soda."
stu "I try to watch my weight."
stu "My mom says if I watched my weight as much as I watch TV, I'd be a supermodel."
stu "That skinny cunt. No surprise that my dad left her when I was five years old."
$ renpy.block_rollback()
stu "Listen to me yap. Let me ask you some questions instead."
stu "What kind of milkshakes do I love?"
scene gender101_fem02_listen with dissolve
show screen scr_gender101_cheats_left
menu:
    "Chocolate" if True:
        $ genderPoints += 1
        mc "You love chocolate milkshakes."
    "Vanilla" if True:
        mc "You love vanilla milkshakes."
    "Orange" if True:
        mc "You love orange milkshakes."
    "Banana" if True:
        mc "You love banana milkshakes."
    "{color=#ffffff}Cheat{/color}" if gender_cheats_left > 0:
        $ gender_cheats_left -= 1
        $ gender_cheat = True
        $ genderPoints += 1
        mc "The bottomless one, am I right?"
        scene gender101_fem02_talk3 with dissolve
        stu "HAHA! Totally!"
        stu "Oh, where was I?"
hide screen scr_gender101_cheats_left
$ renpy.block_rollback()
scene gender101_fem02_talk2 with dissolve
stu "Uh-huh. And how many imaginary boyfriends have I had?"
scene gender101_fem02_listen with dissolve
show screen scr_gender101_cheats_left
menu:
    "2" if True:
        mc "2."
    "3" if True:
        mc "3."
    "4" if True:
        mc "4."
    "5" if True:
        $ genderPoints += 1
        mc "5."
    "{color=#ffffff}Cheat{/color}" if gender_cheats_left > 0:
        $ gender_cheats_left -= 1
        $ gender_cheat = True
        $ genderPoints += 1
        mc "You really deserve a real boyfriend, you know that right?"
        scene gender101_fem02_talk3 with dissolve
        stu "Thank you! You are so right!"
hide screen scr_gender101_cheats_left
$ renpy.block_rollback()
scene gender101_fem02_talk with dissolve
stu "Ok, that's enough about you. My turn to talk."
stu "I've never been to Paris, but I'd love to go there someday."
stu "There's something about French men that makes me moist."
stu "Speaking of being moist, did you hear that it might rain tonight?"
stu "I have three umbrellas, but I forgot them back home, so I'm probably going to get wet."
$ renpy.block_rollback()
stu "Hm..."
stu "How many bottles of soda do I drink every day?"
scene gender101_fem02_listen with dissolve
show screen scr_gender101_cheats_left
menu:
    "2" if True:
        mc "2."
    "3" if True:
        mc "3."
        $ genderPoints += 1
    "4" if True:
        mc "4."
    "5" if True:
        mc "5."
    "{color=#ffffff}Cheat{/color}" if gender_cheats_left > 0:
        $ gender_cheats_left -= 1
        $ gender_cheat = True
        $ genderPoints += 1
        mc "Enough to look pretty."
        scene gender101_fem02_talk3 with dissolve
        stu "Aw! That's so sweet of you!"
        stu "Oh, where was I?"
hide screen scr_gender101_cheats_left
$ renpy.block_rollback()
scene gender101_fem02_talk with dissolve
stu "What kind of sodas are they?"
scene gender101_fem02_listen with dissolve
show screen scr_gender101_cheats_left
menu:
    "Diet cherry" if True:
        mc "Diet cherry sodas."
    "Cherry" if True:
        mc "Cherry sodas."
    "Orange" if True:
        mc "Orange sodas."
    "Diet orange" if True:
        $ genderPoints += 1
        mc "Diet orange sodas."
    "{color=#ffffff}Cheat{/color}" if gender_cheats_left > 0:
        $ gender_cheats_left -= 1
        $ gender_cheat = True
        $ genderPoints += 1
        mc "The bubbly kind."
        scene gender101_fem02_talk3 with dissolve
        stu "HAHA! You're so funny!"
        stu "Oh, where was I?"
hide screen scr_gender101_cheats_left
$ renpy.block_rollback()
scene gender101_fem02_talk with dissolve
stu "Do you remember what I hate?"
scene gender101_fem02_listen with dissolve
show screen scr_gender101_cheats_left
menu:
    "Chocolate milkshakes" if True:
        mc "You hate chocolate milkshakes."
    "Onion rings" if True:
        mc "You hate onion rings."
    "Fries" if True:
        mc "You hate fries."
        $ genderPoints += 1
    "Burgers" if True:
        mc "You hate burgers."
    "{color=#ffffff}Cheat{/color}" if gender_cheats_left > 0:
        $ gender_cheats_left -= 1
        $ gender_cheat = True
        $ genderPoints += 1
        mc "Being lonely?"
        scene gender101_fem02_talk3 with dissolve
        stu "Yes! I do hate that."
        stu "Thank you for noticing."
hide screen scr_gender101_cheats_left
$ renpy.block_rollback()
scene gender101_fem02_talk with dissolve
stu "But I really love my cats..."
stu "Do you remember some of their names?"
scene gender101_fem02_listen with dissolve
show screen scr_gender101_cheats_left
menu:
    "Cake" if True:
        mc "I believe one of them was named Cake."
    "Mr. Pinkie" if True:
        mc "I believe one of them was named Mr. Pinkie."
    "Fluffy" if True:
        mc "I believe one of them was named Fluffy."
    "Whiskers" if True:
        $ genderPoints += 1
        mc "I believe one of them was named Whiskers."
    "{color=#ffffff}Cheat{/color}" if gender_cheats_left > 0:
        $ gender_cheats_left -= 1
        $ gender_cheat = True
        $ genderPoints += 1
        mc "I LOVE CATS, TOO!!"
        scene gender101_fem02_talk3 with dissolve
        stu "RIGHT!? They are so fluffy!"
        stu "Oh, where was I?"
hide screen scr_gender101_cheats_left
$ renpy.block_rollback()
scene gender101_fem02_talk with dissolve
stu "Go ahead, name another one of my cats."
scene gender101_fem02_listen with dissolve
show screen scr_gender101_cheats_left
menu:
    "Mr. Lemons" if True:
        mc "I believe another one was named Mr. Lemons."
    "Lemons" if True:
        mc "I believe another one was named Lemons."
        $ genderPoints += 1
    "Mr. Fluffy" if True:
        mc "I believe another one was named Mr. Fluffy."
    "Puss" if True:
        mc "I believe another one was named Puss."
    "{color=#ffffff}Cheat{/color}" if gender_cheats_left > 0:
        $ gender_cheats_left -= 1
        $ gender_cheat = True
        $ genderPoints += 1
        mc "It's a shame that cats can't talk."
        scene gender101_fem02_talk3 with dissolve
        stu "HAHA! Totally! They would say the funniest things like..."
        stu "Hey! Where is my food hoooman? HAHA!"
hide screen scr_gender101_cheats_left
$ renpy.block_rollback()
scene gender101_fem02_talk with dissolve
stu "How many umbrellas did I bring to college?"
scene gender101_fem02_listen with dissolve
show screen scr_gender101_cheats_left
menu:
    "0" if True:
        mc "You didn't bring any."
        $ genderPoints += 1
    "1" if True:
        mc "You brought one umbrella."
    "2" if True:
        mc "You brought two umbrellas."
    "3" if True:
        mc "You brought three umbrellas."
    "{color=#ffffff}Cheat{/color}" if gender_cheats_left > 0:
        $ gender_cheats_left -= 1
        $ gender_cheat = True
        $ genderPoints += 1
        mc "Is that a burger?"
        scene gender101_fem02_talk with dissolve
        stu "What!? Where?"
        stu "Oh, where was I?"
hide screen scr_gender101_cheats_left
$ renpy.block_rollback()
scene gender101_fem02_jade with dissolve
ja "(Hm...)"
scene gender101_fem02_talk with dissolve
stu "How old was I when my dad left my mom?"
scene gender101_fem02_listen with dissolve
show screen scr_gender101_cheats_left
menu:
    "3 years" if True:
        mc "3 years old."
    "3 months" if True:
        mc "3 months old."
    "5 years" if True:
        mc "5 years old."
        $ genderPoints += 1
    "5 months" if True:
        mc "5 months old."
    "{color=#ffffff}Cheat{/color}" if gender_cheats_left > 0:
        $ gender_cheats_left -= 1
        $ gender_cheat = True
        $ genderPoints += 1
        mc "Too young...how are you holding up?"
        scene gender101_fem02_talk3 with dissolve
        stu "I'm much better now, thank you!"
hide screen scr_gender101_cheats_left
$ renpy.block_rollback()
scene gender101_fem02_talk with dissolve
stu "Close your eyes!"
scene black
$ renpy.block_rollback()
stu "Are they closed?"
mc "Yeah, they are closed all right."
stu "What am I wearing?"
show screen scr_gender101_cheats_left
menu:
    "A white shirt with blue dots" if True:
        mc "A white shirt with blue dots."
    "A red shirt with white dots" if True:
        mc "A red shirt with white dots."
    "A blue shirt with white dots" if True:
        mc "A blue shirt with white dots."
        $ genderPoints += 1
    "A white shirt with red dots" if True:
        mc "A white shirt with red dots."
    "{color=#ffffff}Cheat{/color}" if gender_cheats_left > 0:
        $ gender_cheats_left -= 1
        $ gender_cheat = True
        $ genderPoints += 1
        mc "The color of beautiful."
        stu "You are so sweet!"
hide screen scr_gender101_cheats_left
$ renpy.block_rollback()
$ genderResult = int(100 * genderPoints / 10)
$ genderVar = 90 - genderBoost
$ genderVar2 = 50 - genderBoost
if genderPoints == 10:
    $ maxedGender += 1
stop music fadeout 3
if genderResult + bonusPercentageGender >= 90 - genderBoost:
    scene gender101_class2_result1 with dissolve
    $ passedGender += 1
    if not persistent.ep2_card13:
        $ chat_new_rewards = True
        $ persistent.rew_cathy_unlocked += 1
        $ persistent.ep2_card13 = True
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
    stu "You really listened to me...wanna be my boyfriend?"
    mc "Sorry...I'm in a...um...relationship already."
elif genderResult + bonusPercentageGender >= 70 - genderBoost:
    scene gender101_class2_result1 with dissolve
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
    stu "Hey...thanks for listening to me."
elif True:
    if steamAchievements and not config.console and not config.developer:
        $ achievement.grant("FISFORFAILURE")
        init:
            $ achievement.register("FISFORFAILURE")
        $ achievement.Sync()
    scene gender101_class2_result2 with dissolve
    $ failedGender += 1
    show text "{color=#000000}{size=+50}You scored [genderResult] + {color=#26ef4b}[bonusPercentageGender]{/color}%!\nYou failed the test!{/size}{/color}"
    stu "Why would anyone ever want to talk to you?"
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
$ bonusPercentageGender = 0
hide screen gender_score_bg_scr
show screen phone_screen
$ quick_menu = tmpMenu
jump ep2_after_gender_test2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
