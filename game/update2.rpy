label startUpdate2:
jump header_ep2_label
label previousEp2Label:
play music "music/patched/track_previous.mp3"
scene black
$ renpy.pause(2)
hide screen phone_screen
$ previousEpLabel = "startUpdate2b"
show previously_ol
$ renpy.pause()
hide previously_ol
show screen previous_screen
scene d0_date_26b with wiperight
mc "...I've had a crush on you since the start of this summer."
scene d0_date_29 with dissolve
js "I'm already in a relationship..."

scene d1_drive13 with wipeleft:
    linear 10 zoom 1.1
dad "Burgmeister & Royce."
dad "The first day of college..."

scene d1_corridor3 with wipeleft
my "Haha. Do you need a hand?"

scene d1_tribeta27b with wiperight
my "There's the nerd fraternity, the tri-betas..."
scene d1_campus4 with wipeleft
my "...\"the preps\"."
scene d1_campus4b with dissolve:
    linear 10 zoom 1.02
my "That guy over there is Tybalt, their fraternity president."

scene d1_campus5 with wiperight
my "Then we have the jocks, the tri-alphas."
scene d1_campus9 with wipeleft
my "A new frat house, called the DIKs. It's right over there."
scene d1_campus6b2 with wiperight
my "Rumor has it that the HOTs pay for your entire tuition, if you fit their criteria."
scene d1_campus6c
my "I really need that money..."

scene d1_lunch5 with wipeleft
sa "For the last time, Chad..."
sa "FUCK OFF!!!"
scene d1_tribeta7
ch "Stay the fuck away from Sage!"
scene d1_derek9
de "Beating up a jock would grant you instant access to join the DIKs!"
scene ep1_d2_sage2 with wipeleft
sa "I want you to find out who Chad's been fucking behind my back."
sa "If you scratch my back, I'll scratch yours."

scene d1_dormc with wiperight
troy "I'm not going to live here with you."
scene ep1_troy_fight5 with wipeleft
mc "Hey...where's my guitar?"
troy "It's gone."
if ep1_beat_up_troy and ep1_beat_up_troy_won:
    play sound "sound_effects/hit.mp3"
    scene ep1_troy_fight13 with vpunch
    $ renpy.pause(0.5)
    scene ep1_troy_fight16
    mc "THIS IS FAR FROM FUCKING OVER, TROY!"
elif ep1_beat_up_troy:
    play sound "sound_effects/hit.mp3"
    scene ep1_troy_fight14b with vpunch
    $ renpy.pause(0.5)
    scene ep1_troy_fight16b
    mc "I'LL FUCKING GET YOU FOR THIS!!!"
elif True:
    scene ep1_troy_fight17b
    mc "I'LL GET YOU FOR THIS, TROY!"

scene ep1_diks30 with wiperight
tm "Bring us one small item from the HOTs and we'll consider your pledge."
scene ep1_panties6
qu "What do we have here? A fucking perv!"
if ep1_lewd_camila_quinn:
    scene ep1_panties19
    qu "Give this pervert what he really came for."
elif True:
    scene ep1_panties_leaving1 with hpunch
    qu "PERVERT! SOMEBODY CALL SECURITY!!!"

scene ep1_dorm_aftermath18 with wipeleft
de "Are you crazy? You're giving up? You just got here!"
scene ep1_dorm_aftermath25
de "He needs a place to stay and you need someone to share your dorm with!"

scene ep1_quinn_confront43 with wiperight
qu "So? You want the number to my restaurant or not?"
if ep1_accepted_quinn_offer:
    mc "Sure."
elif True:
    mc "No, I don't pay for sex, Quinn!"

scene d1_tribeta34 with wiperight
mg "Ah! I see that you've spotted {i}the Ice Queen{/i}."
scene ep1_lib_thank31
mc "Gah. You seem to have a personal vendetta with me. I'm leaving..."

scene ep1_cafe_maya9 with wiperight
my "Can you promise me to always be honest with me and to never lie?"
mc "I can be 100%% honest with you."

scene ep1_ending7 with dissolve
my "(You can do this, Maya...)"
scene ep1_ending_shock with dissolve
if dtype > 0:
    mc "[maya]... Take your panties off..."
elif True:
    mc "[maya]... What are we doing?"
play sound "sound_effects/zap.mp3"
scene ep1_ending_shock1 with hpunch
$ renpy.pause(0.5)
label startUpdate2b:
if steamConfig or nonPatreonConfig:
    $ state = "ep2_steam"
elif True:
    $ state = "ep2"
call rpc from _call_rpc_1
scene black
hide screen previous_screen
stop music fadeout 3
$ renpy.pause(5)
scene black with dissolve
show screen ep6_title_screen
play music "music/ep2/acoustic.mp3"
$ renpy.pause(5)
hide screen phone_screen
scene ep2_intro0 with fade
$ renpy.pause()
qu "Have you made up your mind?"
scene ep2_intro2 with dissolve
$ renpy.pause()
scene ep2_intro0 with dissolve
$ renpy.pause()
qu "I can see it in your eyes..."
scene ep2_intro5 with dissolve
qu "You need this. We all do."
qu "Don't think of this as an easy escape."
qu "Think of it as liberation."
scene ep2_intro6 with dissolve
qu "With just a single prick..."
qu "...all of our troubles go-"
scene ep2_intro7
qu "Poof!"
scene ep2_intro8 with dissolve
qu "I promise you...it's not addictive..."
qu "Look, we'll do it together."
qu "I'll take half and you'll take the rest. Here!"
scene ep2_intro9 with dissolve
qu "There...Mmmm..."
qu "Just...do...it..."
scene ep2_intro9b with dissolve
qu "Join me..."
scene ep2_intro130 with dissolve
$ renpy.pause()
scene ep2_intro13 with dissolve
$ renpy.pause()
scene ep2_intro15 at transformTop
$ renpy.pause()
scene ep2_intro16 with dissolve
tm "Rusty! Is everything ready?"
scene ep2_intro17 with dissolve
rs "Yes! The girls are here and the chairs are in place."
scene ep2_intro20 with dissolve
tm "Awesome."
scene ep2_intro17 with dissolve
rs "Yeah, well. Just three pledges this year, though."
scene ep2_intro20 with dissolve
tm "It will have to do."
tm "And what about the...stuff?"
scene ep2_intro19 with dissolve
rs "Hey, that's your business. I'm not going to be responsible for that."
scene ep2_intro18 with dissolve
tm "Come on! Just ask Quinn or Riona for me."
scene ep2_intro19 with dissolve
rs "I know I can't stop you from doing it..."
rs "...but I want no part in it. That's all on you."
stop music fadeout 3
scene ep2_intro20 with dissolve
tm "Whatever... That can wait. Time for the fucking ceremony!"

label ep2_cumpetition_label:
play music "music/ep1/lost_souls.mp3"
scene black
dikcs "Ohm...Ohm..."
mc "(Where the fuck did they bring me?)"
dikcs "Ohm..."
mc "(My neck... It still hurts...)"
tm "Brothers. Before us we have the next generation of maggots."
tm "A DIK is not something you become overnight."
tm "DIK is the title you earn through sacrifice and loyalty."
tm "Will any of these maggots before us be worthy?"
dikcs "Ohm..."
tm "Do you, maggot, wish to rise and become a DIK?"
uk "I do!"
tm "Then you will be tested."
tm "How about you, maggot? Do you wish to rise and become a DIK?"
de "Fuck yes!"
mc "Derek?"
if assman:
    de "Ass man?"
elif True:
    de "Bro?"
tm "Then you will be tested."
play sound "sound_effects/shove.mp3"
scene black with hpunch
tm "Maggot!"
mc "Huh?"
tm "Do you wish to rise and become a DIK?"
menu:
    "Yes" if True:
        $ RPdiks += 1
        mc "Yes."
        tm "Then you will be tested."
    "No?" if True:
        mc "No?"
        tm "There's always one fucking guy who has to ruin it."
        tm "Well, fuck you! You will still be tested!"

tm "The path to becoming a DIK is both long and hard."
tm "And tonight you will take your first step on that path!"
stop music fadeout 3
tm "Brothers! The time has come."
tm "It's time for the annual..."
play music "<from 90.1>music/ep2/stryv.mp3"
scene ep2_init6 with vpunch
tm "...CUM-petition!"
dikcs "DIKs! DIKs! DIKs! DIKs!"
scene ep2_init9 with dissolve
tm "Ensure that these maggots are tightly tied up!"
mc "Hey, what are you doing? That's way too tight!"
de "This. Is. Awesome."
scene ep2_init12 with dissolve
tm "Bring in the girls!"
tm "Tonight, the 3 of you will become 2!"
scene ep2_init13 with dissolve
tm "The DIK tradition of pairwise testing lives on!"
tm "Two maggot brothers!"
tm "We're not accepting more and we're {b}not{/b} accepting less!"
scene ep2_init14 with dissolve
tm "The rules are simple!"
tm "If you cum...you lose!"
dikcs "DIKs! DIKs! DIKs! DIKs!"
stop music fadeout 3
tm "Ladies, they are all yours."
play music "music/ep2/phate.mp3"
queue music ["music/ep2/skyline.mp3", "music/ep2/night_lights.mp3", "music/ep2/phate.mp3"]
scene ep2_init16 with dissolve
qu "Hey there, perv boy."
qu "I've called dibs on you."

scene anim_quinn_cump1_ep2 with dissolve:
    size (config.screen_width, config.screen_height)
qu "I'll make you my bitch in no time."
pause
qu "What's the matter?"
qu "I don't grind you as good as Maya?"
mc "What?"
scene ep2_init19 with dissolve
qu "Hahaha!"

scene anim_quinn_cump2_ep2 with dissolve:
    size (config.screen_width, config.screen_height)
qu "You know..."
qu "She wants to be a HOT so badly..."
qu "...I just wonder how badly?"
menu:
    "Defend Maya" if True:
        mc "Stop playing your fucking mind games!"
        mc "Leave Maya alone."
        scene anim_quinn_cump1_ep2 with dissolve:
            size (config.screen_width, config.screen_height)
        qu "Leave Maya alone? Hah, listen to you."
        qu "Pathetic."
    "Say nothing" if True:
        scene anim_quinn_cump1_ep2 with dissolve:
            size (config.screen_width, config.screen_height)
        qu "Your silence speaks more than words, perv boy."
qu "For the record..."
qu "I'm not the one who asked her to join."
qu "That was all her idea."
mc "I know what you're...hngh...doing with the girls in that sorority..."
scene anim_quinn_cump2_ep2 with dissolve:
    size (config.screen_width, config.screen_height)
if quinn_shop_spicy_lvl > 0 or quinn_shop_japanese_lvl > 0 or quinn_shop_freebie:
    qu "So? You're using them. What does that say about you?"
    qu "You're just the same as me."
    qu "There's no shame in admitting that. I can be very..."
    qu "...fun."
elif True:
    qu "Me? I'm innocent."
    qu "And it will stay that way. Got it?"
scene ep2_init30 with dissolve
stu "Ahhhh!!! Oh no!"
tm "Looks like we got ourselves a fast shooter!"
rs "He's out! We can't have a floppy DIK in the house!"
dikcs "DIKs! DIKs! DIKs! DIKs!"
scene ep2_init32 with dissolve
tm "And there we have it, ladies and gents! Our new maggot brothers!"
dikcs "*{i}Cheers{/i}*"
scene ep2_init33 with dissolve
de "Aw... Is it over already!?"
scene ep2_init34 with dissolve
tm "You wish."
tm "Now we raise the stakes."
scene ep2_init35 with dissolve
de "Mine's already up."
scene ep2_init34 with dissolve
tm "Haha! That's good. Because on comes the condom."
scene ep2_init37 with dissolve
mc "Hey!"
scene ep2_init37b with dissolve
tm "The loser..."
tm "...has to eat it!"
de "What!?"
scene anim_quinn_cump1_ep2 with dissolve:
    size (config.screen_width, config.screen_height)
qu "And the real game begins..."
if ep1_lewd_camila_quinn:
    qu "From what I saw in the showers..."
    qu "...I need some extra tricks to get you off."
scene anim_quinn_cump3_ep2 with dissolve:
    size (config.screen_width, config.screen_height)
qu "How are you holding up?"
qu "You've gone all quiet on me, [mc_quinn]."
qu "Tell me how much you wish that my panties were off, right now."
qu "I bet you'd love to slide that cock into my tight, wet and cleanly shaven pussy."
scene ep2_init19 with dissolve
qu "Haha! You're good, I'll give you that."
if quinn_shop_spicy_lvl > 0:
    scene anim_quinn_cump1_ep2 with dissolve:
        size (config.screen_width, config.screen_height)
    qu "Camila told me how close she was to fucking you in that booth."
    mc "(So, that was Camila?)"
    menu:
        "Tell her the truth" if True:
            $ dk(1)
            $ ep2_quinnKnowsAboutCamila = True
            mc "Close? Hah, your girls are keeping things from you."
            mc "I was completely in."
            scene ep2_init47 with dissolve
            qu "What!?"
            qu "You're going to pay me extra for that."
            scene ep2_init48 with dissolve
            mc "Hey, all I did was to order something spicy."
            mc "Not my fault that the chef put extra peppers on my order."
            scene ep2_init47 with dissolve
            qu "Camila..."
            qu "Enough fucking distraction!"
        "Say nothing" if True:
            $ renpy.pause(0.5)
scene anim_quinn_cump2_ep2 with dissolve:
    size (config.screen_width, config.screen_height)
mc "One Mississippi, two Mississippi..."
qu "Counting Mississippi's? How childish."
qu "You need tricks to not cum, huh?"
scene ep2_init52 with dissolve
qu "Riona, cover us up for a second."
scene ep2_init37 with dissolve
mc "Wait what are you-?"
"*{i}Sshhhllllpp{/i}*"
scene ep2_init19 with dissolve
qu "That condom was a distraction anyway."
menu:
    "Make her stop" if True:
        $ dk(-1)
        $ ep2_wonCumpetition = False
        $ bios_history_mc += "I tricked Quinn and lost the CUM-petition.\n\n"
        $ bios_name_mc = True
        $ bios_history_quinn += "Riona, Camila and Quinn danced in the CUM-petition. They seem to have low inhibitions.\n\n"
        $ bios_history_quinn += "I tricked Quinn during the CUM-petition.\n\n"
        $ bios_name_quinn = True
        $ bios_riona = True
        $ bios_history_riona += "Riona, Camila and Quinn danced in the CUM-petition. They seem to have low inhibitions.\n\n"
        $ bios_camila = True
        $ bios_history_camila += "Riona, Camila and Quinn danced in the CUM-petition. They seem to have low inhibitions.\n\n"
        $ bios_name_riona = True
        $ chat_new_bios = True
        mc "Oh!!!!!! I came!!!!"
        scene ep2_init47 with dissolve
        qu "What!?"
        scene ep2_init56 with dissolve
        tm "We have a winner of the CUM-petition! Derek!"
        de "FUCK YES!"
        scene ep2_init57 with dissolve
        tm "Time for the loser to eat the condom!"
        scene ep2_init58 with dissolve
        qu "Swallow it, you bitch!"
        mc "*{i}Gulp{/i}*"
        "*{i}Cheers{/i}*"
    "Let her continue" if True:
        $ ep2_wonCumpetition = True
        $ bios_history_mc += "I fucked Quinn and won the CUM-petition.\n\n"
        $ bios_name_mc = True
        $ bios_history_quinn += "Riona, Camila and Quinn danced in the CUM-petition. They seem to have low inhibitions.\n\n"
        $ bios_history_quinn += "I fucked Quinn during the CUM-petition.\n\n"
        $ bios_name_quinn = True
        $ bios_riona = True
        $ bios_history_riona += "Riona, Camila and Quinn danced in the CUM-petition. They seem to have low inhibitions.\n\n"
        $ bios_name_riona = True
        $ bios_camila = True
        $ bios_history_camila += "Riona, Camila and Quinn danced in the CUM-petition. They seem to have low inhibitions.\n\n"
        $ chat_new_bios = True

        scene ep2_cump_qu_ride with dissolve
        mc "Are you really...?"
        scene ep2_cump_qu_ride1 with dissolve
        qu "No one but us will see this anyway."
        scene anim_quinn_cump1_ep2 with dissolve:
            size (config.screen_width, config.screen_height)
        qu "*{i}Whispers{/i}* Exciting, huh?"
        qu "*{i}Whispers{/i}* All these people watching..."
        qu "*{i}Whispers{/i}* ...but they don't see the best part."
        scene ep2_init63 with dissolve
        mc "Oh God..."
        qu "*{i}Whispers{/i}* Can you feel how wet I am?"
        qu "*{i}Whispers{/i}* If this music wasn't blasting so loud, you would hear that sloshing sound your dick makes when I do this..."

        scene anim_quinn_ride_ep2 with dissolve:
            size (config.screen_width, config.screen_height)
        pause
        qu "I can see it in your eyes, [mc_quinn]."

        qu "You're going to cum in my pussy."
        scene anim_quinn_cump1_ep2 with dissolve:
            size (config.screen_width, config.screen_height)
        menu:
            "Ask her to stop" if True:
                mc "Ok, that's enough...stop it."
                qu "Nuh-uh. You can't make me stop. I could thrust forward even deeper if I wanted to."
            "Tease her" if True:
                $ dk(1)
                mc "If you push my cock deeper in, I might be able to."
                mc "This does nothing for me."
                qu "I knew from the start that you were my kind of guy."
                scene ep2_init69 with dissolve
                qu "Hngh...fuck you're huge..."
                scene ep2_init69b with dissolve
                qu "*{i}Pants{/i}* I wanna fuck you so hard..."
        scene ep2_init70 with dissolve
        de "Ahhh!!!!"
        tm "Derek is out!!!"
        tm "[name] wins the CUM-petition!"
        "*{i}Cheers{/i}*"
        scene ep2_init37 with dissolve
        qu "Damn...just when it started to get interesting."
        scene ep2_init73 with dissolve
        dikcs "EAT IT! EAT IT! EAT IT!"
        scene ep2_init74 with dissolve
        de "*{i}Gulp{/i}*"
        "*{i}Cheers{/i}*"
scene ep2_init75 with dissolve
tm "The annual CUM-petition has ended and two new maggots have emerged victorious!"
scene ep2_init76 with dissolve
tm "Maggots! Take a real good look at the person standing next to you."
scene ep2_init77 with dissolve
tm "That dude is your maggot brother."
tm "And we all know what the DIK code is...?"
dikcs "Family comes first!"
tm "If you can't prove to us that you can care for your brother..."
tm "...neither of you will become DIKs."
scene ep2_init80 with dissolve
de "What?"
tm "Survive your time as maggots together and you both will become DIKs."
tm "It's either both of you..."
tm "...or neither of you."
scene ep2_init81b with dissolve
tm "Enough of this! Time to start the fucking party!"
dikcs "*{i}Cheers{/i}*"
label ep2_after_cumpetition_label:
scene ep2_init82 with wiperight
if assman:
    de "Ass man! We're so in! Right?"
elif True:
    de "Bro! We're so in! Right?"
$ guideSuggestedPage = 52
scene ep2_init83 with dissolve
menu:
    "Positive response" if True:
        $ ep2_negativeStance = False
        mc "Totally!"
        scene ep2_init82 with dissolve
        de "Now we just pass their stupid tests together and move to this awesome mansion!"
    "Negative response" if True:
        $ ep2_negativeStance = True
        mc "I'm not so sure about this..."
        scene ep2_init82 with dissolve
        de "Come on! Think about it!"
        de "As soon as we're DIKs we can just move from our shitty dorms to this awesome mansion!"
        scene ep2_init83 with dissolve
        mc "If I look past the whole \"leaving me outside naked\" part."
        mc "They still fucking stunned me, put some hood on me and dragged my ass over here!"
        mc "And this CUM-petition...that's pretty demeaning."
        scene ep2_init86 with dissolve
        de "Wow! Really?"
        mc "Yeah, I'm pissed."
        scene ep2_init82 with dissolve
        de "Hey, you're still alive, though..."
        de "...and just think about it..."
de "You wouldn't have to share a dorm with my fugly sister anymore."
scene ep2_init83 with dissolve
menu:
    "I like Maya" if True:
        $ bios_history_derek +="I told Derek that I like Maya.\n\n"
        $ bios_name_derek = True
        $ chat_new_bios = True
        $ ep2_toldDerekLikedMaya = True
        mc "Hey, don't say that. I like Maya."
        scene ep2_init91b with dissolve
        de "..."
        de "What did you do to my sister?"
        mc "Nothing!"
        scene ep2_init91 with dissolve
        de "Nothing..."
        scene ep2_init92 with dissolve
        de "...yet?"
        scene ep2_init91 with dissolve
        menu:
            "Nothing" if True:
                mc "No, just nothing!"
                de "Good..."
            "Nothing...yet" if True:
                mc "Nothing..."
                mc "...yet."
                scene ep2_init93 with dissolve
                de "*{i}Gasps{/i}*"
                de "We're supposed to be brothers, you know."
                scene ep2_init94 with dissolve
                mc "Dude, come on."
                scene ep2_init93 with dissolve
                de "And that's my maggot sister you're talking about."
                scene ep2_init94 with dissolve
                mc "Yeah, so?"
                scene ep2_init93 with dissolve
                de "That's...fucking incest, dude!"
                scene ep2_init94 with dissolve
                mc "Come on, it's not!"
                scene ep2_init97 with dissolve
                de "You disgust me!"
    "Nice" if True:
        $ ep2_toldDerekLikedMaya = False
        mc "It would be great to get another place to stay."
        scene ep2_init82 with dissolve
        de "Tell me about it. Nine months inside a vagina with her was enough for me to know that."
        scene ep2_init83 with dissolve
        mc "Inside...a vagina?"
scene ep2_init100 with dissolve
de "You promise that you will see this through with me?"
de "You're not gonna grab your bag and leave again?"
scene ep2_init101 with dissolve
if not ep2_negativeStance:
    mc "I don't like what they did to get me here..."
    mc "...and I'm not going to trust them that easily, for now..."
    mc "...but I promise, I'm staying with you."
    mc "We're going to do all the crazy shit they have planned together..."
    mc "...and we're gonna be DIKs by the end of it."
    scene ep2_init102 with dissolve
    de "I think I just came a little..."
elif True:
    mc "I know you want this, but if I have to do a lot of crazy things, I'm not sure I'm gonna be able to do it."
    mc "I'm having a real hard time overlooking what they did so far..."
    scene ep2_init104 with dissolve
    de "Come on! I helped you get a place to stay! You owe me this!"
    mc "Really?"
    de "It will be fun! I promise!"
    scene ep2_init106 with dissolve
    de "I really want this... This is the only reason I came here."
    de "Please don't take it away from me... Please!"
    scene ep2_init107 with dissolve
    de "I BEG YOU MAGGOT BROTHER! PLEASE!!!"
    mc "Dude, p-people are looking."
    scene ep2_init109 with dissolve
    de "I WANT THEM TO SEE!"
    scene ep2_init108 with dissolve
    mc "What's wrong with you?"
    scene ep2_init109 with dissolve
    de "BROTHER? IS THAT YOU!?"
    scene ep2_init111 with dissolve
    dikcs "..."
    scene ep2_init108 with dissolve
    mc "Yes, my maggot brother. It's me."
    scene ep2_init113 with dissolve
    dikcs "*{i}Cheers{/i}*"
    de "Awesome! You won't regret this."
    de "If it gets too much for you I will carry the load all by myself, just don't leave my side."
$ bios_history_derek +="Derek and I became maggot brothers at the DIKs.\n\n"
$ bios_name_derek = True
$ chat_new_bios = True
jump ep2_freeroam_party_label

label ep2_after_party_freeroam_label:
scene ep2_party_dildo with dissolve
qu "Ok, boys! Now the party can start for real!"
mc "(Maya...)"
qu "Listen up, you manly DIKs and floppy maggots."
qu "You DIKs have your nasty traditions to keep and us HOTs have ours."
scene ep2_party_dildo2 with dissolve
qu "May I present to you, the fresh batch of HOT pledges."
dikcs "*{i}Whistles{/i}*"
qu "They look good, don't they?"
scene ep2_party_dildo3 with dissolve
qu "Now as you all know, we usually do our ritual with the jocks..."
scene ep2_party_dildo4 with dissolve
dikc "*{i}Booh!{/i}*"
dikc "FUCK THE JOCKS!"
scene ep2_party_dildo5 with dissolve
tm "Yes, fuck the jocks!"
scene ep2_party_dildo3 with dissolve
qu "But your always-so-nice Vice President Tommy, here..."
qu "...made us an offer we couldn't refuse."
scene ep2_party_dildo5 with dissolve
tm "That's right, baby! Woooo!!!"
scene ep2_party_dildo8 with dissolve
sa "What?"
scene ep2_party_dildo9 with dissolve
qu "I've got this."
scene ep2_party_dildo3 with dissolve
qu "So, tonight we're making our ritual into a HOT DIK tradition!"
scene ep2_party_dildo4 with dissolve
dikc "FUCK THE JOCKS!"
dikcs "*{i}Cheers!{/i}*"
scene ep2_party_dildo12c with dissolve
jm "FUCK THE JOCKS IN THEIR TIGHT MUSCULAR ASSHOLES!"
scene ep2_party_dildo12b with dissolve
dikcs "..."
scene ep2_party_dildo12 with dissolve
jm "NO HOMO!"
scene ep2_party_dildo14 with dissolve
sa "Ladies...you've been told what the ritual implies..."
sa "Go find yourself the cutest DIK at the party and make out with him."
mc "(What!?)"
scene ep2_party_dildo16 with dissolve
jac "Hey, redhead! Come here!"
dikc "You, blondie! What about me?"
scene ep2_party_dildo18 with dissolve
$ renpy.pause()
scene ep2_party_dildo19 with dissolve
$ renpy.pause()
scene ep2_party_dildo21 with dissolve
my "Hey..."
scene ep2_party_dildo22 with dissolve
mc "Hey."
scene ep2_party_dildo21 with dissolve
$ guideSuggestedPage = 54
my "Would you like to...you know?"
scene ep2_party_dildo22 with dissolve
menu:
    "To make out with you?" if True:
        mc "To make out with you?"
        scene ep2_party_dildo21 with dissolve
        my "Um...yeah."
    "To help you?" if True:
        $ RPmaya += 1
        $ bios_history_maya +="Maya liked that I was being tactful when she needed help at the party.\n\n"
        $ bios_name_maya = True
        $ chat_new_bios = True
        mc "To help you?"
        scene ep2_party_dildo24 with dissolve
        my "Yes."
scene ep2_party_dildo22 with dissolve
menu:
    "Yes" if True:
        $ ep2HelpedMayaAtParty = True
        $ bios_history_maya +="I tried helping Maya with her HOT ritual at the DIK party.\n\n"
        $ bios_name_maya = True
        $ chat_new_bios = True
        mc "Sure...but we need to talk."
        scene ep2_party_dildo21 with dissolve
        my "I know..."
        scene ep2_party_dildo27 with dissolve
        $ renpy.pause()
        scene ep2_party_dildo28 with dissolve
        $ renpy.pause()
    "No" if True:
        $ ep2HelpedMayaAtParty = False
        $ bios_history_maya +="I didn't help Maya with her HOT ritual at the DIK party.\n\n"
        $ bios_name_maya = True
        $ chat_new_bios = True
        mc "After what you did...no, I don't think so."
        scene ep2_party_dildo21 with dissolve
        my "I know...but it wasn't my fault..."
        scene ep2_party_dildo27 with dissolve
        $ renpy.pause()
scene ep2_party_dildo31 with dissolve
qu "Stop it, Maya."
qu "You fucking suck at following directions."
qu "Didn't you hear what Sage just said?"
scene ep2_party_dildo33 with dissolve
my "Yes, to go find the cutest DIK to make out with."
scene ep2_party_dildo34 with dissolve
qu "So, you can listen! I guess you're just stupid, then."
menu:
    "Stop it" if True:
        $ RPmaya += 1
        $ ep2DefendedMayaAtParty = True
        $ bios_history_maya +="I defended Maya from Quinn at the DIK party.\n\n"
        $ bios_name_maya = True
        $ bios_history_quinn +="Quinn noticed that I care for Maya.\n\n"
        $ bios_name_quinn = True
        $ chat_new_bios = True
        if dtype > -1:
            scene ep2_party_dildo35 with dissolve
            mc "Back the fuck off, Quinn!"
            qu "You're so angry, perv boy!"
            scene ep2_party_dildo37 with dissolve
            qu "You've got a soft spot for barbie here, huh?"
            qu "Wanna be her Ken doll?"
            scene ep2_party_dildo38 with dissolve
            qu "I know you're not smooth down there, though."
            play sound "sound_effects/slap.mp3"
            scene ep2_party_dildo39 with hpunch
            mc "Fuck you!"
            scene ep2_party_dildo41 with dissolve
            qu "Good to know."
        elif True:
            scene ep2_party_dildo41 with dissolve
            mc "Too far, Quinn. Can't you see that she's uncomfortable?"
            qu "..."
    "Let Quinn continue" if True:
        $ ep2DefendedMayaAtParty = False
        $ bios_history_maya +="I didn't defend Maya from Quinn at the DIK party.\n\n"
        $ bios_name_maya = True
        $ bios_history_quinn +="Quinn noticed that I didn't defend Maya.\n\n"
        $ bios_name_quinn = True
        $ chat_new_bios = True
        scene ep2_party_dildo41 with dissolve
        qu "..."
scene ep2_party_dildo42 with dissolve
qu "Either way..."
qu "This maggot here is not a DIK, yet."
qu "So, go find yourself another pretty boy and make his night. Ok?"
my "I...uh..."
label ep2_dildo_label:
stop music
$ renpy.sound.play("sound_effects/glass.mp3", channel = "sfx1", loop= False)
"*{i}CRASH!{/i}*"
play music "music/ep2/metal.mp3"
$ renpy.sound.play("sound_effects/glass.mp3", channel = "sfx2", loop= False)
scene ep2_party_dildo44 with hpunch
$ renpy.pause(0.5)
$ renpy.sound.play("sound_effects/glass.mp3", channel = "sfx1", loop= False)
scene ep2_party_dildo45 with hpunch
$ renpy.pause(0.5)
scene ep2_party_dildo46 with hpunch
$ renpy.sound.play("sound_effects/glass.mp3", channel = "sfx2", loop= False)
$ renpy.pause(1.0)
scene ep2_party_dildo47 with dissolve
hg "Ah!"
rs "What the hell!?"
dikcs "ALPHAS!"
$ renpy.sound.play("sound_effects/glass.mp3", channel = "sfx2", loop= False)
scene ep2_party_dildo49 with hpunch
hg "Ah!!!"
$ renpy.sound.play("sound_effects/glass.mp3", channel = "sfx1", loop= False)
scene ep2_party_dildo50 with hpunch
$ renpy.pause(1.0)
$ renpy.sound.play("sound_effects/glass.mp3", channel = "sfx2", loop= False)
scene ep2_party_dildo51 with hpunch
$ renpy.pause(1.5)
scene ep2_party_dildo52 with dissolve
$ renpy.pause()
scene ep2_party_dildo53 with dissolve
tm "WHAT THE FUCK ARE YOU DOING!?"
scene ep2_party_dildo54 with dissolve
ch "We know the HOTs are in there with you! SAGE!!!"
scene ep2_party_dildo53 with dissolve
tm "So what? Are you jealous because they'd rather party with us than watch you bench at the gym on a Thursday night?"
scene ep2_party_dildo54c with dissolve
an "Monday is chest day! Thursday is leg day!"
scene ep2_party_dildo56 with dissolve
tm "Then go squat on each other's cocks!"
play sound "sound_effects/hit.mp3"
scene ep2_party_dildo57 with hpunch
$ renpy.pause()
scene ep2_party_dildo54b with dissolve
menu:
    "Joke" if True:
        $ ep2_jokedDawe = True
        $ dk(1)
        $ RPjocks -= 1
        $ RPdiks += 1
        $ bios_history_tommy +="Tommy loved that I made fun of Dawe and Chad at the DIK party.\n\n"
        $ bios_name_tommy = True
        $ bios_history_dawe +="I made fun of Dawe and Chad at the DIK party.\n\n"
        $ bios_name_dawe = True
        $ bios_history_chad +="I made fun of Dawe and Chad at the DIK party.\n\n"
        $ bios_name_chad = True
        mc "Funny that you guys own this many dildos..."
        scene ep2_party_dildo59 with dissolve
        mc "Tell me...are they all from your personal stash, Chad?"
        mc "Or did you pull a dozen out of Dawe's ass, too?"
        dikcs "Ohhhhh!"
    "Keep quiet" if True:
        $ ep2_jokedDawe = False
$ bios_jimmy = True
$ bios_john = True
$ bios_alex = True
$ chat_new_bios = True
scene ep2_party_dildo61 with dissolve
dw "Look, Chad! See who it is?"
scene ep2_party_dildo54d with dissolve
ch "[name]! Again!? SAGE!!!?"
scene ep2_party_dildo61 with dissolve
dw "Typical fucking DIKs!!! Always stealing what's ours!"
scene ep2_party_dildo56 with dissolve
tm "Get fucked! They're here because they want to be!"
tm "Times are changing! You guys are out, we're in."
scene ep2_party_dildo65 with dissolve
an "Doesn't look like that to me."
scene ep2_party_dildo66 with dissolve
ch "Sage!"
sa "Yes, I hear you, Chad. Jeez!"
sa "What the fuck were you thinking? You could have hurt someone!"
scene ep2_party_dildo67 with dissolve
dw "Stay the fuck away from the HOTs or next time it won't be dildos coming through the windows!"
scene ep2_party_dildo68 with dissolve
rs "What the fuck does that even mean?"
scene ep2_party_dildo67 with dissolve
dw "CUNTS!!!"
label ep2_story_label:
stop music fadeout 5
scene ep2_party_story with dissolve
tm "Fucking jocks!"
jac "Hey, the girls left."
rs "We know. It's getting worse every week since last semester."
play music "music/ep1/they_say.mp3"
tm "This time they went too fucking far!"
scene ep2_party_story4 with dissolve
mc "What's the deal with you guys and the jocks?"
scene ep2_party_story5 with dissolve
rs "Well it's-"
tm "Hey! That's my story. I'll tell it."
scene ep2_party_story6 with dissolve
tm "Gather around, maggots. It's history time!"
tm "For thousands of years-"
rs "One year."
tm "...the alphas and the DIKs have been at war-"
jac "Been mad at Tommy."
scene ep2_party_story10 with dissolve
tm "Hey, shut up!"
scene ep2_party_story6 with dissolve
tm "{i}It all started a cold Friday night.{/i}"
tm "{i}In a dark muddy alley, a local bar shone bright.{/i}"
scene ep2_party_story12 with dissolve
tm "{i}Arieth the HOT sat alone and so bored.{/i}"
scene ep2_party_story16 with dissolve
tm "{i}Her tri-alpha boyfriend had passed out on the floor.{/i}"
scene ep2_party_story17 with dissolve
tm "{i}In came a charming and valiant DIK.{/i}"
scene ep2_party_story18 with dissolve
tm "{i}He said \"Come follow me and I'll show you a trick\".{/i}"
scene ep2_party_story19p with dissolve
tm "{i}He made her laugh, he made her cry, he made her orgasm twice.{/i}"
play sound "sound_effects/clank.mp3"
scene ep2_party_story19b with vpunch
tm "{i}But what he had done wasn't proven so wise.{/i}"
scene ep2_party_story20 with dissolve
tm "{i}The jock soon found out and gathered his pals.{/i}"
scene ep2_party_story21 with dissolve
tm "{i}They beat the poor DIK and told him \"No one fucks with our gals\".{/i}"
scene ep2_party_story22 with dissolve
tm "{i}That marked the start of the thousand year war.{/i}"
scene ep2_party_story23 with dissolve
tm "{i}And it all started in that small local bar.{/i}"
jac "Tommy fucked Dawe's girl and he beat Tommy for it."
scene ep2_party_story26 with dissolve
tm "Enough chatting! Maggots! You have work to do."
tm "These plastic cocks aren't gonna pick themselves up."
$ bios_history_tommy +="Tommy fucked Dawe's girl in the past. That's the reason why the jocks and DIKs don't get along.\n\n"
$ bios_history_arieth += "Tommy has fucked her as well...\n\n"
$ bios_name_tommy = True
$ chat_new_bios = True

scene ep2_party_story27 with wipeleft
de "Man, what a weird fucking party."
de "I've never seen this many dildos before."
scene ep2_party_story28 with dissolve
menu:
    "Joke" if True:
        $ dk(1)
        $ RPderek -= 1
        mc "Never checked your sister's drawer?"
        scene ep2_party_story28b with dissolve
        de "Dude...not funny."
        $ bios_history_derek +="I made a joke at Maya's expense. Derek didn't like that.\n\n"
        $ bios_name_derek = True
        $ chat_new_bios = True
    "Me neither" if True:
        mc "Me neither..."
        mc "I haven't even seen one before."
        scene ep2_party_story28c with dissolve
        de "I knew a girl who said \"everything's a dildo if you push hard enough\"."
        mc "Hahah!"

scene ep2_party_story29 with dissolve
mc "Rusty, where do you want us to put the dildos?"
scene ep2_party_story30 with dissolve
rs "Give them to Jacob. He will save them until we plan our revenge."
scene ep2_party_story30b with dissolve
mc "So, we're getting them back?"
scene ep2_party_story31 with dissolve
rs "Of course!"
scene ep2_party_story30b with dissolve
mc "Hey... I'm not completely sure about all this..."
scene ep2_party_story30 with dissolve
rs "What's wrong? I thought you wanted this."
scene ep2_party_story30b with dissolve
mc "You guys are so fucking mean..."
mc "You left me standing outside with no clothes..."
mc "...and you used Maya to fool around with me and stun me!"
mc "It hurt like fucking hell and I almost pissed myself!"
scene ep2_party_after1d with dissolve
rs "What? Hold up."
rs "First off, that naked thing..."
rs "...yeah it sucks, but it's tradition."
rs "We take traditions very seriously around here."
scene ep2_party_after1e with dissolve
rs "Just ask Jacob how it is..."
rs "When he did his initiation, he was arrested."
rs "He was mad as fuck and wanted to beat the shit out of us."
rs "But he sucked it up and if you ask him today..."
rs "...it's one of his fondest memories of this place."
scene ep2_party_after1f with dissolve
rs "It gets tough at times, especially early on..."
rs "...but we're not evil. We're a family."
rs "And just like real brothers, we occasionally give each other a hard time."
scene ep2_party_story31 with dissolve
rs "But we still love each other."
rs "Once you're a DIK, you'll be treated as an equal and you'll get friends for life."
scene ep2_party_after1e with dissolve
rs "So, sorry about the tradition rubbing you the wrong way."
rs "It's a way to thin out the herd."
rs "If there's the slightest part of you who wants this, just shrug it off and push on."
rs "I think you'd look really badass in one of these jackets."
scene ep2_party_after1f with dissolve
rs "Oh, and that Maya thing. I've no clue what you're talking about."
rs "We asked the HOTs to bring you guys here. That's all I know."
scene ep2_party_story30b with dissolve
mc "Oh..."
mc "Well, there's a part of me that wants this..."
mc "...and it's a great way of thanking Derek for helping me."
scene ep2_party_story31 with dissolve
rs "Just enjoy it, dude! You'll remember these days for the rest of your life."
scene ep2_party_story30b with dissolve
mc "Oh! And also..."
mc "I was wondering, since I'm a pledge-"
scene ep2_party_story30 with dissolve
rs "A maggot."
scene ep2_party_story30b with dissolve
mc "Since I'm a maggot and all..."
scene ep2_party_story30 with dissolve
rs "I know you want to, but you can't stay in this house."
scene ep2_party_story30b with dissolve
mc "Why not?"
scene ep2_party_after1f with dissolve
rs "You know. DIK rules."
scene ep2_party_story30b with dissolve
mc "But after I become a DIK, I'll get a room, right?"
scene ep2_party_after1f with dissolve
rs "It's a small house...so there aren't really any rooms left."
scene ep2_party_after5 with dissolve
mc "Oh, come on! This mansion is huge!"
scene ep2_party_after1f with dissolve
rs "Yeah, but all the proper rooms are kind of taken."
rs "But...hm..."
rs "There's a janitor's closet..."
scene ep2_party_after5 with dissolve
mc "That will do!"
scene ep2_party_after1e with dissolve
rs "...that Derek already called dibs on."
scene ep2_party_after15 with dissolve
de "Hey, if you don't mind spooning, feel free to stay with me."
de "I'm very gentle."
mc "I'll pass."
scene ep2_party_after1f with dissolve
rs "And an old shitty library. But dude...to be honest...it's disgusting."
rs "No one ever goes in there..."
rs "...you know...except for when the bathroom is occupied."
scene ep2_party_after5 with dissolve
mc "I'll take it. I know how to use a mop."
scene ep2_party_after1d with dissolve
rs "I'll think about it. But rules still apply..."
rs "...it's a DIKs only house."
scene ep2_party_story30b with dissolve
mc "Ok. Let's discuss it when I'm a DIK, then."
scene ep2_party_after15b with dissolve
tm "I think the maggot here meant to say \"{b}if{/b} I become a DIK\"."
tm "Hell Week is coming up. I expect you to fail miserably."
scene ep2_party_after15 with dissolve
de "Hell Week? What does that mean?"
scene ep2_party_after18b with dissolve
tm "If you thought running around naked on campus was bad..."
tm "...prepare yourselves."
scene ep2_party_after17 with dissolve
tm "All right! That's it for tonight."
stop music fadeout 3
tm "Time for you maggots to get the fuck out of here."

label ep2_derek_talk_label:
scene ep2_party_after19 with dissolve
play music "music/ep1/your_smile.mp3"
de "Isn't this exciting?"
scene ep2_party_after20 with dissolve
mc "Why didn't you leave that dildo with Jacob?"
scene ep2_party_after21
de "Just think about the parties we will have in there!"
de "Booze all over!"
de "Girls everywhere!"
scene ep2_party_after22 with dissolve
de "And did you see that new HOT girl, Camila?"
if assman:
    de "I know you're the ass man, but man..."
de "I wouldn't mind using her ass as my own personal bouncy castle."
scene ep2_party_after23 with dissolve
mc "Yeah, she's all right."
scene ep2_party_after24 with dissolve
de "Hey, I saw you talk to Quinn."
de "Do you have a plan for her?"
scene ep2_party_after23 with dissolve
mc "What do you mean by that?"
scene ep2_party_after24 with dissolve
de "A plan for our revenge!"
scene ep2_party_after23 with dissolve
mc "No, not yet. How about you?"
scene ep2_party_after24 with dissolve
de "I have the perfect idea for her."
de "But I'm not sure how we should go about doing it."
scene ep2_party_after29 with dissolve
mc "Do I want to know what it's about?"
scene ep2_party_after30 with dissolve
de "It's really simple! I call it tits for tat."
scene ep2_party_after29 with dissolve
mc "You want us to steal her clothes."
scene ep2_party_after32 with dissolve
if assman:
    de "Yes! Ass man and D-boy are operating on the same fucking wavelength!"
elif True:
    de "Yes! Maggot bro and D-boy are on the same fucking wavelength!"
scene ep2_party_after29 with dissolve
mc "You call yourself D-boy?"
mc "Is it because you talked to John Boy at the party?"
scene ep2_party_after35 with dissolve
de "Perhaps."
scene ep2_party_after36 with dissolve
mc "You're an idiot."
scene ep2_party_after35 with dissolve
de "Hah! You sound just like sis."
scene ep2_party_after36 with dissolve
mc "So, we steal Quinn's clothes, huh?"
scene ep2_party_after32 with dissolve
de "Yes, but it has to be when she least expects it and when we get maximum bang for our buck."
scene ep2_party_after36 with dissolve
mc "You have no idea how to do it."
scene ep2_party_after35 with dissolve
de "Not a clue."
scene ep2_party_after32 with dissolve
de "But that's what you and I should work towards."
stop music fadeout 3
de "As soon as that opportunity shows, we do it."
$ bios_history_derek +="Derek wants us to steal Quinn's clothes, just like she did to us. Tits for tat is what he called it.\n\n"
$ bios_name_derek = True
$ chat_new_bios = True

label ep2_maya_confront_label:
scene ep2_maya_confront with fade
play music "music/ep1/lonely.mp3"
mc "Hey? Are you in here?"
my "Hey..."
mc "It's so dark."
my "I was hoping that you wouldn't notice me and just go to sleep..."
$ guideSuggestedPage = 55
scene ep2_maya_confront1 with dissolve
menu:
    "Joke" if True:
        if dtype > 0:
            $ RPmaya -= 1
            $ bios_history_maya +="I tried cheering Maya up with a joke. It failed.\n\n"
            $ bios_name_maya = True
            $ chat_new_bios = True
            mc "Why? So you can start grinding me again?"
            scene ep2_maya_confront2 with dissolve
            my "..."
        elif True:
            $ RPmaya += 1
            $ bios_history_maya +="I tried cheering Maya up with a joke. It worked.\n\n"
            $ bios_name_maya = True
            $ chat_new_bios = True
            mc "Then you should have hidden in the closet or something. You stink at hiding."
            scene ep2_maya_confront3 with dissolve
            my "Haha..."
    "Ask why" if True:
        mc "Why is that?"
scene ep2_maya_confront4 with dissolve
my "I'm sorry for what happened..."
scene ep2_maya_confront5 with dissolve
mc "Are you going to tell me why you did it?"
scene ep2_maya_confront4 with dissolve
my "I can't..."
scene ep2_maya_confront5 with dissolve
mc "For all that talk about promising to be honest with you..."
mc "...and you can't do the same for me."
scene ep2_maya_confront6 with dissolve
mc "It's your turn to show me what kind of person you are, Maya."
mc "...or I'll leave and find another place to stay."
scene ep2_maya_confront7 with dissolve
mc "...hey."
scene ep2_maya_confront8 with dissolve
my "Initiation...that's what she called it."
mc "Who called it that?"
my "Quinn."
scene ep2_maya_confront9 with dissolve
my "She told me the DIKs had made a deal with the HOTs..."
my "They asked the HOTs to have new HOT pledgers go wake up DIK pledgers."
scene ep2_maya_confront10 with dissolve
mc "Yeah...you really woke me up, all right."
scene ep2_maya_confront9 with dissolve
my "I found out that the other girls actually just woke them up."
my "Not in the way I had to do it."
scene ep2_maya_confront10 with dissolve
mc "So, she told you to go grind on me and stun me?"
scene ep2_maya_confront13 with dissolve
my "{b}Told{/b} me to go do it? No way!"
scene ep1_ending6b with dissolve
my "She and her friends wanted to watch me do it."
scene ep2_maya_confront14 with dissolve
my "She told me to not warn you or anything..."
scene ep2_maya_confront15 with dissolve
my "I didn't know that she planned to stun you..."
scene ep2_maya_confront16 with dissolve
my "I swear!"
scene ep2_maya_confront17 with dissolve
mc "Why did you do it?"
scene ep2_maya_confront18 with dissolve
my "You know why I did it..."
scene ep2_maya_confront17 with dissolve
mc "The tuition?"
scene ep2_maya_confront18 with dissolve
my "Well...the hope of getting free tuition..."
scene ep2_maya_confront17 with dissolve
mc "So, she didn't even offer you it?"
scene ep2_maya_confront18 with dissolve
my "She said that she might have an offer for me, if I passed the initiation..."
my "...but not what for."
scene ep2_maya_confront17 with dissolve
mc "(Not...like she's using Camila...right?)"
menu:
    "Tell her what you know" if True:
        $ ep2_recommendedSage = True
        $ bios_history_maya +="I told Maya to trust Sage instead of Quinn.\n\n"
        $ bios_name_maya = True
        $ chat_new_bios = True
        mc "Don't trust Quinn, Maya."
        scene ep2_maya_confront23 with dissolve
        my "What?"
        mc "She's evil!"
        scene ep2_maya_confront23b with dissolve
        my "Evil? Come on, she's just a bit...rough around the edges."
        scene ep2_maya_confront17 with dissolve
        mc "Nope. EVIL. I know what she does with her girls."
        mc "She uses them to earn money."
        scene ep2_maya_confront26 with dissolve
        my "Uses them how?"
        scene ep2_maya_confront17 with dissolve
        mc "Just...don't trust her, Maya. Please!"
        scene ep2_maya_confront23b with dissolve
        my "Maybe I could talk to Sage, instead?"
        my "She seems kind of cool."
        scene ep2_maya_confront17 with dissolve
        mc "Yes! Sage! Do that!"
        mc "Just not Quinn!"
    "Don't tell her about Quinn" if True:
        $ ep2_recommendedSage = False
        $ bios_history_maya +="I didn't tell Maya about Quinn.\n\n"
        $ bios_name_maya = True
        $ chat_new_bios = True
        mc "I don't know, Maya..."
        mc "I don't think it's the best idea."
        scene ep2_maya_confront23b with dissolve
        my "It is what it is...I'll wait and see what her offer is."

scene ep2_maya_confront30 with dissolve
my "I can't believe I used you this way..."
my "Can you forgive me?"
scene ep2_maya_confront17 with dissolve
mc "What you did...it crossed a line..."
mc "...but it's not your fault that you got used."
mc "I believe in second chances, so I'll forgive you..."
mc "...but please think extra before you do something stupid, next time."
scene ep2_maya_confront32 with dissolve
my "Thank you..."
scene ep2_maya_confront17 with dissolve
mc "So, you're being 100%% honest with me now?"
scene ep2_maya_confront32 with dissolve
my "Maybe 99%%..."
mc "Haha."

scene ep2_maya_confront17 with dissolve
mc "Seriously, though..."
mc "Are you really that desperate?"
scene ep2_maya_confront18 with dissolve
my "What do you mean?"
scene ep2_maya_confront17 with dissolve
mc "That you would do anything they tell you for money?"
scene ep2_maya_confront36 with dissolve
my "No...I don't know."
my "You just don't understand where I'm coming from."
scene ep2_maya_confront37 with dissolve
mc "So, tell me."
scene ep2_maya_confront36 with dissolve
my "No..."
scene ep2_maya_confront37 with dissolve
mc "Why not?"
scene ep2_maya_confront36 with dissolve
my "Please, don't press me on this."
scene ep2_maya_confront37 with dissolve
mc "I'm just trying to understand you, Maya."
stop music fadeout 5
label ep2_maya1_lewd_label:
if _in_replay:
    hide screen phone_screen
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
scene ep2_maya_confront39 with dissolve
mc "Why won't you let me? What is it you're afraid of?"
scene ep2_maya_confront40 with dissolve
mc "That I would judge you!?"
play music "music/ep1/threes_a_crowd.mp3"
scene ep2_maya_confront41 with hpunch
my "YES! Everyone fucking judges me!"
my "ALL THE FUCKING TIME!"
scene ep2_maya_confront42 with dissolve
my "They say, \"Maya, why don't you do that?\""
my "\"Maya, why are you like this?\""
scene ep2_maya_confront43 with dissolve
my "\"Maya, why do you feel like that?\""
my "\"Maya, why can't you be fucking normal!?"
scene ep2_maya_confront44 with dissolve
my "\"Maya, you're not the daughter I wanted!\""
scene ep2_maya_confront45 with dissolve
my "I..."
scene ep2_maya_confront46 with dissolve
my "..."
mc "\"Not the daughter I wanted?\""
scene ep2_maya_confront48 with dissolve
my "Please...forget I said that."
scene ep2_maya_confront49 with dissolve
mc "Maya..."
scene ep2_maya_confront50 with dissolve
mc "Who wouldn't want someone as sweet as you?"
scene ep2_maya_confront51 with dissolve
$ renpy.pause()
scene ep2_maya_confront52 with dissolve
$ renpy.pause()
scene anim_maya_kiss_01_ep2 with dissolve:
    size (config.screen_width, config.screen_height)
pause
scene anim_maya_kiss_02_ep2 with dissolve:
    size (config.screen_width, config.screen_height)
pause
scene anim_maya_kiss_03_ep2 with dissolve:
    size (config.screen_width, config.screen_height)
pause
scene anim_maya_kiss_04_ep2 with dissolve:
    size (config.screen_width, config.screen_height)
pause
scene ep2_maya_confront53 with dissolve
my "I...um..."
scene ep2_maya_confront54 with dissolve
my "..."
scene ep2_maya_confront55 with dissolve
my "I'll count that as a successful HOT ritual."
scene ep2_maya_confront54 with dissolve
mc "A what?"
scene ep2_maya_confront55 with dissolve
my "Haha..."
my "Making out with the cutest DIK."
mc "Oh."
scene ep2_maya_confront57 with dissolve
my "(What is this guy doing to me?)"
my "(This is so wrong...)"
scene ep2_maya_confront59 with dissolve
my "(...but...)"
my "(...there's something in his eyes...)"
my "(I...have never felt this before...)"
my "(...is it because I've been so lonely?)"
my "(...or because I need someone new?)"
mc "What are you thinking about?"
scene ep2_maya_confront62 with dissolve
my "That I shouldn't be doing this."
my "I've used you enough."
scene ep2_maya_confront59 with dissolve
mc "It's not using someone if it's mutual."
scene ep2_maya_confront62 with dissolve
my "Yeah...but still..."
scene ep2_maya_confront59 with dissolve
mc "I get it."
scene ep2_maya_confront65 with dissolve
my "It's getting pretty late..."
my "...or early I should say."
stop music fadeout 3
mc "Yeah..."
mc "Good night, Maya."
$ bios_history_maya +="I made out with Maya. I pushed her to the point that she revealed that she has real family issues.\n\n"
$ bios_name_maya = True
$ chat_new_bios = True
$ renpy.end_replay()
$ persistent.ep2_lewd_maya1 = True
$ calcScenes()
label ep2_pre_ano_label:
scene black with Fade(1.5,1,0.5)
hide screen phone_screen
$ renpy.pause()
$ renpy.sound.play("music/ep2/first_call.mp3", channel = "sfx1", loop = False)
scene ep2_pre_ano
tm "MAGGOT! WAKE THE FUCK UP!"
mc "AAAHH!!!"
scene ep2_pre_ano1 with dissolve
tm "Time for some morning gymnastics!"
tm "MOVE IT!"
play music "music/ep1/art_nouveau.mp3"
scene ep2_pre_ano2 with wipeleft
rs "You fucked Heather again last night?"
scene ep2_pre_ano3 with dissolve
tm "Yeah, but sometimes, I just don't know..."
tm "I tell her to deepthroat me and she just goes halfway before she starts to gag."
scene ep2_pre_ano2 with dissolve
rs "Ah. Yeah, some chicks can't do that."
scene ep2_pre_ano3 with dissolve
tm "Yeah, she's no Riona, that's for sure."
scene ep2_pre_ano4 with dissolve
rs "Oh, last semester there was that girl..."
rs "...what was her name, again?"
scene ep2_pre_ano3 with dissolve
tm "Judith?"
scene ep2_pre_ano4 with dissolve
rs "No, not Judith... Jo-..."
rs "Something Jo-..."
scene ep2_pre_ano3 with dissolve
tm "Joanne?"
scene ep2_pre_ano2 with dissolve
rs "Yes! Thank you!"
rs "Man...that girl really knew how to blow that whistle."
scene ep2_pre_ano3 with dissolve
tm "You lucky dog."
scene ep2_pre_ano2 with dissolve
rs "Yeah, she really was-"
play sound "sound_effects/thud.mp3"
scene ep2_pre_ano8 with vpunch
rs "Hey!"
rs "Did I say stop?"
scene ep2_pre_ano9 with dissolve
de "Dude, I'm so tired!"
rs "I'm not your \"dude\". Who am I?"
de "Father..."
rs "That's right."
scene ep2_pre_ano10 with dissolve
tm "What about you, maggot? Are you quitting, too?"
menu:
    "Yes" if True:
        mc "Yeah, this is just stupid."
        tm "What a bunch of pussies we got this year!"
    "No, father" if True:
        $ bios_history_tommy +="I respected Tommy's authority. He liked that.\n\n"
        $ bios_name_tommy = True
        $ chat_new_bios = True
        $ RPdiks += 1
        mc "No, father."
        tm "Damn straight!"
scene ep2_pre_ano14 with dissolve
mc "Why do we have to do this in our underwear?"
scene ep2_pre_ano15 with dissolve
de "Yeah! I don't get why that's a punishment."
scene ep2_pre_ano15b with dissolve
tm "Well, maggots, this was just your warm up."
tm "Time for your first real assignment."
scene ep2_pre_ano17 with wiperight
tm "See that mansion over there?"
mc "Yeah, that's the Alpha Nu Omega mansion."
scene ep2_pre_ano18 with dissolve
tm "Good boy. You probably already know what greedy cunts those rich boys are."
scene ep2_pre_ano19 with dissolve
rs "We have this tradition in the DIK house..."
rs "...and today we're passing that torch to the two of you."
scene ep2_pre_ano20 with dissolve
mc "What are these for?"
scene ep2_pre_ano20b with dissolve
rs "Just put them on."
scene ep2_pre_ano20c with dissolve
tm "Their president, Tybalt, is a royal cunt."
tm "And we want you to have a bit of \"fun\" in his room."
scene ep2_pre_ano24 with dissolve
de "What kind of fun?"
scene ep2_pre_ano20b with dissolve
rs "Get creative."
rs "But we need photo proof."
scene ep2_pre_ano26 with dissolve
stop music fadeout 3
de "I got my phone with me, so we're all good."
scene ep2_pre_ano27 with dissolve
$ renpy.pause()
play music "music/ep2/marty.mp3"
scene ep2_pre_ano28 with dissolve
de "*{i}Hngh{/i}*"
scene ep2_pre_ano29 with dissolve
de "Oh man! This is so exciting!"
de "I feel like a secret agent."
menu:
    "Agree" if True:
        scene ep2_pre_ano30 with dissolve
        mc "You look like one, too."
    "Focus" if True:
        scene ep2_pre_ano30 with dissolve
        mc "Come on. Focus. I don't want to get caught."
        scene ep2_pre_ano29 with dissolve
        de "Don't worry! They won't see us coming."
scene ep2_pre_ano31 with dissolve
de "Now, if I was a rich president..."
de "...where would I live?"
mc "Probably on the top floor."
scene ep2_pre_ano33 with dissolve
de "Ah! Of course! The penthouse!"
$ guideSuggestedPage = 56
jump ep2_freeroam_ano_label

label ep2_after_ano_freeroam_label:
scene ep2_freeroam_ano53 with dissolve
de "Are you thinking what I'm thinking?"
mc "Probably not."
de "Dude, that thing is begging to be ridden."
de "Gimme a hand!"
scene ep2_freeroam_ano54 with dissolve
de "Hngh..."
mc "Dude, that will break!"
de "Relax, it won't break."
scene ep2_freeroam_ano55 with dissolve
de "Woho!"
de "Sometimes a guy's gotta ride the moose, am I right?"
mc "It's \"the bull\" and also that's not a moose."
de "Whatever... Take the picture!"
scene white
play sound "sound_effects/camera_shutter.mp3"
$ renpy.pause(0.5)
scene ep2_freeroam_ano55 with dissolve
play sound "sound_effects/crack.mp3"
$ renpy.pause(0.5)
scene ep2_freeroam_ano56 with dissolve
de "Ah!"
play sound "sound_effects/thud.mp3"
scene ep2_freeroam_ano57 with hpunch
mc "Shit! Are you ok?"
de "Moose 1 - Derek 0."

scene ep2_freeroam_ano59 with dissolve
de "Who should do it?"
mc "Do what?"
de "Make sexy poses in his bed."
menu:
    "I'll do it" if True:
        $ bios_history_derek +="Derek snapped photos of me getting creative in Tybalt's bed.\n\n"
        $ bios_name_derek = True
        $ chat_new_bios = True
        $ ep2_tybaltPhotoMc = True
        mc "I've got this. Get that camera ready!"
        scene ep2_freeroam_ano60 with dissolve
        de "Sexy! Sexy!"
        scene white
        play sound "sound_effects/camera_shutter.mp3"
        $ renpy.pause(0.5)
        scene ep2_freeroam_ano60 with dissolve
        de "Give me something else!"
        scene ep2_freeroam_ano61 with dissolve
        de "HAH! Excellent!"
        scene white
        play sound "sound_effects/camera_shutter.mp3"
        $ renpy.pause(0.5)
        scene ep2_freeroam_ano61 with dissolve
        de "Hey, I have an idea!"
        scene ep2_freeroam_ano62 with dissolve
        de "PERFECT!"
        scene white
        play sound "sound_effects/camera_shutter.mp3"
        $ renpy.pause(0.5)
        scene ep2_freeroam_ano62 with dissolve
        $ renpy.pause()
    "You'll do it" if True:
        $ bios_history_derek +="I snapped photos of Derek getting creative in Tybalt's bed.\n\n"
        $ bios_name_derek = True
        $ chat_new_bios = True
        $ ep2_tybaltPhotoMc = False
        mc "I think you should do it."
        scene ep2_freeroam_ano63 with dissolve
        de "Dude, take a picture!"
        scene white
        play sound "sound_effects/camera_shutter.mp3"
        $ renpy.pause(0.5)
        scene ep2_freeroam_ano63 with dissolve
        de "Yes! I'm so sexy!"
        scene ep2_freeroam_ano64 with dissolve
        de "Look at me! I'm a rich boy in a rich boy bed!"
        scene white
        play sound "sound_effects/camera_shutter.mp3"
        $ renpy.pause(0.5)
        scene ep2_freeroam_ano64 with dissolve
        de "My farts smell like cinnamon and my cum tastes like cotton candy!"
        mc "Is this how you imagine rich people?"
scene ep2_freeroam_ano65 with dissolve
mc "Great! We have the photos!"
mc "Let's go, I don't want to waste any more time here."
de "Nah, not yet! Let's do something else."
scene ep2_freeroam_ano66 with dissolve
mc "(Man...we're really playing with fire here.)"
mc "Enough, Derek. We got what we came for."
scene ep2_freeroam_ano66b with dissolve
play sound "sound_effects/footsteps_indoors.mp3"
"*{i}Footsteps{/i}*"
mc "Shit, Derek! He's coming back!"
scene ep2_freeroam_ano67 with dissolve
mc "Derek! Where did you go?"
scene ep2_freeroam_ano68 with dissolve
de "Huh?"
mc "What are you doing? Is that..."
mc "...his toothbrush?"
scene ep2_freeroam_ano68b with dissolve
de "I'm leaving a gift."
mc "Tybalt's coming! Hide!"
scene ep2_freeroam_ano68 with dissolve
de "Oh, shit!"
scene ep2_freeroam_ano70 with dissolve
mc "*{i}Whispers{/i}* Don't say a word."
de "Are you sure he's coming?"
mc "I definitely saw him..."
mc "Maybe he left again?"
scene ep2_freeroam_ano73 with dissolve
mc "Either way, let's go. We've pushed our luck far enough."
scene ep2_freeroam_ano73b with dissolve
$ renpy.pause(0.5)
play sound "sound_effects/plop.mp3"
scene ep2_freeroam_ano74
"*{i}Plop{/i}*"
scene ep2_freeroam_ano74b with dissolve
mc "Ok, he's not here. Come on."
scene ep2_freeroam_ano75 with dissolve
mc "What are you doing?"
scene ep2_freeroam_ano75b with dissolve
de "I'm bringing a souvenir."
mc "Really?"
scene ep2_freeroam_ano76 with dissolve
mc "Ok, go for the window."
de "Huh!"
stop music fadeout 3
scene ep2_freeroam_ano77 with dissolve
de "Oh my God!"
scene ep2_freeroam_ano77b with dissolve
ty "Huh! What the hell is this!?"
scene ep2_freeroam_ano78 with dissolve
ty "Security!! Burglars!"
play music "music/ep1/credits.mp3"
scene ep2_freeroam_ano79 with vpunch
mc "Hurry!"
de "Shit! Shit! Shit!"
scene ep2_freeroam_ano80 with dissolve
de "Hngh!"
mc "Forget about that deer! Run!"
scene ep2_freeroam_ano11 with dissolve
mc "Climb faster!"
de "I'm going as fast as I can!"
mc "Just jump!"
scene ep2_freeroam_ano80b with dissolve
$ renpy.pause()
scene ep2_freeroam_ano81 with vpunch
sec "Hey!!! Stop running!"
scene ep2_freeroam_ano81b with dissolve
mc "Hurry! He's almost here!"
scene ep2_freeroam_ano82 with dissolve
mc "Hngh..."
stop music fadeout 3
scene ep2_freeroam_ano83 with dissolve
sec "Damn it!!"
$ bios_history_tybalt +="Derek and I saw Tybalt going through Jill's drawer and sniffing her panties.\n\n"
$ bios_name_tybalt = True
$ chat_new_bios = True

label ep2_post_ano_label:
scene ep2_freeroam_ano84 with wiperight
play music "music/ep1/someways.mp3"
mc "Hahaha!"
de "That shit was crazy!"
mc "Holy crap! Haha!"
mc "My heart is beating so fast!"
scene ep2_freeroam_ano86 with dissolve
de "Such a fucking adrenaline high!"
scene ep2_freeroam_ano85 with dissolve
mc "Haha! You shoved his toothbrush up your ass!"
scene ep2_freeroam_ano86 with dissolve
de "Hell yeah! But what about him!?"
de "Did you see what he did with her panties?"
de "What a fucking creep!"
scene ep2_freeroam_ano85 with dissolve
mc "Totally!"
mc "That girl by the way... Her name is Jill."
scene ep2_freeroam_ano88 with dissolve
de "You know her?"
scene ep2_freeroam_ano85 with dissolve
mc "We've talked a couple of times. She's really nice."
mc "You got the pictures we needed?"
scene ep2_freeroam_ano86 with dissolve
de "Yeah, they will love these shots."
scene ep2_freeroam_ano85 with dissolve
mc "Do you always keep your phone in your underwear?"
scene ep2_freeroam_ano88 with dissolve
de "I like the vibration it makes when someone calls me."
scene ep2_freeroam_ano85 with dissolve
mc "..."
mc "I'm never calling you..."
scene ep2_freeroam_ano88 with dissolve
de "Ah, come on! Don't act like you haven't tried it."
de "Just put it between the balls and the asshole."
de "That's why they invented the vibrating effect."
scene ep2_freeroam_ano85 with dissolve
mc "I don't think that's the truth."
mc "Hey, we're going to be late for class if we don't hurry up."
scene ep2_freeroam_ano88 with dissolve
de "Right. See you in English class, [mc_de]."
$ guideSuggestedPage = 57

label ep2_english_label:
scene ep2_english0 with wiperight
$ ep2_scoldLabel = "ep2_english_label1"
$ updateDikScore()
$ ep2_CathyScoldScreen = True
show screen scoremsg
$ ui.imagebutton("phone_btn_alert", "phone_btn_alert", clicked=ui.returns("OK"), xalign=0.02, yalign=0.02)
if notifications:
    play sound "sound_effects/message.mp3"
$ renpy.pause(2)
hide screen scoremsg
show screen phone_screen_scold
label ep2_english_label1:
scene ep2_english0
my "I heard the DIKs were up to something this morning..."
my "Did you guys have fun?"
label ep2_english_label2:
$ ep2_scoldLabel = "ep2_english_label2"
scene ep2_english0c with dissolve
mc "It was a very {i}rich{/i} experience..."
de "*{i}Holds back laughter{/i}*"
mc "We had some \"homework\" to do."
label ep2_english_label3:
scene ep2_english0f with dissolve
$ ep2_scoldLabel = "ep2_english_label3"
de "Yes..."
de "You can almost say that my ass was swamped with homework."
label ep2_english_label4:
scene ep2_english0g with dissolve
$ ep2_scoldLabel = "ep2_english_label4"
mc "If homework was a toothbrush."
de "HAHAH!"
my "Haha, what?"
jump ep2_no_scold_label
label ep2_scold_label_main:
scene ep2_english_scold with dissolve
hide screen phone_screen_scold
ca "[name], class is starting soon. Turn off your phone, please."
if dtype < 0:
    mc "Sorry, Cathy."
$ ep2_CathyScoldedYou = True
$ renpy.jump(ep2_scoldLabel)
label ep2_no_scold_label:
hide screen phone_screen_scold
scene ep2_english with dissolve
ca "Look who it is!"
scene ep2_english1 with dissolve
ca "Dawe! Welcome back!"
ca "I see that we will be blessed by your presence for another year."
ca "And you brought Anthony with you. Marvelous."
ca "I hope you pay better attention this time."
$ ep2_CathyScoldScreen = False
scene ep2_english3 with dissolve
stop music fadeout 3
ca "Let's do some exercises today. You may begin."
if not minigames:
    scene black with Fade(1.5, 1, 0.5)
    jump ep2_after_english_test
play music "music/ep3/sing_along_with_jim.mp3"
scene english_test_board
jump english101_test2
label ep2_after_english_test:
$ renpy.block_rollback()
if minigames:
    scene ep2_eng_after with wiperight
    stop music fadeout 3
elif True:
    scene ep2_eng_after with fade
play music "music/ep1/scrapbook.mp3"
ca "No, that's not correct, Dawe. Please, try again."
scene ep2_eng_after1 with dissolve
dw "Why the fuck do I need to learn how to spell this shit!?"
scene ep2_eng_after2 with dissolve
an "I'm with Dawe! Our phones have auto-correct! No one writes on paper!"
ca "Sometimes a class is not about learning a skill that you will remember and have use for..."
ca "...but for showing that your minds are capable of passing it."
scene ep2_eng_after3 with dissolve
dw "That doesn't make any sense!"
scene ep2_eng_after2 with dissolve
an "Yeah! I don't remember the skills I learned in this class last year..."
an "...and I already showed that I could pass it."
ca "You didn't pass it, Anthony. You failed."
an "How would {b}you{/b} know?"
ca "*{i}Sigh{/i}*"

play sound "sound_effects/cellphone.mp3"
"*{i}Cellphone rings{/i}*"
scene ep2_eng_after17 with dissolve
if ep2_CathyScoldedYou:
    $ dk(1)
    ca "[name]... Didn't I tell you to turn your phone off?"
elif True:
    ca "[name]...please turn off your cellphone."
mc "Sorry, it's my dad. I have to take this."
scene ep2_eng_after18 with dissolve
mc "Hey dad!"
scene ep2_eng_after19 with dissolve
dad "Son! I'm not calling at a bad time, am I?"
scene ep2_eng_after20 with dissolve
mc "No, I can talk. I was going to call you later today anyway."
scene ep2_eng_after19 with dissolve
dad "Oh, how come?"
scene ep2_eng_after20 with dissolve
mc "I'm coming home this weekend..."
mc "...to see Josy again."
scene ep2_eng_after19 with dissolve
dad "The one that almost got away, huh?"
scene ep2_eng_after20 with dissolve
mc "I have to give it one more chance, dad..."
mc "I just have to..."
scene ep2_eng_after19 with dissolve
dad "You're as stubborn as your mom was."
dad "I'd love to have you home this weekend."
dad "Your room will always be yours."
scene ep2_eng_after18 with dissolve
mc "Great! I'll be home tomorrow, then."
mc "How are things at work?"
scene ep2_eng_after27 with dissolve
dad "We've just started renovating this fancy hotel."
dad "It brings back memories..."
scene ep2_eng_after28 with dissolve
mc "You're not going to fall in love with the owner's daughter this time, though?"
scene ep2_eng_after27 with dissolve
dad "Haha! Not this time."
scene ep2_eng_after31 with dissolve
dad "Hey, kiddo! Where the hell is your hardhat!?"
scene ep2_eng_after32 with dissolve
dad "Son, I have to go. I'll see you tomorrow."
dad "I love you."
menu:
    "Love you, too" if True:
        $ dk(-1)
        mc "I love you, dad."
        scene ep2_eng_after33b with dissolve
        dw "\"I love you, dad!\""
        dw "You fucking homo."
    "Bye" if True:
        $ dk(1)
        mc "Ok, bye!"
scene ep2_eng_after34 with dissolve
mc "(Looks like class is over.)"
scene ep2_eng_after35 with dissolve
de "[mc_de_up]! Did Tommy text you?"
scene ep2_eng_after36 with dissolve
mc "No?"
scene ep2_eng_after35 with dissolve
de "What a sucky father you have..."
de "Rusty just texted and told us to be at the DIKs by 8.00 p.m., tonight."
de "There's gonna be a big fucking party!"
scene ep2_eng_after39 with dissolve
mc "Sweet!"
stop music fadeout 3
scene ep2_eng_after40 with dissolve
de "Come, let's get some food."

label ep2_tyb_jill_label:
play music "music/ep2/freedom.mp3"
scene ep2_tyb_jill with wipeleft
ty "Did they steal anything from you?"
scene ep2_tyb_jill1 with dissolve
ji "Some of my underwear is gone..."
if found_money or found_money2:
    $ ep2_stole_money = True
    ji "...and money, too."
scene ep2_tyb_jill with dissolve
ty "That's just horrible, Jill."
ty "They stole a beloved heirloom of mine and my wallet."
ty "There must have been at least $2000 in it..."
ty "You know how it is. I don't keep count."
ty "I did my best to fight them off, but they ran away scared after the first couple of punches."
scene ep2_tyb_jill1 with dissolve
ji "Thank you..."
ji "Just the thought of someone breaking in here, though..."
scene ep2_tyb_jill5 with dissolve
ty "Don't worry, Jill."
stop music fadeout 3
ty "They won't harm you. I'm here for you."
jump ep2_freeroam_maya_label

label ep2_after_maya_freeroam_label:
scene ep2_fri_party with dissolve
mc "Ok, I'm heading out. I guess I'll be seeing you over there."
scene ep2_fri_party1 with dissolve
my "Over where?"
scene ep2_fri_party2 with dissolve
mc "You know? At the DIK's house party."
scene ep2_fri_party3 with dissolve
my "Nope, not tonight. Sage told me that the HOTs were taking the night off."
scene ep2_fri_party2 with dissolve
if dtype > 0:
    mc "Wow...then this party will suck."
elif True:
    mc "Hm...it won't be as fun without you."
mc "So, what are you going to do?"
scene ep2_fri_party5 with dissolve
$ guideSuggestedPage = 58
my "I'm thinking about having a movie night or something."
scene ep2_fri_party6 with dissolve
menu:
    "Stay with Maya" if True:
        $ bios_history_maya +="I told Maya that I'd rather stay with her than go to the DIK's party.\n\n"
        $ bios_name_maya = True
        $ chat_new_bios = True
        $ RPmaya += 1
        $ ep2_stayWithMaya = True
        if dtype > 0:
            mc "Well, screw that party. I'm in."
        elif True:
            mc "That sounds so much more fun. Mind if I join you?"
        scene ep2_fri_party7 with dissolve
        my "You seriously would rather spend the night with me than go to that party?"
        scene ep2_fri_party8 with dissolve
        mc "Without even second-guessing myself."
        scene ep2_fri_party9 with dissolve
        my "Wow...I..."
        my "All right..."
        scene ep2_fri_party10 with hpunch
        my "Oh!"
        my "You know what we could do?"
        my "We could run out and get some beers and snacks..."
        my "...and have a fun party of our own!"
        scene ep2_fri_party11 with dissolve
        mc "Yes! Let's do that!"
        scene ep2_fri_party10 with dissolve
        my "Yeah!"
        play sound "sound_effects/cellphone.mp3"
        "*{i}Cellphone rings{/i}*"
        scene ep2_fri_party13 with dissolve
        mc "It's Derek."
        scene ep2_fri_party14 with dissolve
        de "Hey, where are you!?"
        scene ep2_fri_party15 with dissolve
        mc "I'm still at Maya's. Hey, listen, I-"
        scene ep2_fri_party14 with dissolve
        de "Dude! Hurry up! They are waiting for you!"
        scene ep2_fri_party15 with dissolve
        mc "I was thinking that I would stay home tonight..."
        scene ep2_fri_party14 with dissolve
        de "NO! You can't! Dude, don't do this to me!"
        de "You promised me!"
        de "Rusty and Tommy will throw us both out!"
        scene ep2_fri_party15 with dissolve
        mc "Fuck..."
        mc "Ok, but I can't stay for very long."
        scene ep2_fri_party14 with dissolve
        de "Just hurry up. They have something planned for us."
        scene ep2_fri_party21 with dissolve
        my "Everything good?"
        scene ep2_fri_party22 with dissolve
        mc "..."
        mc "Listen, I have to..."
        scene ep2_fri_party21 with dissolve
        my "No worries. I understand."
        my "Another time, then."
        scene ep2_fri_party22 with dissolve
        mc "I can come back early. It's just that I have to do some pledge stuff."
        scene ep2_fri_party25 with dissolve
        my "Don't worry. Look who you're talking to."
        my "I know what that's like."
        my "Have a nice night!"
        stop music fadeout 3
        scene ep2_fri_party26 with dissolve
        mc "I'll see you soon, ok?"
    "Go to party" if True:
        $ bios_history_maya +="I didn't offer Maya to stay with her instead of going to the DIK's party.\n\n"
        $ bios_name_maya = True
        $ chat_new_bios = True
        $ ep2_stayWithMaya = False
        mc "Sounds fun!"
        stop music fadeout 3
        mc "Have a nice night, Maya."
        scene ep2_fri_party5 with dissolve
        my "You too!"

label ep2_fri_party_label:
play music "music/ep2/night_lights.mp3"
scene ep2_fri_party28 with wipeleft
rs "Hey, good job getting those photos."
mc "Did we pass?"
tm "We'll see when it's time for your evaluation."
scene ep2_fri_party28b with dissolve
mc "This house is really packed tonight!"
scene ep2_fri_party28 with dissolve
rs "Of course! It's Friday, maggots."
tm "One of the big party nights!"
scene ep2_fri_party29 with dissolve
mc "Hey...the HOTs are here."
scene ep2_fri_party30 with dissolve
tm "You're fucking right they are."
tm "Those jocks can jack each other off tonight."
tm "The HOTs want some DIK!"
scene ep2_fri_party31 with dissolve
de "So, your plan is to piss them off even more?"
tm "Hell yes! There's no way we're giving up partying with the HOTs..."
tm "...just because some fucking asshole ticklers are thrown through our windows."
scene ep2_fri_party33 with dissolve
mc "Maya's not here tonight."
de "Yeah, you're right!"
scene ep2_fri_party34 with dissolve
rs "Who's Maya?"
scene ep2_fri_party34b with dissolve
tm "I told you about Maya, she's-"
de "She's my sis. She pledged the HOTs...she should be here."
rs "Hm...beats me."
scene ep2_fri_party33b with dissolve
tm "Maya's your sister?"
scene ep2_fri_party36 with dissolve
sa "[name]! There you are!"
sa "Come, I wanna dance with you!"
if dtype > 0:
    mc "Sure! Lead the way."
elif True:
    mc "With me?"
scene ep2_fri_party37 with dissolve
tm "Hold on, Sage. These two have some maggot business to attend to first."
scene ep2_fri_party36 with dissolve
sa "Come find me after that, ok?"
scene ep2_fri_party38 with dissolve
$ renpy.pause()

scene ep2_fri_party39 with dissolve
tm "Dude..."
tm "Are you banging that ass?"
scene ep2_fri_party39b with dissolve
menu:
    "I intend to" if True:
        $ ep2_toldTommyBangSage = True
        $ RPdiks += 1
        $ bios_history_tommy +="I told Tommy that I intended to bang Sage. He liked that.\n\n"
        $ bios_name_tommy = True
        $ chat_new_bios = True
        if dtype > 0:
            mc "Not yet, but I'm gonna."
        elif True:
            mc "Not yet, but I want to..."
        scene ep2_fri_party39 with dissolve
        tm "Dude...respect."
        tm "I thought I had balls banging Dawe's girl..."
        tm "...and here you are trying to fuck Sage."
        tm "Don't worry. As long as you're with the DIKs, we got your back."
        scene ep2_fri_party39b with dissolve
        mc "I'm just a maggot, remember."
        scene ep2_fri_party39 with dissolve
        tm "That's what impresses me."
        tm "Ok, fuck you! I've been nice enough."
    "No" if True:
        $ ep2_toldTommyBangSage = False
        $ bios_history_tommy +="I told Tommy that I didn't intend to bang Sage.\n\n"
        $ bios_name_tommy = True
        $ chat_new_bios = True
        mc "Nope. I'm not interested."
        scene ep2_fri_party42 with dissolve
        tm "Pff... You should."
scene ep2_fri_party43 with dissolve
tm "Maggots! Follow me."
tm "It's time for another challenge."
$ bios_history_arieth += "I saw her make out with Jacob at the DIK party...\n\n"
$ chat_new_bios = True
label ep2_fri_party_shots_label:
scene ep2_fri_shots with wiperight
rs "Easy...easy..."
rs "Are you two maggots ready?"
scene ep2_fri_shots1 with dissolve
de "Fuck yes!"
scene ep2_fri_shots2 with dissolve
tm "The first one to down all shots wins."
tm "But you can't use your hands when you do the shot."
scene ep2_fri_shots3 with dissolve
if minigames and tutorials:
    show path_tutorial1 with dissolve
    "{i}\nIn the shot mini-game you must navigate a maze using your mouse cursor.{i}"
    "{i}\nHover over the orange circle to start each attempt.{/i}"
    show path_tutorial2 with dissolve
    hide path_tutorial1 with dissolve
    "{i}\nIf you move outside the path the attempt is lost and your opponent gets a point.{/i}"
    "{i}\nIf you take too long time navigating the maze your opponent also gets a point.{/i}"
    "{i}\nReach the goal before the invisible timer ends to win.{/i}"
    hide path_tutorial2 with dissolve
rs "Ready. Set..."
rs "GO!"
if minigames:
    jump ep2_shot_game_label
elif True:
    menu:
        "Give it all" if True:
            $ ep2_shotWon = True
            scene ep2_fri_shots3 with dissolve
            $ renpy.pause()
            scene ep2_fri_shots3_hand with dissolve
            $ renpy.pause()
            scene ep2_fri_shots5 with dissolve
            tm "YES!"
            scene ep2_fri_shots3_2nohand with dissolve
            $ renpy.pause()
            scene ep2_fri_shots3_belly with dissolve
            $ renpy.pause()
            scene ep2_fri_shots5 with dissolve
            rs "Almost there now! Push!!"
            scene ep2_fri_shots3_1mouth with dissolve
            $ renpy.pause()
            scene ep2_fri_shots3_mouth with dissolve
            $ renpy.pause()
            scene ep2_fri_shots5 with dissolve
            $ renpy.pause()
        "Let Derek win" if True:
            $ ep2_shotWon = False
            scene ep2_fri_shots3 with dissolve
            $ renpy.pause()
            scene ep2_fri_shots3_hand with dissolve
            $ renpy.pause()
            scene ep2_fri_shots5 with dissolve
            tm "YES!"
            scene ep2_fri_shots3_2nohand with dissolve
            $ renpy.pause()
            scene ep2_fri_shots3_belly with dissolve
            $ renpy.pause()
            scene ep2_fri_shots5 with dissolve
            rs "GO! GO! GO!"
            scene ep2_fri_shots3_1mouth with dissolve
            $ renpy.pause()
            scene ep2_fri_shots3_mouth with dissolve
            $ renpy.pause()
label ep2_after_shot_game_label:
$ renpy.block_rollback()
if ep2_shotWon:
    scene ep2_fri_shots8 with dissolve
    $ renpy.block_rollback()
    if minigames:
        show path_bg_result with dissolve
        show text "{font=collegiate.ttf}{size=+65}{color=#d10014}[name]{/color} {color=#000000}[shotWon]{/color}\n{color=#0066ff}Derek{/color} {color=#000000}[shotFail]{/color}{/size}{/font}":
            xalign 0.5
            yalign 0.5
    mc "Done!!!"
    tm "[name] wins!"
    rs "Great job, dude!"
    scene ep2_fri_shots9 with dissolve
    de "Wow, you really know how to drink!"
    scene ep2_fri_shots11 with dissolve
    tm "For the winner..."
    tm "...there's a special shot."
    scene ep2_fri_shots12 with dissolve
    sar "Go ahead, sexy. Lick that shot up."
    sar "Lick it up good."
    menu:
        "Do it" if True:
            $ bios_history_tommy +="I won the shot battle and did the special shot. Tommy liked that.\n\n"
            $ bios_name_tommy = True
            $ bios_history_rusty +="I won the shot battle and did the special shot. Rusty liked that.\n\n"
            $ bios_name_rusty = True
            $ chat_new_bios = True
            $ RPdiks += 1
            scene ep2_fri_shots3_pussy with dissolve
            $ renpy.pause()
            scene ep2_fri_shots5 with dissolve
            $ renpy.pause()
            scene ep2_fri_shots14 with dissolve
            sar "Mmm..."
            scene ep2_fri_shots15 with dissolve
            "*{i}Smack{/i}*"
            scene ep2_fri_shots16 with dissolve
            sar "*{i}Whispers{/i}* That made me so fucking horny..."
            if ep2_hotOpportunity:
                sar "*{i}Whispers{/i}* I'm so excited that you ordered the special from Quinn, too."
                sar "*{i}Whispers{/i}* Come find me after this..."
        "Pass" if True:
            mc "Sorry, I've had enough."
            scene ep2_fri_shots17 with dissolve
            tm "Man...what a pussy!"
elif True:
    scene ep2_fri_shots18 with dissolve
    $ renpy.block_rollback()
    if minigames:
        show path_bg_result with dissolve
        show text "{font=collegiate.ttf}{size=+65}{color=#d10014}[name]{/color} {color=#000000}[shotWon]{/color}\n{color=#0066ff}Derek{/color} {color=#000000}[shotFail]{/color}{/size}{/font}":
            xalign 0.5
            yalign 0.5
    de "Done!"
    tm "Derek wins!"
    rs "What a champ!"
    scene ep2_fri_shots19 with dissolve
    mc "Congrats bro."
    scene ep2_fri_shots20 with dissolve
    de "Man, that last one really did the trick."
    scene ep2_fri_shots21 with dissolve
    tm "Time for your winning shot!"
    ml "Go ahead. Slurp that shot up."
    scene ep2_fri_shots23 with hpunch
    de "*{i}Pukes{/i}*"
    ml "AHHHHHH!!!!!"
    sar "Oh my God!"
    scene ep2_fri_shots25 with dissolve
    tm "HAHAH!"
    rs "FUCKIN' A!"
    scene ep2_fri_shots26 with dissolve
    mc "Hey, are you ok?"
    scene ep2_fri_shots27 with dissolve
    de "Yeah, I'm good. How about you?"
    scene ep2_fri_shots26 with dissolve
    mc "..."
    mc "Don't worry about me."

scene ep2_fri_shots28 with dissolve
tm "Great work, maggots! You're relieved from your duties."
rs "Join the rest for the party! Have a great time tonight."
rs "You've earned it."
if not ep2_shotWon:
    scene ep2_fri_shots30 with dissolve
    de "Bro, don't hate me, but I'm just gonna take off."
    scene ep2_fri_shots31 with dissolve
    menu:
        "Go home to Maya" if True:
            $ guideSuggestedPage = 59
            $ ep2_danceSage = False
            $ ep2_fuckHOT = False
            $ ep2_choseMayaOverParty = True
            $ RPderek += 1
            $ bios_history_derek +="I chose to help Derek home and spend the night with Maya. He liked that.\n\n"
            $ bios_name_derek = True
            $ chat_new_bios = True
            mc "Hey, I'll make sure you get home all right."
            scene ep2_fri_shots32 with dissolve
            de "Thanks! I owe you one."
            scene ep2_fri_shots31 with dissolve
            stop music fadeout 3
            mc "Let me just grab some beers first."
            jump ep2_mayamovienight_label
        "Stay and party with Sage" if True:
            $ guideSuggestedPage = 59
            $ ep2_choseMayaOverParty = False
            $ bios_history_derek +="When Derek had puked, I chose to stay and party with Sage.\n\n"
            $ bios_name_derek = True
            $ chat_new_bios = True
            $ ep2_danceSage = True
            $ ep2_fuckHOT = False
            mc "Yeah, go ahead, dude. Rest up."
            scene ep2_fri_shots32 with dissolve
            de "Yeah, puking just means that the party is over."
            de "Have fun tonight! Do stuff I would do, will ya?"
            scene ep2_fri_shots31 with dissolve
            mc "Haha, I'll try."
            mc "Sage wanted to dance with me."
            stop music fadeout 3
            mc "I think I'm gonna take her up on that offer."
            scene ep2_fri_shots35 with dissolve
            de "Hah, nice..."
            jump ep2_danceSage_label
elif True:
    scene ep2_fri_shots37 with dissolve
    de "It's time to get down and dirty, [mc_de]!"
    de "You're up for it, right?"
    scene ep2_fri_shots38 with dissolve
    menu:
        "Go home to Maya" if True:
            $ guideSuggestedPage = 59
            $ bios_history_derek +="I chose to spend the night with Maya, since she was home alone. Derek liked that.\n\n"
            $ bios_name_derek = True
            $ chat_new_bios = True
            $ ep2_danceSage = False
            $ ep2_fuckHOT = False
            $ ep2_choseMayaOverParty = True
            $ RPderek += 1
            mc "Actually, I'm just gonna grab some beers and head home to Maya."
            scene ep2_fri_shots40 with dissolve
            de "You wanna hang out with my sis instead of partying?"
            de "You're up to something."
            scene ep2_fri_shots41 with dissolve
            mc "Relax. I feel bad for her staying home alone tonight."
            mc "I have no clue why she wasn't invited, but it kind of sucks."
            scene ep2_fri_shots42 with dissolve
            de "When you put it that way..."
            de "...it sounds less sleazy."
            de "Go ahead. Have fun with her..."
            scene ep2_fri_shots44 with dissolve
            de "...but watch your hands!"
            scene ep2_fri_shots41 with dissolve
            mc "I promise to wash my hands."
            scene ep2_fri_shots44 with dissolve
            de "No! Not wash, WATCH!"
            scene ep2_fri_shots41 with dissolve
            mc "Haha, I'm just fucking with you."
            play sound "sound_effects/slap.mp3"
            scene ep2_fri_shots48 with hpunch
            stop music fadeout 3
            mc "Have a fun night, bro."
            jump ep2_mayamovienight_label
        "Stay and party" if True:
            play sound "sound_effects/slap.mp3"
            scene ep2_fri_shots48 with hpunch
            mc "You know it."
            scene ep2_fri_shots37 with dissolve
            de "Awesome! So, what are your plans?"
            scene ep2_fri_shots38 with dissolve
            menu:
                "Find Sage" if True:
                    $ guideSuggestedPage = 59
                    $ ep2_danceSage = True
                    $ ep2_fuckHOT = False
                    $ bios_history_derek +="After the shot battle, I chose to stay and party with Sage.\n\n"
                    $ bios_name_derek = True
                    $ chat_new_bios = True
                    mc "Sage wanted to dance with me."
                    mc "I think I'm gonna take her up on that offer."
                    scene ep2_fri_shots37 with dissolve
                    de "Nice!"
                    scene ep2_fri_shots38 with dissolve
                    mc "What about you?"
                    scene ep2_fri_shots37 with dissolve
                    de "I saw this redheaded HOT girl that I'm aiming for."
                    scene ep2_fri_shots38 with dissolve
                    mc "Do you mean Sage, too?"
                    scene ep2_fri_shots53 with dissolve
                    de "No, not Sage. I don't know this one's name, but she looked hot and stupid."
                    jump ep2_danceSage_label
                "Find Sarah ({color=#ffffff}Requires offer{/color})" if ep2_hotOpportunity:
                    $ ep2_danceSage = False
                    $ ep2_fuckHOT = True
                    $ bios_history_derek +="After the shot battle, I chose to stay and party with Sarah.\n\n"
                    $ bios_name_derek = True
                    $ chat_new_bios = True
                    mc "I'm gonna go and find Sarah."
                    scene ep2_fri_shots37 with dissolve
                    de "Nice!"
                    scene ep2_fri_shots38 with dissolve
                    mc "What about you?"
                    scene ep2_fri_shots37 with dissolve
                    de "I saw this redheaded HOT girl that I'm aiming for."
                    scene ep2_fri_shots38 with dissolve
                    mc "Do you mean Sage?"
                    scene ep2_fri_shots53 with dissolve
                    stop music fadeout 3
                    de "No, not Sage. I don't know this one's name, but she looked hot and stupid."
                    jump ep2_fuckHOT_label

label ep2_danceSage_label:
hide screen phone_screen
play music "music/ep2/sound_of_summer.mp3"
scene ep2_sage_dance with dissolve
mc "(There she is...)"
scene ep2_sage_dance1 with dissolve
mc "(Even in a crowd of people, she stands out.)"
scene ep2_sage_dance2 with dissolve
mc "Hey."
scene ep2_sage_dance3b with dissolve
mc "(Hm...what happened to her all of a sudden?)"
mc "(This is not the Sage I've seen so far...)"
scene ep2_sage_dance2 with dissolve
mc "Are you ok?"
scene ep2_sage_dance5 with dissolve
sa "Why do you ask?"
scene ep2_sage_dance2 with dissolve
mc "You're holding your arms around me like this."
scene ep2_sage_dance5 with dissolve
sa "We're just dancing."
scene ep2_sage_dance2 with dissolve
mc "Ah, just dancing, huh?"
scene ep2_sage_dance9 with dissolve
sa "Yeah."
sa "For now."
scene ep2_sage_dance3b with dissolve
mc "(Ok...she's drunk...)"
mc "(Well...that makes two of us.)"
scene ep2_sage_dance3a with dissolve
$ renpy.pause(13)
show text "Click to continue" with dissolve:
    xpos 0.5
    ypos 0.9
$ renpy.pause(2)
hide text "Click to continue" with dissolve
$ renpy.pause()
menu:
    "Kiss her" if True:
        $ ep2_kissedSage = True
        $ bios_history_sage +="I made out with Sage at the party.\n\n"
        $ bios_name_sage = True
        $ chat_new_bios = True
        scene ep2_sage_dance12 with dissolve
        $ renpy.pause()
        scene ep2_sage_dance13 with dissolve
        $ renpy.pause()
        scene ep2_sage_dance15 with dissolve
        sa "Hey..."
        mc "Something wrong?"
        scene ep2_sage_dance17 with dissolve
        sa "..."
        mc "(Fuck... What did I just do?)"
        scene ep2_sage_dance19 with dissolve
        $ renpy.pause()
        scene ep2_sage_dance21 with dissolve
        $ renpy.pause()
        play sound "sound_effects/shove.mp3"
        scene ep2_sage_dance22 with hpunch
        $ renpy.pause()
        scene ep2_sage_dance_kiss1 with dissolve
        $ renpy.pause()
        scene ep2_sage_dance24 with dissolve
        jac "Bro...look."
        scene ep2_sage_dance25 with dissolve
        tm "That's my son..."
        scene ep2_sage_dance26 with dissolve
        jac "What!? Are you crazy?"
        jac "You do realize what this means?"
        tm "Well, look at {i}who{/i} you're doing yourself tonight."
        jac "Come on. No one cares about Dawe."
        scene ep2_sage_dance25 with dissolve
        tm "Don't worry."
        tm "We'll handle it."
        scene ep2_sage_dance_kiss1 with dissolve
        $ renpy.pause()
        scene ep2_sage_dance30 with dissolve
        sa "Wanna fuck?"
        scene ep2_sage_dance31 with dissolve
        mc "(What's with her?)"
        mc "What about Chad?"
        scene ep2_sage_dance30 with dissolve
        sa "He's not joining us."
        scene ep2_sage_dance31 with dissolve
        mc "That wasn't what I meant."
        scene ep2_sage_dance34 with dissolve
        sa "I know what you meant."
        sa "So? Are you gonna make me regret asking?"
        scene ep2_sage_dance31 with dissolve
        mc "No...I..."
        scene ep2_sage_dance30 with dissolve
        sa "So?"
        sa "Wanna fuck?"
        menu:
            "Yes" if True:
                $ dk(1)
                if dtype > 0:
                    $ RPsage+=1
                    mc "Ever since I first laid eyes on you."
                elif True:
                    mc "Yeah... I do."
                scene ep2_sage_dance_kiss2 with dissolve
                mc "Oh...you meant right here?"
                sa "*{i}Moans{/i}* Mhm..."
                mc "...in public?"
                scene ep2_sage_dance30 with dissolve
                sa "Is that a problem?"
                mc "How drunk are you?"
                scene ep2_sage_dance30b with dissolve
                sa "Haha! I'm pretty fucking hammered."
                scene ep2_sage_dance30 with dissolve
                sa "So, are you gonna whip that cock out?"
                sa "Or do you want me to do it for you?"
                scene ep2_sage_dance50 with dissolve
                jac "MAGGOT! GET OVER HERE! NOW!"
                scene ep2_sage_dance31 with dissolve
                mc "Shit...gimme one second!"
                scene ep2_sage_dance52 with dissolve
                mc "Hey, what's the problem I was kinda busy over th-"
                scene ep2_sage_dance53 with dissolve
                jac "You do realize who you're about to bang in public?"
                scene ep2_sage_dance54 with dissolve
                mc "Yeah, of course."
                scene ep2_sage_dance55 with dissolve
                jac "Man...you're fucking crazy."
                jac "This isn't the CUM-petition anymore, you know that?"
                scene ep2_sage_dance53 with dissolve
                jac "If you fuck her on that couch, everyone at this party will talk about that tomorrow."
                jac "For one, it {b}will{/b} reach Chad before sunrise."
                jac "And secondly, it will reach-"
                scene ep2_sage_dance54 with dissolve
                mc "I know she's his girl, but she came on to me!"
                scene ep2_sage_dance53 with dissolve
                jac "Man, do you think that matters?"
                jac "He will fucking kill you with his own hands."
                jac "I'm not even joking!"
                scene ep2_sage_dance54 with dissolve
                mc "Well, I like that girl. What do you expect me to do?"
                mc "She wants me...I want her..."
                scene ep2_sage_dance53 with dissolve
                jac "Dude... We got your back...but don't be an idiot."
                jac "Do it in private. Not with all these people watching you."
                jac "Go home. Now!"
                scene ep2_sage_dance54 with dissolve
                mc "Come on, don't be like that."
                scene ep2_sage_dance63 with dissolve
                jac "I'm only saying it because I care. Go home."
                scene ep2_sage_dance64 with dissolve
                mc "(Fuck...I know he's right...)"
                mc "(...)"
                mc "(I could ask her to go to her place...right?)"
                scene ep2_sage_dance65 with dissolve
                mc "(...and she's already gone.)"
                stop music fadeout 3
                mc "(What a failure.)"
            "No" if True:
                $ dk(-1)
                mc "No... Not like this."
                scene ep2_sage_dance34 with dissolve
                sa "What do you mean \"not like this\"?"
                sa "Don't you realize what I'm offering?"
                scene ep2_sage_dance34b with dissolve
                mc "I do. But making out with you was stupid enough for me, tonight..."
                scene ep2_sage_dance34 with dissolve
                sa "Are you calling me stupid?"
                scene ep2_sage_dance34b with dissolve
                if dtype>0:
                    mc "No, will you fucking relax!?"
                elif True:
                    mc "No. Calm down."
                mc "I'm just saying that it's bad enough that we're doing this in public..."
                mc "...you know...because of Chad."
                scene ep2_sage_dance39 with dissolve
                sa "I get it..."
                sa "Fucking double standards!"
                sa "It's ok for him to fuck other girls..."
                sa "...but when I wanna fuck another guy there's a problem?"
                scene ep2_sage_dance34b with dissolve
                mc "I don't think you understood me."
                scene ep2_sage_dance41 with dissolve
                sa "Don't bother..."
                mc "(Fuck...)"
                stop music fadeout 3
                mc "(What a failure.)"
    "Leave" if True:
        $ bios_history_sage +="I didn't kiss Sage at the party.\n\n"
        $ bios_name_sage = True
        $ chat_new_bios = True
        $ dk(-1)
        scene ep2_sage_dance28 with dissolve
        mc "Thanks for the dance."
        mc "I'm gonna head back home..."
        mc "I'm getting pretty tired."
        scene ep2_sage_dance29 with dissolve
        stop music fadeout 3
        $ renpy.pause()
        scene black with Fade(1.5,1,0.5)
show screen phone_screen
jump ep2_sat_morning_label2
label ep2_fuckHOT_label:
label ep2_fuckHOT_lewd_label:
hide screen phone_screen
if _in_replay:
    hide screen phone_screen
    if persistent.name == None:
        $ name = "MC"
    elif True:
        $ name = persistent.name
    scene black
play music "music/ep2/jingle.mp3"
scene ep2_hot_1 with wiperight
mc "(Sarah...the special order?)"
mc "(What do I even say to her?)"
scene ep2_hot_2 with dissolve
mc "(Great... Riona and that girl Melanie are right there, too...)"
mc "(Fuck it, she told me to find her.)"
mc "(I'll just approach her and see what happens.)"
scene ep2_hot_3 with dissolve
if dtype > 0:
    mc "Great, you saved a seat for me."
elif True:
    mc "Hey..."
    mc "Is this seat taken?"
scene ep2_hot_4 with dissolve
sar "So...?"
scene ep2_hot_5 with dissolve
mc "So...what?"
scene ep2_hot_4 with dissolve
sar "Got the cash?"
scene ep2_hot_5 with dissolve
mc "Oh...I..."
scene ep2_hot_6 with dissolve
ri "Haha, he's so nervous."
scene ep2_hot_7 with dissolve
ml "Aww, maybe we should go easy on him."
mc "We?"
sar "Haha!"
scene ep2_hot_4 with dissolve
sar "You're with me tonight...pervert."
scene ep2_hot_5 with dissolve
mc "Stop calling me that."
scene ep2_hot_6 with dissolve
ri "Quinn really got under his skin."
scene ep2_hot_11 with dissolve
sar "Now, slowly unbutton your pants, drop them to your ankles and whip it out."
scene ep2_hot_12 with dissolve
mc "What? Right here?"
scene ep2_hot_11 with dissolve
sar "To start with..."
scene ep2_hot_6 with dissolve
ri "Afraid of an audience?"
mc "No..."
play sound "sound_effects/zipper.mp3"
scene ep2_hot_12 with dissolve
mc "Ok...it's out."
scene ep2_hot_15 with dissolve
mc "Oh, shit..."
scene ep2_hot_16 with dissolve
sar "Relax... Focus on my eyes."
sar "And don't make a sound..."
scene anim_hot_footjob_ep2 with dissolve:
    size (config.screen_width, config.screen_height)
sar "How does that feel for you?"
mc "It feels so fucking good..."
pause
sar "Do you like it when I stroke the shaft of your cock?"
mc "Yeah...stroke the tip too..."
scene ep2_hot_16 with dissolve
sar "Maybe Melanie can help with that?"
scene anim_hot_footjob2_ep2 with dissolve:
    size (config.screen_width, config.screen_height)
ml "Like this...?"
mc "Shit! Yes, just like that..."
pause
scene ep2_hot_6 with dissolve
ri "Wow... Your face is all red."
ri "Can you even handle another foot?"
scene anim_hot_footjob3_ep2 with dissolve:
    size (config.screen_width, config.screen_height)
mc "(Shit! This is too much...)"
pause
sar "Haha, wow..."
sar "You look like you're ready to cum any second now."
mc "Can you blame me?"
mc "Three hot girls working it at the same time..."
scene ep2_hot_7 with dissolve
ml "I'm gonna stop right there."
ri "Me too."
sar "Haha!"
mc "What? Why?"
scene ep2_hot_17 with dissolve
ml "Quinn would kinda freak out if she knew about this."
scene ep2_hot_16 with dissolve
sar "You ordered the special, remember?"
sar "Consider that the starter."
scene ep2_hot_12 with dissolve
mc "So there is more to this?"
scene ep2_hot_11 with dissolve
sar "Do you know the janitor's closet?"
scene ep2_hot_12 with dissolve
mc "I think so."
scene ep2_hot_11 with dissolve
stop music fadeout 3
sar "Time for you and me to have the main course and dessert there..."
sar "...right now!"

play music "music/ep1/slow_day_blues.mp3"
scene anim_hot_wall_ep2 with dissolve:
    size (config.screen_width, config.screen_height)
sar "Fuck me, [name]!"
sar "Get your money's worth..."
pause
scene anim_hot_wall2_ep2 with dissolve:
    size (config.screen_width, config.screen_height)
pause
mc "Hngh! You're so tight, Sarah."
sar "Can you feel how I squeeze harder? Like....this?"
scene anim_hot_wall2b_ep2 with dissolve:
    size (config.screen_width, config.screen_height)
mc "Ohhhh!!! Yes, shit that's so fucking tight!"
mc "If you keep that up, I'm going to cum in no time."
pause
scene ep2_hot_sex with dissolve
sar "No way you're cumming early. We're just in the middle of the main course."
sar "Fuck my hole, [name]."
scene anim_hot_doggy_ep2 with dissolve:
    size (config.screen_width, config.screen_height)
sar "Uh-huh! Yes! Just like that!"
pause
scene anim_hot_doggy2_ep2 with dissolve:
    size (config.screen_width, config.screen_height)
mc "You're so sexy, Sarah!"
sar "Are you afraid I'm gonna break or what?"
sar "Push it deeper in!"
pause
scene anim_hot_doggy3_ep2 with dissolve:
    size (config.screen_width, config.screen_height)
sar "*{i}Moans{/i}* YES!!! OH MY FUCKING GOD!!!"
pause
sar "FASTER!"
scene anim_hot_doggyb_ep2 with dissolve:
    size (config.screen_width, config.screen_height)
sar "*{i}Moans{/i}* Pound that pussy, [name]!"
pause

scene ep2_hot_sex2 with dissolve
sar "*{i}Phew{/i}* Main course's over. Time for dessert..."
scene anim_hot_ride_ep2 with dissolve:
    size (config.screen_width, config.screen_height)
sar "The first time fucking a HOT, huh?"
sar "You're lucky, maggot."
sar "No way any other freshman would get this special treat..."
pause
scene anim_hot_ride2_ep2 with dissolve:
    size (config.screen_width, config.screen_height)
sar "Haha... I can feel it twitching inside me, [name]."
pause
scene ep2_hot_cum2 with dissolve
sar "Are you gonna cum for me, [name]?"
scene anim_hot_ride3_ep2 with dissolve:
    size (config.screen_width, config.screen_height)
pause
sar "Are you gonna cum inside my pretty little pussy?"
mc "Yes...I'm...cumming!"
scene ep2_hot_cumb with hpunch
$ renpy.pause(0.5)
scene ep2_hot_cumb with hpunch
$ renpy.pause(0.5)
scene ep2_hot_cumb with dissolve
mc "Oh fuck!!!"
scene ep2_hot_cum with dissolve
sar "Wow, you really filled me up good..."
scene ep2_hot_cum2 with dissolve
sar "I hope you enjoyed your order from Quinn's restaurant..."
stop music fadeout 3
sar "Cum again..."
$ bios_history_quinn +="I fucked Sarah, one of Quinn's girls, at the party.\n\n"
$ bios_name_quinn = True
$ chat_new_bios = True
$ renpy.end_replay()
$ persistent.ep2_lewd_hot = True
$ calcScenes()
$ bios_history_sarah = "I fucked Sarah at the DIK party.\n\n"
$ bios_name_sarah = True
show screen phone_screen
jump ep2_sat_morning_label2

label ep2_mayamovienight_label:
play music "music/ep1/fresh_air.mp3"
scene ep2_mayamovienight with wipeleft
mc "Hey!"
scene ep2_mayamovienight1 with dissolve
my "Oh...you're back already?"
my "Sorry, I didn't think you were getting home this early so I got myself ready for bed."
scene ep2_mayamovienight2 with dissolve
if ep2_stayWithMaya:
    mc "Yeah, I wasn't lying when I said I'd rather spend the night here with you."
elif True:
    mc "Yeah, I'd rather spend the night here with you."
my "..."
scene ep2_mayamovienight1 with dissolve
my "Let me just put something more on..."
scene ep2_mayamovienight3 with dissolve
mc "Oh, come on! That doesn't matter!"
scene ep2_mayamovienight5 with dissolve
mc "Look! I brought beer!"
scene ep2_mayamovienight5b with dissolve
my "Did you drink half of it?"
my "Haha, you really smell of alcohol."
scene ep2_mayamovienight6 with dissolve
mc "Yeah, there was some pledge stuff I had to do."
mc "But I'm not {b}that{/b} drunk."
scene ep2_mayamovienight5b with dissolve
my "It's ok. I'll just have to catch up with you."
scene ep2_mayamovienight8 with dissolve
$ renpy.pause()
scene ep2_mayamovienight9 with dissolve
my "How was the party?"
scene ep2_mayamovienight10 with dissolve
menu:
    "Tell her about the HOTs" if True:
        $ ep2_toldMayaAboutTheHots = True
        mc "It was fun...but I don't know why you weren't invited."
        mc "The HOTs were there."
        scene ep2_mayamovienight11 with dissolve
        my "The pledges too?"
        scene ep2_mayamovienight12 with dissolve
        mc "Hm... No. I don't think I saw any of them."
        mc "Quinn wasn't even there."
    "Don't tell her about the HOTs" if True:
        $ ep2_toldMayaAboutTheHots = False
        mc "It was a fun night..."
        mc "You should have been there..."

scene ep2_mayamovienight13 with dissolve
my "Well, it doesn't matter..."
my "I get to have beer and movie night with you."
scene ep2_mayamovienight8 with dissolve
mc "Hey, let's have our own party!"
scene ep2_mayamovienight14 with dissolve
my "You'd want that?"
scene ep2_mayamovienight16 with dissolve
stop music
play sound "sound_effects/switch.mp3"
mc "Yeah! Like this."
play music "music/ep2/fallen_colors.mp3"
mc "We have beer and now we have music, too!"
scene ep2_mayamovienight18 with dissolve
mc "All that's missing is some dancing!"
scene ep2_mayamovienight19 with dissolve
my "Haha! My God, you look stupid!"
scene ep2_mayamovienight18 with dissolve
mc "Of course I look stupid."
scene ep2_mayamovienight20 with dissolve
mc "I'm drunk and I'm dancing alone. Come join me!"
scene ep2_maya_dance with dissolve
$ renpy.pause(13)
show text "Click to continue" with dissolve:
    xpos 0.5
    ypos 0.9
$ renpy.pause(2)
hide text "Click to continue" with dissolve
$ renpy.pause()
scene ep2_mayamovienight25f with dissolve
menu:
    "Kiss her" if True:
        $ ep2_TriedToKissMaya = True
        scene ep2_mayamovienight26 with dissolve
        $ renpy.pause()
        scene ep2_mayamovienight27 with dissolve
        $ renpy.pause()
        scene ep2_mayamovienight27b with dissolve
        my "Hey...what are you doing?"
        scene ep2_mayamovienight28 with dissolve
        mc "It's no party without a little bit of fooling around, right?"
        scene ep2_mayamovienight29 with dissolve
        my "You're even drunker than I thought."
    "Don't kiss her" if True:
        $ ep2_TriedToKissMaya = False
        $ renpy.pause(0.5)
scene ep2_mayamovienight30 with dissolve
my "Hey, turn down the music and come over here."
$ renpy.music.set_volume(0.8, delay=0, channel='music')
$ renpy.pause(0.5)
$ renpy.music.set_volume(0.6, delay=0, channel='music')
$ renpy.pause(0.5)
$ renpy.music.set_volume(0.4, delay=0, channel='music')
$ renpy.pause(0.5)
$ renpy.music.set_volume(0.2, delay=0, channel='music')
scene ep2_mayamovienight31 with dissolve
mc "We're doing movie night?"
scene ep2_mayamovienight32 with dissolve
my "No, let's skip that for tonight."
my "Let me show you something instead."
scene ep2_mayamovienight33 with dissolve
my "This is me and Derek when we were younger."
mc "Wow, you were so young. And what is Derek doing?"
scene ep2_mayamovienight33b with dissolve
my "Haha! Derek wanted to be a knight and not Santa Claus."
my "Mom was willing to compromise."
my "When my dad saw this picture...he was pretty pissed at Derek."
scene ep2_mayamovienight34 with dissolve
my "This place right here is where my family took us when we were kids."
my "I have so many fond memories of the wildlife."
my "We used to go on caravan holidays every summer."
scene ep2_mayamovienight35 with dissolve
my "This is taken the day of my graduation."
my "I graduated Magna Cum Laude."
my "Do you see?"
if dtype > 0:
    mc "Haha, cum."
    my "Wow, you have spent way too much time with Derek."
elif True:
    mc "Is that your dad?"
    my "Yes."
scene ep2_mayamovienight36 with dissolve
my "And this..."
my "...this is me when I'm at my happiest."
mc "Hey, isn't that the same place as in the picture from before?"
my "It is."
my "The photo is not the best."
mc "I like it. Who's that girl?"
my "Oh, that one is one of my friends who Derek had a crush on."
my "Haha, he got together with her that night and was so happy."
my "It didn't turn into something, though."
scene ep2_mayamovienight37 with dissolve
mc "Why are you showing me all of these photos?"
scene ep2_mayamovienight38 with dissolve
my "You know..."
my "As you said to me... It's my turn to show you who I am."
my "That's what I'm doing..."
my "But I'm gonna take it slow...and slowly work my way up to 100%% trust."
scene ep2_mayamovienight39 with dissolve
my "So, if there are things I don't want to tell you."
my "You will have to be ok with that... Ok?"
scene ep2_mayamovienight37 with dissolve
mc "Of course I'm ok with that."
scene ep2_mayamovienight41 with dissolve
$ renpy.pause()
scene ep2_mayamovienight42 with dissolve
my "..."
mc "Something wrong?"
scene ep2_mayamovienight43 with dissolve
my "It's nothing... I..."
my "We shouldn't be kissing..."
my "And I just know that if I look into your eyes like that..."
my "...it's going to happen..."
my "...again."
$ guideSuggestedPage = 60
scene ep2_mayamovienight42 with dissolve
menu:
    "Why shouldn't we kiss?" if True:
        mc "Why shouldn't we kiss?"
        scene ep2_mayamovienight43 with dissolve
        my "I'm... I can't say."
        scene ep2_mayamovienight42 with dissolve
        mc "Not there yet, huh?"
        scene ep2_mayamovienight43 with dissolve
        my "No..."
        scene ep2_mayamovienight42 with dissolve
        mc "That's ok."
    "Don't you want to kiss?" if True:
        mc "Don't you want to kiss?"
        scene ep2_mayamovienight43 with dissolve
        my "I don't know..."
        my "A part of me screams yes, just do it!"
        my "But then there's this other part...that just..."
        scene ep2_mayamovienight42 with dissolve
        my "..."
$ bios_history_maya +="I had a memorable private party with Maya instead of staying at the DIK's party.\n\n"
$ bios_name_maya = True
$ chat_new_bios = True
label ep2_maya_lewd_label:
hide screen phone_screen
if _in_replay:
    hide screen phone_screen
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
    $ renpy.music.set_volume(0.2, delay=0, channel='music')
    play music "music/ep2/fallen_colors.mp3"
    scene ep2_mayamovienight42 with dissolve
mc "Keep your eyes closed, Maya."
mc "Turn and face me."
scene ep2_mayamovienight49 with dissolve
mc "Just lie there with your eyes closed and breathe."
mc "Truly feel which part you want to listen to."
if dtype > 2 and not _in_replay:
    scene ep2_mayamovienight53 with dissolve
    my "I'm sorry..."
    my "I just have to listen to the other part..."
    scene ep2_mayamovienight55 with dissolve
    mc "That's ok..."
elif True:
    scene ep2_mayamovienight54 with dissolve
    my "It's...a tie..."
    my "I really want to..."
    my "...but...it's just crossing that line that..."
    my "...that..."
    if _in_replay:
        jump ep2_lewd_maya_cont_label
    if dtype > -3 and ep2_TriedToKissMaya:
        $ ep2_fingeredMaya = True
        label ep2_lewd_maya_cont_label:
        scene ep2_mayamovienight58 with dissolve
        $ renpy.pause()
        scene ep2_mayamovienight59 with dissolve
        mc "Let's keep our eyes closed."
        my "Ok..."
        scene ep2_mayamovienight58 with dissolve
        $ renpy.pause()
        scene ep2_mayamovienight60 with dissolve
        $ renpy.pause()
        scene ep2_mayamovienight61 with dissolve
        $ renpy.pause()
        scene ep2_mayamovienight62 with dissolve
        $ renpy.pause()
        scene ep2_mayamovienight63 with dissolve
        $ renpy.pause()
        scene ep2_mayamovienight64 with dissolve
        my "Hngn...mmm..."
        scene ep2_mayamovienight65 with dissolve
        my "*{i}Moans{/i}*"
        scene ep2_mayamovienight66 with dissolve
        my "*{i}Breathes heavily{/i}* Be...gentle..."

        scene anim_maya_finger_ep2 with dissolve:
            size (config.screen_width, config.screen_height)
        mc "(Wow...)"
        mc "(This is the smoothest pussy I've ever felt.)"
        pause
        mc "(I wonder how she reacts if I insert a finger...?)"
        scene anim_maya_finger2_ep2 with dissolve:
            size (config.screen_width, config.screen_height)
        my "Oh my... *{i}Moans{/i}*"
        mc "(Remember...be gentle.)"
        my "Not too deep..."
        mc "(She's so tight...and warm...and wet.)"
        pause
        scene anim_maya_finger3_ep2 with dissolve:
            size (config.screen_width, config.screen_height)
        my "Yes...just like that..."
        my "Don't stop..."
        pause
        my "Go...a little bit faster..."
        scene anim_maya_finger2b_ep2 with dissolve:
            size (config.screen_width, config.screen_height)
        my "Yes! Ahhh!!! I'm...I'm gonna..."
        pause
        my "I'm cumming!!!"
        scene bg anim_maya_finger_cum_ep2 movie with dissolve
        my "OH!!! AAAAAHH!!!!!"
        my "Oh...wow..."
        my "..."
        my "That was just..."
        my "Wow..."
        scene ep2_finger_maya_suck with dissolve
        my "Here...let me just..."
        scene ep2_finger_maya_suck2 with dissolve
        mc "(Oh wow...)"
        scene ep2_finger_maya_suck3 with dissolve
        my "Mmm... Yummy..."
        $ renpy.end_replay()
        $ persistent.ep2_lewd_maya = True
        $ calcScenes()
        $ bios_history_maya +="I made out and fingered Maya tonight...unbelievable.\n\n"
        $ bios_name_maya = True
        $ chat_new_bios = True
        scene ep2_mayamovienight56 with dissolve
        my "Come..."
        my "That was amazing..."
        stop music fadeout 3
        mc "It really was."
        my "I won't forget this night..."
        scene black with Fade(1.5,1,0.5)
        $ renpy.pause(1)
        $ renpy.music.set_volume(1.0, delay=0, channel='music')
        show screen phone_screen
        jump ep2_sat_morning_label
    elif True:
        scene ep2_mayamovienight55 with dissolve
        mc "It's ok. I'm not going to force you."

scene ep2_mayamovienight56 with dissolve
my "Come..."
my "I really do appreciate what you did for me tonight..."
stop music fadeout 3
my "I won't forget it."
scene black with Fade(1.5,1,0.5)
$ renpy.pause(1)
$ renpy.music.set_volume(1.0, delay=0, channel='music')
show screen phone_screen

label ep2_sat_morning_label:
$ renpy.sound.play("sound_effects/rain_inside.mp3", channel="sfx1", loop=True)
scene ep2_sat_maya_bed with fade
mc "(It's morning already...)"
mc "(Sounds like pretty shitty weather...)"
scene ep2_sat_maya_bed2 with dissolve
mc "(What!? Josy...?)"
scene ep2_sat_maya_bed3 with hpunch
mc "(Oh...Maya...we fell asleep like this...)"
mc "(Shit! It's Saturday today!)"
mc "(I'm supposed to go home and see Josy...and dad, of course.)"
mc "(Last night was just...wow...)"
mc "(I don't regret coming home early...)"
mc "(Being with Maya almost made me regret every single second I stayed longer at the DIK house...)"
mc "(She's so cute when she sleeps...)"
scene ep2_sat_maya_bed4 with dissolve
$ renpy.pause()
scene ep2_sat_maya_bed5 with hpunch
my "AH!!!!"
mc "AAAH!"
play sound "sound_effects/shove.mp3"
scene ep2_sat_maya_bed6 with vpunch
my "Oh! Fuck!"
my "Are you ok?"
scene ep2_sat_maya_bed6b with dissolve
my "Hahaha! Fuck!"
my "You scared the crap out of me!"
mc "Not used to waking up next to someone, huh?"
my "It's been a while."
scene ep2_sat_maya_bed8b with dissolve
my "Good morning, [name]."
scene ep2_sat_maya_bed8 with dissolve
mc "Morning, Maya."
mc "Thanks for last night."
scene ep2_sat_maya_bed8b with dissolve
my "You too. I had a blast."
scene ep2_sat_maya_bed8c with dissolve
my "Wow, it's really pouring outside!"
mc "Yeah, I just love rain. It makes such a peaceful sound."
scene ep2_sat_maya_bed9 with dissolve
jump ep2_sat_morning_label3
label ep2_sat_morning_label2:
$ renpy.sound.play("sound_effects/rain_inside.mp3", channel="sfx1", loop=True)
scene ep2_sat_maya_bed9 with Fade(2.5,1,0.5)
mc "Morning, Maya."
my "Good morning, [name]."
my "Did you have a good time, last night?"
mc "From what I can remember...yeah, it was great."
mc "Pretty shitty weather today..."
my "So it seems."
label ep2_sat_morning_label3:
my "What are you up to, today?"
scene ep2_sat_maya_bed10 with dissolve
mc "I'm going back home until tomorrow."
scene ep2_sat_maya_bed11 with dissolve
my "Visiting family?"
$ guideSuggestedPage = 60
scene ep2_sat_maya_bed10 with dissolve
menu:
    "Tell the truth" if True:
        $ ep2_toldMayaTruthAboutDate = True
        $ bios_history_maya +="I told Maya that I was going home to date a girl.\n\n"
        $ bios_name_maya = True
        $ chat_new_bios = True
        mc "Yeah and this girl I used to work with this summer."
        scene ep2_sat_maya_bed12 with dissolve
        my "Oh. Sounds like a date."
        scene ep2_sat_maya_bed14b with dissolve
        mc "Well...it kinda is a date."
        scene ep2_sat_maya_bed14 with dissolve
        my "Oh."
        my "Good for you..."
        scene ep2_sat_maya_bed14b with dissolve
        mc "Does that make you jealous?"
        scene ep2_sat_maya_bed16 with dissolve
        my "Jealous? Me?"
        my "Why would that make me jealous?"
        scene ep2_sat_maya_bed16b with dissolve
        my "I mean...why would it?"
        my "It's not like you and I date or something."
        scene ep2_sat_maya_bed16 with dissolve
        my "So it would be pretty weird if I was jealous."
        my "You know?"
        scene ep2_sat_maya_bed17 with dissolve
        my "..."
        scene ep2_sat_maya_bed18 with dissolve
        my "No...I'm not jealous."
        scene ep2_sat_maya_bed14b with dissolve
        menu:
            "Kiss her cheek" if True:
                $ RPmaya += 1
                scene ep2_sat_maya_bed19 with dissolve
                mc "*{i}Smack{/i}*"
                scene ep2_sat_maya_bed20 with dissolve
                my "You're an idiot."
            "Don't kiss her" if True:
                $ renpy.pause(0.5)
    "Dodge the question" if True:
        $ ep2_toldMayaTruthAboutDate = False
        $ bios_history_maya +="I didn't tell Maya I was going home to date Josy.\n\n"
        $ bios_name_maya = True
        $ chat_new_bios = True
        mc "Yeah, among other things."
scene ep2_sat_maya_bed21 with dissolve
mc "What about you? Any plans?"
scene ep2_sat_maya_bed22 with dissolve
my "It's Saturday, so probably some pledge stuff."
scene ep2_sat_maya_bed21 with dissolve
mc "Don't do anything your brother would do, then."
scene ep2_sat_maya_bed24 with dissolve
my "Haha! I won't."
scene ep2_sat_maya_bed21 with dissolve
mc "Time for me to catch a train."
mc "I'll see you tomorrow."
if ep2_toldMayaTruthAboutDate and ep2_TriedToKissMaya and dtype < 1:
    scene ep2_sat_maya_bed26 with dissolve
    my "Wait!"
    scene ep2_sat_maya_bed27 with hpunch
    $ renpy.pause()
    scene ep2_sat_maya_bed28 with dissolve
    mc "Maya..."
    scene ep2_sat_maya_bed29 with dissolve
    my "Have a nice date."
    $ renpy.music.stop(channel="sfx1", fadeout=3)
elif True:
    scene ep2_sat_maya_bed24 with dissolve
    my "Have a good time!"
    $ renpy.music.stop(channel="sfx1", fadeout=3)
label ep2_sat_train_label:
play music "music/ep2/relaxing_ballad.mp3"
$ renpy.sound.play("sound_effects/train.mp3", channel="sfx1", loop=True)
scene ep2_train_fr0 with wiperight
mc "(Josy...)"
mc "(It just dawned on me that this might be the last time I'll see her...)"
scene ep2_train_fr1 with dissolve
mc "(That is, if she's serious about moving and starting fresh.)"
mc "(I keep thinking about the date we had...)"
scene ep2_train_fr2 with dissolve
mc "(It's so stupid going after her...)"
mc "(There's so much that speaks against us ever being together...)"
scene ep2_train_fr3 with dissolve
mc "(Her boyfriend...)"
mc "(Her not being accepted to college...)"
scene ep2_train_fr4 with dissolve
mc "(Her moving far away...)"
mc "(So, why am I sitting on this train back home to her?)"
scene ep2_train_fr5 with dissolve
mc "(Why is it that I still just can't let go?)"
mc "(It's just a crush...)"
play sound "sound_effects/cellphone.mp3"
"*{i}Cellphone rings{/i}*"
scene ep2_train1 with dissolve
mc "Derek?"
scene ep2_train2 with dissolve
de "[mc_de_up]! Party. Tonight. DIK house."
scene ep2_train1 with dissolve
mc "What? Again?"
scene ep2_train2 with dissolve
de "Man! Check your phone!"
de "I sent you like 10 messages about it already!"
scene ep2_train1 with dissolve
mc "Are you sure you sent them to me?"
mc "Because I didn't get them."
scene ep2_train2 with dissolve
de "..."
de "You know what must have happened?"
de "I think I sent them to someone else."
de "Don't drink and text..."
scene ep2_train1 with dissolve
mc "You're drinking already?"
scene ep2_train2 with dissolve
de "It's Saturday!"
scene ep2_train1 with dissolve
mc "About that party, though..."
mc "I can't make it. I'm going home for the day and I'll be back sometime tomorrow."
scene ep2_train3 with dissolve
de "What!? You have to come!"
de "We're gonna get kicked out!"
scene ep2_train1 with dissolve
mc "Come on, you can explain it to them."
mc "Oh, I know!"
mc "Tell them that I went home to see my family..."
mc "...and that \"Family comes first\"."
mc "They'll love that."
scene ep2_train2 with dissolve
de "Hm...it could work."
de "You're really just going home to see your family?"
scene ep2_train1 with dissolve
mc "Well, there's that and this other thing."
scene ep2_train2 with dissolve
de "Which is?"
scene ep2_train1 with dissolve
mc "A date...sort of."
scene ep2_train2 with dissolve
de "Does she have a friend?"
scene ep2_train4 with dissolve
mc "Haha, I'm sure she has a lot of friends."
scene ep2_train2 with dissolve
de "I meant for me."
scene ep2_train4 with dissolve
mc "I'm not gonna ask her that."
scene ep2_train2 with dissolve
de "Does she swing?"
scene ep2_train4 with dissolve
mc "Ok, I'm hanging up."
scene ep2_train5 with dissolve
mc "(Haha...fucking Derek.)"
mc "(He really is an idiot.)"
$ renpy.music.stop(channel="sfx1", fadeout=3)

label ep2_sat_store_label:
scene ep2_store1 with wiperight
mc "(Maybe she's working today?)"
mc "(If she isn't, I have a perfect opportunity to buy her something for tonight.)"
scene ep2_store2 with dissolve
mc "(Nope, doesn't look like she's here...)"
scene ep2_store3 with dissolve
mc "Hey, Tina!"
tn "Well who do we have here!? If it isn't hot shot [name]."
mc "Hot shot?"
scene ep2_store4 with dissolve
tn "Hey, Steve's words, not mine."
scene ep2_store6 with dissolve
mc "Haha! I see."
mc "How are things?"
scene ep2_store7 with dissolve
tn "About the same. I've missed you."
tn "And now that Josy's gone, too, I have no one to gossip with."
scene ep2_store6 with dissolve
mc "Wait, what? Josy quit?"
scene ep2_store7 with dissolve
tn "Yup, she quit yesterday..."
tn "...it was pretty sudden."
scene ep2_store6 with dissolve
mc "Did she mention why?"
scene ep2_store7 with dissolve
tn "She just said she was leaving town for something new..."
scene ep2_store6 with dissolve
mc "(She's really doing it...)"
mc "(A part of me thought it was all talk.)"
mc "Thanks, Tina."
mc "I'll see you soon, ok?"
scene ep2_store4 with dissolve
tn "I'm not going anywhere anytime soon."

scene ep2_store15 with dissolve
mc "(Fuck, this is not good...)"
mc "(I must convince her to stay.)"
play sound "sound_effects/message.mp3"
scene ep2_store16 with dissolve
js "{i}Hey, are you in town?{/i}"
mc "{i}Yeah, I just arrived.{/i}"
js "{i}Cool! I'm thinking dinner at my place. I'm home alone for the night.{/i}"
mc "{i}Sounds great.{/i}"
js "{i}See you at 6 p.m.!{/i}"

$ chat_josy_history_is_them.append(True)
$ chat_josy_history.append("Hey, are you in town?")
$ chat_josy_history_is_them.append(False)
$ chat_josy_history.append("Yeah, I just arrived.")
$ chat_josy_history_is_them.append(True)
$ chat_josy_history.append("Cool! I'm thinking dinner at my place. I'm home alone for the night.")
$ chat_josy_history_is_them.append(False)
$ chat_josy_history.append("Sounds great.")
$ chat_josy_history_is_them.append(True)
$ chat_josy_history.append("See you at 6 p.m.!")

$ bios_history_josy +="Josy quit her job at the minimart.\n\n"
$ bios_name_josy = True
$ chat_new_bios = True

scene ep2_store15 with dissolve
mc "(Ok, what can I get her for our date?)"
mc "(Yes, date. This is a date.)"
mc "(I don't care if we really didn't say that.)"
if money == 0:
    show screen moneymsg
    mc "(Fuck me...)"
    mc "(I don't have a single dollar on me...)"
    mc "(Let's just hope she isn't expecting a gift...)"
    hide screen moneymsg
elif True:
    if ep1_josy_prefer_flowers:
        mc "(If I recall correctly, she said she preferred flowers.)"
    elif True:
        mc "(Flowers or chocolate...? That's the question.)"
    show screen moneymsg
    menu:
        "Buy chocolate ({color=#36ca2b}${/color})" if True:
            $ ep2_boughtFlowers = False
            $ ep2_boughtChocolate = True
            $ mny(-1)
            $ dk(-1)
            mc "(Chocolate it is...)"
            hide screen moneymsg
        "Buy flowers ({color=#36ca2b}${/color})" if True:
            $ ep2_boughtFlowers = True
            $ ep2_boughtChocolate = False
            $ mny(-1)
            $ dk(-1)
            mc "(Flowers it is...)"
            hide screen moneymsg
            mc "(I better make it something simple though...)"
            mc "(That's all I can afford.)"
        "Don't buy her anything" if True:
            $ ep2_boughtFlowers = False
            $ ep2_boughtChocolate = False
            mc "(I'm running a bit low on cash.)"
            hide screen moneymsg
            mc "(You know what...? Let's skip the gift.)"
            mc "(That's not what this night is about.)"
stop music fadeout 3
scene ep2_store18 with dissolve
uk "*{i}Sniffles{/i}*"
mc "(Huh? Is someone crying?)"
play music "music/ep1/they_say.mp3"
scene ep2_store19 with dissolve
mc "Steve?"
scene ep2_store20 with dissolve
st "What!?"
st "G-go away! You...you fucker!"
st "Leave me...*{i}sobs{i}*...alone..."
show screen majorChoiceScale
scene ep2_store19 with dissolve
menu:
    "Talk to him" if True:
        $ ep2_comfortedSteve = True
        $ addDPenalty()
        $ renpy.pause(1)
        mc "Hey...are you ok?"
        hide screen majorChoiceScale
        scene ep2_store22 with dissolve
        st "Why the fuck would you care?"
        scene ep2_store23 with dissolve
        mc "I know you and I don't get along that well..."
        mc "...but I'm not that narrow-minded or evil that I'd enjoy seeing you cry."
        mc "So, what's up?"
        scene ep2_store24 with dissolve
        st "It's my mom and dad..."
        st "They are getting divorced."
        scene ep2_store23 with dissolve
        mc "Man...that sucks."
        scene ep2_store24b with dissolve
        st "My dad is the one who fucking sucks."
        st "He fucking cheated on my mom..."
        st "...and now he's leaving her for his new whore."
        scene ep2_store23 with dissolve
        mc "And what about you?"
        scene ep2_store24 with dissolve
        st "I'm gonna stay with my mom..."
        st "...so I just told my dad I'm quitting."
        scene ep2_store23 with dissolve
        mc "Wow, that's a really tough choice."
        scene ep2_store30 with dissolve
        st "It's the right thing to do."
        scene ep2_store23 with dissolve
        mc "You staying there by your mom's side...?"
        mc "Yeah. That's what I would have done, too."
        scene ep2_store30 with dissolve
        st "I just don't know what to do now."
        scene ep2_store23 with dissolve
        mc "Sure, you do."
        mc "You find yourself another job and be a better person than your dad is."
        mc "Make your mom proud, Steve."
        mc "You can do it."
        scene ep2_store34 with dissolve
        $ renpy.pause()
        scene ep2_store35 with dissolve
        st "Hey..."
        st "Thanks."
        scene ep2_store35b with dissolve
        stop music fadeout 3
        mc "Stay strong, Steve."
        $ bios_history_mc +="I comforted Steve when he cried.\n\n"
        $ bios_name_mc = True
        $ bios_history_steve +="I comforted Steve when he cried.\n\n"
        $ bios_name_steve = True
        $ chat_new_bios = True
    "Walk away" if True:
        $ ep2_comfortedSteve = False
        $ addCPenalty()
        $ renpy.pause(1)
        mc "Whatever."
        stop music fadeout 3
        mc "I'll leave you to sit there and cry in your corner."
        $ bios_history_mc +="I didn't comfort Steve when he cried.\n\n"
        $ bios_history_steve +="I didn't comfort Steve when he cried.\n\n"
        $ bios_name_steve = True
        $ bios_name_mc = True
        $ chat_new_bios = True
        hide screen majorChoiceScale

label ep2_sat_home_label:
play music "music/ep2/simple_ballad.mp3"
scene ep2_sat_home with wipeleft
mc "Hey, dad! It's me!"
dad "Hey, me! It's dad!"
scene ep2_sat_home2 with dissolve
mc "...really?"
dad "You'll understand that one better when you get older."
dad "How was the first week?"
dad "Come, tell me all about it!"
scene ep2_sat_home5 with fade
dad "So what does maggot brother mean?"
scene ep2_sat_home6 with dissolve
mc "It's just a stupid term for my friend Derek who's also pledging the DIKs."
scene ep2_sat_home7 with dissolve
dad "The dicks, the hot ones, the AA..."
dad "Where do you kids get these ideas from?"
scene ep2_sat_home6 with dissolve
mc "It's a Greek thing."
scene ep2_sat_home7 with dissolve
dad "A lot of toga and meze, then."
scene ep2_sat_home6 with dissolve
mc "...sure."
mc "Well, it's kinda fun, but also a bit mean..."
mc "Overall, they say it's a great way of finding friends and contacts for the future."
scene ep2_sat_home5 with dissolve
dad "I'm just happy you're happy, son."
dad "Remind me, you aren't staying for dinner tonight?"
scene ep2_sat_home6 with dissolve
mc "No, Josy's making me dinner."
scene ep2_sat_home5 with dissolve
dad "Hehe. A homemade dinner date at your age?"
dad "I think this Josy is quite smitten with you."
scene ep2_sat_home6 with dissolve
mc "I'm gonna find out tonight..."
scene ep2_sat_home8 with dissolve
dad "Did you bring a condom?"
scene ep2_sat_home16 with dissolve
if dtype > 0:
    mc "Dad, what the fuck is it with you and condoms?"
elif True:
    mc "Why do you keep talking about condoms?"
scene ep2_sat_home8 with dissolve
dad "STDs aren't fun to have, son."
dad "And unprotected sex is like a candy shop full of them."
dad "You try to resist, but once you're done in there, you'll be leaving with more than you came for."
scene ep2_sat_home16 with dissolve
mc "..."
mc "What!?"
scene ep2_sat_home8 with dissolve
dad "I'm just saying."
scene ep2_sat_home6 with dissolve
mc "Look, I gotta get ready for my date."
stop music fadeout 3
mc "Thanks for the chat, dad."
scene ep2_sat_home5 with dissolve
dad "Anytime."

label ep2_josy_date_label:
stop music fadeout 3
play music "music/ep2/journey_of_hope.mp3"
scene ep2_josy_date with wiperight
js "Come in!"
js "Fuck! Sorry, I'm in the kitchen!"
js "Shit!"
js "It's not going that well."
mc "Oh, ok. Do you need any help?"
js "No, just a sec..."
scene ep2_josy_date1 with dissolve
js "I wish I were better at cooking...I almost set the kitchen on fire just now."
mc "Are you ok?"
js "Don't worry about it."
scene ep2_josy_date2 with dissolve
js "Hey!"
$ guideSuggestedPage = 61
mc "Hi, great to see you."
menu:
    "Hug" if True:
        scene ep2_josy_date4 with dissolve
        js "You too!"
    "Kiss on cheek" if True:
        $ bios_history_josy +="I kissed Josy on her cheek. She liked it.\n\n"
        $ bios_name_josy = True
        $ chat_new_bios = True
        scene ep2_josy_date5 with dissolve
        "*{i}Smack{/i}*"
        $ RPjosy += 1
        scene ep2_josy_date6 with dissolve
        js "You too..."

if ep2_boughtFlowers:
    scene ep2_josy_date6b with dissolve
    mc "I got you this as a thank you for making dinner."
    mc "It's not much..."
    scene ep2_josy_date6c with dissolve
    if ep1_josy_prefer_flowers:
        $ RPjosy += 2
        js "You remembered..."
        js "It's beautiful. I just love it."
        $ bios_history_josy +="I gave Josy a rose. She loved that I remembered what she wrote in her text message.\n\n"
        $ bios_name_josy = True
        $ chat_new_bios = True
    elif True:
        $ RPjosy += 1
        js "It's beautiful. I just love it."
        $ bios_history_josy +="I gave Josy a rose. She loved it.\n\n"
        $ bios_name_josy = True
        $ chat_new_bios = True
elif ep2_boughtChocolate:
    $ bios_history_josy +="I gave Josy a box of chocolates. She liked it.\n\n"
    $ bios_name_josy = True
    $ chat_new_bios = True
    scene ep2_josy_date6d with dissolve
    mc "I got you this as a thank you for making dinner."
    mc "It's not much..."
    $ RPjosy += 1
    scene ep2_josy_date6e with dissolve
    if ep1_josy_prefer_flowers:
        js "Haha, chocolates, huh?"
        js "You so forgot what I wrote in that text, didn't you?"
        js "But thanks, I like chocolate, too."
    elif True:
        js "Thank you so much. I like chocolate!"
scene ep2_josy_date7 with dissolve
if ep1_josy_prefer_beer:
    js "I got you some beers for dinner."
    scene ep2_josy_date8 with dissolve
    mc "That's so sweet of you. Thank you!"
elif ep1_josy_prefer_wine:
    js "I got us some wine for dinner."
    scene ep2_josy_date8 with dissolve
    mc "That's so sweet of you. Thank you!"
    scene ep2_josy_date9 with dissolve
    js "I gotta admit I was surprised that you also like wine."
    js "Most people our age would go for beer or other drinks."
    scene ep2_josy_date8 with dissolve
    mc "Yeah, I don't know why I like it."
    mc "My dad let me taste some red wine once and I just loved it."
elif True:
    js "Do you want something to drink? I have beer or wine..."
    scene ep2_josy_date8 with dissolve
    menu:
        "Beer" if True:
            mc "Sure, I could go for some beer."
        "Wine" if True:
            mc "Sure, I'm not saying no to wine."
            scene ep2_josy_date9 with dissolve
            js "You're just like me, then. I love wine."
            js "It's not common for our age."
            scene ep2_josy_date8 with dissolve
            mc "Well, if it tastes good, why shouldn't you drink it?"
scene ep2_josy_date7 with dissolve
js "Come, let's eat before it gets cold."
scene ep2_josy_date12 with fade
js "Ok, dig in..."
scene ep2_josy_date13 with dissolve
js "I really hope you can eat this..."
js "I tried following the recipe..."
js "...but it doesn't look like the picture at all."

scene ep2_josy_date14 with dissolve
mc "(She put a lot of effort into this...it's such a shame that it's overcooked.)"
menu:
    "Compliment food" if True:
        mc "I really like it!"
        scene ep2_josy_date18 with dissolve
        js "Come on, stop it."
        js "It tastes like shit..."
        scene ep2_josy_date16 with dissolve
        js "Hahaha!"
        scene ep2_josy_date17 with dissolve
        mc "I still like it."
    "Compliment effort" if True:
        $ bios_history_josy +="I was honest about her cooking and complimented her effort. She liked it.\n\n"
        $ bios_name_josy = True
        $ chat_new_bios = True
        mc "I can really tell that you put a lot of effort into this, Josy."
        mc "That's what matters."
        $ RPjosy+=1
        scene ep2_josy_date18 with dissolve
        js "I really did... Thank you for noticing."
        scene ep2_josy_date17 with dissolve

if dtype > 0:
    mc "Your home is really sweet."
elif True:
    mc "I love your home."
scene ep2_josy_date20 with dissolve
js "It's not so much my home as it is dad's..."
js "...and Monica's."
scene ep2_josy_date21 with dissolve
mc "Monica is your stepmom, right?"
scene ep2_josy_date20b with dissolve
js "Right..."
js "I don't like her..."
scene ep2_josy_date21 with dissolve
mc "Why is that?"
scene ep2_josy_date20b with dissolve
js "She's the reason why my mom and dad aren't together..."
js "How could I like that?"

label ep2_josy_date_loop_label:
scene ep2_josy_date21c2 with dissolve
if ep2_asked_mom and ep2_asked_dad:
    jump ep2_josy_date_loop_label2
menu:
    "Ask about mom" if not ep2_asked_mom:
        $ ep2_asked_mom = True
        mc "And what about your mom?"
        mc "Where is she?"
        scene ep2_josy_date26 with dissolve
        js "She lives a couple of hours by car away from here."
        scene ep2_josy_date21b with dissolve
        mc "She lives alone?"
        scene ep2_josy_date28 with dissolve
        js "No, she has a new guy..."
        js "I don't like him either."
        jump ep2_josy_date_loop_label
    "Ask about dad" if not ep2_asked_dad:
        $ ep2_asked_dad = True
        mc "What about your dad? He likes Monica, right?"
        scene ep2_josy_date26 with dissolve
        js "Yeah, of course he likes her."
        js "He got tired of mom's nagging and met Monica on a business trip."
        scene ep2_josy_date28 with dissolve
        js "He says that nothing happened between them while he still was with mom."
        js "But that's just a big lie."
        js "I know he wasn't faithful to mom."
        scene ep2_josy_date26 with dissolve
        js "But he ended up with someone who makes him happy..."
        js "...so I guess that makes it ok."
        scene ep2_josy_date32 with dissolve
        js "Is that weird?"
        scene ep2_josy_date21b with dissolve
        menu:
            "Yes" if True:
                mc "Yeah, it's kinda weird..."
                mc "Isn't it cheating?"
                scene ep2_josy_date28 with dissolve
                js "Either that or a way out from being unhappy."
                js "At least that's how I see it."
            "No" if True:
                mc "I wouldn't want that to happen to me..."
                mc "...but no, it's not weird."
                mc "It seems to be really common these days."
                scene ep2_josy_date26 with dissolve
                js "Yeah, I don't really know what to think."
        jump ep2_josy_date_loop_label

label ep2_josy_date_loop_label2:
scene ep2_josy_date21 with dissolve
mc "So, you never stay with your mom?"
scene ep2_josy_date26 with dissolve
js "Not really. I've always been daddy's girl."
js "Even though he hurt my mom...you know...emotionally..."
scene ep2_josy_date28 with dissolve
js "...he's my dad."
js "I love him so much..."
js "I'd pick him over my mom any day."
scene ep2_josy_date20b with dissolve
js "But I'm not sure if he would pick me over Monica and my stupid stepbrother..."
scene ep2_josy_date21 with dissolve
mc "Ah, yeah. That's right, you have a stepbrother."
mc "The one who cheated his way through high school, right?"
scene ep2_josy_date40 with dissolve
js "Yes, that's right."
js "Maybe you'll meet him if you'd ever pledge the DIKs."
mc "(What!?)"
js "His name is Tommy."
mc "(Oh no...)"
scene ep2_josy_date32 with dissolve
js "What's wrong?"
scene ep2_josy_date21b with dissolve
mc "Tommy's your stepbrother!?"
scene ep2_josy_date32 with dissolve
js "You've met him?"
scene ep2_josy_date21b with dissolve
mc "He's my father."
scene ep2_josy_date32 with dissolve
js "Your what?"
scene ep2_josy_date40e with dissolve
mc "I'm a DIK pledge! Tommy's my father and I'm his maggot son."
scene ep2_josy_date40 with dissolve
js "No freaking way! For real?"
scene ep2_josy_date21b with dissolve
mc "He is so fucking evil!"
scene ep2_josy_date40b with dissolve
js "I know! I hate him!"
scene ep2_josy_date40c with dissolve
js "Hahaha! I can't believe this!"
mc "Right!?"
scene ep2_josy_date40d with dissolve
js "So, now you get to live through the torture that is Tommy; the same that I have been living with for years?"
scene ep2_josy_date21b with dissolve
mc "Not once, but twice he has forced me outside nude or almost nude."
scene ep2_josy_date40d with dissolve
js "Haha! I can't relate to that..."
js "...but this one time he stole my nail polish because he thought he could get high from it."
scene ep2_josy_date21c2 with dissolve
mc "I wonder what he would say if he knew I was sitting here across from you right now, eating dinner..."
scene ep2_josy_date40e with dissolve
js "Oh my God, he would {b}so{/b} beat you up."
js "He has the shortest fuse ever!"
scene ep2_josy_date40f with dissolve
js "He probably gets that from Monica."
scene ep2_josy_date40d with dissolve
js "You're really going to be a DIK?"
scene ep2_josy_date21 with dissolve
mc "Yeah, I think I am..."
mc "If me and my maggot brother pass the tests."
if dtype > 0:
    scene ep2_josy_date40 with dissolve
    js "I can totally see you being a DIK."
    scene ep2_josy_date21b with dissolve
    mc "Really?"
    scene ep2_josy_date40 with dissolve
    js "Yeah, you have the right attitude for it, I think."
elif True:
    scene ep2_josy_date40 with dissolve
    js "I would never have imagined you joining the DIKs."
    scene ep2_josy_date21b with dissolve
    mc "Why is that?"
    scene ep2_josy_date40 with dissolve
    js "You're too sweet for them."

scene ep2_josy_date62 with Fade(1.5,1,0.5)
js "Are you full?"
scene ep2_josy_date62b with dissolve
mc "I am. Thank you for the dinner."
scene ep2_josy_date64 with dissolve
stop music fadeout 3
js "Come, let's sit on the couch."
$ bios_history_josy +="Josy is Tommy's stepsister! I can't believe this!\n\n"
$ bios_name_josy = True
$ bios_history_tommy +="Josy is Tommy's stepsister! I can't believe this!\n\n"
$ bios_name_tommy = True
$ chat_new_bios = True

scene ep2_josy_sofa0 with dissolve
play music "music/ep1/fresh_air.mp3"
js "I'm guessing you're enjoying college life, huh?"
scene ep2_josy_sofa0b with dissolve
mc "It has both ups and downs."
mc "But yeah...I think I'm going to enjoy it as a whole."
scene ep2_josy_sofa0c with dissolve
js "So, what's happening next week?"
scene ep2_josy_sofa0b with dissolve
mc "You know, a bunch of classes...and something called Hell Week, I think."
scene ep2_josy_sofa0c with dissolve
js "Yeah...good luck with Hell Week."
js "I heard it gets really bad."
js "How are your classes? What do you take?"
scene ep2_josy_sofa0b with dissolve
mc "You know, the mandatory Gen. Ed. classes."
mc "I'm taking Math, English...and a Gender Studies class."
scene ep2_josy_sofa0h with dissolve
js "Gender Studies?"
js "Haha! What on earth made you sign up for that?"
scene ep2_josy_sofa0i with dissolve
mc "Hey, what if I happen to like that kind of class?"
scene ep2_josy_sofa0j with dissolve
js "Do you?"
scene ep2_josy_sofa0k with dissolve
mc "No..."
scene ep2_josy_sofa0l with dissolve
js "Hahaha!"
mc "Maybe I would have liked it..."
scene ep2_josy_sofa0m with dissolve
mc "But it seems to be a class where we're supposed to discuss things..."
mc "...but this week I didn't even get the chance to talk."
scene ep2_josy_sofa0n with dissolve
js "I would love to watch you take that class."
mc "Maybe you will?"
scene ep2_josy_sofa0o with dissolve
mc "Did you hear anything from B&R?"
scene ep2_josy_sofa0p with dissolve
js "If I did, I would be standing outside of your dorm right now, jumping for joy."
js "It's not gonna happen, [name]."
js "I've given up."
scene ep2_josy_sofa0o with dissolve
mc "On that note..."
mc "I went to the minimart."
js "..."
mc "Tina told me you quit."
scene ep2_josy_sofa2 with dissolve
js "..."
mc "You're really doing it? You're moving away from here?"
scene ep2_josy_sofa3 with dissolve
mc "Josy?"
scene ep2_josy_sofa4 with dissolve
js "*{i}Sobs{/i}*"
mc "Hey... Was it something I said?"
scene ep2_josy_sofa6 with dissolve
js "These last few months have been hell, [name]."
js "I've been so lonely and scared."
scene ep2_josy_sofa7 with dissolve
js "And you know what I did?"
js "I told myself that I would get accepted to B&R and that everything would be great again."
js "And I actually believed it. I almost took it for granted."
js "And now..."
scene ep2_josy_sofa9 with dissolve
js "I'm not going to get accepted. It's like the biggest blow to my psyche ever."
js "I get anxiety attacks when I think about it."
scene ep2_josy_sofa10 with dissolve
js "I can't breathe when I think of being stuck in this hole, living with dad and Monica for another year!"
js "I just have to get away from here and do something new and start all over."
scene ep2_josy_sofa11 with dissolve
mc "I had no idea that you've been this upset."
mc "You really fooled me on that one."
scene ep2_josy_sofa12 with dissolve
js "Meeting you made me feel different about this..."
js "It was exciting... I felt that spark that's been missing in my life for quite some time now."
scene ep2_josy_sofa13 with dissolve
js "Relationships when you can't be with each other every week suck, by the way..."
js "Never do that with anyone."
scene ep2_josy_sofa14 with dissolve
mc "You miss feeling loved?"
scene ep2_josy_sofa13 with dissolve
js "More than anything..."
js "And now...I think of just cutting all ties and moving away."
scene ep2_josy_sofa16 with dissolve
js "*{i}Sniffles{/i}* Great solution, huh? Hah."
scene ep2_josy_sofa17 with dissolve
mc "I think you just want that change in your life so badly that you think that running away will solve all those problems."
scene ep2_josy_sofa18 with dissolve
js "It's just that staying here does nothing for me."
js "I would have to put up with Steve every day and have no friends to hang out with, because they all moved away."
js "Growing up sucks!"
scene ep2_josy_sofa17 with dissolve
mc "I know what you mean..."
mc "You know... I almost quit college this week."
scene ep2_josy_sofa21 with dissolve
js "Say what?"
scene ep2_josy_sofa22 with dissolve
mc "I didn't go through with it, but I was almost on my way back home."
scene ep2_josy_sofa21 with dissolve
js "Why was that?"
scene ep2_josy_sofa22 with dissolve
mc "The change was too big and fast for me. And you might feel lonely in this town..."
mc "But until recently, I've felt lonely every day this week, over there."
mc "Loneliness sucks."
scene ep2_josy_sofa23 with dissolve
$ renpy.pause()
scene ep2_josy_sofa24 with dissolve
js "I'm so happy you wanted to come over this weekend."
js "It's been on my mind every day since you called..."
scene ep2_josy_sofa25 with dissolve
js "Well... That feeling split with guilt..."
js "Because of..."
js "You know..."
scene ep2_josy_sofa27 with dissolve
mc "You don't seem happy in that relationship, Josy."
mc "I know it's not my thing to say...but you're attracted to me and I'm attracted to you."
mc "I don't want to be the other guy, but look at us right now."
mc "Don't you want this?"
mc "Or am I just here because you're lonely?"
scene ep2_josy_sofa25 with dissolve
js "No...you're not here just because I'm lonely."
js "You're right...I want this, but..."
js "...it's complicated..."
js "...and I feel like I shouldn't."
scene ep2_josy_sofa30b with dissolve
mc "Right..."
scene ep2_josy_sofa31 with dissolve
js "It's getting pretty late."
scene ep2_josy_sofa31b with dissolve
mc "Yeah, I should probably be-"
scene ep2_josy_sofa31 with dissolve
js "Wanna stay the night?"
scene ep2_josy_sofa31b with dissolve
menu:
    "Accept" if True:
        $ ep2_fuckedJosy = True
        stop music fadeout 5
        jump ep2_josy_lewd_label
    "Not like this" if True:
        $ ep2_fuckedJosy = False
        $ bios_history_josy +="I didn't stay the night with Josy. It didn't feel right to do so.\n\n"
        $ bios_name_josy = True
        $ chat_new_bios = True
        mc "I really want to...but no..."
        scene ep2_josy_sofa33 with dissolve
        mc "...it wouldn't be good if I did."
        mc "You need to think things through, before we do something you will regret."
        mc "This is not the way I want to do this."
        scene ep2_josy_sofa34 with dissolve
        js "You're right..."
        scene ep2_josy_sofa33 with dissolve
        if dtype > 0:
            mc "Thank you for dinner."
        elif True:
            mc "Thank you for the lovely night."
        scene ep2_josy_sofa34 with dissolve
        stop music fadeout 5
        js "Talk to you soon?"
        scene ep2_josy_sofa33 with dissolve
        mc "Whenever you want to. I'm here for you."
        jump ep2_josy_after_date2_label
label ep2_josy_lewd_label:
hide screen phone_screen
if _in_replay:
    hide screen phone_screen
    if persistent.name == None:
        $ name = "MC"
    elif True:
        $ name = persistent.name
    if persistent.mc_josy == None:
        $ mc_josy = name
    elif True:
        $ mc_josy = persistent.mc_josy
    if persistent.josy == None:
        $ josy = "Josy"
    elif True:
        $ josy = persistent.josy
scene ep2_josy_lewd with Fade(1.5,1,0.5)
mc "(My palms are all sweaty...)"
mc "(I'm really going to sleep with her in this bed?)"
play music "music/ep1/windswept.mp3"
scene ep2_josy_lewd1 with dissolve
js "Hi."
mc "Hi..."
scene ep2_josy_lewd1a with dissolve
$ renpy.pause()
scene ep2_josy_lewd1b with dissolve
$ renpy.pause()
scene ep2_josy_lewd2 with dissolve
menu:
    "Compliment her" if True:
        scene ep2_josy_lewd2b with dissolve
        if dtype < 1:
            $ RPjosy += 1
            mc "You're beautiful in that..."
            js "Do you mean that?"
            mc "Yeah."
            scene ep2_josy_lewd5 with dissolve
            js "Thanks..."
        elif True:
            mc "Wow, you're super-hot."
            scene ep2_josy_lewd5 with dissolve
            js "Thanks..."
    "Don't push your luck" if True:
        $ renpy.pause(0.5)
scene ep2_josy_lewd6 with dissolve
mc "Is this really your room?"
scene ep2_josy_lewd7 with dissolve
js "No...it's my dad's and Monica's room."
scene ep2_josy_lewd6 with dissolve
mc "Oh..."
scene ep2_josy_lewd7 with dissolve
js "My bed is too small for both of us."
scene ep2_josy_lewd6 with dissolve
mc "(What does that mean?)"
mc "(Didn't she want to lie close to me?)"
scene ep2_josy_lewd7 with dissolve
js "Good night..."
mc "...good night."
scene ep2_josy_lewd13 with dissolve
mc "(But if so...why would she sleep in this bed, too?)"
mc "(Or even ask me to stay the night...?)"
mc "(...I think she's scared to make that first move.)"
mc "(Her boyfriend obviously doesn't know what he's got.)"
scene ep2_josy_lewd12 with dissolve
mc "(I know she would be cheating...but, fuck it!)"
mc "(It's just like she described it with her dad and Monica...)"
mc "(If it leads to happiness...why wouldn't it be ok?)"
mc "(I'm going for it.)"
scene ep2_bed_josy_spoon with dissolve
mc "(I knew it...)"
mc "(She's not resisting, at all.)"
js "(Oh God...it's happening...it's really happening.)"
js "(Human contact...how I've missed this...)"
js "*{i}Breathes louder{/i}*"
scene ep2_bed_josy_spoon1 with dissolve
mc "(She is so soft and smooth...)"
mc "(I could smell her hair for days...)"
js "Mmm..."
js "(Is he...?)"
js "(He is!)"
js "(He's moving his hand further down...)"
scene ep2_bed_josy_spoon2 with dissolve
mc "(This must be a dream...)"
mc "(I'm touching her thigh and her ass is softly pressed up against my dick...)"
js "*{i}Moans softly{/i}*"
mc "(This is really going to happen...)"
scene ep2_bed_josy_spoon3 with dissolve
mc "(My heart is racing...she must be feeling that.)"
mc "(Ok...I've taken the first step now...)"
scene ep2_bed_josy_spoon4 with dissolve
mc "(Wow...what a view...)"
mc "(Her breasts look so sexy in that bra...)"
scene ep2_bed_josy_spoon5 with dissolve
mc "(She's touching herself...)"
mc "(There's no doubt now. She wants this.)"
mc "(I'll start gently...)"

scene anim_josy_spoon1_ep2 with dissolve:
    size (config.screen_width, config.screen_height)
js "*{i}Moans softly{/i}*"
pause
scene ep2_josy_spoon_remove with dissolve
js "(Wow... I can't even breathe normally...)"
js "(Yes... Don't stop...)"
scene anim_josy_spoon2_ep2 with dissolve:
    size (config.screen_width, config.screen_height)
mc "(She has the softest breasts I've ever felt...)"
mc "(I can feel her hard nipple against my palm through her tiny bra.)"
pause
scene anim_josy_spoon3_ep2 with dissolve:
    size (config.screen_width, config.screen_height)
js "*{i}Moans softly{/i}*"
js "(I can't help myself any longer...)"
js "(I'm getting so wet...)"
scene ep2_josy_spoon_remove with dissolve
js "*{i}Whispers{/i}* [mc_josy]..."
js "*{i}Whispers{/i}* Please, touch me down there..."
scene anim_josy_spoon4_ep2 with dissolve:
    size (config.screen_width, config.screen_height)
mc "(She's so wet...her panties are totally soaked...)"
mc "(I'm so fucking hard...and she's rubbing her soft hand against the tip of my cock just right.)"
pause
scene ep2_josy_spoon_remove with dissolve
js "*{i}Whispers{/i}* Let me remove my panties for you..."
scene anim_josy_spoon5_ep2 with dissolve:
    size (config.screen_width, config.screen_height)
js "(Oh my God! The way he caresses my pussy...)"
js "(Where did he learn that gentle touch? It's almost better than...)"
js "(No...just enjoy this now...)"
js "(He's teasing me so much right now...)"
js "(I can't take this anymore... I just have to...)"
pause
scene anim_josy_kiss_ep2 with dissolve:
    size (config.screen_width, config.screen_height)
mc "(She just removed my underwear...)"
mc "(She really wants me to fuck her tonight...)"
mc "(I'm going to fuck Josy...)"
mc "(This is a dream...)"
pause
scene anim_josy_kiss3_ep2 with dissolve:
    size (config.screen_width, config.screen_height)
mc "(Shit... I'm actually sliding my cock against her wet pussy...)"
mc "(That wet sound it makes with each thrust just makes me harder...)"
pause
scene anim_josy_kiss2_ep2 with dissolve:
    size (config.screen_width, config.screen_height)
js "(I haven't been this horny in forever.)"
js "(His cock grinding against my clit like that...)"
js "(God, I'm so sensitive...)"
pause
js "(I gotta take control before I cum all over him...)"

scene anim_josy_kiss4_ep2 with dissolve:
    size (config.screen_width, config.screen_height)
js "(Mmm... Much better...)"
js "(It still feels great but now I can control the pace more...)"
pause
js "(...no!)"
js "(I'm still on the edge of cumming...)"
scene ep2_josy_spoon_cover with dissolve
js "(This is so embarrassing! I can't cum this early...)"

scene ep2_josy_spoon_cover2 with dissolve
js "[mc_josy]...?"
mc "Yeah?"
js "Let's just stop for a second..."
mc "Is something wrong?"
scene ep2_josy_spoon_cover3 with dissolve
js "Shh..."
js "Let me take care of you for a while..."
scene ep2_josy_spoon_cover4 with dissolve
mc "Huh? What are you do-"
scene ep2_josy_spoon_cover5 with dissolve
mc "Oh God! Yes!"
scene ep2_josy_spoon_cover6 with dissolve
js "*{i}Lick lick suck suck{/i}*"
mc "(She's really licking my cock...)"
scene ep2_josy_spoon_cover7 with dissolve
mc "(I just have to watch her do it...)"
scene ep2_josy_spoon_cover8 with dissolve
mc "(Fuck me...)"
scene anim_josy_bj_ep2 with dissolve:
    size (config.screen_width, config.screen_height)
mc "(She's killing me...)"
mc "(Looking me in the eyes like that while giving me a handjob and licking my cock...)"
mc "(This is just too much for me to take in...)"
pause
js "Do you like it, [mc_josy]?"
mc "It feels amazing, Josy..."
js "Do you want me to use my mouth more?"
if dtype > 0:
    mc "Yeah...suck my cock."
elif True:
    mc "Yeah, if you want to."
scene anim_josy_bj2_ep2 with dissolve:
    size (config.screen_width, config.screen_height)
mc "(Her mouth is so warm and tight...)"
mc "(She's moving her tongue left and right as she's bobbing her head up and down...)"
js "(He has such a fucking big dick!)"
js "(I just can't get it down further...)"
js "(I'm gonna start gagging on it if I push more...)"
pause
scene ep2_josy_spoon_cover3 with dissolve
js "Did you like it?"
scene ep2_josy_spoon_cover2 with dissolve
mc "I loved it..."
js "I want to feel you inside of me, [mc_josy]."
js "Slide into me...slowly..."
scene bg anim_josy_on_top_slide_ep2 movie with dissolve
js "Oh my GOD!!!"
js "You're huge!!!"
mc "You're so tight around my cock..."
js "Oh, [mc_josy]..."
scene anim_josy_on_top_ep2 with dissolve:
    size (config.screen_width, config.screen_height)
js "Fuck me..."
js "Fuck me as much as you want and then fill me up!"
pause
scene anim_josy_on_top2_ep2 with dissolve:
    size (config.screen_width, config.screen_height)
js "YES! YES!!!"
js "FUCK ME!"
scene anim_josy_on_top2b_ep2 with dissolve:
    size (config.screen_width, config.screen_height)
js "HARDER!!! HARDER!!!"
js "OH GOD!"
pause
$ renpy.end_replay()
$ persistent.ep2_lewd_josy = True
$ calcScenes()
label ep2_josy_date3_label:
stop music
play sound "sound_effects/key_jiggle.mp3"
scene ep2_josy_date_parents
"*{i}Keys jiggle from the front door{/i}*"
play music "music/ep1/credits.mp3"
scene ep2_josy_date_parents1 with dissolve
js "Oh fuck! My dad and Monica are back already!"
mc "What!? You said they were gone for tonight!"
scene ep2_josy_date_parents2 with dissolve
js "Fuck this is bad! So bad!"
js "Hide!!!"
scene ep2_josy_date_parents3 with dissolve
play sound "sound_effects/door_lock.mp3"
"*{i}Click{/i}*"
mon "Josy? Are you home?"
scene ep2_josy_date_parents4 with dissolve
js "Just a minute, Monica!"
play sound "sound_effects/door_knob.mp3"
scene ep2_josy_date_parents5 with hpunch
pt "Sweetie? Why have you locked yourself in our bedroom?"
scene ep2_josy_date_parents6 with dissolve
js "*{i}Whisper{/i}* What are you doing!?"
mc "*{i}Whisper{/i}* I'm panicking!"
scene ep2_josy_date_parents7 with dissolve
js "*{i}Whisper{/i}* Exit through the window!"
scene ep2_josy_date_parents8 with dissolve
js "*{i}Whisper{/i}* Here! Your clothes!!"
scene ep2_josy_date_parents8b with dissolve
stop music fadeout 5
play sound "sound_effects/door_lock.mp3"
"*{i}Click{/i}*"
js "(FUCK!)"
mon "Josy! What the hell is this!?"
$ bios_history_josy +="I fucked Josy, but didn't get to finish as her parents came back earlier than expected. I hope she didn't get into trouble because of this.\n\n"
$ bios_name_josy = True
$ chat_new_bios = True
show screen phone_screen

label ep2_josy_after_date_label:
play music "music/ep1/your_smile.mp3"
scene ep2_after_josy_1 with wiperight
mc "(Nope...she hasn't answered yet...)"
mc "(Fuck...)"
mc "(She must have gotten into trouble because of me...)"
mc "(We really did {i}it{/i}...I mean...we kinda did...)"
mc "(It still counts though.)"
scene ep2_after_josy_2 with dissolve
mc "(I just made things harder for myself...)"
mc "(If I had a hard time letting go before tonight...)"
mc "(...how will it be after this?)"
mc "(Now that she's shown me that she really wants it...)"
mc "(...it's not just a crush anymore.)"
mc "(We just took the next step.)"
scene ep2_after_josy_3 with dissolve
mc "(I need to figure out a way to keep her in my life.)"
mc "(But what about Maya...?)"
if ep2_danceSage:
    mc "(...and Sage.)"
mc "(I'm a fucking mess...)"
jump ep1_sleep_after_josy_date
label ep2_josy_after_date2_label:
    play music "music/ep1/your_smile.mp3"
scene ep2_after_josy_2 with wiperight
mc "(I did the right thing...)"
mc "(...right?)"
mc "(What kinda guy would I be if I stayed the night?)"
mc "(Josy is right...)"
mc "(Growing up really sucks.)"
mc "(I have no fucking clue what I feel right now...)"
mc "(I showed her what I felt and she did too...)"
mc "(It's not just a crush anymore...)"
mc "(...is it?)"
mc "(But what about Maya...?)"
if ep2_danceSage:
    mc "(...and Sage.)"
mc "(My mind is all over tonight...)"

label ep1_sleep_after_josy_date:
mc "(Lying here thinking about it won't solve shit.)"
stop music fadeout 3
mc "(I need to sleep.)"
if preferredmilf == 0:
    label ep2_jade_lewd_label:
    if _in_replay:
        $ currentEpisode = 2
        $ preferredmilf = 0
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
    hide screen phone_screen
    play music "music/ep1/slow_day_blues.mp3"
    scene ep2_jade_dream1 with Fade(1.5,1,0.5)
    ja "I heard someone had a bad night..."
    scene ep2_jade_dream2 with dissolve
    mc "[jade]... Yes, it wasn't the ending to it that I had hoped for."
    scene ep2_jade_dream1 with dissolve
    ja "Are you sad that you didn't get to cum, tonight?"
    ja "Because [jade] can fix that for you..."
    ja "It's just you and me, up here."
    scene ep2_jade_dream3 with dissolve
    ja "...and tonight I'm going to make your dreams come true."
    ja "Let me start by worshiping that big cock of yours."

    scene anim_jade_blowjob_ep2 with dissolve:
        size (config.screen_width, config.screen_height)
    ja "*{i}Mmphf{i}* You taste so...good..."
    pause
    scene anim_jade_blowjob2_ep2 with dissolve:
        size (config.screen_width, config.screen_height)
    mc "Oh, [jade]... Don't stop..."
    ja "*{i}Mmphf{i}*"
    pause
    mc "Go faster..."
    scene anim_jade_blowjob3_ep2 with dissolve:
        size (config.screen_width, config.screen_height)
    pause
    scene ep2_jade_dream3 with dissolve
    ja "You're so big, [mc_jade]..."
    ja "I can't fit all of you inside in this position."
    ja "I have an idea..."
    scene anim_jade_blowjob4_ep2 with dissolve:
        size (config.screen_width, config.screen_height)
    pause
    ja "Oh god, yes!!!"
    ja "Eat my pussy, [mc_jade]!"
    ja "*{i}Mmphf{i}* God...it's...just...too...big!"
    scene anim_jade_blowjob5_ep2 with dissolve:
        size (config.screen_width, config.screen_height)
    pause
    scene ep2_jade_dream4 with dissolve
    ja "Hey...are you licking my asshole?"
    scene ep2_jade_dream6 with dissolve
    ja "Oh wow...mmm...I see what you're trying to do..."

    scene ep2_jade_dream7 with dissolve
    ja "[mc_jade]... You never told me that you wanted to fuck my ass..."
    ja "Didn't I tell you last time that you can do whatever you want with me up here?"
    ja "Just come here and take what you really want..."
    scene anim_jade_anal6_ep2 with dissolve:
        size (config.screen_width, config.screen_height)
    ja "That's it...slow and deep..."
    ja "Just how I like it..."
    pause
    scene anim_jade_anal7_ep2 with dissolve:
        size (config.screen_width, config.screen_height)
    ja "Keep pushing that dick deeper in, [mc_jade]."
    ja "I can take it..."
    pause
    scene anim_jade_anal_ep2 with dissolve:
        size (config.screen_width, config.screen_height)
    pause
    ja "YES! Oh, [mc_jade]!"
    scene anim_jade_anal2_ep2 with dissolve:
        size (config.screen_width, config.screen_height)
    ja "Oh God! You're so deep inside me!"
    pause
    scene anim_jade_anal4_ep2 with dissolve:
        size (config.screen_width, config.screen_height)
    pause
    ja "Do you like how my asshole feels wrapped around your cock, [mc_jade]?"
    mc "Does it hurt?"
    ja "Nuh-uh... Fuck me harder, if you want to."
    scene anim_jade_anal5_ep2 with dissolve:
        size (config.screen_width, config.screen_height)
    ja "Yes! Just like that!"
    pause
    scene anim_jade_anal3_ep2 with dissolve:
        size (config.screen_width, config.screen_height)
    pause
    $ currentSexLabel = "ep2_jade_lewd2"
    $ lewd_jade_phase = 2
    jump jade_sex_scene_loop
    label ep2_jade_lewd2:
    stop music fadeout 3
    $ persistent.ep2_lewd_jade = True
    $ renpy.end_replay()
    $ calcScenes()
elif True:
    label ep2_cathy_lewd:
    if _in_replay:
        $ currentEpisode = 2
        $ preferredmilf = 1
        if persistent.name == None:
            $ name = "MC"
        elif True:
            $ name = persistent.name
        if persistent.mc_cathy == None:
            $ mc_cathy = name
        elif True:
            $ mc_cathy = persistent.mc_cathy
        if persistent.cathy == None:
            $ cathy = "Cathy"
        elif True:
            $ cathy = persistent.cathy
    hide screen phone_screen
    play music "music/ep1/slow_day_blues.mp3"
    $ currentSexLabel = "ep2_cathy_lewd2"
    $ lewd_cathy_phase = 2
    scene ep2_cathy_scene1 with Fade(1.5,1,0.5)
    mc "*{i}Hmph!{/i}*"
    scene ep2_cathy_scene2 with dissolve
    ca "No! That's not my name!"
    ca "Say my name, [mc_cathy]!"
    scene ep2_cathy_scene1 with dissolve
    mc "*{i}Muffled voice{/i}* [cathy]..."
    scene ep2_cathy_scene2 with dissolve
    ca "Better!"
    scene ep2_cathy_scene3 with dissolve
    ca "So, your date didn't go as planned, huh?"
    ca "Well, boo fucking hoo!"
    ca "Quit your whining and make yourself useful!"
    scene anim_cathy_cunn_ep2 with dissolve:
        size (config.screen_width, config.screen_height)
    mc "*{i}Hmph!{/i}*"
    ca "Yes....eat that pussy!"
    pause
    scene anim_cathy_cunn2_ep2 with dissolve:
        size (config.screen_width, config.screen_height)
    ca "It's my turn to get off..."
    pause
    scene ep2_cathy_scene2 with dissolve
    ca "Try harder, [mc_cathy]!"
    ca "Put your tongue into it!"
    ca "Just wiggling the tip around doesn't do shit for me!"
    scene anim_cathy_cunn3_ep2 with dissolve:
        size (config.screen_width, config.screen_height)
    ca "That's it! Yes!"
    ca "Dig in deep, [mc_cathy]!"
    pause
    scene anim_cathy_cunn4_ep2 with dissolve:
        size (config.screen_width, config.screen_height)
    ca "Oh my God! I'm gonna...cum!"
    pause
    scene ep2_cathy_scene4 with dissolve
    ca "AHHHHH!!!"
    scene ep2_cathy_scene2 with dissolve
    ca "Good boy!"
    ca "What are you looking at!?"
    ca "So, you got me off..."
    ca "You want some kind of reward for that?"
    scene ep2_cathy_scene5 with dissolve
    ca "I'll let you fuck my throat this one time."
    ca "But don't do it like a pussy!"
    ca "Fuck it really hard, or I will bite down on that dick without warning you!"
    scene anim_cathy_bj_ep2 with dissolve:
        size (config.screen_width, config.screen_height)
    pause
    scene anim_cathy_bj2_ep2 with dissolve:
        size (config.screen_width, config.screen_height)
    pause
    scene anim_cathy_bj3_ep2 with dissolve:
        size (config.screen_width, config.screen_height)
    pause
    mc "(Shit!!! She's starting to bite!)"
    mc "(I better pump harder!)"
    scene anim_cathy_bj2_fast_ep2 with dissolve:
        size (config.screen_width, config.screen_height)
    pause
    scene anim_cathy_bj_fast_ep2 with dissolve:
        size (config.screen_width, config.screen_height)
    pause
    scene anim_cathy_bj3_fast_ep2 with dissolve:
        size (config.screen_width, config.screen_height)
    pause

    jump cathy_sex_scene_loop
    label ep2_cathy_lewd2:
    stop music fadeout 3
    $ persistent.ep2_lewd_cathy = True
    $ renpy.end_replay()
    $ calcScenes()

label ep2_sun_back_label:
show screen phone_screen
scene ep2_sun_back1 with Fade(2.5,1,0.5)
play music "music/ep2/by_your_side.mp3"
my "Hey! Welcome home!"
scene ep2_sun_back3 with dissolve
mc "Home? Huh..."
mc "I never thought of it that way."
mc "But I guess you're right, it kinda is my home..."
mc "Well...until you find a new roomie, that is."
scene ep2_sun_back2 with dissolve
my "Haha. All right, smartass."
my "How was your trip?"
scene ep2_sun_back4 with dissolve
mc "It was nice seeing my dad again."
scene ep2_sun_back5 with dissolve
my "And what about your date?"
$ guideSuggestedPage = 62
scene ep2_sun_back4 with dissolve
if not ep2_toldMayaTruthAboutDate:
    $ RPmaya -= 1
    $ bios_history_maya +="Maya heard from Derek that I was going on a date with someone. She didn't like that I hid it from her.\n\n"
    $ bios_name_maya = True
    $ chat_new_bios = True
    mc "My date?"
    mc "..."
    mc "Did Derek tell you about that?"
    scene ep2_sun_back5 with dissolve
    my "I didn't mean to pry...but yeah he did."
    scene ep2_sun_back4 with dissolve
mc "It didn't go as expected."
mc "I'm not sure what will happen now, really."
scene ep2_sun_back7 with dissolve
my "So, this girl...tell me about her."
scene ep2_sun_back4 with dissolve
mc "Why are you interested?"
scene ep2_sun_back7 with dissolve
my "I don't know why..."
my "It's just that it feels a bit awkward...no?"
scene ep2_sun_back9 with dissolve
menu:
    "Yeah, it does" if True:
        mc "Yeah, I guess it is kinda awkward..."
        mc "I've never been in this situation before."
    "Not really" if True:
        mc "Well, not really."
        mc "I'm a single guy, there's nothing wrong with it."
        scene ep2_sun_back7 with dissolve
        my "I didn't say there was anything wrong with it."
        my "Just that it's a bit awkward since...you know..."
        scene ep2_sun_back9 with dissolve
mc "..."
mc "I met her this summer..."
mc "I've had a big crush on her since I first saw her."
mc "And just before I left to go here..."
mc "...we had this moment that said that there was something more between us."
scene ep2_sun_back13 with dissolve
mc "That's what I wanted to find out by coming back home to her."
mc "To see if there was something worth fighting for..."
mc "...or if I should try to forget her and just move on."
scene ep2_sun_back9 with dissolve
mc "And I'm just not sure how to do that."
mc "I've had a girlfriend before..."
scene ep2_sun_back15 with dissolve
my "Yeah, you told me; it ended poorly."
scene ep2_sun_back9 with dissolve
mc "Right."
mc "Even though I've had a girlfriend..."
mc "...I've never experienced love."
mc "So, I'm kind of a rookie with this sort of thing."
scene ep2_sun_back15 with dissolve
my "Love..."
my "...can be painful."
scene ep2_sun_back9 with dissolve
mc "Like when it's not returned?"
scene ep2_sun_back15 with dissolve
my "Yeah, but even when it is, it can hurt like hell."
my "But sometimes that pain..."
my "...is a good kind of pain."
my "Because you realize that you have something to lose and fight for."
scene ep2_sun_back7 with dissolve
my "This girl..."
my "Does she make you hurt?"
scene ep2_sun_back9 with dissolve
mc "..."
play sound "sound_effects/cellphone.mp3"
"*{i}Cellphone rings{/i}*"
scene ep2_sun_back15 with dissolve
my "Such bad timing..."
scene ep2_sun_back24 with dissolve
my "Oh..."
my "I really have to take this."
my "We'll talk later!"
scene ep2_sun_back25 with dissolve
mc "*{i}Sigh{/i}*"
if not ep2_toldMayaTruthAboutDate:
    mc "(I should have told her about the date...)"
    mc "(Derek has some loose lips...)"
    mc "(Maybe it's just because of Maya, though...)"
    mc "(I hope...)"
elif True:
    mc "(I'm glad I told her about the date...)"
    mc "(It's tough bringing something like that up...)"
mc "(Maya is really beginning to open up more to me...)"
mc "(And I really feel like I can do the same to her.)"
play sound "sound_effects/cellphone.mp3"
"*{i}Cellphone rings{/i}*"
scene ep2_sun_back26 with dissolve
mc "(Huh? What does she want?)"
scene ep2_sun_back27 with dissolve
mc "Hey, Sage."
if ep2_kissedSage:
    mc "Listen...is this about what happened at the party?"
    mc "Because I really want to-"
scene ep2_sun_back28 with dissolve
sa "You need to go to the gym, right now!"
scene ep2_sun_back27 with dissolve
menu:
    "Joke" if True:
        mc "Come on, I'm not that fat."
        mc "Let me rest for a day, will you?"
        scene ep2_sun_back28 with dissolve
        sa "This is not the time for jokes!"
        sa "Go there now!"
        scene ep2_sun_back27 with dissolve
        mc "Why is that?"
    "Ask why" if True:
        mc "Why is that?"
scene ep2_sun_back28 with dissolve
sa "Chad just took a call and left in the middle of his workout."
scene ep2_sun_back27 with dissolve
mc "So?"
scene ep2_sun_back28 with dissolve
sa "SO!? He never breaks in the middle of a workout!"
sa "Not even for me!"
sa "I'm telling you, he's talking to his bitch, right now!"
scene ep2_sun_back27 with dissolve
mc "Wait a second! How the hell do you know this?"
mc "Are you at the gym?"
scene ep2_sun_back28 with dissolve
sa "I'm watching him with my binoculars. Duh!"
scene ep2_sun_back27 with dissolve
mc "What? Binoculars!?"
mc "Why the fuck do you own a pair of binoculars?"
scene ep2_sun_back28 with dissolve
sa "Um...birdwatching."
scene ep2_sun_back27 with dissolve
mc "Huh?"
scene ep2_sun_back28 with dissolve
sa "Stop with the third fucking degree, already!"
sa "Remember, you owe me this!"
scene ep2_sun_back27 with dissolve
mc "Yeah, yeah. I remember."
mc "I'll be right there."
scene ep2_sun_back28 with dissolve
sa "Hurry up! I'm not sure how long he's gonna be on the phone."
sa "And remember! I want proof!"
scene ep2_sun_back25 with dissolve
mc "(She's obsessed...)"
mc "(I'll do this for her and then I'm out.)"
scene ep2_gym_reception1 with wiperight
mc "(Seems fancy...)"
mc "(It would be nice to have a real gym to train in...)"
mc "(...but this place is way too rich for my blood.)"
scene ep2_gym_reception with dissolve
mc "Hi."
rc "Excuse me dear. I didn't hear you coming."
rc "I don't recognize your face..."
rc "Are you a freshman?"
scene ep2_gym_receptionb with dissolve
menu:
    "Check her cleavage" if True:
        $ dk(1)
        scene ep2_gym_reception2 with dissolve
        rc "My eyes are up here, sweetie."
        scene ep2_gym_receptionb with dissolve
    "Don't check her cleavage" if True:
        $ dk(-1)
mc "I am. I...uh...wanted to check out the gym."
mc "Do I have to be a member for that?"
scene ep2_gym_reception with dissolve
rc "We offer freshmen a free pass the first time..."
rc "...after that you need to sign up for a membership."
rc "Would you like to sign up for one, right now?"
scene ep2_gym_receptionb with dissolve
mc "I'll think about it."
scene ep2_gym_reception with dissolve
stop music fadeout 5
rc "I see. Well, we're not going anywhere."
rc "Feel free to check out our establishment."

play music "music/ep2/rockin_riff.mp3"
scene ep2_gym_talk with wipeleft
an "YEAH BRO!!! ALL THE WAY DOWN!"
an "FUCK YES!"
dw "ARGH!!!!"
play sound "sound_effects/clang.mp3"
scene ep2_gym_talk1 with vpunch
dw "YEAH! I FUCKING DID IT!"
play sound "sound_effects/slap.mp3"
scene ep2_gym_talk2 with hpunch
an "Amazing! That's a new personal best for you!"
dw "Man, my pecs are so jacked up!"
scene ep2_gym_talk4 with dissolve
dw "Feel how swole I am!"
an "You're mad swole!"
mc "(What the fuck is wrong with these jocks?)"
scene ep2_gym_talk5 with dissolve
dw "Where's my shake!? I need my fucking protein!"
mc "(Loud assholes...)"
scene ep2_gym_talk6 with dissolve
dw "Hey, it's Chad's turn! Where is he?"
scene ep2_gym_talk7 with dissolve
an "In the locker room. He got a phone call."
scene ep2_gym_talk6 with dissolve
dw "A phone call? In the middle of fucking One-Rep Max Sunday?"
scene ep2_gym_talk7 with dissolve
an "Yeah, I think it was Sage."
scene ep2_gym_talk6 with dissolve
dw "Fucking bitches!"
dw "He's missing out on a personal best attempt and a great pump, for her?"
scene ep2_gym_talk9 with dissolve
an "He's probably in there getting a pump in his dick right now."
scene ep2_gym_talk6 with dissolve
dw "The cock wants what the cock wants, huh?"

scene ep2_gym_talk11 with dissolve
an "Dammit, Dawe."
scene ep2_gym_talk6 with dissolve
dw "What?"
scene ep2_gym_talk11 with dissolve
an "She's doing it, again."
scene ep2_gym_talk13 with dissolve
an "Didn't you tell her that you don't do sit-ups in that machine?"
stop music fadeout 3
dw "Dude, I told her like three times, already."

play music "music/ep2/marty.mp3"
scene ep2_gym_sneak with wipeleft
mc "(I guess the gym must be sponsoring the tri-alphas or something...)"
scene ep2_gym_sneak1 with dissolve
mc "(This entire hallway seems to be theirs.)"
scene ep2_gym_sneak2 with dissolve
mc "(Bingo.)"
scene ep2_gym_shower with dissolve
mc "(I can hear someone chatting...)"
mc "(...it must be him.)"
scene ep2_gym_shower2 with dissolve
mc "(Not there...)"

scene ep2_chad_shower with dissolve
mc "(Shit! There he is.)"
ch "Mmm... You're such a tease, babe."
ch "Describe it to me."
mc "(Ok, time to record this...)"
scene ep2_chad_shower1 with dissolve
ch "You liked the new panties I got you?"
ch "Haha, uh-huh!"
ch "Put them on..."
ch "Now, tell me how you squeeze my cock..."
ch "Yeah... Reach down my pants and grab it..."
scene ep2_chad_shower2 with dissolve
ch "And then what?"
ch "Yeah, use your tongue..."
ch "Mmm... Yes..."
ch "I can't wait until I see you again..."
ch "I'm gonna bend you over and slide my wet fingers into you and fuck you so hard-"
play sound "sound_effects/clank.mp3"
scene ep2_chad_shower3 with hpunch
mc "(FUCK!)"
stop music
$ renpy.sound.play("sound_effects/heartbeat.mp3", channel="sfx1", loop=True)
scene ep2_chad_shower4 with dissolve
ch "Huh!?"
ch "Shit... Hang on a second, babe."
scene ep2_chad_shower5 with dissolve
ch "Hello?"
scene ep2_chad_shower6 with dissolve
$ renpy.pause()
scene ep2_chad_shower7 with dissolve
ch "I'm back. No, it's good. I just thought I heard someone."
ch "Where were we?"
$ renpy.sound.stop(channel="sfx1", fadeout=3)
mc "(Ok, that will do.)"
scene ep2_chad_shower8 with dissolve
dw "Huh! What the fuck!?"
play music "music/ep2/metal2.mp3"
scene ep2_chad_shower8b with dissolve
dw "What were you doing in there?"
scene ep2_chad_shower9 with dissolve
menu:
    "Calm approach" if True:
        $ dk(-1)
        mc "Relax. I just went into the wrong changing room. That's all."
        scene ep2_chad_shower8b with dissolve
        dw "No way I'm buying that. The door clearly says tri-alphas!"
    "Hostile approach" if True:
        $ dk(1)
        mc "Fuck off! I was just looking for the changing room."
        scene ep2_chad_shower8b with dissolve
        dw "No way I'm buying that. The door clearly says tri-alphas!"
        scene ep2_chad_shower9 with dissolve
        mc "Oh, you can read now? Cathy will be pleased to hear that."

scene ep2_chad_shower12 with dissolve
dw "I see what you're doing here..."
dw "You're with the DIKs now. You came looking for revenge."
if ep2_jokedDawe:
    dw "And I remember your dildo joke."
    dw "It's not true!"
scene ep2_chad_shower9 with dissolve
mc "Calm down. I'm leaving."
scene ep2_chad_shower17 with dissolve
stop music fadeout 3
dw "Oh...sure... Go ahead..."
scene ep2_chad_shower18 with dissolve
$ renpy.pause()
play sound "sound_effects/whoosh.mp3"
play music "music/ep2/metal.mp3"
scene ep2_chad_shower19
$ renpy.pause(0.5)

if minigames:
    $ brawlerStoryFight = "dawe"
    $ brawlerStoryFightLabel = "ep2_after_dawe_fight_label"
    hide screen phone_screen
    jump app_brawler_label
    label ep2_after_dawe_fight_label:
    $ brawlerStoryFightLabel = ""
    show screen phone_screen
    $ sports_opponent_idx = 0
    $ brawlerStoryFight = ""
    $ brawlerStoryFightLabel = ""
    if ep2_dawe_fight_won and brawler_difficulty == 3 and steamAchievements and not config.console and not config.developer:
        $ achievement.grant("VICEPRESIDENTIALBEATDOWN")
        init:
            $ achievement.register("VICEPRESIDENTIALBEATDOWN")
        $ achievement.Sync()
elif True:
    $ ep2_dawe_fight_won = True
if ep2_dawe_fight_won:
    play sound "sound_effects/hit.mp3"
    scene ep2_chad_shower20 with hpunch
    $ renpy.pause(1)
    play sound "sound_effects/hit.mp3"
    scene ep2_chad_shower21 with hpunch
    $ renpy.pause(1)
    play sound "sound_effects/hit.mp3"
    scene ep2_chad_shower22 with hpunch
    $ renpy.pause(1)
    scene ep2_chad_shower24 with dissolve
    stop music fadeout 3
    dw "You...fucking...cunt..."
    mc "Don't blame me for finishing what you started!"
elif True:
    play sound "sound_effects/hit.mp3"
    scene ep2_chad_shower20 with hpunch
    $ renpy.pause(0.5)
    play sound "sound_effects/hit.mp3"
    scene ep2_chad_shower21 with hpunch
    $ renpy.pause(0.5)
    play sound "sound_effects/hit.mp3"
    scene ep2_chad_shower22b with hpunch
    $ renpy.pause(0.5)
    scene ep2_chad_shower24b with dissolve
    stop music fadeout 3
    dw "Had enough, bitch?"
scene ep2_chad_shower26 with dissolve
an "What's going on here!?"
mc "(Shit!)"
$ bios_history_dawe +="I got into a big fist fight with Dawe.\n\n"
$ bios_name_dawe = True
$ chat_new_bios = True

$ renpy.sound.play("sound_effects/heartbeat.mp3", channel="sfx1", loop=True)
scene ep2_chad_shower26c with dissolve
"*{i}Heartbeats{/i}*"
show screen majorChoiceScale
mc "(Fuck...)"
mc "(I'm not supposed to use my fighting skills this way...)"
mc "(What do I do?)"
if minigames:
    menu:
        "Fight ({color=#ffffff}Requirement: Beat Dawe{/color})" if ep2_dawe_fight_won:
            jump ep2_stayAndFightLabel
        "Run away" if True:
            jump ep2_runLabel
elif True:
    menu:
        "Stay and fight" if True:
            jump ep2_stayAndFightLabel
        "Run away" if True:
            jump ep2_runLabel


label ep2_stayAndFightLabel:
$ ep2FoughtJocks = True
$ renpy.sound.stop(channel="sfx1", fadeout=3)
$ bios_history_mc +="I chose to stay and fight the jocks.\n\n"
$ bios_name_mc = True
$ chat_new_bios = True
$ addCPenalty()
$ renpy.pause(1)
hide screen majorChoiceScale
play music "music/ep2/heavy.mp3"
mc "(Nope. There's only so much shit a man can take.)"
mc "(This is where I draw my line and make my stand.)"
mc "(I'm not gonna be bullied anymore.)"
play sound "sound_effects/hit.mp3"
scene ep2_chad_shower26d with vpunch
$ renpy.pause(0.5)
play sound "sound_effects/hit.mp3"
scene ep2_chad_shower26c2 with vpunch
$ renpy.pause(0.5)
play sound "sound_effects/hit.mp3"
scene ep2_chad_shower26d2 with vpunch
dad2 "{i}Great! Don't stop now!{/i}"
scene ep2_chad_shower26f with dissolve
dad2 "{i}High kick!{/i}"
play sound "sound_effects/hit.mp3"
scene ep2_chad_shower26g with vpunch
$ renpy.pause(0.5)
dad2 "{i}Perfect!{/i}"
scene ep2_chad_shower26h with dissolve
dad2 "{i}Flurry!{/i}"
play sound "sound_effects/hit.mp3"
scene ep2_chad_shower26g2 with vpunch
$ renpy.pause(0.5)
play sound "sound_effects/hit.mp3"
scene ep2_chad_shower26h2 with vpunch
$ renpy.pause(0.5)
play sound "sound_effects/hit.mp3"
scene ep2_chad_shower26i with vpunch
$ renpy.pause(0.5)
scene ep2_chad_shower26k with dissolve
dw "ARRRGH!!!"
play sound "sound_effects/hit.mp3"
scene ep2_chad_shower26j with hpunch
stop music
scene black
$ renpy.pause(1)
scene ep2_chad_shower26l with fade
$ renpy.sound.play("sound_effects/ring.mp3", channel="sfx1", loop=True)
mc "What the..."
mc "(Shit...)"
$ renpy.sound.stop(channel="sfx1", fadeout= 3)
jump ep2_afterRunLabel

label ep2_runLabel:
$ ep2FoughtJocks = False
$ renpy.sound.stop(channel="sfx1", fadeout=3)
$ bios_history_mc +="I chose to run away from the jocks.\n\n"
$ bios_name_mc = True
$ chat_new_bios = True
$ addDPenalty()
$ renpy.pause(1)
hide screen majorChoiceScale
play sound "sound_effects/hit.mp3"
scene ep2_chad_shower27 with hpunch
$ renpy.pause(0.5)

label ep2_afterRunLabel:
scene ep2_chad_shower28 with dissolve
dw "You better run, you cunt!"
scene ep2_chad_shower29 with dissolve
stop music fadeout 5
ch "What the fuck happened here?"
scene ep2_chad_shower30 with dissolve
dw "Remember that freshy who hit on your girl?"
dw "I just caught him sneaking around in our locker room."
scene ep2_chad_shower31 with dissolve
$ renpy.pause()
$ bios_history_chad +="I recorded a video of Chad having phone sex with his side chick.\n\n"
$ bios_name_chad = True
$ chat_new_bios = True

label ep2_after_gym_label:
play music "music/ep2/wings.mp3"
scene ep2_sage_after_jocks with fade
mc "Hey, I'm back."
sa "What the hell happened to you?"
$ guideSuggestedPage = 63
scene ep2_sage_after_jocks1 with dissolve
menu:
    "Alphas" if True:
        mc "Alphas happened..."
    "Cute outfit" if True:
        mc "Hey! Cute outfit!"
        mc "It really suits you."
        scene ep2_sage_after_jocks1b with dissolve
        sa "What!?"
        scene ep2_sage_after_jocks1 with dissolve
mc "It's just a nose bleed, I'll be fine."
scene ep2_sage_after_jock2 with dissolve
sa "Here, lie down."

scene ep2_sage_after_jocks3 with dissolve
mc "Thanks."
menu:
    "Check her out ({color=#ffffff}{size=-1}{font=collegiate.ttf}DIK{/font}{/size}{/color})" if dtype > 0:
        $ dk(1)
        scene ep2_sage_after_jocks4 with dissolve
        $ renpy.pause()
    "Don't risk it" if True:
        $ renpy.pause(0.5)

scene ep2_sage_after_jocks8 with dissolve
sa "Was it Chad?"
scene ep2_sage_after_jocks9 with dissolve
mc "No...Dawe and his pals."
scene ep2_sage_after_jocks10 with dissolve
sa "Dawe!?"
sa "I never liked Dawe."
scene ep2_sage_after_jocks9 with dissolve
menu:
    "Mock Dawe" if True:
        if dtype > 0:
            mc "Dawe's a cunt."
        elif True:
            mc "Me neither."
        mc "What is he, like 35 and still in college?"
        scene ep2_sage_after_jocks12 with dissolve
        sa "Hahaha!"
        sa "Yeah, such a fucking loser."
        $ RPsage += 1
        $ dk(1)
        $ bios_history_sage +="Sage seems to hate Dawe as much as I do. She liked my mean joke about him.\n\n"
        $ bios_name_sage = True
        $ chat_new_bios = True
    "Don't mock Dawe" if True:
        $ dk(-1)
        mc "Me neither."
scene ep2_sage_after_jocks8 with dissolve
sa "But you saw Chad, right?"
scene ep2_sage_after_jocks9 with dissolve
mc "Mhm."
scene ep2_sage_after_jocks8 with dissolve
sa "And...?"
scene ep2_sage_after_jocks9 with dissolve
mc "Yeah, he's cheating on you."
scene ep2_sage_after_jocks16 with dissolve
sa "How sure are you of this?"
mc "I have a video on my phone."
sa "Send it to me."
play sound "sound_effects/message.mp3"
scene ep2_sage_after_jocks19 with dissolve
$ renpy.pause()
scene ep2_sage_after_jocks20 with dissolve
ch "{i}You liked the new panties I got you?{/i}"
ch "{i}Haha, uh-huh!{/i}"
ch "{i}Put them on...{/i}"
ch "{i}Now, tell me how you squeeze my cock...{/i}"
ch "{i}Yeah... Reach down my pants and grab it...{/i}"
scene ep2_sage_after_jocks21 with dissolve
sa "That fucking scumbag! I knew it!"
scene ep2_sage_after_jocks22 with dissolve
mc "Yeah, you were right. Now you know and can move on."
scene ep2_sage_after_jocks24 with dissolve
mc "Are you ok?"
scene ep2_sage_after_jocks24b with dissolve
mc "I'm here for you, if you need to talk."
scene ep2_sage_after_jocks25 with dissolve
$ renpy.pause()
scene ep2_sage_after_jocks25b with dissolve
$ renpy.pause()
scene ep2_sage_after_jocks26 with dissolve
mc "What are you doing?"
scene ep2_sage_after_jocks27 with dissolve
if ep2_kissedSage:
    sa "Continuing from where we left off at the party."
    sa "And you know..."
sa "Scratching your back... Like I promised I would."
sa "You don't like it?"
scene ep2_sage_after_jocks26 with dissolve
menu:
    "Stop" if True:
        $ ep2KissedSage = False
        $ bios_history_sage +="Sage kissed me, but I stopped her.\n\n"
        $ bios_name_sage = True
        $ chat_new_bios = True
        mc "Please, stop it."
        mc "I just wanted to help, because you returned my guitar."
        mc "I didn't want this."
        mc "At least not like this..."
        scene ep2_sage_after_jocks26 with dissolve
        sa "..."
    "Kiss her back" if True:
        $ ep2KissedSage = True
        $ bios_history_sage +="Sage kissed me and I kissed her back.\n\n"
        $ bios_name_sage = True
        $ chat_new_bios = True
        mc "I do like it..."
        scene anim_sage_kiss1_ep2 with dissolve:
            size (config.screen_width, config.screen_height)
        mc "(She has the softest lips...)"
        pause
        scene anim_sage_kiss1b_ep2 with dissolve:
            size (config.screen_width, config.screen_height)
        mc "(That way she runs her fingers through my hair...)"
        mc "(It's both hot and comforting at the same time.)"
        pause

scene ep2_sage_after_jocks32 with dissolve
mc "This whole thing is over now, right?"
scene ep2_sage_after_jocks33 with dissolve
sa "No... Not yet."
scene ep2_sage_after_jocks32 with dissolve
mc "Don't tell me..."
scene ep2_sage_after_jocks33 with dissolve
sa "I want to know who the bitch is."
scene ep2_sage_after_jocks32 with dissolve
menu:
    "Talk her out of it" if True:
        mc "Why don't you just ask him? You have proof of it now."
        scene ep2_sage_after_jocks33 with dissolve
        sa "He would never tell me..."
        sa "He would probably just lie and be more careful."
    "Sympathize" if True:
        mc "I understand how you must be feeling."
        mc "But please, just let it go. This isn't healthy."
        scene ep2_sage_after_jocks33 with dissolve

sa "This isn't over until I find out who that cunt is."
scene ep2_sage_after_jocks38 with dissolve
sa "But as for you and me..."
sa "...we're even."
scene ep2_sage_after_jocks32 with dissolve
mc "Well, that's something..."
scene ep2_sage_after_jocks38 with dissolve
sa "But I'm begging you..."
sa "Will you help me find out who it is?"
scene ep2_sage_after_jocks32 with dissolve
menu:
    "Yes" if True:
        $ ep2_helpSageMore = True
        mc "I can't believe this..."
        mc "Ok... I'll help you."
        scene ep2_sage_after_jocks38 with dissolve
        sa "Thank you."
        scene ep2_sage_after_jocks32 with dissolve
        mc "...but I'm only doing it so you can move on, ok?"
        $ bios_history_sage +="I told Sage I would help her find out who Chad is cheating on her with.\n\n"
        $ bios_name_sage = True
        $ chat_new_bios = True
    "No" if True:
        $ ep2_helpSageMore = False
        mc "Not gonna happen."
        mc "I did my part. I'm out."
        mc "I hope you can manage to move on, Sage."
        $ bios_history_sage +="I told Sage I wouldn't help her find out who Chad is cheating on her with.\n\n"
        $ bios_name_sage = True
        $ chat_new_bios = True
scene ep2_sage_after_jocks44 with dissolve
sa "Move on!?"
sa "Pff!"
scene ep2_sage_after_jocks44c with dissolve
mc "Look..."
mc "He made his choice already."
mc "Just accept that."
sa "..."
mc "I can see that you're still angry..."
scene ep2_sage_after_jocks25 with dissolve
stop music fadeout 3
mc "Hey..."
mc "I have a surefire way to help with that."
label ep2_sage_fight_label:
play music "music/ep2/rockin_riff.mp3"
play sound "sound_effects/hit.mp3"
scene ep2_sage_train0 with hpunch
sa "Aargh!!!"
play sound "sound_effects/hit.mp3"
scene ep2_sage_train0b with hpunch
sa "Hngh!!!"
play sound "sound_effects/hit.mp3"
scene ep2_sage_train0 with hpunch
sa "GAH!!!"
scene ep2_sage_train0c with dissolve
sa "Hahaha!"
mc "Feels good, huh?"
scene ep2_sage_train0d with dissolve
sa "It feels fantastic!"
sa "I never knew training like this was so effective!"
sa "You're really good at this!"
scene ep2_sage_train1 with dissolve
mc "Thank you. I practiced a lot with my dad, growing up."
scene ep2_sage_train2 with dissolve
sa "Not enough to beat the jocks, though."
scene ep2_sage_train1b with dissolve
mc "It's not like I'm superhuman. There were too many of them."
mc "Besides, I don't practice fighting to use it against people."
mc "It's just for being able to defend myself or others."
scene ep2_sage_train3 with dissolve
sa "You mean like it's a code?"
scene ep2_sage_train1b with dissolve
mc "Yeah, exactly. Like a code."
if ep2FoughtJocks:
    mc "(But I kinda broke it today...)"
scene ep2_sage_train5 with dissolve
sa "I can understand that. Frats and sororities have codes, too."
scene ep2_sage_train1b with dissolve
mc "So, what's the HOTs' code?"
scene ep2_sage_train5 with dissolve
sa "All HOTs are sisters. We don't turn against each other."
scene ep2_sage_train1b with dissolve
mc "The way Quinn treats your pledgers doesn't seem like sisterhood to me."
scene ep2_sage_train7 with dissolve
sa "Oh, come on! It's just a bit of hazing."
sa "It's no different from what the DIKs put you through."
scene ep2_sage_train8 with dissolve
sa "I mean, you don't have to like it..."
sa "... but it's a one-time thing you endure before you're one of the gang."
sa "If you don't get that, you will never become a DIK."
scene ep2_sage_train9 with dissolve
mc "I see..."
scene ep2_sage_train8 with dissolve
sa "Either way, that's the HOTs' public code. \"Don't turn on each other.\""
scene ep2_sage_train9 with dissolve
mc "Public code? Do you mean you have a secret code, too?"
scene ep2_sage_train12 with dissolve
sa "Maybe."
scene ep2_sage_train9 with dissolve
mc "What is it?"
scene ep2_sage_train12 with dissolve
sa "Would it be a secret code if I told you?"
scene ep2_sage_train8 with dissolve
sa "The DIKs have codes, too. But you probably knew that already."
scene ep2_sage_train9 with dissolve
mc "Yeah. \"Family comes first\"."
scene ep2_sage_train8 with dissolve
sa "Exactly."
sa "If you are a DIK, you're a brother. And, much like the HOTs, brothers never let their siblings down."
scene ep2_sage_train9 with dissolve
mc "It's a nice code. I never had any siblings to care for."
mc "Although...from what I've seen so far, that's not the impression I've gotten from the DIKs."
mc "Everything is pretty mean-spirited."
scene ep2_sage_train19 with dissolve
sa "There's a lot of things that you don't see until you start looking for them."
mc "What does that mean?"
sa "Nothing..."
scene ep2_sage_train20 with dissolve
mc "Hey...before I forget..."
mc "Thank you for returning my guitar. You did the right thing."
scene ep2_sage_train22 with dissolve
sa "Do you play a lot?"
scene ep2_sage_train20 with dissolve
mc "Yes, almost daily."
scene ep2_sage_train3 with dissolve
sa "I always wanted to learn how to play the guitar."
sa "I never took the initiative..."
scene ep2_sage_train2 with dissolve
sa "Chad knew that... That's why he gave it to me."
$ guideSuggestedPage = 64
scene ep2_sage_train1b with dissolve
menu:
    "Be mad at Chad" if True:
        if dtype < 1:
            mc "It may sound nice of him to give you a gift like that, but it was my guitar that he had stolen."
        elif True:
            mc "I think you meant to say that he stole it and unloaded it on you."
        sa "..."
        scene ep2_sage_train2 with dissolve
    "Ask more about Sage" if True:
        mc "What stopped you from starting to learn?"
        scene ep2_sage_train3 with dissolve
        sa "You know...excuses. Procrastination."
        sa "Certain family members that thought I should be playing something fancier than a guitar."
        scene ep2_sage_train1b with dissolve
        mc "Fancier?"
        scene ep2_sage_train2 with dissolve
        sa "Meh...fuck it."
sa "Would you teach me how to play it?"

scene ep2_sage_train1b with dissolve
if dtype > 0:
    $ RPsage += 1
    mc "So, you want me to be your {i}teacher{/i}?"
    scene ep2_sage_train30 with dissolve
    sa "Haha, not in a naughty way."
elif True:
    mc "So, you want me to be your teacher?"
    scene ep2_sage_train3 with dissolve
    sa "Yeah, if you want to."
scene ep2_sage_train33 with dissolve
menu:
    "Yes" if True:
        $ ep2SageGuitarTeacher = True
        $ RPsage += 1
        mc "Sure."
        scene ep2_sage_train34 with dissolve
        sa "Really? For real?"
        scene ep2_sage_train33 with dissolve
        mc "It sounds like fun."
        scene ep2_sage_train34 with dissolve
        sa "Great...then let's set something up."
        $ bios_history_sage +="Sage asked me to teach her to play the guitar. I accepted.\n\n"
        $ bios_name_sage = True
        $ chat_new_bios = True
    "No" if True:
        $ ep2SageGuitarTeacher = False
        mc "Sorry, but I have to say no."
        scene ep2_sage_train3 with dissolve
        sa "Ok, that's cool."
        $ bios_history_sage +="Sage asked me to teach her to play the guitar. I declined.\n\n"
        $ bios_name_sage = True
        $ chat_new_bios = True

scene ep2_sage_train34b with dissolve
sa "Thank you for the training session. It was fun and I needed it."
scene ep2_sage_train33 with dissolve
mc "Anytime, Sage."
mc "I hope that you've cooled down."
stop music fadeout 3
scene ep2_sage_train36 with dissolve
sa "Time to hit the showers. See you later!"

label ep2_yoga_label:

play music "music/ep2/relaxing_ballad.mp3"
scene ep2_yoga with dissolve
isa "And breathe out."
mc "(Hm, that's Bella doing yoga with someone.)"
isa "Great form, Jill."
mc "(Jill!?)"
scene ep2_yoga1 with dissolve
menu:
    "Look closer" if True:
        $ dk(1)
        scene ep2_yoga2 with dissolve
        mc "(Oh my God!!!)"
    "Don't risk it" if True:
        $ dk(-1)
scene ep2_yoga3 with dissolve
isa "Looks like we have ourselves a spectator."
scene ep2_yoga4 with dissolve
mc "Oh, me? No, I wasn't looking."
scene ep2_yoga5 with dissolve
ji "Hi, [name]!"
scene ep2_yoga6 with dissolve
mc "Hey, Jill."
isa "*{i}Coughs{/i}*"
scene ep2_yoga7 with dissolve
mc "And hey, Bella!"
scene ep2_yoga8 with dissolve
isa "Don't call me Bella."
scene ep2_yoga7 with dissolve
menu:
    "Hi Bella" if True:
        $ RPisabella -= 1
        $ bios_history_isabella +="You teased Isabella. She didn't like it.\n\n"
        $ bios_name_isabella = True
        $ chat_new_bios = True
        mc "Hi Bella."
    "Hi Isabella" if True:
        mc "Hi Isabella."
mc "Practicing yoga?"
scene ep2_yoga12 with dissolve
ji "Yes, we do it a couple of times every week."
scene ep2_yoga13 with dissolve
mc "It's a good way to stay in shape."
scene ep2_yoga14 with dissolve
isa "And how would you know that?"
scene ep2_yoga14b with dissolve
menu:
    "Compliment them" if True:
        mc "Well, you said you do it a couple of times a week and are both in great shape."
        scene ep2_yoga15 with dissolve
        $ renpy.pause()
        $ RPjill += 1
        $ bios_history_jill +="I complimented Jill. She liked it.\n\n"
        $ bios_name_jill = True
        $ chat_new_bios = True
    "Don't push it" if True:
        mc "Common knowledge..."
mc "Also, I've done yoga before, too."
scene ep2_yoga14 with dissolve
isa "Lies."
scene ep2_yoga14b with dissolve
mc "I'm not lying. I'm very bendy."
scene ep2_yoga14 with dissolve
isa "Then show me."
scene ep2_yoga19 with dissolve
mc "All right, I'll do that pose Jill just did."
scene ep2_yoga20 with dissolve
isa "How would you know what pose she did? You weren't watching, remember?"
scene ep2_yoga19 with dissolve
mc "I...ah..."
scene ep2_yoga20 with dissolve
isa "Go ahead. Do the pose that Jill just did."
scene ep2_yoga22 with dissolve
mc "See?"
isa "You're doing it wrong."
mc "Really?"
scene ep2_yoga23 with dissolve
ji "Yes, straighten your back more."
ji "Like this."
if dtype > 0:
    scene ep2_yoga23b with dissolve
    mc "(Oh shit...)"
elif True:
    mc "(Oh, wow...)"
scene ep2_yoga25 with dissolve
isa "Yes, straighten your back, boy."
mc "Ouch!"
scene ep2_yoga26 with dissolve
isa "That's...better."
scene ep2_yoga27 with dissolve
ji "How about this pose?"
scene ep2_yoga28 with dissolve
isa "You almost got it. Lift your back a bit more."
menu:
    "Look closer" if True:
        $ dk(1)
        scene ep2_yoga32 with dissolve
        mc "(She's so fucking hot...)"
    "Don't risk it" if True:
        $ dk(-1)
        mc "(Focus...don't look...)"
$ guideSuggestedPage = 65
isa "Are you watching her?"
menu:
    "Yes" if True:
        mc "Yes..."
    "No" if True:
        mc "No..."
        isa "Then watch closer!"
        scene ep2_yoga32 with dissolve
mc "Looks good."
isa "Let me see you try it."
scene ep2_yoga34 with dissolve
mc "Hngh...like this?"
isa "What do you think, Jill?"
ji "Not quite right..."
isa "I agree."
scene ep2_yoga37 with dissolve
ji "Straighten your legs more and try bending a bit further."
scene ep2_yoga38 with dissolve
ji "Great! Haha! Hi!"
mc "Hi!"
scene ep2_yoga39 with dissolve
mc "..."
mc "Isabella."
scene ep2_yoga40 with dissolve
isa "Sloppy."
isa "At least you weren't lying. I see that you have done similar exercises before."
scene ep2_yoga40b with dissolve
ji "I think he did great."
scene ep2_yoga41 with dissolve
isa "Excuse me for a minute, I need to refill my water bottle."

label ep2_jill_yoga_label:
scene ep2_yoga43 with dissolve
if dtype > 0:
    mc "That woman scares the shit out of me."
elif True:
    mc "That woman really scares me."
scene ep2_yoga44 with dissolve
ji "Haha! Come on! She's not scary, she's nice."
scene ep2_yoga43 with dissolve
mc "Nice? Kittens are nice. That woman is no pussycat..."
mc "She's more like a cheetah!"
scene ep2_yoga46 with dissolve
ji "That's still a feline."
scene ep2_yoga43 with dissolve
mc "You two seem so different..."
mc "How come you're friends?"
scene ep2_yoga46 with dissolve
ji "We're not that different."
ji "We share a lot of common hobbies, such as books, yoga and wine tasting."
scene ep2_yoga43 with dissolve
mc "Does she tell you that you're drinking wine the wrong way, too?"
scene ep2_yoga54b with dissolve
ji "Haha, now you're the mean one!"
ji "Give her a chance. I think you would see that there's much more to her than you think."
scene ep2_yoga43 with dissolve
mc "I am giving her a chance, but so far I went from calling her Bella to Isabella."
mc "That's a big step backwards."
scene ep2_yoga46 with dissolve
ji "You should probably not have called her Bella to begin with."
scene ep2_yoga43 with dissolve
mc "It's just a name! How could that upset her, really?"
scene ep2_yoga54 with dissolve
ji "It's your attitude, too."
scene ep2_yoga54c with dissolve
if dtype > 0:
    mc "*{i}Sigh{/i}* Whatever..."
elif True:
    mc "*{i}Sigh{/i}*"
mc "I just wanted to show her that I'm thankful for the help."
scene ep2_yoga54 with dissolve
ji "She knows that you're thankful. She just doesn't let people in that easily."
ji "Don't take it personally."
scene ep2_yoga54c with dissolve
mc "You seem a lot more open than her."
scene ep2_yoga58 with dissolve
ji "Well, not really..."
ji "...just a bit more understanding, maybe."
scene ep2_yoga59 with dissolve
ty "Jill! I thought that was you! Hi!"
scene ep2_yoga61 with dissolve
ji "Oh...hi!"
mc "(The panty sniffer...)"
mc "(Such a creep...)"
menu:
    "Say hey" if True:
        mc "Hi, Tybalt!"
    "Ignore him" if True:
        $ renpy.pause(0.5)
scene ep2_yoga62 with dissolve
ty "I was just out running laps. You know, working on my endurance."
ty "You like running, right?"
scene ep2_yoga62b with dissolve
menu:
    "Joke" if True:
        if dtype > 0:
            mc "Maybe she does..."
            mc "Why don't you start running again and find out if she follows you?"
        elif True:
            mc "I do like running! Thanks for asking!"
    "Let Jill answer" if True:
        scene ep2_yoga62c with dissolve
        ji "Yes, I suppose."
scene ep2_yoga62 with dissolve
ty "Why don't you join me for a brisk jog back to the mansion?"
ty "I have some excellent ideas for that campaign you wanted to start!"
scene ep2_yoga66 with dissolve
ji "You do? Really?"
scene ep2_yoga65 with dissolve
ty "Yes, I've been thinking about it all morning!"
ty "Come, I'll tell you all about it."
ji "Oh! Well, all right!"
scene ep2_yoga67b with dissolve
ji "I gotta run. See you later, [name]."
scene ep2_yoga68 with dissolve
ty "Ok, so here's where you should start with the campaign..."
mc "(Ok, I definitely get it...)"
mc "(That snob has a crush on Jill...)"
$ bios_history_jill +="Jill is interested in starting some sort of campaign. I wonder what for.\n\n"
$ bios_name_jill = True
$ bios_history_tybalt +="Tybalt is in love with Jill and uses tricks to catch her interest.\n\n"
$ bios_name_tybalt = True
$ chat_new_bios = True

label ep2_after_yoga_label:
scene ep2_yoga69 with dissolve
isa "I knew it."
mc "Knew what?"
scene ep2_yoga70 with dissolve
isa "You scared her off, didn't you?"
scene ep2_yoga70b with dissolve
mc "I didn't. She left with Tybalt."
scene ep2_yoga71 with dissolve
isa "Tybalt!? I don't like that guy."
scene ep2_yoga70b with dissolve
menu:
    "Me neither" if True:
        $ RPisabella += 1
        mc "That makes two of us."
        $ bios_history_isabella +="Isabella doesn't like Tybalt. That's one thing we have in common.\n\n"
        $ bios_name_isabella = True
        $ chat_new_bios = True
    "Who do you like?" if True:
        mc "Well, you don't like anyone."
        scene ep2_yoga73 with dissolve
        isa "..."
        mc "Case in point."

scene ep2_yoga71 with dissolve
isa "So... You're into Jill?"
scene ep2_yoga75 with dissolve
mc "That's none of your business."
scene ep2_yoga71 with dissolve
isa "She seems to like you."
scene ep2_yoga75 with dissolve
mc "..."
mc "She does?"
scene ep2_yoga76 with dissolve
isa "Jill is...special...to me."
isa "If you don't get along with me, you won't get along with her. I can assure you that."
scene ep2_yoga75 with dissolve
mc "What?"
scene ep2_yoga71 with dissolve
isa "Jill and I are close. And I think you're trouble."
scene ep2_yoga75 with dissolve
mc "Of course you would say that! You have been against me since day one."
mc "It's not like she's your daughter or anything. Let her make her own decisions."
scene ep2_yoga77 with dissolve
$ renpy.pause()
scene ep2_yoga71 with dissolve
isa "I know boys like you. You're only after one thing."
scene ep2_yoga75 with dissolve
mc "You have no clue what I'm looking for or where I'm coming from."
scene ep2_yoga80 with dissolve
isa "(...)"
isa "(This is just for Jill...)"
scene ep2_yoga71 with dissolve
isa "Then tell me. You get one chance to change my mind."
scene ep2_yoga75 with dissolve
mc "Look, I'm all sweaty. Can we do this another time?"
scene ep2_yoga71 with dissolve
isa "Tonight. Dinner at Luigi's. 8 p.m....do {b}not{/b} be late."
scene ep2_yoga83 with dissolve
mc "Fine! It's a date."
stop music fadeout 3
isa "It is NOT a date."

label ep2_pre_dinner_label:
scene ep2_dik_night with wiperight
tm "Maggot! Where the fuck have you been?"
mc "In the shower."
scene ep2_dik_night1 with dissolve
tm "Unless it was a golden one, I'm not interested in hearing more about that."
tm "Here! Drink!"
scene ep2_dik_night3 with dissolve
play sound "sound_effects/bottle_open.mp3"
mc "Oh, I can't tonight. I'm going out for dinner."
scene ep2_dik_night4 with dissolve
play sound "sound_effects/bottle_pour.mp3"
tm "Are you refusing orders, maggot!?"
tm "DRINK!"
play music "music/ep2/feel_bad.mp3"
scene ep2_dik_night6 with wipeleft
play sound "sound_effects/bottle_pour.mp3"
dikcs "CHUG! CHUG! CHUG!"
tm "That's fucking right, you maggots!"
tm "You're both gonna make up for what shitface over here missed out on this weekend."
scene ep2_dik_night8 with dissolve
play sound "sound_effects/bottle_pour.mp3"
tm "Going home to see your family during the first big weekend at campus..."
tm "I've never been this disappointed before!"
scene ep2_dik_night9 with dissolve
mc "*{i}Glug{/i}* Hey, I've had enough..."
mc "I'm gonna be late for dinner..."
scene ep2_dik_night8 with dissolve
play sound "sound_effects/bottle_pour.mp3"
tm "You've had enough when I say so!"
tm "DRINK!"
tm "You don't see your maggot brother complaining now, do you?"
scene ep2_dik_night12 with dissolve
play sound "sound_effects/bottle_pour.mp3"
mc "Derek? Are you ok?"
scene ep2_dik_night13 with dissolve
de "Yesh, yeshhh! I'm totally fine."
play sound "sound_effects/shove.mp3"
scene ep2_dik_night14 with vpunch
tm "Now, that's how it looks when you've had enough."
scene ep2_dik_night8 with dissolve
play sound "sound_effects/bottle_pour.mp3"
tm "DRINK!"
scene ep2_dik_night15 with wiperight
mc "DEREK!?"
de "Haha...yeah...?"
scene ep2_dik_night16 with dissolve
mc "WHAT TIME IS IT!?"
mc "HOLY SHIT! I'M--I'M-GONNA BE LATE FOR DINNER!"
mc "DEEEEREEK! I'M GONNA GO EAT DINNER WITH THE ICE QUEEN!"
scene ep2_dik_night19 with dissolve
de "Haha...ice cream..."
scene ep2_dik_night16 with dissolve
mc "DEEEEREEK! DO YOU WANT SOME PASTA FROM LUIGI'S!?"
scene ep2_dik_night21 with dissolve
de "[mc_de_up]! I've got it!"
de "."
de ".."
de "..."
play sound "sound_effects/shove.mp3"
scene ep2_dik_night26 with vpunch
mc "I NEED TO GO AND EAT DINNER WITH LUIGI!"
stop music fadeout 3

label ep2_bella_date_label:
$ renpy.sound.set_volume(0.3,channel='sfx1')
$ renpy.sound.play("sound_effects/cafeteria.mp3", channel="sfx1", loop=True)
scene ep2_bella_date with wipeleft
mc "Hey! Bella!"
play music "music/ep2/marty.mp3"
isa "Isabella. You're late."
mc "I'm so, sorry. Something, came up."
scene ep2_bella_date2 with dissolve
mc "I'm here now."
scene ep2_bella_date3 with dissolve
isa "You're drunk."
scene ep2_bella_date2 with dissolve
mc "It's not my fault. They forced me to drink."
mc "I kept telling them that I had enough, but-"
play sound "sound_effects/burp.mp3"
scene ep2_bella_date4 with dissolve
mc "*{i}Burp{/i}*"
mc "You know how it is..."
scene ep2_bella_date6 with dissolve
isa "I can't believe that I actually wanted to give you a shot."
scene ep2_bella_date7 with dissolve
mc "Wait, don't leave! Bella!"
scene ep2_bella_date8 with dissolve
isa "Isabella."
mc "Sorry!"
mc "Bella, I-"
isa "Isabella!!"
mc "Are you hungry? Let's eat."
scene ep2_bella_date7 with dissolve
isa "I'm leaving."
mc "Come on."
play sound "sound_effects/shove.mp3"
scene ep2_bella_date15 with vpunch
mc "Haha. Whoops..."
scene ep2_bella_date16 with dissolve
isa "Dear God. You can't even stand up straight."
scene ep2_bella_date17 with dissolve
mc "But I can lay down flat!"
mc "Here, come join me...the stars are beautiful tonight."
scene ep2_bella_date18 with dissolve
mc "Bella! Don't go!"
scene ep2_bella_date19 with dissolve
mc "Bella! I need you!"
scene ep2_bella_date20 with dissolve
mc "Haha! Oh look, a quarter!"
scene ep2_bella_date19 with dissolve
mc "I'm so tired..."
scene ep2_bella_date16 with dissolve
isa "Get up!"
scene ep2_bella_date17 with dissolve
mc "Hey! Bella!"
mc "Or is it...Belladonna?"
scene ep2_bella_date24 with dissolve
isa "Isabella! Get up!"
isa "You're going to get yourself arrested. Is that what you want?"
scene ep2_bella_date25 with dissolve
isa "You are such a mess."
mc "Your eyes sparkle."
scene ep2_bella_date28 with dissolve
isa "Get in the car."
mc "Oh my God! You're so bossy."
$ renpy.sound.stop(channel="sfx1", fadeout=3)
scene ep2_bella_date29 with dissolve
isa "I'm dropping you off at your fraternity so you can sleep and sober up."
scene ep2_bella_date30 with dissolve
mc "Good luck with that. I'm not allowed to sleep there, yet."
scene ep2_bella_date29 with dissolve
isa "So, where do you stay?"
$ renpy.sound.set_volume(1,channel='sfx1')
scene ep2_bella_date31 with dissolve
mc "You are driving {b}really{/b} fast."
scene ep2_bella_date32 with dissolve
isa "I haven't even started the engine yet."
stop music fadeout 3
scene ep2_bella_date33 with dissolve
mc "Well, slow down!"
scene ep2_bella_date34 with Fade(1.5, 1, 0.5)
play music "music/ep1/apra_hyde.mp3"
mc "Hey...it's this song."
mc "I love this song."
scene ep2_bella_date35 with dissolve
isa "It's my favorite song."
scene ep2_bella_date36 with dissolve
mc "No way! It is my dad's favorite, too!"
mc "When I was young, my dad played me this song on the radio!"
scene ep2_bella_date37 with dissolve
isa "Your breath reeks of alcohol."
scene ep2_bella_date36 with dissolve
mc "Thanks!"
scene ep2_bella_date38 with dissolve
mc "And I surprised him by learning to play it on the guitar."
mc "On his birthday, I played it for him."
mc "He said that it was the nicest gift he'd ever gotten."
mc "That felt really good to hear, because I couldn't afford to buy him something."
scene ep2_bella_date35 with dissolve
isa "...that was a very nice gesture."
scene ep2_bella_date36 with dissolve
mc "I fucked up at several parts, though."
mc "But he didn't care."
mc "I love my dad."
scene ep2_bella_date42 with dissolve
mc "..."
scene ep2_bella_date37 with dissolve
isa "What?"
scene ep2_bella_date42 with dissolve
menu:
    "Compliment her" if True:
        $ RPisabella += 1
        $ bios_history_isabella +="I complimented Isabella, she actually liked it.\n\n"
        $ bios_name_isabella = True
        $ chat_new_bios = True
        scene ep2_bella_date43 with dissolve
        mc "You look very pretty tonight, Isabella."
        scene ep2_bella_date45 with dissolve
        isa "Isabe-!"
        scene ep2_bella_date46 with dissolve
        isa "Oh..."
        isa "Thank you."
    "Thank her" if True:
        scene ep2_bella_date36 with dissolve
        mc "Thank you for the ride!"
        mc "I have no clue where we're going, but thanks!"
        isa "..."

scene ep2_bella_date36 with dissolve
mc "Did you dress up just for me?"
isa "..."
mc "I think you did..."
mc "I guessed I fucked up my chance..."
scene ep2_bella_date37 with dissolve
isa "Your chance of what?"
scene ep2_bella_date43 with dissolve
mc "You know, about our date. Showing you that I'm thankful to you..."
mc "...and that I'm not the kind of guy that you think I am."
isa "..."
mc "You don't talk much."
scene ep2_bella_date37 with dissolve
isa "I talk enough."
scene ep2_bella_date43 with dissolve
mc "And you never smile."
scene ep2_bella_date37 with dissolve
isa "I do smile."
scene ep2_bella_date36 with dissolve
mc "No, I don't think you do."
scene ep2_bella_date53 with dissolve
mc "You go like this!"
scene ep2_bella_date54 with dissolve
mc "Or like this!"
scene ep2_bella_date36 with dissolve
mc "What's up with that?"
scene ep2_bella_date37 with dissolve
isa "Just...sit back and close your eyes for a while."

label ep2_bella_date2_label:
scene ep2_bella_date56 with fade
mc "Hey, this isn't the DIK mansion."
isa "No. This is my house."
scene ep2_bella_date56b with dissolve
mc "It's so big!"
scene ep2_bella_date57 with dissolve
isa "Here you go. Eat this."
scene ep2_bella_date58 with dissolve
mc "This tastes very good. Did you cook this?"
isa "When you're done eating you may sleep on the couch upstairs. Goodnight."
scene ep2_bella_date62 with dissolve
mc "This food is {b}so{/b} good."
mc "Oh..."
$ guideSuggestedPage = 66
jump ep2_freeroam_bella_label
label ep2_after_bella_freeroam_label:
play sound "sound_effects/door_knob.mp3"
if ep2_helpedBellaFrame3:
    scene ep2_fr_bella_main6a with hpunch
elif True:
    scene ep2_fr_bella_main6b with hpunch
mc "(Hm...this door is locked.)"
scene ep2_bella_home with dissolve
isa "Did I tell you to sleep downstairs or did I say upstairs on the couch?"
scene ep2_bella_home1 with dissolve
mc "I can't find upstairs."
scene ep2_fr_bella_main7 with dissolve
isa "Have you seen staircases before? That one over there would likely be what you're looking for."
scene ep2_bella_home3 with dissolve
mc "I found the couch, Isabella! I found it."
scene ep2_bella_home4 with dissolve
isa "There. Go to sleep, we'll talk in the morning."
scene ep2_bella_home4b with dissolve
mc "You are so beautiful."
isa "..."
scene ep2_bella_home5 with dissolve
isa "You're still drunk."

label ep2_bella_home_label:
scene black with Fade(1.5, 1, 0.5)
$ renpy.pause(0.5)
scene ep2_bella_night with fade
mc "(I can't sleep...)"
mc "(Where am I...?)"
scene ep2_bella_night1 with dissolve
mc "(Bella?)"
scene ep2_bella_night2 with dissolve
mc "(I'm naked...?)"
scene ep2_bella_night3 with dissolve
mc "(Damn...my head...it's spinning.)"
scene ep2_bella_night4 with hpunch
mc "Oh, shit! You startled me."
scene ep2_bella_night5 with dissolve
isa "Are you ok?"
scene ep2_bella_night4 with dissolve
mc "I'm a bit thirsty..."
scene ep2_bella_night7 with dissolve
isa "I put some water right next to you."
mc "Thank you."
scene ep2_bella_night8 with dissolve
isa "Are you starting to sober up?"
scene ep2_bella_night8b with dissolve
mc "I...think so..."
scene ep2_bella_night9 with dissolve
isa "Well, you seem to be able to actually answer questions now..."
isa "...without breathing close to my face..."
isa "...so you shouldn't be far off."
scene ep2_bella_night9b with dissolve
mc "Oh crap..."
mc "I'm sorry."
scene ep2_bella_night9c with dissolve
isa "Yeah, you're sorry."
scene ep2_bella_night9e with dissolve
mc "You seem to catch me at my worst, every time."
mc "If I'm not drunk, I'm naked..."
scene ep2_bella_night9d with dissolve
isa "Or both..."
scene ep2_bella_night9e with dissolve
mc "Haha...whoops..."
scene ep2_bella_night9d with dissolve
isa "Yeah, you're not sober, yet."
scene ep2_bella_night9e with dissolve
mc "You know, I was forced to drink, tonight."
mc "It's part of the hazing they put us through."
scene ep2_bella_night9h with dissolve
isa "Even with peer pressure..."
isa "...there's always a choice."
scene ep2_bella_night9i with dissolve
mc "Then you haven't met Tommy..."
label ep2_bella_lewd_label:
hide screen phone_screen
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
    play music "music/ep2/winter.mp3"
scene ep2_bella_night9e with dissolve
mc "Anyway..."
mc "I didn't mean to ruin our date."
scene ep2_bella_night9f with dissolve
isa "Dinner! Not date!"
scene ep2_bella_night9e with dissolve
mc "You sure do like correcting me."
scene ep2_bella_night9f with dissolve
isa "It's just beyond comprehension that you refuse to listen to what I sa-"
scene ep2_bella_kiss11 with dissolve
isa "Wha-!?"
scene ep2_bella_kiss_shock1 with dissolve
isa "(What the hell is this boy doing!?)"
scene ep2_bella_kiss_shock2 with dissolve
isa "(I have never been this...)"
scene ep2_bella_kiss_shock3 with dissolve
isa "(...this...)"
scene ep2_bella_kiss_shock4 with dissolve
isa "(...)"

scene anim_bella_kiss_ep2 with dissolve:
    size (config.screen_width, config.screen_height)
isa "(...calm...)"
pause
scene ep2_bella_kiss2 with dissolve
mc "(Did I just go in for a kiss?)"
scene anim_bella_kiss2_ep2 with dissolve:
    size (config.screen_width, config.screen_height)
mc "(I did... I'm kissing Bella...)"
mc "(...and she's kissing me back!)"
pause
scene ep2_bella_kiss3 with dissolve
mc "(She even has her hand between my legs...)"
mc "(...and slightly grazing my cock with her fingers.)"
mc "(I don't even know what I'm doing...)"
mc "(This must be a drunken dream...)"
scene ep2_bella_kiss4 with dissolve
mc "(If it is a dream...)"
mc "(...maybe she'll let me touch her boobs?)"
scene ep2_bella_kiss5 with dissolve
mc "(Oh my god! They are so fucking big!)"
scene ep2_bella_kiss6 with dissolve
mc "(Oh...)"
scene ep2_bella_kiss7 with dissolve
isa "(I...just can't...)"
isa "(Not with a young student...)"
isa "(Not with anyone!)"
isa "(Fuck, Bella. Snap out of it!)"
scene ep2_bella_kiss9 with dissolve
isa "This didn't happen."
isa "You're still drunk."
scene ep2_bella_kiss10 with dissolve
mc "Are you...sure?"
scene ep2_bella_kiss9 with dissolve
isa "[name]... I'm a married woman."
scene ep2_bella_kiss10 with dissolve
mc "Oh..."
scene ep2_bella_kiss12 with dissolve
isa "Go to sleep."
mc "(Damn...)"
menu:
    "Look closer" if True:
        $ dk(1)
        scene ep2_bella_kiss13 with dissolve
        mc "(So close...)"
    "Don't look closer" if True:
        $ dk(-1)
        mc "(So close...)"

label ep2_bella_home2_label:
scene ep2_bella_mast with fade
isa "(Why did he...?)"
isa "(I don't understand...)"
isa "(I feel so...so...dirty...)"
isa "(This is not what a married woman does...)"
play sound "sound_effects/switch.mp3"
scene ep2_bella_mast1 with dissolve
isa "(I'm so sorry...)"
scene ep2_bella_mast2 with dissolve
isa "(It just caught me completely off guard...)"
isa "(How long has it been since a man did this to me?)"
isa "(Three years?)"
isa "(No, that can't be right...)"
isa "(I haven't gotten an urge to touch myself...that's all...)"
isa "(Until tonight...)"
scene ep2_bella_mast3 with dissolve
$ renpy.pause()
scene ep2_bella_mast4 with dissolve
isa "(Just...for a little bit...)"
scene ep2_bella_mast5 with dissolve
isa "(Oh...wow...)"
isa "(...now I remember...)"
scene anim_bella_mast_ep2 with dissolve:
    size (config.screen_width, config.screen_height)
isa "(Oh God... I can't believe that it took a drunken college idiot to get me going again...)"
isa "(That moronic...boy!)"
isa "([name]...)"
isa "(No...I can't be thinking about...)"
isa "([name]...)"
isa "(...)"
stop music fadeout 3
isa "(Take it slow, [name].)"
$ renpy.end_replay()
$ persistent.ep2_lewd_bella = True
$ calcScenes()
label ep2_bella_morning_label:
if ep2_textedMaya:
    $ chat_maya_history = ["Hey...are you ok? I just saw Derek and it got me worried about you.", "YuarthmstbutiflglIvesen Irlythnkthweshuldgt2gthertnight right?"]
    $ chat_maya_history_is_them = [True, False]
show screen phone_screen
$ bios_history_isabella +="Our dinner date was interesting... I was an asshole for showing up drunk, but somehow I ended up in her home and I even made out with her.\n\nBella told me she was married.\n\n"
$ bios_name_isabella = True
$ chat_new_bios = True
scene ep2_bella_morning1 with Fade(1.5,1,0.5)
play music "music/ep2/relaxing_ballad.mp3"
isa "Good morning."
mc "Morning..."
isa "There's breakfast if you want it."
scene ep2_bella_morning2 with dissolve
mc "Thank you."
scene ep2_bella_morning3 with dissolve
isa "Are you fully sober, yet?"
scene ep2_bella_morning2 with dissolve
mc "My headache says yes..."
mc "I don't feel very good today."
scene ep2_bella_morning3 with dissolve
isa "You deserve what you're feeling."
scene ep2_bella_morning6 with dissolve
mc "I did say I was sorry to you last night...right?"
scene ep2_bella_morning3 with dissolve
isa "You don't remember?"
scene ep2_bella_morning2 with dissolve
menu:
    "I remember" if True:
        mc "I remember our first kiss."
        scene ep2_bella_morning5 with dissolve
        isa "Our last kiss."
        scene ep2_bella_morning4 with dissolve
        mc "Well, it was our first, too."
    "It's foggy" if True:
        mc "No, it's foggy...."
        scene ep2_bella_morning3 with dissolve
        isa "Good."

$ ep2_bellaQuestions = 0
if ep2_helpedBellaKitchen or ep2_helpedBellaFrame1 or ep2_helpedBellaFrame2 or ep2_helpedBellaFrame3 or ep2_helpedBellaMask:
    if ep2_helpedBellaKitchen:
        $ ep2_bellaQuestions +=1
    if ep2_helpedBellaFrame1:
        $ ep2_bellaQuestions +=1
    if ep2_helpedBellaFrame2:
        $ ep2_bellaQuestions +=1
    if ep2_helpedBellaFrame3:
        $ ep2_bellaQuestions +=1
    if ep2_helpedBellaMask:
        $ ep2_bellaQuestions +=1



    scene ep2_bella_morning5 with dissolve
    isa "I have a question."
    scene ep2_bella_morning4 with dissolve
    mc "Ok?"

    scene ep2_bella_morning5 with dissolve

    if ep2_helpedBellaKitchen:
        isa "Why did you drink all my white wine?"
        scene ep2_bella_morning4 with dissolve
        mc "Your...wine?"
        play sound "sound_effects/whoosh_2.mp3"
        scene ep2_freeroam_bella_kitchen3
        $ renpy.pause()
        scene ep2_bella_morning2
        play sound "sound_effects/whoosh_2.mp3"
        mc "Oh shit...I..."
        mc "I think I used it when I did the dishes..."
        scene ep2_bella_morning6 with dissolve
        isa "Mhm..."
        $ ep2_bellaQuestions -=1
        if ep2_bellaQuestions > 0:
            scene ep2_bella_morning3 with dissolve
            isa "I have another question."

    if ep2_helpedBellaFrame1 or ep2_helpedBellaFrame2 or ep2_helpedBellaFrame3:
        isa "Why is almost every photo frame in my house tilted?"
        scene ep2_bella_morning2 with dissolve
        mc "Um...I think they were tilted and I helped you with them..."
        scene ep2_bella_morning6 with dissolve
        isa "Mhm..."
        $ ep2_bellaQuestions -=3
        if ep2_helpedBellaMask:
            scene ep2_bella_morning3 with dissolve
            isa "I have another question."
            mc "(What the fuck did I do last night?)"

    if ep2_helpedBellaMask:
        isa "Why is my antique African mask lying on the floor in the study?"
        $ renpy.sound.set_volume(0.0,channel='music')
        play sound "sound_effects/whoosh_2.mp3"
        scene ep2_bella_study6
        play sound "sound_effects/rain_dance.mp3"
        mc "Watch me do the rain dance, bitches!"
        mc "When I'm done dancing you'll all be drowning!!!"
        mc "Muhahaha!"
        stop sound
        play sound "sound_effects/whoosh_2.mp3"
        $ renpy.sound.set_volume(1.0,channel='music')
        scene ep2_bella_morning2
        mc "No comment..."
        scene ep2_bella_morning3 with dissolve
        isa "And speaking of the study..."
        isa "Can you think of any reason why you decided to block the door with my plants?"
        play sound "sound_effects/whoosh_2.mp3"
        scene ep2_bella_study7
        mc "Fuck you, army guy! You're not getting the treasure!"
        play sound "sound_effects/whoosh_2.mp3"
        scene ep2_bella_morning2
        mc "I thought I saw someone in there..."
        mc "An intruder..."
        mc "But thinking about it..."
        play sound "sound_effects/whoosh_2.mp3"
        scene ep2_bella_study4b
        mc "It might have been a mannequin..."
        scene ep2_bella_morning6 with dissolve
        isa "Mhm..."
    scene ep2_bella_morning2 with dissolve
    mc "I'm sorry..."
elif True:
    scene ep2_bella_morning2 with dissolve
mc "Where are we, by the way?"
scene ep2_bella_morning3 with dissolve
isa "In my house."
scene ep2_bella_morning2 with dissolve
mc "Yeah, well, duh. I meant, where do you live?"
scene ep2_bella_morning3 with dissolve
isa "About 15 minutes by car from campus."
scene ep2_bella_morning2 with dissolve
menu:
    "Ask for a ride" if True:
        mc "Would you mind giving me a ride back?"
        scene ep2_bella_morning3 with dissolve
        isa "Did your legs not regain their function to walk this morning?"
        scene ep2_bella_morning4 with dissolve
        if dtype > 0:
            $ RPisabella -= 1
            mc "Jeez...are we in a mood today?"
            isa "..."
        elif True:
            mc "Well, I just thought since we're going the same way..."
            mc "You know what? Never mind..."
    "Walk" if True:
        mc "Yikes... That's a long walk back."
        scene ep2_bella_morning3 with dissolve
        isa "If that's supposed to be reverse psychology to give you a lift..."
        isa "...it failed."
scene ep2_bella_morning2 with dissolve
mc "Thank you for breakfast...and everything else."
mc "If you don't mind...I'll grab a shower before I start walking back."
scene ep2_bella_morning_7 with dissolve
$ renpy.pause()
scene ep2_bella_morning_8a with dissolve
play sound "sound_effects/car_beep.mp3"
mc "Huh?"
scene ep2_bella_morning_9 with dissolve
isa "Get in."

scene ep2_carride_1 with wipeleft
mc "Thank you, for doing this for me."
scene ep2_carride_2 with dissolve
isa "Don't flatter yourself. I'm going to work."
scene ep2_carride_3 with dissolve
mc "Another day with the books, huh?"
isa "..."
mc "It will be the same for me."
mc "I have math class in the morning and gender studies in the afternoon."
scene ep2_carride_4 with dissolve
isa "You take Gender Studies?"
scene ep2_carride_3 with dissolve
mc "I do."
scene ep2_carride_4 with dissolve
$ guideSuggestedPage = 67
isa "What for?"
scene ep2_carride_3 with dissolve
menu:
    "Learn about women's issues" if True:
        mc "To learn about women's issues and more."
        scene ep2_carride_4 with dissolve
        isa "Hm...ironic."
        scene ep2_carride_3 with dissolve
        mc "How so?"
        scene ep2_carride_4 with dissolve
        isa "Because you are one of women's issues."
        scene ep2_carride_3 with dissolve
        mc "Haha! Thanks!"
        scene ep2_carride_5 with dissolve
        $ renpy.pause()
        $ RPisabella += 1
    "Easy credits" if True:
        if dtype > 0:
            mc "It's just a fuck off class for easy credits."
        elif True:
            mc "My friend Maya convinced me to take it."
            mc "It's supposedly easy credits."
        scene ep2_carride_4 with dissolve
        isa "Figures..."

scene ep2_carride_6 with wipeleft
isa "Off you go."
scene ep2_carride_7 with dissolve
menu:
    "Thank her" if True:
        $ ep2_triedToKissBella = False
        stop music fadeout 5
        mc "Thank you for the ride. I'll find a way to make it up to you."
        scene ep2_carride_8 with dissolve
        isa "Take care now."
    "Kiss her" if True:
        $ ep2_triedToKissBella = True
        $ bios_history_isabella +="I tried to kiss Bella in a sober state... It failed.\n\n"
        $ bios_name_isabella = True
        $ chat_new_bios = True
        mc "Thank you for the ride..."
        scene ep2_carride_10 with dissolve
        isa "Whoa! Slow down!"
        isa "I don't know what you think you're doing right now."
        isa "But no! We're not doing this."
        isa "I told you I was married."
        stop music fadeout 5
        mc "Oh yeah. I guess I forgot..."
        scene ep2_carride_8 with dissolve
        isa "Take care now."

label ep2_math_label:
play music "music/ep1/golden_alley.mp3"
scene ep2_math0 with wiperight
my "Where were you last night?"
scene ep2_math0b with dissolve
mc "Just...don't ask..."
scene ep2_math0 with dissolve
my "I was a bit worried..."
scene ep2_math0b with dissolve
mc "It was just some...pledge stuff..."
if ep2_textedMaya:
    scene ep2_math0 with dissolve
    my "And about the message you sent me..."
    scene ep2_math0b with dissolve
    mc "(Shit...what did I write her?)"
    mc "(It was something sweet or flirty I believe...)"
    mc "Yeah?"
    scene ep2_math0g with dissolve
    my "What does this mean?"
    scene ep2_math0b with dissolve
    mc "..."
mc "Hey, gimme a second I need to check up on Derek..."
scene ep2_math0j with dissolve
mc "Bro...are you ok?"
scene ep2_math0k with dissolve
de "Never been better!"
scene ep2_math0j with dissolve
mc "Really? Dude, I have such a fucking hangover today..."
scene ep2_math0k with dissolve
de "Oh, I don't get those."
de "I've never had one."
scene ep2_math0j with dissolve
mc "All right, good to see that you're ok."
mc "...but I think it's the first time I've seen you in a t-shirt."
scene ep2_math0o with dissolve
de "It's for gender class...Jade asked me to wear clothes last time."
scene ep2_math0j with dissolve
mc "Ah yeah! Let's chat later, I have some stuff to tell you."

scene ep2_math with dissolve
stu "Hey..."
mc "Yes?"
scene ep2_math1 with dissolve
stu "Cathy is still busy helping that student over there..."
stu "I need some help with this math problem. Would you help me?"
scene ep2_math3 with dissolve
menu:
    "Yes" if True:
        $ ep2HelpedStudent = True
        $ dk(-1)
        mc "Sure. Let me see."
        scene ep2_math4 with dissolve
        mc "Ah, there's your problem."
        stu "Oh! Is it like that?"
        stu "Thank you!"
        mc "Don't mention it."
    "No" if True:
        $ ep2HelpedStudent = False
        $ dk(1)
        if dtype > 0:
            mc "Nope, that's not my problem."
        elif True:
            mc "Sorry, but no. I'm not good at explaining math problems."
if ep2HelpedStudent:
    scene ep2_math6 with dissolve
    ca "Ok, now I'm free to help you. What do you need?"
    scene ep2_math7 with dissolve
    stu "Oh, I needed help with this problem, but that guy helped me with it already."
    ca "[name], helped you? That was nice of him. Let me have a look."
    if not minigames or failedEnglish == 0:
        scene ep2_math9 with dissolve
        ca "This is a really good solution..."
        ca "...in fact, it's excellent."
        ca "He did that, you say?"
        stu "Yeah."
        ca "Perhaps I should hire him as a teacher's assistant."
        stu "Haha!"
        $ bios_history_cathy +="I helped a student in math class. Cathy was pleasantly surprised.\n\n"
        $ bios_name_cathy = True
        $ chat_new_bios = True
    elif True:
        scene ep2_math9 with dissolve
        ca "Hm... It's nice that he tried to help you, but this isn't quite correct."
        ca "This is how it should be."
        $ bios_history_cathy +="I helped a student in math class, but my solution was incorrect.\n\n"
        $ bios_name_cathy = True
        $ chat_new_bios = True

if minigames:
    stop music fadeout 3
scene ep2_math13 with dissolve
mc "Let's do today's exercises..."
if not minigames:
    scene black with Fade(1.5, 1, 0.5)
    jump ep2_after_math_test
play music "music/ep3/sing_along_with_jim.mp3"
scene desk_bg_test with wipeleft
jump math101_test2

label ep2_after_math_test:
$ renpy.block_rollback()
if minigames:
    scene ep2_math_after with wiperight
    stop music fadeout 3
elif True:
    scene ep2_math_after with fade
my "Gah... I can't wait until this class is over and done with..."
if minigames:
    play music "music/ep1/golden_alley.mp3"
scene ep2_math_after1 with dissolve
mc "What's the matter?"
scene ep2_math_after2 with dissolve
my "I just really don't like math."
scene ep2_math_after1 with dissolve
mc "I thought you did ok on the test."
scene ep2_math_after2 with dissolve
my "Yeah... I did, but I just don't like it."
my "I just wanna skip these Gen Ed classes and start learning what I really came here for."
scene ep2_math_after1 with dissolve
mc "I heard that a lot of students drop out early because of the feeling you have right now."
scene ep2_math_after3 with dissolve
mc "Look at it this way..."
mc "Each day you're here, you're one day closer to completing the class."
mc "After that, you won't have to retake it..."
mc "You know... Unless you're someone like Dawe."

play sound "sound_effects/table_slam.mp3"
scene ep2_math_after5 with vpunch
dw "FUCKING SHIT! Algebra sucks cock!"
scene ep2_math_after6 with dissolve
ca "Language, Dawe!"
scene ep2_math_after7 with dissolve
dw "I have no fucking use for this shit in my life!"
scene ep2_math_after8 with dissolve
an "I'm with Dawe! Our phones have calculators! No one does math on paper anymore!"
scene ep2_math_after6 with dissolve
ca "(Again with his phone...)"
ca "Remember what we talked about last Friday?"
scene ep2_math_after11 with dissolve
dw "Yes..."
ca "Let me show you how you solve that problem."
$ guideSuggestedPage = 68
scene ep2_math_after13 with dissolve
my "Yeah, that's all the motivation I need to take this class seriously."
scene ep2_math_after14 with dissolve
my "..."
mc "What's wrong?"
scene ep2_math_after15 with dissolve
my "I have a feeling that Derek will be the new Dawe next year."
my "Unless he cheats, like he always does..."
mc "You know about that, huh?"
scene ep2_math_after17 with dissolve
my "Sadly... I wouldn't turn him in for it, you know...because I love him."
my "But I've been trying to make him understand how it may end up hurting him in the long run."
my "He just shrugs it off..."
scene ep2_math_after19 with dissolve
menu:
    "Sympathize" if True:
        if dtype > 0:
            mc "He means a lot to you... So, that must really suck..."
        elif True:
            mc "I understand that you care a lot for him..."
            mc "It's not fun feeling helpless."
    "It's his choice" if True:
        mc "He knows what he's doing and what the consequences are."
        mc "Sometimes learning things the hard way is the only way that works."
scene ep2_math_after20 with dissolve
my "You don't have any siblings, right?"
scene ep2_math_after21 with dissolve
mc "Nope, just a dad."
scene ep2_math_after20 with dissolve
my "No...mother?"
scene ep2_math_after21 with dissolve
mc "She passed away during childbirth."
scene ep2_math_after24 with dissolve
my "I'm sorry..."
scene ep2_math_after21 with dissolve
mc "You don't have to say that, I've lived my entire life without knowing her."
scene ep2_math_after20 with dissolve
my "Anyway...I care about my brother. It hurts when he does stupid things."
scene ep2_math_after21 with dissolve
if dtype > 0:
    mc "You do stupid shit, too."
elif True:
    mc "You do stupid things, too."
scene ep2_math_after17 with dissolve
my "I know what you're getting at..."
scene ep2_math_after21 with dissolve
mc "Exactly. The things you submit to with the HOTs aren't the best for you."
mc "You know the consequences and still do it."
scene ep2_math_after20 with dissolve
my "Yeah, I can't argue that. You got me."
scene ep2_math_after21 with dissolve
mc "It wasn't about getting you."
mc "But what do you think Derek would say if he knew what you did for them?"
scene ep2_math_after15 with dissolve
my "He would feel just the same as I do for him..."
my "He would hate it and want me to stop."
scene ep2_math_after21 with dissolve
mc "And would you?"
scene ep2_math_after20 with dissolve
my "No... I can't..."
scene ep2_math_after21 with dissolve
mc "There you have it. You two are more alike than you think."
mc "Only that you don't walk around nude outdoors...right?"
scene ep2_math_after36 with dissolve
stop music fadeout 5
my "Haha! Right!"
my "Thank you. That strangely makes me feel a little bit better."
if not ep2SageGuitarTeacher:
    jump ep2_after_sage_guitar_label
label ep2_sage_guitar_label:
scene ep2_sage_guitar with fade
play sound "sound_effects/door_knock.mp3"
play music "music/ep2/simple_ballad.mp3"
sa "Yeah?"
mc "Hey! You busy?"
scene ep2_sage_guitar1 with dissolve
sa "No, I'm just studying a bit."
scene ep2_sage_guitar2 with dissolve
sa "You brought your guitar?"
scene ep2_sage_guitar4 with dissolve
mc "Yeah, I have a break between classes and I thought this was a great time to teach you how to play."
scene ep2_sage_guitar5 with dissolve
sa "Now? Um..."
scene ep2_sage_guitar4 with dissolve
mc "You can't right now?"
scene ep2_sage_guitar5 with dissolve
sa "I don't know...I..."
sa "I didn't think we would do it this soon."
scene ep2_sage_guitar4 with dissolve
mc "It's scary starting new things, but let's take it slow the first time."
mc "Do you know anything about playing the guitar?"
scene ep2_sage_guitar9 with dissolve
sa "I know a chord or two."
scene ep2_sage_guitar10 with dissolve
mc "Show me."
scene ep2_sage_guitar11 with dissolve
sa "I think this is a G major."
scene ep2_sage_guitar12b with dissolve
mc "(Ok, that's the cheater's G major...)"
menu:
    "Correct her" if True:
        if dtype > 0:
            mc "No, that's not a proper G major."
            scene ep2_sage_guitar12b2 with dissolve
            sa "Fuck... See, I knew I sucked."
        elif True:
            mc "You're correct. It's indeed a G chord, but it's not quite the proper chord."
            scene ep2_sage_guitar12c with dissolve
            sa "All right..."
    "Wait until she's done" if True:
        mc "Ok, what else do you know?"
scene ep2_sage_guitar13 with dissolve
sa "Hm..."
scene ep2_sage_guitar13b with dissolve
mc "(...)"
mc "(Fuck...focus...)"
scene ep2_sage_guitar13c with dissolve
sa "..."
scene ep2_sage_guitar13d with dissolve
sa "This is an E major... I think."
scene ep2_sage_guitar14 with dissolve
mc "(No. That's an A major. Her fingering is good.)"
menu:
    "Correct her" if True:
        if dtype >  0:
            mc "Nope, it's actually an A major."
            scene ep2_sage_guitar15 with dissolve
            sa "Shit..."
        elif True:
            mc "I'm impressed. That's a proper A major."
            scene ep2_sage_guitar16 with dissolve
            sa "Oh yeah! Damn, I should have remembered that it was an A and not an E."
        scene ep2_sage_guitar14 with dissolve
        mc "Hey, that's ok. Your fingering is very good."
        scene ep2_sage_guitar18 with dissolve
        sa "My {i}fingering{/i} is awesome."
        sa "How's yours?"
        scene ep2_sage_guitar19 with dissolve
        menu:
            "Flirt" if True:
                $ RPsage += 1
                mc "Maybe I'll show you afterwards."
                $ bios_history_sage +="I flirted with Sage during our music lesson.\n\n"
                $ bios_name_sage = True
                $ chat_new_bios = True
                scene ep2_sage_guitar18 with dissolve
                sa "Haha, deal."
            "Stay focused" if True:
                mc "Sage, focus."
    "Wait until she's done" if True:
        mc "Mhm. Continue."
scene ep2_sage_guitar16 with dissolve
sa "Those are the only chords I know."
scene ep2_sage_guitar14 with dissolve
mc "Ok, it's definitely a start."
mc "To sum up, your G major needs some work and you need to learn the names of the chords."
mc "But honestly, I never learned to play with the help of a teacher."
mc "All that really matters is that you're enjoying it and that the music sounds good to you."
mc "We do enough studying for classes, let's just keep things practical when we play guitar."
mc "You will still pick up the theory along the way."
scene ep2_sage_guitar16 with dissolve
sa "I like that approach."
sa "So, what's wrong with my G major?"
scene ep2_sage_guitar14 with dissolve
mc "You just need some extra fingers and you're good to go."
scene ep2_sage_guitar14b with dissolve
sa "*{i}Giggles{/i}*"
mc "Haha, that wasn't a sexual thing."
scene ep2_sage_guitar16 with dissolve
sa "Will you help me with my fingers?"
sa "Where am I supposed to put them?"
scene ep2_sage_guitar11 with dissolve
mc "First, put your index finger on the second fret of the A string."
sa "..."
sa "What?"
sa "Show me while I hold the guitar."
scene ep2_sage_guitar24 with dissolve
mc "It's...a...there."
sa "What?"
mc "Here!"
scene ep2_sage_guitar27 with dissolve
sa "Haha! What are you doing?"
scene ep2_sage_guitar28 with dissolve
mc "It's hard to show you from the front."
scene ep2_sage_guitar27 with dissolve
sa "Sure. I bet that's why."
scene ep2_sage_guitar30 with dissolve
mc "This is how you do it."
sa "Oh. I can do that."
scene ep2_sage_guitar31 with dissolve
sa "Like this?"
mc "There you go."
sa "Yes! That's it."
mc "Great job."
scene ep2_sage_guitar33 with dissolve
sa "Hey, [name]...?"
scene ep2_sage_guitar35 with dissolve
mc "Yeah?"
scene ep2_sage_guitar33 with dissolve
sa "I think your major D is poking me."
scene ep2_sage_guitar37 with dissolve
menu:
    "Kiss her" if True:
        $ ep2QuinnSawYouAndSage = True
        $ bios_history_sage +="I kissed Sage during our music lesson and it got very interesting after that...\n\n"
        $ bios_name_sage = True
        $ chat_new_bios = True
        stop music fadeout 3
        label ep2_sage_lewd_label:
        if _in_replay:
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
            if persistent.ep2_lewd_sage_full:
                $ ep2_kissedSage = True
            elif True:
                $ ep2_kissedSage = False
        hide screen phone_screen
        scene ep2_sage_guitar38 with dissolve
        sa "Hm!!!"
        play music "music/ep1/slow_day_blues.mp3"
        scene anim_sage_kiss2_ep2 with dissolve:
            size (config.screen_width, config.screen_height)
        pause
        scene ep2_sage_guitar40 with dissolve
        sa "Um...what are we doing?"
        scene ep2_sage_guitar41 with dissolve
        if ep2_kissedSage:
            mc "Picking up from where we left off at the party."
            scene ep2_sage_guitar40 with dissolve
            sa "I think we left off a little bit later, though."
            sa "Kiss me again."
        elif True:
            mc "I don't know..."
            mc "I just felt like kissing you."
            scene ep2_sage_guitar40 with dissolve
            sa "Do it again..."
        scene anim_sage_kiss2_ep2 with dissolve:
            size (config.screen_width, config.screen_height)
        pause
        scene anim_sage_kiss3_ep2 with dissolve:
            size (config.screen_width, config.screen_height)
        pause
        scene ep2_sage_guitar42 with dissolve
        sa "You really like my tits, huh?"
        sa "I saw you looking at them before, you know."
        scene ep2_sage_guitar40 with dissolve
        mc "You did?"
        scene ep2_sage_guitar42 with dissolve
        sa "Haha, yeah. Don't you think girls notice that?"
        sa "Tell me...what do you think of them?"
        scene ep2_sage_guitar44 with dissolve
        mc "They are so big and soft..."
        sa "Soft!? That's not a compliment..."
        mc "Of course it is!"
        sa "No, soft means saggy."
        scene ep2_sage_guitar41 with dissolve
        mc "That's not what I meant."
        mc "I meant that they feel so soft and amazing..."
        mc "...that I can't help wondering how they would feel against my..."
        mc "...major D."
        scene ep2_sage_guitar51 with dissolve
        sa "You mean like this?"
        scene ep2_sage_guitar52 with dissolve
        mc "...kinda."
        scene ep2_sage_guitar53 with dissolve
        sa "Surely you don't mean without clothes?"
        scene ep2_sage_guitar52 with dissolve
        if dtype > 0:
            mc "Would you?"
        elif True:
            mc "..."
        scene ep2_sage_guitar55 with dissolve
        sa "(If it's ok that Chad does it...)"
        sa "(Why wouldn't it be ok if I did it, too?)"
        sa "(Yes... That will teach him.)"
        scene ep2_sage_guitar53 with dissolve
        sa "Close your eyes, [mc_sage]."
        scene black with fade
        sa "Are they closed?"
        mc "Yeah."
        sa "Keep them closed..."
        play sound "sound_effects/zipper.mp3"
        mc "(She's taking off my pants.)"
        play sound "sound_effects/clothes.mp3"
        sa "Wow..."
        sa "You weren't lying about the major D..."
        sa "It's fucking huge!"
        sa "..."
        sa "So...how does that feel?"
        mc "Wha-? Oh my God..."
        mc "(She's squeezing her tits over my cock...)"
        mc "It feels so fucking good..."
        mc "Just like what I said...so soft..."
        mc "In the best way possible."
        mc "Can I open my eyes, already?"
        sa "Mhm..."
        scene anim_sage_boobjob3_ep2 with dissolve:
            size (config.screen_width, config.screen_height)
        mc "(Wow!!!)"
        pause
        sa "Do you like it, [mc_sage]?"
        mc "Yeah, this is so sexy..."
        sa "How about this...?"
        scene anim_sage_boobjob1_ep2 with dissolve:
            size (config.screen_width, config.screen_height)
        pause
        mc "Amazing... Keep going..."
        if not renpy.variant("pc"):
            jump ep2_sage_lewd2_label
        if _in_replay and not persistent.ep2_lewd_sage_full:
            jump ep2_sage_lewd2_label
        elif not ep2_kissedSage:
            label ep2_sage_lewd2_label:
            sa "I've been missing someone to have fun with..."
            mc "We can have a lot of fun together, if you want to."
            sa "(Perfect...)"
            sa "Would you like it better if I removed my top?"
            if dtype > 0:
                mc "Yeah...show me your tits."
            elif True:
                mc "Yes, definitely."
            stop music
            scene ep2_sage_guitar_quinn
            qu "Sage, do you have a min-"
            scene ep2_sage_guitar_quinn1 with dissolve
            qu "No fucking way!"
            sa "Shit!"
            scene ep2_sage_guitar_quinn4 with dissolve
            qu "Are you fucking perv boy?"
            scene ep2_sage_guitar_quinn5 with dissolve
            mc "I'm leaving..."
            scene ep2_sage_guitar_quinn6 with dissolve
            qu "I see you."
            $ renpy.end_replay()
            $ persistent.ep2_lewd_sage_half = True
            $ calcScenes()
            $ bios_history_quinn +="Quinn caught me and Sage being intimate...\n\n"
            $ bios_name_quinn = True
            $ chat_new_bios = True
            show screen phone_screen
            jump ep2_after_sage_guitar_label

        sa "Would you like it better if I removed my top?"
        if dtype > 0:
            mc "Yeah...show me your tits."
        elif True:
            mc "Yes, definitely."

        scene ep2_sage_guitar56 with dissolve
        sa "How do I look?"
        scene anim_sage_boobjob2_ep2 with dissolve:
            size (config.screen_width, config.screen_height)
        if dtype > 0:
            mc "You're so fucking sexy..."
        elif True:
            mc "Wow..."
        sa "Feels better, huh?"
        pause
        scene anim_sage_boobjob4_ep2 with dissolve:
            size (config.screen_width, config.screen_height)
        sa "Fuck...I wonder what you taste like..."
        mc "You wanna try?"
        sa "Mmm..."
        sa "No...not today..."
        sa "Just a lick..."
        pause
        scene ep2_sage_guitar58 with dissolve
        sa "What are you waiting for?"
        sa "Come here and fuck my tits, [mc_sage]..."
        scene anim_sage_boobjob5_ep2 with dissolve:
            size (config.screen_width, config.screen_height)
        sa "Fuck them..."
        sa "I want you to cum all over my tits, [mc_sage]."
        pause
        mc "Shit...I'm...close..."
        sa "Cum! Cum all over my big tits!"
        scene bg anim_sage_cum_ep2 movie with dissolve:
            size (config.screen_width, config.screen_height)
        mc "Holy fuck!"
        sa "Mmm..."
        sa "Wow, that's a lot of cum!"
        mc "I've never done that before..."
        mc "That was so hot!"
        scene ep2_sage_guitar59 with dissolve
        sa "You're as crazy as I am...aren't you?"
        scene ep2_sage_guitar61 with dissolve
        mc "How do you mean?"
        scene ep2_sage_guitar59 with dissolve
        sa "You know, about trying new stuff..."
        sa "...sexually."
        scene ep2_sage_guitar61 with dissolve
        mc "We can try anything you want."
        sa "(Perfect...)"
        $ renpy.end_replay()
        $ persistent.ep2_lewd_sage_half = True
        $ persistent.ep2_lewd_sage_full = True
        $ calcScenes()
        stop music
        scene ep2_sage_guitar_quinn
        qu "Sage, do you have a min-"
        scene ep2_sage_guitar_quinn1 with dissolve
        qu "No fucking way!"
        sa "Shit!"
        scene ep2_sage_guitar_quinn4 with dissolve
        qu "Are you fucking perv boy?"
        scene ep2_sage_guitar_quinn5 with dissolve
        mc "I'm leaving..."
        scene ep2_sage_guitar_quinn6 with dissolve
        qu "I see you."
        $ bios_history_quinn +="Quinn caught me and Sage being intimate...\n\n"
        $ bios_name_quinn = True
        $ chat_new_bios = True
        show screen phone_screen
        jump ep2_after_sage_guitar_label
    "Don't take it further" if True:
        $ ep2QuinnSawYouAndSage = False
        $ bios_history_sage +="I didn't kiss Sage during our music lesson.\n\n"
        $ bios_name_sage = True
        $ chat_new_bios = True
        scene ep2_sage_guitar35 with dissolve
        mc "Haha! Stop it."
        scene ep2_sage_guitar33b with dissolve
        sa "Thanks for teaching me..."
        scene ep2_sage_guitar35 with dissolve
        mc "No worries."
        mc "We can continue this at another time, maybe?"
        scene ep2_sage_guitar33b with dissolve
        sa "Absolutely."
        scene ep2_sage_guitar35 with dissolve
        mc "I'm off to my afternoon class."
        scene ep2_sage_guitar33b with dissolve
        sa "Talk to you later, then."

label ep2_after_sage_guitar_label:
play music "music/ep1/art_nouveau.mp3"
scene ep2_fem_class with wiperight
mc "So, you have no idea what they are planning for tonight?"
scene ep2_fem_classb with dissolve
de "Nope, not a clue. But it seems big, because they're all excited for it."
scene ep2_fem_class1 with dissolve
ja "Ah, Derek. How nice to see you in clothes for a change."
scene ep2_fem_class1b with dissolve
de "Yeah, I remembered what you said and you were right."
scene ep2_fem_class1c with dissolve
de "I was being indecent. It's just that clothes are so restricting to me."
de "I feel much more like myself without them."
scene ep2_fem_class3 with dissolve
ja "Derek... Your shirt is sending out a very strong sexist statement."
ja "Perhaps you should have chosen a more appropriate piece of attire for this class?"
ja "...or in general?"
scene ep2_fem_class1d with dissolve
de "Men can wear purple, too."
scene ep2_fem_class6 with dissolve
de "Now who's the sexist...?"
ja "*{i}Sigh{/i}*"
scene ep2_fem_class8 with dissolve
ja "Good afternoon, class."
ja "For today, I want you all to engage in discussion about a topic that's close to your heart."
scene ep2_fem_class9 with dissolve
ja "As an opponent, I want you to come up with arguments that challenge your partner..."
ja "...even if you agree with what they are saying."
scene ep2_fem_class8 with dissolve
ja "Don't be shy, I want to hear interesting and passionate discussions..."
if minigames:
    stop music fadeout 3
ja "...but please keep it civil."
scene ep2_gender with dissolve
mc "Hey! Do you wanna pair up?"
if not minigames:
    jump ep2_after_gender_test2
$ guideSuggestedPage = 69
jump gender101_test2
label ep2_after_gender_test2:
if minigames:
    play music "music/ep1/art_nouveau.mp3"
    scene ep2_gender_after with dissolve
elif True:
    scene ep2_gender_after with Fade(1.5, 1, 0.5)
ja "[name]... May I have a word with you after class?"
scene ep2_gender_after1 with dissolve
mc "Um...sure."
mc "(What does she want with me?)"

scene ep2_gender_after2 with dissolve
wen "No! You are wrong! Meat {b}is{/b} murder!"
scene ep2_gender_after3 with dissolve
de "You just told me you eat fish! That would be murder, too!"
scene ep2_gender_after2 with dissolve
wen "No, it isn't! Fishes don't suffer!"
scene ep2_gender_after3 with dissolve
de "You can't just choose which animal suffers or not, Wendy!"
de "Either it's all wrong or nothing is!"
scene ep2_gender_after6 with dissolve
wen "I can too! I read about fishes online!"
wen "As long as I don't eat meat, I can have a clear conscience."
wen "So, I can and I will eat everything else!"
scene ep2_gender_after3 with dissolve
de "The only thing you won't eat is \"less\"."
scene ep2_gender_after8 with dissolve
ja "Derek, remember this is a class where we discuss sensitive issues..."
ja "...NOT a roast."
stop music fadeout 3
scene ep2_gender_after9 with dissolve
de "Easy credits, my ass... My ears are bleeding."

scene ep2_gender_after10 with dissolve
mc "You wanted to have a word with me?"
play music "music/ep2/jingle.mp3"
scene ep2_gender_after11 with dissolve
$ guideSuggestedPage = 70
ja "Ah yes, [name]."
ja "I've been paying some extra attention to you..."
ja "What do you think of this class this far?"
scene ep2_gender_after13 with dissolve
menu:
    "Positive response" if True:
        if dtype > 0:
            mc "It's ok. I've had worse."
            scene ep2_gender_after14 with dissolve
            ja "Haha, you've had worse, you say?"
            scene ep2_gender_after11 with dissolve
        elif True:
            mc "It's interesting."
            scene ep2_gender_after11 with dissolve
            ja "That's good."
        ja "I overheard you and your study partner's discussion today."
        scene ep2_gender_after13 with dissolve
        mc "I was trying to start a good discussion but it turned into something else entirely."
    "Negative response" if True:
        if dtype > 0:
            mc "Honestly, it stinks."
        elif True:
            mc "Yeah...this class is not for me."
            mc "I'm beginning to feel that it was a mistake signing up for it."
        scene ep2_gender_after17 with dissolve
        ja "May I ask why?"
        scene ep2_gender_after13 with dissolve
        mc "These \"discussions\" we have are pretty one-sided."
        scene ep2_gender_after11 with dissolve
        ja "So I've noticed."
scene ep2_gender_after17 with dissolve
ja "That's twice in a row now."
scene ep2_gender_after19 with dissolve
mc "Sorry, I can try to do better next time."
scene ep2_gender_after20 with dissolve
ja "Oh, stop it. I wasn't looking for an apology."
ja "Quite the contrary, I wanted to check if you're getting any value from attending this class."
scene ep2_gender_after28 with dissolve
ja "Maybe there's an {i}itch{/i} to get something off your chest that your study partners haven't been able to {i}scratch{/i}."
scene ep2_gender_after22 with dissolve
mc "(Is she flirting...or is this just about the class?)"
if dtype > 0:
    mc "Sure...it would be nice if I got to talk, too."
elif True:
    mc "I wouldn't mind being allowed to contribute more to the discussion, if that's what you're getting at."
scene ep2_gender_after28 with dissolve
ja "Precisely."
scene ep2_gender_after22 with dissolve
mc "But you must feel the same thing, no?"
scene ep2_gender_after24 with dissolve
ja "Me?"
scene ep2_gender_after23 with dissolve
mc "Yeah, I can imagine that you would like to discuss things, too."
mc "But you're kind of like me in this class. Just someone who listens."
ja "(It's been years since someone wanted to listen to me talk...)"
scene ep2_gender_after24 with dissolve
ja "Well, I'm your teacher. It's my job."
scene ep2_gender_after23 with dissolve
mc "So, you never want to join in on the discussion?"
scene ep2_gender_after24 with dissolve
ja "Of course I would..."
ja "I'll tell you what..."
scene ep2_gender_after28 with dissolve
ja "If there's ever an odd couple in the class you and I could pair up and have a good..."
scene ep2_gender_after20 with dissolve
ja "...back and forth."
scene ep2_gender_after30 with dissolve
menu:
    "Flirt" if True:
        $ ep2_flirtedJade = True
        mc "Yes...a back and forth...and back and forth."
        scene ep2_gender_after29 with dissolve
        $ renpy.pause()
    "Don't flirt" if True:
        $ ep2_flirtedJade = False
        mc "...I guess."

scene ep2_gender_after32 with dissolve
ja "Shall we?"
scene ep2_gender_after33 with dissolve
$ renpy.pause()
scene ep2_gender_after34 with dissolve
$ renpy.pause()
scene ep2_gender_after35 with dissolve
ja "(Fuck...did I just do that?)"
ja "(That's so unprofessional...)"
stop music fadeout 3
scene ep2_gender_after36 with dissolve
ja "(...but if he can do this to me...so can I.)"
$ bios_history_jade +="Jade is definitely flirting with me... What do I do?\n\n"
$ bios_name_jade = True
$ chat_new_bios = True

label ep2_jill_piano_label:
play music "music/ep2/reaching_the_sky.mp3"
scene ep2_jill_piano with wiperight
"*{i}Piano music plays{/i}*"
mc "(...)"
mc "(Where's that wonderful melody coming from?)"
mc "(The auditorium...why wasn't this place part of the campus tour?)"
scene ep2_jill_piano1 with dissolve
mc "(That's...her.)"
mc "(Jill...)"
mc "(Her technique is amazing...)"
scene ep2_jill_piano3 with dissolve
$ renpy.pause(13)
show text "Click to continue" with dissolve:
    xpos 0.5
    ypos 0.9
$ renpy.pause(2)
hide text "Click to continue" with dissolve
$ renpy.pause()
stop music fadeout 3
scene ep2_jill_piano4 with dissolve
$ renpy.sound.play("sound_effects/applaud_one.mp3", channel="sfx1", loop=False)
"*{i}Applaud{/i}*"
mc "Wow...just wow!"
ji "Huh?"
scene ep2_jill_piano5 with dissolve
play music "music/ep2/winter.mp3"
ji "[name]!? What are you doing here?"
scene ep2_jill_piano6 with dissolve
mc "I was passing by when I heard you play."
scene ep2_jill_piano6b with dissolve
ji "Oh... I..."
ji "Do you like music?"
scene ep2_jill_piano6 with dissolve
ji "..."
scene ep2_jill_piano6b with dissolve
ji "That's like the stupidest question ever..."
ji "I'm a bit flustered."
ji "You caught me at a very personal time..."
scene ep2_jill_piano6 with dissolve
if dtype > 0:
    mc "Sorry, I didn't mean to make you feel weird and stuff."
elif True:
    mc "Oh, I'm so sorry. I didn't mean to bother you..."
mc "I just couldn't help myself..."
mc "I'm a real sucker for melodies."
ji "..."
scene ep2_jill_piano6c with dissolve
ji "Me too."
ji "So...you really liked it?"
scene ep2_jill_piano6 with dissolve
mc "Totally! You're so skilled."
mc "I can tell you've been practicing for a long time."
scene ep2_jill_piano6b with dissolve
ji "Yes... I've played the piano ever since I was eight years old."
scene ep2_jill_piano6 with dissolve
mc "I never had the chance to play the piano..."
mc "...but I've played guitar since I was 12 years old."
mc "I mostly play acoustic stuff...like...songs that are played on the radio."
mc "And I've written some songs myself, too."
scene ep2_jill_piano6b with dissolve
ji "Uh-huh."
scene ep2_jill_piano6 with dissolve
ji "..."
mc "(Hm...I think she's still uncomfortable...)"
menu:
    "Ask her about the song" if True:
        mc "That song you just played..."
        mc "...what was it?"
        scene ep2_jill_piano6d with dissolve
        ji "Oh...it's..."
        scene ep2_jill_piano6b with dissolve
        ji "Just a song."
        scene ep2_jill_piano6 with dissolve
        mc "Ok...I've never heard it before."
    "Apologize and leave" if True:
        mc "Sorry for interrupting your practice."
        mc "...but thanks for the music."
        if dtype > 0:
            mc "It sounded awesome."
        elif True:
            mc "It was beautiful."

scene ep2_jill_piano6e with dissolve
mc "And I'm making you uncomfortable. I'm leaving."
scene ep2_jill_piano20 with dissolve
mc "(Was that really Jill in there?)"
mc "(I mean...sure I get it...)"
mc "(I go to my special place in my mind when I play the guitar...)"
mc "(...but it still felt like something was off.)"
stop music fadeout 3
play sound "sound_effects/cellphone.mp3"
"*{i}Cellphone rings{/i}*"
scene ep2_jill_piano21 with dissolve
de "[mc_de_up]! It's starting!"
de "You need to come here! Now!"
scene ep2_jill_piano22 with dissolve
mc "What is it?"
scene ep2_jill_piano21 with dissolve
de "Hell Week..."
mc "..."
scene ep2_jill_piano22 with dissolve
mc "I'll be right there."
$ bios_history_jill +="Jill plays the piano, beautifully at that! But she seemed a bit off when she realized I saw her playing it.\n\n"
$ bios_name_jill = True
$ chat_new_bios = True

label ep2_ending_label:
hide screen phone_screen
scene ep2_ending with fade
play music "music/ep2/metal2.mp3"
tm "Maggot brothers! The time has come to prove your worth."
tm "You don't become a brother overnight and this weekend was just a simple warm up."
scene ep2_ending1 with dissolve
tm "One week."
tm "One week is what you must endure. But not just any week."
scene ep2_ending with dissolve
tm "Dear brothers, it's that time of year again."
tm "It's time for-"
scene ep2_ending3 with dissolve
dikcs "Hell Week!"
scene ep2_ending1 with dissolve
tm "One week of trials to test every fiber of your beings."
tm "One week to test if you and your maggot brother are worthy to join the true brotherhood."
scene ep2_ending6 with dissolve
rs "If you can't prove to us that you and your maggot brother can work together, fighting alongside, enduring hell..."
rs "...we can't expect you to live by the DIK code."
scene ep2_ending3 with dissolve
dikcs "Family comes first!"
scene ep2_ending with dissolve
tm "And now it's time for the grand reveal!"
tm "Rusty!"
scene ep2_ending9 with dissolve
rs "Let me proudly present..."
play sound "sound_effects/cloth.mp3"
scene ep2_ending10 with dissolve
rs "THE DEVIL'S PLEDGE BOARD!"
scene ep2_ending11 with dissolve
de "HOLY FUCK!"
mc "We're going to do all that in one week?"
scene black
$ renpy.pause(1)
$ updateDikScore()
$ guideSuggestedPage = 71

if steamAchievements and persistent.vault2 and not config.console and not config.developer:
    $ achievement.grant("VAULTLOOTER2")
    init:
        $ achievement.register("VAULTLOOTER2")
    $ achievement.Sync()
if steamAchievements and persistent.vault1 and persistent.vault2 and persistent.vault3 and persistent.vault4 and not config.console and not config.developer:
    $ achievement.grant("VAULTLOOTER")
    init:
        $ achievement.register("VAULTLOOTER")
    $ achievement.Sync()
if steamAchievements and not config.console and not config.developer:
    $ achievement.grant("EPISODE2")
    init:
        $ achievement.register("EPISODE2")
    $ achievement.Sync()
if persistent.current_episode == 2:
    scene ep2_episode_end
    $ renpy.pause()
elif True:
    scene ep2_episode_endb
    $ renpy.pause()
$ calcRenders()
scene black with fade
stop music fadeout 3
show screen scoremsg
$ renpy.pause(3)
hide screen scoremsg

play music "music/ep2/reaching_the_sky.mp3"
$ episodeIsEnding = True
show screen endingScreen with dissolve
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
    $ josyScore = RPjosy / -1.0
if RPmaya >= 0:
    $ mayaScore = RPmaya / 21.0
elif True:
    $ mayaScore = RPmaya / -5.0
if RPsage >=0:
    $ sageScore = RPsage / 11.0
elif True:
    $ sageScore = RPsage / -2.0
if RPisabella >= 0:
    $ isabellaScore = RPisabella / 4.0
elif True:
    $ isabellaScore = RPisabella / -5.0
if RPjill >= 0:
    $ jillScore = RPjill / 3.0
elif True:
    $ jillScore = RPjill / -2.0
$ episodeContLabel = "ep2_ending_label2"
jump ep2_report_jill_label

label ep2EndLabel:
stop music fadeout 3
scene black
$ renpy.pause(1.0)
$ renpy.sound.play("sound_effects/crickets.mp3", channel="sfx1", loop=True)
scene ep2_ending12 with fade
$ renpy.pause()
scene ep2_ending13 with dissolve
play sound "sound_effects/door_knock.mp3"
"*{i}Door knocking{/i}*"
play sound "sound_effects/running.mp3"
$ renpy.pause(1)
scene ep2_ending14 with dissolve
ch "Hello?"
scene ep2_ending15 with dissolve
"{i}Is this the secret you're hiding?{/i}"
ch "No...no..."
scene ep2_ending16 with dissolve
ch "..."
ch "[name]..."
$ renpy.music.stop(channel="sfx1", fadeout=0)
play sound "sound_effects/whoosh_2.mp3"
scene black
$ renpy.pause(2)

if renpy.loadable("update3.rpyc"):
    jump startUpdate3
elif True:
    play music "music/patched/track_previous.mp3"
    jump endOfVersion2

label endOfVersion2:
scene black
show spr_bg
show spr_mid
show spr_top
show massive_diks
$ renpy.pause()
hide massive_diks
show acknowledgements
$ renpy.pause()
hide acknowledgements
show music_credits
$ renpy.pause()
hide music_credits
show version_end
$ renpy.pause()
hide version_end
scene episode3_polls
$ renpy.pause()
scene patreon_promo
$ renpy.pause()
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
