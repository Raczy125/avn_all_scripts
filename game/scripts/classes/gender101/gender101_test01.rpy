screen scr_gender101_cheats_left:
    modal False
    imagebutton at show_hide_dissolve:
        idle "bg_toprightmsg_short"
        xalign 0.9825
        yalign -0.01
        action NullAction()
    text "{color=#ffffff}Cheats left: [gender_cheats_left]{/color}" at show_hide_dissolve:
        xpos 0.855
        ypos 0.015

label gender101_test1:
$ tmpMenu = quick_menu
$ quick_menu = 0
hide screen phone_screen
$ genderPoints = 0
$ gender_cheat = False
$ gender_cheats_left = 1 + genderCheatBoost
play music "music/ep1/radio_martini.mp3"
if tutorials:
    scene gender101_fem01_listen with dissolve
    "{i}In the Gender Studies class, you are tested in various ways in discussions.{/i}"
    "{i}Listen to what your study partner says and answer her questions when prompted.{/i}"
    "{i}Let's begin!{/i}"
scene gender101_fem01_talk with dissolve
stu "So, my name's Danielle, but they call me Dany for short. I hate when people call me Daniel! Come on; I don't look like a boy!"
stu "I have a pet rabbit named Franz; he's 2 years old and all fluffy and brown."
stu "Did you ever wonder how many times a female can orgasm during sex? I hear the world record is close to 13 times."
stu "I could be very wrong, though; I didn't even look it up."
stu "Speaking of orgasms, do you think I should wear glasses? I prefer to wear lenses because glasses make my cheeks look fat."
$ renpy.block_rollback()
stu "Are you listening?"
scene gender101_fem01_listen with dissolve
mc "Of course, I am."
scene gender101_fem01_talk with dissolve
stu "Then I guess you remember what my name is?"
scene gender101_fem01_listen with dissolve
show screen scr_gender101_cheats_left
menu:
    "Dany" if True:
        mc "Your name is Dany."
    "Daniel" if True:
        mc "Your name is Daniel."
    "Danielle" if True:
        mc "Your name is Danielle."
        $ genderPoints += 1
    "Franz" if True:
        mc "Your name is Franz."
    "{color=#ffffff}Cheat{/color}" if gender_cheats_left > 0:
        $ gender_cheats_left -= 1
        $ gender_cheat = True
        $ genderPoints += 1
        mc "I just love your hair!"
        scene gender101_fem01_talk3 with dissolve
        stu "Really? That's so sweet of you!"
        stu "Oh, where was I?"
hide screen scr_gender101_cheats_left
$ renpy.block_rollback()
scene gender101_fem01_talk with dissolve
stu "What about my pet rabbit? What color and age is he?"
scene gender101_fem01_listen with dissolve
show screen scr_gender101_cheats_left
menu:
    "2 months old, brown." if True:
        mc "Your pet rabbit is 2 months old and is brown and fluffy."
    "2 years old, brown." if True:
        mc "Your pet rabbit is 2 years old and is brown and fluffy."
        $ genderPoints += 1
    "2 months old, white." if True:
        mc "Your pet rabbit is 2 months old and is white and fluffy."
    "2 years old, white." if True:
        mc "Your pet rabbit is 2 years old and is white and fluffy."
    "{color=#ffffff}Cheat{/color}" if gender_cheats_left > 0:
        $ gender_cheats_left -= 1
        $ gender_cheat = True
        $ genderPoints += 1
        mc "I really like your attitude!"
        scene gender101_fem01_talk3 with dissolve
        stu "Thanks, such a nice compliment..."
        stu "Oh, where was I?"
hide screen scr_gender101_cheats_left
$ renpy.block_rollback()
scene gender101_fem01_talk with dissolve
stu "My parents really wanted me to go to a fancier college like W&W, but I told them that a major in gender studies and the female body at B&R is even better."
stu "My best friend Linda is so sweet; she's a hefty girl, 20 years old, and weighs 240 pounds. Can you believe that!?"
stu "She just eats burgers and ice cream every day. I'm all for eating, but, damn girl! Show some restraint! Am I right?"
stu "I'm kind of moody today. I haven't had my period in two months, my friend Suzy thinks I'm pregnant."
stu "I should probably get it checked, but a pregnancy test costs like $12! I could be buying hair dye for that money!"
stu "I mean, why pay money for something that you piss on. Am I right!?"
$ renpy.block_rollback()
stu "You're like a super-good listener, right?"
scene gender101_fem01_listen with dissolve
mc "I've been known to lend an ear to those who need to vent, yes."
scene gender101_fem01_talk3 with dissolve

stu "That's so sweet. Just as sweet as my pet rabbit. Do you remember his name?"
scene gender101_fem01_listen with dissolve
show screen scr_gender101_cheats_left
menu:
    "Dany" if True:
        mc "It was Dany, right?"
    "Daniel" if True:
        mc "It was Daniel, right?"
    "Frank" if True:
        mc "It was Frank, right?"
    "Franz" if True:
        mc "It was Franz, right?"
        $ genderPoints += 1
    "{color=#ffffff}Cheat{/color}" if gender_cheats_left > 0:
        $ gender_cheats_left -= 1
        $ gender_cheat = True
        $ genderPoints += 1
        mc "I really love rabbits! Aren't they the best?"
        scene gender101_fem01_talk3 with dissolve
        stu "Oh! Totally!"
        stu "Oh, where was I?"
hide screen scr_gender101_cheats_left
$ renpy.block_rollback()
scene gender101_fem01_talk2 with dissolve
stu "Are you seriously asking {i}me{/i} that? You're the one who's supposed to know."
stu "I bet you don't even remember my mom's name."
scene gender101_fem01_listen with dissolve
show screen scr_gender101_cheats_left
menu:
    "Danielle" if True:
        mc "Sure, I do. Her name is Danielle."
    "Linda" if True:
        mc "Sure, I do. Her name is Linda."
    "Suzy" if True:
        mc "Sure, I do. Her name is Suzy."
    "You never told me" if True:
        mc "I can't remember something you never told me."
        $ genderPoints += 1
    "{color=#ffffff}Cheat{/color}" if gender_cheats_left > 0:
        $ gender_cheats_left -= 1
        $ gender_cheat = True
        $ genderPoints += 1
        mc "I feel that names are just used to put labels on people. I don't want to use them."
        scene gender101_fem01_talk3 with dissolve
        stu "That's really insightful!"
        stu "Oh, where was I?"
hide screen scr_gender101_cheats_left
$ renpy.block_rollback()
scene gender101_fem01_talk with dissolve
stu "Whatever, do you remember how much a pregnancy test costs?"
stu "Because I just told you that. It would be very rude of you to forget."
scene gender101_fem01_listen with dissolve
show screen scr_gender101_cheats_left
menu:
    "$10" if True:
        mc "It costs the same as hair dye, $10."
    "$11" if True:
        mc "It costs the same as hair dye, $11."
    "$12" if True:
        mc "It costs the same as hair dye, $12."
        $ genderPoints += 1
    "$22" if True:
        mc "It costs the same as hair dye, $22."
    "{color=#ffffff}Cheat{/color}" if gender_cheats_left > 0:
        $ gender_cheats_left -= 1
        $ gender_cheat = True
        $ genderPoints += 1
        mc "I don't like talking about money. It's so unfair that men tend to make more than women..."
        scene gender101_fem01_talk3 with dissolve
        stu "I think that too!"
        stu "Oh, where was I?"
hide screen scr_gender101_cheats_left
$ renpy.block_rollback()
scene gender101_fem01_talk with dissolve
stu "Yeah, I'm not gonna buy that test. If I'm pregnant, I'll make my boyfriend Jamie pay for the kid."
stu "Do you remember if it was glasses or lenses that made my cheeks look fat?"
scene gender101_fem01_listen with dissolve
show screen scr_gender101_cheats_left
menu:
    "Lenses" if True:
        mc "You think that it's your lenses that make you look fat."
        scene gender101_fem01_talk with dissolve
    "Glasses" if True:
        mc "You think that it's your glasses that make you look fat."
        $ genderPoints += 1
        scene gender101_fem01_talk with dissolve
    "Both" if True:
        mc "Both lenses and glasses make you look fat."
        $ renpy.block_rollback()
        scene gender101_fem01_talk2 with dissolve
        stu "RUDE!"
    "{color=#ffffff}Cheat{/color}" if gender_cheats_left > 0:
        $ gender_cheats_left -= 1
        $ gender_cheat = True
        $ genderPoints += 1
        mc "Fat? I think you look beautiful without glasses and probably equally beautiful with them."
        scene gender101_fem01_talk3 with dissolve
        stu "I didn't expect that to come from you."
        stu "Oh, where was I?"
hide screen scr_gender101_cheats_left
$ renpy.block_rollback()
stu "Speaking of fat people, what's my fat friend's name and how much does she weigh?"
scene gender101_fem01_listen with dissolve
show screen scr_gender101_cheats_left
menu:
    "Linda, 220 lbs" if True:
        mc "Your fat friend is named Linda and she weighs 220 lbs."
    "Linda, 240 lbs" if True:
        mc "Your fat friend is named Linda and she weighs 240 lbs."
        $ genderPoints += 1
    "Suzy, 220 lbs" if True:
        mc "Your fat friend is named Suzy and she weighs 220 lbs."
    "Suzy, 240 lbs" if True:
        mc "Your fat friend is named Suzy and she weighs 240 lbs."
    "{color=#ffffff}Cheat{/color}" if gender_cheats_left > 0:
        $ gender_cheats_left -= 1
        $ gender_cheat = True
        $ genderPoints += 1
        mc "You're probably a way better friend to her than she is to you, am I right?"
        scene gender101_fem01_talk3 with dissolve
        stu "Yes, totally!"
hide screen scr_gender101_cheats_left
$ renpy.block_rollback()
scene gender101_fem01_talk with dissolve
stu "That fat lump waddles when she walks. If she had a theme song, it would be tuba music."
stu "How long has it been since I had my period?"
scene gender101_fem01_listen with dissolve
show screen scr_gender101_cheats_left
menu:
    "1 week" if True:
        mc "1 week."
    "2 weeks" if True:
        mc "2 weeks."
    "1 month" if True:
        mc "1 month."
    "2 months" if True:
        $ genderPoints += 1
        mc "2 months."
    "{color=#ffffff}Cheat{/color}" if gender_cheats_left > 0:
        $ gender_cheats_left -= 1
        $ gender_cheat = True
        $ genderPoints += 1
        mc "You are so brave that you can talk about this openly with a stranger."
        mc "I admire you!"
        scene gender101_fem01_talk3 with dissolve
        stu "That's so nice to say!"
        stu "Oh, where was I?"
hide screen scr_gender101_cheats_left
$ renpy.block_rollback()
scene gender101_fem01_talk with dissolve
stu "If I have a kid, who will pay for it?"
scene gender101_fem01_listen with dissolve
show screen scr_gender101_cheats_left
menu:
    "Your boyfriend, Peter." if True:
        mc "Your boyfriend, Peter."
        scene gender101_fem01_talk with dissolve
    "Your boyfriend, Steve." if True:
        mc "Your boyfriend, Steve."
        scene gender101_fem01_talk with dissolve
    "Your boyfriend, Jamie." if True:
        mc "Your boyfriend, Jamie."
        scene gender101_fem01_talk with dissolve
        $ genderPoints += 1
    "Society" if True:
        mc "Society."
        $ renpy.block_rollback()
        scene gender101_fem01_talk2 with dissolve
        stu "RUDE!"
    "{color=#ffffff}Cheat{/color}" if gender_cheats_left > 0:
        $ gender_cheats_left -= 1
        $ gender_cheat = True
        $ genderPoints += 1
        mc "Probably some male who doesn't deserve his money, am I right?"
        scene gender101_fem01_talk3 with dissolve
        stu "Spot fucking on!"
        stu "Oh, where was I?"
hide screen scr_gender101_cheats_left
$ renpy.block_rollback()
stu "Do you remember the world record for female orgasms during sex that I totally just made up because I was too lazy to look it up?"
scene gender101_fem01_listen with dissolve
show screen scr_gender101_cheats_left
menu:
    "13" if True:
        $ genderPoints += 1
        mc "13."
    "20" if True:
        mc "20."
    "240" if True:
        mc "240."
    "12" if True:
        mc "12."
    "{color=#ffffff}Cheat{/color}" if gender_cheats_left > 0:
        $ gender_cheats_left -= 1
        $ gender_cheat = True
        $ genderPoints += 1
        mc "Come on, are you really quizzing me on that?"
        mc "You're a smart girl; you don't need to make things up."
        scene gender101_fem01_talk3 with dissolve
        stu "You're right. I am smarter than that."
hide screen scr_gender101_cheats_left
$ renpy.block_rollback()
$ genderResult = int(100 * genderPoints / 10)
$ genderVar = 90 - genderBoost
$ genderVar2 = 50 - genderBoost
if genderPoints == 10:
    $ maxedGender += 1
stop music fadeout 3
if genderResult + bonusPercentageGender >= 90 - genderBoost:
    scene gender101_class1_result1 with dissolve
    $ passedGender += 1
    if not persistent.ep1_card14:
        $ chat_new_rewards = True
        $ persistent.rew_riona_unlocked += 1
        $ persistent.ep1_card14 = True
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
    stu "Wow, you're different from other men. You actually listen to me."
elif genderResult + bonusPercentageGender >= 70 - genderBoost:
    scene gender101_class1_result1 with dissolve
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
    stu "You're a pretty decent listener."
elif True:
    if steamAchievements and not config.console and not config.developer:
        $ achievement.grant("FISFORFAILURE")
        init:
            $ achievement.register("FISFORFAILURE")
        $ achievement.Sync()
    scene gender101_class1_result2 with dissolve
    $ failedGender += 1
    show text "{color=#000000}{size=+50}You scored [genderResult] + {color=#26ef4b}[bonusPercentageGender]{/color}%!\nYou failed the test!{/size}{/color}"
    stu "You suck at listening, you know that?"

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
"{i}You can buy items to lower the limit for getting lewd renders and to increase your cheating skill. By studying, you can make the Gender Studies tests easier to pass.{/i}"
hide screen gender_score_bg_scr
show screen phone_screen
$ quick_menu = tmpMenu
jump ep1_after_gender_test1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
