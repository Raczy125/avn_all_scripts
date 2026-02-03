label startUpdate3:
jump header_ep3_label
label previousEp3Label:

if brawler_difficulty == 0 and minigames:
    $ brawler_question = True
    scene black
    show text "Brawler has changed drastically since last time.\nYou may want to restart the game, but it's your choice.\nYou can still continue the game if you want to."
    $ renpy.pause()
    show text "{color=#ffffff}Do you want to play in easy, normal or hard mode?\nHard mode will put a premium on reaction time.{/color}"
    $ renpy.pause()
    menu:
        "{size=-2}Easy mode{/size}" if True:
            $ brawler_difficulty = 1
        "{size=-2}Normal mode (recommended){/size}" if True:
            $ brawler_difficulty = 2
        "{size=-2}Hard mode (You have been warned!){/size}" if True:
            $ brawler_difficulty = 3

play music "music/patched/track_previous.mp3"
scene black
$ renpy.pause(2)
hide screen phone_screen
$ previousEpLabel = "startUpdate3b"

show previously_ol
$ renpy.pause()
hide previously_ol
show screen previous_screen
scene ep2_init77 with dissolve
tm "That dude is your maggot brother."
tm "If you can't prove to us that you can care for your brother..."
tm "...neither of you will become DIKs."
scene ep2_party_dildo53 with wipeleft
tm "WHAT THE FUCK ARE YOU DOING!?"
scene ep2_party_dildo54
ch "We know the HOTs are in there with you! SAGE!!!"
scene ep2_party_dildo61
dw "Typical fucking DIKs!!! Always stealing what's ours!"
scene ep2_party_story23
jac "Tommy fucked Dawe's girl and he beat Tommy for it."
scene ep2_maya_confront4 with wiperight
my "I'm sorry for what happened..."
scene ep2_maya_confront17
my "You know why I did it..."
mc "The tuition?"
my "She said that she might have an offer for me, if I passed the initiation..."
mc "So, you're being 100%% honest with me now?"
scene ep2_maya_confront32
my "Maybe 99%%..."
scene anim_maya_kiss_01_ep2 with dissolve:
    size (config.screen_width, config.screen_height)
pause

scene ep2_freeroam_ano76 with wipeleft
mc "Ok, go for the window."
de "Huh!"
scene ep2_freeroam_ano77
de "Oh my God!"
scene ep2_tyb_jill5
ty "They won't harm you. I'm here for you."

if ep2_choseMayaOverParty:
    scene ep2_mayamovienight25f with wiperight
    my "We shouldn't be kissing..."
    if ep2_fingeredMaya:
        scene ep2_mayamovienight66
        my "*{i}Moans{/i}*"
    elif True:
        mc "It's ok. I'm not going to force you."
elif ep2_danceSage and ep2_kissedSage:
    scene ep2_sage_dance13 with wiperight
    tm "That's my son..."
    jac "You do realize what this means?"
elif ep2_fuckHOT:
    scene ep2_hot_11 with wiperight
    sar "Got the cash?"
    sar "Now, slowly unbutton your pants, drop them to your ankles and whip it out."
    scene ep2_hot_cum
    sar "Wow, you really filled me up good..."

scene ep2_store20 with wipeleft
st "G-go away! You...you fucker!"
if ep2_comfortedSteve:
    scene ep2_store24
    st "It's my mom and dad..."
    st "They are getting divorced."
    mc "Stay strong, Steve."
elif True:
    mc "I'll leave you to sit there and cry in your corner."

scene ep2_josy_date40 with wiperight
mc "Tommy's your stepbrother!?"
mc "I'm a DIK pledge! Tommy's my father and I'm his maggot son."

scene ep2_josy_sofa7
mc "Did you hear anything from B&R?"
js "I've given up."

if ep2_fuckedJosy:
    scene ep2_josy_date_parents1 with wipeleft
    js "Oh, fuck! My dad and Monica are back already!"
    js "Hide!!!"

scene ep2_sun_back7 with wiperight
my "This girl..."
my "Does she make you hurt?"

scene ep2_sun_back28 with wipeleft
sa "I'm telling you, he's talking to his bitch, right now!"
scene ep2_chad_shower2
ch "I can't wait until I see you again..."

scene ep2_chad_shower8b
dw "What were you doing in there?"
if ep2FoughtJocks:
    scene ep2_chad_shower26g with vpunch
    $ renpy.pause()
elif True:
    scene ep2_chad_shower28
    dw "You better run, you cunt!"
scene ep2_chad_shower31
dw "I just caught him sneaking around in our locker room."

scene ep2_dik_night6 with wiperight
dikcs "CHUG! CHUG! CHUG!"
scene ep2_bella_date3
isa "You're drunk."
scene ep2_bella_night9e
mc "You seem to catch me at my worst, every time."
scene ep2_bella_kiss_shock1
isa "(What the hell is this boy doing!?)"

if ep2QuinnSawYouAndSage:
    scene ep2_sage_guitar44 with wipeleft
    mc "They are so big and soft..."
    scene ep2_sage_guitar_quinn4
    qu "Are you fucking perv boy?"

scene ep2_gender_after20 with wiperight
ja "If there's ever an odd couple in the class you and I could pair up and have a good..."
scene ep2_gender_after34
ja "...back and forth."

scene ep2_ending10 with wipeleft
rs "THE DEVIL'S PLEDGE BOARD!"
mc "We're going to do all that in one week?"

scene ep2_ending15 with wiperight
"{i}Is this the secret you're hiding?{/i}"
scene ep2_ending16
ch "[name]..."
$ renpy.music.stop(channel="sfx1", fadeout=0)
play sound "sound_effects/whoosh_2.mp3"
label startUpdate3b:
scene black
$ renpy.pause(2)
hide screen previous_screen
stop music fadeout 5
scene black with dissolve
show screen ep6_title_screen
$ renpy.pause(5)
hide screen phone_screen

label ep3_jade_intro:
if steamConfig or nonPatreonConfig:
    $ state = "ep3_steam"
elif True:
    $ state = "ep3"
call rpc from _call_rpc_2
play music "music/ep3/dc_love_go_go.mp3"
scene ep3_introb with fade
$ renpy.pause()
scene ep3_intro with dissolve
ja "Argh!!!"
play sound "sound_effects/glass.mp3"
scene ep3_intro1 with hpunch
"*{i}CRASH!{/i}*"
scene ep3_intro2 with dissolve
sb "Hey! Calm the fuck down, sweetheart!"
scene ep3_intro3 with dissolve
ja "Don't you call me sweetheart!"
scene ep3_intro2 with dissolve
sb "You need to fucking relax!"
sb "I told you that it was a one-time thing!"
scene ep3_intro3 with dissolve
ja "You're such a bad fucking liar, Stephen!"
ja "Do you think I'm stupid?"
ja "I know that you've done this many times!"
ja "Every time there's a different perfume or lipstick color on your shirt."
scene ep3_intro4 with dissolve
sb "You're overreacting, love!"
sb "We agreed that we should try to spice things up, didn't we?"
scene ep3_intro6 with dissolve
ja "Yes! With each other! Not on our own!"
scene ep3_intro4 with dissolve
sb "Well, we tried that already!"
sb "Most recently with Isabella!"
sb "She was clearly already in love!"
scene ep3_intro6 with dissolve
ja "That's usually the case when there's a {b}fucking{/b} wedding ring on a finger!"
scene ep3_intro9 with dissolve
ja "Oh! And again with Isabella!"
ja "I'm beginning to think that you have a crush on her!"
scene ep3_intro10 with dissolve
sb "I don't have a crush on her!"
sb "That's ridiculous! I love you!"
scene ep3_intro9 with dissolve
ja "Do you really!?"
ja "Because that's the first time you've told me that this year!"
scene ep3_intro10 with dissolve
sb "*{i}Sigh{/i}*"
sb "You've been in long-term relationships before."
sb "You know how these things go."
scene ep3_intro10b with dissolve
sb "People don't keep that spark forever."
sb "Sometimes we need something new and exciting to make us feel alive!"
scene ep3_intro3 with dissolve
ja "Young college girls, Stephen! Is that what you need?"
ja "Do you need a brand-new model to handle your shriveled cock!?"
scene ep3_intro10b with dissolve
sb "What are you saying? Isabella is almost our age."
scene ep3_intro16 with dissolve
ja "AGAIN WITH ISABELLA!"
play sound "sound_effects/glass.mp3"
scene ep3_intro1 with hpunch
"*{i}CRASH!{/i}*"
scene ep3_intro2 with dissolve
sb "It was just an example! Calm down!"
sb "I haven't even fucked her and you're acting like I did!"
scene ep3_intro9 with dissolve
ja "Who have you fucked, then? Tell me!"
ja "And no more fucking lies!"
scene ep3_intro10 with dissolve
sb "Come on, sweetheart. Let's not do this."
scene ep3_intro9 with dissolve
ja "How many, Stephen!?"
ja "Tell me or I will walk out that door, right now!"
scene ep3_intro10b with dissolve
sb "Three..."
scene ep3_intro9 with dissolve
ja "Three...students?"
scene ep3_intro10c with dissolve
$ renpy.pause()
scene ep3_intro16b with dissolve
stop music fadeout 3
ja "AARGH!!!"
play sound "sound_effects/whoosh.mp3"
image ep3_intro15_fr:
    "images/ep3/intro/ep3_intro15_frame.png"
    zoom 0.6
    xalign 0.5 yalign 0.5
    linear 0.5 zoom 3
scene ep3_intro15
show ep3_intro15_fr
$ renpy.pause(.5)
label ep3_mall_intro:
play music "music/ep3/get_back.mp3"
scene ep3_mall
show screen phone_screen
de "What about her?"
mc "Who do you mean?"
de "The girl in the tight skirt."
de "Totally a 10, right?"
scene ep3_mall1 with dissolve
mc "Hm..."
menu:
    "Agree" if True:
        mc "Yeah, for sure."
        if dtype > 0:
            scene ep3_mall2 with dissolve
            mc "Her body is amazing."
        elif True:
            mc "I like her necklace."
            de "Her...necklace?"
            de "How many beers did you drink?"
            mc "Shut up."
    "Disagree" if True:
        scene ep3_mall4 with dissolve
        mc "Nah, she's more like a 5."
        de "A 5? That's bullshit."
        mc "She's good-looking, but far from a 10."
scene ep3_mall5 at transformSide
mc "What about..."
mc "...that one? The blonde with the bag."
scene ep3_mall6 with dissolve
de "Hm... Hard to tell. Gotta see her behind first."
de "If she only would turn around."
scene ep3_mall8 with dissolve
de "Ah! There she goes."
mc "And?"
de "Nope. I need it to be bigger."
scene ep3_mall7 with dissolve
mc "{i}It{/i}, as in her ass?"
de "Yup. Camila really spoiled me."
mc "Still thinking about her, huh?"
de "Yeah..."
de "You think that's a bad idea?"
scene ep3_mall9 with dissolve
menu:
    "Yes" if True:
        $ bios_derek = True
        $ bios_history_derek += "I told Derek that him being interested in Camila was a bad idea.\n\n"
        $ chat_new_bios = True
        $ ep3_camilaDerek = False
        mc "Yeah, I don't think she's right for you."
        de "Why would you say that? She's beautiful!"
        mc "Ok, I really meant that you aren't right for her."
        de "Haha! Fuck you!"
    "No" if True:
        $ ep3_camilaDerek = True
        $ bios_derek = True
        $ bios_history_derek += "I told Derek that him being interested in Camila was a good idea.\n\n"
        $ chat_new_bios = True
        mc "No, not at all. Go for it."
de "She is hot."
mc "She is a HOT, all right. Well...almost."
de "What does that mean?"
scene ep3_mall10 with dissolve
mc "I don't know..."
mc "How do you feel about the way the HOTs treat their pledgers?"
mc "Making them do stuff like Camila did, for one...?"
de "It's part of their thing, you know."
de "They are party girls."
mc "What if that was Maya?"
scene ep3_mall13 with dissolve
de "Come on, Maya wouldn't do that."
mc "Yeah..."
mc "Even so, I think she's more malleable than you think."
de "Doesn't matter. I'll protect her."
if ep2_shotWon:
    if ep2_danceSage or ep2_fuckHOT:
        mc "Hey, what happened to that redheaded girl you were going for at the party?"
        de "When I found her, Jacob was already boning her."
        mc "Ah, that sucks."
        de "Not really, she asked me to join."

scene ep3_mall15 with dissolve
de "Oh! Oh! Look at those two!"
de "Total milfs!"
scene ep3_mall14 with dissolve
de "No way! That's Cathy and Jade!"
mc "You're right! Wow, I haven't seen them in casual clothes before."
if preferredmilf == 0:
    scene ep3_mall16 with dissolve
    de "You like Jade better, right?"
    mc "Yeah, I do."
    mc "Cathy's not bad either, though."
elif True:
    scene ep3_mall17 with dissolve
    de "You like Cathy better, right?"
    mc "Yeah, I do."
    mc "Jade's not bad either, though."

scene ep3_mall14 with dissolve
de "I still think Jade is the one."
mc "The one?"
de "Yeah...you know?"
scene ep3_mall19 with dissolve
de "For our list."
scene ep3_mall19b with dissolve
mc "Dude, I'm not sure we can do everything on that pledge board."
stop music fadeout 3
mc "Some of it seems fucking impossible."

label ep3_hell_week_presentation_label:
play music "music/ep1/energetic.mp3"
scene ep3_list
rs "Gay guard catcher!"
rs "Streak in front of at least one security guard and have him chase you."
rs "Watch as he dies inside trying to catch you."
scene ep3_list1 with dissolve
rs "Fuck a teacher! Simple, but impossible."
scene ep3_list2 with dissolve
rs "Prank the Alphas! A good prank that effectively pisses them off is all that's needed."
rs "Having sex outdoors! Perhaps with the aforementioned teacher?"
scene ep3_list4 with dissolve
rs "Have a stripper sign your cock!"
scene ep3_list5
tm "An erect cock is simpler to autograph."
scene ep3_list4 with dissolve
rs "If you're not tactful while doing that, maybe you'll end up fulfilling the goal of being slapped by three girls."
scene ep3_list7 with dissolve
tm "This week will be a very special week, maggots."
tm "You're pretty much gonna be buzzed constantly since you must finish 100 beers during Hell Week."
tm "And all tasks are of course going to be completed while wearing the traditional 24/7 Dildo helmet."
scene ep3_list9 with dissolve
tm "Being drunk is a great way to muster up courage and egg the preps!"
tm "And don't forget to book some time for that sexy car wash."
scene ep3_list11 with dissolve
tm "Maybe a granny or two wanna see some hot college boy ass while getting her car sparkling for her bridge tournament."
scene ep3_list12 with dissolve
rs "If you thought fucking a teacher was hard, how about you try to bang a feminist."
scene ep3_list13 with dissolve
tm "Watch out...they tend to bite."
tm "And finally! We can't forget about those who society always forgets about..."
tm "The nerds!"
scene ep3_list16 with dissolve
rs "Wrap up Hell Week by giving one a wedgie so far up that his ass crack gets extended."
rs "And yes, maggots! You're going to do all of that!"
scene ep3_list5 with dissolve
tm "12 tasks! One week...sort of."
tm "Rusty, tell them the rules."
scene ep3_list19 with dissolve
rs "The following rules must be followed!"
rs "Rule number 1. Proof or DIK witness is needed for every task."
scene ep3_list21 with dissolve
rs "Rule number 2. You may choose who completes the tasks or you can cooperate."
rs "But to give you some motivation..."
rs "The maggot who pulls the most weight during Hell Week will get a special prize, if the list is completed."
rs "And finally..."
scene ep3_list23 with dissolve
rs "Rule number 3. Hell Week ends at 8 p.m. on Saturday."
rs "On average, that means you must complete more than 2 tasks per day..."
scene ep3_list25 with dissolve
tm "What better way to start Hell Week than with the traditional 24/7 Dildo helmet!?"
tm "This helmet right here has been worn by each and everyone in this very room."
tm "Now, it's your turn."
tm "Wear it, at all times."
scene ep3_list27 with dissolve
rs "You may take turns wearing it and you can only take it off when you pass it to your maggot brother."
scene ep3_list28 with dissolve
mc "24/7 Dildo helmet? Since we only get five days, shouldn't it be 24/5?"
tm "Shut up."
tm "So? Who wants it first?"
if affinity == "DIK":
    $ specialMessage = "Current affinity: DIK"
elif affinity == "CHICK":
    $ specialMessage = "Current affinity: CHICK"
elif True:
    $ specialMessage = "Current affinity: NEUTRAL"

if tutorials:
    show major_choice_personality_tutorial with dissolve
    $ renpy.pause()
    hide major_choice_personality_tutorial with dissolve
show screen specialmsg
menu:
    "I do ({color=#ffffff}{size=-1}{font=collegiate.ttf}DIK{/font}{/size} or Neutral affinity{/color})" if not affinity == "CHICK":
        $ dk(1)
        $ RPdiks += 1
        $ ep3_hellWeekHelmet = 1
        $ ep3_wearHelmet = True
        $ ep3_jillHelmetChad = True
        hide screen specialmsg
        scene ep3_list32 with dissolve
        mc "I do. Give it here."
        de "Aw. I wanted to have a DIK head, too."
        scene ep3_list33 with dissolve
        mc "Don't worry, we'll take turns."
        tm "Such enthusiasm! I love it."
        scene ep3_list35 with dissolve
        de "You look like a unicorn."
    "Not me ({color=#ffffff}{size=-1}{font=collegiate.ttf}CHICK{/font}{/size} or Neutral affinity{/color})" if not affinity == "DIK":
        $ dk(-1)
        $ ep3_hellWeekHelmet = 0
        $ ep3_jillHelmetChad = False
        $ ep3_wearHelmet = False
        hide screen specialmsg
        mc "Not me."
        tm "Immediate resistance from the weakest maggot."
        scene ep3_list39 with dissolve
        de "I want it!"
        rs "Looks like someone wants to win that big prize!"
        scene ep3_list39b with dissolve
        tm "Son... I'm disappointed in you."
scene ep3_list40 with dissolve
rs "Jacob! John Boy! Bring them in."
tm "Ah, another fun part of the week."
tm "The 100 beer challenge."
stop music fadeout 3
rs "These beers are yours. Finish them by Saturday to complete the task."
label ep3_derek_dik_convo:
play music "music/ep2/rockin_riff.mp3"
if ep3_wearHelmet:
    scene ep3_post_mclist with fade
elif True:
    scene ep3_post_delist with fade
de "What's our strategy?"
if ep3_wearHelmet:
    scene ep3_post_mclist1 with dissolve
elif True:
    scene ep3_post_delist1 with dissolve
mc "To complete it?"
if ep3_wearHelmet:
    scene ep3_post_mclist with dissolve
elif True:
    scene ep3_post_delist with dissolve
de "Yeah, do we split it down the middle or what?"
if ep3_wearHelmet:
    scene ep3_post_mclist1 with dissolve
elif True:
    scene ep3_post_delist1 with dissolve
mc "I don't know, dude..."
mc "I think it's better to cooperate."
if ep3_wearHelmet:
    scene ep3_post_mclist2 with dissolve
elif True:
    scene ep3_post_delist2 with dissolve
de "I never thought you'd want to do that with me..."
if ep3_wearHelmet:
    scene ep3_post_mclist3 with dissolve
elif True:
    scene ep3_post_delist3 with dissolve
mc "To cooperate?"
if ep3_wearHelmet:
    scene ep3_post_mclist2 with dissolve
elif True:
    scene ep3_post_delist2 with dissolve
de "No, to double team a teacher and a feminist."
if ep3_wearHelmet:
    scene ep3_post_mclist3 with dissolve
elif True:
    scene ep3_post_delist3 with dissolve
mc "No, that wasn't what I was saying."
mc "I meant we try to help each other out and do the tasks together..."
mc "...except for the ones that include fucking."
if ep3_wearHelmet:
    scene ep3_post_mclist5 with dissolve
elif True:
    scene ep3_post_delist5 with dissolve
de "Cheers, [mc_de]. To Hell Week!"
mc "To Hell Week!"
if ep3_wearHelmet:
    scene ep3_post_mclist5b with dissolve
elif True:
    scene ep3_post_delist5b with dissolve
$ renpy.pause()
if ep3_wearHelmet:
    scene ep3_post_mclist2 with dissolve
elif True:
    scene ep3_post_delist2 with dissolve
de "As I see it, the hardest one by far is the teacher one."
if ep3_wearHelmet:
    scene ep3_post_mclist3 with dissolve
elif True:
    scene ep3_post_delist3 with dissolve
mc "Hm..."
mc "Jade made a move on me today."
if ep3_wearHelmet:
    scene ep3_post_mclist4 with dissolve
elif True:
    scene ep3_post_delist4 with dissolve
de "..."
mc "Yeah... That's pretty much my reaction to it, too."
de "You think you could do her?"
mc "I don't know..."
if ep3_wearHelmet:
    scene ep3_post_mclist3 with dissolve
elif True:
    scene ep3_post_delist4b with dissolve
if ep2_flirtedJade:
    mc "We flirted a bit and she surprised me and grabbed my ass when we left class together."
elif True:
    mc "She tried to flirt with me and she surprised me and grabbed my ass when we left class together."
if ep3_wearHelmet:
    scene ep3_post_mclist4 with dissolve
elif True:
    scene ep3_post_delist4 with dissolve
de "She grabbed your ass...?"
de "That is so sexist."
de "I love her."
if ep3_wearHelmet:
    scene ep3_post_mclist3 with dissolve
elif True:
    scene ep3_post_delist4b with dissolve
mc "So, hypothetically...maybe it can be done."
if ep3_wearHelmet:
    scene ep3_post_mclist2 with dissolve
elif True:
    scene ep3_post_delist2 with dissolve
de "Hypothetically? So, you're not up for it?"
de "Think about it! She's a feminist teacher!"
de "You'd be fucking two birds with one stone."
if ep3_wearHelmet:
    scene ep3_post_mclist3 with dissolve
elif True:
    scene ep3_post_delist3 with dissolve
menu:
    "I'll try" if True:
        $ ep3_hellWeekTryFuckJade = True
        mc "I'm not making any promises...but I'll try."
        if ep3_wearHelmet:
            scene ep3_post_mclist2 with dissolve
        elif True:
            scene ep3_post_delist2 with dissolve
        de "Yes! Nice!"
        de "But as a backup plan..."
        $ bios_history_derek += "I told Derek that I would try to sleep with Jade.\n\n"
        $ bios_name_derek = True
    "No way" if True:
        $ ep3_hellWeekTryFuckJade = False
        mc "Nuh uh. No way! I'm not going to do that."
        if ep3_wearHelmet:
            scene ep3_post_mclist6 with dissolve
        elif True:
            scene ep3_post_delist4 with dissolve
        de "Dammit!"
        de "*{i}Sigh{/i}*"
        de "Then I'll have to do it myself."
        if ep3_wearHelmet:
            scene ep3_post_mclist2 with dissolve
        elif True:
            scene ep3_post_delist2 with dissolve
        $ bios_history_derek += "I told Derek that I wouldn't try to sleep with Jade.\n\n"
        $ bios_name_derek = True
$ chat_new_bios = True
de "Maybe I can find another teacher and feminist...?"
if ep3_wearHelmet:
    scene ep3_post_mclist3 with dissolve
elif True:
    scene ep3_post_delist3 with dissolve
mc "Your sister is a feminist."
if ep3_wearHelmet:
    scene ep3_post_mclist7 with dissolve
elif True:
    scene ep3_post_delist7 with dissolve
de "I'm not going to fuck my sister, you pervert!"
de "Wow, you're a fucking degenerate for even suggesting that!"
if ep3_wearHelmet:
    scene ep3_post_mclist8 with dissolve
elif True:
    scene ep3_post_delist8 with dissolve
mc "I didn't suggest that!"
if ep3_wearHelmet:
    scene ep3_post_mclist7 with dissolve
elif True:
    scene ep3_post_delist7 with dissolve
de "Oh! You mean that {b}you{/b} could!"
de "No way, dude! Just...don't!"
if ep3_wearHelmet:
    scene ep3_post_mclist1 with dissolve
elif True:
    scene ep3_post_delist1 with dissolve
mc "Man...ten of these per day, each..."
mc "We're going to be drunk constantly..."
if ep3_wearHelmet:
    scene ep3_post_mclist with dissolve
elif True:
    scene ep3_post_delist with dissolve
de "If we spread it out evenly over the day, it might work."
if ep3_wearHelmet:
    scene ep3_post_mclist1 with dissolve
elif True:
    scene ep3_post_delist1 with dissolve
mc "How are we going to do that, when we have classes and all?"
mc "You know they have that stupid rule about alcohol on campus."
if ep3_wearHelmet:
    scene ep3_post_mclist with dissolve
elif True:
    scene ep3_post_delist with dissolve
stop music fadeout 3
de "We can always chug a lot before bedtime."
de "We'll figure it out."

label ep3_hot_maya_label:
play music "music/ep3/black_box.mp3"
scene ep3_hot_week with wipeleft
$ renpy.pause()
scene ep3_hot_weekb with dissolve
qu "Sisters and daughters!"
qu "We're still waiting for Sage and the rest before we can kickstart the HOT scavenger hunt."
scene ep3_hot_week1 with dissolve
qu "And while we wait, as vice president, I wanted to take the time to shine the spotlight on Camila for her excellent performance during the DIKs' CUM-petition."
scene ep3_hot_week2 with dissolve
qu "A very nice job indeed."
if ep2_wonCumpetition:
    qu "Managing to make a maggot cum before yours truly is an amazing accomplishment."
    qu "She really deserves applause, ladies."
elif True:
    qu "She wasn't quite up to par with her mother, Riona, and yours truly."
    qu "But I think she really deserves applause, ladies."
if ep2_quinnKnowsAboutCamila:
    scene ep3_hot_week4 with dissolve
    qu "*{i}Whispers{/i}* Fucking a customer who only paid for something less, on the other hand..."
    qu "That deserves punishment."
if ep2_shotWon:
    scene ep3_hot_week6 with dissolve
    if ep2_wonCumpetition:
        ml "Seriously? Applause for making that moron maggot cum?"
        ml "He couldn't even hold his alcohol, much less his cum."
        sar "Yeah, such a loser!"
    elif True:
        ml "That maggot, Derek, seems to be born to lose."
        sar "Yeah, he totally choked during the maggot shot battle."
elif True:
    scene ep3_hot_week6 with dissolve
    if ep2_wonCumpetition:
        ml "Seriously? Applause for making that moron maggot cum?"
        sar "Yeah, he's such a loser!"
    elif True:
        ml "Seriously? Applause for grinding on a loser?"
        sar "Yeah, that's ridiculous!"
scene ep3_hot_week8 with dissolve
my "..."
qu "Oh, you mean sisters! Stop it..."
scene ep3_hot_week9 with dissolve
qu "You might not realize it, but that maggot has a wannabe HOT blood relative."
qu "Isn't that right, buttercup?"
if ep2DefendMayaChance:
    sar "That's right! Derek did mention that."
elif True:
    sar "You're Derek's sister?"
scene ep3_hot_week12 with dissolve
my "Yeah, he's my twin brother."
scene ep3_hot_week13 with dissolve
qu "Interesting."
qu "And his friend..."
qu "Oh, what am I saying?"
scene ep3_hot_week13b with dissolve
qu "You know him. Your midnight booty call..."
if ep2DefendedMayaAtParty:
    qu "...he really seems to like you."
elif True:
    qu "...do you like him?"
my "..."
scene ep3_hot_week14 with dissolve
qu "You're cute."
scene ep3_hot_week15 with dissolve
qu "Camila?"
scene ep3_hot_week16 with dissolve
cam "Yes?"
scene ep3_hot_week15 with dissolve
qu "You've had the luxury to get closer to the HOTs than Maya and..."
scene ep3_hot_week18 with dissolve
mn "Mona."
scene ep3_hot_week19 with dissolve
qu "Really? Maya and Mona, hah."
scene ep3_hot_week15 with dissolve
qu "Do you like the opportunity you've been given?"
scene ep3_hot_week16 with dissolve
cam "Yes, Quinn. I...love it."
scene ep3_hot_week15 with dissolve
qu "Good answer."
qu "You see, I'm beginning to think that Maya and Mona, here, might be suitable as well."
qu "Would you agree?"
scene ep3_hot_week16 with dissolve
cam "I guess. Sure."
scene ep3_hot_week24 with dissolve
my "What's the offer?"
scene ep3_hot_week13b with dissolve
qu "Oh, you will like this."
qu "I'm aware that you ladies have heard some rumors about the HOTs, right?"
scene ep3_hot_week24 with dissolve
my "I've heard something about...free...tuition."
scene ep3_hot_week19 with dissolve
qu "Did you hear about that, as well, Mona?"
scene ep3_hot_week18 with dissolve
mn "It's been mentioned in whispers."
scene ep3_hot_week19 with dissolve
qu "Ah! The grapevine..."
qu "Seems like there's a HOT among us who can't keep her trap shut."
qu "You know how the saying goes..."
scene ep3_hot_week13b with dissolve
qu "Loose lips, sink ships."
scene ep3_hot_week13c with dissolve
qu "But loose hips, get tips."
scene ep3_hot_week19 with dissolve
qu "So, girls...are you interested?"
scene ep3_hot_week18 with dissolve
mn "Free tuition? Sign me up."
mn "I'm not passing on that offer."
scene ep3_hot_week13 with dissolve
qu "And you, buttercup?"
qu "Are you in?"
scene ep3_hot_week24 with dissolve
my "What do we have to do, exactly?"
scene ep3_hot_week34 with dissolve
sa "All right, sisters and daughters!"
sa "Sorry for the delay!"
scene ep3_hot_week13b with dissolve
qu "*{i}Whispers{/i}* Now, zip it."
scene ep3_hot_week36 with dissolve
qu "No worries, sister."
qu "I've been teaching our new daughters about the traditions."
scene ep3_hot_week37 with dissolve
sa "Awesome. Then our daughters are aware of the task at hand."
sa "Much like fraternities have their Hell Weeks and hazing rituals..."
sa "...the HOTs have an annual scavenger hunt."
scene ep3_hot_week38 with dissolve
play sound "sound_effects/water_splash.mp3"
$ renpy.sound.play("sound_effects/water_pool.mp3", channel="sfx1", loop=True)
sa "You have two weeks to complete your list and you'll work in pairs."
sa "But seeing that we're an odd number of daughters this year, we'll have to figure something out."
sa "For now, let's just take some time and relax down here."
scene ep3_hot_week39 with dissolve
play sound "sound_effects/water_splash.mp3"
sa "Quinn has been given the task to prepare your lists for later."
$ loopInt = 0
label ep3_hot_week_loop_label:
menu:
    "Check out Riona and Camila" if loopInt != 1 and loopInt != 3 and loopInt != 5 and loopInt != 7:
        $ loopInt += 1
        scene ep3_hot_week_rc with dissolve
        ri "Had enough?"
        cam "I'm just gonna grab a drink."
        scene ep3_hot_week_rc1 with dissolve
        ri "I won't say no to that."
        play sound "sound_effects/slap.mp3"
        scene ep3_hot_week_rc2 with hpunch
        cam "Ouch! Haha! Stop that!"
        scene ep3_hot_week_rc3 with dissolve
        ri "You're not into spanking?"
        cam "What made you think I was?"
        scene ep3_hot_week_rc6 with dissolve
        ri "If I had that big ass, I'd be all about getting it spanked."
        scene ep3_hot_week_rc6b with dissolve
        cam "Well, I'm not {b}all{/b} about getting spanked."
        cam "Maybe...just a little bit."
        ri "I knew it."
        jump ep3_hot_week_loop_label
    "Check out Heather and Quinn" if loopInt != 2 and loopInt != 3 and loopInt != 6 and loopInt != 7:
        $ loopInt += 2
        scene ep3_hot_week_hq with dissolve
        qu "Sup, girlfriend."
        he "Really? You couldn't find a sluttier bikini?"
        scene ep3_hot_week_hq2 with dissolve
        qu "Um... Jealous much?"
        scene ep3_hot_week_hq3 with dissolve
        he "Who are you dressing like this for? It's only us here tonight, no?"
        scene ep3_hot_week_hq4 with dissolve
        qu "Ah, that explains why you chose to dress like a fucking nun."
        qu "Here's a tip! Men like to watch tits."
        scene ep3_hot_week_hq4b with dissolve
        qu "Also, when they are used correctly in this setting, the freshies get uncomfortable."
        qu "Ergo, tits are empowering."
        scene ep3_hot_week_hq3 with dissolve
        he "Hah! Gotcha."
        he "Did Tommy say anything?"
        scene ep3_hot_week_hq5 with dissolve
        qu "Tommy says a lot of things..."
        qu "...but about what you're referring to..."
        qu "Yes. I got the info."
        scene ep3_hot_week_hq3b with dissolve
        he "Make sure you get him a bit extra. You know how he gets."
        scene ep3_hot_week_hq5 with dissolve
        qu "Then he'll have to pay extra. I'm not a free ride."
        scene ep3_hot_week_hq3b with dissolve
        he "I know, but he keeps stealing from me when he runs out."
        scene ep3_hot_week_hq5 with dissolve
        qu "Well, that's {b}your{/b} problem, isn't it?"
        scene ep3_hot_week_hq3b with dissolve
        he "You were right..."
        he "...those tits give you some weird power."
        jump ep3_hot_week_loop_label
    "Check out Sarah and Melanie" if loopInt != 4 and loopInt != 5 and loopInt != 6 and loopInt != 7:
        $ loopInt += 4
        play sound "sound_effects/shove.mp3"
        scene ep3_hot_week_sm with hpunch
        ml "Hey, scooch."
        sar "What the fuck!"
        scene ep3_hot_week_sm1 with dissolve
        sar "You almost spilled my drink!"
        scene ep3_hot_week_sm2 with dissolve
        ml "What's the big deal? You're in a bathing suit and there's water right there."
        scene ep3_hot_week_sm1 with dissolve
        sar "Get a towel and clean this mess up."
        scene ep3_hot_week_sm4 with dissolve
        ml "I'm supposed to clean {b}your{/b} mess up?"
        ml "Who am I? Your butler?"
        scene ep3_hot_week_sm5 with dissolve
        sar "If you were, you'd be fired. Spilling your Mistress' drink like that."
        scene ep3_hot_week_sm4 with dissolve
        ml "Oh, I'd be a real bad butler."
        scene ep3_hot_week_sm7 with dissolve
        ml "You want me to clean you, my Mistress?"
        sar "Haha! What are you doing!?"
        scene ep3_hot_week_sm8 with dissolve
        ml "*{i}Lick lick{/i}*"
        sar "Such a naughty, fucking butler!"
        scene ep3_hot_week_sm9 with dissolve
        sar "Here. You missed some."
        scene ep3_hot_week_sm10 with dissolve
        ml "You think I won't do it?"
        sar "I'm pretty sure you won't."
        scene ep3_hot_week_sm12 with dissolve
        sar "Melanie! HAHA! For fuck's sake!"
        ml "I'm gonna make you rehire me."
        scene ep3_hot_week_sm12b with dissolve
        sar "Hahaha!"
        jump ep3_hot_week_loop_label
    "Continue" if True:
        if not ep2_recommendedSage:
            $ renpy.music.stop(channel="sfx1", fadeout=3)

if ep2_recommendedSage:
    scene ep3_hot_week40 with dissolve
    my "Can I talk with you for a bit?"
    sa "Sure, what's up?"
    scene ep3_hot_week41 with dissolve
    my "I'm wondering if it's ok if I changed mothers?"
    scene ep3_hot_week42 with dissolve
    sa "You don't like having Quinn as your mother?"
    scene ep3_hot_week43 with dissolve
    my "Hm...I like her, but she's a bit..."
    qu "A bit what!?"
    scene ep3_hot_week45 with dissolve
    my "..."
    scene ep3_hot_week46 with dissolve
    qu "Say it."
    scene ep3_hot_week47 with dissolve
    my "Mean."
    scene ep3_hot_week46 with dissolve
    qu "Pff. Mean?"
    qu "I know what this is all about."
    qu "That maggot, [name], is trying to manipulate you."
    scene ep3_hot_week53 with dissolve
    sa "[name]?"
    scene ep3_hot_week51 with dissolve
    qu "Yeah, he's the one giving her these ideas."
    scene ep3_hot_week46 with dissolve
    qu "This is how we do it in the HOT sorority."
    qu "We don't tell the DIKs how to handle their traditions..."
    qu "...and they can't tell us how to handle ours."
    qu "Especially not a maggot."
    scene ep3_hot_week53 with dissolve
    sa "I think the two of you got off on the wrong foot."
    sa "But more importantly..."
    sa "...what's the HOTs' public code, Maya?"
    scene ep3_hot_week54 with dissolve
    my "Don't turn on each other."
    scene ep3_hot_week53 with dissolve
    sa "Spend some time getting to know Quinn."
    sa "You're not switching mothers."
    scene ep3_hot_week56 with dissolve
    qu "I guess we just found out who's working solo in the scavenger hunt."
    my "..."
    $ renpy.music.stop(channel="sfx1", fadeout=3)
    scene ep3_hot_week58 with dissolve
    $ renpy.pause()

label ep3_chad_ambush_label:
$ renpy.music.stop(channel= 'music1', fadeout=3)
$ renpy.music.stop(channel= 'music', fadeout=3)
if ep3_wearHelmet:
    scene ep3_chad_confront with wipeleft
elif True:
    scene ep3_chad_confrontb with wipeleft
$ renpy.sound.play("sound_effects/crickets.mp3", channel="sfx1", loop=True)
$ renpy.sound.play("sound_effects/dial_tone.mp3", channel="sfx2", loop=False)
"*{i}Dial tone{/i}*"
if ep2_fuckedJosy:
    mc "(Come on, Josy... Pick up...)"
    mc "(Still no answer...)"
    mc "(This doesn't feel good.)"
elif True:
    mc "(Hm... Josy doesn't answer...)"
    mc "(And she's been ignoring my texts...)"
if ep3_wearHelmet:
    scene ep3_chad_confront1 with dissolve
elif True:
    scene ep3_chad_confront1b with dissolve
mc "(I hope she's ok...)"
mc "(I could ask if Tommy heard something from her.)"
mc "(Nah, that's just stupid. She hates him.)"
if ep3_wearHelmet:
    scene ep3_chad_confront2b with dissolve
elif True:
    scene ep3_chad_confront2 with dissolve
mc "(She wouldn't reach out to him and ignore me.)"

play music "<from 14.8>music/ep1/food_chain.mp3"
play sound "sound_effects/hit.mp3"
$ renpy.music.stop(channel="sfx1", fadeout=0)
if ep3_wearHelmet:
    scene ep3_chad_confront3 with hpunch
elif True:
    scene ep3_chad_confront3b with hpunch
ch "Argh!!"
ch "You fucking asshole!"
ch "You think you can blackmail me!?"
play sound "sound_effects/hit.mp3"
if ep3_wearHelmet:
    scene ep3_chad_confront4 with hpunch
elif True:
    scene ep3_chad_confront4b with hpunch
$ renpy.pause(1)
play sound "sound_effects/hit.mp3"
if ep3_wearHelmet:
    scene ep3_chad_confront4c with hpunch
elif True:
    scene ep3_chad_confront4d with hpunch
$ renpy.pause(1)
if ep3_wearHelmet:
    scene ep3_chad_confront4e
elif True:
    scene ep3_chad_confront4f
ch "ARRGH!"
if minigames:
    hide screen phone_screen
    $ brawlerStoryFight = "chad"
    $ brawlerStoryFightLabel = "ep3_after_chad_fight_pov_label"
    jump app_brawler_label
    label ep3_after_chad_fight_pov_label:
    $ brawlerStoryFightLabel = ""
    $ brawlerStoryFight = ""
    show screen phone_screen
    if ep3_chad_fight_won and brawler_difficulty == 3 and steamAchievements and not config.console and not config.developer:
        $ achievement.grant("PRESIDENTIALBEATDOWN")
        init:
            $ achievement.register("PRESIDENTIALBEATDOWN")
        $ achievement.Sync()
elif True:
    $ ep3_chad_fight_won = True

if ep3_chad_fight_won:
    scene ep3_fight_chad_neutralb with dissolve
    ch "*{i}Grunts{/i}*"
    mc "Back the fuck off!"
    play sound "sound_effects/hit.mp3"
    if ep3_wearHelmet:
        scene ep3_chad_confront3bb with hpunch
    elif True:
        scene ep3_chad_confront3bbb with hpunch
    ch "What about you!?"
    $ renpy.pause(1)
elif True:
    $ renpy.pause(1)
$ renpy.sound.play("sound_effects/ring.mp3", channel="sfx1", loop=True)
stop music fadeout 3
if ep3_chad_fight_won:
    scene ep3_chad_confront4_2b with dissolve
elif True:
    scene ep3_chad_confront4_2 with dissolve
ch "What the fuck do you want from me!?"
mc "...wha-?"
if ep3_chad_fight_won:
    scene ep3_chad_confront4_3b with dissolve
elif True:
    scene ep3_chad_confront4_3 with dissolve
ch "..."
if ep3_chad_fight_won:
    scene ep3_chad_confront4_2b with dissolve
elif True:
    scene ep3_chad_confront4_2 with dissolve
ch "Threaten me again and I'll destroy you."
$ renpy.sound.stop(channel="sfx1", fadeout= 3)
if ep3_chad_fight_won:
    $ bios_history_chad += "Chad ambushed me and we fought, I think I really messed him up.\n\n"
elif True:
    $ bios_history_chad += "Chad ambushed me and we fought.\n\n"
$ bios_name_chad = True
$ chat_new_bios = True

label ep3_jill_rescue_label:
scene ep3_chad_confront5 with dissolve
uk "HELP! SECURITY!!!"
play sound "sound_effects/running.mp3"
scene ep3_chad_confront6 with dissolve
uk "SOMEONE!"
scene ep3_chad_confront7 with dissolve
ji "[name]!"
ji "Can you hear me? [name]?"
play music "music/ep3/guitar_gentle.mp3"
mc "Jill?"
ji "Are you ok!? Should I call for an ambulance!?"
scene ep3_chad_confront10 with dissolve
mc "No, I'm fine. I-I just..."
mc "...I lost it for a minute there."
if ep3_wearHelmet:
    scene ep3_chad_confront11 with dissolve
elif True:
    scene ep3_chad_confront11b with dissolve
mc "Aargh..."
ji "Easy! Take it slow."
mc "I'm a bit woozy."
scene ep3_chad_confront13 with dissolve
ji "You may have a concussion! We should get you to a hospital."
mc "No, I'm fine. I'll snap out of it soon."
ji "How would you know?"
mc "I'm used to getting hit."
scene ep3_chad_confront15 with dissolve
ji "Oh my God! That's terrible!"
mc "I didn't mean it that way."
mc "I practice fighting. I've learned to take punches."
ji "But still... I-I..."
scene ep3_chad_confront20 with dissolve
ji "You can barely stand on your own..."
ji "Something's wrong."
scene ep3_chad_confront21 with dissolve
mc "Nothing's wrong..."
mc "...it could be the beer I drank, too."
mc "Would you help me get back to my dorm?"
scene ep3_chad_confront20 with dissolve
ji "No."
ji "Mine is closer. Come."
if ep3_wearHelmet:
    scene ep3_chad_confront23 with dissolve
elif True:
    scene ep3_chad_confront23b with dissolve
mc "Am I allowed to be in here?"
if dtype > 0:
    mc "Isn't there a rule like preps only?"
    ji "Preps, huh?"
elif True:
    mc "Isn't there a rule against it?"
ji "Don't worry about that."
if ep3_wearHelmet:
    scene ep3_chad_confront25b with dissolve
    $ renpy.pause()
    scene ep3_chad_confront26b with dissolve
elif True:
    scene ep3_chad_confront25 with dissolve
    $ renpy.pause()
    scene ep3_chad_confront26 with dissolve
ty "Jill? Is everything ok?"
ji "Yes, don't worry."
ty "Are you sure? I can call an ambulance for your...um...{size=-8}friend{/size}."
scene ep3_chad_confront28 with dissolve
ji "I've got this, Tybalt."
if ep3_wearHelmet:
    scene ep3_chad_confront29 with dissolve
elif True:
    scene ep3_chad_confront29b with dissolve
ji "It's the door to the left."
mc "Yeah, I kn-...um...ok..."

label ep3_jill_room_label:
if ep3_wearHelmet:
    scene ep3_chad_confront30 with dissolve
elif True:
    scene ep3_chad_confront30b with dissolve
ji "Lie down on the bed, [name]."
ji "I'm going to make a call."
scene ep3_chad_confront31 with dissolve
mc "No ambulance."
mc "It's really not needed."
scene ep3_chad_confront32 with dissolve
ji "You need to get your head checked out."
ji "What if you're bleeding internally?"
scene ep3_chad_confront31 with dissolve
mc "Please...no ambulance."
scene ep3_chad_confront32 with dissolve
ji "Why won't you let me help you?"
scene ep3_chad_confront31 with dissolve
mc "Look...I can't afford to go to the hospital."
mc "And I really think I'm fine."
mc "Let's just wait for a bit."
mc "If I get worse...then...maybe an ambulance."
mc "Ok?"
scene ep3_chad_confront36 with dissolve
ji "Is it really worth risking your health over this?"
ji "Don't you have insurance?"
scene ep3_chad_confront37 with dissolve
if dtype > 0:
    mc "I'm not loaded like you."
    ji "Loaded?"
    mc "Yeah. Like I told you, I can't afford this."
elif True:
    mc "I'm not like you, Jill."
    mc "Trust me... I can't afford it."
scene ep3_chad_confront36 with dissolve
ji "But I can. Let me help you."
scene ep3_chad_confront37 with dissolve
mc "You don't have to. I'm already feeling better."
if ep3_wearHelmet:
    scene ep3_chad_confront40b with dissolve
elif True:
    scene ep3_chad_confront40 with dissolve
ji "God, you're stubborn!"
if ep3_wearHelmet:
    scene ep3_chad_confront41 with dissolve
elif True:
    scene ep3_chad_confront41b with dissolve
mc "Just let me sit for a few minutes, then I'm off on my way."
if ep3_wearHelmet:
    scene ep3_chad_confront40b with dissolve
elif True:
    scene ep3_chad_confront40 with dissolve
ji "You're not leaving like this."
ji "If you're not going to let me call an ambulance for you, you're staying until I'm sure you're really ok."
if ep3_wearHelmet:
    scene ep3_chad_confront41 with dissolve
elif True:
    scene ep3_chad_confront41b with dissolve
mc "Fine..."
if ep3_wearHelmet:
    scene ep3_chad_confront44c with dissolve
    ji "..."
    mc "..."
    scene ep3_chad_confront40b with dissolve
    ji "Are you going to tell me what's up with that silly helmet?"
    scene ep3_chad_confront41 with dissolve
    mc "Pledge stuff."
    scene ep3_chad_confront40b with dissolve
    ji "\"Pledge stuff\"?"
    scene ep3_chad_confront41 with dissolve
    mc "Pledge stuff..."
    scene ep3_chad_confront40b with dissolve
    ji "All right..."
    ji "Can I take it off to check your head?"
    scene ep3_chad_confront41 with dissolve
    mc "No need to."
    mc "I think the dildo saved me from a couple of punches."
    scene ep3_chad_confront44b with dissolve
    ji "That's a...weird sentence."
    scene ep3_chad_confront44c with dissolve
elif True:
    scene ep3_chad_confront44 with dissolve
mc "..."
if ep3_wearHelmet:
    scene ep3_chad_confront41 with dissolve
elif True:
    scene ep3_chad_confront41b with dissolve
mc "Your dorm is very nice."
if ep3_wearHelmet:
    scene ep3_chad_confront40b with dissolve
elif True:
    scene ep3_chad_confront40 with dissolve
ji "No. Don't change the subject."
ji "What just happened out there?"
$ guideSuggestedPage = 72
scene ep3_chad_confront49 with dissolve
menu:
    "Joke" if True:
        mc "You've been hanging out with Bella too much. You even sound like her."
        ji "..."
        mc "Hey, you even got the look right!"
        scene ep3_chad_confront52 with dissolve
        ji "[name]... Can you be serious for one moment?"
        scene ep3_chad_confront49b with dissolve
    "Just tell her" if True:
        scene ep3_chad_confront49b with dissolve
mc "Your guess is as good as mine. I don't know what happened."
mc "I got ambushed from out of nowhere."
mc "He screamed something about being blackmailed."
mc "But I have no clue what he meant."
scene ep3_chad_confront56 with dissolve
ji "That was the president of the tri-alpha fraternity, correct?"
scene ep3_chad_confront49b with dissolve
mc "Yeah, Chad."
scene ep3_chad_confront56 with dissolve
ji "You've had problems with him before, too."
ji "The day we met."
scene ep3_chad_confront49b with dissolve
mc "Well, yeah, not only him, though."
mc "There's this other guy...Dawe."
scene ep3_chad_confront56 with dissolve
ji "Are the tri-alphas bullying you?"
scene ep3_chad_confront49b with dissolve
menu:
    "Yes" if True:
        $ ep3_toldJillBullying = True
        mc "Kind of..."
        mc "...but it's been justified, sometimes."
        scene ep3_chad_confront56 with dissolve
        ji "Bullying is never justified, [name]."
    "No" if True:
        $ ep3_toldJillBullying = False
        mc "No, they're not bullying me."
        mc "Things like this happen. Some people aren't meant to get along and they get into fights."
        scene ep3_chad_confront56 with dissolve
        ji "Unprovoked fights?"
ji "Have you talked to someone about this?"
scene ep3_chad_confront49b with dissolve
mc "I'm talking to you."
scene ep3_chad_confront52 with dissolve
ji "And that's it? Do you know that the campus has counselors you could talk to?"
scene ep3_chad_confront49b with dissolve
mc "And say what exactly?"
scene ep3_chad_confront56 with dissolve
ji "T-that other students are beating you."
ji "H-how are you ok with this?"
scene ep3_chad_confront49b with dissolve
mc "Relax, Jill. I'll be fine..."
if ep3_wearHelmet:
    scene ep3_chad_confront60 with dissolve
    ji "Gah! I can't take you seriously when you have that thing on your head..."
scene ep3_chad_confront56 with dissolve
ji "How is your head?"
scene ep3_chad_confront49b with dissolve
mc "It's still there."
scene ep3_chad_confront63 with dissolve
ji "Please, lie down and rest for a while. I'll be back shortly."
stop music fadeout 5
if dtype > 0:
    mc "You better not call for an ambulance."
elif True:
    mc "You're not calling for an ambulance, I hope."
ji "Not for now."

label ep3_cathy_bathtub:
if _in_replay:
    hide screen phone_screen
play music "music/ep1/slow_day_blues.mp3"
scene ep3_cathy1 with wipeleft
ca "(Hm...this one is kind of hot...)"
ca "(Lean muscles...washboard stomach...)"
ca "(He's maybe a bit too young for me...)"
scene ep3_cathy2 with dissolve
ca "(...)"
ca "(Oh, what does that matter?)"
ca "(I can picture him in front of me, right now...)"
scene ep3_cathy3 with dissolve
ca "(Massaging my feet... Kissing my calves...)"
ca "(Gently tickling my leg...)"
scene ep3_cathy4 with dissolve
ca "(Then he lets his fingers wander along the inside of my thigh...)"
scene ep3_cathy5 with dissolve
ca "(...all the way up...)"
ca "(Where he stops...)"
scene ep3_cathy6 with dissolve
ca "(...and looks at me with a playful grin...)"
ca "(He sees how I wanted him to continue...)"
ca "(How I wished for him to go that last inch...)"
scene ep3_cathy5 with dissolve
ca "(Just as I think he will pull back...)"
scene ep3_cathy7 with dissolve
ca "(He moves that last bit and places his fingers against my labia...)"
ca "(...and with a firm but gentle and slow movement...)"
scene anim_cathy_rub_ep3 with dissolve
ca "(...he rubs me...)"
scene ep3_cathy10b with dissolve
ca "(I fall backwards, pressing my head against the wall, as he pushes his finger into me...)"
scene ep3_cathy10 with dissolve
ca "*{i}Moans{/i}*"
scene anim_cathy_finger_ep3 with dissolve
ca "(Deep!)"
ca "(And he doesn't stop...)"
ca "(His finger goes in and out of my pussy with a steady pace...)"
ca "*{i}Moans{/i}* Oh, God!"
ca "(HARDER!!! I want all of you inside of me!)"
stop music
play sound "sound_effects/cellphone.mp3"
scene ep3_cathy12
"*{i}Cellphone rings{/i}*"
ca "(Impeccable timing...)"
$ renpy.end_replay()
$ persistent.ep3_lewd_cathy = True
$ calcScenes()
play music "music/ep3/guitar_gentle.mp3"
scene ep3_cathy13 with dissolve
ca "Hello?"
scene ep3_chad_confront65 with dissolve
ji "Hi, it's Jill. I hate to bother you at this hour..."
ji "...but something happened."
scene ep3_cathy13 with dissolve
ca "What's wrong?"
if ep3_wearHelmet:
    scene ep3_chad_confront67 with dissolve
elif True:
    scene ep3_chad_confront67b with dissolve
mc "(This bed is really comfy...)"
mc "(Like, super-comfy...)"
mc "(I've never slept in a bed like this before.)"

label ep3_jill_night_label:
scene black with fade
stop music fadeout 15
mc "(My ears finally stopped ringing...that's a good sign.)"
mc "(It must have been all that beer that made me extra woozy.)"
mc "(What the fuck did Chad want from me?)"
mc "(Maybe Dawe told him I snuck around in their locker room?)"
mc "(That could've been it...since he's been cheating on Sage.)"
mc "(But I wouldn't call that blackmailing.)"
mc "."
mc ".."
mc "..."
mc "(Huh?)"
play music "music/ep2/winter.mp3"
scene ep3_jill_bed with fade
mc "Hey. I was resting my eyes for a while."
scene ep3_jill_bed1 with dissolve
ji "*{i}Whispers{/i}* Shh... Go ahead."
ji "I was just checking up on you."
scene ep3_jill_bed2 with dissolve
mc "Thanks..."
mc "I'm fine, though. Really. I can tell."
scene ep3_jill_bed1 with dissolve
ji "Good..."
ji "...good."
scene ep3_jill_bed2 with dissolve
mc "So, are you going to let me leave?"
scene ep3_jill_bed4 with dissolve
ji "You might just as well stay the night..."
ji "...it's already past midnight."
scene ep3_jill_bed2 with dissolve
mc "What? I fell asleep?"
scene ep3_jill_bed4 with dissolve
ji "Yeah. I've been watching you."
scene ep3_jill_bed2 with dissolve
menu:
    "That's nice." if True:
        mc "That's nice of you..."
        scene ep3_jill_bed1 with dissolve
        ji "Don't mention it."
    "That's creepy." if True:
        mc "That's...creepy."
        scene ep3_jill_bed7 with dissolve
        ji "Haha. You're welcome."
scene ep3_jill_bed8 with dissolve
ji "*{i}Yawns{/i}*"
mc "You don't need to stay up and watch me..."
mc "Go to sleep, Jill."
scene ep3_jill_bed10 with dissolve
ji "Are you really sure?"
scene ep3_jill_bed10b with dissolve
mc "Yes, if nothing has happened by now, I should be fine."
scene ep3_jill_bed11 with dissolve
ji "I still think it was stupid not going to the hospital."
scene ep3_jill_bed10b with dissolve
mc "..."
mc "Your dorm is very nice."
scene ep3_jill_bed13 with dissolve
ji "Haha. Shut up!"
scene ep3_jill_bed13b with dissolve
ji "Whoops, sorry."
mc "What? You don't have to apologize for that."
scene ep3_jill_bed13c with dissolve
ji "Anyway, let's get some rest."
scene ep3_jill_bed10b with dissolve
mc "Would it be ok if I took my clothes off?"
mc "I'm a bit hot."
scene ep3_jill_bed10 with dissolve
ji "Um..."
ji "Sure."
scene ep3_jill_bed19 with dissolve
if ep3_wearHelmet:
    ji "By clothes I hope you're also referring to that thing on your head."
    scene ep3_jill_bed19b with dissolve
    mc "Sorry...I can't. I promised them not to remove it."
    scene ep3_jill_bed19 with dissolve
    ji "No one here would notice."
    scene ep3_jill_bed19b with dissolve
    mc "It would bug me if I did, though."
    scene ep3_jill_bed19 with dissolve
    ji "Fair enough..."
elif True:
    ji "I'd offer you something to sleep in, but I don't have anything that would fit you..."
    scene ep3_jill_bed19b with dissolve
    mc "That's ok, it's not like I'm sleeping in the nude."
    scene ep3_jill_bed19 with dissolve
    ji "Haha, I surely hope that's not the case when I turn around."
scene ep3_jill_bed20 with dissolve
ji "I-... Oh."
mc "What's wrong?"
scene ep3_jill_bed22 with dissolve
ji "I thought you were done."
mc "I am...but not under the covers, yet."
if ep3_wearHelmet:
    scene ep3_jill_bed24 with dissolve
elif True:
    scene ep3_jill_bed24_nohelmet with dissolve
mc "There."
if ep3_wearHelmet:
    scene ep3_jill_bed25h with dissolve
elif True:
    scene ep3_jill_bed25 with dissolve
ji "Great..."
ji "Well... Good night."
if ep3_wearHelmet:
    play sound "sound_effects/shove.mp3"
    scene ep3_jill_bed27 with hpunch
    ji "Ouch!"
    scene ep3_jill_bed28 with dissolve
    mc "Oh, shit! Sorry!"
    mc "What were you doing?"
    scene ep3_jill_bed29 with dissolve
    ji "I was going to kiss your cheek good night."
    scene ep3_jill_bed28 with dissolve
    mc "Oh..."
    mc "Why?"
    scene ep3_jill_bed31 with dissolve
    ji "You know... Like moms do."
elif True:
    scene ep3_jill_bed33 with dissolve
    menu:
        "Turn your head" if True:
            scene ep3_jill_bed34 with dissolve
            ji "(!!!)"
            scene ep3_jill_bed35 with dissolve
            ji "Oh! I...I was going for the cheek."
            scene ep3_jill_bed37 with dissolve
            mc "Why?"
            scene ep3_jill_bed31 with dissolve
            ji "You know... Like moms do."
        "Don't move" if True:
            scene ep3_jill_bed40 with dissolve
            ji "*{i}Smack{/i}*"
            scene ep3_jill_bed37 with dissolve
            mc "What was that for?"
            scene ep3_jill_bed31 with dissolve
            ji "You know...just a kiss goodnight."
            ji "Like moms do."
ji "It's not that weird...right?"
scene ep3_jill_bed39 with dissolve
mc "I...uh...wouldn't know."
scene ep3_jill_bed31 with dissolve
ji "Your mother never did that?"
scene ep3_jill_bed39 with dissolve
mc "I'm sure she would've if she didn't pass away after I was born."
scene ep3_jill_bed44 with dissolve
ji "..."
mc "My dad kissed me a lot, though!"
scene ep3_jill_bed39 with dissolve
mc "You know...on the cheek and stuff..."
mc "No...not on the stuff...just the cheek."
scene ep3_jill_bed43 with dissolve
ji "Hahaha..."
mc "(Derek's stupidity is rubbing off on me...)"
scene ep3_jill_bed46 with dissolve
ji "Well, I'm glad your dad took care of you."
scene ep3_jill_bed39 with dissolve
mc "I'm glad you took care of me, tonight."
mc "Um...sorry, for being stubborn."
scene ep3_jill_bed31 with dissolve
ji "Don't worry. I'm the same."
ji "It's not the most flattering trait to have..."
scene ep3_jill_bed39 with dissolve
mc "We all have flaws."
mc "I have to say...this bed..."
mc "It's the most comfortable bed I've slept in."
mc "I feel like a king."
if ep3_wearHelmet:
    scene ep3_jill_bed46 with dissolve
    ji "You have a weird-looking crown, your majesty."
    scene ep3_jill_bed51b with dissolve
    ji "..."
    scene ep3_jill_bed52 with dissolve
    ji "I'm glad you're comfortable, but it's just a bed."
elif True:
    scene ep3_jill_bed52 with dissolve
    ji "It's just a bed."
scene ep3_jill_bed53 with dissolve
mc "Yeah, to you maybe. I'm not used to this."
mc "Everything in here is so...so...shiny."
scene ep3_jill_bed52 with dissolve
ji "All these possessions, they don't mean anything..."
ji "...it's just money."
scene ep3_jill_bed53 with dissolve
mc "Hm... Funny how that is."
scene ep3_jill_bed56 with dissolve
mc "All my life I've watched my dad struggle to make ends meet."
mc "I've always thought that money would solve all his problems."
mc "And here you are...saying that it doesn't mean anything..."
scene ep3_jill_bed56b with dissolve
ji "Uh...sorry, it came out wrong."
ji "I don't want to sound unappreciative..."
ji "...or cliché...but it's true..."
ji "...this isn't happiness."
scene ep3_jill_bed52 with dissolve
ji "Sure, that shiny dresser is of remarkable craftsmanship..."
ji "...and I sleep very well in this soft bed..."
ji "...but I would be perfectly fine without them."
scene ep3_jill_bed56b with dissolve
ji "And having a lot of things..."
ji "...just makes you think of what you can't buy..."
ji "...no matter how much money you have to spend."
scene ep3_jill_bed56 with dissolve
mc "Like...an island?"
scene ep3_jill_bed56c with dissolve
ji "No, not an island."
scene ep3_jill_bed56 with dissolve
mc "Two...islands?"
scene ep3_jill_bed56c with dissolve
ji "Now you're just messing with me."
scene ep3_jill_bed56 with dissolve
mc "Surely...you don't mean...three-"
scene ep3_jill_bed65 with dissolve
ji "Haha! Quiet, you!"
ji "Go to sleep, your majesty."
scene ep3_jill_bed67 with dissolve
mc "Good night, Jill..."
if ep3_wearHelmet:
    mc "I'm sorry for poking you in the eye with my penis."
$ bios_history_jill += "Jill helped me after Chad beat me. I stayed the night in her bed.\n\n"
$ bios_name_jill = True
$ chat_new_bios = True

label ep3_jill_night_sleep_label:
if ep3_wearHelmet:
    $ ep3_jillCuddle = 0
    scene ep3_jill_cuddle with Fade(1.5, 1, 0.5)
    $ renpy.pause()
    play sound "sound_effects/shove.mp3"
    scene ep3_jill_cuddle1 with hpunch
    ji "Hmph..."
    stop music fadeout 3
    scene ep3_jill_cuddle2 with dissolve
    ji "..."
    jump ep3_jill_morning_label
label ep3_jill_lewd_label:
if _in_replay:
    hide screen phone_screen
    if persistent.name == None:
        $ name = "MC"
    elif True:
        $ name = persistent.name
    if persistent.mc_jill == None:
        $ mc_jill = name
    elif True:
        $ mc_jill = persistent.mc_jill
    if persistent.jill == None:
        $ jill = "Jill"
    elif True:
        $ jill = persistent.jill
    play music "music/ep2/winter.mp3"
$ ep3_jillCuddle = 1
scene ep3_jill_cuddleb with Fade(1.5, 1, 0.5)
$ renpy.pause()
scene ep3_jill_cuddle4 with dissolve
$ renpy.pause()
scene ep3_jill_cuddle5 with dissolve
mc "(Huh...?)"
mc "([jill]...is hugging me...)"
mc "(She's fast asleep.)"
scene ep3_jill_cuddle6 with dissolve
mc "(Oh...she's got her legs all wrapped around my arm...)"
scene ep3_jill_cuddle7 with dissolve
ji "*{i}Breathes gently{/i}*"
mc "(Oh, God...)"
mc "(She's so close to my face, right now...)"
mc "(...I'm getting goosebumps all over my body.)"
scene ep3_jill_cuddle8 with dissolve
mc "(If I remove my arm slowly...she might not wake up.)"
scene ep3_jill_cuddle9 with dissolve
ji "*{i}Moans gently{/i}*"
scene ep3_jill_cuddle11 with dissolve
mc "(Is she getting off from my hand?)"
mc "(I think I can get it out...)"
mc "(I'll do it slowly again...)"
scene ep3_jill_cuddle9 with dissolve
mc "*{i}Gulp{/i}*"
ji "*{i}Moans gently{/i}*"
scene ep3_jill_cuddle11 with dissolve
ji "*{i}Breathing intensifies{/i}*"
mc "(My hand...is pressed against her pussy...)"
mc "(Is this a dream? I've been having a lot of those lately...)"
scene anim_jill_rub_ep3 with dissolve
mc "(She's starting to move her hips!?)"
mc "(She's really using my hand...to get her off in her sleep!)"
pause
menu:
    "Remove hand" if True:
        $ dk(-1)
        if not persistent.bg_jill_alt2_unlocked:
            $ persistent.bg_jill_alt2_unlocked = True
            $ chat_new_bg = True
            $ calcWallpapers()
        scene ep3_jill_cuddle15 with dissolve
        mc "(Ok...there! I'm out.)"
        mc "(I'm hard as a fucking rock...)"
        mc "(...but I can't take advantage of this situation... She's sleeping.)"
        $ bios_history_jill += "Jill rubbed herself against my hand in her sleep, I didn't take advantage of the situation.\n\n"
        $ bios_name_jill = True
        $ chat_new_bios = True
    "Move your hand a bit" if True:
        $ ep3_jillCuddle = 2
        $ dk(1)
        if not persistent.bg_jill_alt_unlocked:
            $ persistent.bg_jill_alt_unlocked = True
            $ chat_new_bg = True
            $ calcWallpapers()
        scene anim_jill_rub2_ep3 with dissolve
        mc "(Ok, that only made it worse...)"
        if dtype > 0:
            mc "(Wow...she's still going...)"
        elif True:
            mc "(But...she's not stopping...)"
        scene anim_jill_rub3_ep3 with dissolve
        mc "(She's moving her leg along my cock as she's slowly thrusting...)"
        scene anim_jill_rub2_ep3 with dissolve
        mc "(She's starting to tremble!)"
        scene ep3_jill_cuddle16a with hpunch
        ji "*{i}Moans{/i}*"
        ji "*{i}Breathes heavily{/i}*"
        mc "(Oh my God! She came!)"
        scene ep3_jill_cuddle16 with dissolve
        mc "(My hand is all warm and moist...)"
        mc "(I can't believe it!)"
        mc "(I need to remove my hand...)"
        $ bios_history_jill += "Jill rubbed herself against my hand in her sleep and I let her.\n\n"
        $ bios_name_jill = True
        $ chat_new_bios = True
        scene ep3_jill_cuddle15 with dissolve

mc "(She's still hugging me tightly, though...)"
mc "(Her hair smells all sweet and fruity...)"
mc "(...)"
stop music fadeout 3
mc "(This feels really nice...)"
mc "(...)"
$ renpy.end_replay()
$ persistent.ep3_lewd_jill = True
$ calcScenes()

label ep3_jill_morning_label:
scene ep3_jill_morning with Fade(1.5,1,1.5)
play music "music/ep2/relaxing_ballad.mp3"
mc "..."
ji "Good morning."
scene ep3_jill_morning1 with dissolve
menu:
    "Compliment her outfit" if True:
        mc "Oh...mornin'."
        if dtype > 0:
            mc "You look really hot in that outfit!"
        elif True:
            mc "What a wonderful sight to wake up to..."
            mc "That outfit really suits you."
            $ RPjill += 1
        ji "..."
    "Good morning" if True:
        mc "Good morning."
mc "I can't believe how good I slept..."
scene ep3_jill_morning2 with dissolve
ji "Glad to hear it."
ji "Listen... I don't mean to kickstart your day or anything..."
ji "...but I got you an appointment with the guidance counselors."
scene ep3_jill_morning3 with dissolve
mc "You what?"
scene ep3_jill_morning2 with dissolve
ji "The incident, yesterday..."
ji "I just had to. I can't stand idly by when I see someone get bullied."
scene ep3_jill_morning3 with dissolve
if not ep3_toldJillBullying:
    mc "I already told you yesterday..."
    mc "It wasn't bullying."
elif True:
    mc "This isn't necessary, Jill..."
mc "Ratting out Chad will only make things worse for me."
scene ep3_jill_morning2 with dissolve
ji "Don't say that. There are effective disciplinary actions to take against bullying."
scene ep3_jill_morning3 with dissolve
mc "You should have asked me before you did this."
scene ep3_jill_morning6 with dissolve
ji "I think we've already established that we're both stubborn, haven't we?"
scene ep3_jill_morning7 with dissolve
ji "I'll go prepare some breakfast for us, then I'll join you for the meeting as a witness."
scene ep3_jill_morning8 with dissolve
mc "(Fuck...)"
mc "(I get that she's trying to help, but she doesn't seem to understand...)"
mc "(She expects me to start shit with the alphas, just like that?)"
mc "(It would be like kicking a hornet's nest.)"
mc "(Besides...it's not like the DIKs are playing by the rulebook either.)"
mc "(I better watch what I say during that meeting...)"
if ep3_wearHelmet:
    scene ep3_jill_morning9 with dissolve
elif True:
    scene ep3_jill_morning9b with dissolve
$ renpy.pause()
scene ep3_jill_morning10 with dissolve
$ guideSuggestedPage = 73
ty "..."
menu:
    "Tease him" if True:
        $ RPpreps -= 1
        $ dk(1)
        if ep3_wearHelmet:
            scene ep3_jill_morning12b with dissolve
        elif True:
            scene ep3_jill_morning12 with dissolve
        mc "*{i}Pew pew{/i}*"
        stop music fadeout 3
        scene ep3_jill_morning13 with dissolve
        $ renpy.pause()
    "Greet him" if True:
        $ dk(-1)
        mc "Tybalt. Good morning to you."
        stop music fadeout 3
        scene ep3_jill_morning13b with dissolve
        $ renpy.pause()

label ep3_office_label:
play music "music/ep1/your_smile.mp3"
scene ep3_office with wipeleft
sb "Good morning."
sb "This is the affected student? What was your name, again?"
mc "[name]..."
scene ep3_office2 with dissolve
sb "Ah. [name]."
sb "I'm Professor Stephen Burke..."
sb "...this is my wife, Dr. Jade Burke..."
scene ep3_office3 with dissolve
sb "...and I believe you already know Ms. Cathy Jones, here."
scene ep3_office6 with dissolve
mc "Actually, I know both of them. I attend their classes."
scene ep3_office5 with dissolve
sb "Ah. Very well."
if ep3_wearHelmet:
    sb "Let's address the obvious thing first..."
    sb "...what's with the helmet?"
    scene ep3_office6 with dissolve
    mc "Fraternity hazing."
    scene ep3_office5 with dissolve
    sb "Very well."
sb "Jill told us that you're a victim of bullying and physical violence. Is that correct?"
scene ep3_office6 with dissolve
menu:
    "Agree" if True:
        mc "Well...yeah, kind of..."
        mc "...but there's more to it than that."
    "Disagree" if True:
        mc "No, that's not my truth."
        scene ep3_office7 with dissolve
        ji "[name]... Please, be honest."
        ji "It's ok."
        scene ep3_office6 with dissolve
        mc "I am honest."
        mc "There's been some...um...differences between me and Chad, but nothing too serious."
        mc "I wouldn't call it bullying."
scene ep3_office5 with dissolve
sb "But this student, Chad, he assaulted you last night?"
scene ep3_office6 with dissolve
menu:
    "Yes" if True:
        mc "Assaulting is a very harsh word..."
        mc "But yeah, he jumped me and we fought a bit."
    "No" if True:
        $ RPjill -= 1
        mc "No, not really."
        scene ep3_office7 with dissolve
        ji "Why are you lying, [name]?"
        ji "I saw how he beat you to the ground with my own eyes."
scene ep3_office10 with dissolve
sb "I understand how you must be feeling, [name]."
sb "You're afraid...and that's perfectly fine."
sb "We're here to help you."
scene ep3_office11 with dissolve
mc "I'm not afraid."
mc "I just don't want to start any more trouble."
scene ep3_office12 with dissolve
ca "If I may..."
if failedEnglish + failedMath <= 1:
    ca "[name], here, is an excellent student. One of the better ones in my classes."
    ca "It pains me to see someone so smart fall victim to bullying."
    ca "It reminds me of my own young adulthood."
elif failedEnglish + failedMath <= 3:
    ca "[name], here, is a good student. He's very diligent."
    ca "It pains me to see someone with such great potential fall victim to bullying."
    ca "It reminds me of my own young adulthood."
elif True:
    ca "[name], here, struggles a lot in my classes."
    ca "It pains me to see him fall victim to bullying and maybe it's a reason for his underperformance."
scene ep3_office13 with dissolve
ca "Let me just ask you this..."
ca "...would it be ok if we brought in Chad to discuss this predicament you've gotten yourself into?"
ca "Even though disciplinary actions may have some effect..."
ca "...maybe we can truly sort this matter out with a proper discussion?"
scene ep3_office14 with dissolve
ja "Cathy, you can't be that soft."
ja "Bullies will always be bullies."
ja "The only way to stop them is through punishment."
scene ep3_office15 with dissolve
ja "Being a student here at B&R isn't a right; it's a privilege."
menu:
    "Peek" if True:
        $ ep3_peekedJade = True
        $ dk(1)
        scene ep3_office15b with dissolve
        mc "*{i}Gulp{/i}*"
        scene ep3_office15c with dissolve
        ja "If you can't behave as an adult, you lose that privilege."
    "Don't risk it" if True:
        $ ep3_peekedJade = False
        $ dk(-1)
        ja "If you can't behave as an adult, you lose that privilege."
ja "Simple as that."

scene ep3_office16 with dissolve
sb "I'm not so sure about this."
sb "I think Cathy might be onto something."
sb "Maybe we can solve this without having to expel anyone and make this boy's student life more worthy."
sb "And you know...it's not just anyone we're talking about."
sb "It's Chad."
sb "How about if we try to find a middle ground?"
scene ep3_office17 with dissolve
ja "(Of course you'd side with Cathy before you'd side with your wife...)"
ja "(You cheating bastard!)"
scene ep3_office18 with dissolve
mc "Can we forget about this?"
mc "I just want to leave."
scene ep3_office19 with dissolve
ji "[name]...please?"
scene ep3_office20 with dissolve
sb "I'm sorry, [name]."
sb "Once we get a report about physical violence between students, we can't just ignore it."
sb "But let's try to do this Cathy's way."
label ep3_office_chad_label:
if ep3_chad_fight_won:
    scene ep3_office_chadb with dissolve
elif True:
    scene ep3_office_chad with dissolve
sb "Chad, welcome. Please, come in."
sb "I hope you're ok with an open discussion like this."
if ep3_chad_fight_won:
    scene ep3_office_chad2b with dissolve
elif True:
    scene ep3_office_chad2 with dissolve
ch "I haven't done anything, Stephen."
sb "Relax. You'll get your chance to tell your side of the story."
if ep3_chad_fight_won:
    scene ep3_office_chad3b with dissolve
elif True:
    scene ep3_office_chad3 with dissolve
ch "There is no story to tell."
if ep3_chad_fight_won:
    scene ep3_office_chad4b with dissolve
elif True:
    scene ep3_office_chad4 with dissolve
sb "How about you start by telling us why you assaulted [name], yesterday?"
ch "I don't know what you're talking about."
if ep3_chad_fight_won:
    scene ep3_office_chad6b with dissolve
elif True:
    scene ep3_office_chad6 with dissolve
ji "Oh, stop it! I saw it with my own eyes!"
scene ep3_office_chad7 with dissolve
ca "Jill, come with me. I think it's best if you wait outside for a while."
if ep3_chad_fight_won:
    scene ep3_office_chad8b with dissolve
elif True:
    scene ep3_office_chad8 with dissolve
sb "There's an eyewitness saying that you did."
sb "Just...come clean with us and this will be much easier for you."
if ep3_chad_fight_won:
    scene ep3_office_chad9b with dissolve
elif True:
    scene ep3_office_chad9 with dissolve
ch "..."
if ep3_chad_fight_won:
    sb "How did you get those bruises?"
elif True:
    sb "Looks like you're in a bit of pain over there."
    sb "Where did you injure yourself?"
if ep3_chad_fight_won:
    scene ep3_office_chad10bb with dissolve
elif True:
    scene ep3_office_chad10 with dissolve
ch "In the gym."
if ep3_chad_fight_won:
    scene ep3_office_chad10bbb with dissolve
elif True:
    scene ep3_office_chad10b with dissolve
sb "Aha..."
sb "That's right, you train a lot."
sb "Being here on a B&R scholarship for athletes and all..."
scene ep3_office_chad_jade with dissolve
$ renpy.pause()
scene ep3_office_chad_jade1 with dissolve
$ renpy.pause()
scene ep3_office_chad_jade2 with dissolve
$ renpy.pause(2)
scene ep3_office_chad_jade3 with dissolve
mc "(What the hell!?)"
if ep3_chad_fight_won:
    scene ep3_office_chad12b with dissolve
elif True:
    scene ep3_office_chad12 with dissolve
$ bios_history_jade += "Jade flashed me during a meeting in front of her husband!\n\n"
$ bios_name_jade = True
$ chat_new_bios = True
ch "Is that supposed to be some kind of a threat?"
scene ep3_office_chad13 with dissolve
sb "Don't be stupid. I don't make threats."
sb "But the hard truth is that your scholarship will be revoked if you're assaulting fellow students."
sb "We have to follow the rules."
sb "But if you admit to what you've done and promise to not do it again..."
sb "...perhaps we can come to an agreement that mitigates your punishment."
if ep3_chad_fight_won:
    scene ep3_office_chad14bb with dissolve
elif True:
    scene ep3_office_chad14 with dissolve
ch "..."
if ep3_chad_fight_won:
    scene ep3_office_chad12b with dissolve
elif True:
    scene ep3_office_chad12 with dissolve
ch "Fine, I hit him. I'm sorry."
scene ep3_office_chad13 with dissolve
sb "Great, that's a start. Now, why did you hit him?"
if ep3_chad_fight_won:
    scene ep3_office_chad12b with dissolve
elif True:
    scene ep3_office_chad12 with dissolve
ch "...no reason."
scene ep3_office_chad13 with dissolve
sb "Chad... There's got to be a reason."
sb "I know you. You're not the type of guy to beat up a guy, unprovoked."
if ep3_chad_fight_won:
    scene ep3_office_chad14bb with dissolve
elif True:
    scene ep3_office_chad14 with dissolve
ch "..."
scene ep3_office_chad13 with dissolve
sb "Well...you did admit your guilt."
sb "That's something."
sb "You do understand that you can't expect to keep your position as the president of the tri-alphas after this?"
if ep3_chad_fight_won:
    scene ep3_office_chad14bbb with dissolve
elif True:
    scene ep3_office_chad14b with dissolve
ch "What!? C-come on!"
scene ep3_office_chad13 with dissolve
sb "I'm sorry Chad, but I can't think of any scenario where B&R would allow that."
sb "You're suspended from any fraternal activities for the near future..."
sb "...and consider yourself lucky that we're not going to revoke your scholarship."
if ep3_chad_fight_won:
    scene ep3_office_chad14bb with dissolve
elif True:
    scene ep3_office_chad14 with dissolve
menu:
    "Defend Chad" if True:
        $ ep3_intervenedChad = True
        scene ep3_office_chad14c2 with dissolve
        mc "Hey, Professor Burke..."
        mc "You don't have to do this to him."
        mc "Can't you let it slide with a warning or something?"
        if ep3_chad_fight_won:
            scene ep3_office_chad14c3b with dissolve
        elif True:
            scene ep3_office_chad14c3 with dissolve
        $ renpy.pause()
        scene ep3_office_chad14c4 with dissolve
        sb "It might not look like it to you, but this {b}is{/b} him getting off with a warning."
        sb "We can't do much else."
        $ bios_history_chad += "I tried to defend Chad when he got suspended from being the tri-alpha president.\n\n"
        $ bios_name_chad = True
    "Stay quiet" if True:
        $ ep3_intervenedChad = False
        $ bios_history_chad += "I didn't defend Chad when he got suspended from being the tri-alpha president.\n\n"
        $ bios_name_chad = True
$ chat_new_bios = True
if ep3_chad_fight_won:
    scene ep3_office_chad14bb with dissolve
elif True:
    scene ep3_office_chad14 with dissolve
ch "..."
scene ep3_office_chad13 with dissolve
sb "Then it's settled."
sb "You get one final chance and we will be watching you, very closely..."
sb "The same goes for your former fraternity."
sb "Be sure to tell your friends that."
if ep3_chad_fight_won:
    scene ep3_office_chad14fb with dissolve
elif True:
    scene ep3_office_chad14f with dissolve
sb "Hey..."
sb "We're giving you a second chance, here. Don't let it go to waste."
sb "We don't do third chances."
sb "Go apply for a standard dorm, will you?"
sb "We'll talk more about your punishment later."
scene ep3_office_chad17 with dissolve
sb "Ok, [name]. Unless you want to press charges against Chad, we're done here."
scene ep3_office_chad18 with dissolve
mc "We're done here."
scene ep3_office_chad17 with dissolve
sb "Let us know immediately if this happens again."
sb "I want you to be well aware that we're on your side in this matter."
sb "You may leave."
if ep3_wearHelmet:
    scene ep3_office_chad20 with dissolve
elif True:
    scene ep3_office_chad20b with dissolve
ji "Hey, [name]! Wait!"
scene ep3_office_chad23 with dissolve
ji "Don't be mad..."
scene ep3_office_chad23b with dissolve
$ ep3_scoldedJill = False
menu:
    "Discuss" if True:
        mc "Don't be mad?"
        scene ep3_office_chad23 with dissolve
        ji "You know I did it because I care."
        scene ep3_office_chad23b with dissolve
        mc "Who are you to decide what's best for me like that?"
        if dtype > 0:
            mc "You treated me like a fucking kid!"
        mc "You really should have asked me first."
        scene ep3_office_chad23 with dissolve
        ji "What choice did you leave me with!?"
        ji "You'd just say no when you clearly needed help."
        scene ep3_office_chad23b with dissolve
        mc "If you just had asked me, I would have told you why this was a bad idea."
        scene ep3_office_chad23 with dissolve
        ji "Then tell me! Why was it?"
        $ guideSuggestedPage = 74
        scene ep3_office_chad23b with dissolve
        menu:
            "Go easy on her" if True:
                mc "It doesn't matter now. What's done is done."
                scene ep3_office_chad23c with dissolve
                ji "..."
                mc "Just let me be, ok?"
            "Be harsh" if True:
                $ ep3_scoldedJill = True
                $ RPjill -= 1
                mc "Just don't be surprised when you find me on the ground again."
                scene ep3_office_chad23d with dissolve
                ji "..."
                $ bios_history_jill += "I scolded Jill for going behind my back and reporting the assault to the guidance counselors.\n\n"
                $ bios_name_jill = True
                $ chat_new_bios = True
    "Leave" if True:
        if dtype > 0:
            mc "I can't look at you right now."
        elif True:
            mc "Just let me be."
stop music fadeout 3
scene ep3_office_chad29 with dissolve
$ renpy.pause()
$ guideSuggestedPage = 74
label ep3_maya_morning_label:
play music "music/ep2/by_your_side.mp3"
scene ep3_maya_morning with wipeleft
my "Um...what the hell happened to you!?"
scene ep3_maya_morning1 with dissolve
mc "Don't worry, the swelling is gone."
scene ep3_maya_morning2 with dissolve
my "You got beat up?"
scene ep3_maya_morning1 with dissolve
mc "Kind of..."
mc "You know Chad?"
scene ep3_maya_morning2 with dissolve
my "He did this to you!?"
scene ep3_maya_morning1 with dissolve
mc "Yeah, I don't know why..."
mc "It might be because I spied on him before."
scene ep3_maya_morning2 with dissolve
my "Huh?"
my "Because of the DIKs?"
scene ep3_maya_morning1 with dissolve
mc "No, because of Sage. It's a long story."
scene ep3_maya_morning4 with dissolve
my "Sage, huh?"
if ep2_recommendedSage:
    my "You know, I tried talking to her about the Quinn situation."
    scene ep3_maya_morning3 with dissolve
    mc "Oh, good."
    scene ep3_maya_morning4 with dissolve
    my "No. Not good."
    scene ep3_maya_morning3 with dissolve
    mc "What?"
    scene ep3_maya_morning5 with dissolve
    my "Let's just say that I can't switch mothers."
    scene ep3_maya_morning3 with dissolve
    mc "Why?"
    scene ep3_maya_morning5 with dissolve
    my "{i}Don't turn on each other.{/i}"
    scene ep3_maya_morning3 with dissolve
    mc "Their public code..."
    scene ep3_maya_morning5 with dissolve
    my "Yes...and what's worse..."
    my "Quinn found out I tried to switch and she's punishing me for it."
    scene ep3_maya_morning3 with dissolve
    mc "You don't have to do what she tells you, Maya."
    if ep3_wearHelmet:
        scene ep3_maya_morning6 with dissolve
        my "Have you looked at yourself in the mirror, lately?"
        scene ep3_maya_morning3 with dissolve
        mc "Excuse me, but I wanted to wear this."
        scene ep3_maya_morning6 with dissolve
        my "Haha, you're such an idiot."
elif True:
    my "And I thought Quinn was trouble."
    scene ep3_maya_morning3 with dissolve
    mc "Sage isn't trouble...but she has her issues, too."

scene ep3_maya_morning7 with dissolve
my "Derek told me you started your Hell Week."
my "He was here this morning dropping your beer off."
menu:
    "Peek" if True:
        $ dk(1)
        scene ep3_maya_morning7b with dissolve
        mc "(Nice...)"
    "Don't risk it" if True:
        $ dk(-1)
play sound "sound_effects/bottle_open.mp3"
scene ep3_maya_morning8 with dissolve
my "He also told me to help you get started."
my "...or {b}force{/b} you to get started was more how he phrased it."
scene ep3_maya_morning8b with dissolve
mc "Thanks. Yeah, Hell Week is really intense."
mc "It's just me and Derek and we're supposed to do so many impossible things in just five days."
scene ep3_maya_morning8c with dissolve
my "Things like what?"
scene ep3_maya_morning8d with dissolve
if dtype > 0:
    mc "If it's not related to alcohol, it's either fucking with or just fucking people."
elif True:
    mc "It involves alcohol, pranks and sex."
scene ep3_maya_morning9 with dissolve
my "They expect you to sleep with people for Hell Week?"
scene ep3_maya_morning8d with dissolve
mc "Yes..."
scene ep3_maya_morning11 with dissolve
my "You too, huh?"
scene ep3_maya_morning12 with dissolve
mc "What? Maya?"
scene ep3_maya_morning13 with dissolve
my "You thought DIKs were the only ones having Hell Week?"
my "It's pretty much a standard for all frats and sororities."
scene ep3_maya_morning12 with dissolve
mc "I didn't even think of that..."
scene ep3_maya_morning13 with dissolve
my "Yup. The HOTs don't call it Hell Week, though."
my "They call it \"The HOT scavenger hunt\"."
scene ep3_maya_morning14 with dissolve
my "We get a list of things we must do or find."
my "Finish the list in two weeks or you're rejected."
scene ep3_maya_morning12 with dissolve
mc "You have to do all of it?"
scene ep3_maya_morning14 with dissolve
my "I think so... We're supposed to work in pairs..."
my "...but we're an uneven number of pledgers..."
if ep2_recommendedSage:
    my "...and remember that Quinn wanted to punish me?"
    scene ep3_maya_morning12 with dissolve
    mc "You're doing it all by yourself?"
    scene ep3_maya_morning13 with dissolve
    my "Bingo."
elif True:
    my "...so we're working as a team of three for this."
    my "And Quinn gave us all some individual tasks to compensate..."
scene ep3_maya_morning12 with dissolve
mc "What do you have to do?"
scene ep3_maya_morning13 with dissolve
my "Most things aren't {b}that{/b} bad..."
scene ep3_maya_morning14 with dissolve
my "...but the hardest ones are sexual."
my "I'm gonna fail."
scene ep3_maya_morning12 with dissolve
mc "Are they that hard to complete?"
scene ep3_maya_morning22 with dissolve
my "Make out with a guy. Make out with a girl."
my "Give a handjob. Give a blowjob. Give a thighjob."
mc "Ok, I get it."
my "Fuck a guy. Have a threesome. Have sex in public."
scene ep3_maya_morning12 with dissolve
mc "And the list keeps going..."
scene ep3_maya_morning14 with dissolve
my "Yeah. So, I'm fucked..."
my "...no pun intended."
scene ep3_maya_morning12 with dissolve
mc "Does B&R really allow this?"
scene ep3_maya_morning13 with dissolve
my "No clue. But, if I ask, I will likely ruin my chances for tuition."
my "And yesterday...Quinn actually offered that to us."
scene ep3_maya_morning28 with dissolve
my "It's funny..."
my "It feels like it's within reach..."
my "...but I thought about what you asked me to do..."
my "...to think things through next time, before I do something stupid."
scene ep3_maya_morning29 with dissolve
my "And yeah... I want that tuition..."
my "...but this list..."
my "...I'm not someone who, practically, will sell my body to get it."
scene ep3_maya_morning28 with dissolve
my "That \"waking you up\" thingy I did was so humiliating..."
my "...and I refused to do the CUM-petition."
scene ep3_maya_morning12 with dissolve
mc "They asked you to do that?"
scene ep3_maya_morning14 with dissolve
my "Luckily, Camila stepped up."
scene ep3_maya_morning12 with dissolve
mc "I see..."
scene ep3_maya_morning28 with dissolve
my "So...I thought it through..."
my "...and I'm gonna do the only thing I can do..."
scene ep3_maya_morning29b with dissolve
mc "Which is?"
scene ep3_maya_morning29 with dissolve
my "I'm not going to pledge the HOTs."
my "I'll have to survive college without that tuition."
scene ep3_maya_morning29b with dissolve
mc "Honestly..."
mc "...if you still have the money to survive college..."
mc "...fuck that free tuition."
scene ep3_maya_morning28 with dissolve
my "You really don't get it..."
my "That tuition...it changes everything."
scene ep3_maya_morning29b with dissolve
menu:
    "Offer to help her" if True:
        $ RPmaya += 1
        $ ep3_mayaOfferedHelp = True
        scene ep3_maya_morning29c with dissolve
        mc "Hey..."
        mc "What if I helped you?"
        if ep3_wearHelmet:
            scene ep3_maya_morning37 with dissolve
            my "Haha! Sorry..."
            my "It's hard to take you seriously with that helmet on."
            scene ep3_maya_morning29c with dissolve
            mc "Well, I am serious..."
        elif True:
            scene ep3_maya_morning13 with dissolve
            my "What?"
            scene ep3_maya_morning29c with dissolve
        mc "I know it sounds weird, but hear me out..."
        mc "You have a list that you can't finish by yourself..."
        mc "...and I kind of have one, too."
        scene ep3_maya_morning13 with dissolve
        my "Which ones do you need help with?"
        scene ep3_maya_morning12 with dissolve
        if dtype > 0:
            mc "Public sex and sex with a feminist."
            scene ep3_maya_morning42 with dissolve
            my "This isn't a good way to proposition anyone."
        elif True:
            mc "We have some joint ones. So, if we finish yours we'll get a few of mine as well."
            scene ep3_maya_morning42 with dissolve
            my "Oh...wow...um..."
        $ bios_history_maya += "I offered to help Maya with her HOT scavenger hunt.\n\n"
        $ bios_name_maya = True
    "Don't offer your help" if True:
        $ ep3_mayaOfferedHelp = False
        mc "If that's so, then don't give up so easily."
        $ bios_history_maya += "I didn't offer to help Maya with her HOT scavenger hunt.\n\n"
        $ bios_name_maya = True
$ chat_new_bios = True
scene ep3_maya_morning28 with dissolve
my "Listen...I appreciate what you're trying to do...but..."
my "That list is not easy for me..."
scene ep3_maya_morning29 with dissolve
my "...for many reasons."
scene ep3_maya_morning29b with dissolve
if dtype > 0:
    mc "It's just sex, Maya."
elif True:
    mc "If you do those things with someone you like..."
    mc "...it's not bad, Maya."
scene ep3_maya_morning28 with dissolve
my "[name]..."
scene ep3_maya_morning29b with dissolve
my "..."
scene ep3_maya_morning28 with dissolve
my "I've dated guys before..."
my "...but I've never slept with one."
scene ep3_maya_morning29b with dissolve
mc "So, you're a virgin?"
scene ep3_maya_morning29 with dissolve
my "...no."
scene ep3_maya_morning29b with dissolve
mc "Oh...you mean that you've..."
scene ep3_maya_morning29 with dissolve
my "I've only been with a girl, so far."
scene ep3_maya_morning49 with dissolve
mc "But...what about...you know..."
scene ep3_maya_morning48 with dissolve
my "You and me?"
scene ep3_maya_morning49 with dissolve
mc "Yeah...?"
scene ep3_maya_morning48 with dissolve
my "It beats me..."
my "It's the first time I've gotten this close and felt this kind of attraction to a guy..."
scene ep3_maya_morning29b with dissolve
mc "Is this what you've been hiding?"
my "..."
scene ep3_maya_morning29 with dissolve
my "I can't complete that list on my own."
my "And I shouldn't complete that list..."
scene ep3_maya_morning29b with dissolve
mc "This might be a long shot..."
mc "...but what if you told them where you come from?"
scene ep3_maya_morning53 with dissolve
my "And tell them that I've only been with a girl!?"
my "Are you insane!? No way!"
my "No fucking way!"
scene ep3_maya_morning54 with dissolve
my "I'm not telling anyone that! Nuh-uh!"
my "Not again!"
mc "You told me..."
scene ep3_maya_morning42 with dissolve
my "Don't tell anyone... Ok?"
scene ep3_maya_morning12 with dissolve
mc "Of course not."
mc "Is this why you have family issues?"
scene ep3_maya_morning28 with dissolve
my "It's that obvious, huh?"
scene ep3_maya_morning12 with dissolve
mc "I'm just trying to connect the dots here."
scene ep3_maya_morning14 with dissolve
my "Yes. That's why."
my "My family is...um...well my dad is..."
my "He's very religious..."
scene ep3_maya_morning29 with dissolve
my "And when he found out I had a girlfriend...he..."
scene ep3_maya_morning12 with dissolve
mc "Oh...say no more...I understand."
scene ep3_maya_morning14 with dissolve
my "Ok... So...now you know."
my "And please...don't tell anyone about it."
scene ep3_maya_morning12 with dissolve
mc "Derek knows, right?"
scene ep3_maya_morning13 with dissolve
my "Yeah, Derek knows."
scene ep3_maya_morning12 with dissolve
mc "Ok... This is a lot to take in."
mc "I need to think for a bit."
mc "...and get a shower, too. I reek..."
$ bios_history_maya += "Maya's family issues are due to her liking girls. Her religious father didn't like that.\n\n"
$ bios_name_maya = True
$ chat_new_bios = True
jump ep3_freeroam_maya_label

label ep3_maya_grass_label:
scene ep3_maya_grass with dissolve
mc "This isn't working."
mc "Come. Let's get some air."
scene ep3_maya_grass1 with dissolve
my "Totally. I need to clear my head."
scene ep3_maya_grass2a at transformSide2
ty "Come on, chaps!"
ty "It isn't called Hell Week for no reason."
ty "Personally, I wanted to rename it to Dante Week."
ty "But the board pointed out to me that it sounded way too foreign and perhaps even a tad German, so they passed on that idea."
ty "But that's not what matters now!"
ty "Who will lose this one? I think it's too close to call."
scene ep3_maya_grass2ab with hpunch
prepp "*{i}Exhales quickly{/i}*"
rich "We have a loser!"
scene ep3_maya_grass2ac with dissolve
ty "Haha! Remember the rules!"
ty "The loser must spend the week without a jacket and eat a lemon!"

if ep3_wearHelmet:
    scene ep3_maya_grass2 with dissolve
elif True:
    scene ep3_maya_grass2b with dissolve
mc "It's times like these I wish I were rich."
if ep3_wearHelmet:
    scene ep3_maya_grass3 with dissolve
elif True:
    scene ep3_maya_grass3b with dissolve
my "You're jealous of what they're doing?"
my "I can buy you a lemon, if you want one."
if ep3_wearHelmet:
    scene ep3_maya_grass2 with dissolve
elif True:
    scene ep3_maya_grass2b with dissolve
mc "Haha, no! I just meant in general."
if ep3_wearHelmet:
    scene ep3_maya_grass3 with dissolve
elif True:
    scene ep3_maya_grass3b with dissolve
my "What would you do if you were?"
if ep3_wearHelmet:
    scene ep3_maya_grass2 with dissolve
elif True:
    scene ep3_maya_grass2b with dissolve
mc "I'd help you out with the tuition."
scene ep3_maya_grass4 with dissolve
my "Haha. No, I meant for yourself."
my "Do you have any dreams?"
scene ep3_maya_grass5 with dissolve
mc "I'd help dad renovate our house."
mc "I'd buy him a proper kitchen and help him install it."
mc "I'd change every wallpaper, tear up the carpet and replace the floorboards with some proper wood."
mc "To show him that I've really learned a lot from him."
mc "I can only imagine the smile it would put on his face."
scene ep3_maya_grass6 with dissolve
my "That's so sweet..."
my "...but that's not for yourself, either."
scene ep3_maya_grass5 with dissolve
mc "Oh, but it is."
mc "It would make me so happy, too."
scene ep3_maya_grass6 with dissolve
my "That's very unselfish."
scene ep3_maya_grass5 with dissolve
mc "What would you do?"
scene ep3_maya_grass10 with dissolve
my "Easy!"
my "I'd buy a yacht with a shitload of servants."
scene ep3_maya_grass11 with dissolve
my "Hahaha!"
if ep3_wearHelmet:
    scene ep3_maya_grass12 with dissolve
elif True:
    scene ep3_maya_grass12b with dissolve
mc "Haha! I don't believe you one bit."
my "Haha, good! No, that's not me."
if ep3_wearHelmet:
    scene ep3_maya_grass12c with dissolve
elif True:
    scene ep3_maya_grass12d with dissolve
my "You know what I'd do?"
my "I'd buy a movie theater and just binge-watch all the best movies."
my "To have a movie theater...just for myself..."
my "...that would really be something."
scene ep3_maya_grass13 with dissolve
mc "Could I come?"
my "Of course you could come. We could watch scary movies together!"
mc "That's a nice dream."
if ep3_wearHelmet:
    scene ep3_maya_grass16 with dissolve
    $ renpy.pause()
    scene ep3_maya_grass16b with dissolve
    $ renpy.pause()
    scene ep3_maya_grass16c with dissolve
    $ renpy.pause()
elif True:
    scene ep3_maya_grass17 with dissolve
    $ renpy.pause()
    scene ep3_maya_grass18 with dissolve
    $ renpy.pause()
    scene ep3_maya_grass19 with dissolve
    $ renpy.pause()

label ep3_derek_confront_label:
if ep3_wearHelmet:
    scene ep3_derek_confront with dissolve
    de "Get that plastic dick away from my sister's face!"
    scene ep3_derek_confront1b with dissolve
elif True:
    scene ep3_derek_confrontb with dissolve
    de "[mc_de_up]!? What the hell are you doing to our maggot sister!?"
    scene ep3_derek_confront1 with dissolve
de "How could you, Maya!?"
if not ep2_wonCumpetition:
    de "You know that this guy eats his own cum, right?"
if ep3_wearHelmet:
    scene ep3_derek_confront2 with dissolve
elif True:
    scene ep3_derek_confront2b with dissolve
my "Relax, Derek! [name] was just helping me."
if ep3_wearHelmet:
    scene ep3_derek_confront1b with dissolve
elif True:
    scene ep3_derek_confront1 with dissolve
if not ep2_wonCumpetition:
    de "How the hell is he helping you with his cummy mouth?"
elif True:
    de "You call that helping you?"
if ep3_wearHelmet:
    scene ep3_derek_confront2 with dissolve
elif True:
    scene ep3_derek_confront2b with dissolve
my "It's Hell Week, Derek. Who would you rather see me do it with?"
if ep3_wearHelmet:
    scene ep3_derek_confront1b with dissolve
elif True:
    scene ep3_derek_confront1 with dissolve
de "Hell Week?"
scene ep3_derek_confront5 with dissolve
my "Yes! Just like yours. I have this scavenger hunt."
my "And [name] was just...helping me...with a thing on the list."
if ep3_wearHelmet:
    scene ep3_derek_confront6 with dissolve
elif True:
    scene ep3_derek_confront6b with dissolve
de "Don't you say sex outdoors. Please...not sex outdoors."
mc "Hey, you're overreacting."
if ep3_wearHelmet:
    scene ep3_derek_confront7 with dissolve
elif True:
    scene ep3_derek_confront7b with dissolve
de "Am I?"
if ep3_wearHelmet:
    scene ep3_derek_confront8 with dissolve
elif True:
    scene ep3_derek_confront8b with dissolve
de "This isn't you, sis."
my "..."
de "Yeah, you know what I'm talking about."
de "Are you throwing that away?"
if ep3_wearHelmet:
    scene ep3_derek_confront9b with dissolve
elif True:
    scene ep3_derek_confront9 with dissolve
my "I don't know...this is so much easier..."
my "...and when there's nothing but fighting or being ghosted..."
my "...I'm wondering if there's something left to keep."
if ep3_wearHelmet:
    scene ep3_derek_confront8 with dissolve
elif True:
    scene ep3_derek_confront8b with dissolve
de "Then...do it the right way..."
de "Not like this."
if ep3_wearHelmet:
    scene ep3_derek_confront9b with dissolve
elif True:
    scene ep3_derek_confront9 with dissolve
my "Can we talk about this later?"
if ep3_wearHelmet:
    scene ep3_derek_confront8 with dissolve
elif True:
    scene ep3_derek_confront8b with dissolve
de "You know I mean well, right?"
if ep3_wearHelmet:
    scene ep3_derek_confront10 with dissolve
elif True:
    scene ep3_derek_confront10b with dissolve
my "Always and ever."
de "Always and ever."
scene ep3_derek_confront16 with dissolve
my "Later, [name]. Ok?"
mc "Sure."

if ep3_wearHelmet:
    scene ep3_derek_confront17 with dissolve
elif True:
    scene ep3_derek_confront17b with dissolve
de "Hey. Look..."
de "I'm not the one to cockblock a maggot brother..."
de "...but that's my sis."
if ep3_wearHelmet:
    scene ep3_derek_confront18 with dissolve
elif True:
    scene ep3_derek_confront18b with dissolve
if ep2_toldDerekLikedMaya:
    mc "I already told you that I like her..."
    if ep3_wearHelmet:
        scene ep3_derek_confront19 with dissolve
    elif True:
        scene ep3_derek_confront19b with dissolve
    de "..."
elif True:
    mc "I'm not into her...remember?"
    if ep3_wearHelmet:
        scene ep3_derek_confront17 with dissolve
    elif True:
        scene ep3_derek_confront17b with dissolve
    de "Then what the fuck was that about?"
    de "Just Hell Week stuff?"
    if ep3_wearHelmet:
        scene ep3_derek_confront18 with dissolve
    elif True:
        scene ep3_derek_confront18b with dissolve
    mc "Well... I don't know."
    if ep3_wearHelmet:
        scene ep3_derek_confront19 with dissolve
    elif True:
        scene ep3_derek_confront19b with dissolve
mc "Hey! I'm single, she's single."
mc "Things happen, you know?"
if ep3_wearHelmet:
    scene ep3_derek_confront20 with dissolve
elif True:
    scene ep3_derek_confront20b with dissolve
de "Ok, screw this. I don't want to fight."
de "Let's go cross some shit off that pledge board, before I slap you."
de "I already drank five beers this morning."
if ep3_wearHelmet:
    scene ep3_derek_confront21 with dissolve
elif True:
    scene ep3_derek_confront21b with dissolve
if ep3_drunkBeerMayaFreeroam:
    mc "Sweet, me too!"
mc "So, what do you wanna do?"
if ep3_wearHelmet:
    scene ep3_derek_confront20 with dissolve
elif True:
    scene ep3_derek_confront20b with dissolve
de "The gay guard catcher."
de "Let's get that one out of the way early and while we still have beers left to drink."
if ep3_wearHelmet:
    scene ep3_derek_confront21 with dissolve
elif True:
    scene ep3_derek_confront21b with dissolve
mc "Deal."
if ep3_wearHelmet:
    scene ep3_derek_confront20 with dissolve
    de "And pass the helmet! I've been wanting to wear that bad boy since yesterday."
    scene ep3_derek_confront21 with dissolve
    mc "I almost forgot I had it on me. It's not that bad to wear."
    mc "Well, except for the looks students give me..."
    mc "...and it does smell a bit."
    scene ep3_derek_confront31 with dissolve
    de "Did you ask someone to sit on your face, yet?"
    mc "Why would I?"
    scene ep3_derek_confront33 with dissolve
    de "Good. Then I still can use that one."
scene ep3_derek_confront20b with dissolve
de "And by the way..."
de "One of these days, I'm gonna fuck one of your sisters."
scene ep3_derek_confront21b with dissolve
mc "I'm an only child."
scene ep3_derek_confront20b with dissolve
de "Your mom, then."
scene ep3_derek_confront21b with dissolve
mc "She's been dead for a long time."
scene ep3_derek_confront38 with dissolve
stop music fadeout 3
de "Daddy, here I come."
mc "What?"
$ bios_history_derek += "Derek is very protective of Maya... He really didn't like seeing me kiss her.\n\n"
$ bios_name_derek = True
$ chat_new_bios = True

label ep3_ggc_label:
play music "music/ep3/get_back.mp3"
scene ep3_ggc with wipeleft
de "The list is not impossible! We can do it!"
scene ep3_ggc1 with dissolve
if ep3_hellWeekTryFuckJade:
    mc "But fucking a teacher..."
    mc "I know I said I'd do it, but it's such a risk."
    mc "If it gets out...think about the consequences."
elif True:
    mc "I already told you that I won't try to fuck her."
mc "And Jade, she seems so daring!"
mc "This morning, she flashed me!"
scene ep3_ggc2 with dissolve
de "Oh my God! It's history time!"
scene ep3_ggc3
de "One-two-three-GO!"
scene ep3_ggc4 with dissolve
mc "Get this! Chad attacks me last night, out of nowhere!"
scene ep3_ggc3 with dissolve
de "And then Jade showed you her pussy?"
scene ep3_ggc4 with dissolve
mc "No! Listen!"
mc "Jill comes and helps me; she even lets me sleep in her bed for the night."
scene ep3_ggc6 with dissolve
de "And...then...Jade showed you her pussy?"
mc "Not yet!"
scene ep3_ggc7 with dissolve
de "Just...get to the pussy part."
scene ep3_ggc4 with dissolve
mc "This morning, I got called into a counselors meeting. And guess who's in charge of that?"
scene ep3_ggc8 with dissolve
de "Jade! And her pussy!"
scene ep3_ggc9 with dissolve
mc "Well, no. Jade's husband, Professor Burke."
mc "Jade and Cathy were in there with us, too."
scene ep3_ggc10 with dissolve
de "This story sucks."
scene ep3_ggc9 with dissolve
mc "So, Cathy, Jade and this professor dude were all in there discussing with me and Chad about the assault."
mc "And Professor Burke even punished Chad by removing him as president of the tri-alphas!"
mc "And that's when it happened."
de "..."
mc "Jade...showed me her pussy..."
scene ep3_ggc12 with dissolve
de "Was it hairy?"
mc "That's your first question?"
mc "You didn't hear that Chad's not the tri-alpha president anymore?"
scene ep3_ggc14 with dissolve
de "Is she a natural blonde?"
mc "..."
mc "I don't remember. It was a pretty quick flash..."
mc "...but she definitely meant to do it!"
scene ep3_ggc with dissolve
de "Dude... You gotta go for it!"
scene ep3_ggc1 with dissolve
if ep3_hellWeekTryFuckJade:
    mc "How?"
elif True:
    mc "Come on... Stop it."
scene ep3_ggc17 with dissolve
de "[mc_de_up]... This is how I see it..."
de "She showed you her pussy..."
de "Now you show her yours."
scene ep3_ggc18 with dissolve
if dtype > 0:
    mc "I don't have a pussy."
elif True:
    mc "You want me to flash her back?"
scene ep3_ggc17 with dissolve
de "Just casually whip out your dick when you're talking to her."
de "You know...through the zipper or something."
scene ep3_ggc19
stop music
tm "Maggots! Look alive!"
scene ep3_ggc20 with dissolve
play music "music/ep3/hot_mustard.mp3"
de "Oh, shit! Oh, shit! We got one."
mc "He's the guy?"
de "He's fat, we're not. We should be able to outrun him."
scene ep3_ggc22 with wipeleft
mc "I'm nervous... If we get caught, we're in big trouble."
de "*{i}Muffled voice{/i}* That's why we have the balaclavas."
scene ep3_ggc23 with dissolve
mc "These aren't balaclavas..."
de "*{i}Muffled voice{/i}* Whatever! Ready?"
scene ep3_ggc24 with dissolve
de "Run for it!"
scene ep3_ggc25 with dissolve
$ renpy.pause()
scene ep3_ggc27 with dissolve
de "Yoo hoo! Mr. security guard!"
de "Come and get some!"
scene ep3_ggc28 with dissolve
de "Run!!!"
scene ep3_ggc29 with dissolve
sec "Oh, Lord, not this year, too! Have mercy!"
sec "Y-you...get back here!"
scene ep3_ggc31 with dissolve
dikcs "Hahaha!"
scene ep3_ggc32 with dissolve
mc "(Oh, fuck! Oh, fuck!)"
sec "Ugh...no...stop!"
scene ep3_ggc34 with dissolve
sec "Stop it!"
play sound "sound_effects/slap.mp3"
scene ep3_ggc35 with hpunch
ca "Ahh!!! What's happening!?"
ja "Oh my!"
scene ep3_ggc36 with dissolve
ja "Hahaha!"
ca "That's a first!"
scene ep3_ggc37 with dissolve
sec "Ok...*{i}Wheeze{/i}*"
sec "You've had your fun."
scene ep3_ggc38 with dissolve
$ renpy.pause()
scene ep3_ggc37 with dissolve
sec "Put your hands on your head and drop to your knees."
play sound "sound_effects/fart.mp3"
scene ep3_ggc40 with hpunch
"*{i}Farts{/i}*"
scene ep3_ggc40b with dissolve
sec "Ugh! What the-!"
scene ep3_ggc41 with dissolve
sec "*{i}Coughs{/i}* Oh my Lord! I can taste it!"
label ep3_diks_talk_label:
scene ep3_diks_talk with wipeleft
rs "That was a pretty impressive run."
rs "I'd say that my son was the star of that one."
tm "Are you serious? My son even took a slap during that run!"
scene ep3_diks_talk1 with dissolve
rs "You're right..."
rs "This one is too close to call."
scene ep3_diks_talk3 with dissolve
tm "Let's have the coin decide who gets most credit for this."
de "HEADS!"
tm "It's not that kind of a coin."
mc "You're right, it looks like an ancient Ionian coin to me."
tm "Get a load of this smartass."
play sound "sound_effects/coin.mp3"
scene ep3_diks_talk4 with vpunch
$ renpy.pause()
play sound "sound_effects/hand.mp3"
scene ep3_diks_talk5
tm "My son won the toss."
de "Aww..."
scene ep3_diks_talk6 with dissolve
rs "Hey, don't pout! That's one task you can cross off the board!"
scene ep3_diks_talk7 with dissolve
de "Hey, that's right! Our first completed task!"
play sound "sound_effects/slap.mp3"
scene ep3_diks_talk11 with hpunch
$ guideSuggestedPage = 75
de "Nice one, [mc_de]!"
menu:
    "Wear the Dildo helmet" if True:
        $ ep3_wearHelmet = True
        $ ep3_mallHelmet = True
        $ ep3_hellWeekHelmet += 1
        scene ep3_diks_talk11a with dissolve
        mc "Ok, gimme the helmet! I want it now!"
    "Let Derek keep it" if True:
        $ ep3_wearHelmet = False
        $ ep3_mallHelmet = False
        $ renpy.pause(0.5)
scene ep3_diks_talk12 with dissolve
tm "Ah...what a beautiful moment."
tm "Take a picture, Jamie."
scene ep3_diks_talk13 with dissolve
jm "*{i}Cliiiick{/i}*"
tm "What the fuck are you doing?"
scene ep3_diks_talk15 with dissolve
jm "Oh, I...uh...lost my phone."
scene ep3_diks_talk16 with dissolve
stop music fadeout 3
le "Hey, I've got this."
scene white
play sound "sound_effects/camera_shutter.mp3"
$ renpy.pause(0.5)

$ bios_history_mc += "Cathy slapped me at the mall when me and Derek were streaking.\n\n"
$ bios_history_mc += "I got the most credit for the gay guard catcher event during Hell Week.\n\n"
$ bios_name_mc = True
$ chat_new_bios = True

label ep3_jocks_talk_label:
play music "music/ep1/dont_count_on_me.mp3"
scene ep3_jocks_talk
dw "Hngn... Hngn... Almost..."
scene ep3_jocks_talk1 with dissolve
ar "Do you need some help?"
dw "No! I've almost got it."
scene ep3_jocks_talk with dissolve
dw "Come on, Li'l Dawie."
dw "Don't disappoint me."
scene ep3_jocks_talk3 with dissolve
dw "Ah! There we go! Yes!"
scene ep3_jocks_talk1 with dissolve
ar "Took you long enough."
dw "Hey! Most girls would kill for someone who lasts as long in bed as I do!"
ar "It doesn't count when most of the time is spent on getting your dick hard."
scene ep3_jocks_talk5 with dissolve
dw "Well, it's up now. And here it comes."
dw "I'll be gentle."
scene ep3_jocks_talk6 with dissolve
dw "Hm?"
dw "What the fuck...?"
dw "You're usually much tighter."
scene ep3_jocks_talk7 with dissolve
ar "I...um..."
ar "Are you sure?"
scene ep3_jocks_talk6 with dissolve
dw "Yeah! Right now it feels like I'm stirring my drink with a straw or something."
scene ep3_jocks_talk9 with dissolve
an "Dawe! Crisis alert!"
scene ep3_jocks_talk10 with dissolve
an "Oh... Hi, Ari."
ar "Hi, Big A!"
scene ep3_jocks_talk12 with dissolve
dw "What's happening?"
if ep3_chad_fight_won:
    scene ep3_jocks_talk13b with dissolve
elif True:
    scene ep3_jocks_talk13 with dissolve
ch "I fucked up. Big time."
ch "And now I'm getting suspended for it."
scene ep3_jocks_talk14 with dissolve
an "They're kicking you out of college?"
if ep3_chad_fight_won:
    scene ep3_jocks_talk15b with dissolve
elif True:
    scene ep3_jocks_talk15 with dissolve
ch "No, I still get one chance to keep my scholarship, but I can't be a part of the tri-alphas anymore."
scene ep3_jocks_talk16 with dissolve
dw "But what about our big competition next year!?"
dw "We were going to win!"
if ep3_chad_fight_won:
    scene ep3_jocks_talk15b with dissolve
elif True:
    scene ep3_jocks_talk15 with dissolve
ch "I know... Maybe there's a way for me to get back in, but it won't be for a while."
scene ep3_jocks_talk16 with dissolve
dw "That's bullshit! They can't do that!"
if ep3_chad_fight_won:
    scene ep3_jocks_talk15b with dissolve
elif True:
    scene ep3_jocks_talk15 with dissolve
ch "They can. I lost my cool and beat up that freshy, [name]."
scene ep3_jocks_talk16 with dissolve
dw "What the fuck did he do this time?"
if ep3_chad_fight_won:
    scene ep3_jocks_talk18bb with dissolve
elif True:
    scene ep3_jocks_talk18 with dissolve
ch "See for yourself."
ch "I think he's the one who snapped these."
scene ep3_jocks_talk19d with dissolve
dw "What the hell!?"
scene ep3_jocks_talk18b with dissolve
dw "This can't be real!"
scene ep3_jocks_talk19 with dissolve
dw "Is that my Arieth?"
if ep2_shotWon:
    if ep2_danceSage or ep2_fuckHOT:
        scene ep3_jocks_talk19b with dissolve
    elif True:
        scene ep3_jocks_talk19c with dissolve
elif True:
    scene ep3_jocks_talk19c with dissolve
dw "It is!"
scene ep3_jocks_talk20 with dissolve
dw "Has she fucked all of them?"
scene ep3_jocks_talk21 with dissolve
dw "There are just...so many DIKs!"
scene ep3_jocks_talk22 with dissolve
an "Wait! DIKs?"
an "Come on! It can't be him who took these."
an "Those two are clearly selfies."
scene ep3_jocks_talk22b with dissolve
an "And look at that one! Her hair is different."
an "These are way older than a week."
play sound "sound_effects/thud.mp3"
if ep3_chad_fight_won:
    scene ep3_jocks_talk23b with hpunch
elif True:
    scene ep3_jocks_talk23 with hpunch
ch "Yeah, I don't know. I wasn't thinking when I beat him up."
scene ep3_jocks_talk24 with dissolve
dw "I'm gonna kill them!"
if ep3_chad_fight_won:
    scene ep3_jocks_talk23b with dissolve
elif True:
    scene ep3_jocks_talk23 with dissolve
ch "That's the thing...you can't!"
ch "The counselors will be watching you guys from now on."
ch "I don't know for how long, but if you beat them up and they hear about it..."
ch "That's it for the tri-alphas."
ch "No more frat house, no more competition, no more parties, no more brotherhood."
if ep3_chad_fight_won:
    scene ep3_jocks_talk26b with dissolve
elif True:
    scene ep3_jocks_talk26 with dissolve
ch "And {b}you know{/b} what else they might find out if they're watching us closely..."
if ep3_chad_fight_won:
    scene ep3_jocks_talk27b with dissolve
elif True:
    scene ep3_jocks_talk27 with dissolve
an "Hey, what happens to you, now?"
if ep3_chad_fight_won:
    scene ep3_jocks_talk23b with dissolve
elif True:
    scene ep3_jocks_talk23 with dissolve
ch "I'll still see you guys at the gym and all..."
ch "I'm not gonna stop training for the competition."
ch "But for now, I just have to find someplace else to stay."
if ep3_chad_fight_won:
    scene ep3_jocks_talk27b with dissolve
elif True:
    scene ep3_jocks_talk27 with dissolve
an "What about Sage? I'm sure she'll help you."
if ep3_chad_fight_won:
    scene ep3_jocks_talk23b with dissolve
elif True:
    scene ep3_jocks_talk23 with dissolve
ch "Yeah, maybe..."
ch "...and you need to get yourselves a new president."
if ep3_chad_fight_won:
    scene ep3_jocks_talk29b with dissolve
elif True:
    scene ep3_jocks_talk29 with dissolve
an "Hey, that's you, Dawe."
if ep3_chad_fight_won:
    scene ep3_jocks_talk30b with dissolve
elif True:
    scene ep3_jocks_talk30 with dissolve
dw "Chad... Dude, I'm sorry."
dw "Thanks for sticking up for me."
if ep3_chad_fight_won:
    scene ep3_jocks_talk23b with dissolve
elif True:
    scene ep3_jocks_talk23 with dissolve
stop music fadeout 3
ch "I'm sorry for fucking up, guys."

label ep3_lunch_bella_label:
play music "music/ep2/journey_of_hope.mp3"
if ep3_wearHelmet:
    scene ep3_lunch_bella with wipeleft
    ash "That helmet is pretty disgusting."
    scene ep3_lunch_bella1 with dissolve
    de "Yeah, totally! Can you believe that this guy was gonna go around asking girls to sit on his face while wearing that?"
    scene ep3_lunch_bella with dissolve
    ash "Oh my God! Are you for real!?"
    mc "What!? That's what you sa-"
    scene ep3_lunch_bella3b with dissolve
    de "Totally not cool, [mc_de]."
    scene ep3_lunch_bella1 with dissolve
    mc "(He's obviously trying to impress Ashley...)"
    mc "(Using a very shitty strategy, but fine... I'll let him look good {b}for once{/b}.)"
elif True:
    scene ep3_lunch_bellab with wipeleft
    ash "Well I think you look cute in that helmet."
    ash "You kind of look like a baby seal with your big eyes."
    scene ep3_lunch_bella1b with dissolve
    de "*{i}Aueu aue aue{/i}*"
    scene ep3_lunch_bellab with dissolve
    ash "That was your impression of a baby seal? That's just weird."
    scene ep3_lunch_bella4b with dissolve
    de "I'm weird? You're the one watching nature programs with seals growing cocks on their heads."
    ash "Hahaha!"
    mc "(Wow, they haven't even talked to me once.)"
    mc "(I feel like a third wheel, right now.)"
$ bios_history_ashley += "She seems to like Derek.\n\n"
$ bios_name_ashley = True
$ bios_ashley = True
$ chat_new_bios = True

scene ep3_lunch_bella5 with dissolve
mc "(Bella...)"
mc "(I have an idea...)"
if ep3_wearHelmet:
    scene ep3_lunch_bella1 with dissolve
elif True:
    scene ep3_lunch_bellab with dissolve
mc "See you in math class, something came up."
mc "...whatever. Enjoy your date."

scene ep3_lunch_bella8 with dissolve
isa "And a coffee, please."
ll "That will be {color=#36ca2b}$${/color}."
if ep2_triedToKissBella:
    $ ep3_bella_counter = 1
elif True:
    $ ep3_bella_counter = 0
if ep2_peekedBella:
    $ ep3_bella_counter -= 1
show screen moneymsg
menu:
    "Pay for her meal ({color=#36ca2b}$${/color})" if money > 1:
        $ ep3_bella_counter += 1
        $ ep3_paidBellaMeal = True
        $ mny(-2)
        $ dk(-1)
        if ep1_maya_question_money and steamAchievements and not config.console and not config.developer:
            $ achievement.grant("ITSONME")
            init:
                $ achievement.register("ITSONME")
            $ achievement.Sync()
        scene ep3_lunch_bella10 with dissolve
        mc "Here, let me get that for you."
        hide screen moneymsg
        scene ep3_lunch_bella11 with dissolve
        isa "Why? You're up to something."
        scene ep3_lunch_bella12 with dissolve
        mc "I thought I could make up for ruining our date by buying you lunch."
    "Don't pay for her meal" if True:
        $ ep3_paidBellaMeal = False
        hide screen moneymsg
        scene ep3_lunch_bella12 with dissolve
        mc "I'd offer to pay for that, but I'm a bit short on money."
        mc "Student life ain't that luxurious."
        scene ep3_lunch_bella11 with dissolve
        isa "What do you want?"
        scene ep3_lunch_bella12 with dissolve
        mc "I thought I could make up for ruining our date by joining you for lunch."

if ep2_cafeteriaWorkerInsulted:
    $ ep3_bella_counter -= 1
    scene ep3_lunch_bella41 with dissolve
    ll "Look who's back!"
    ll "Are you enjoying our shitty, smelly food?"
    scene ep3_lunch_bella42 with dissolve
    mc "No... Stop it."
    scene ep3_lunch_bella41 with dissolve
    ll "You're not enjoying it, huh?"
    ll "If I wasn't working right now, I'd pour another drink over you."
elif ep1_insulted_cafeteria_worker:
    $ ep3_bella_counter -= 1
    scene ep3_lunch_bella41 with dissolve
    ll "Well, look who it is!"
    ll "Are you enjoying our smelly food?"
    scene ep3_lunch_bella42 with dissolve
    mc "What are you talking about?"
    scene ep3_lunch_bella41 with dissolve
    ll "Talking shit about the place I work and the food we cook..."
    ll "Pff! If I wasn't working right now, I'd slap you."
$ bios_beth = True
if ep1_insulted_cafeteria_worker or ep2_cafeteriaWorkerInsulted:
    scene ep3_lunch_bella43 with dissolve
    isa "..."
    mc "Sorry...where were we?"
    mc "Ah, yes! I wanted to make up for ruining our date."

if ep3_wearHelmet:
    scene ep3_lunch_bella13 with dissolve
elif True:
    scene ep3_lunch_bella13b with dissolve
isa "How many times do I have to reiterate!? It wasn't a {b}date{/b}."
isa "I'm a staff member. You're a student."
scene ep3_lunch_bella11 with dissolve
isa "And that is all this is."
if ep3_paidBellaMeal:
    scene ep3_lunch_bella14b with dissolve
    show screen moneymsg
    isa "And keep your money."
    $ mny(2)
    isa "I'm sure you can find a better use for it."
    hide screen moneymsg
scene ep3_lunch_bella12 with dissolve
mc "I still want to eat lunch with you."
scene ep3_lunch_bella11 with dissolve
isa "Only if you stop referring to anything we do together as a date."
scene ep3_lunch_bella12 with dissolve
mc "You got it."
play sound "sound_effects/shove.mp3"
if ep3_wearHelmet:
    scene ep3_lunch_bella17b2 with hpunch
elif True:
    scene ep3_lunch_bella17b with hpunch
mc "Oh..."

if ep1_beat_up_troy and ep1_beat_up_troy_won:
    $ ep3_bella_counter -= 2
    if ep3_wearHelmet:
        scene ep3_lunch_bella17c with dissolve
    elif True:
        scene ep3_lunch_bella17c2 with dissolve
    troy "What are you looking at? Gonna beat me up again?"
    mc "No... Sorry."
elif ep1_beat_up_troy:
    $ ep3_bella_counter -= 2
    if ep3_wearHelmet:
        scene ep3_lunch_bella17c with dissolve
    elif True:
        scene ep3_lunch_bella17c2 with dissolve
    troy "What are you looking at? Gonna start a fight with me again?"
    mc "No... Sorry."
elif True:
    if ep3_wearHelmet:
        scene ep3_lunch_bella17d with dissolve
    elif True:
        scene ep3_lunch_bella17d2 with dissolve
    troy "Sorry..."
    mc "Don't mention it..."
scene ep3_lunch_bella18 with dissolve
mc "So, Isabella..."
mc "Do you come here often?"
isa "..."
mc "It was a joke... You know...to lighten the mood."
scene ep3_lunch_bella20 with dissolve
isa "Yes, I eat here every day. It's the only restaurant that's close to work."
scene ep3_lunch_bella18 with dissolve
mc "Um... I said it was a joke."
scene ep3_lunch_bella20 with dissolve
isa "So was mine. Are you the only one who's allowed to tell them?"
scene ep3_lunch_bella18 with dissolve
mc "Oh! Haha. I didn't catch that...since you know..."
mc "...it lacked tone."
if ep3_wearHelmet:
    scene ep3_lunch_bella24 with dissolve
    isa "What's up with the hat? A new trend or something?"
    scene ep3_lunch_bella23 with dissolve
    mc "I'm just showcasing my personality."
    scene ep3_lunch_bella24 with dissolve
    isa "Ironic... With boys there's often the notion that the brain is found close to that thing."
    scene ep3_lunch_bella23 with dissolve
elif True:
    scene ep3_lunch_bella24b with dissolve
    isa "That's your friend over there...with the...hat?"
    scene ep3_lunch_bella23 with dissolve
    mc "Yeah, that's Derek."
mc "The helmet is part of our Hell Week. Hell Week is a kind of hazing process."
scene ep3_lunch_bella24 with dissolve
isa "I know what Hell Week is. It was a thing when I went to college, too."
scene ep3_lunch_bella23 with dissolve
mc "Oh, so they had it back then?"
scene ep3_lunch_bella26 with dissolve
isa "Back then?"
isa "How old do you think I am?"
scene ep3_lunch_bella26b with dissolve
mc "My dad taught me that you don't discuss a woman's age or weight."
scene ep3_lunch_bella26 with dissolve
isa "Apparently, I'm not only old but also fat."
scene ep3_lunch_bella23 with dissolve
mc "No! That's not what I meant."
scene ep3_lunch_bella20 with dissolve
isa "It was a joke."
scene ep3_lunch_bella18 with dissolve
mc "Hilarious... Thanks for making me sweat for nothing."
scene ep3_lunch_bella26 with dissolve
if ep3_wearHelmet:
    isa "So, you're going to wear that hat, all week?"
elif True:
    isa "So, he's going to wear that hat, all week?"
scene ep3_lunch_bella26b with dissolve
if ep3_wearHelmet:
    mc "No, I take turns with my friend Derek."
    scene ep3_lunch_bella34 with dissolve
    isa "Derek is your friend?"
elif True:
    mc "No, we take turns. He just happens to like it, so I let him wear it more."
    scene ep3_lunch_bella34b with dissolve
    isa "That sounds like Derek."
mc "You know him?"
isa "It's difficult to miss a shirtless student walking the hallways."
isa "Also, he's got quite the reputation among teachers, too."
scene ep3_lunch_bella26b with dissolve
mc "A reputation? Like what?"
scene ep3_lunch_bella26 with dissolve
isa "Like I would tell you that. You'd run off to him and spill the beans immediately."
scene ep3_lunch_bella26b with dissolve
mc "No, come on! I promise. What do they say?"
scene ep3_lunch_bella26 with dissolve
isa "I'm not telling you."
scene ep3_lunch_bella26b with dissolve
mc "If you tell me a secret, I'll tell you one."
scene ep3_lunch_bella26 with dissolve
isa "Are we resorting to manipulation now?"

scene ep3_lunch_bella18 with dissolve
mc "No, I was just looking to share things with you."
mc "Like you do during conversations."
mc "For instance, why did you want to have dinner with me in the first place?"
scene ep3_lunch_bella20 with dissolve
isa "Like I told you, I wanted to give you one chance to change my mind about you."
scene ep3_lunch_bella18 with dissolve
mc "So...have I?"
scene ep3_lunch_bella20 with dissolve
isa "No."
scene ep3_lunch_bella18 with dissolve
mc "Thanks...that's...blunt."
scene ep3_lunch_bella20 with dissolve
isa "I would have asked you about your background and tried to figure out if you find trouble or if trouble finds you."
scene ep3_lunch_bella26b with dissolve
mc "Oh, it's definitely the first one. No, wait, what were the options?"
isa "..."
scene ep3_lunch_bella26 with dissolve
isa "Have you been drinking?"
scene ep3_lunch_bella26b with dissolve
mc "There's really no winning with you."
mc "And, hey! You already know a bit about my background."
scene ep3_lunch_bella26 with dissolve
isa "You mean about your mom?"
scene ep3_lunch_bella26b with dissolve
mc "Exactly."
scene ep3_lunch_bella20 with dissolve
isa "I was looking for a little bit more than that."
scene ep3_lunch_bella18 with dissolve
mc "Oh, about my dad?"
scene ep3_lunch_bella20 with dissolve
isa "No! About {b}you{/b}."
scene ep3_lunch_bella18 with dissolve
mc "(She likes me...)"
isa "(God, he's so dense...)"
mc "Ok. I'm a straight, single guy who enjoys playing guitar and practicing martial arts."
scene ep3_lunch_bella20 with dissolve
isa "Great. Now try it again, without sounding like a personal ad."
scene ep3_lunch_bella26b with dissolve
mc "I don't get what you want me to say."
scene ep3_lunch_bella26 with dissolve
isa "Could the straight, single guy tell me about his past relationships?"
scene ep3_lunch_bella26b with dissolve
mc "There's really just been one."
mc "It's pretty personal..."
$ guideSuggestedPage = 76
scene ep3_lunch_bella20 with dissolve
isa "Share it with me and I'll share something about Derek's reputation."
scene ep3_lunch_bella18 with dissolve
stop music fadeout 3
menu:
    "Joke" if True:
        mc "Manipulation, huh? That's my kind of girl."
    "Just tell her" if True:
        $ renpy.pause(0.5)

label ep3_zoey_label:
play music "music/ep3/guitar_melancholy2.mp3"
scene ep3_zoey with dissolve
mc "{i}Um...well...{/i}"
mc "{i}When I was young, I had some really rough years.{/i}"
mc "{i}School wasn't very fun for me. I didn't have any friends and kids picked on me...a lot.{/i}"
isa "What for?"
mc "{i}You know...for being poor, not having the newest sneakers...oh...and, of course, for not having a mom.{/i}"
scene ep3_zoey2 with dissolve
mc "{i}My dad was worried about me after I came home one day from school...with bruises all over my arms.{/i}"
scene ep3_zoey1 with dissolve
mc "{i}The cool kids at school had this stupid challenge to see how many times they could punch me before I reacted.{/i}"
mc "{i}I was known as the kid who just sat there... I learned to take their insults and just ignore them...{/i}"
mc "{i}They didn't like that.{/i}"
scene ep3_zoey3 with dissolve
mc "{i}After that, dad taught me how to fight...well, he taught himself, too.{/i}"
mc "{i}He had never done it before and he could barely afford the training gear.{/i}"
mc "{i}His usual hobbies were a bit less action-filled...{/i}"
mc "{i}Like solving crossword puzzles, meditation, collecting stamps and coins, reading and of course...home improvement.{/i}"
mc "{i}You see, he's a carpenter, so he really enjoys that sort of thing.{/i}"
scene ep3_zoey2b with dissolve
mc "{i}We practiced almost daily and I could feel how I got a real confidence boost from it.{/i}"
mc "{i}Dad made me promise to never use what he taught me for anything other than self-defense.{/i}"
mc "{i}I guess by doing that he imparted good morals and to not become a bully myself.{/i}"
mc "{i}For me, training was a great way to bond with my dad. I never wanted to fight anyone.{/i}"
scene ep3_zoey4 with dissolve
mc "{i}Until one day...when I didn't have a choice.{/i}"
mc "{i}I could sense how that punch was coming my way.{/i}"
play sound "sound_effects/hit.mp3"
scene ep3_zoey5 with hpunch
mc "{i}But the boy throwing it never saw mine coming right back at him.{/i}"
mc "{i}In self-defense, I beat him.{/i}"
scene ep3_zoey6 with dissolve
mc "{i}I beat him so hard that my fists got blood all over them.{/i}"
mc "{i}The other kids did nothing. They just stood there on the sidelines and stared.{/i}"
mc "{i}They watched me hit their friend. Repeatedly.{/i}"
scene ep3_zoey7 with dissolve
mc "{i}Until eventually a teacher came and broke it up.{/i}"
mc "{i}You think that a teacher would side with the victim.{/i}"
mc "{i}But when there are so many voices against one...{/i}"
mc "{i}...it's hard to make yours heard.{/i}"
scene ep3_zoey8 with dissolve
mc "{i}Apparently, I wasn't the victim.{/i}"
mc "{i}The parents of the boy I beat up wanted to press charges against my dad for teaching me how to fight.{/i}"
mc "{i}Luckily for me and my dad, they never did.{/i}"
mc "{i}I was even lucky enough to not be sent to juvenile hall.{/i}"
scene ep3_zoey9 with dissolve
mc "{i}But I got my punishment for standing up for myself. Detention.{/i}"
mc "{i}Every day for two whole months.{/i}"
mc "{i}And that's how I met her.{/i}"
scene ep3_zoey10 with dissolve
mc "{i}Zoey.{/i}"
mc "{i}She was a bit like me. An outcast.{/i}"
mc "{i}That's probably why we got along so well.{/i}"
scene ep3_zoey11 with dissolve
mc "{i}Zoey was in detention for smoking during class...{/i}"
mc "{i}...that pretty much sums her attitude up.{/i}"
mc "{i}Her looks were...rugged... That's not a word usually used to describe a girl...but she was.{/i}"
scene ep3_zoey12 with dissolve
mc "{i}She wore dirty clothes, her hair was a mess and she had a self-pierced nose.{/i}"
mc "{i}We were the only ones in detention.{/i}"
mc "{i}And the supervisor just left us alone for most of the time.{/i}"
scene ep3_zoey13 with dissolve
mc "{i}So, naturally, we got to talking.{/i}"
mc "{i}By that I mean, she talked and I listened.{/i}"
mc "{i}She became my first real friend.{/i}"
mc "{i}A girl as a best friend.{/i}"
scene ep3_zoey14 with dissolve
mc "{i}Zoey taught me a lot of things...{/i}"
mc "{i}Like how to smoke and stand on a skateboard.{/i}"
mc "{i}I didn't like smoking and my balance wasn't meant for skateboarding...{/i}"
scene ep3_zoey15 with dissolve
mc "{i}...but I blindly did those things...{/i}"
mc "{i}It was always fun being with her.{/i}"
label zoey_lewd_label:
if _in_replay:
    play music "music/ep3/guitar_melancholy2.mp3"
    hide screen phone_screen
    if persistent.name == None:
        $ name = "MC"
    elif True:
        $ name = persistent.name
scene ep3_zoey15b with Dissolve(2.0)
mc "{i}As we grew up, our...pastime activities...changed...{/i}"
scene ep3_zoey15c with dissolve
mc "{i}She had a friend with an older brother who would buy them alcohol.{/i}"
mc "{i}She would share it with me...{/i}"
scene ep3_zoey16 with dissolve
mc "{i}And one night, we were partying together in a tree house.{/i}"
scene ep3_zoey16b with dissolve
mc "{i}I don't even remember whose tree house it was...but we were in it...drinking and having a good time.{/i}"
scene ep3_zoey17 with dissolve
mc "{i}At one moment, our eyes met and there was this awkward silence...{/i}"
mc "{i}For the first time in my life...{/i}"
scene ep3_zoey18 with dissolve
mc "{i}I got kissed.{/i}"
mc "{i}My best friend, for all those years...kissed me.{/i}"
mc "{i}Our relationship shifted...from being a friendship...{/i}"
scene ep3_zoey18b with dissolve
mc "{i}...into something more.{/i}"
mc "{i}We had no clue what we were doing. At first, we thought it was something fun to do while being drunk.{/i}"
scene ep3_zoey19 with dissolve
mc "{i}But then we started doing it when we were sober.{/i}"
scene ep3_zoey20 with dissolve
mc "{i}And it also led to more than just kissing.{/i}"
scene anim_zoey_ride1_ep3 with dissolve
mc "{i}But I'm not sure if it was love.{/i}"
mc "{i}I mean, she was my best friend.{/i}"
scene anim_zoey_ride2_ep3 with dissolve
mc "{i}I already loved her for that...but real love...?{/i}"
mc "{i}What does that even mean?{/i}"
mc "{i}No... I don't think it was real love.{/i}"
scene ep3_zoey25 with dissolve
mc "{i}Not long ago, she left town for San Diego. She wanted to become a surfer.{/i}"
mc "{i}She asked me to come with her, but I chose to stay with my dad and finish high school.{/i}"
mc "{i}It was the smart thing to do.{/i}"
scene ep3_zoey26 with dissolve
mc "{i}I guess I really didn't see her as a girlfriend until that point when we said our goodbyes to each other.{/i}"
mc "{i}It actually hurt...a lot.{/i}"
mc "{i}But once again, I wasn't completely sure if I was sad for losing my best friend...or for losing something more.{/i}"
scene ep3_zoey27 with dissolve
mc "{i}We stayed in touch on social media. I saw that she got a new boyfriend.{/i}"
scene ep3_zoey27b with dissolve
mc "{i}She also got herself a bunch of tattoos and really seemed happy and living life.{/i}"
mc "{i}Now it's been six months since our last message to each other.{/i}"
$ renpy.end_replay()
$ persistent.ep3_lewd_zoey = True
$ calcScenes()
mc "{i}Since that, I've moved on and even managed to fall for a girl at my summer job...{/i}"
mc "{i}But here we are right now...{/i}"
scene black with dissolve
mc "...and I'm not sure what I'm doing, at all."
mc "Lately, I seem to get crushes easily..."
mc "...but what I think it really is..."
mc "...is that I'm trying to find myself and what I want in life."
$ bios_zoey = True
$ chat_new_bios = True

stop music fadeout 3
label ep3_bella_lunch_continued_label:
scene ep3_lunch_bella55 with dissolve
mc "..."
mc "Was that story what you wanted to hear?"
play music "music/ep2/journey_of_hope.mp3"
isa "..."
scene ep3_lunch_bella55b with dissolve
isa "That was..."
isa "...very revealing."
scene ep3_lunch_bella55 with dissolve
mc "So, what's Derek's reputation?"
scene ep3_lunch_bella58 with dissolve
ca "[name]? Are you joining us for lunch, today? How nice!"
ja "If it isn't my favorite student. [name]... I'm glad to see you."
scene ep3_lunch_bella60 with dissolve
isa "[name] is in both of your classes?"
ca "He's actually in two of mine and surprisingly also in one of Jade's classes."
scene ep3_lunch_bella62 with dissolve
ja "Surprisingly? Listen to you. It's {b}refreshing{/b}, that's what it is!"
ca "My bad! You're absolutely right!"
ca "It is refreshing to see a young man attend Gender Studies."
ca "It's very modern."
if failedEnglish + failedMath <= 1:
    $ ep3_bella_counter += 2
    ca "And he's such an excellent student!"
elif failedEnglish + failedMath <= 3:
    $ ep3_bella_counter += 1
    ca "And he's a very good student."

scene ep3_lunch_bella63 with dissolve
ja "Look at us, we're embarrassing the poor boy."
scene ep3_lunch_bella63b with dissolve
mc "(This woman really wants me...)"
scene ep3_lunch_bella60 with dissolve
ca "Isabella, do you wanna join in?"
isa "I think he's had enough."
if ep3_wearHelmet:
    $ ep3_bella_counter -= 1
    scene ep3_lunch_bella65 with dissolve
    ja "Cathy? Is it just me or does that helmet ring any bells?"
    ca "*{i}Gasps{/i}*"
    scene ep3_lunch_bella66 with dissolve
    ca "[name]! I know we give fraternity hazing some leeway but running naked through a mall is not ok!"
    scene ep3_lunch_bella66b with dissolve
    menu:
        "Tell them it was Derek" if True:
            mc "It...wasn't me...it was Derek."
            mc "We take turns wearing the helmet."
            scene ep3_lunch_bella63 with dissolve
            ja "Aha, so you were the well-endowed streaker. Got it."
            mc "No, that's not what I said..."
        "Stay silent" if True:
            mc "..."
elif True:
    scene ep3_lunch_bella65b with dissolve
    ja "Cathy? Look. Is it just me or does that helmet ring any bells?"
    ca "*{i}Gasps{/i}*"
    ja "Typical Derek! As if walking around without a shirt on wasn't enough for him."
    ja "Now he's going around exposing himself in malls."
    ca "We should have a word with him."
    scene ep3_lunch_bella62 with dissolve
    ja "Yes, and find out who his naked friend was, too."
scene ep3_lunch_bella71 with dissolve
ca "Leaving so soon?"
isa "Something came up."
$ bios_history_isabella += "I had lunch with Bella and I told her about my past.\n\n"
$ bios_name_isabella = True
$ chat_new_bios = True
if ep3_bella_counter < 0:
    $ ep3_bella_came_around = False
    $ RPisabella -= 1
elif True:
    $ ep3_bella_came_around = True
    $ RPisabella += 2
scene ep3_lunch_bella73 with dissolve
ca "How are things with you since this morning, [name]?"
ja "Yes! How are you?"
scene ep3_lunch_bella63b with dissolve
menu:
    "Place a hand on her thigh" if True:
        $ ep3_handOnJadesThigh = True
        $ dk(1)
        scene ep3_lunch_bella76 with dissolve
        mc "I'm fine..."
        scene ep3_lunch_bella77 with dissolve
        ja "(Well, this was a pleasant surprise...)"
        ja "(God...this boy makes me feel like I'm 18 years old and attractive, again.)"
        scene ep3_lunch_bella78 with dissolve
        mc "(Oh, shit... She's really doing that now!?)"
        $ bios_history_jade += "I flirted with Jade under the table in the cafeteria.\n\n"
        $ bios_name_jade = True
        $ chat_new_bios = True
    "Do nothing" if True:
        $ ep3_handOnJadesThigh = False
        $ dk(-1)
        mc "I'm fine..."
        $ bios_history_jade += "I didn't flirt with Jade under the table in the cafeteria.\n\n"
        $ bios_name_jade = True
        $ chat_new_bios = True
scene ep3_lunch_bella81 with dissolve
ca "I really hope that we can help you for the better."
ca "We will be watching out for you to the best of our abilities."
if ep3_handOnJadesThigh:
    scene ep3_lunch_bella80 with dissolve
    ja "Most certainly. We will take care of you."
scene ep3_lunch_bella79 with dissolve
ca "Jill is such a sweet girl. Always wanting the best for people."
ca "I hope you thanked her for the help."
scene ep3_lunch_bella82 with dissolve
mc "I...uh...didn't ask to be helped."
mc "It kind of puts me into a weird spot."
scene ep3_lunch_bella81 with dissolve
ca "Trust me, in the long run, it's better that things like this are brought to the surface."
if ep3_handOnJadesThigh:
    scene ep3_lunch_bella80 with dissolve
    mc "(This...is surreal.)"
sb "What's this?"
scene ep3_lunch_bella84 with dissolve
sb "It looks like a student-teacher lunch, to me."
ca "Hi, Professor."
if ep3_handOnJadesThigh:
    scene ep3_lunch_bella80 with dissolve
    mc "(What the hell? She's squeezing even harder now!)"
    mc "(It's starting to hurt...)"
    scene ep3_lunch_bella85 with dissolve
    mc "(Enough of this...)"
scene ep3_lunch_bella86 with dissolve
mc "I was just leaving, thanks for the company."
stop music fadeout 3
ca "I'll see you in class soon, [name]."

label ep3_math_label:
play music "music/ep1/someways.mp3"
if ep3_wearHelmet:
    scene ep3_math_1 with wipeleft
elif True:
    scene ep3_math_1b with wipeleft
mc "Hey...look at Derek and that girl...Ashley..."
my "What about them?"
mc "Don't they hang out a lot?"
my "You mean like you and me?"
scene ep3_math_3 with dissolve
mc "Yeah, exactly."
scene ep3_math_4 with dissolve
my "He's never mentioned her to me before."
my "Also, he's kind of a ladies' man."
my "...or...let's be honest...ladies' {b}boy{/b}."
scene ep3_math_3 with dissolve
mc "Ah, a ladyboy, gotcha."
scene ep3_math_6 with dissolve
my "Hahaha! No! Stop it!"
my "That's not what I said."
scene ep3_math_3 with dissolve
mc "So, he's always surrounded himself with girls?"
scene ep3_math_4 with dissolve
my "He's {b}tried{/b} to do that, yes."
my "He's not often successful."
my "But he believes that rejection is the key to success."
my "He read it in a book..."
my "Which is funny... Because I never saw him read anything besides comic books or dad's secret magazines."
scene ep3_math_9 with dissolve
my "Like if he doesn't try with a girl, he definitely won't score..."
my "And the worst thing that happens if he does try, is that he'll get a no."
my "So, he tries...a lot."
if ep3_wearHelmet:
    scene ep3_math_1 with dissolve
elif True:
    scene ep3_math_1b with dissolve
my "And it does look like he's trying with this one, now that you mention it."
if ep3_wearHelmet:
    scene ep3_math_10 with dissolve
elif True:
    scene ep3_math_10b with dissolve
my "You know what...strike that."
if ep3_wearHelmet:
    scene ep3_math_11 with dissolve
elif True:
    scene ep3_math_11b with dissolve
play sound "sound_effects/camera_shutter.mp3"
de "*{i}Coughs{/i}* *{i}Click{/i}*"
my "Yeah...definitely strike that."
play sound "sound_effects/message.mp3"
scene ep3_math_12 with dissolve
mc "(From Derek, huh...)"
mc "(I can probably guess what this is...)"
$ renpy.pause()
mc "(Yep...I knew it.)"
scene ep3_math_14 with dissolve
mc "(!!!)"
ca "How many times do I need to tell you that phones should be turned off when you're in class?"
scene ep3_math_16 with dissolve
ca "..."
mc "(OH NO!!!)"
scene ep3_math_14 with dissolve
ca "Turn it off...ok?"
if ep3_wearHelmet:
    scene ep3_math_18 with dissolve
elif True:
    scene ep3_math_18b with dissolve
de "(I'M SORRY!)"
if minigames:
    stop music fadeout 3
scene ep3_math_cathy1 with dissolve
ca "T-time for a pop quiz, today!"
scene ep3_math_cathy2 with dissolve
dw "That's fucking bullshit!"
$ guideSuggestedPage = 77
scene ep3_math_cathy3 with dissolve
ca "Language, Dawe."
$ bios_history_cathy += "Cathy saw Derek's embarrassing text on my phone! She was blushing as she walked away.\n\n"
$ bios_name_cathy = True
$ chat_new_bios = True
if not minigames:
    scene black with Fade(1.5, 1, 0.5)
    jump ep3_after_math_test
play music "music/ep3/sing_along_with_jim.mp3"
scene desk_bg_test with wipeleft
jump math101_test3

label ep3_after_math_test:
$ renpy.block_rollback()
if minigames:
    scene ep3_math_after with wiperight
    stop music fadeout 3
elif True:
    scene ep3_math_after with fade
ca "(...)"
if minigames:
    play music "music/ep1/golden_alley.mp3"
ca "(\"Maybe you should try to fuck her?\")"
ca "(I...I'm not sure if I should feel offended or flattered.)"
ca "(Probably a bit of both.)"
ca "(I try to dress professionally and this is what I get?)"
scene ep3_math_aftera with dissolve
ca "(Young men seeing me as someone...sexual?)"
ca "(No, Cathy! {b}Students{/b} seeing you as someone sexual.)"
ca "(I'm twice his age...)"
ca "(That can absolutely not happen.)"
scene ep3_math_afterb with dissolve
ca "(Although, it's funny how men see me as attractive in real life...)"
ca "(...while there are slim pickings online.)"
ca "(Maybe it's my photos?)"
ca "(The other women on this site sure love to show cleavage in their profile pictures.)"
scene ep3_math_afterc with dissolve
ca "(A little bit of cleavage would probably not hurt.)"
ca "(Haha... Is it weird that I get a bit excited by thinking of that?)"
ca "(Showing strangers on the internet more of myself...)"
ca "(Oh, Cathy... Save it for the bathtub.)"
scene ep3_math_afterd with dissolve
ca "(...)"
ca "(Yes. Save it for the bathtub.)"
scene ep3_math_afterf with dissolve
ca "Ok, class. You may turn in your tests now."
play sound "sound_effects/shove.mp3"
if ep3_wearHelmet:
    scene ep3_math_after1 with hpunch
elif True:
    scene ep3_math_after1b with hpunch
$ renpy.pause()
scene ep3_math_after2 with dissolve
dw "..."
mc "(What...for real?)"
scene ep3_math_after4 with dissolve
mc "(Oh, right... It's probably because of Chad...)"
mc "(Cathy's watching them closer now.)"
if ep3_wearHelmet:
    scene ep3_math_after5b with dissolve
elif True:
    scene ep3_math_after5 with dissolve
de "[mc_de_up]... Sorry about that text."
if ep3_wearHelmet:
    scene ep3_math_after6b with dissolve
elif True:
    scene ep3_math_after6 with dissolve
menu:
    "Don't worry" if True:
        mc "Don't worry about it."
        if ep3_wearHelmet:
            scene ep3_math_after5b with dissolve
        elif True:
            scene ep3_math_after5 with dissolve
        de "No. No. I fucked up."
        de "And I'm sorry..."
        if ep3_wearHelmet:
            scene ep3_math_after8b with dissolve
        elif True:
            scene ep3_math_after8 with dissolve
        de "But did you see her ass?"
        if ep3_wearHelmet:
            scene ep3_math_after6b with dissolve
        elif True:
            scene ep3_math_after6 with dissolve
        mc "Yeah, I saw it."
        if ep3_wearHelmet:
            scene ep3_math_after8b with dissolve
        elif True:
            scene ep3_math_after8 with dissolve
        de "And!?"
        if ep3_wearHelmet:
            scene ep3_math_after6b with dissolve
        elif True:
            scene ep3_math_after6 with dissolve
        $ RPderek += 1
        mc "..."
        mc "It was very hot..."
        if ep3_wearHelmet:
            scene ep3_math_after8b with dissolve
        elif True:
            scene ep3_math_after8 with dissolve
        de "Hell yeah!"
    "That was stupid" if True:
        mc "That was really stupid!"
        mc "You got me into trouble with her."
        if ep3_wearHelmet:
            scene ep3_math_after5b with dissolve
        elif True:
            scene ep3_math_after5 with dissolve
        de "Yep, I did. I fucked up."
        de "And I'm sorry..."
        if ep3_wearHelmet:
            scene ep3_math_after8b with dissolve
        elif True:
            scene ep3_math_after8 with dissolve
        de "But did you see her ass?"
        if ep3_wearHelmet:
            scene ep3_math_after6b with dissolve
        elif True:
            scene ep3_math_after6 with dissolve
        mc "Yeah, I saw it."
        if ep3_wearHelmet:
            scene ep3_math_after8b with dissolve
        elif True:
            scene ep3_math_after8 with dissolve
        de "And!?"
        if ep3_wearHelmet:
            scene ep3_math_after6b with dissolve
        elif True:
            scene ep3_math_after6 with dissolve
        menu:
            "It was hot" if True:
                $ RPderek += 1
                mc "..."
                mc "It was very hot..."
                if ep3_wearHelmet:
                    scene ep3_math_after8b with dissolve
                elif True:
                    scene ep3_math_after8 with dissolve
                de "Hell yeah!"
            "Fuck you" if True:
                mc "And fuck you!"
                mc "Don't pull that shit again!"
if ep3_wearHelmet:
    scene ep3_math_after5b with dissolve
elif True:
    scene ep3_math_after5 with dissolve
de "I saw you bump into Dawe..."
de "I was kind of expecting something to happen."
if ep3_wearHelmet:
    scene ep3_math_after6b with dissolve
elif True:
    scene ep3_math_after6 with dissolve
mc "You know, I was just thinking the same thing."
mc "After the counselors meeting this morning..."
mc "Chad may have told the alphas to back off, since Professor Burke told him they'd watch them closely from now on."
if ep3_wearHelmet:
    scene ep3_math_after8b with dissolve
elif True:
    scene ep3_math_after8 with dissolve
de "You do realize what this means?"
if ep3_wearHelmet:
    scene ep3_math_after6b with dissolve
elif True:
    scene ep3_math_after6 with dissolve
mc "No, what?"
if ep3_wearHelmet:
    scene ep3_math_after8b with dissolve
elif True:
    scene ep3_math_after8 with dissolve
de "We can fuck with them in the open without being worried about the consequences!"
if ep3_wearHelmet:
    scene ep3_math_after6b with dissolve
elif True:
    scene ep3_math_after6 with dissolve
mc "I wouldn't take it that far. Who knows how they will act when there's no one around?"
mc "Also, just because we're not alphas, doesn't mean we're immune to punishment."
if ep3_wearHelmet:
    scene ep3_math_after16b with dissolve
elif True:
    scene ep3_math_after16 with dissolve
de "But we do need to prank them."
if ep3_wearHelmet:
    scene ep3_math_after6b with dissolve
elif True:
    scene ep3_math_after6 with dissolve
mc "Yeah, I know... It's tricky... Do you have any ideas?"
if ep3_wearHelmet:
    scene ep3_math_after16b with dissolve
elif True:
    scene ep3_math_after16 with dissolve
de "Did you see his shaker?"
if ep3_wearHelmet:
    scene ep3_math_after6b with dissolve
elif True:
    scene ep3_math_after6 with dissolve
mc "What about it?"
if ep3_wearHelmet:
    scene ep3_math_after8b with dissolve
elif True:
    scene ep3_math_after8 with dissolve
de "What if we add some extra protein to it?"
de "You know...CUM-petition style..."
if ep3_wearHelmet:
    scene ep3_math_after6b with dissolve
elif True:
    scene ep3_math_after6 with dissolve
mc "That would definitely be a prank..."
mc "But I'm not gonna stick my cock in that shaker."
if ep3_wearHelmet:
    scene ep3_math_after8b with dissolve
elif True:
    scene ep3_math_after8 with dissolve
de "You don't have to! We fill a condom with some love juice..."
de "One of us distracts him and the other one just plops it in there."
if ep3_wearHelmet:
    scene ep3_math_after6b with dissolve
elif True:
    scene ep3_math_after6 with dissolve
mc "It's a very risky plan..."
if ep3_wearHelmet:
    scene ep3_math_after16b with dissolve
elif True:
    scene ep3_math_after16 with dissolve
$ guideSuggestedPage = 78
de "I'm gonna have to do it all by myself, huh?"
if ep3_wearHelmet:
    scene ep3_math_after6b with dissolve
elif True:
    scene ep3_math_after6 with dissolve
menu:
    "Do it" if True:
        $ dk(1)
        $ ep3_dawe_prank = True
        mc "Don't assume that. I've got this..."
        mc "...but you'll have to help me, somehow."
        if ep3_wearHelmet:
            scene ep3_math_after8b with dissolve
        elif True:
            scene ep3_math_after8 with dissolve
        de "Tomorrow. English class."
        stop music fadeout 3
        de "You bring the balls, I bring the goo."
        $ bios_history_mc += "I told Derek I wanted to prank Dawe.\n\n"
        $ bios_name_mc = True
        $ chat_new_bios = True
    "Let Derek do it" if True:
        $ dk(-1)
        $ ep3_dawe_prank = False
        mc "Not all by yourself...I can get the proof..."
        mc "We still need that, you know."
        if ep3_wearHelmet:
            scene ep3_math_after8b with dissolve
        elif True:
            scene ep3_math_after8 with dissolve
        de "Great. Tomorrow. English class."
        stop music fadeout 3
        de "I'm gonna fill that shaker up to the brim."
        $ bios_history_mc += "I convinced Derek to prank Dawe.\n\n"
        $ bios_name_mc = True
        $ chat_new_bios = True

label ep3_jill_isa_label:
scene ep3_isa_jill with fade
play music "music/ep1/fresh_air.mp3"
ji "Bella!"
scene ep3_isa_jill1 with dissolve
isa "Jill? What's wrong?"
ji "I need you..."
isa "Come with me."
scene ep3_isa_jill3 with dissolve
isa "What happened? You look upset."
ji "It's [name]..."
scene ep3_isa_jill5 with dissolve
isa "What did he do to you!?"
scene ep3_isa_jill4 with dissolve
ji "He didn't do anything to me. He got beat up last night."
scene ep3_isa_jill6 with dissolve
isa "He got beat up? I just had lunch with him...he seemed ok."
scene ep3_isa_jill4 with dissolve
ji "Yeah, I know. I helped him, but I'm not sure I did him a favor..."
ji "I may have gotten him into more trouble by reporting it to the guidance counselors."
scene ep3_isa_jill4b with dissolve
ji "The student who beat him up might hold a grudge..."
ji "[name] wasn't happy about what I did..."
ji "I hope I didn't paint a giant target on his back."
scene ep3_isa_jill4 with dissolve
ji "I just did what I wished people would have done for me, you know?"
scene ep3_isa_jill10 with dissolve
isa "I know."
scene ep3_isa_jill4 with dissolve
ji "So, what do I do now? I can't just let it be, right?"
ji "I have to fix this, somehow."
scene ep3_isa_jill10 with dissolve
isa "You've done enough."
isa "Seeing as he got into trouble before you helped him, you did the right thing."
if ep3_bella_came_around:
    if not persistent.bg_isa_alt_unlocked:
        $ persistent.bg_isa_alt_unlocked = True
        $ chat_new_bg = True
        $ calcWallpapers()
    scene ep3_isa_jill13 with dissolve
    isa "He's been unlucky...or chosen his friends poorly, I should say."
    ji "Huh?"
    scene ep3_isa_jill14 with dissolve
    ji "I thought you didn't like him."
    ji "What made you change your mind, all of a sudden?"
    scene ep3_isa_jill15 with dissolve
    isa "I had a talk with him."
    scene ep3_isa_jill16 with dissolve
    ji "And? You like him now?"
    scene ep3_isa_jill15 with dissolve
    isa "No. Not at all."
    scene ep3_isa_jill14 with dissolve
    ji "But?"
    scene ep3_isa_jill15 with dissolve
    isa "But he's not all bad."
    scene ep3_isa_jill17 with dissolve
    ji "Not all bad?"
    ji "You know, that's the nicest thing you've ever said about a guy."
    scene ep3_isa_jill18 with dissolve
    isa "..."
    ji "I think you might be right."
    scene ep3_isa_jill15 with dissolve
    isa "Good. So, go ahead."
    scene ep3_isa_jill14 with dissolve
    ji "Go ahead and...befriend him?"
    scene ep3_isa_jill15 with dissolve
    isa "Yeah, that or date him. Whatever."
    scene ep3_isa_jill16 with dissolve
    ji "Date him?"
elif True:
    scene ep3_isa_jill13 with dissolve
    isa "He's not just unlucky like you were, Jill. He's actively looking for trouble."
    ji "Huh?"
    scene ep3_isa_jill12b with dissolve
    isa "I had a talk with him... I wanted to give him a chance, you know, for you."
    isa "But the way he's acting..."
    scene ep3_isa_jill15 with dissolve
    isa "I hoped it was different, but as it is, right now..."
    isa "...he's still just a boy."
    scene ep3_isa_jill14 with dissolve
    ji "You gave him a chance...for me?"
    ji "Why?"
    scene ep3_isa_jill15 with dissolve
    isa "I wanted to make sure if he was good enough for you..."
    isa "To befriend...or to date...or whatever."
    scene ep3_isa_jill16 with dissolve
    ji "To date?"
ji "I'm not sure I'm looking for someone to date..."
ji "Did you think I was?"
scene ep3_isa_jill15 with dissolve
isa "Well, you're a woman. Stranger things have happened."
scene ep3_isa_jill17 with dissolve
ji "Haha, yeah, but still..."
scene ep3_isa_jill14 with dissolve
ji "I mean...I can feel how Tybalt is trying to win me over..."
ji "He seems to believe that we belong together..."
scene ep3_isa_jill15 with dissolve
if ep3_bella_came_around:
    isa "[name] is a way better choice than Tybalt. That's for sure."
    scene ep3_isa_jill14 with dissolve
    ji "[name] must really have impressed you. I'm stunned."
elif True:
    isa "[name] is not a good choice..."
    isa "...but he's a way better choice than Tybalt. That's for sure."
    scene ep3_isa_jill14 with dissolve
    ji "So, you kind of like [name]?"
scene ep3_isa_jill12b with dissolve
isa "No. I just really hate Tybalt."
stop music fadeout 3
scene ep3_isa_jill24f with dissolve
ji "Hahaha! Never change, Bella."

label ep3_march_label:
play music "music/ep3/lets_begin.mp3"
if ep3_wearHelmet:
    scene ep3_marchb with wipeleft
elif True:
    scene ep3_march with wipeleft
mc "A strip club?"
if ep3_wearHelmet:
    scene ep3_march0b with dissolve
elif True:
    scene ep3_march0 with dissolve
tm "A strip club."
if ep3_wearHelmet:
    scene ep3_marchb with dissolve
elif True:
    scene ep3_march with dissolve
mc "Tonight?"
if ep3_wearHelmet:
    scene ep3_march0b with dissolve
elif True:
    scene ep3_march0 with dissolve
tm "Tonight."
if ep3_wearHelmet:
    scene ep3_marchb with dissolve
elif True:
    scene ep3_march with dissolve
mc "I'm not 21."
if ep3_wearHelmet:
    scene ep3_march0b with dissolve
elif True:
    scene ep3_march0 with dissolve
tm "We're fully aware."
if ep3_wearHelmet:
    scene ep3_marchb with dissolve
elif True:
    scene ep3_march with dissolve
mc "And that's not a problem?"
if ep3_wearHelmet:
    scene ep3_march0b with dissolve
elif True:
    scene ep3_march0 with dissolve
tm "Only if you make it one."
if ep3_wearHelmet:
    scene ep3_marchb with dissolve
elif True:
    scene ep3_march with dissolve
mc "What does that mean?"
if ep3_wearHelmet:
    scene ep3_march00b with dissolve
elif True:
    scene ep3_march00 with dissolve
tm "Just show up, shut up and watch the naked ladies."
if ep3_wearHelmet:
    scene ep3_march0db with dissolve
elif True:
    scene ep3_march0d with dissolve
rs "And get your dick signed."
if ep3_wearHelmet:
    scene ep3_march00b with dissolve
elif True:
    scene ep3_march00 with dissolve
tm "Oh, yeah!"
tm "And get your dick signed!"
scene ep3_march0e with dissolve
jac "Hey! Hey! Bros! Here they come!"
if ep3_wearHelmet:
    scene ep3_march0f with dissolve
elif True:
    scene ep3_march0f2 with dissolve
mc "What's happening?"
tm "Shh! Shut up and watch."
de "What are we looking at?"
rs "This happens every semester."
scene ep3_march2 with dissolve
tm "We call it the march of the rejects."
mc "The rejects?"
rs "Yes. What you're witnessing right now are the people who weren't quite good enough to make the first cut..."
rs "...but had luck and still got accepted."
scene ep3_march4 with dissolve
tm "Their entire presence here is due to quitters and no shows."
tm "These people are happy to accept what wasn't good enough for those who left."
tm "The rejects."
mc "I don't see a difference between them and us."
mc "We're still going to the same college and studying the same things."
if ep3_wearHelmet:
    scene ep3_march6b with dissolve
elif True:
    scene ep3_march6 with dissolve
tm "Such a naive maggot."
tm "The best HOTs are always rejects."
tm "Quinn and Riona. Both rejects."
de "How are they the best ones?"
tm "You know."
scene ep3_march11 with dissolve
$ renpy.pause()
if ep3_wearHelmet:
    scene ep3_march12b with dissolve
elif True:
    scene ep3_march12 with dissolve
mc "So, rejects are better because of lower inhibitions?"
if ep3_wearHelmet:
    scene ep3_march6b with dissolve
elif True:
    scene ep3_march6 with dissolve
tm "Well, yeah!"
tm "Strictly speaking of the girls, of course."
tm "The dudes are all fucking retarded."
scene ep3_march16 with dissolve
tm "What are you looking at!? Keep on walking, you fucking reject!"
if ep3_wearHelmet:
    scene ep3_march12b with dissolve
elif True:
    scene ep3_march12 with dissolve
mc "So, if someone was on the waiting list and got accepted..."
mc "...they would be with that group, right now?"
if ep3_wearHelmet:
    scene ep3_march6b with dissolve
elif True:
    scene ep3_march6 with dissolve
tm "Quinn and Riona weren't. And a few others that came later."
scene ep3_march19 with dissolve
rs "It sounds like you're waiting for someone to show up."
scene ep3_march19b with dissolve
menu:
    "Yes" if True:
        mc "Hoping is more the word I'd use."
        if ep3_wearHelmet:
            scene ep3_march6b with dissolve
        elif True:
            scene ep3_march6 with dissolve
        tm "A chick, huh?"
        mc "(Yeah, your sister...)"
        if ep3_wearHelmet:
            scene ep3_march12b with dissolve
        elif True:
            scene ep3_march12 with dissolve
        mc "Y-yeah."
        if ep3_wearHelmet:
            scene ep3_march6b with dissolve
        elif True:
            scene ep3_march6 with dissolve
        tm "Me too."
    "No" if True:
        mc "No... I just wondered."
        if ep3_wearHelmet:
            scene ep3_march6b with dissolve
        elif True:
            scene ep3_march6 with dissolve
tm "I thought my sister would be with them, today."
tm "Apparently not."
menu:
    "Pry" if True:
        if ep3_wearHelmet:
            scene ep3_march12b with dissolve
        elif True:
            scene ep3_march12 with dissolve
        mc "Did she say she was coming?"
        if ep3_wearHelmet:
            scene ep3_march6b with dissolve
        elif True:
            scene ep3_march6 with dissolve
        tm "Nah. I'm just making sure she isn't."
        tm "That way she won't ruin my fun by trying to join the HOTs or something."
        $ bios_history_tommy += "Tommy is concerned that Josy would come to B&R and join the HOTs.\n\n"
        $ bios_name_tommy = True
        $ chat_new_bios = True
    "Leave it alone" if True:
        $ renpy.pause(0.5)
scene ep3_march25 with dissolve
jac "Hey! Isn't that..."
tm "IT IS!!!"
scene ep3_march25g at transformTop
tm "LILY!"
tm "She's a fucking smokeshow!"
le "Did she quit The Pink Rose?"
rs "Last time I saw her she said she applied for health studies here at B&R."
rs "But she's not quitting The Pink Rose."
jac "Damn... Then college will be cheap for her."
scene ep3_march25g2 with dissolve
tm "Man... Lily's some proper HOT material."
jac "You think they'd want her?"
scene ep3_march25g3 with dissolve
tm "My cock wants her. I'm gonna go convince her to pledge."
rs "Wait for me!"
scene ep3_march25g4 with dissolve
jac "Hey! I saw her first!"
if ep3_wearHelmet:
    scene ep3_march27b with dissolve
elif True:
    scene ep3_march27 with dissolve
de "Hey...everything good?"
if ep3_wearHelmet:
    scene ep3_march29b with dissolve
elif True:
    scene ep3_march29 with dissolve
mc "There's this other girl I've been dating..."
mc "The one I went home to see last weekend."
mc "I was hoping she'd be with that group."
if ep3_wearHelmet:
    scene ep3_march27b with dissolve
elif True:
    scene ep3_march27 with dissolve
de "Oh..."
de "How do I put this delicately?"
de "Is she someone you want to..."
if ep3_wearHelmet:
    scene ep3_march31b with dissolve
elif True:
    scene ep3_march31 with dissolve
de "...?"
mc "She's a bit more than that...I think."
if ep3_wearHelmet:
    scene ep3_march33b with dissolve
elif True:
    scene ep3_march33 with dissolve
de "Oh..."
if ep3_wearHelmet:
    scene ep3_march35b with dissolve
elif True:
    scene ep3_march35 with dissolve
mc "I don't think you get it."
if ep3_wearHelmet:
    scene ep3_march27b with dissolve
elif True:
    scene ep3_march27 with dissolve
de "It's about love, huh?"
if ep3_wearHelmet:
    scene ep3_march29b with dissolve
elif True:
    scene ep3_march29 with dissolve
mc "I'm not sure. It started as a crush..."
mc "But after this weekend..."
mc "I just don't know how I feel or what to do."
if ep3_wearHelmet:
    scene ep3_march27b with dissolve
elif True:
    scene ep3_march27 with dissolve
de "And what is it that you're doing with my sis, then?"
if ep3_wearHelmet:
    scene ep3_march29b with dissolve
elif True:
    scene ep3_march29 with dissolve
mc "I thought you didn't want to talk about it."
if ep3_wearHelmet:
    scene ep3_march27b with dissolve
elif True:
    scene ep3_march27 with dissolve
de "[mc_de_up]... Can you be serious, for once?"
if ep3_wearHelmet:
    scene ep3_march29b with dissolve
elif True:
    scene ep3_march29 with dissolve
mc "Says you."
if ep3_wearHelmet:
    scene ep3_march27b with dissolve
elif True:
    scene ep3_march27 with dissolve
de "This may be hard to believe, but I've known my sister all my life."
mc "Why would that be hard to believe?"
de "And that look I saw on her face when you were lying in the grass talking..."
if ep3_wearHelmet:
    scene ep3_march29b with dissolve
elif True:
    scene ep3_march29 with dissolve
mc "You were watching us!?"
if ep3_wearHelmet:
    scene ep3_march45 with dissolve
elif True:
    scene ep3_march45b with dissolve
de "[mc_de_up]... Please. Ok?"
if ep3_wearHelmet:
    scene ep3_march27b with dissolve
elif True:
    scene ep3_march27 with dissolve
de "That look on her face..."
de "I've only seen it once before."
de "And I don't know how to say this..."
de "...but it's big."
if ep3_wearHelmet:
    scene ep3_march29b with dissolve
elif True:
    scene ep3_march29 with dissolve
mc "What are you getting at?"
mc "To be careful with Maya?"
if ep3_wearHelmet:
    scene ep3_march27b with dissolve
elif True:
    scene ep3_march27 with dissolve
stop music fadeout 5
de "Don't hurt my sister."
de "Ok, [mc_de]?"
$ bios_lily = True
$ bios_name_lily = True
$ chat_new_bios = True
label ep3_quinn_riona_label:
play music "music/ep3/chill.mp3"
scene ep3_quri with wipeleft
ri "Count it again."
qu "I already counted it."
scene ep3_quri2 with dissolve
ri "That's why I said \"again\"."
scene ep3_quri3 with dissolve
qu "Then you fucking do it. I'm telling you, we're short."
scene ep3_quri2 with dissolve
ri "Fuck."
scene ep3_quri3 with dissolve
qu "Relax. Once Camila is fully in...we'll turn it around."
scene ep3_quri6 with dissolve
ri "You're acting like that's a given. What if she bails?"
scene ep3_quri7 with dissolve
qu "Didn't I tell you to relax?"
scene ep3_quri8 with dissolve
ri "I was relaxed, until you started bringing in more girls."
ri "We were fine the way it was!"
ri "Camila was a gamble...and now you're going to ask both Maya and Mona!?"
ri "You're getting cocky."
scene ep3_quri7 with dissolve
qu "It's called expanding, Riona."
scene ep3_quri8 with dissolve
ri "Not when we can't handle it!"
ri "Plus, we're risking it all doing this your way."
ri "That's not called \"expanding\", that's called being a fucking idiot."
scene ep3_quri11 with dissolve
qu "What did you just call me?"
scene ep3_quri8 with dissolve
ri "A fucking idiot!"
play sound "sound_effects/slap.mp3"
scene ep3_quri13 with hpunch
$ renpy.pause()
scene ep3_quri14 with dissolve
ri "You know I'm right. You're just scared to admit it."
scene ep3_quri15 with dissolve
qu "Then tell me your fucking plan, because I've yet to hear one good suggestion from you."
scene ep3_quri16 with dissolve
ri "We stop what we're doing, right now. No more new girls. None of this fucking \"expanding\" bullshit!"
ri "We stick to the original plan, with the current girls and maybe Camila, and we just sell what we need to sell, on top of our obligations..."
ri "...then we cut our losses and we move on..."
ri "...before this gets harder to keep up with."
scene ep3_quri17 with dissolve
ri "And I'm still fucking concerned about who's been spreading that HOTs give free tuition."
scene ep3_quri18 with dissolve
qu "Don't worry about it. It's just a stupid rumor."
qu "We can dismiss that easily."
scene ep3_quri18b with dissolve
qu "*{i}Smack{/i}*"
scene ep3_quri19 with dissolve
qu "We just have to make sure that the girls keep their lids shut."
qu "And we can't cut back, we're so close now!"
qu "Look at Sarah and Melanie! They are paying for themselves and more, at this point."
scene ep3_quri20 with dissolve
ri "Then how the fuck are we short?"
scene ep3_quri22 with dissolve
qu "I don't know...but we're not {b}that{/b} short..."
qu "With the alphas' upcoming big order and some extra efforts from the girls, we can catch up."
$ tmpInt = 0
if ep2_fuckHOT:
    $ tmpInt += 1
if quinn_shop_spicy_lvl == 1:
    $ tmpInt +=1
if quinn_shop_japanese_lvl == 1:
    $ tmpInt += 1
if tmpInt > 1 and quinnLikesYou:
    $ ep3_threesomeOffer = True
    scene ep3_quri23 with dissolve
    ri "What about that pervert?"
    ri "He's been buying girls."
    ri "And I'd much prefer him to the usual customers."
    scene ep3_quri22 with dissolve
    qu "You're right..."
    qu "What if we offer him something big?"
    scene ep3_quri23 with dissolve
    ri "For more money?"
    scene ep3_quri22 with dissolve
    qu "It's a start."
    scene ep3_quri23 with dissolve
    ri "What kind of offer are you thinking about?"
    scene ep3_quri18 with dissolve
    qu "How about a two-course fusion meal?"
    scene ep3_quri26 with dissolve
    ri "Go ahead and set it up."
    ri "I'll talk to Sarah and Melanie to see if they've got something."
    scene ep3_quri31 with dissolve
    qu "{i}Do I have a special for you!{/i}"
    qu "{i}How about a luxurious two course meal?{/i}"
    stop music fadeout 3
    qu "{i}Check back tomorrow if you're interested.{/i}"
    if not ep2SageGuitarTeacher:
        jump ep3_guitar_sage_generic_label
    elif True:
        scene ep3_sage_chad with dissolve
elif ep1_accepted_quinn_offer:
    scene ep3_quri23 with dissolve
    ri "What about that pervert?"
    ri "He's been buying from us."
    scene ep3_quri22 with dissolve
    if ep2_fuckHOT or quinn_shop_spicy_lvl == 1 or quinn_shop_japanese_lvl == 1:
        qu "Yeah, he has, but he's not a big spender."
    elif True:
        qu "Nope, he hasn't. He has my number, but didn't place an order yet."
    qu "I don't think he would go for something expensive."
    scene ep3_quri23 with dissolve
    stop music fadeout 3
    ri "Ok... I'll talk to Sarah and Melanie to see if they've got something."
    if not ep2SageGuitarTeacher:
        jump ep3_guitar_sage_generic_label
    elif True:
        scene ep3_sage_chad with dissolve
elif True:
    stop music fadeout 3
    $ renpy.pause(2)
if not ep2SageGuitarTeacher:
    jump ep3_guitar_sage_generic_label
elif True:
    scene ep3_sage_chad with wipeleft
label ep3_guitar_sage_label:
play music "music/ep1/your_smile.mp3"
if ep2QuinnSawYouAndSage:
    mc "(I wonder if she's up for some more practicing...?)"
    mc "(...or some more fun?)"
elif True:
    mc "(I wonder if she's up for some more practicing?)"
    mc "(Last time I got the feeling she wanted something more, though.)"
mc "(Oh... Sounds like she's got company.)"
scene ep3_sage_chad1 with dissolve
jump ep3_guitar_sage2_label
label ep3_guitar_sage_generic_label:
play music "music/ep1/your_smile.mp3"
if ep3_chad_fight_won:
    scene ep3_sage_chad4b with fade
elif True:
    scene ep3_sage_chad4 with fade
label ep3_guitar_sage2_label:
ch "Please, Sage! Can't you at least talk to them?"
ch "Do you want me to lose everything?"
sa "That's why you're here?"
ch "Yes!"
if ep3_chad_fight_won:
    scene ep3_sage_chad2bbb with dissolve
elif True:
    scene ep3_sage_chad2 with dissolve
sa "What about me?"
if ep3_chad_fight_won:
    scene ep3_sage_chad3b with dissolve
elif True:
    scene ep3_sage_chad3 with dissolve
ch "What about you?"
if ep3_chad_fight_won:
    scene ep3_sage_chad2bb with dissolve
elif True:
    scene ep3_sage_chad2b with dissolve
sa "You're never here just for me..."
sa "I don't fucking get you!"
sa "It's like I'm only good enough for you at parties and when we're with your friends."
if ep3_chad_fight_won:
    scene ep3_sage_chad3b with dissolve
elif True:
    scene ep3_sage_chad3 with dissolve
ch "Sage, this isn't about us. It's about my future!"
if ep3_chad_fight_won:
    scene ep3_sage_chad2bbb with dissolve
elif True:
    scene ep3_sage_chad2 with dissolve
sa "You put yourself into this situation."
sa "I can't fix that for you."
if ep3_chad_fight_won:
    scene ep3_sage_chad4b with dissolve
elif True:
    scene ep3_sage_chad4 with dissolve
ch "Yes, you can! They will listen to you."
sa "..."
if ep3_chad_fight_won:
    scene ep3_sage_chad5b with dissolve
elif True:
    scene ep3_sage_chad5 with dissolve
sa "I'm not promising anything."
if ep3_chad_fight_won:
    scene ep3_sage_chad4b with dissolve
elif True:
    scene ep3_sage_chad4 with dissolve
ch "But you'll try, right?"
if ep3_chad_fight_won:
    scene ep3_sage_chad5b with dissolve
elif True:
    scene ep3_sage_chad5 with dissolve
sa "For you...of course."
if ep3_chad_fight_won:
    scene ep3_sage_chad4b with dissolve
elif True:
    scene ep3_sage_chad4 with dissolve
ch "Thank you."
if ep3_chad_fight_won:
    scene ep3_sage_chad7b with dissolve
elif True:
    scene ep3_sage_chad7 with dissolve
$ renpy.pause()
if ep3_chad_fight_won:
    scene ep3_sage_chad8b with dissolve
elif True:
    scene ep3_sage_chad8 with dissolve
ch "*{i}Smack{/i}*"
if ep3_chad_fight_won:
    scene ep3_sage_chad9b with dissolve
elif True:
    scene ep3_sage_chad9 with dissolve
sa "Hey! What the fuck!?"
ch "What?"
sa "I try to help you and that's all I get?"
if ep3_chad_fight_won:
    scene ep3_sage_chad10b with dissolve
elif True:
    scene ep3_sage_chad10 with dissolve
ch "What do you want?"
if ep3_chad_fight_won:
    scene ep3_sage_chad9b with dissolve
elif True:
    scene ep3_sage_chad9 with dissolve
sa "A real fucking kiss! Not just a peck on my forehead!"
sa "Oh! And it's about fucking time you start getting more physical with me, too!"
if ep3_chad_fight_won:
    scene ep3_sage_chad10b with dissolve
elif True:
    scene ep3_sage_chad10 with dissolve
ch "That's how you want to do this?"
ch "Attaching strings to your helping hand?"
if ep3_chad_fight_won:
    scene ep3_sage_chad12b with dissolve
elif True:
    scene ep3_sage_chad12 with dissolve
sa "Who the fuck talks like that!?"
sa "And no, that's not how I want to do this..."
sa "...but look at yourself! Do you call yourself a man?"
scene ep3_sage_chad13 with dissolve
sa "You've got this sexy woman in front of you trying to throw herself into your arms..."
sa "...and you can't wait to leave instead of trying to get inside of her panties!"
if ep3_chad_fight_won:
    scene ep3_sage_chad14b with dissolve
elif True:
    scene ep3_sage_chad14 with dissolve
ch "I already told you why that is."
if ep3_chad_fight_won:
    scene ep3_sage_chad12b with dissolve
elif True:
    scene ep3_sage_chad12 with dissolve
sa "Stop with the fucking steroid bullshit! I know that's not the truth."
if ep3_chad_fight_won:
    scene ep3_sage_chad14b with dissolve
elif True:
    scene ep3_sage_chad14 with dissolve
ch "I'm not lying! How would you know!?"
if ep3_chad_fight_won:
    scene ep3_sage_chad12b with dissolve
elif True:
    scene ep3_sage_chad12 with dissolve
sa "I know because..."
sa "I-I..."
sa "I talked to Arieth!"
sa "She says Dawe fucks her all the time!"
sa "Sure, he has some issues with his tiny penis, but they still fuck!"
if ep3_chad_fight_won:
    scene ep3_sage_chad14b with dissolve
elif True:
    scene ep3_sage_chad14 with dissolve
ch "Dawe isn't taking the same things I am. He's on the pill, you know?"
ch "It's not as potent."
if ep3_chad_fight_won:
    scene ep3_sage_chad9b with dissolve
elif True:
    scene ep3_sage_chad9 with dissolve
sa "On the pill? Like a fucking girl?"
if ep3_chad_fight_won:
    scene ep3_sage_chad14b with dissolve
elif True:
    scene ep3_sage_chad14 with dissolve
ch "Hey! Don't mock Dawe. He's a nice guy."
ch "And yes, he takes the pill. It's a cheaper alternative and an effective way to build some extra muscles."
ch "Maybe it doesn't make his dick as soft, but..."
if ep3_chad_fight_won:
    scene ep3_sage_chad18b with dissolve
elif True:
    scene ep3_sage_chad18 with dissolve
ch "This isn't about Dawe and his flaccid cock!"
if ep3_chad_fight_won:
    scene ep3_sage_chad12b with dissolve
elif True:
    scene ep3_sage_chad12 with dissolve
sa "You're right! It's about you and yours."
if ep3_chad_fight_won:
    scene ep3_sage_chad14b with dissolve
elif True:
    scene ep3_sage_chad14 with dissolve
ch "Gimme a break! You think this puts me in the mood?"
ch "I'm on the verge of losing everything I worked so hard to build up."
if ep3_chad_fight_won:
    scene ep3_sage_chad12b with dissolve
elif True:
    scene ep3_sage_chad12 with dissolve
sa "Worked so hard, huh? Steroids is cheating, you moron."
sa "You think that will go unnoticed forever?"
sa "You think they don't test for that at your precious fucking competition!?"
sa "You made those choices and brought all of this upon yourself."
scene ep3_sage_chad22 with dissolve
ch "I can't fucking deal with you right now."
ch "I have to sign up for a dorm. I need somewhere to live."
sa "It's funny that you didn't ask for help with getting a place to stay!"
sa "Maybe I would have let you sleep with me!"
if ep3_chad_fight_won:
    scene ep3_sage_chad24b with dissolve
elif True:
    scene ep3_sage_chad24 with dissolve
ch "Take some time to cool down, Sage. Thanks for nothing."
if not ep2SageGuitarTeacher:
    stop music fadeout 3
    sa "Fuck off!!!"
    jump ep3_strip_club_intro_label
scene ep3_sage_chad25 with dissolve
sa "Fuck off!!!"
scene ep3_sage_chad26 with dissolve
sa "*{i}Sobs{/i}*"
mc "Hey..."
scene ep3_sage_guitar1 with dissolve
sa "[name]? Sorry, I'm..."
mc "You don't have to explain."
scene ep3_sage_guitar2 with dissolve
sa "So, you were eavesdropping?"
scene ep3_sage_guitar3 with dissolve
mc "Caring is more the word I'd use."
scene ep3_sage_guitar2 with dissolve
sa "He really beat you up?"
scene ep3_sage_guitar3 with dissolve
menu:
    "Focus on the fight" if True:
        mc "Yeah, well, he attacked me out of nowhere."
        mc "I wasn't prepared."
        mc "Besides...I believe I got a few good shots in there."
    "Focus on Sage" if True:
        $ RPsage += 1
        mc "Hey, I'm alive. But what about you?"
        scene ep3_sage_guitar2 with dissolve
        sa "I'm alive, too."
$ guideSuggestedPage = 79
scene ep3_sage_guitar6 with dissolve
sa "I'm just so stupid. I thought he came here for me."
sa "Apparently not..."
sa "He's probably gonna leave me for his side bitch, too."
sa "That guy has lost all fucking interest in me."
scene ep3_sage_guitar3 with dissolve
menu:
    "I'm here for you" if True:
        mc "Well... I came here for you."
        scene ep3_sage_guitar2 with dissolve
        sa "Why?"
        scene ep3_sage_guitar9 with dissolve
        sa "Oh..."
        sa "That..."
        scene ep3_sage_guitar3 with dissolve
        mc "Well, it was for that, but now I'm just here for you."
        scene ep3_sage_guitar2 with dissolve
        sa "Thank you."
    "Forget about him" if True:
        mc "Forget about him, then."
        mc "You're just wasting your time with him."
        scene ep3_sage_guitar6 with dissolve
        sa "It's easy to say...but harder to do."
        sa "I can't just abandon him like that."
        scene ep3_sage_guitar9 with dissolve
        sa "Oh, you brought your guitar?"
        mc "I thought we could continue to practice, but now I don't know."
        scene ep3_sage_guitar2 with dissolve
sa "Just like Chad's not in the mood for me..."
sa "...I'm not in the mood for practicing, today."
scene ep3_sage_guitar3 with dissolve
mc "I get that."
label ep3_sage_lewd_label:
if _in_replay:
    hide screen phone_screen
    if persistent.name == None:
        $ name = "MC"
    elif True:
        $ name = persistent.name
    if persistent.mc_sage == None:
        $ mc_sage = name
    elif True:
        $ mc_sage = persistent.mc_sage
    if persistent.sage == None:
        $ sage = "Sage"
    elif True:
        $ sage = persistent.sage
    $ ep2QuinnSawYouAndSage = True
    $ dtype = 1
scene ep3_sage_guitar15 with dissolve
stop music fadeout 3
sa "What are you doing?"
mc "You're not in the mood for practicing, but I want to play for you."
mc "I find music helps a lot when you're feeling down."
play music "music/ep1/trow.mp3"
scene ep3_sage_guitar17 with dissolve
$ renpy.pause(13)
show text "Click to continue" with dissolve:
    xpos 0.5
    ypos 0.9
$ renpy.pause(2)
hide text "Click to continue" with dissolve
$ renpy.pause()
scene ep3_sage_guitar19 with dissolve
$ renpy.pause()
scene ep3_sage_guitar20 with dissolve
$ renpy.pause()
scene ep3_sage_guitar22 with dissolve
sa "I remember you doing this to me last time."
scene ep3_sage_guitar23 with dissolve
mc "Yeah..."
mc "But you know...it was for teaching purposes."
if ep2QuinnSawYouAndSage:
    scene ep3_sage_guitar22 with dissolve
    sa "Not only..."
    scene ep3_sage_guitar23 with dissolve
    mc "I admit, it was a way to get closer to you as well."
elif True:
    scene ep3_sage_guitar24 with dissolve
    sa "Only for teaching purposes?"
    scene ep3_sage_guitar23 with dissolve
    menu:
        "Yes" if not _in_replay:
            $ rejectedSage = True
            mc "Yeah."
            scene ep3_sage_guitar24 with dissolve
            sa "All right..."
            $ bios_history_sage += "I told Sage that I only wanted to teach her to play guitar. She didn't like that.\n\n"
            $ bios_name_sage = True
            $ chat_new_bios = True
            jump ep3_rejectedSageLabel
        "No" if True:
            $ rejectedSage = False
            mc "Well...no. It was a way to get closer to you, too."

scene ep3_sage_guitar22 with dissolve
sa "Closer to me, huh?"
scene ep3_sage_guitar23 with dissolve
mc "Yeah..."
scene ep3_sage_guitar22 with dissolve
sa "I remember the feeling when you did it."
sa "It was...comforting."
sa "I know it wasn't supposed to be that, but still..."
scene ep3_sage_guitar29 with dissolve
sa "Then you looked at me..."
sa "...and you know that feeling you get...?"
sa "When you're really close to someone like that."
scene ep3_sage_guitar23 with dissolve
if dtype > 0:
    mc "You mean you get horny?"
    scene ep3_sage_guitar29 with dissolve
    sa "Haha... No!"
    sa "Well...maybe a little bit..."
    scene ep3_sage_guitar22 with dissolve
    sa "But mostly that warm feeling and your heart is beating a bit heavier."
elif True:
    mc "You mean when adrenaline rushes through your body?"
    scene ep3_sage_guitar22 with dissolve
    sa "Yeah...and you get all warm and your heart starts beating a bit heavier."
sa "And your mouth gets dry."
scene ep3_sage_guitar33 with dissolve
$ renpy.pause()
scene ep3_sage_guitar34 with dissolve
sa "Don't mind me..."
sa "Keep playing that guitar..."
scene ep3_sage_guitar35 with dissolve
mc "Oh, God...um..."
mc "Haha...it's hard to focus."
scene ep3_sage_guitar36 with dissolve
sa "Don't stop playing..."
sa "I'm just gonna check something..."
scene ep3_sage_guitar37 with dissolve
sa "Wow..."
sa "See...this is how it should be when a hot girl touches you."
sa "You're rock fucking hard."
scene ep3_sage_guitar38_fr with dissolve
sa "You don't take any steroids, right?"
mc "No, never..."
stop music fadeout 3
scene ep3_sage_guitar39 with dissolve
sa "Hey...did I tell you to stop?"
scene ep3_sage_guitar40 with dissolve
mc "I'm just gonna take my pants off..."
mc "It's too hot when you do that."
sa "Lose the shirt, too."
scene ep3_sage_guitar42 with dissolve
play music "music/ep1/slow_day_blues.mp3"
mc "Ok..."
sa "I thought you were going to play for me again."
scene ep3_sage_guitar44 with dissolve
mc "Let's just keep doing this..."
mc "...whatever it is."
scene ep3_sage_guitar43 with dissolve
sa "*{i}Whispers{/i}* Ah, so you like it when I play with your...cock?"
scene ep3_sage_guitar45 with dissolve
sa "*{i}Smack{/i}*"
scene ep3_sage_guitar46 with dissolve
sa "This is what I wanted..."
sa "It's not too much to ask for, right?"
scene ep3_sage_guitar47 with dissolve
sa "Someone to play with..."
sa "Someone to explore..."
scene ep3_sage_guitar48 with dissolve
mc "I want the same."
scene ep3_sage_guitar47 with dissolve
sa "You do?"
scene ep3_sage_guitar48 with dissolve
mc "Yeah..."
mc "It's fun, it's sexy and it makes you happy."
mc "Who in their right mind wouldn't want that?"
scene ep3_sage_guitar51 with dissolve
sa "Exactly! It's just sex!"
sa "People put the pussy on some kind of a pedestal."
sa "Like it's something holy or a present you can only open on Christmas morning."
sa "And it's {b}SOOOO{/b} important that sex must be with someone you're dating or love."
scene ep3_sage_guitar52 with dissolve
mc "Maybe sex is the start of a relationship, instead of being the reward you get for starting one."
scene ep3_sage_guitar51 with dissolve
sa "This is not about relationships..."
sa "This right here, right now..."
sa "...it's me being horny. Are you ok with that?"
menu:
    "It's just me being horny, too." if True:
        $ RPsage += 1
        scene ep3_sage_guitar52 with dissolve
        mc "Don't worry. I don't have any expectations."
        mc "I'm just horny, too."
    "We'll see what happens." if True:
        $ RPsage -= 1
        scene ep3_sage_guitar52 with dissolve
        mc "Well, maybe it's a bit of both? And we can see what happens?"
        scene ep3_sage_guitar54 with dissolve
        sa "Not for me. Are you in or are you out?"
        scene ep3_sage_guitar52 with dissolve
        mc "Of course I'm in."
scene ep3_sage_guitar56 with dissolve
sa "Good."
scene ep3_sage_guitar56b with dissolve
sa "Now shut up and let me jack you off."
scene anim_sage_hj_ep3 with dissolve
pause
scene anim_sage_hj2_ep3 with dissolve
sa "Your cock is so thick!"
mc "Is it?"
sa "Yeah, I haven't seen anything like it before."
pause
scene anim_sage_hj_ep3 with dissolve
sa "Tell me..."
sa "Do you prefer it when a girl takes control or when you have the control?"
menu:
    "To give up control" if True:
        $ sageControlEp3 = True
        mc "I love it when a girl takes control..."
        $ bios_history_sage += "I had some \"fun\" with Sage. I told her that I like to give up control and she started to please me.\n\n"
        $ bios_name_sage = True
        $ chat_new_bios = True
    "To have control" if True:
        $ bios_history_sage += "I had some \"fun\" with Sage. I told her that I like to be in control and I fucked her mouth.\n\n"
        $ bios_name_sage = True
        $ chat_new_bios = True
        $ sageControlEp3 = False
        mc "I prefer to have the control."
if sageControlEp3:
    scene ep3_sage_guitar56c with dissolve
    sa "Good..."
    scene ep3_sage_guitar56d with dissolve
    sa "Let's see how you like this..."
    scene anim_sage_footjob_ep3 with dissolve
    mc "Oh, wow...don't stop..."
    sa "Giving up control is fun, huh?"
    sa "I like both..."
    pause
    scene anim_sage_footjob2_ep3 with dissolve
    sa "Sometimes I'd prefer to pin you down and ride you hard until you cum..."
    sa "...and other times I'd want you to choke me and fuck me hard in the ass from behind."
    pause
    scene ep3_sage_guitar60 with dissolve
    sa "I like getting inventive, too..."
    sa "But remember... I'm in control..."
    scene ep3_sage_guitar61 with dissolve
    sa "You just lie there...and don't you dare to move your hips."
    sa "If you do...I will stop. Got it?"
    mc "Yeah... I got it."
    scene anim_sage_pussy_ep3 with dissolve
    sa "Let's see how long you can last when I do this..."
    mc "Oh, man... Can you put it in further?"
    sa "Haha! I know that's what you want..."
    sa "But remember... I'm the one in charge here."
    sa "And I'm saying that this is what you'll get from me..."
    pause
    scene anim_sage_pussy2_ep3 with dissolve
    sa "And what I want from you..."
    sa "Is your hot load sprayed outside of my pussy..."
    sa "Can you cum for me, [mc_sage]?"
    mc "Yeah..."
    pause
    sa "CUM! Cum all over my pussy!"
    scene ep3_sage_guitar63a with hpunch
    mc "Ah!!!"
    sa "Oh, God! Yes! Just like that..."
    scene ep3_sage_guitar63 with dissolve
    sa "Mmm...this is exactly what I wanted..."
    sa "To feel sexual..."
    scene ep3_sage_guitar65 with dissolve
    mc "I can make you feel that anytime you want..."
    scene ep3_sage_guitar66 with dissolve
    sa "Like a fuck buddy?"
    scene ep3_sage_guitar65 with dissolve
    mc "Yeah, if you'd want that."
    scene ep3_sage_guitar66 with dissolve
    stop music fadeout 3
    sa "I'll think about it..."
    $ renpy.end_replay()
    $ persistent.ep3_lewd_sage = True
    $ calcScenes()
    if not persistent.bg_sage_alt_unlocked:
        $ persistent.bg_sage_alt_unlocked = True
        $ chat_new_bg = True
        $ calcWallpapers()
    jump ep3_strip_club_intro_label
elif True:
    scene ep3_sage_guitar56c with dissolve
    sa "Ok..."
    scene ep3_sage_guitar57 with dissolve
    sa "Then do it."
    sa "Control me. Dominate me."
    scene ep3_sage_guitar58 with dissolve
    sa "I like where this is going..."
    mc "Open up..."
    scene ep3_sage_guitar58b with dissolve
    sa "Hngnn..."
    scene anim_sage_blowjob_ep3 with dissolve
    mc "That's it...take it all..."
    pause
    scene anim_sage_blowjob2_ep3 with dissolve
    mc "Do you like it?"
    sa "Mphff... Mhm..."
    pause
    mc "Am I doing it too hard?"
    scene ep3_sage_guitar58 with dissolve
    sa "Use my mouth as your pleasure hole..."
    sa "Fill it up."
    mc "Ok... Tap me if it's too hard..."
    scene anim_sage_blowjob2b_ep3 with dissolve
    mc "This feels fucking great."
    mc "Ah yes!!!"
    scene anim_sage_blowjob3_ep3 with dissolve
    mc "Fuck! It's so tight!"
    mc "Your mouth and throat are wrapped around my entire cock!"
    pause
    mc "I'm...gonna...CUM!"
    scene ep3_sage_throat_cum with hpunch
    $ renpy.pause(0.5)
    scene ep3_sage_throat_cum with hpunch
    $ renpy.pause(0.5)
    scene ep3_sage_throat_cum with hpunch
    $ renpy.pause()
    scene ep3_sage_throat_cum2 with dissolve
    sa "*{i}Gurgle{/i}* *{i}Coughs{/i}*"
    sa "Now, that's how you control someone..."
    sa "Wow..."
    scene ep3_sage_guitar67 with dissolve
    sa "See...this is what I wanted..."
    sa "To feel sexual..."
    scene ep3_sage_guitar68 with dissolve
    mc "I can make you feel that anytime you want..."
    scene ep3_sage_guitar67 with dissolve
    sa "Like a fuck buddy?"
    scene ep3_sage_guitar68 with dissolve
    mc "Yeah, if you'd want that."
    scene ep3_sage_guitar67 with dissolve
    stop music fadeout 3
    sa "I'll think about it..."
    $ renpy.end_replay()
    $ persistent.ep3_lewd_sage = True
    $ calcScenes()
    if not persistent.bg_sage_alt_unlocked:
        $ persistent.bg_sage_alt_unlocked = True
        $ chat_new_bg = True
        $ calcWallpapers()
    jump ep3_strip_club_intro_label

label ep3_rejectedSageLabel:
scene ep3_sage_rejected with dissolve
sa "I think... I need to be alone now."
scene ep3_sage_rejected1 with dissolve
mc "Because of what I said?"
scene ep3_sage_rejected with dissolve
sa "Just...leave."
scene ep3_sage_rejected1 with dissolve
stop music fadeout 3
mc "If you say so."

label ep3_strip_club_intro_label:
$ renpy.music.set_volume(0.8, delay=0, channel='music')
$ renpy.pause(0.5)
$ renpy.music.set_volume(0.6, delay=0, channel='music')
$ renpy.pause(0.5)
$ renpy.music.set_volume(0.4, delay=0, channel='music')
$ renpy.pause(0.5)
$ renpy.music.set_volume(0.2, delay=0, channel='music')
play music "music/ep3/raveyard.mp3"
scene ep3_sclub_intro with wiperight
rs "Now maggots, this is important."
rs "This place right here, is sacred ground for DIKs."
scene ep3_sclub_intro1 with dissolve
rs "We're only allowed to be in here because they let us."
rs "Several of us aren't 21, yet, which means that they are taking a huge risk letting us in."
scene ep3_sclub_intro with dissolve
rs "Some ground rules..."
rs "Be respectful to the ladies and don't drink too much."
scene ep3_sclub_intro2 with dissolve
tm "And if the bouncer taps you on your shoulder..."
tm "...it means that you must stop sucking on the stripper's titties."
tm "Got it?"
mc "Got it."
tm "Then follow us, because it's time to party with some hotties!"
scene ep3_sclub_intro10 with dissolve
bo "Mr. B!"
rs "Stanley! Thanks for setting this up."
scene ep3_sclub_intro12 with dissolve
bo "You know the boss, man. Money talks."
bo "And frankly, the place has been a ghost town since Saturday."
bo "I bet the ladies are glad that you guys showed up."
scene ep3_sclub_intro13 with dissolve
bo "You boys behave tonight. The ladies are waiting for you."
bo "Remember, no phones allowed! Or I'ma whoop your asses."
hide screen phone_screen
scene ep3_sclub_intro4b with dissolve
rs "Maggots and brothers, newcomers and veterans..."
rs "Let me welcome you to..."
$ bios_history_rusty += "Rusty seems to have a lot of money being able to rent The Pink Rose for an entire night.\n\n"
$ bios_name_rusty = True
$ bios_stanley  = True
$ chat_new_bios = True

scene ep3_sclub_intro5
$ renpy.music.set_volume(1.0, delay=0, channel='music')
play music "<from 60.1>music/ep3/raveyard.mp3"
queue music ["music/ep3/roads.mp3", "music/ep2/night_lights.mp3", "music/ep2/fallen_colors.mp3","music/ep2/phate.mp3","music/ep3/raveyard.mp3"]
rs "The Pink Rose!"
scene ep3_sclub_intro6 with dissolve
tm "You guys better get your asses back to the ATMs..."
tm "...because our boy Rusty here got us the club all to ourselves, tonight!"
scene ep3_sclub_intro7 with dissolve
de "The whole club!?"
scene ep3_sclub_intro8 with dissolve
rs "It's just a Tuesday."
de "But...still."
scene ep3_sclub_intro9 with dissolve
tm "Sweet! Lily works tonight!"
jump ep3_fr_sclub_label

label ep3_wed_morning_label:
show screen phone_screen
if ep3_wearHelmet:
    scene ep3_wed_morning with vpunch
elif True:
    scene ep3_wed_morningb with vpunch
mc "...whoa!"
play music "music/ep3/sunny_acoustic_rock.mp3"
if ep3_wearHelmet:
    scene ep3_wed_morning1 with dissolve
elif True:
    scene ep3_wed_morning1b with dissolve
mc "Hmpf..."
mc "(I have no clue how it happened...but I got home ok.)"
mc "(Well...close enough.)"
if ep3_wearHelmet:
    scene ep3_wed_morning2b with dissolve
elif True:
    scene ep3_wed_morning2 with dissolve
mc "(No Maya? Phew...good.)"
mc "(Man...sunlight is not my friend today...)"
if ep3_wearHelmet:
    scene ep3_wed_morning3 with dissolve
elif True:
    scene ep3_wed_morning3b with dissolve
mc "(I really don't want to look at another bottle of beer...)"
mc "(But I have to...)"
mc "(Last night I drank way more than 10...I think...)"
mc "(I need to count them later.)"

play sound "sound_effects/cellphone.mp3"
if ep3_wearHelmet:
    scene ep3_wed_morning4 with hpunch
elif True:
    scene ep3_wed_morning4b with hpunch
"*{i}Cellphone rings{/i}*"
mc "(Ah!!! Stop that noise...)"
if ep3_wearHelmet:
    scene ep3_wed_morning5 with dissolve
elif True:
    scene ep3_wed_morning5b with dissolve
mc "*{i}Smacks{/i}* Uh...hello?"
scene ep3_wed_morning6 with dissolve
js "Hi...it's me..."
if ep3_wearHelmet:
    scene ep3_wed_morning7 with hpunch
elif True:
    scene ep3_wed_morning7b with hpunch
mc "Josy!"
if ep3_wearHelmet:
    scene ep3_wed_morning8
elif True:
    scene ep3_wed_morning8b
mc "Ahh!!!"
scene ep3_wed_morning9 with dissolve
js "What's wrong?"
if ep3_wearHelmet:
    scene ep3_wed_morning10 with dissolve
elif True:
    scene ep3_wed_morning10b with dissolve
mc "It's just a hangover..."
mc "How are you? I've tried reaching you."
scene ep3_wed_morning11 with dissolve
js "Yeah, I saw it. I was grounded and they took my phone."
if ep3_wearHelmet:
    scene ep3_wed_morning10 with dissolve
elif True:
    scene ep3_wed_morning10b with dissolve
mc "What? Why?"
if ep2_fuckedJosy:
    scene ep3_wed_morning13 with dissolve
    js "Really? You're asking why?"
    js "I {i}think{/i} you know exactly why..."
elif True:
    scene ep3_wed_morning11 with dissolve
    js "Dad and Monica came home early and saw that I had someone over..."
    js "They saw that we've been drinking and yeah..."
    js "They put two and two together..."
if ep3_wearHelmet:
    scene ep3_wed_morning10 with dissolve
elif True:
    scene ep3_wed_morning10b with dissolve
mc "Oh...I'm sorry for getting you into trouble."
scene ep3_wed_morning15 with dissolve
js "Don't be... Things needed to be said..."
js "...and my dad got to hear an earful about Monica..."
if ep3_wearHelmet:
    scene ep3_wed_morning10 with dissolve
elif True:
    scene ep3_wed_morning10b with dissolve
mc "You argued?"
scene ep3_wed_morning15 with dissolve
js "Yeah... It doesn't matter anymore..."
js "Because I'm moving out..."
if ep3_wearHelmet:
    scene ep3_wed_morning10 with dissolve
elif True:
    scene ep3_wed_morning10b with dissolve
mc "Oh, no...you are? Where are you going?"
scene ep3_wed_morning18 with dissolve
js "I'm coming to you..."
if ep3_wearHelmet:
    scene ep3_wed_morning7 with hpunch
elif True:
    scene ep3_wed_morning7b with hpunch
mc "No way!!? You got in!?"
if ep3_wearHelmet:
    scene ep3_wed_morning8
elif True:
    scene ep3_wed_morning8b
mc "Ahh!!!"
scene ep3_wed_morning13 with dissolve
js "Hangover?"
if ep3_wearHelmet:
    scene ep3_wed_morning21 with dissolve
elif True:
    scene ep3_wed_morning21b with dissolve
mc "Yeah..."
mc "Hey, I thought you'd be happier about coming here!"
scene ep3_wed_morning9 with dissolve
js "It's just...you know..."
js "The way I'm leaving my dad..."
js "I thought it would be different."
if ep3_wearHelmet:
    scene ep3_wed_morning21 with dissolve
elif True:
    scene ep3_wed_morning21b with dissolve
mc "I don't know what to say..."
scene ep3_wed_morning9 with dissolve
js "You don't have to say anything..."
js "...except..."
scene ep3_wed_morning18 with dissolve
js "...tell me your dorm number."
if ep3_wearHelmet:
    scene ep3_wed_morning10 with dissolve
elif True:
    scene ep3_wed_morning10b with dissolve
mc "Why do you ask?"
scene ep3_wed_morning18 with dissolve
js "Well, I was thinking..."
scene ep3_wed_morning13 with dissolve
js "Maybe...until I get my own dorm...I could stay with you?"
$ guideSuggestedPage = 81
scene ep3_wed_morning29 with dissolve
mc "I...uh..."
$ bios_history_josy += "Josy got accepted! She's coming to B&R!\n\n"
$ bios_name_josy = True
$ chat_new_bios = True
menu:
    "Tell her about Maya" if True:
        $ bios_history_josy += "I told her that I was sharing my dorm with a girl.\n\n"
        $ bios_name_josy = True
        $ chat_new_bios = True
        $ ep3_toldJosyStaySomewhereElse = False
        mc "I'm actually living with someone, already...a girl..."
        scene ep3_wed_morning13 with dissolve
        js "A girl, huh?"
        js "Look at you, you stud."
        js "Do you think she'd mind if I stayed there, too?"
        if ep3_wearHelmet:
            scene ep3_wed_morning10 with dissolve
        elif True:
            scene ep3_wed_morning10b with dissolve
        mc "It might get a bit awkward..."
        scene ep3_wed_morning18 with dissolve
        js "Don't worry...I can always stay with a friend or something."
        js "And, hey... I get it..."
        js "I mean...given how you and I met..."
        js "I'm not surprised if you've started dating others."
        scene ep3_wed_morning29 with dissolve
        mc "I care about you a lot...but, yeah, the boyfriend part..."
        mc "It kind of bugs me."
        scene ep3_wed_morning9 with dissolve
        js "When I get there...I promise..."
        js "I'll put my cards on the table..."
        js "I'm gonna have to do it anyway."
    "Find someplace else to stay" if True:
        $ bios_history_josy += "She wanted to stay in my dorm. I told her to find somewhere else to stay.\n\n"
        $ bios_name_josy = True
        $ chat_new_bios = True
        $ RPjosy -= 1
        $ ep3_toldJosyStaySomewhereElse = True
        mc "I'm actually living with someone, already...and there's really not much room here."
        scene ep3_wed_morning9 with dissolve
        js "Oh, I get it."
        js "Don't worry...I can always stay with a friend or something."
        if ep3_wearHelmet:
            scene ep3_wed_morning10 with dissolve
        elif True:
            scene ep3_wed_morning10b with dissolve
        mc "That's right, you know people who go here, right?"
        scene ep3_wed_morning9 with dissolve
        js "Yeah, a few."
        js "But also...it's a bit weird coming there..."

if ep3_wearHelmet:
    scene ep3_wed_morning10 with dissolve
elif True:
    scene ep3_wed_morning10b with dissolve
mc "Why is that?"
scene ep3_wed_morning9 with dissolve
js "I should have told you this before...but..."
js "Remember when I told you how relationships when you can't see each other every week suck?"
js "That won't be the case for me when I come there..."
if ep3_wearHelmet:
    scene ep3_wed_morning10 with dissolve
elif True:
    scene ep3_wed_morning10b with dissolve
mc "No way..."
scene ep3_wed_morning9 with dissolve
js "I really don't wanna have this conversation over a phone call."
js "Can you promise to let me explain in person?"
if ep3_wearHelmet:
    scene ep3_wed_morning10 with dissolve
elif True:
    scene ep3_wed_morning10b with dissolve
mc "I'm getting a bit nervous...what if I know your boyfriend?"
scene ep3_wed_morning40 with dissolve
js "Hey! Promise!"
if ep3_wearHelmet:
    scene ep3_wed_morning10 with dissolve
elif True:
    scene ep3_wed_morning10b with dissolve
mc "All right, I promise to let you explain when you get here."
scene ep3_wed_morning29b with dissolve
js "Thank you. I guess I'll see you at B&R, then?"
if ep3_wearHelmet:
    scene ep3_wed_morning10 with dissolve
elif True:
    scene ep3_wed_morning10b with dissolve
mc "It seems so."
scene ep3_wed_morning18 with dissolve
js "Bye..."

if ep3_wearHelmet:
    scene ep3_wed_morning45 with dissolve
elif True:
    scene ep3_wed_morning45b with dissolve
mc "(She's really coming here...)"
mc "(I don't know what to feel, right now.)"
scene ep3_wed_morning46 with dissolve
mc "(Huh... Is that a note?)"
if ep3_wearHelmet:
    scene ep3_wed_morning47b with dissolve
elif True:
    scene ep3_wed_morning47 with dissolve
my "{i}Good morning. I'm sure you have a headache today, so I'll write this without exclamation marks.{/i}"
my "{i}I'm leaving for some scavenger hunt activities before class.{/i}"
my "{i}If you're wondering why you slept naked under the bed...{/i}"
my "{i}...so do I.{/i}"
my "{i}Let me just tell you that it wasn't for lack of convincing, on my part.{/i}"
my "{i}And I put your blanket in the laundry basket...you might not want to open that until you've sobered up.{/i}"
my "{i}In case (read hopefully) you have forgotten about the other thing you did...then we're good.{/i}"
my "{i}XOXO{/i}"
mc "(I...don't remember any of that.)"
mc "(How much did I drink?)"
$ bios_history_maya += "I apparently did some \"thing\" to Maya after coming home drunk...\n\n"
$ bios_name_maya = True
$ chat_new_bios = True
if ep3_wearHelmet:
    scene ep3_wed_morning49 with dissolve
elif True:
    scene ep3_wed_morning49b with dissolve
mc "(Well it's only Hell Week once...)"
mc "(But I'm gonna try to squeeze in some actual studying, today.)"
stop music fadeout 3
mc "(First a shower and breakfast, though.)"

label ep3_lib_study_label:
scene ep3_lib_study with wipeleft
mc "(How am I supposed to study while being buzzed?)"
mc "(I can't even focus...)"
if minigames:
    menu:
        "Study English" if True:
            $ bonusPercentageEnglish += 10
            "+10%% score on your next English test.\nYour total bonus for the next test is [bonusPercentageEnglish]%%."
        "Study Math" if True:
            $ bonusPercentageMath += 10
            "+10%% score on your next Math test.\nYour total bonus for the next test is [bonusPercentageMath]%%."
        "Study Gender Studies" if True:
            $ bonusPercentageGender += 10
            "+10%% score on your next Gender Studies test.\nYour total bonus for the next test is [bonusPercentageGender]%%."
    mc "(Ok... I understand {b}that{/b}.)"
mg "You rolled a 2! Your character dropped the sword in the lake."
tri "Hahaha!"
scene ep3_lib_study1 with dissolve
mc "(Man...they are annoying...)"
mc "(This is a library...not a clubhouse...)"
mc "(This must be how Bella feels like...)"
scene ep3_lib_study with dissolve
mc "(Come on... Focus!)"
if minigames:
    menu:
        "Study English" if True:
            $ bonusPercentageEnglish += 10
            "+10%% score on your next English test.\nYour total bonus for the next test is [bonusPercentageEnglish]%%."
        "Study Math" if True:
            $ bonusPercentageMath += 10
            "+10%% score on your next Math test.\nYour total bonus for the next test is [bonusPercentageMath]%%."
        "Study Gender Studies" if True:
            $ bonusPercentageGender += 10
            "+10%% score on your next Gender Studies test.\nYour total bonus for the next test is [bonusPercentageGender]%%."
    mc "(Hm... I see...)"
mg "Sally's fire spell was a success! The monster is slain!"
tri "Hurrah!"
if ep3_wearHelmet:
    scene ep3_lib_study2 with dissolve
elif True:
    scene ep3_lib_study2b with dissolve
mc "(...)"
scene ep3_lib_study3 with dissolve
isa "Hey! Keep that noise down!"
scene ep3_lib_study4 with dissolve
$ renpy.pause()
if ep3_wearHelmet:
    scene ep3_lib_study5 with dissolve
elif True:
    scene ep3_lib_study5b with dissolve
$ renpy.pause()
scene ep3_lib_study6 with dissolve
mc "(What's with her?)"
menu:
    "Check her out" if True:
        $ dk(1)
        scene ep3_lib_study6b with dissolve
        $ renpy.pause()
    "Don't check her out" if True:
        $ dk(-1)
scene ep3_lib_study7 with dissolve
isa "{i}He's here. Just letting you know...{/i}"
scene ep3_lib_study with dissolve
mc "(My head is spinning...)"
mc "(I can't wait for this week to be over.)"
ji "Good morning..."
scene ep3_lib_study8 with dissolve
mc "Morning..."
ji "Coffee?"
mc "For me? Thanks!"
scene ep3_lib_study11b with dissolve
ji "..."
scene ep3_lib_study11 with dissolve
ji "Are you reading?"
scene ep3_lib_study11c with dissolve
mc "We're not supposed to be talking in here, you know."
scene ep3_lib_study14 with dissolve
ji "Mimicry... Funny..."
scene ep3_lib_study11c with dissolve
mc "I had to break the ice, somehow."
if not ep3_jillHelmetChad and ep3_wearHelmet:
    scene ep3_lib_study11 with dissolve
    $ ep3_jillHelmetLibrary = True
    ji "Um...nice helmet..."
    scene ep3_lib_study11b with dissolve
    mc "Ah, it's a part of Hell Week. I know, it's stupid."
mc "Listen... I'm sorry for the way I acted, yesterday."
mc "I shouldn't have reacted the way I did..."
mc "...it's just-"
scene ep3_lib_study16 with dissolve
ji "I know."
ji "I shouldn't have gone behind your back, either."
ji "Are we good?"
scene ep3_lib_study18 with dissolve
mc "Yeah...we're good."
scene ep3_lib_study19 with dissolve
isa "(...)"
scene ep3_lib_study20 with dissolve
$ renpy.pause()
scene ep3_lib_study11 with dissolve
ji "What are you studying?"
scene ep3_lib_study22 with dissolve
mc "A bit of everything... I'm really behind after all the pledge stuff the DIKs are putting us through."
scene ep3_lib_study11 with dissolve
ji "Need any help?"
scene ep3_lib_study22 with dissolve
mc "Did you ever take any Gender Studies class?"
scene ep3_lib_study23 with dissolve
ji "No... Why? Do you?"
scene ep3_lib_study22 with dissolve
mc "Yeah. My friend Maya told me it was supposed to be easy credits, but I don't understand half of it."
scene ep3_lib_study23 with dissolve
ji "I'm afraid I wouldn't, either."
ji "Are you planning on taking an economics class?"
scene ep3_lib_study22 with dissolve
mc "Hm...no? I'm going to be an engineer. Should I be taking economics?"
scene ep3_lib_study23 with dissolve
ji "Honestly, yes. Who knows what you may end up doing in life?"
ji "If you ever want to start your own business or get ahead in a field of work..."
ji "...a few basic courses in economics could help you a lot."
scene ep3_lib_study22 with dissolve
mc "Yeah, maybe you're right. Perhaps I'll do it next semester."
scene ep3_lib_study with fade
mc "(Gender and sex? This doesn't seem that important to read about...)"
scene ep3_lib_study27 with dissolve
mc "(She's pretty cute when she's reading.)"
scene ep3_lib_study28 with dissolve
$ bios_history_jill += "I apologized to Jill after treating her poorly this morning, it felt good.\n\n"
$ bios_name_jill = True
$ chat_new_bios = True
menu:
    "Flirt with your feet" if True:
        $ bios_history_jill += "I flirted with Jill under the table in the library.\n\n"
        $ bios_name_jill = True
        $ chat_new_bios = True
        $ ep3_flirtedJill = True
        $ RPjill += 1
        scene ep3_lib_study29 with dissolve
        $ renpy.pause()
        scene ep3_lib_study30 with dissolve
        $ renpy.pause()
        scene ep3_lib_study28 with dissolve
        $ renpy.pause()
        scene ep3_lib_study31 with dissolve
        $ renpy.pause()
        scene ep3_lib_study32 with dissolve
        $ renpy.pause()
        scene ep3_lib_study28 with dissolve
        $ renpy.pause()
        scene ep3_lib_study33 with dissolve
        $ renpy.pause()
        scene ep3_lib_study30 with dissolve
        $ renpy.pause()
        scene ep3_lib_study34 with dissolve
        $ renpy.pause()
        scene ep3_lib_study with Fade(1.5,1,0.5)
    "Keep studying" if True:
        $ ep3_flirtedJill = False
        scene ep3_lib_study with wipeleft
mc "(My brain is starting to get full...)"
mc "(It's like I hear the words I read, but I don't understand them.)"
mg "Huzzah! The wizard has been defeated!"
$ guideSuggestedPage = 82
label ep3_lib_dng_label:
scene ep3_dng_intro with dissolve
mc "Hey, Magnar. You do realize you're gonna make her come back if you keep it up?"
scene ep3_dng_intro1 with dissolve
mg "It's just so hard to contain our feelings when we play!"
mg "And don't tell us to take it elsewhere, because there's no better place for us to play than here."
scene ep3_dng_intro with dissolve
mc "What is it that you're playing?"
scene ep3_dng_intro3 with dissolve
rn "Um, hello!? Dungeons and Gremlins."
scene ep3_dng_intro with dissolve
if dtype > 0:
    mc "Sounds stupid."
    scene ep3_dng_intro3 with dissolve
    rn "Said the student who wasn't smart enough to join the tri-beta fraternity."
elif True:
    mc "Sounds weird."
    scene ep3_dng_intro3 with dissolve
    if ep3_wearHelmet:
        rn "Said the student with a cock for a hat."
    elif True:
        rn "Said the male student reading a book about feminism."
scene ep3_dng_intro with dissolve
mc "You just play with a pen and paper?"
scene ep3_dng_intro7 with dissolve
sy "And a die and instructions."
sy "Today, Magnar is the game master controlling the game."
scene ep3_dng_intro1 with dissolve
mg "Precisely! But you forgot the most powerful asset of all!"
mg "Absolutely vital to make the game interesting!"
mg "Imagination!"
mg "The entire game takes place within our minds."
scene ep3_lib_study23 with dissolve
ji "Wanna try it?"
scene ep3_lib_study22 with dissolve
mc "I'm not sure..."
scene ep3_lib_study23 with dissolve
ji "We could use a break."
scene ep3_dng_intro with dissolve
mc "Let us in on the {i}fun{/i}."
scene ep3_dng_intro1 with dissolve
mg "I don't appreciate the undertone, but I think that we can get rid of it with one playthrough."
mg "What do you say, gang?"
scene ep3_dng_intro3 with dissolve
rn "They don't even have characters."
scene ep3_dng_intro1 with dissolve
mg "Well it's quick to make one. Take a seat, please."
label ep3_dng_game:
scene ep3_dng_magnar_talk with dissolve
mg "All right, let's start with you, [name]."
mg "What kind of character do you want to play as?"
scene ep3_dng_magnar_listen with dissolve
mc "So, I can...like...pick anything?"
scene ep3_dng_magnar_talk with dissolve
mg "Yes, anything that fits the lore of fantasy."
scene ep3_dng_magnar_listen with dissolve
mc "How about a fighter...like a knight?"
scene ep3_dng_magnar_talk with dissolve
mg "This one wants to be a knight immediately, haha."
mg "Let's start you off as a simple brute."
scene ep3_dng_magnar_jill with dissolve
mg "And for Jill? I'm thinking a cute rogue elf, perhaps?"
ji "Uh, sure? Why not?"
scene ep3_dng_magnar_talk with dissolve
mg "Now...let's play!"

play music "music/ep3/the_unbound_inn.mp3"
scene ep3_dng with dissolve
mg "{i}The group of heroes find themselves in a local tavern.{/i}"
mg "{i}The mead is plenty and in the background you hear the bard play his tunes.{/i}"
mg "{i}The crackling fire keeps the tavern warm and the locals are enjoying themselves after a hard day of work.{/i}"
mg "{i}Sally, you start.{/i}"
scene ep3_dng1 with dissolve
sy "I spend my turn greeting the party."
sy "Greetings fellow heroes! I'm Sally, the witch!"
sy "Fate has brought us together to this tavern, today."
mg "{i}Sally greets the party and slightly increases their morale.{/i}"
mg "{i}Ron, you're up.{/i}"
scene ep3_dng2 with dissolve
rn "I spend my turn charming Jill the elf."
rn "Jill, a pleasure meeting you! The name's Ron, the rogue."
rn "Don't let my charms fool you, I'm silent and deadly, but I have a soft spot for elves."
mg "{i}Ron charms Jill and increases her health.{/i}"
mg "{i}Jill the elf, it's your turn.{/i}"
scene ep3_dng4 with dissolve
ji "I...uh...say hi to the party."
mg "{i}Jill greets the party and slightly increases their morale.{/i}"
scene ep3_dng1b with dissolve
sy "Such a copycat."
scene ep3_dng5 with dissolve
mg "{i}[name] the brute. What's your move?{/i}"
mc "What can I do?"
mg "{i}Use your imagination!{/i}"
menu:
    "Greet the party" if True:
        mc "I don't know... I also greet the party..."
        mg "{i}Another boost of morale for the group.{/i}"
    "I spank Sally ({color=#ffffff}Huge {size=-1}{font=collegiate.ttf}DIK{/font}{/size}{/color})" if dtype > 1:
        $ ep3_spankedSally = 1
        mc "I spank Sally's ass."
        scene ep3_dng5_ass with dissolve
        sy "You what?"
        mc "Hey, I'm a brute, right?"
        mg "{i}Spanking Sally's ass...that requires a roll of at least a 3.{/i}"
        mg "{i}It's a 5! You have successfully spanked Sally's ass.{/i}"
        play sound "sound_effects/slap.mp3"
        scene ep3_dng5_ass2 with hpunch
        sy "Ouch!"
        scene ep3_dng5_ass2b with dissolve
        $ renpy.pause()
    "Flirt with Jill ({color=#ffffff}Huge {size=-1}{font=collegiate.ttf}CHICK{/font}{/size}{/color})" if dtype < -1:
        mc "I...flirt with the elf."
        scene ep3_dng_flirt with dissolve
        rn "Keep your paws from my elf. I called dibs!"
        scene ep3_dng_flirt2 with dissolve
        mc "Hi, I always thought that long ears are beautiful."
        scene ep3_dng_flirt3 with dissolve
        ji "Haha! Well, I got them!"
play sound "sound_effects/door_break.mp3"
stop music
scene ep3_dng_thieves with hpunch
$ renpy.pause(0.5)
play music "music/ep3/slavic_battle_theme.mp3"
mg "{i}The bard's beautiful melody abruptly stops as a group of three thieves rushes the tavern!{/i}"
mg "{i}The crowd quickly scatters, except for our four heroes.{/i}"
scene ep3_dng_thieves1 with dissolve
sy "I swiftly cast a fire spell!"
mg "{i}Sally rolls for casting a fire spell.{/i}"
mg "{i}It's a success!{/i}"
play sound "sound_effects/fire.mp3"
scene ep3_dng_thieves2 with hpunch
mg "{i}One of the thieves bursts into flames!{/i}"
scene ep3_dng_thieves3 with dissolve
rn "I throw two of my daggers at the thieves!"
mg "{i}It's a tough roll, you'll need a 5 or better.{/i}"
mg "{i}Ouch...you roll a 4.{/i}"
play sound "sound_effects/knife.mp3"
scene ep3_dng_thieves4 with dissolve
play sound "sound_effects/knife_hit.mp3"
mg "{i}One of the daggers hits one of the thieves, who falls dead to the ground!{/i}"
scene ep3_dng_thieves5 with dissolve
mg "{i}The other dagger grazes [name] the brute's shoulder!{/i}"
play sound "sound_effects/knife_hit.mp3"
mg "{i}[name] loses a bit of health!{/i}"
mc "What?"

rn "Come on, use your imagination!"
scene ep3_dng_thieves6 with dissolve
mg "{i}Jill?{/i}"
ji "I..."
if RPjill > 2:
    ji "...heal [name] with...a spell?"
    sy "Hey, you can't do that! Only high elves and mages can use spells!"
    mg "{i}Rolling the die...{/i}"
    scene ep3_dng_thieves10 with dissolve
    play sound "sound_effects/heal.mp3"
    mg "{i}It turns out Jill the elf is a high elf and successfully heals [name].{/i}"
    mg "{i}Now if Jill's spell only had the power to make [name] enjoy this.{/i}"
    mc "Yeah... I just don't get this game."
elif True:
    ji "I cast a fire spell at the thief, too."
    sy "This game isn't fun when you're just copying what I do."
    sy "Also, only high elves and mages can use spells!"
    mg "{i}Rolling the die...{/i}"
    play sound "sound_effects/fire.mp3"
    scene ep3_dng_thieves13 with hpunch
    mg "{i}It turns out Jill the elf is a high elf and successfully casts a fire spell.{/i}"
    mg "{i}But the fire spell misses the last thief!{/i}"

scene ep3_dng5 with dissolve
mg "{i}And so we come to [name] the brute...{/i}"
mg "{i}Come on, use your imagination!{/i}"
menu:
    "I attack" if True:
        mc "I attack the thief with my sword."
        mg "{i}Your character doesn't come with a sword.{/i}"
        mc "Ok, then I pick up Ron's dagger and throw it."
        scene ep3_dng_thieves15 with dissolve
        mg "{i}The brute tries to throw a dagger...{/i}"
        mg "{i}It fails!{/i}"
        play sound "sound_effects/knife.mp3"
        scene ep3_dng_thieves16 with dissolve
        play sound "sound_effects/knife_hit.mp3"
        mg "{i}The dagger hits Ron!{/i}"
        rn "You suck!"
        if dtype > 0:
            mc "How is that a fail?"
        elif True:
            mc "Whoops..."
    "I protect the elf" if True:
        $ ep3_protectedElf = True
        mc "I protect Jill the elf."
        scene ep3_dng_thieves17 with dissolve
        mg "{i}[name] the brute stands in front of Jill the elf, in an attempt to defend her from the thief's oncoming assault!{/i}"
        mg "{i}It fails!{/i}"
        play sound "sound_effects/slash.mp3"
        scene ep3_dng_thieves19 with dissolve
        mg "{i}The thief chops off the head of [name] the brute and holds it in his hands and laughs!{/i}"
    "I spank Sally ({color=#ffffff}Huge {size=-1}{font=collegiate.ttf}DIK{/font}{/size}{/color})" if dtype > 1:
        if ep3_spankedSally == 1:
            mc "I spank Sally, again. Hard."
        elif True:
            mc "I spank Sally. Hard."
        $ ep3_spankedSally = 1
        play sound "sound_effects/slap.mp3"
        scene ep3_dng5_ass2 with hpunch
        sy "OUCH! What the hell!?"
        scene ep3_dng5_ass2b with dissolve
        mc "Relax! It's just a game. I'm not spanking you in real life."
        scene ep3_dng5_ass2c with dissolve
        sy "Just knowing that you're imagining something makes this weird!"
        scene ep3_dng5_ass2d with dissolve
        mc "I'm not imagining anything close to what you may think."
        scene ep3_dng5_ass2e with dissolve
        $ renpy.pause()

stop music
scene ep3_dng_ice with hpunch
ice "SILENCE!"
scene ep3_dng_after with dissolve
mg "..."
mg "I think it's time for classes..."
mg "Let's go..."
scene ep3_dng_after2 with dissolve
mc "Is there something wrong with Isabella?"
mc "She seems...angrier than usual."
scene ep3_dng_after3 with dissolve
ji "It's...uh...probably one of those days."
ji "I'll check up on her."
ji "Thanks for the company and the...game."
if ep3_protectedElf:
    ji "Oh, and of course...!"
    scene ep3_dng_after4 with dissolve
    ji "*{i}Smack{/i}*"
    scene ep3_dng_after3 with dissolve
    ji "For giving your life to protect me."
    mc "Haha... My pleasure."
$ bios_ron = True

$ bios_history_sally += "I played Dungeons and Gremlins with her, Ron and Magnar.\n\n"
$ bios_name_sally = True
$ bios_history_magnar += "I played Dungeons and Gremlins with him, Ron and Sally.\n\n"
$ bios_name_magnar = True
$ chat_new_bios = True

label ep3_sage_hall_label:
play music "music/ep3/sunny_acoustic_rock.mp3"
scene ep3_mona with wipeleft
mn "Hey! You!"
mc "Me?"
mn "Yes! [name], right?"
scene ep3_mona1 with dissolve
mc "Yeah, that's me. Hi, Camila! And you are?"
scene ep3_mona2 with dissolve
mn "Wow... Way to leave an impression..."
mn "I'm Mona... I'm in your English and Math classes."
scene ep3_mona1 with dissolve
mc "Ah, that's right. Did you want anything? Class is starting soon."
scene ep3_mona4 with dissolve
mn "Um... Camila?"
cam "Yes! Mona and I are on a scavenger hunt and we need a pair of underwear from a guy."
scene ep3_mona1 with dissolve
mc "And I'm that guy?"
scene ep3_mona4 with dissolve
cam "If you want to be."
if not ep2_recommendedSage:
    scene ep3_mona1 with dissolve
    mc "I'm confused...isn't Maya doing this scavenger hunt with you?"
    scene ep3_mona4 with dissolve
    cam "Yeah, but she's off buying 10 packs of condoms. Haha!"
    if dtype > 0:
        scene ep3_mona1 with dissolve
        mc "Sounds like a fun night."
        scene ep3_mona4 with dissolve
        cam "Haha! Oh, stop it!"
scene ep3_mona10 with dissolve
mc "Is that Sage and Riona, over there?"
mn "Yeah, Sage is my mother and Riona is Camila's mother... They can't help us with this."
scene ep3_mona2 with dissolve
mn "Now, where did we land on getting that pair of underwear?"
scene ep3_mona1 with dissolve
menu:
    "Sure" if True:
        $ ep3_helpedCamilaAndMona = True
        $ bios_history_mona += "I helped Mona and Camila with their scavenger hunt.\n\n"
        $ bios_name_mona = True
        $ bios_history_camila += "I helped Mona and Camila with their scavenger hunt.\n\n"
        $ bios_name_camila = True
        $ chat_new_bios = True
        mc "Sure, but I can't just strip out here."
        scene ep3_mona2 with dissolve
        mn "Let's go to the bathroom!"
        label ep3_camila_lewd:
        if _in_replay:
            hide screen phone_screen
            if persistent.name == None:
                $ name = "MC"
            elif True:
                $ name = persistent.name
            if persistent.mc_camila == None:
                $ mc_camila = name
            elif True:
                $ mc_camila = persistent.mc_camila
            if persistent.camila == None:
                $ camila = "Camila"
            elif True:
                $ camila = persistent.camila
        scene ep3_mona13 with wiperight
        mc "What do you need these for? Like, what are you gonna do with them?"
        mn "No clue. We just show them to Sage and drop them off at the HOTs."
        scene ep3_mona15 with dissolve
        mn "*{i}Whispers{/i}* Stop it! What are you doing?"
        cam "*{i}Whispers{/i}* Shush! I'm just checking something..."
        mn "*{i}Whispers{/i}* You mean you're checking his thing!"
        cam "*{i}Whispers{/i}* Yeah, whatever!"
        scene ep3_mona16 with dissolve
        menu:
            "Give them the underwear" if not _in_replay:
                $ renpy.pause(0.5)
            "Call Camila out" if True:
                scene ep3_mona23 with dissolve
                mn "Are you done in there, yet?"
                scene ep3_mona16 with dissolve
                mc "I would be, if Camila wasn't waiting for her chance to catch a peek of my dick."
                scene ep3_mona24 with dissolve
                cam "Oh my gosh! I'm sorry!"
                mn "I told you to stop!"
                scene ep3_mona25 with dissolve
                mc "Did you see what you wanted to see?"
                scene ep3_mona25b with dissolve
                cam "Almost..."
                scene ep3_mona25 with dissolve
                menu:
                    "Tell her off" if not _in_replay:
                        mc "That's pretty humiliating."
                        scene ep3_mona25b with dissolve
                        cam "I'm sorry..."
                    "Show me yours (Huge {color=#ffffff}{size=-1}{font=collegiate.ttf}DIK{/font}{/size}{/color})" if dtype > 1 or _in_replay:
                        $ dk(1)
                        stop music fadeout 3
                        mc "(I better teach them a lesson.)"
                        play music "music/ep3/some_obsession.mp3"
                        mc "Ok. It's your turn now. Show me what you got."
                        scene ep3_mona27 with dissolve
                        mn "What?"
                        cam "For real?"
                        scene ep3_mona28 with dissolve
                        mc "Get in here!"
                        scene ep3_mona28b with dissolve
                        mc "Come on. Both of you."
                        mc "Consider it punishment for peeking and payment for the underwear."
                        mn "Fine! But not a word about this to anyone!"
                        scene ep3_mona29 with dissolve
                        mn "Is this what you want to see?"
                        mc "Yeah, Camila is definitely showing what I wanted to see."
                        scene ep3_mona29b with dissolve
                        mn "Haha, you slut! You're going commando, aren't you!?"
                        cam "What? Haha!"
                        scene ep3_mona29c with dissolve
                        mn "How about now?"
                        $ guideSuggestedPage = 83
                        menu:
                            "Stop" if not _in_replay:
                                stop music fadeout 3
                                mc "Thanks, that's enough."
                                play music "music/ep3/sunny_acoustic_rock.mp3"
                            "Continue" if True:
                                $ ep3_fuckedCamilaAndMona = True
                                $ dk(1)
                                mc "Nice! Now, strip and lose your tops, too."
                                scene ep3_mona30 with dissolve
                                mn "Are you joking!?"
                                scene ep3_mona29c with dissolve
                                mc "No, I'm not. I showed my dick, remember?"
                                scene ep3_mona30 with dissolve
                                mn "Only to Camila! I didn't see it."
                                play sound "sound_effects/zipper.mp3"
                                "*{i}Unzips pants{i}*"
                                mc "There!"
                                mn "Oh, wow!"
                                mc "Let's go."
                                scene ep3_mona31 with dissolve
                                mc "Perfect..."
                                mc "Now, turn around for me."
                                scene ep3_mona32 with dissolve
                                mn "Ok...what now?"
                                scene ep3_mona33 with dissolve
                                mc "I don't know... What do you think Camila?"
                                cam "I want it..."
                                mn "Camila!"
                                cam "What? I do!"
                                cam "Why do you think I peeked to begin with?"
                                mn "You're such a slut!"
                                cam "Don't act like you don't want it either."
                                scene ep3_mona36 with dissolve
                                cam "[name]... Put it into Mona...slowly..."
                                cam "I wanna see how her smile grows with pleasure..."
                                scene ep3_mona37 with dissolve
                                mn "Haha! I'm gonna get you for this..."
                                mn "Ok... Do it..."
                                scene ep3_mona38 with dissolve
                                $ renpy.pause()
                                scene ep3_mona39 with dissolve
                                mn "*{i}Moans{/i}* Oh! Damn! Hngh..."
                                scene anim_mona_doggy_ep3 with dissolve
                                mn "Oh, God! Fuck!"
                                mc "Shh! You don't want anyone to overhear us..."
                                $ ep3_currentSexStyle = 2
                                label ep3_camila_mona_loop_label:
                                menu:
                                    "Fuck Camila" if True:
                                        menu:
                                            "Doggystyle" if ep3_currentSexStyle != 0:
                                                $ ep3_currentSexStyle = 0
                                                scene ep3_mona40 with dissolve
                                                mc "Here we go... I'm gonna give you what you wanted..."
                                                scene anim_camila_doggy_ep3 with dissolve
                                                cam "*{i}Moans{/i}* Yes!!! [mc_camila]!"
                                                mn "Hngn... Yes!"
                                                $ renpy.pause()
                                                scene ep3_mona41 with dissolve
                                                mc "Shh! What is it with you two? Keep it down or I'll stop."
                                                scene anim_camila_doggy_ep3 with dissolve
                                                cam "Hngh... Mmm..."
                                                $ renpy.pause()
                                                jump ep3_camila_mona_loop_label
                                            "Face to face" if ep3_currentSexStyle != 1:
                                                $ ep3_currentSexStyle = 1
                                                scene anim_camila_face_ep3 with dissolve
                                                cam "*{i}Muffled moans{/i}*"
                                                mc "That's it [camila]... Stay silent and feel all of me."
                                                $ renpy.pause()
                                                scene anim_camila_face2_ep3 with dissolve
                                                cam "Mpfh..."
                                                mc "What's that? You're gonna cum?"
                                                mc "I'm not gonna stop..."
                                                mc "I want you to explode on my cock."
                                                scene ep3_camila_cum with hpunch
                                                $ renpy.pause(0.5)
                                                scene ep3_camila_cum with hpunch
                                                $ renpy.pause(0.5)
                                                scene ep3_camila_cum with hpunch
                                                cam "*{i}Loud moan{/i}* Oh, God!!!"
                                                scene anim_camila_face2_ep3 with dissolve
                                                $ renpy.pause()
                                                jump ep3_camila_mona_loop_label
                                    "Fuck Mona" if True:
                                        menu:
                                            "Doggystyle" if ep3_currentSexStyle != 2:
                                                $ ep3_currentSexStyle = 2
                                                scene anim_mona_doggy_ep3 with dissolve
                                                mc "You like it when I spank you, right?"
                                                mn "Hngh... Yes... Don't stop!"
                                                $ renpy.pause()
                                                jump ep3_camila_mona_loop_label
                                            "Cowgirl" if ep3_currentSexStyle != 3:
                                                $ ep3_currentSexStyle = 3
                                                scene ep3_mona40b with dissolve
                                                mc "Here. Get on me."
                                                mn "This guy loves to be in control, huh?"
                                                scene anim_mona_face2_ep3 with dissolve
                                                mc "Maybe you can cross this off your scavenger hunt, too?"
                                                mn "Mmm... Hah, I wish."
                                                $ renpy.pause()
                                                scene anim_mona_face_ep3 with dissolve
                                                $ renpy.pause()
                                                jump ep3_camila_mona_loop_label
                                    "Cum" if True:
                                        mc "Ok... I'm cumming!"
                                        menu:
                                            "Inside" if True:
                                                if ep3_currentSexStyle == 0:
                                                    scene ep3_camila_doggy_cum with hpunch
                                                    $ renpy.pause(0.5)
                                                    scene ep3_camila_doggy_cum with hpunch
                                                    $ renpy.pause(0.5)
                                                    scene ep3_camila_doggy_cum with hpunch
                                                    $ renpy.pause()
                                                    scene ep3_camila_doggy_cum2 with dissolve
                                                elif ep3_currentSexStyle == 1:
                                                    scene ep3_camila_face_cum with hpunch
                                                    $ renpy.pause(0.5)
                                                    scene ep3_camila_face_cum with hpunch
                                                    $ renpy.pause(0.5)
                                                    scene ep3_camila_face_cum with hpunch
                                                    $ renpy.pause()
                                                    scene ep3_camila_doggy_cum2 with dissolve
                                                elif ep3_currentSexStyle == 2:
                                                    scene ep3_mona39 with hpunch
                                                    $ renpy.pause(0.5)
                                                    scene ep3_mona39 with hpunch
                                                    $ renpy.pause(0.5)
                                                    scene ep3_mona39 with hpunch
                                                    $ renpy.pause()
                                                    scene ep3_mona_doggy_cum2 with dissolve
                                                elif True:
                                                    scene ep3_mona_face_cum with hpunch
                                                    $ renpy.pause(0.5)
                                                    scene ep3_mona_face_cum with hpunch
                                                    $ renpy.pause(0.5)
                                                    scene ep3_mona_face_cum with hpunch
                                                    $ renpy.pause()
                                                    scene ep3_mona_doggy_cum2 with dissolve
                                                stop music fadeout 3
                                                mc "Ahhh! That was so fucking good!"
                                            "Outside" if True:
                                                scene anim_cum_ep3 with dissolve
                                                mc "Get ready, girls! I'm gonna cum..."
                                                scene anim_cum2_ep3 with dissolve
                                                mc "Ahhh!"
                                                scene ep3_both_cum2 with dissolve
                                                mc "Haha, wow... You better clean each other up before heading back out there."
                                                cam "Mmm..."
                                                stop music fadeout 3
                                                mn "This guy's fun..."
                                $ renpy.end_replay()
                                $ persistent.ep3_lewd_camila = True
                                $ calcScenes()
                                $ bios_history_mona +="I fucked Mona and Camila in the school bathroom.\n\n"
                                $ bios_history_camila +="I fucked Mona and Camila in the school bathroom.\n\n"
                                $ bios_name_mona = True
                                $ bios_name_camila = True
                                $ chat_new_bios = True
                                play music "music/ep3/sunny_acoustic_rock.mp3"

        scene ep3_mona17 with dissolve
        mc "Here you go! One pair of underwear."
        mn "Thank you! You've been most helpful!"
        mn "Oh! You wouldn't happen to know where to find a rainbow-colored umbrella?"
        scene ep3_mona19 with dissolve
        mc "Is that really on your list?"
        cam "Lame, huh?"
        mc "Yeah, I have no clue."
        scene ep3_mona21 with dissolve
        mn "Anyway..."
        mn "Thanks for the help!"
    "Nope" if True:
        $ ep3_helpedCamilaAndMona = False
        $ bios_history_mona += "I didn't help Mona and Camila with their HOT scavenger hunt.\n\n"
        $ bios_history_camila += "I didn't help Mona and Camila with their HOT scavenger hunt.\n\n"
        $ bios_name_mona = True
        $ bios_name_camila = True
        $ chat_new_bios = True
        mc "No, sorry. I need my underwear. You'll have to find another guy."
        scene ep3_mona10b with dissolve
        mn "Dammit..."
        mn "Camila! Over there! Let's ask that guy!"
$ bios_mona = True
label ep3_english_label:
$ guideSuggestedPage = 83
if ep3_wearHelmet:
    scene ep3_english with wipeleft
elif True:
    scene ep3_englishb with wipeleft
de "Hey..."
de "Did you see what Dawe brought with him?"
if ep3_wearHelmet:
    scene ep3_english1 with dissolve
elif True:
    scene ep3_english1b with dissolve
mc "His shaker?"
mc "Shit...we're really doing this now?"
if ep3_wearHelmet:
    scene ep3_english2 with dissolve
elif True:
    scene ep3_english2b with dissolve
de "Damn straight! I didn't jizz into this for nothing."
mc "That's so gross..."
if ep3_dawe_prank:
    if ep3_wearHelmet:
        scene ep3_english4 with dissolve
    elif True:
        scene ep3_english4b with dissolve
    de "Here! Take it."
    if ep3_wearHelmet:
        scene ep3_english5 with dissolve
    elif True:
        scene ep3_english5b with dissolve
    mc "Dude... N-no!"
    if ep3_wearHelmet:
        scene ep3_english4 with dissolve
    elif True:
        scene ep3_english4b with dissolve
    de "You said you'd do it."
    if ep3_wearHelmet:
        scene ep3_english5 with dissolve
    elif True:
        scene ep3_english5b with dissolve
    mc "I don't know what I was thinking when I said that..."
    mc "I don't wanna touch something that was on your dick."
    if ep3_wearHelmet:
        scene ep3_english4 with dissolve
    elif True:
        scene ep3_english4b with dissolve
    de "Come on! You'll get used to it."
    if ep3_wearHelmet:
        scene ep3_english5 with dissolve
    elif True:
        scene ep3_english5b with dissolve
    mc "What!? I'm not gonna get used to it."
    if ep3_wearHelmet:
        scene ep3_english4 with dissolve
    elif True:
        scene ep3_english4b with dissolve
    de "Ok, let's do it like this..."
    de "I'll put it in your pocket and then you only have to touch it once."
    scene ep3_english10 with dissolve
    mc "Hey! I didn't agree to that!"
    de "It's in there now! Relax."
    de "Now we just wait until there's a break and we'll do it."
    if ep3_wearHelmet:
        scene ep3_english1 with dissolve
    elif True:
        scene ep3_english1b with dissolve
    mc "You're telling me I have to sit in class with your cum in my pants until then?"
    scene ep3_english13 with dissolve
    my "I...did so not hear that."
elif True:
    if ep3_wearHelmet:
        scene ep3_english4 with dissolve
    elif True:
        scene ep3_english4b with dissolve
    de "How is it gross? It's just cum."
    de "It was inside my balls 10 minutes ago and now it's here."
    if ep3_wearHelmet:
        scene ep3_english5 with dissolve
    elif True:
        scene ep3_english5b with dissolve
    mc "That's too much information."
    if ep3_wearHelmet:
        scene ep3_english4 with dissolve
    elif True:
        scene ep3_english4b with dissolve
    de "No, too much information would be if I told you that I thought about Camila when spanking it."
    de "What I said was just information."
    if ep3_wearHelmet:
        scene ep3_english5 with dissolve
    elif True:
        scene ep3_english5b with dissolve
    mc "So, what's next?"
    if ep3_wearHelmet:
        scene ep3_english4 with dissolve
    elif True:
        scene ep3_english4b with dissolve
    de "We either create a distraction or wait for one."
    de "As soon as I get the chance, I'll pop it in his shaker and you film it."
scene ep3_english19a with dissolve
mc "(Cathy is dressing casually at work? That's new...)"
scene ep3_english19 with dissolve
ca "Guess what, class? It's time for another quiz!"
stop music fadeout 3
scene ep3_english20 with dissolve
dw "YOU'VE GOTTA BE KIDDING ME!"
if not minigames:
    scene black with Fade(1.5, 1, 0.5)
    jump ep3_after_english_test
play music "music/ep3/sing_along_with_jim.mp3"
scene english_test_board
jump english101_test3
label ep3_after_english_test:
$ renpy.block_rollback()
if minigames:
    scene ep3_english21 with wiperight
    stop music fadeout 3
elif True:
    scene ep3_english21 with fade
play music "music/ep1/scrapbook.mp3"
an "*{i}Whispers{/i}* Dawe...don't be stupid. Put that away."
dw "*{i}Whispers{/i}* I'm not being stupid, I'm being crafty."
an "*{i}Whispers{/i}* Can you look up number four for me?"
ca "Boys. Is that a phone?"
scene ep3_english24 with dissolve
dw "I'm...waiting for a very important phone call."
ca "Hallway. Now!"
scene ep3_english26 with dissolve
$ renpy.pause()
if ep3_dawe_prank:
    scene ep3_english27 with dissolve
    mc "(Here it goes...)"
    mc "(This is so sick...)"
elif True:
    scene ep3_english28 with dissolve
    mc "(He's really doing it...)"
    mc "(I've got to record it...)"
scene ep3_english29 with dissolve
ca "This is your final warning, boys..."
if ep3_wearHelmet:
    scene ep3_english30b with dissolve
elif True:
    scene ep3_english30 with dissolve
$ renpy.pause()
scene ep3_english19 with fade
ca "Class dismissed."
scene ep3_english32 with dissolve
mc "Hey, he didn't drink it, yet. Did he?"
de "Nope. I got a pain in my neck from checking every minute."
de "Let's follow him and see if he drinks..."
scene ep3_english34 with dissolve
mc "Come on... Just drink it..."
mc "Or this prank is no good..."
scene ep3_english36 with dissolve
if ep2_danceSage or ep2_fuckHOT:
    de "Hey, that's the redhead me and Jacob double-teamed."
    mc "Seriously? You went through with that?"
    mc "I just thought he asked you to do it."
    mc "That's Dawe's girl."
    de "Really? What are the odds?"
elif True:
    de "Hey, that's the redhead I like."
    mc "Seriously? That one?"
    mc "I think she's Dawe's girl."
    de "Really? That's a shame."
scene ep3_english38 with dissolve
de "Look! Look! He's drinking. Get that camera ready!"
mc "Oh my God! He's really drinking all of it!"
mc "This is so bad..."
de "This is gonna be great!"
scene ep3_english39 with dissolve
dw "Arieth...you need to stop dodging my phone calls..."
dw "I wanna have a talk with you."
scene ep3_english39b with dissolve
ar "I'm not dodging them... I've been busy."
scene ep3_english39 with dissolve
dw "Anyway... I still want to have a..."
scene ep3_english39c with dissolve
dw "Hmph..."
ar "What's up with you?"
scene ep3_english41 with dissolve
dw "There's something weird with my protein shake..."
dw "I think it was thicker than usual."
ar "You have to shake it more to get out the lumps."
scene ep3_english43 with dissolve
dw "Don't you think I know how to shake a protein shake, by now!?"
"*{i}Slosh thud slosh{/i}*"
dw "Hm...?"
scene ep3_english45 with dissolve
dw "What the fuck...is that a..."
dw "Hngh..."
scene ep3_english47 with hpunch
dw "*{i}Blargh{/i}*"
ar "AHH!!! YOU SICKO!"
scene ep3_english48 with dissolve
dw "I've been poisoned!"
de "Yes, we got it!"
dw "Oh, shit... Hngh..."
dw "*{i}Blargh{/i}*"
$ bios_history_dawe += "Derek and I pranked Dawe. He puked on his girlfriend, Arieth.\n\n"
$ bios_name_dawe = True
$ chat_new_bios = True

label ep3_gender_studies_label:
if ep3_wearHelmet:
    scene ep3_genderb with wipeleft
elif True:
    scene ep3_gender with wipeleft
de "We're on fucking fire, [mc_de]!"
de "At this rate we're gonna complete most of the tasks before Saturday!"
if ep3_wearHelmet:
    scene ep3_gender1b2 with dissolve
elif True:
    scene ep3_gender1b with dissolve
mc "We still have the really hard ones left..."
mc "Speak of the devil..."
scene ep3_gender1c with dissolve
de "Damn, she's so fucking hot."
if ep3_hellWeekTryFuckJade:
    de "I can't believe that you're gonna fuck her."
    mc "You're speaking as if it's a given."
    de "Well, it is! She flashed you!"
    mc "Maybe she just was looking for a thrill... I don't know."
    de "Then find out."
elif True:
    de "Are you sure you don't wanna try fucking her?"
    mc "Go ahead and try if you want to. I'm not doing it."
if ep3_wearHelmet:
    scene ep3_gender1e with dissolve
    de "Hey, gimme the helmet."
    mc "You're volunteering to wear that in this class?"
    scene ep3_gender1g with dissolve
    de "Most of these women already hate me."
    de "This helmet won't change a thing."

scene ep3_gender1h with dissolve
ja "Good afternoon, class."
ja "Are we feeling up for some proper discussions?"
scene ep3_gender1i with dissolve
ja "Today I want you to engage in a conversation about the difference between sex and gender."
ja "I trust that you all did your homework and read up on the topic."

scene ep3_gender1 with dissolve
$ renpy.pause()
scene ep3_gender1i with dissolve
ja "What are you waiting for? Go ahead and pair up."
scene ep3_gender3 with dissolve
de "Hey, hey! Don't go, [mc_de]!"
de "Let's do this one together."
scene ep3_gender4 with dissolve
mc "I'm not sure Jade would like that."
scene ep3_gender3 with dissolve
de "I'm sure she won't mind!"
de "Here! I'll start!"
play music "music/ep1/radio_martini.mp3"
scene ep3_gender6 with dissolve
de "What's the deal with vaginas?"
de "They are either dry or wet. Am I right?"
scene ep3_gender7 with dissolve
menu:
    "Agree" if True:
        mc "Yeah, I guess that's a bit of a mystery."
    "Disagree" if True:
        mc "Well, not all the time."
scene ep3_gender7b with dissolve
de "That's a very interesting standpoint."
scene ep3_gender6 with dissolve
de "They come in so many different shapes, too!"
de "One time I saw a vagina that looked like a pair of clown's lips."
de "You know...the really red and big ones."
scene ep3_gender7 with dissolve
menu:
    "Whose were they?" if True:
        mc "Whose were they?"
        scene ep3_gender7b with dissolve
        de "You know what...? I don't recall."
        de "I was very young when that happened and it may have been a dream."
    "Clown's lips?" if True:
        mc "Really? Clown's lips?"
        scene ep3_gender7b with dissolve
        de "Yes! All that was missing was red pubes for a wig."
        de "True story."
scene ep3_gender6 with dissolve
$ guideSuggestedPage = 84
de "What's your favorite kind of vagina, [mc_de]?"
scene ep3_gender7d with dissolve
$ renpy.pause()
scene ep3_gender7 with dissolve
menu:
    "The shaven one" if True:
        mc "I'm gonna say the shaven one."
        scene ep3_gender6 with dissolve
        de "Huh... That's an excellent argument!"
        de "I can tell that you've read the literature for this!"
    "The hairy one" if True:
        mc "I like them hairy."
        scene ep3_gender6 with dissolve
        de "The hairier the merrier!"
        de "I totally agree!"
    "No preference" if True:
        mc "I don't have a preference, really."
        scene ep3_gender6 with dissolve
        de "Pussy is indeed pussy."
        de "You couldn't be more right about that, [mc_de]!"
stop music
scene ep3_gender8
ja "Derek..."
ja "This class will be more meaningful if you were to pair up with someone who has a different opinion than yours and challenges you."
play sound "sound_effects/table_slam.mp3"
scene ep3_gender9 with vpunch
de "No! No more! Every time now!"
de "Every fucking time I've been paired up with Wendy!"
de "That ends today!"
scene ep3_gender10 with dissolve
de "I want to be with my buddy!"
de "He and I will sit here and we will discuss vaginas."
scene ep3_gender11
de "Kill me. Someone please...just kill me."
play music "music/ep3/black_box.mp3"
scene ep3_gender12 with dissolve
ja "Hm, it looks like we're one student short today."
mc "It seems so..."
ja "Then you're with me."
scene ep3_gender14 with dissolve
ja "Come, let's sit in the back where we don't bother the rest of the class."
scene ep3_gender14b with dissolve
$ renpy.pause()
scene ep3_gender14c with dissolve
ja "Take a seat..."
scene ep3_gender15 with dissolve
ja "So...[name]."
ja "Now is your chance to talk for a change."
scene ep3_gender16 with dissolve
mc "Haha, yeah! I guess you're right."
mc "..."
scene ep3_gender17 with dissolve
ja "What's the matter?"
scene ep3_gender16 with dissolve
mc "I have no idea what I should talk about."
scene ep3_gender17 with dissolve
ja "The topic is the difference between gender and sex."
ja "What comes to mind when you hear those words?"
scene ep3_gender16 with dissolve
mc "Um... Gender is like male or female...right?"
scene ep3_gender17 with dissolve
ja "Did you read the literature?"
scene ep3_gender16 with dissolve
mc "Sorry... No, this week has been crazy, with all the hazing I didn't find time to do it."
scene ep3_gender17 with dissolve
ja "Ok... Let me hear your personal views on it, then."
ja "You said gender is male or female. In which ways?"
scene ep3_gender16 with dissolve
mc "You know..."
mc "Biological ways."
scene ep3_gender17 with dissolve
ja "Then what would sex be?"
scene ep3_gender16 with dissolve
mc "Um... The same thing, maybe?"
mc "I don't know."
scene ep3_gender15 with dissolve
ja "At least you didn't say it's a verb."
scene ep3_gender16 with dissolve
mc "Haha."
scene ep3_gender_jade1 with dissolve
ja "Commonly, sex refers to the biological elements."
ja "Females have vaginas..."
scene ep3_gender_jade2 with dissolve
$ renpy.pause(0.5)
scene ep3_gender_jade3 with dissolve
mc "(She just flashed me again! What the hell?)"
ja "And males have..."
scene ep3_gender_jade4 with dissolve
ja "Cocks."
mc "(Oh, shit! She's going for it!)"
ja "While sex stems from biology..."
ja "...gender, on the other hand, can mean so much more."
mc "(She isn't letting go. Is she crazy!?)"
show screen majorChoiceScale
menu:
    "Take it further" if True:
        stop music fadeout 3
        $ bios_history_mc += "Jade and I had some \"fun\" during Gender Studies class.\n\n"
        $ bios_name_mc = True
        $ bios_history_jade += "Jade and I had some \"fun\" during Gender Studies class.\n\n"
        $ bios_name_jade = True
        $ chat_new_bios = True
        if not persistent.bg_jade_alt_unlocked:
            $ persistent.bg_jade_alt_unlocked = True
            $ chat_new_bg = True
            $ calcWallpapers()
        $ ep3_acceptedJade = True
        $ addCPenalty()
        $ renpy.pause(1)
        hide screen majorChoiceScale
    "Stop her" if True:
        stop music fadeout 3
        $ bios_history_mc += "I rejected Jade when she flirted with me during class.\n\n"
        $ bios_name_mc = True
        $ bios_history_jade += "I rejected Jade when she flirted with me during class.\n\n"
        $ bios_name_jade = True
        $ chat_new_bios = True
        $ ep3_acceptedJade = False
        $ addDPenalty()
        $ renpy.pause(1)
        hide screen majorChoiceScale
        scene ep3_gender_jade4b with dissolve
        $ renpy.pause()
        scene ep3_gender_jade4c with dissolve
        ja "You should spend the time left in this class reading and be {b}quiet{/b}..."
        ja "That way I might not fail you..."
        jump ep3_after_gender_label
label ep3_lewd_jade_label:
hide screen phone_screen
if _in_replay:
    hide screen phone_screen
    if persistent.name == None:
        $ name = "MC"
    elif True:
        $ name = persistent.name
    if persistent.mc_jade == None:
        $ mc_jade = name
    elif True:
        $ mc_jade = persistent.mc_jade
    if persistent.jade == None:
        $ jade = "Jade"
    elif True:
        $ jade = persistent.jade
        scene ep3_gender_jade4 with dissolve

mc "(What if a student should see what she's doing?)"
mc "(But we're pretty hidden over here...)"
mc "(...and I'm not the one to turn a hot woman like her down.)"
scene ep3_gender_jade5 with dissolve
play music "music/ep1/slow_day_blues.mp3"
mc "(Let's find out if she's serious or not.)"
scene ep3_gender_jade6 with dissolve
ja "(I've actually taken the step...)"
ja "(That was...easy...)"
ja "(Not to mention fucking exciting!)"
scene ep3_gender_jade7 with dissolve
ja "(And he seems to be following my lead.)"
scene anim_jade_footjob_ep3 with dissolve:
    size (config.screen_width, config.screen_height)
ja "(I can't believe that I'm doing this during class with a student...)"
ja "(It's grounds for dismissal, not to mention a lot of additional trouble...)"
ja "(That's what makes it so fucking hot!)"
ja "(I still must act normally. I can't risk anyone seeing this.)"
scene ep3_gender_jade7 with dissolve
ja "Uh... Gender can mean roles that individuals assume in society and in their personal lives."
scene anim_jade_footjob2_ep3 with dissolve:
    size (config.screen_width, config.screen_height)
mc "(Look at her doing that so casually.)"
mc "(She's a fucking pro...)"
mc "(I wonder how many times she's done this before...)"
ja "Just because your sex is male doesn't mean that you identify as such. Thus, your gender role is different."
scene anim_jade_footjob3_ep3 with dissolve:
    size (config.screen_width, config.screen_height)
mc "(Her feet are so soft and smooth...)"
mc "(They smell of perfume and lotion...)"
mc "(I love how she alternates between stroking the tip and the shaft...)"
mc "(She does it so effortlessly.)"
scene ep3_jade_pussy with dissolve
mc "(I wonder how she reacts if I try to touch her pussy...)"
ja "In today's society-uh..."
scene ep3_jade_pussy2 with dissolve
ja "(This boy is really trying to test me...)"
scene ep3_jade_pussy3 with dissolve
ja "(But he's not the one in charge here.)"
ja "(I'm gonna make that perfectly clear.)"
scene anim_jade_handjob2_ep3 with dissolve:
    size (config.screen_width, config.screen_height)
ja "As I was saying..."
ja "In today's society there's a growing acceptance of gender neutrality and identification."
mc "(How the hell did I end up getting a handjob in class from one of the hottest teachers I've ever seen?)"
scene anim_jade_handjob_ep3 with dissolve:
    size (config.screen_width, config.screen_height)
mc "(Oh, God! It's even better than when I do it myself.)"
mc "(Her wrist is moving so sexy as she's jerking me off.)"
mc "(She has such a great technique. She knows exactly how to squeeze it.)"
stu "Jade?"
mc "(Oh, fuck!)"
scene ep3_jade_student1 with dissolve
ja "Um. Yes?"
dn "I'm sorry to interrupt, but I have a question."
mc "(Fuck... Just when it started to get good.)"
ja "Yes? What's your question?"
scene anim_jade_handjob3_ep3 with dissolve:
    size (config.screen_width, config.screen_height)
mc "(She's...not stopping!)"
mc "(She's out of her mind!)"
mc "(If that student sees her doing this, we're both screwed!)"
scene ep3_jade_student1 with dissolve
dn "Would you say that an individual with the male sex identifying with a female gender is female or male?"
dn "Which takes precedence, biology or the individual's perception?"
ja "It is an excellent philosophical question."
scene ep3_jade_student2 with dissolve
ja "What do you think about this, [name]?"
scene anim_jade_handjob4_ep3 with dissolve:
    size (config.screen_width, config.screen_height)
mc "(Man... I'm gonna bust soon.)"
pause
ja "[name]?"
mc "Huh?"
scene ep3_jade_student2 with dissolve
ja "What do you think a biological male identifying as a female should be called? Male or female?"
scene ep3_jade_student5 with dissolve
menu:
    "Male" if True:
        mc "Uh... A male!"
        scene anim_jade_handjob4_ep3 with dissolve:
            size (config.screen_width, config.screen_height)
        ja "Interesting. [name] here has chosen sex to be more important than gender in classification of individuals."
        ja "It's often a loaded topic and this stance is very bold to take in today's society."
        ja "While your answer isn't incorrect, the other answer is also true."
        ja "That's why tolerance is important."
    "Female" if True:
        mc "A female... Yes! A female."
        scene anim_jade_handjob4_ep3 with dissolve:
            size (config.screen_width, config.screen_height)
        ja "[name] here has adopted the view that it's the choice of the individual that matters."
        ja "It's very common today and mostly accepted."
        ja "The gender identification can however never change the fact that sex also defines an individual."
        ja "That's why tolerance is so important."
mc "(Shit! I'm coming!)"
scene bg anim_jade_handjob_cum_ep3 movie with dissolve:
    size (config.screen_width, config.screen_height)
$ renpy.pause(2.5)
play sound "sound_effects/table_slam.mp3"
scene ep3_jade_student5 with vpunch
mc "Yes! Yes! Yes!!!"
mc "..."
mc "So important!"
scene ep3_jade_student1 with dissolve
dn "Uh. Thanks, Jade..."
scene ep3_jade_student8 with dissolve
ja "I hope you felt today's class got you some release."
scene ep3_jade_student9 with dissolve
ja "Keep this up and I'm sure you will pass with the highest grade."
stop music fadeout 3
scene ep3_jade_student10 with dissolve
mc "Maybe I could get some private courses to pass it easier...?"
scene ep3_jade_student11 with dissolve
ja "I'll see what I can do..."
$ renpy.end_replay()
$ persistent.ep3_lewd_jade = True
$ calcScenes()
show screen phone_screen
label ep3_after_gender_label:
play music "music/ep1/someways.mp3"
scene ep3_gender_wendy with dissolve
de "Not surprising!"
de "You're wrong, again, Wendy!"
de "Nature doesn't lie!"
de "Just because you chop your dick off doesn't mean you're a woman!"
de "Would you call a banana a peach just because you cut it halfway and magically tucked it in?"
de "Or would you call it a disgusting and mushed banana?"
scene ep3_gender_wendy1 with dissolve
de "And just because you decide to, you can't be gender neutral!"
de "Look at the fucking DNA!"
de "There's XX and XY and some weird ass mutations that still makes you a woman."
de "Where's that neutral person!? Where is it?"
scene ep3_gender_wendy4 with dissolve
wen "You're confusing sex and gender! Did you even read your homework!?"
wen "Oh! And also! What about hermaphrodites!?"
wen "They have both a penis and a vagina!"
scene ep3_gender_wendy5 with dissolve
de "Fuck me. She actually made a good point."
scene ep3_gender_wendy1 with dissolve
de "Since we're all women in the earliest stages of life I would call it a male due to the penis."
scene ep3_gender_wendy4 with dissolve
wen "But they aren't just a male!"
scene ep3_gender_wendy1 with dissolve
de "A male with some extra holes, then. A swiss male!"
scene ep3_gender_wendy4 with dissolve
wen "You're so fucking stupid!"
scene ep3_gender_wendy with dissolve
de "Great argument, Wendy!"
de "Argue the point instead of insulting me!"
scene ep3_gender_wendy4 with dissolve
wen "I'm so sick of you!"
scene ep3_gender_wendy with dissolve
de "Me too, Wendy! And so are all others in here as well."
scene ep3_gender_wendy6 with dissolve
stop music fadeout 5
de "Apparently, we're {b}both{/b} at the bottom of the food chain in this class!"

label ep3_after_gender2_label:
play music "music/ep3/get_back.mp3"
if ep3_acceptedJade:
    scene ep3_dik_board10 with wiperight
    de "You really got the golden opportunity now, [mc_de]!"
    de "Fucking a teacher! No one is expecting us to complete that one!"
    de "It's too good to be true!"
    scene ep3_dik_board1 with dissolve
    mc "Yeah, I suggested some \"private courses\" and she said that she will look into it."
    mc "The difficult part will be to get the proof..."
    scene ep3_dik_board13 with dissolve
    de "Just grab your phone as you fuck her and then get out of there!"
    de "I mean, this is just about the pledge board, right?"
    scene ep3_dik_board1 with dissolve
    mc "Yeah... I don't know... I don't want to make things awkward, though."
    mc "And if she sees that we're doing that...there might be more trouble than doing it without her noticing."
    mc "How about something else? Like taking a photo through a pair of binoculars?"
    scene ep3_dik_board2 with dissolve
    de "Nah, that's gonna be too tricky and it depends on where you're fucking her, too!"
    scene ep3_dik_board1 with dissolve
    mc "Maybe at her place? But her husband's gonna be a problem..."
    scene ep3_dik_board2 with dissolve
    de "Maybe a hotel?"
    scene ep3_dik_board1 with dissolve
    mc "Yeah... Maybe."
    mc "We can think of the details if she suggests it..."
    scene ep3_dik_board10 with dissolve
    de "If {b}she{/b} suggests it?"
    de "We don't have a lot of time to just sit around and wait for her to do it."
    de "You've gotta show her that you want her! That's the only way to make it work."
    de "Be more forward with her! And the next time you see her, make sure you ask her up front to bang her."
elif True:
    scene ep3_dik_board3 with wiperight
    de "Let me get this straight..."
    de "She had her foot on your dick...in class...and you turned her down."
    scene ep3_dik_board4 with dissolve
    mc "Yes."
    scene ep3_dik_board3 with dissolve
    de "Why!?"
    scene ep3_dik_board4 with dissolve
    mc "Because I decided I don't want to do it."
    mc "Why are you acting like this? When I told you about my crush, you were concerned about Maya and now you want me to fuck Jade."
    mc "Double standards, much?"
    scene ep3_dik_board3 with dissolve
    de "It's just...the pledge board!"
    scene ep3_dik_board4 with dissolve
    mc "Fuck the pledge board."
    scene ep3_dik_board5 with dissolve
    de "*Gasps* Fuck the pledge board?"
    mc "I mean..."
    mc "I'm not going to fuck someone just because it's on a pledge board."
    mc "That's not how I work. I need to want it, to do it."
    scene ep3_dik_board6 with dissolve
    de "I know you're right. But it still sucks, you know?"
    de "I haven't met a teacher who wants to fuck me, yet!"
    de "I jiggle my ass in front of Cathy and I get nothing!"
    de "I've tried looking for other teachers, but I only find male ones."
    scene ep3_dik_board7 with dissolve
    de "..."
    mc "You're not gonna fuck a male teacher, are you?"
    scene ep3_dik_board7b with dissolve
    de "It's for the pledge board..."
    scene ep3_dik_board7 with dissolve
    mc "Dude...are you serious?"
    scene ep3_dik_board7b with dissolve
    de "I'm pretty sure I'd hate every second of it..."
    scene ep3_dik_board9b with dissolve
    de "Then again, it's college... You should be experimenting."
    mc "Just...leave me out of it."

scene ep3_dik_board with dissolve
mc "Look at that pledge board..."
mc "It feels like we've done a lot..."
mc "...but we've barely made a dent!"
mc "Just the gay guard catcher, the stripper signature and the prank..."
mc "There are only three days to go!"
de "Don't be like that! We're well on our way with several of those tasks."
de "Wanna wear the helmet?"
menu:
    "Wear helmet" if True:
        scene ep3_dik_board12 with dissolve
        $ ep3_wearHelmet = True
        $ ep3_mansionHelmet = True
        $ ep3_hellWeekHelmet += 1
        mc "Yeah, give it here. It's my turn."
    "Don't wear it" if True:
        $ ep3_wearHelmet = False
        $ ep3_mansionHelmet = False
        mc "No, you can keep it."
if ep3_wearHelmet:
    scene ep3_dik_board13b with dissolve
elif True:
    scene ep3_dik_board13 with dissolve
de "All right... I'm off to find someone to bang."
de "What will you be up to?"
stop music fadeout 3
mc "I'm going to pay Jill another visit. I owe her something."

label ep3_ano_label:
play music "music/ep2/freedom.mp3"
if ep3_wearHelmet:
    scene ep3_mansion with wipeleft
elif True:
    scene ep3_mansionb with wipeleft
mc "Excuse me?"
scene ep3_mansion1 with dissolve
sec "Yes?"
scene ep3_mansion2 with dissolve
mc "I'm wondering if you would let me in?"
mc "I'm here to see Jill."
scene ep3_mansion1 with dissolve
sec "Does she know that you're coming?"
scene ep3_mansion2 with dissolve
mc "No, it's more of a surprise visit."
scene ep3_mansion1 with dissolve
sec "Sorry, we don't do those here."
sec "You can call her and have her tell me to open the gates for you."
scene ep3_mansion2 with dissolve
mc "I don't have her number."
ty "What's this?"
scene ep3_mansion4 with dissolve
sec "Good evening, sir."
sec "There's an unannounced visitor for Ms. Jill-"
scene ep3_mansion6 with dissolve
ty "Shush. This boy cannot be allowed to enter the premises."
ty "With the burglary and all, we have to be stringent."
if ep3_wearHelmet:
    ty "And that...thing...on his head should have been your first clue on what to do."
scene ep3_mansion7 with dissolve
sec "I'm sorry, sir."
sec "You heard him. No entrance allowed."
stop music fadeout 3
sec "Please step away from the gates."
hide screen phone_screen
if ep3_wearHelmet:
    scene ep3_mansion10b with wiperight
elif True:
    scene ep3_mansion10 with wiperight
play music "music/ep2/marty.mp3"
mc "(I'm not giving up that easily.)"
mc "(Ok. Let's do this, again.)"
mc "(I can't climb up the pillars with the guitar, this time.)"
mc "(I better find another way inside.)"
jump ep3_ano_freeroam

label ep3_after_ano_freeroam_label:
show screen phone_screen
stop music fadeout 3
if ep3_wearHelmet:
    scene ep3_mansion11 with dissolve
elif True:
    scene ep3_mansion11b with dissolve
play sound "sound_effects/door_knock.mp3"
"*{i}Door knocking{/i}*"
scene ep3_mansion12 with dissolve
ji "[name]? What are you doing here?"
if not ep3_jillHelmetChad and not ep3_jillHelmetLibrary and ep3_wearHelmet:
    ji "And what is that you're wearing?"
    scene ep3_mansion13 with dissolve
    mc "Ah, it's a part of Hell Week. I know, it's stupid."
    mc "I wanted to see you, but I didn't have your number so I had to improvise."
elif True:
    scene ep3_mansion13 with dissolve
    mc "Hey! I wanted to see you, but I didn't have your number so I had to improvise."
scene ep3_mansion12 with dissolve
ji "Huh? I'm surprised they let you in."
$ guideSuggestedPage = 85
scene ep3_mansion13 with dissolve
menu:
    "Be honest" if True:
        $ ep3_honestWithJill = True
        mc "They didn't...I had to climb the walls."
        scene ep3_mansion16 with dissolve
        ji "[name]... You can't do that."
        scene ep3_mansion13 with dissolve
        mc "I'm sorry, but what choice did I have?"
        mc "To scream until you heard me?"
        scene ep3_mansion16 with dissolve
        ji "You could have asked the security guard to call me?"
        scene ep3_mansion13 with dissolve
        mc "Tybalt told him to not let me in."
    "Hide the truth" if True:
        $ ep3_honestWithJill = False
        mc "What can I say? I'm adorable."
scene ep3_mansion16 with dissolve
ji "Well, we've recently had a break-in, so security is on high alert."
ji "Come on in."
scene ep3_mansion22 with dissolve
ji "You brought your guitar?"
mc "Yes, sit down and just listen."
scene ep3_mansion24 with dissolve
ji "But...why?"
scene ep3_mansion23 with dissolve
mc "I'm making things up to you."
mc "For being a jerk yesterday and also for walking in on you playing the piano."
mc "I noticed how weird it felt when you realized that I heard you play..."
mc "So, I thought I could even things out for us."
scene ep3_mansion24 with dissolve
ji "Ok...?"
scene ep3_mansion26 with dissolve
play music "music/ep1/apra_hyde.mp3"
show text "Click to continue" with dissolve:
    xpos 0.5
    ypos 0.9
$ renpy.pause(2)
hide text "Click to continue" with dissolve
$ renpy.pause()
stop music
scene ep3_mansion27 with dissolve
mc "Now we're even."
mc "That was a very personal song I just played for you."
scene ep3_mansion28 with dissolve
ji "You're really talented. I loved it."
ji "You know...that's Bella's favorite song."
scene ep3_mansion27 with dissolve
mc "Oh, yeah! I forgot, she told me that."
scene ep3_mansion28 with dissolve
ji "Do you play any classical music?"
scene ep3_mansion27 with dissolve
mc "No, the fingering in those songs is very tricky for me."
scene ep3_mansion28 with dissolve
ji "Didn't they teach you that in class?"
scene ep3_mansion27 with dissolve
mc "I never took any music classes, I learned everything I know on my own."
scene ep3_mansion28 with dissolve
ji "Then it's even more impressive."
ji "And yes...we're even."
scene ep3_mansion27 with dissolve
mc "Great! Because I would love to hear you play again!"
scene ep3_mansion29 with dissolve
ji "You what?"
scene ep3_mansion27 with dissolve
mc "I haven't been able to get that melody you played off my mind."
scene ep3_mansion28 with dissolve
ji "All right... Let's go to the west wing."
ji "My piano is there."
scene ep3_mansion37 with wipeleft
mc "This is your piano?"
scene ep3_mansion38 with dissolve
ji "Yes, my dad bought it for my tenth birthday."
scene ep3_mansion37 with dissolve
mc "It's a beautiful instrument."
play music "music/ep3/gentle_theme_piano.mp3"
scene ep3_mansion39 with dissolve
$ renpy.pause(13)
show text "Click to continue" with dissolve:
    xpos 0.5
    ypos 0.9
$ renpy.pause(2)
hide text "Click to continue" with dissolve
$ renpy.pause()
mc "Oh, wow. What a song!"
ji "Did you ever learn to read sheet music?"
mc "I know the basics, but I can't figure it out while playing."
mc "So, I'm not...um...fluent or what you'd call it."
ji "Take a look and see if you understand something while I play, then."
ji "I should be fine without it, for this song."

scene ep3_mansion40 with dissolve
mc "(Hm...no, this is going way too fast for me.)"
mc "(And I can't really focus standing this close to her...)"
menu:
    "Check her out" if True:
        $ dk(1)
        scene ep3_mansion41 with dissolve
        mc "*{i}Gulp{/i}*"
        ji "Can you see them?"
    "Don't risk it" if True:
        $ dk(-1)
        ji "Can you see them?"
mc "Um...what?"
ji "The notes I'm playing."
scene ep3_mansion42 with dissolve
mc "Yeah, but I don't quite understand where you are in the song."
mc "Would you mind if I snapped a photo of the sheet? Just so I can study it later."
ji "Please, go ahead."
stop music fadeout 3
mc "Thanks."
scene ep3_mansion44 with dissolve
mc "It's a beautiful song. The melody really sticks with you."
play music "music/ep2/journey_of_hope.mp3"
mc "I was thinking..."
mc "Since you practiced in the auditorium before and not in here..."
mc "...are you reciting for a performance or something?"
scene ep3_mansion45 with dissolve
ji "You're sharp."
if ep3_wearHelmet:
    ji "Which is weird considering what you're wearing right now."
ji "Yes, once in a while the campus has concerts in the auditorium."
ji "I've been invited to perform in one of them."
scene ep3_mansion46 with dissolve
ji "And I'm a bit nervous and really like to be prepared...so..."
scene ep3_mansion44 with dissolve
mc "You're already practicing like crazy, huh?"
scene ep3_mansion46 with dissolve
ji "Yes. I don't do big audiences."
ji "It's been a dream of mine to do it...but my nerves..."
ji "I'm not a performer."
scene ep3_mansion50 with dissolve
menu:
    "Check her out" if True:
        $ dk(1)
        scene ep3_mansion50b with dissolve
        $ renpy.pause()
        scene ep3_mansion50 with dissolve
    "Don't check her out" if True:
        $ dk(-1)
mc "That's why you acted strange when I saw you play?"
ji "..."
mc "It really was a wonderful song."
ji "Thank you."
ji "I think so, too."
mc "I think you can do it. Just keep practicing until you're confident."
scene ep3_mansion54 with dissolve
ji "You think?"
scene ep3_mansion55 with dissolve
mc "Hey, I can be your audience. I'd love to hear you play more."
mc "It's the first time I've had the luxury to hear great piano music up close."
scene ep3_mansion56 with dissolve
$ renpy.pause()
if ep3_bella_came_around:
    scene ep3_mansion57 with dissolve
    ji "What did you do to make Bella come around?"
    scene ep3_mansion55 with dissolve
    mc "Um...nothing."
    mc "Wait...she came around?"
    scene ep3_mansion57 with dissolve
    ji "She did."
    ji "What did you tell her?"
    scene ep3_mansion55 with dissolve
    mc "I...ah...have no idea, really."
    mc "I thought she didn't like me that much."
    scene ep3_mansion57 with dissolve
    ji "Well...you're wrong."
    ji "She told me to give you a chance."
    scene ep3_mansion62 with dissolve
    ji "She does like you."
    ji "And I think you're-"
elif True:
    scene ep3_mansion57 with dissolve
    ji "Why don't you get along with Bella?"
    scene ep3_mansion55 with dissolve
    mc "I can't be the only one who's not getting along with her...right?"
    scene ep3_mansion57 with dissolve
    ji "No...but what did you tell her?"
    scene ep3_mansion55 with dissolve
    mc "I...ah...have no idea, really."
    mc "I just get the feeling that she doesn't like anything I say or do."
    scene ep3_mansion57 with dissolve
    ji "Well...you're not wrong."
    ji "I guess I just look at you differently from her..."
    scene ep3_mansion62 with dissolve
    ji "Because, I think you're-"
scene ep3_mansion63
ty "You are an absolute mad man, Rich!"
ty "That's another perfect challenge for our new protégés."
ty "One bottle of champagne and a beer glass is coming right-"
scene ep3_mansion64 with dissolve
ty "Huh!"
if ep3_wearHelmet:
    scene ep3_mansion66b with dissolve
elif True:
    scene ep3_mansion66 with dissolve
ty "Jill?"
scene ep3_mansion68 with dissolve
ty "How did this boy get past the gates?"
ty "Rich, call for security!"
scene ep3_mansion69 with dissolve
ji "Tybalt, wait!"
ji "He's my guest and he's free to come here whenever he wants to."
ty "I beg your pardon."
ty "Jill, please! This student has no business in the mansion."
scene ep3_mansion72 with dissolve
ty "Look at his rags."
ty "You call those clothes?"
if ep3_wearHelmet:
    ty "And that absolutely atrocious piece of attire he wears on his head."
scene ep3_mansion69 with dissolve
ji "He's my guest and you will treat him with respect."
mc "I was just leaving."
scene ep3_mansion72 with dissolve
ty "Good. Get security to show this boy out."
ty "We cannot take any risks after the burglary."
scene ep3_mansion76 with dissolve
mc "Thank you for the music..."
mc "It was nice."
scene ep3_mansion77 with dissolve
$ renpy.pause()
scene ep3_mansion78 with dissolve
$ renpy.pause()
if ep3_wearHelmet:
    scene ep3_mansion79 with dissolve
elif True:
    scene ep3_mansion79b with dissolve
mc "(No... Not like this.)"
scene ep3_mansion80 with dissolve
$ renpy.pause()
scene ep3_mansion81 with dissolve
mc "Jill."
mc "Would you like to go out on a date with me?"
mc "I would love to get to know you better."
scene ep3_mansion82 with dissolve
$ renpy.pause()
scene ep3_mansion83 with dissolve
ji "Yes... I'd love that, too."
scene ep3_mansion85 with dissolve
mc "Maybe I could get your number so we can avoid this situation in the future?"
$ number_jill = True
scene ep3_mansion81 with dissolve
mc "Bye..."
$ guideSuggestedPage = 86
scene ep3_mansion86 with dissolve
menu:
    "Be a {size=-1}{font=collegiate.ttf}DIK{/font}{/size}" if True:
        $ RPpreps -= 1
        $ dk(1)
        if ep3_wearHelmet:
            scene ep3_mansion87 with dissolve
        elif True:
            scene ep3_mansion87b with dissolve
        $ renpy.pause()
    "Be a {size=-1}{font=collegiate.ttf}CHICK{/font}{/size}" if True:
        $ dk(-1)
        mc "Tybalt. Always a pleasure."
if ep3_wearHelmet:
    scene ep3_mansion89 with dissolve
elif True:
    scene ep3_mansion89b with dissolve
mc "(Hm...why was it that I asked her out like that?)"
menu:
    "Because of Jill" if True:
        $ ep3_interestedInJill = True
        mc "(I think I'm really interested in Jill...)"
        mc "(It makes it a bit difficult for me...)"
        if not ep3_bella_came_around:
            stop music fadeout 3
        mc "(But I'm going to give Jill an honest chance.)"
        $ bios_history_jill += "I asked Jill out on a date because I'm interested in her.\n\n"
        $ bios_name_jill = True
        $ chat_new_bios = True
    "Because of Tybalt" if True:
        $ ep3_interestedInJill = False
        mc "(I think it was because I wanted to piss Tybalt off...)"
        mc "(I don't know...)"
        mc "(It's probably not the best thing to do, given my situation.)"
        if not ep3_bella_came_around:
            stop music fadeout 3
        mc "(Couldn't hurt giving her a shot, though.)"
        $ bios_history_jill += "I asked Jill out on a date because I wanted to spite Tybalt.\n\n"
        $ bios_name_jill = True
        $ chat_new_bios = True
if ep3_bella_came_around:
    $ bios_history_isabella += "Bella likes me...at least according to Jill.\n\n"
    $ bios_name_isabella = True
    $ chat_new_bios = True
    if ep3_wearHelmet:
        scene ep3_mansion91 with dissolve
    elif True:
        scene ep3_mansion91b with dissolve
    mc "(...)"
    mc "(Bella came around...)"
    stop music fadeout 3
    mc "(...and recommended me to Jill?)"
    menu:
        "Go see Bella" if True:
            $ ep3_BellaLewd = True
        "Ignore Bella" if True:
            $ ep3_BellaLewd = False
            jump ep3_maya_wed_label
elif True:
    jump ep3_maya_wed_label

label ep3_bella_confront_label:
scene ep3_isa_confront with wipeleft
isa "(...)"
scene ep3_isa_confront1
isa "(Huh?)"
isa "(Hm...no...)"
scene ep3_isa_confront2 with dissolve
isa "(Stop thinking about it, already.)"
stu "Excuse me, miss?"
scene ep3_isa_confront3 with dissolve
isa "What!? And it's {b}missus{/b}."
scene ep3_isa_confront4 with dissolve
stu "Ahh...I'm looking for class literature for my analytical chemistry class."
$ bios_eugene   = True
$ bios_name_eugene   = True
$ chat_new_bios = True
scene ep3_isa_confront5 with dissolve
isa "Looking for it, huh?"
isa "Is that why you came up to me immediately upon entry?"
isa "You're a student."
isa "Learn to use the {b}fucking{/b} computer and search for it yourself."
scene ep3_isa_confront6 with dissolve
stu "..."
scene ep3_isa_confront7 with dissolve
$ renpy.pause()
scene ep3_isa_confront2b with dissolve
isa "(I can't lash out at students like that...)"
scene ep3_isa_confront2 with dissolve
isa "(...)"
isa "(I did the right thing.)"
isa "(This was for Jill.)"
isa "(Married women don't fool around with young students.)"
scene ep3_isa_confront2b with dissolve
isa "(...)"
isa "(They aren't intimate with friends either...)"
isa "(But that...that was different!)"
isa "(It doesn't matter... I've stopped it.)"
scene ep3_isa_confront2c with dissolve
isa "(Please, James... Forgive me.)"
isa "(Please, just come home again...)"
isa "(It's been long enough now.)"
scene ep3_isa_confront13 with dissolve
mg "What you just witnessed was the bad temper of the Ice Queen."
stu "*{i}Giggles{/i}*"
stu "Why is she called the Ice Queen?"
scene ep3_isa_confront14 with dissolve
isa "(Hm?)"
scene ep3_isa_confront13 with dissolve
mg "Oh, the new pledge doesn't play Dungeons and Gremlins?"
mg "That's almost grounds for rejection."
stu "*{i}Giggles{/i}*"
scene ep3_isa_confront16 with dissolve
mg "We call her the Ice Queen, because much like in Dungeons and Gremlins..."
mg "...she protects a great treasure, this library."
scene ep3_isa_confront17 with dissolve
mg "But, moreover, she has a heart made of ice, completely devoid of love, and doesn't show any sympathy to intruders."
isa "Is that so?"
scene ep3_isa_confront20 with dissolve
mg "Oh, Isabella. Um-I..."
scene ep3_isa_confront19 with dissolve
isa "Listen here, you nerdy little shit..."
isa "Get the fuck out of my dungeon before I shove one of my treasures up your ass."
isa "All of you! Get out. It's closing time."
scene ep3_isa_confront22 with dissolve
mg "*{i}Whispers{/i}* Sir Magnar fought the beast and lived to tell his tale."
scene ep3_isa_confront23 with dissolve
isa "(...)"
if ep3_wearHelmet:
    scene ep3_isa_confront24 with dissolve
elif True:
    scene ep3_isa_confront24b with dissolve
isa "Leave! You insolent fool!"
mc "Wow...fine."
scene ep3_isa_confront26 with dissolve
isa "[name]!?"
mc "Yeah? Is something wrong, Isabella?"
scene ep3_isa_confront28 with dissolve
isa "No."
isa "I was just closing, that's all."
scene ep3_isa_confront29 with dissolve
mc "Need any help?"
scene ep3_isa_confront28 with dissolve
isa "No."
scene ep3_isa_confront29 with dissolve
mc "Just...let me help."
scene ep3_isa_confront28 with dissolve
isa "Ok... You can help me by putting books back into their shelves."
if ep3_wearHelmet:
    scene ep3_isa_confront33b with dissolve
elif True:
    scene ep3_isa_confront33 with dissolve
mc "Is it ok if I speak up a bit!?"
mc "I know it's a library, but I wanted to have a word with you!"
scene ep3_isa_confront34 with dissolve
$ renpy.pause()
scene ep3_isa_confront35 with dissolve
isa "Go ahead!"
if ep3_wearHelmet:
    scene ep3_isa_confront33b with dissolve
elif True:
    scene ep3_isa_confront33 with dissolve
mc "I just talked to Jill!"
scene ep3_isa_confront35 with dissolve
isa "Ok!?"
if ep3_wearHelmet:
    scene ep3_isa_confront33b with dissolve
elif True:
    scene ep3_isa_confront33 with dissolve
mc "I asked her out on a date!"
scene ep3_isa_confront34b with dissolve
isa "..."
scene ep3_isa_confront35 with dissolve
isa "Good!"
if ep3_wearHelmet:
    scene ep3_isa_confront33b with dissolve
elif True:
    scene ep3_isa_confront33 with dissolve
mc "I don't think I would have done it..."
mc "...if it weren't for you."
scene ep3_isa_confront35 with dissolve
isa "Why not!?"
label ep3_bella_lewd_label:
if _in_replay:
    hide screen phone_screen
    if persistent.name == None:
        $ name = "MC"
    elif True:
        $ name = persistent.name
    if persistent.mc_isabella == None:
        $ mc_isabella = name
    elif True:
        $ mc_isabella = persistent.mc_isabella
    if persistent.isabella == None:
        $ isabella = "Isabella"
    elif True:
        $ isabella = persistent.isabella
    $ ep3_wearHelmet = False
    $ ep2_triedToKissBella = False
if ep3_wearHelmet:
    scene ep3_isa_confront33b with dissolve
elif True:
    scene ep3_isa_confront33 with dissolve
mc "When did you come around about me!?"
scene ep3_isa_confront35 with dissolve
isa "Huh!?"
if ep3_wearHelmet:
    scene ep3_isa_confront33b with dissolve
elif True:
    scene ep3_isa_confront33 with dissolve
mc "Do you...like me now?"
scene ep3_isa_confront35 with dissolve
isa "Don't be-"
scene ep3_isa_confront45
isa "Jesus!"
scene ep3_isa_confront46 with dissolve
mc "Do you?"
scene ep3_isa_confront47 with dissolve
isa "I don't like you..."
isa "I tolerate you."
scene ep3_isa_confront46 with dissolve
mc "That's not what Jill said."
scene ep3_isa_confront47 with dissolve
isa "Jill tends to embellish."
scene ep3_isa_confront46 with dissolve
mc "Even so..."
mc "I...uh..."
mc "I tolerate you, too, Isabella."
scene ep3_isa_confront48 with dissolve
play music "music/ep1/windswept.mp3"
isa "It's...Bella."
scene ep3_isa_confront52 with dissolve
mc "(I...can't help myself.)"
mc "(There's just something about her.)"
scene ep3_isa_confront53 with dissolve
$ renpy.pause()
scene ep3_isa_confront54 with dissolve
$ renpy.pause()
scene ep3_isa_confront55 with dissolve
isa "Stop!"
isa "I've told you that I'm married."
if ep2_triedToKissBella:
    isa "Why are you trying this, again?"
    isa "Why won't you listen?"
elif True:
    isa "Why are you doing this?"
scene ep3_isa_confront57 with dissolve
mc "Look at you, right now."
mc "You're telling me to stop..."
if ep3_wearHelmet:
    scene ep3_isa_confront58b with dissolve
elif True:
    scene ep3_isa_confront58 with dissolve
mc "...but you're the one pulling us closer."
isa "..."
if ep3_wearHelmet:
    scene ep3_isa_confront60 with dissolve
elif True:
    scene ep3_isa_confront60b with dissolve
$ renpy.pause()
scene anim_bella_kiss_ep3 with dissolve
$ renpy.pause()
scene ep3_isa_confront60c with dissolve
$ renpy.pause()
scene anim_bella_kiss2_ep3 with dissolve
$ renpy.pause()
scene anim_bella_kiss3_ep3 with dissolve
isa "No! No... I...can't..."
isa "I can't..."
mc "But...you want to!"
$ renpy.pause()
scene ep3_isa_confront62 with dissolve
isa "But I can't!"
scene ep3_isa_confront63 with dissolve
isa "I can't."
scene ep3_isa_confront64 with dissolve
$ renpy.pause()
$ renpy.end_replay()
$ persistent.ep3_lewd_bella = True
$ calcScenes()
mc "{i}At the time I couldn't understand Bella.{/i}"
mc "{i}The attraction was there, but for her it felt so wrong.{/i}"
scene ep3_isa_confront66 with dissolve
mc "{i}I remember feeling bad about kissing a married woman.{/i}"
mc "{i}I figured she felt the same since she was being unfaithful to her husband...{/i}"
mc "{i}...which, of course, is a very big deal.{/i}"
mc "{i}But if I had known the real reasons to her tears...{/i}"
mc "{i}...and to her persona...{/i}"
stop music fadeout 3
scene black with fade
mc "{i}I wouldn't have kissed her that night.{/i}"
mc "{i}I would have called out for help.{/i}"
$ bios_history_isabella += "I made out with Bella in the library...but she cried and stopped it... What's going on with her?\n\n"
$ bios_name_isabella = True
$ chat_new_bios = True

label ep3_maya_wed_label:
play music "music/ep1/scrapbook.mp3"
scene ep3_maya_wed with wipeleft
mc "(Hm... That's our dorm... Who's that man?)"
scene ep3_maya_wedb with dissolve
if ep2_choseMayaOverParty:
    mc "(I recognize him from somewhere...)"
elif True:
    mc "(Hm...his face doesn't ring a bell.)"
scene ep3_maya_wedc with dissolve
mc "Hey, Maya."
scene ep3_maya_wedd with dissolve
my "[name]! Hi!"
scene ep3_maya_wede with dissolve
mc "Say, who was that man leaving our dorm?"
scene ep3_maya_wedd with dissolve
my "That was my dad, you see?"
scene ep3_maya_wede with dissolve
if ep2_choseMayaOverParty:
    mc "Oh, yeah! I thought I recognized him."
elif True:
    mc "Your dad?"
mc "Why was he here?"
scene ep3_maya_wedg with dissolve
my "You know. Just checking up on me."
scene ep3_maya_wedh with dissolve
my "Hey! Did you drink your beer, yet?"
scene ep3_maya_wedi with dissolve
mc "No, I still have five left, today."
scene ep3_maya_wedh with dissolve
my "Get to it, then!"
scene ep3_maya_wedi with dissolve
mc "Ok! Let's do this! Gooooo [name]!"
play sound "sound_effects/bottle_open.mp3"
scene ep3_maya_wedj with dissolve
my "Haha! It's that exciting, huh?"
scene ep3_maya_wed2 with dissolve
mc "I'm just getting my spirit up to be able to down some spirits."
scene ep3_maya_wedj with dissolve
my "That's clever, but beer's not a spirit...I think."
scene ep3_maya_wed2 with dissolve
mc "That doesn't matter."
scene ep3_maya_wedj with dissolve
my "Oh, wow, you're really going at it."
scene ep3_maya_wed2 with dissolve
mc "I have to..."
scene ep3_maya_wedj2 with dissolve
$ renpy.pause()
scene ep3_maya_wed2 with dissolve
mc "...ten a day..."
scene ep3_maya_wedj2 with dissolve
$ renpy.pause()
scene ep3_maya_wed2 with dissolve
mc "...that's the minimum..."
scene ep3_maya_wedj with dissolve
my "Is it smart doing them all at once, like that?"
scene ep3_maya_wed2 with dissolve
mc "Nothing is smart about me this week, Maya..."
scene ep3_maya_wedj with dissolve
my "Haha, at least you seem to enjoy it. I'm glad."
scene ep3_maya_wedj2 with dissolve
mc "You know what...? I think I am."
if dtype > 0:
    mc "Even the crazy parts are fun!"
elif True:
    mc "Maybe not the crazy parts...but overall it's pretty fun times."
scene ep3_maya_wedj with dissolve
my "Don't overdo it tonight."
jump ep3_freeroam_maya2_label

label ep3_chose_quri_label:
play music "music/ep1/trow.mp3"
scene ep3_ending_0 with dissolve
mc "Hey, I'm going out for a while."
my "Should I be worried, now that you drunk all that beer?"
mc "Nope, I'm just going for a walk..."
if ep3_wearHelmet:
    scene ep3_quri_intro2 with dissolve
    de "Hey, [mc_de_up]... Are you good?"
    mc "Yeah, I'm just going for a walk."
    scene ep3_quri_intro4 with dissolve
    de "Perfect timing, I need to talk to my sis."
    mc "Great, have fun."
    scene ep3_quri_intro6 with dissolve
    de "Pass the helmet, will ya?"
    mc "Oh, I forgot I had it."
    stop music fadeout 3
    scene ep3_quri_intro8 with dissolve
    de "I know! It really becomes a part of you."
elif True:
    scene ep3_quri_intro2b with dissolve
    de "Hey, [mc_de_up]... Are you good?"
    mc "Yeah, I'm just going for a walk."
    scene ep3_quri_intro4b with dissolve
    de "Perfect timing, I need to talk to my sis."
    stop music fadeout 3
    mc "Great, have fun."

label ep3_quri_lewd_label:
hide screen phone_screen
if _in_replay:
    hide screen phone_screen
    if persistent.name == None:
        $ name = "MC"
    elif True:
        $ name = persistent.name
    if persistent.mc_riona == None:
        $ mc_riona = name
    elif True:
        $ mc_riona = persistent.mc_riona
    if persistent.riona == None:
        $ riona = "Riona"
    elif True:
        $ riona = persistent.riona
    if persistent.mc_quinn == None:
        $ mc_quinn = "pervert"
    elif True:
        $ mc_quinn = persistent.mc_riona
    if persistent.quinn == None:
        $ quinn = "Quinn"
    elif True:
        $ quinn = persistent.quinn
    $ ep3_fuckedCamilaAndMona = True
scene ep3_quri_intro9 with wipeleft
mc "(Going to her dorm for this...)"
mc "(I'm betting that this special will be worth the money.)"
mc "(I shouldn't use tuition money for this...)"
mc "(...but pocket money won't cover this and I can always save up the money I borrowed.)"
if not ep3_fuckedCamilaAndMona:
    mc "(And there's no way I wanna miss out on a threesome...)"
    mc "(Who even gets the chance to be in one?)"
elif True:
    mc "(And there's no way I wanna miss out on another threesome...)"
play sound "sound_effects/door_knock.mp3"
scene ep3_quri_intro10 with dissolve
play music "music/ep3/chill.mp3"
mc "Hey."
qu "Hey..."
qu "Come in and lock the door."
play sound "sound_effects/door_lock.mp3"
scene ep3_quri_intro12 with dissolve
ri "Do you have the money?"
scene ep3_quri_intro12b with dissolve
qu "Relax, Riona, there's no need to rush things."
scene ep3_quri_intro12c with dissolve
qu "Can I get you something to drink?"
scene ep3_quri_intro12d with dissolve
mc "No, I'm good. I'm already pretty buzzed from the beer."
scene ep3_quri_intro12c with dissolve
qu "Ah, yes. Hell Week."
qu "Fun times."
scene ep3_quri_intro12d with dissolve
mc "Hm...is something wrong?"
mc "You seem different..."
scene ep3_quri_intro12c with dissolve
qu "What's different?"
scene ep3_quri_intro12d with dissolve
mc "You seem...nice..."
scene ep3_quri_intro12c with dissolve
qu "I am a nice girl."
scene ep3_quri_intro12i with dissolve
qu "Well..."
qu "It depends on the situation."
scene ep3_quri_intro12j with dissolve
qu "Tonight I have a feeling I'll be a bad girl."
qu "So, I figured I'll start off nicely."
scene ep3_quri_intro13 with dissolve
mc "Oh...and yes, I have the money..."
mc "Here."
ri "This is perfect."
scene ep3_quri_intro15 with dissolve
qu "*{i}Whispers{/i}* I told you we could do it."
mc "That's a lot of money, you know... This special better be worth it."
scene ep3_quri_intro17 with dissolve
qu "Of course it is. I wouldn't lie to a customer."
scene ep3_quri_intro20 with dissolve
ri "This special is definitely worth it."
ri "I'm gonna let you do everything you want to me tonight."
scene ep3_quri_intro21 with dissolve
qu "Now that's how you welcome a customer."
if mc_quinn == "pervert":
    scene ep3_quri_intro22 with dissolve
    qu "Would you like that...um...?"
    qu "Man, I've gotten so used to calling you pervert that I can't think of anything else..."
    qu "What do you want me to call you in bed?"
    scene ep3_quri_intro23 with dissolve
    show input_ol_box with dissolve
    label getPlayerLewdNameQuinn:
    $ mc_quinn = renpy.input("What should Quinn call you during lewd scenes?")
    $ mc_quinn = mc_quinn.strip()
    if mc_quinn == "":
        jump getPlayerLewdNameQuinn
    if mc_quinn == "pervert" or mc_quinn == "Pervert":
        scene ep3_quri_intro24 with dissolve
        qu "Really, you still want me to call you that? Haha!"
        qu "You're fun."
    scene ep3_quri_intro25 with dissolve
    qu "As you wish...[mc_quinn]..."
    scene ep3_quri_intro22 with dissolve
    qu "Do you wanna give me a pet name, too?"
    scene ep3_quri_intro23 with dissolve
    menu:
        "Yes" if True:
            show input_ol_box with dissolve
            label getPlayerLewdNameQuinn2:
                $ quinn = renpy.input("What do you want to call Quinn during lewd scenes?")
                $ quinn = quinn.strip()
                if quinn == "":
                    jump getPlayerLewdNameQuinn2
            if quinn != "Quinn" and quinn != "quinn":
                scene ep3_quri_intro22 with dissolve
                qu "[quinn], huh? I like it."
        "No" if True:
            mc "No, it's ok."
    scene ep3_quri_intro27 with dissolve
    ri "What about me?"
    label getPlayerLewdNameRiona:
    scene ep3_quri_intro23 with dissolve
    menu:
        "Give her a pet name" if True:
            show input_ol_box with dissolve
            label getPlayerLewdNameRiona2:
                $ riona = renpy.input("What do you want to call Riona during lewd scenes?")
                $ riona = riona.strip()
                if riona == "":
                    jump getPlayerLewdNameRiona2
                elif True:
                    jump getPlayerLewdNameRiona
        "Have her call you something" if True:
            show input_ol_box with dissolve
            label getPlayerLewdNameRiona3:
                $ mc_riona = renpy.input("What should Riona call you during lewd scenes?")
                $ mc_riona = mc_riona.strip()
                if mc_riona == "":
                    jump getPlayerLewdNameRiona3
                elif True:
                    jump getPlayerLewdNameRiona
        "Done" if True:
            $ renpy.pause(0.5)
    scene ep3_quri_intro22 with dissolve
    qu "Now, as I was saying..."
qu "Would you like to do everything to Riona, [mc_quinn]?"
scene ep3_quri_intro23 with dissolve
mc "Everything? You mean that?"
scene ep3_quri_intro24 with dissolve
qu "Oh my... I'm picking up a kinky vibe from this."
scene ep3_quri_intro27 with dissolve
ri "Try me."
scene ep3_quri_intro23 with dissolve
menu:
    "Vaginal sex?" if True:
        $ ep3_quri_mode = 1
        mc "How about vaginal sex?"
        scene ep3_quri_intro33 with dissolve
        ri "Haha, vaginal sex!? That's it!?"
        ri "You do know that sex kind of implies that?"
        ri "Man, I thought you were gonna ask something hardcore, like fisting."
        scene ep3_quri_intro27 with dissolve
        ri "Yeah, you can fuck me as much as you want in my pussy."
    "Anal sex?" if True:
        $ ep3_quri_mode = 2
        mc "How about anal sex?"
        scene ep3_quri_intro27 with dissolve
        ri "Yeah, I'm definitely up for that."
ri "Lose the clothes and let's go."
scene ep3_quri_intro35 with dissolve
qu "Aw, you two. I'm not running a fast food joint now, am I?"
qu "He's not paying for a run-of-the mill fish burger. He's paying for perfection."
qu "Besides, he can't go in all dry. We need some proper preparations."
if ep3_quri_mode == 1:
    qu "First, you have to make sure his cock is slippery and that your pussy is dripping."
elif ep3_quri_mode == 2:
    qu "First, you have to make sure his cock is slippery and that your ass and pussy are ready for him."
scene ep3_quri_intro36 with dissolve
mc "You'll join too, right?"
scene ep3_quri_intro37 with dissolve
qu "Oh, I'll join. It wouldn't be a threesome if I didn't, right?"
qu "But think of me more like the head chef..."
qu "I'll make sure that you'll cum more than you've done in your entire life, tonight, [mc_quinn]..."
scene ep3_quri_intro38 with dissolve
qu "Now let's see what you're packing, up close..."
scene ep3_quri_intro40 with dissolve
qu "This cock, Riona...it's something else."
ri "Wow..."
scene ep3_quri_intro40b with dissolve
ri "Fuck me!! It's huge!"
scene ep3_quri_intro41 with dissolve
qu "Poor Riona..."
qu "You're gonna destroy her with that thing."
scene ep3_quri_intro42 with dissolve
qu "Look who's already starting..."
qu "She really went all silent and just took it in her mouth..."
scene anim_threesome_bj_ep3 with dissolve
ri "*{i}Schlurp{/i}*"
qu "Hey, [mc_quinn]. Look at her go..."
qu "That's right, you slut...earn his money."
qu "Riona's mouth and throat feel good, right?"
qu "She's a natural born cock sucker..."
qu "That dick does look tasty..."
qu "Wanna share it with me, Riona?"
scene anim_threesome_bj2_ep3 with dissolve
qu "*{i}Lick lick{/i}*"
qu "Stop looking into our eyes, [mc_quinn]..."
qu "That's how you avoid cumming early..."
ri "*{i}Schlurp{/i}*"
ri "He's still doing it..."
mc "I'm just enjoying the view..."
mc "This is the first time I've ever had two hot girls suck my cock..."
ri "Whatever you say, [mc_riona]..."
scene ep3_quri_sex1 with dissolve
qu "Wow, you're way too hard, already."
qu "You could play baseball with that thing."
ri "Yeah, what the fuck...we haven't even stripped, yet."
scene ep3_quri_sex3 with dissolve
qu "Here. You need to drink this..."
qu "Take a moment to cool down...you're gonna need it."
qu "Meanwhile...I'll get Riona ready for you."
scene ep3_quri_sex3a with dissolve
$ renpy.pause()
scene ep3_quri_sex3b with dissolve
qu "Perhaps, you'd like something to smoke?"
mc "I tried smoking when I was younger... I never liked it."
scene ep3_quri_sex3d with dissolve
qu "Aw, cute... I wasn't talking about cigarettes, but fine..."
qu "Maybe next time..."
qu "I don't want you to completely lose your senses...yet."
scene ep3_quri_sex4 with dissolve
qu "You look so hot in those clothes...but I know that you look way hotter without them."
scene ep3_quri_sex5 with dissolve
qu "Do you like Riona's tits, [mc_quinn]?"
menu:
    "Just how I like them" if True:
        mc "Small and perky...just how I like them."
    "Too small" if True:
        $ dk(1)
        mc "They are a bit too small for me. I usually like them bigger."
        scene ep3_quri_sex5b with dissolve
        ri "Rude..."
        qu "Hahaha, he calls it like he sees it. Such a dick."
        qu "That's why I like him."

scene ep3_quri_sex6 with dissolve
qu "*{i}Suck{/i}*"
ri "Mmm..."
scene ep3_quri_sex6b with dissolve
qu "They taste great..."
scene ep3_quri_sex7 with dissolve
$ renpy.pause()
scene ep3_quri_sex7b with dissolve
qu "How about this?"
scene ep3_quri_sex8 with dissolve
if ep3_quri_mode == 1:
    qu "Can you see that pretty pussy from over there?"
elif ep3_quri_mode == 2:
    qu "Can you see her pretty holes from over there?"
qu "Come closer..."
scene ep3_quri_sex9 with dissolve
qu "Should I put it in?"
menu:
    "Put it in her pussy" if True:
        mc "Yeah, put it in her pussy."
        qu "As you wish..."
        scene ep3_quri_sex9b with dissolve
        ri "*{i}Moans{/i}*"
        qu "Haha, if you're moaning from this, I can't imagine what that monster over there will do to you."
    "Put it in her ass" if True:
        mc "Yeah, put it in her ass."
        qu "You're so kinky..."
        scene ep3_quri_sex9c with dissolve
        ri "Hngh..."
        qu "We really need to stretch your ass if you can't handle a candy cane, Riona."
scene ep3_quri_sex10 with dissolve
qu "*{i}Lick lick{/i}*"
scene ep3_quri_sex13 with dissolve
qu "How are you feeling, [mc_quinn]?"
qu "Did you cool down, yet?"
scene ep3_quri_sex13b with dissolve
mc "Yeah, but I'm still rock hard thanks to you two."
scene ep3_quri_sex11 with dissolve
qu "It's time for you to join us. I wanna see Riona get fucked. Hard!"
scene ep3_quri_sex14 with dissolve
mc "Aren't you going to remove those panties?"
scene ep3_quri_sex15 with dissolve
qu "Come and take them from me."
scene ep3_quri_sex16 with vpunch
$ renpy.pause()
scene ep3_quri_sex17 with dissolve
qu "Wow... That sultry look in your eyes."
qu "I fucking love it!"
qu "Come, lay down with us..."
scene ep3_quri_sex18 with dissolve
qu "Get on him, Riona."
qu "Let's show him who the best HOTs are."
jump ep3_quri_loop_cowgirl_label
label ep3_quri_loop_label:

menu:
    "Cowgirl" if True:
        if ep3_quri_mode == 2:
            menu:
                "Vaginal" if True:
                    label ep3_quri_loop_cowgirl_label:
                    scene anim_threesome12_ep3 with dissolve
                    $ renpy.pause()
                    scene anim_threesome12b_ep3 with dissolve
                    $ renpy.pause()
                    scene anim_threesome12c_ep3 with dissolve
                    $ renpy.pause()
                    scene anim_threesome12d_ep3 with dissolve
                    qu "Yes...[mc_quinn]... Eat my pussy, it's all yours..."
                    $ renpy.pause()
                    jump ep3_quri_loop_label
                "Anal" if True:
                    if ep3_firstTimeAnal:
                        $ ep3_firstTimeAnal = False
                        scene ep3_quri_sex20 with dissolve
                        qu "Time to give him what he really wants. Put it in your ass, Riona!"
                        scene ep3_quri_sex20b with dissolve
                        ri "Shit... I would, but it's so thick!"
                        ri "Maybe it doesn't fit?"
                        scene ep3_quri_sex20 with dissolve
                        qu "Quit your bitching! We both know you will do it!"
                        scene ep3_quri_sex19 with dissolve
                        ri "*{i}Moans{/i}* Ahhh! It's too big!"
                        qu "No, it's not... It's a perfect fit!"
                    scene anim_threesome6_ep3 with dissolve
                    ri "Hngn...fuck! You're so big, [mc_riona]!"
                    $ renpy.pause()
                    scene anim_threesome6b_ep3 with dissolve
                    qu "I told you I picked up a kinky vibe from him..."
                    if assman:
                        qu "I heard your nickname was ass man...now I know why."
                    qu "Keep moving that tongue, [mc_quinn]."
                    $ renpy.pause()
                    scene anim_threesome6c_ep3 with dissolve
                    $ renpy.pause()
                    jump ep3_quri_loop_label
        elif True:
            scene anim_threesome12_ep3 with dissolve
            $ renpy.pause()
            scene anim_threesome12b_ep3 with dissolve
            $ renpy.pause()
            scene anim_threesome12c_ep3 with dissolve
            $ renpy.pause()
            scene anim_threesome12d_ep3 with dissolve
            $ renpy.pause()
            jump ep3_quri_loop_label
    "Doggystyle" if True:
        if ep3_firstTimeDoggy:
            $ ep3_firstTimeDoggy = False
            scene ep3_quri_sex21 with dissolve
            qu "How about this...?"
            qu "Oh my...oh my..."
            qu "How will he ever choose where to put his cock?"
        scene ep3_quri_sex22 with dissolve
        label ep3_doggychoice_label:
        menu:
            "Quinn" if True:
                scene anim_threesome16d_ep3 with dissolve
                qu "Oh, [mc_quinn]... Just like that..."
                $ renpy.pause()
                scene anim_threesome16e_ep3 with dissolve
                $ renpy.pause()
                scene anim_threesome16c_ep3 with dissolve
                qu "*{i}Moans{/i}*"
            "Riona" if True:
                scene anim_threesome16_ep3 with dissolve
                ri "Yes! Fuck me, [mc_riona]!"
                $ renpy.pause()
                scene anim_threesome16b_ep3 with dissolve
                $ renpy.pause()
                scene anim_threesome16c_ep3 with dissolve
                ri "*{i}Moans{/i}*"
            "Change position" if True:
                jump ep3_doggychoice_label2
        jump ep3_doggychoice_label
        label ep3_doggychoice_label2:
        jump ep3_quri_loop_label
    "Missionary" if True:
        if ep3_firstTimeMission:
            scene ep3_quri_sex23 with dissolve
            qu "Let's use Riona together..."
            qu "Fuck her hard! I wanna feel her screams of pleasure against my pussy!"
            scene ep3_quri_sex24 with dissolve
            mc "Come here, [quinn]..."
        scene anim_threesome19_ep3 with dissolve
        $ renpy.pause()
        scene anim_threesome19b_ep3 with dissolve
        qu "Mmm..."
        $ renpy.pause()
        scene anim_threesome19c_ep3 with dissolve
        $ renpy.pause()
        if ep3_firstTimeMission:
            $ ep3_firstTimeMission = False
            scene ep3_quri_sex25 with dissolve
            $ renpy.pause()
            scene ep3_quri_sex26 with dissolve
            qu "Dammit, Riona, put some fucking tongue into it!"
        jump ep3_quri_loop_label
    "Missionary + Doggystyle" if True:
        if ep3_firstTimeMission2:
            scene ep3_quri_sex27 with dissolve
            qu "What are you waiting for? Put it in her..."
        scene anim_threesome20_ep3 with dissolve
        mc "Do you like that, [riona]?"
        ri "Fuck yes, [mc_riona]! Go deeper!"
        $ renpy.pause()
        scene anim_threesome20b_ep3 with dissolve
        $ renpy.pause()
        if ep3_firstTimeMission2:
            $ ep3_firstTimeMission2 = False
            scene ep3_quri_sex28 with dissolve
            qu "I can feel your eyes on my ass, [mc_quinn]."
            qu "Are you gonna fuck me?"
            mc "Of course I am, [quinn]..."
        scene anim_threesome20c_ep3 with dissolve
        qu "*{i}Moans{/i}*"
        mc "You feel amazing around my cock..."
        $ renpy.pause()
        scene anim_threesome20d_ep3 with dissolve
        qu "Pound my pussy, [mc_quinn]!!!"
        $ renpy.pause()
        jump ep3_quri_loop_label
    "Cum" if True:
        mc "I'm gonna cum..."

scene anim_threesome_cum_ep3 with dissolve
qu "Do it, [mc_quinn]!"
qu "Spray Riona's face with your cum!"
$ renpy.pause()
scene anim_threesome_cum2_ep3 with dissolve
mc "Oh...shit... Are you ready, [riona]?"
ri "Mhm...[mc_riona]..."
$ renpy.pause()
scene anim_threesome_cum3_ep3 with dissolve
$ renpy.pause()
mc "Ahhh...I'm cumming!!!"

scene ep3_threesome_cum3 with hpunch
$ renpy.pause(0.5)
scene ep3_threesome_cum3 with hpunch
$ renpy.pause(0.5)
scene ep3_threesome_cum3 with hpunch
$ renpy.pause()
scene ep3_threesome_cum4 with dissolve
mc "Wow...that was so intense..."
scene ep3_threesome_cum5 with dissolve
$ renpy.pause()
scene ep3_threesome_cum6 with dissolve
qu "Don't be greedy, Riona... Share it with me."
scene ep3_threesome_cum7 with dissolve
ri "*{i}Smack{/i}*"
scene ep3_threesome_cum8 with dissolve
mc "That's really hot..."
scene ep3_threesome_cum10 with dissolve
qu "Was that your first threesome?"
scene ep3_threesome_cum9 with dissolve
if ep3_fuckedCamilaAndMona:
    mc "No, it was my second...but definitely the best."
elif True:
    mc "Yeah, it was. It was fucking amazing."
scene ep3_threesome_cum10 with dissolve
qu "I'm glad you enjoyed it..."
qu "Say...thanks for buying from my restaurant."
scene ep3_threesome_cum9 with dissolve
mc "Drop that act. Even if I paid for it...I know you enjoyed it, too."
qu "..."
scene ep3_threesome_cum10 with dissolve
qu "Well...until next time...[mc_quinn]..."
stop music fadeout 3
show screen phone_screen
$ renpy.end_replay()
if not persistent.bg_quinn_alt_unlocked:
    $ persistent.bg_quinn_alt_unlocked = True
    $ chat_new_bg = True
    $ calcWallpapers()
$ persistent.ep3_lewd_quri = True
$ calcScenes()
$ bios_history_riona += "I had a threesome with Quinn and Riona!\n\n"
$ bios_name_riona = True
$ bios_history_quinn += "I had a threesome with Quinn and Riona!\n\n"
$ bios_name_quinn = True
$ chat_new_bios = True
jump ep3_not_maya_label

label ep3_chose_maya_label:
play music "music/ep1/trow.mp3"
if ep3_wearHelmet:
    scene ep3_chose_maya with dissolve
elif True:
    scene ep3_chose_mayab with dissolve
de "Maya, you here?"
my "Yeah, I'm here."
if ep3_wearHelmet:
    scene ep3_chose_maya1 with dissolve
elif True:
    scene ep3_chose_maya1b with dissolve
de "[mc_de_up], can I have a word with my sis?"
mc "Sure. You want me to wait outside or...?"
de "Would you?"
mc "Of course."
scene ep3_chose_maya2 with fade
mc "(What's taking them so long?)"
if ep3_wearHelmet:
    scene ep3_chose_maya3 with dissolve
elif True:
    scene ep3_chose_maya3b with dissolve
de "Hey, we're done."
if ep3_wearHelmet:
    scene ep3_chose_maya4 with dissolve
    de "Pass the helmet?"
scene ep3_chose_maya5 with dissolve
mc "What was that about?"
scene ep3_chose_maya5b with dissolve
de "Sorry...family stuff."
de "See you tomorrow, [mc_de]."
if not ep3_mayaOfferedHelp:
    stop music fadeout 3
scene ep3_chose_maya6 with dissolve
mc "A lot of family visits today, heh."
if not ep3_mayaOfferedHelp:
    jump ep3_not_maya_label2
label ep3_maya_lewd_label:
if _in_replay:
    if persistent.name == None:
        $ name = "MC"
    elif True:
        $ name = persistent.name
    if persistent.mc_maya == None:
        $ mc_maya = name
    elif True:
        $ mc_maya = persistent.mc_maya
    if persistent.maya == None:
        $ maya = "Maya"
    elif True:
        $ maya = persistent.maya
    if persistent.ep3_lewd_maya_full:
        $ RPmaya = 15
    elif True:
        $ RPmaya = 0
    $ ep2_fingeredMaya = True
    play music "music/ep1/trow.mp3"
hide screen phone_screen
$ ep3_mayaLewd = True
scene ep3_maya_lewd with dissolve
my "Does your offer still stand? You know...about {i}helping{/i} me?"
scene ep3_maya_lewd1 with dissolve
mc "Oh... Yeah, just like I said. I'll help you."
mc "We can figure this out together."
scene ep3_maya_lewd2 with dissolve
my "Right!?"
my "It's just a couple of weeks of this and it will all be over."
my "After that they can't force me to do things...right?"
scene ep3_maya_lewd1 with dissolve
mc "No one can force you to do anything, but I know what you mean."
mc "Just like DIKs seem to be all friends, at least from the outside..."
mc "I think that's the case for HOTs, too."
scene ep3_maya_lewd with dissolve
my "Yes! So, if I just pass these stupid tests..."
my "...I should be ok after...I hope."
scene ep3_maya_lewd1 with dissolve
mc "You know I'll help you with the tests. I'm very creative!"
mc "If we get Derek's help as well, I think we can make it work."
scene ep3_maya_lewd2 with dissolve
my "That's what I've been thinking about."
my "That I need your help with this..."
my "...and aside from Derek, you're the only one here I can really trust."
my "All of this doesn't have to be this hard...you know?"
scene ep3_maya_lewd with dissolve
my "But please know...this is not just me using you..."
my "I mean, I do need your help, but it's not only because of that."
my "I have decided...that I want it, too."
scene ep3_maya_lewd1 with dissolve
mc "Great! Let's start thinking about this together."
mc "We could use the dildo helmet to fake some of the tasks, maybe?"
scene ep3_maya_lewd with dissolve
my "I don't think you quite understand what I'm getting at."
scene ep3_maya_lewd1 with dissolve
mc "I don't?"
scene ep3_maya_lewd12 with dissolve
mc "Oh..."
my "Yeah..."
scene ep3_maya_lewd13 with dissolve
my "I can't find the right words to ask for something like this."
scene ep3_maya_lewd14 with dissolve
mc "I understand what you're asking, [maya]."
mc "What parts of the list do you want me to help you with?"
scene ep3_maya_lewd15 with dissolve
my "All of them."
my "You and me..."
my "...we take it slow..."
my "...but...we do all of them."

scene anim_maya_kiss_ep3 with dissolve:
    size (config.screen_width, config.screen_height)
mc "Mmm... This was on the list, right?"
my "Yes. It was...but this right now...it's just me."
pause
scene anim_maya_kiss2_ep3 with dissolve:
    size (config.screen_width, config.screen_height)
pause
scene ep3_maya_lewd13 with dissolve
my "How do you feel?"
scene ep3_maya_lewd14 with dissolve
mc "A bit jittery..."
mc "...and horny."
scene ep3_maya_lewd15 with dissolve
my " Me too..."
my "I hate to be pragmatic with this-"
scene ep3_maya_lewd14 with dissolve
mc "What does that mean?"
scene ep3_maya_lewd15 with dissolve
my "You know...practical."
my "But what if we try to do as many things as possible, right now?"
my "Then this will all be over."
scene ep3_maya_lewd14 with dissolve
mc "Are you sure you want to do this?"
mc "It doesn't sound like it right now."
scene ep3_maya_lewd24 with dissolve
my "I just meant that if we do all those things right now, there won't be this whole..."
my "...forced feeling about it."
scene ep3_maya_lewd25 with dissolve
mc "Remind me...what do you want to do?"
scene ep3_maya_lewd24 with dissolve
my "Handjob, blowjob, thighjob, sex, public sex and a threesome."
my "Those latter two..."
scene ep3_maya_lewd25 with dissolve
mc "They will have to wait."
mc "Don't worry. We will figure it out."
scene ep3_maya_lewd28 with dissolve
my "Hey! What about your list?"
my "Anything that works for you?"
scene ep3_maya_lewd29 with dissolve
mc "You're a feminist, so that's one."
mc "And...public sex, I've got that one, too."
mc "You wouldn't happen to be a teacher...would you?"
scene ep3_maya_lewd28 with dissolve
my "Haha, no."
scene ep3_maya_lewd29 with dissolve
mc "And I don't suppose you could slap me in my face during this?"
play sound "sound_effects/slap.mp3"
scene ep3_maya_lewd30 with hpunch
"*{i}Slap{/i}*"
my "Done!"
mc "Ouch!"
scene ep3_maya_lewd31 with dissolve
mc "I should've been clearer...I need photo proof on that one."
my "Oh! I'm so sorry!"
scene ep3_maya_lewd32 with dissolve
my "Hahaha!"
scene ep3_maya_lewd31 with dissolve
my "Wait..."
my "I totally forgot about that, too!"
my "I also need proof."
my "How the hell will this work?"
scene ep3_maya_lewd35 with dissolve
mc "Do you have to show it to everyone?"
scene ep3_maya_lewd36 with dissolve
my "With the other things I've done this far I've just given them or showed a photo of it to Quinn."
scene ep3_maya_lewd35 with dissolve
mc "Oh, no... Not Quinn."
scene ep3_maya_lewd36 with dissolve
my "She's my mother... What can I do?"
scene ep3_maya_lewd35 with dissolve
mc "I don't trust her one bit."
scene ep3_maya_lewd38 with dissolve
my "Ok, I feel we're overthinking this."
my "I'll put my phone to record a video and then I'll edit it."
my "We'll have to think about all this a bit extra afterwards..."
scene ep3_maya_lewd39 with dissolve
my "Trust me, I'm not going to let this video get out in the open."
stop music fadeout 3
scene ep3_maya_lewd40 with dissolve
my "But now that I've gotten the courage to go through with it..."
play sound "sound_effects/clothes.mp3"
scene ep3_maya_lewd41 with dissolve
$ renpy.pause()
play music "music/ep1/windswept.mp3"
scene ep3_maya_lewd42 with dissolve
my "There's no way in hell..."
scene ep3_maya_lewd43 with dissolve
my "...that I'm stopping."
scene ep3_maya_lewd44 with dissolve
mc "I'm with you, [maya]."
scene ep3_maya_lewd45 with dissolve
label ep3_maya_lewd_loop:
menu:
    "Play with her breasts" if True:
        jump ep3_maya_breast_loop
    "Play with her pussy (Maya likes you)" if RPmaya > 14:
        jump ep3_maya_pussy_loop
    "Continue" if True:
        jump ep3_maya_continue_loop

label ep3_maya_breast_loop:
scene anim_maya_breast_ep3 with dissolve:
    size (config.screen_width, config.screen_height)
mc "You have such a perfect body, [maya]."
my "Be gentle, [mc_maya]..."
mc "Does it hurt?"
my "No...it feels good."
pause
scene anim_maya_breast2_ep3 with dissolve:
    size (config.screen_width, config.screen_height)
my "Haha...you really seem to like my breasts."
mc "Do you want me to stop?"
my "No...I like this, too."
my "It turns me on..."
pause
scene anim_maya_breast3_ep3 with dissolve:
    size (config.screen_width, config.screen_height)
mc "They are so soft, yet firm."
pause
menu:
    "Play with her pussy (Maya likes you)" if RPmaya > 14:
        jump ep3_maya_pussy_loop
    "Continue" if True:
        jump ep3_maya_continue_loop

label ep3_maya_pussy_loop:
$ ep3_fingered_maya = True
scene anim_maya_pussy_ep3 with dissolve:
    size (config.screen_width, config.screen_height)
if ep2_fingeredMaya:
    mc "Last time I touched you..."
    mc "I thought to myself that you had the smoothest pussy I've ever felt."
elif True:
    mc "Wow... You have the smoothest pussy I've ever felt."
my "[mc_maya]...my entire body is shaking..."
my "Oh...[mc_maya]."
my "Remember to take it slow with me..."
mc "I remember."
scene ep3_maya_lewd47 with dissolve
my "(Hngh...my body feels so warm...)"
my "(...and my pussy is getting all wet when he gently rubs it like that.)"
scene anim_maya_pussy2_ep3 with dissolve:
    size (config.screen_width, config.screen_height)
my "(Oh, fuck! He's doing this just right...)"
my "(If he continues like that, this will get too intense.)"
pause
my "Um...[mc_maya]?"
my "How about if you try to insert one finger in me, instead?"
my "It feels great, but it's getting to a point where I'm about to scream..."
mc "Ok, I'll slow it down for you."
scene anim_maya_pussy3_ep3 with dissolve:
    size (config.screen_width, config.screen_height)
pause
my "Hngn...yes...oh...fuck!"
mc "You're so tight, [maya]."
my "Yes...I usually play with small dildos."
mc "Tell me if it hurts."
my "No, it doesn't hurt...but I don't think I'm quite there yet."
menu:
    "Play with her breasts" if True:
        jump ep3_maya_breast_loop
    "Continue" if True:
        jump ep3_maya_continue_loop

label ep3_maya_continue_loop:
scene ep3_maya_lewd49 with dissolve
my "Ok... Do it."
mc "Do what?"
my "You know what I mean."
my "Stop smiling and drop your shorts."
scene ep3_maya_lewd50 with dissolve
my "Don't look."
scene ep3_maya_lewd50b with dissolve
mc "Haha, why?"
scene ep3_maya_lewd50 with dissolve
my "It's embarrassing..."
my "I haven't done this before."
scene ep3_maya_lewd50b with dissolve
mc "Ok. I'll close my eyes."
mc "Go ahead and do what you want."
scene ep3_maya_lewd53 with dissolve
my "(Are cocks meant to be this big?)"
my "(Like...damn...)"
my "(I have no clue if I'm doing this the right way...)"
scene anim_maya_hj0_ep3 with dissolve:
    size (config.screen_width, config.screen_height)
pause
my "(I hope he tells me if it hurts...)"
my "(Am I supposed to go this slow?)"
scene anim_maya_hj0b_ep3 with dissolve:
    size (config.screen_width, config.screen_height)
pause
my "(He seems to like it when I'm at the top of the head...)"
my "(That's like the male clitoris if I recall correctly from sexual education.)"
my "(This thing is so big I could easily fit two hands on it...)"
my "[mc_maya], does it feel good? I'm not doing it too hard, right?"
mc "Actually, you can grip it even tighter. It's not as sensitive as you may think."
my "Oh! Can I use two hands?"
mc "Yeah, but I have to watch it, I can't take this anymore."
mc "It's killing me."
scene anim_maya_hj_ep3 with dissolve:
    size (config.screen_width, config.screen_height)
my "Ok, you can look."
mc "Wow..."
mc "This feels so much better already."
my "It's kind of like a massage, right?"
mc "Yeah...mmm...you have a perfect grip now."
mc "Don't stop it."
pause
scene anim_maya_hj2_ep3 with dissolve:
    size (config.screen_width, config.screen_height)
my "(Wow, his cock is pulsating in my hands.)"
my "(And it's so fucking hard! Way harder than it was before.)"
my "(It's quite beautiful...)"
my "(Haha! It's so weird to think that I'd like this...)"
my "(Pussies are better, though...)"
my "(...I think.)"
pause
scene ep3_maya_lewd54b with dissolve
my "Do you think that counts as a handjob?"
mc "It definitely does."
my "It's funny..."
my "We're already naked doing this..."
scene ep3_maya_lewd54 with dissolve
my "...but I'm embarrassed to ask for more."
scene ep3_maya_lewd55 with dissolve
mc "Then let me handle it."
my "Whoa!"
my "Hahaha!"
scene ep3_maya_lewd56 with dissolve
my "Oh!!! Yes! [mc_maya]..."
scene anim_maya_cunn_ep3 with dissolve:
    size (config.screen_width, config.screen_height)
pause
scene anim_maya_cunn2_ep3 with dissolve:
    size (config.screen_width, config.screen_height)
pause
scene ep3_maya_lewd57 with dissolve
my "You're so good at that..."
my "I would never have thought a guy could be this good."
scene anim_maya_cunn3_ep3 with dissolve:
    size (config.screen_width, config.screen_height)
pause
mc "(She tastes so good!)"
mc "(Her pussy is so warm in my mouth...)"
mc "(...and it has opened up more than before.)"
mc "(I can stick my tongue so far into her.)"
mc "(And looking into those beautiful eyes at the same time...)"
mc "(...it makes me so horny.)"
mc "(I wanna be inside her...so badly.)"
scene ep3_maya_lewd58 with dissolve
my "Um...[mc_maya]..."
scene ep3_maya_lewd59 with dissolve
mc "Are you having second thoughts?"
scene ep3_maya_lewd58 with dissolve
my "It's just that..."
my "I'm not so sure it will fit..."
scene ep3_maya_lewd59 with dissolve
mc "Trust me, it will fit."
scene ep3_maya_lewd58 with dissolve
my "Can you do it really slow?"
my "And I mean REALLY slow!"
scene ep3_maya_lewd59 with dissolve
mc "I'll start on the outside, [maya]."
mc "That won't hurt you."
scene anim_maya_rub_ep3 with dissolve:
    size (config.screen_width, config.screen_height)
mc "See?"
my "Yeah..."
my "You're right, this feels good."
if ep3_fingered_maya:
    my "Just like how it felt when you did it with your finger."
pause
scene anim_maya_rub2_ep3 with dissolve:
    size (config.screen_width, config.screen_height)
mc "Yeah and it feels so good for me, too."
my "*{i}Gently moans{/i}*"
pause
scene anim_maya_rub3_ep3 with dissolve:
    size (config.screen_width, config.screen_height)
mc "(She's wet...but not as wet as she was when I licked her pussy.)"
mc "(As long as I listen to what she says, I can try to slowly put it in...)"
pause

scene ep3_maya_lewd59 with dissolve
mc "[maya], if it hurts, just let me know and I will stop."
scene ep3_maya_lewd58 with dissolve
my "Ok..."
scene ep3_maya_lewd60 with dissolve
my "Ahhh!"
mc "It's ok, I'm stopping right there. Just relax."
my "I can't! [mc_maya], it's too big for me!"
scene ep3_maya_lewd61 with dissolve
mc "(She's not lying...I can barely fit the tip...)"
mc "(It feels like she's tightened up since I was licking her pussy, too.)"
scene ep3_maya_lewd62 with dissolve
mc "(But God! I want her so fucking bad!)"
mc "(I just want to push it as deep I can inside her and fuck her.)"
scene ep3_maya_lewd63 with dissolve
my "[mc_maya]... I'm sorry, I don't think I can."
scene ep3_maya_lewd59 with dissolve
mc "Don't worry. We'll cross that off the list another time."
scene ep3_maya_lewd58 with dissolve
my "Can you lie down?"
scene anim_maya_grind_ep3 with dissolve:
    size (config.screen_width, config.screen_height)
my "I know it's not what you may have wanted..."
my "...but thighjob was on the list, too."
my "That's when you go like this, right?"
mc "Mmm...yes, I think that's it."
pause
scene anim_maya_grind2_ep3 with dissolve:
    size (config.screen_width, config.screen_height)
my "Does it feel better than rubbing my pussy?"
mc "Yeah, it feels like a handjob and pussy rubbing all at once."
pause
scene anim_maya_grind3_ep3 with dissolve:
    size (config.screen_width, config.screen_height)
my "*{i}Moans{/i}* I like...it...too."
my "(When I angle it right, he rubs my clit so good!)"
pause
scene anim_maya_grind_long_ep3 with dissolve:
    size (config.screen_width, config.screen_height)
my "I could mix it up like this?"
mc "Yes! That's so sexy, [maya]."
pause
scene ep3_maya_lewd65 with dissolve
my "Hi..."
mc "Hey..."
my "How about this?"
scene anim_maya_grind_special_ep3 with dissolve:
    size (config.screen_width, config.screen_height)
mc "Oh, yes! Wow...you're really creative."
my "Haha, I guess I'm gifted."
pause
scene anim_maya_grind_special3_ep3 with dissolve:
    size (config.screen_width, config.screen_height)
my "This feels really good, [mc_maya]."
mc "Yeah... I'm getting pretty close."
my "Close to cumming?"
mc "Yeah, how about you?"
my "No, I don't think I can cum anytime soon..."
pause
scene anim_maya_grind_special2_ep3 with dissolve:
    size (config.screen_width, config.screen_height)
my "But if you're close...just go for it!"
mc "Yeah... I'm so close."
pause
scene anim_maya_grind_special4_ep3 with dissolve:
    size (config.screen_width, config.screen_height)
my "Look into my eyes when you do it..."
pause
my "Can you cum?"
mc "Yeah... I'm cumming!!!"
scene bg anim_maya_grind_cum_ep3 movie with dissolve:
    size (config.screen_width, config.screen_height)
mc "Ah!!"
scene ep3_maya_cum1 with dissolve
my "Oh, wow! This is...!"
scene ep3_maya_lewd65 with dissolve
my "[mc_maya]... I..."
my "That was my first time with a boy!"
scene ep3_maya_lewd67 with dissolve
$ renpy.pause()
scene ep3_maya_lewd65 with dissolve
my "Thank you..."
my "Haha... I'm a bit unsure..."
scene ep3_maya_lewd66 with dissolve
mc "About what?"
scene ep3_maya_lewd65 with dissolve
my "Like, what am I supposed to do with all that cum on my back?"
scene ep3_maya_lewd66 with dissolve
mc "Don't worry, I'll help you."
mc "You don't get to be a guy without becoming an expert at this."
scene ep3_maya_lewd69 with dissolve
my "Hahaha!"
stop music fadeout 3
scene ep3_maya_lewd67 with dissolve
$ renpy.pause()
$ renpy.end_replay()
$ persistent.ep3_lewd_maya = True
$ calcScenes()
if RPmaya > 14:
    $ persistent.ep3_lewd_maya_full = True
if not persistent.bg_maya_alt_unlocked:
    $ persistent.bg_maya_alt_unlocked = True
    $ chat_new_bg = True
    $ calcWallpapers()
$ bios_history_maya += "I helped Maya with her HOT scavenger hunt list...it was amazing.\n\n"
$ bios_name_maya = True
$ chat_new_bios = True
scene ep3_chose_maya6b with fade
mc "Maya... I'm curious... What really made you change your mind about all this?"
mc "Yesterday it seemed like you were gonna survive college without the help from the HOTs."
scene ep3_chose_maya7 with dissolve
my "After today..."
my "...I just know what I have to do."
jump ep3_not_maya_label3

label ep3_not_maya_label:
scene ep3_chose_maya6 with Fade(1,1,1)
mc "I'm back."
mc "Did you have a good talk with Derek?"
label ep3_not_maya_label2:
scene ep3_chose_maya7 with dissolve
my "Yeah."
my "And now I know what I have to do."
label ep3_not_maya_label3:
hide screen phone_screen
play music "music/ep3/spring_in_russia.mp3"
if ep3_mayaLewd:
    scene ep3_chose_maya8b with dissolve
elif True:
    scene ep3_chose_maya8 with dissolve
mc "What?"
my "No matter the tasks on that list..."
my "I'm doing them."
mc "Did Derek tell you that?"
my "No, but he confirmed something I've been thinking for a while now."
mc "Which is?"
my "That I can't trust my dad's lies."
scene ep3_chose_maya11 with dissolve
mc "So...that wasn't a happy visit from your dad, before?"
mc "I'm...lost. You'll have to tell me everything."
mc "100%%, remember?"
my "..."
scene ep3_chose_maya9 with dissolve
my "All right..."
my "There's something I haven't told you..."
my "Because I wasn't sure of how you'd react...or how to approach the subject."
my "I kind of tried telling you this before...even though I wasn't ever going to tell this to anyone here..."
my "But it's better if you know this...for both of us."
scene ep3_chose_maya12 with dissolve
my "It started as the reason why I needed that money..."
my "...but thanks to Derek, and now even you, I've realized that I need it for an even bigger reason."
scene ep3_chose_maya11 with dissolve
mc "Just tell me! What are the reasons?"
$ bios_history_maya += "Maya is more determined than ever to get that free tuition.\n\n"
$ bios_name_maya = True
$ chat_new_bios = True
jump ep3_ending_label

label ep3_ending_label:
scene ep3_ending_0
play sound "sound_effects/door_knock.mp3"
"*{i}Door knocking{/i}*"
scene black
mc "{i}Doors are funny.{/i}"
mc "{i}Be it metal or be it wood, they're made to do the same things.{/i}"
mc "{i}To keep you safe or secluded...{/i}"
mc "{i}...and to protect the things you value.{/i}"
mc "{i}Protect you from whatever is on the other side.{/i}"
mc "{i}Or worse...{/i}"
mc "{i}They are made to keep things on the inside.{/i}"
mc "{i}Things you don't want anyone else to see.{/i}"
mc "{i}Locked away.{/i}"
mc "{i}It's weird to think that something so simple as a knock, often repeated three times, is all it takes to get someone to open that door.{/i}"
mc "{i}Curiosity takes over and it exposes you.{/i}"
mc "{i}Some doors are meant to stay closed.{/i}"
mc "{i}Because opening them...{/i}"
scene ep3_ending_1
qu "Yeah?"
dw "We need to talk."
scene ep3_ending_2
isa "..."
scene ep3_ending_3
my "(NO! NO! NO! NO! NOT LIKE THIS!)"
my "What are you doing here?"
scene black
mc "{i}...may change everything{/i}."
scene ep3_ending_4
stop music fadeout 3
my "Come in! Um..."
scene ep3_ending_5
my "[name]..."
my "This is my..."
my "...girlfriend..."
scene ep3_ending_6
my "Josy."
scene ep3_ending_7
$ renpy.pause()
$ renpy.music.stop(channel="sfx1", fadeout=0)
play sound "sound_effects/whoosh_2.mp3"
scene black
$ renpy.pause(2)
$ bios_history_maya += "Josy and Maya...are a couple...\n\n"
$ bios_name_maya = True
$ bios_history_josy += "Josy and Maya...are a couple...\n\n"
$ bios_name_josy = True
$ chat_new_bios = True

scene black with dissolve
label ep3_choosePathLoop:
$ ui.imagebutton("ep3_choose_derek_disabled", "ep3_choose_derek_scr", clicked=ui.returns("DEREK"), xpos=2, ypos=0)
if not rejectedSage and ep2SageGuitarTeacher:
    $ ui.imagebutton("ep3_choose_sage_disabled", "ep3_choose_sage_scr", clicked=ui.returns("SAGE"), xpos=676, ypos=0)
elif True:
    $ ui.imagebutton("ep3_choose_sage_locked", "ep3_choose_sage_locked", clicked=ui.returns("NULL"), xpos=676, ypos=0)
if ep3_bella_came_around and ep3_BellaLewd:
    $ ui.imagebutton("ep3_choose_bella_disabled", "ep3_choose_bella_scr", clicked=ui.returns("BELLA"), xpos=1352, ypos=0)
elif True:
    $ ui.imagebutton("ep3_choose_bella_locked", "ep3_choose_bella_locked", clicked=ui.returns("NULL"), xpos=1352, ypos=0)
$ result = ui.interact()
if result == "SAGE":
    $ ep3_choseSage = True
    scene black
    play sound "sound_effects/door_knock.mp3"
    $ renpy.pause(1)
    scene ep3_endsage with fade
    mc "Hi... Can I stay with you?"
elif result == "BELLA":
    $ ep3_choseBella = True
    scene black
    play sound "sound_effects/door_knock.mp3"
    $ renpy.pause(1)
    scene ep3_endbella with fade
    mc "Hi... Can I stay with you?"
elif result == "DEREK":
    $ ep3_choseDerek = True
    scene black
    play sound "sound_effects/door_knock.mp3"
    $ renpy.pause(1)
    scene ep3_endderek with fade
    mc "Hi... Can I stay with you?"
elif True:
    jump ep3_choosePathLoop

label ep3_save_here_label:
$ renpy.pause(1)
$ updateDikScore()
if steamAchievements and persistent.vault3 and not config.console and not config.developer:
    $ achievement.grant("VAULTLOOTER3")
    init:
        $ achievement.register("VAULTLOOTER3")
    $ achievement.Sync()
if steamAchievements and persistent.vault1 and persistent.vault2 and persistent.vault3 and persistent.vault4 and not config.console and not config.developer:
    $ achievement.grant("VAULTLOOTER")
    init:
        $ achievement.register("VAULTLOOTER")
    $ achievement.Sync()
if steamAchievements and not config.console and not config.developer:
    $ achievement.grant("EPISODE3")
    init:
        $ achievement.register("EPISODE3")
    $ achievement.Sync()
if persistent.current_episode == 3:
    scene ep3_episode_end
elif True:
    scene ep3_episode_endb
$ calcRenders()
$ renpy.pause()
scene black with fade
stop music fadeout 10
show screen scoremsg
$ renpy.pause(2)
hide screen scoremsg

play music "music/ep3/spring_in_russia.mp3"
$ episodeIsEnding = True
show screen endingScreen
show screen majorChoiceScale
$ renpy.pause()
$ episodeIsEnding = False
hide screen endingScreen
hide screen majorChoiceScale

if not renpy.variant("pc"):
    $ RPjosy = 0
    $ RPmaya = 0
    $ RPisabella = 0
    $ RPsage = 0
    $ RPjill = 0
if RPjosy >= 0:
    $ josyScore = RPjosy / 15.0
elif True:
    $ josyScore = RPjosy / -2.0
if RPmaya >= 0:
    $ mayaScore = RPmaya / 24.0
elif True:
    $ mayaScore = RPmaya / -5.0
if RPsage >=0:
    $ sageScore = RPsage / 13.0
elif True:
    $ sageScore = RPsage / -3.0
if RPisabella >= 0:
    $ isabellaScore = RPisabella / 6.0
elif True:
    $ isabellaScore = RPisabella / -6.0
if RPjill >= 0:
    $ jillScore = RPjill / 5.0
elif True:
    $ jillScore = RPjill / -4.0
$ episodeContLabel = "ep3_ending_label2"
jump ep3_report_jill_label
$ renpy.pause()
label ep3EndLabel:
stop music fadeout 2
$ renpy.pause(2)

if renpy.loadable("update4.rpyc"):
    jump startUpdate4
elif True:
    play music "music/patched/track_previous.mp3"
    jump endOfVersion3

label endOfVersion3:
scene black
show spr_bg_ep3
show spr_mid_ep3
show spr_top_ep3
show massive_diks
$ renpy.pause()
hide massive_diks
show massive_diks2
$ renpy.pause()
hide massive_diks2
show acknowledgements
$ renpy.pause()
hide acknowledgements
show music_credits
$ renpy.pause()
hide music_credits
show version_end
$ renpy.pause()
hide version_end
scene twitter_promo
$ renpy.pause()
scene episode4_polls
$ renpy.pause()
scene patreon_promo
$ renpy.pause()
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
