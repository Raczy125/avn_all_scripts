label ep4_night_talk_derek_label:
$ guideSuggestedPage = 88
scene ep4_night_talk_derek with Fade(1.5,1.5,1.5)
$ renpy.pause()
scene ep4_night_talk_derek1 with dissolve
de "Here you go, [mc_de]."
scene ep4_night_talk_derek2 with dissolve
mc "What the hell is this?"
scene ep4_night_talk_derek3 with dissolve
de "When you're feeling upset, you should drink something warm."
scene ep4_night_talk_derek2 with dissolve
mc "But...why are there lumps in it?"
scene ep4_night_talk_derek3 with dissolve
de "It's ramen noodle water..."
de "Sorry, I don't have any tea."
de "I can warm you a beer if you want that instead?"
scene ep4_night_talk_derek2 with dissolve
mc "I'd rather have a cold one."
scene ep4_night_talk_derek6 with dissolve
be "Hey, keep it down! I'm trying to sleep over here."
scene ep4_night_talk_derek7 with dissolve
de "Shut up, Bert! My brother needs me!"
de "Go find some earplugs or sleep in the corridor!"
scene ep4_night_talk_derek6 with dissolve
be "It's always something with you, isn't it!?"
scene ep4_night_talk_derek7 with dissolve
de "Excuse me for having a life, Bert!"
de "Not everyone goes to college to study!"
scene ep4_night_talk_derek10 with dissolve
de "So...what's up with you?"
mc "..."
scene ep4_night_talk_derek11 with dissolve
mc "It's Josy."
scene ep4_night_talk_derek10 with dissolve
de "Josy?"
scene ep4_night_talk_derek11 with dissolve
mc "Your sister...her girlfriend is Josy."
scene ep4_night_talk_derek10 with dissolve
de "She...told you that? Wow..."
de "Yeah...that's what I've been bugged about..."
de "I couldn't tell you... I mean, you're my maggot brother and all, but we just kinda met."
de "She's in a..."
scene ep4_night_talk_derek15 with dissolve
de "...this kind of a relationship."
scene ep4_night_talk_derek10 with dissolve
de "How did you find out?"
scene ep4_night_talk_derek11 with dissolve
mc "Josy showed up...she's the girl I've been dating."
scene ep4_night_talk_derek18 with dissolve
de "Wait wait wait wait! Hold the FUCK up!"
de "What!?"
de "You need to tell me everything because this sounds fucking nuts!"
stop music fadeout 3
de "What exactly happened last night?"
jump ep4_flashback_label

label ep4_night_talk2_derek_label:
play music "music/ep2/by_your_side.mp3"
scene ep4_night_talk2_derek with fade
de "I can't believe this..."
scene ep4_night_talk2_derek1 with dissolve
mc "It's the truth."
scene ep4_night_talk2_derek with dissolve
de "How do you feel?"
scene ep4_night_talk2_derek1 with dissolve
mc "Hurt...betrayed...kind of..."
mc "I don't know... Do you think I overreacted by storming out like that?"
scene ep4_night_talk2_derek with dissolve
de "You are a bit of a drama queen; I'll give you that."
scene ep4_night_talk2_derek4 with dissolve
mc "What!?"
scene ep4_night_talk2_derek3 with dissolve
de "Come on! You know you are!"
de "You cry when you get locked out of your dorm by Troy..."
de "You cry when the DIKs let you roam naked on campus..."
de "You wanted to leave and go back home when you just got here..."
de "You cry when Stanley threw you out..."
scene ep4_night_talk2_derek4 with dissolve
mc "Wait...what? Stanley threw me out?"
scene ep4_night_talk2_derek6 with dissolve
de "Ahhh...I'm just saying that you're over-dramatic."
de "But it's fine!"
scene ep4_night_talk2_derek7 with dissolve
de "You're a snowflake."
de "A precious little snowflake."
de "And that's ok."
menu:
    "Agree" if True:
        scene ep4_night_talk2_derek11 with dissolve
        mc "Ok... I'm a snowflake."
        de "And I love you for it."
    "Fuck you" if True:
        scene ep4_night_talk2_derek18 with dissolve
        mc "Fuck you."
        de "A snowflake with a potty mouth."
    "Punch him" if True:
        $ dk(1)
        play sound "sound_effects/hit.mp3"
        scene ep4_night_talk2_derek12 with hpunch
        de "Ouch!"
        de "That's a bad snowflake!"
        mc "Stop calling me that!"
scene ep4_night_talk2_derek3 with dissolve
de "All I'm saying is that you need to toughen up!"
scene ep4_night_talk2_derek14 with dissolve
mc "I'm tough! I know how to fight."
scene ep4_night_talk2_derek3 with dissolve
de "I didn't mean in a physical way."
scene ep4_night_talk2_derek13b with dissolve
de "I was talking about the insides of the coconut that rests on your meaty neck."
scene ep4_night_talk2_derek3 with dissolve
de "Look at me! I'm tough as fuck."
de "Go ahead! Try to insult me."
menu:
    "Mean insult" if True:
        scene ep4_night_talk2_derek14 with dissolve
        mc "You look really stupid without a shirt."
        scene ep4_night_talk2_derek16 with dissolve
        de "*{i}Gasps{/i}* My emotions!"
        scene ep4_night_talk2_derek3 with dissolve
        de "Come on. That was stupid."
    "Really mean insult" if True:
        scene ep4_night_talk2_derek14 with dissolve
        mc "You think you're good with women, but I see the way they look at you..."
        mc "They are really not interested in you and you look like a moron when you're trying."
        scene ep4_night_talk2_derek18 with dissolve
        de "You...bitch."
        play sound "sound_effects/slap.mp3"
        scene ep4_night_talk2_derek19 with hpunch
        mc "Hey!"
        play sound "sound_effects/slap.mp3"
        scene ep4_night_talk2_derek20 with hpunch
        $ renpy.pause(0.5)
        play sound "sound_effects/slap.mp3"
        scene ep4_night_talk2_derek19 with hpunch
        $ renpy.pause(0.5)
        play sound "sound_effects/slap.mp3"
        scene ep4_night_talk2_derek20 with hpunch
        $ renpy.pause(0.5)
        scene ep4_night_talk2_derek21
        de "Aargh!!!"
        mc "Fuck you!!!"
        de "Take it back!"
        mc "NEVER!"
        de "Ok! Stop!"
        scene ep4_night_talk2_derek22 with dissolve
        mc "Who's the snowflake now?"
        de "Sorry, I lost my cool."
    "Don't insult him" if True:
        $ dk(-1)
        scene ep4_night_talk2_derek14 with dissolve
        mc "I don't want to insult you."
        scene ep4_night_talk2_derek7 with dissolve
        de "And that's why you're a snowflake."
scene ep4_night_talk2_derek3 with dissolve
de "But yeah... I think you overreacted."
de "If it was me, in a similar situation and definitely not with my sister...hello!"
de "...I would try to turn it into a threesome."
de "But your strategy of storming out...nah. Not for me."
menu:
    "I overreacted" if True:
        $ ep4_overreacted = True
        scene ep4_night_talk2_derek14 with dissolve
        mc "You're right... Maybe I overreacted..."
        mc "...but they hurt me."
        mc "They lied and they kept things from me..."
    "I didn't overreact" if True:
        $ ep4_overreacted = False
        scene ep4_night_talk2_derek14 with dissolve
        mc "I didn't overreact! I gave Maya several chances, but she didn't tell me the truth until she was forced to."
        mc "And Josy's not much better..."
        mc "She was more honest with me but still kept things from me."
scene ep4_night_talk2_derek3 with dissolve
de "I know why that is..."
de "...but it's not my story to tell."
scene ep4_night_talk2_derek14 with dissolve
mc "Why? I know their secret now."
scene ep4_night_talk2_derek3 with dissolve
de "Yeah, and it was a secret for a reason, dude."
de "Not everyone is cool with gay relationships."
scene ep4_night_talk2_derek1 with dissolve
mc "*{i}Sigh{/i}*"
mc "What should I do?"
scene ep4_night_talk2_derek with dissolve
de "You're not gonna like it."
scene ep4_night_talk2_derek1 with dissolve
mc "Tell me."
scene ep4_night_talk2_derek with dissolve
de "You will just call it a stupid idea."
scene ep4_night_talk2_derek1 with dissolve
mc "Probably...but tell me."
scene ep4_night_talk2_derek32 with dissolve
de "Don't get attached to women this easily."

de "You're young, [mc_de]."
de "Do you see yourself as the relationship type of guy?"
menu:
    "Yeah" if True:
        scene ep4_night_talk2_derek33 with dissolve
        $ ep4_derek_relationship = True
        mc "Yeah. I want a relationship."
        scene ep4_night_talk2_derek32 with dissolve
        de "Ok, but why do you want it right now?"
        de "You just started college!"
        de "It would be like walking into a restaurant when you're already full."
        scene ep4_night_talk2_derek33 with dissolve
        if ep1_accepted_quinn_offer:
            mc "Don't talk about restaurants..."
        mc "I see your point, but I still want a relationship."
    "Not really" if True:
        scene ep4_night_talk2_derek33 with dissolve
        $ ep4_derek_relationship = False
        mc "No, not really."
        scene ep4_night_talk2_derek32 with dissolve
        de "Then sleep around, dude!"
        de "You might wake up one day next to someone who will change your mind..."
        de "...but getting locked up this early in life?"
        de "What for?"
        scene ep4_night_talk2_derek with dissolve
        de "As you told me the other day... You're single."
        de "Embrace that."
scene ep4_night_talk2_derek32 with dissolve
de "Why don't you try to date more?"
de "Figure out what you want instead of rushing into things."
scene ep4_night_talk2_derek33 with dissolve
mc "What do {b}you{/b} want?"
scene ep4_night_talk2_derek38 with dissolve
de "I want to bang Ashley."
if not ep4_derekFuckedArieth:
    de "I want to bang Arieth."
de "I want to bang Camila."
de "I want to bang Cathy."
de "I want to bang Jade."
de "I want to-"
scene ep4_night_talk2_derek33 with dissolve
mc "You want to bang a lot of chicks. I get it."
scene ep4_night_talk2_derek32 with dissolve
de "That's what I'm saying! If you have many goals in life, you're bound to fulfill some of them!"
de "Don't pout. I'll find a way to cheer you up."
de "Wanna get some shuteye?"
scene ep4_night_talk2_derek33 with dissolve
mc "Sure..."
scene ep4_night_talk2_derek32 with dissolve
de "Big spoon or little spoon?"
scene ep4_night_talk2_derek33 with dissolve
mc "No spoon."
scene ep4_night_talk2_derek32 with dissolve
de "It's only gay if you get a boner."
scene ep4_night_talk2_derek33 with dissolve
mc "I don't want to find out if you get one."
scene ep4_night_talk2_derek45 with dissolve
de "Sleep tight, bud."
stop music fadeout 3
scene black with Fade(2,2,2)
$ renpy.pause(0.5)

$ bios_history_derek += "After fighting with Josy and Maya, I went to stay with Derek.\n\n"
$ bios_history_mc += "After fighting with Josy and Maya, I went to stay with Derek.\n\n"
if ep4_derek_relationship:
    $ bios_history_derek += "I told Derek that I see myself as a relationship kind of guy.\n\n"
elif True:
    $ bios_history_derek += "I told Derek that I don't see myself as a relationship kind of guy.\n\n"
$ bios_name_derek = True
$ bios_name_mc = True
$ chat_new_bios = True

label ep4_morning_talk_derek_label:
scene ep4_morning_talk_derek with fade
$ renpy.pause()
play sound "sound_effects/slap.mp3"
scene ep4_morning_talk_derek1 with hpunch
mc "Euw!!!"
play music "music/ep1/never_give_up.mp3"
scene ep4_morning_talk_derek2 with dissolve
de "What!?"
scene ep4_morning_talk_derek3 with dissolve
mc "I had your fucking toes in my mouth!"
mc "When was the last time you showered!?"
scene ep4_morning_talk_derek4 with dissolve
de "Stop sucking on my toe like it's a pacifier! That's on you, [mc_de]!"
be "Shut up!!!"
scene ep4_morning_talk_derek6 with dissolve
de "EARPLUGS BERT! FOR FUCK'S SAKE!"
scene ep4_morning_talk_derek7 with wipeleft
de "Here! Breakfast."
play sound "sound_effects/bottle_open.mp3"
scene ep4_morning_talk_derek10 with dissolve
mc "You really don't get along with your roommate."
scene ep4_morning_talk_derek11 with dissolve
de "Pot, kettle, black cock."
de "Bert is a nerdy dick! But you don't see me crying about it."
scene ep4_morning_talk_derek12 with dissolve
mc "Yeah, screaming at him is much healthier."
$ renpy.sound.play("sound_effects/shower.mp3", channel="sfx1", loop=True)
scene ep4_morning_talk_derek13 with dissolve
de "When we become DIKs, man, I tell you...I'm out of that place."
de "I can't wait to come home to that sweet old janitor's closet."
if ep2_fuckHOT:
    mc "I banged a girl in that closet."
    de "Really? Who!?"
    mc "You know Sarah?"
    de "The HOT?"
    mc "Yeah."
    scene ep4_morning_talk_derek14 with dissolve
    de "Nice! Cheers!"
    play sound "sound_effects/bottle_clink.mp3"
    scene ep4_morning_talk_derek15 with hpunch
    $ renpy.pause(0.5)
    scene ep4_morning_talk_derek13 with dissolve
if ep4_derekFuckedArieth:
    de "I banged Arieth with Jacob in there."
    mc "What!? I didn't think you went through with that!"
    de "What can I say? I have a soft spot for redheads and Jacob's a cool dude."
mc "How sure are you that you'll get that closet?"
de "I'm pretty sure and it beats living with Bert."
play sound "sound_effects/fart.mp3"
"*{i}Farts{/i}*"
mc "Can I get your dorm when you move out? I'm not convinced they will let me stay there as well."
de "Be more confident. We'll share that closet if worst comes to worst."
de "You're my brother, [mc_de]."
$ renpy.music.stop(channel="sfx1", fadeout=3)
stop music fadeout 3
de "Family comes first!"
jump ep4_jmq_label

label ep4_afternoon_derek_label:
play music "music/ep2/rockin_riff.mp3"
jump ep4_freeroam_derek_label

label ep4_pink_rose_label:
$ ep4_pinkRoseEvent = True
play music "music/ep2/sound_of_summer.mp3"
scene ep4_pink_rose with wipeleft
rs "Hey, there you are! Did you get lost?"
scene ep4_pink_rose1 with dissolve
de "It's not easy finding this place buzzed!"
scene ep4_pink_rose2 with dissolve
tm "Let's go already!"
scene ep4_pink_rose3 with dissolve
rs "You heard him."
scene ep4_pink_rose4 with dissolve
rs "Stanley!"
stan "Hell fucking no! Not him!"
mc "Me?"
scene ep4_pink_rose6 with dissolve
rs "It's cool, Stanley."
rs "It won't happen again."
scene ep4_pink_rose7 with dissolve
stan "You're paying double for him! This is not a DIKs only night."
stan "And if he causes any more trouble, this deal is off."
scene ep4_pink_rose8 with dissolve
rs "Don't worry about it. He won't drink that much tonight. Correct?"
mc "Me? Uh...yeah. What exactly did I do last time?"
scene ep4_pink_rose9 with dissolve
stan "Is this bitch for real?"
scene ep4_pink_rose8 with dissolve
rs "Let's go, boys."
scene ep4_pink_rose12 with dissolve
stan "I'll be watching your ass closely."
if dtype > 0:
    mc "(He really doesn't like me... What the fuck did I do?)"
elif True:
    mc "(*{i}Gulp{/i}* He really doesn't like me... What did I do?)"
hide screen phone_screen
scene ep4_pink_rose13 with dissolve
tm "I'll be at the bar."
rs "Hey, I'll join you in a bit."
scene ep4_pink_rose15 with dissolve
rs "Listen... Tommy's a bit upset tonight."
rs "Don't take it personally. Go have fun."
scene ep4_pink_rose16 with dissolve
mc "This place sure looks different tonight."
de "Yeah, the cock to pussy ratio is way off..."
de "Looks like all girls are busy."
jump ep4_fr_sclub1_label

label ep4_derek_morning_label:
scene ep4_derek_morning with fade
play music "music/ep4/inspiring_acoustic.mp3"
play sound "sound_effects/cellphone.mp3"
de "[mc_de_up]."
mc "Huh?"
de "Your phone is ringing."
mc "This early?"
scene ep4_derek_morning1 with vpunch
de "Shit, it's 9.45 a.m., we're gonna be late for class!"
mc "What the fuck, dude! Did you sleep naked!?"
scene ep4_derek_morning2 with dissolve
mc "Hello?"
scene ep4_derek_morning3 with dissolve
ji "Good morning! Are you up and about?"
scene ep4_derek_morning2 with dissolve
if ep4_pinkRoseEvent:
    mc "Almost. I had a long night."
elif True:
    mc "Almost..."
scene ep4_derek_morning4 with dissolve
ji "Sorry, I didn't mean to wake you up."
scene ep4_derek_morning2 with dissolve
mc "It's fine, both Derek and I forgot to set the alarm."
mc "Did you want anything?"
de "Where the fuck is my shirt!?"
scene ep4_derek_morning5 with dissolve
ji "Yes. I wanted to let you know that we're going to get sweaty today."
ji "So, it's best that you bring some clothes to exercise in."
scene ep4_derek_morning2 with dissolve
de "Jade's gonna beat my ass!"
mc "Sounds interesting. I look forward to sweating together with you."
scene ep4_derek_morning7 with dissolve
ji "Hahah! Me too! See you later today."
scene ep4_derek_morning8 with dissolve
stop music fadeout 3
de "[mc_de_up]! Hurry up! I already lost Jade, don't make me lose Cathy, too!"

jump ep4_friday_math_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
