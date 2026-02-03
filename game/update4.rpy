label startUpdate4:
jump header_ep4_label
label previousEp4Label:
play music "music/patched/track_previous.mp3"
scene black
$ renpy.pause(2)
hide screen phone_screen
$ previousEpLabel = "startUpdate4b"
$ guideSuggestedPage = 88
show previously_ol
$ renpy.pause()
hide previously_ol
show screen previous_screen
scene ep3_intro9
ja "Who have you fucked, then? Tell me!"
scene ep3_intro10b
sb "Three..."
scene ep3_intro9
ja "Three...students?"
play sound "sound_effects/whoosh.mp3"
scene ep3_intro15
show ep3_intro15_fr
$ renpy.pause(.5)
scene ep3_list12 with wipeleft
rs "Hell Week ends at 8 p.m. on Saturday."
rs "That means you must complete more than 2 tasks per day..."
scene ep3_dik_board
mc "Look at that pledge board..."
mc "...we've barely made a dent!"

if ep3_chad_fight_won:
    scene ep3_office_chad12b with wipeleft
elif True:
    scene ep3_office_chad12 with wipeleft
ch "Fine, I hit him. I'm sorry."
scene ep3_office_chad13
sb "You can't expect to keep your position as the president of the tri-alphas after this."

if ep3_chad_fight_won:
    scene ep3_jocks_talk23b
elif True:
    scene ep3_jocks_talk23
ch "...you need to get yourselves a new president."
if ep3_chad_fight_won:
    scene ep3_jocks_talk29b
elif True:
    scene ep3_jocks_talk29
an "Hey, that's you, Dawe."
scene ep3_jocks_talk18b
dw "Is that my Arieth?"
scene ep3_jocks_talk20
dw "Has she fucked all of them?"

scene ep3_isa_jill15 with wiperight
isa "I wanted to make sure if he was good enough for you..."
if ep3_bella_came_around:
    isa "[name] is a way better choice than Tybalt."
elif True:
    isa "[name] is not a good choice..."
scene ep3_mansion81
mc "Would you like to go out on a date with me?"
scene ep3_mansion83 with dissolve
ji "I'd love that."
if ep3_BellaLewd:
    if ep3_mansionHelmet:
        scene ep3_isa_confront33b with dissolve
    elif True:
        scene ep3_isa_confront33 with dissolve
    mc "When did you come around about me!?"
    scene anim_bella_kiss_ep3 with dissolve
    $ renpy.pause()
    scene ep3_isa_confront63
    isa "I can't."

if not rejectedSage and ep2SageGuitarTeacher:
    scene ep3_sage_guitar46 with wipeleft
    sa "This is what I wanted..."
    sa "To feel sexual..."
    if sageControlEp3:
        scene ep3_sage_guitar65
        mc "I can make you feel that anytime you want..."
        scene ep3_sage_guitar66
    elif True:
        scene ep3_sage_guitar68 with dissolve
        mc "I can make you feel that anytime you want..."
        scene ep3_sage_guitar67 with dissolve
    sa "Like a fuck buddy?"
    sa "I'll think about it..."

scene ep3_hot_week19 with wiperight
qu "So, girls...are you interested?"
scene ep3_hot_week18
mn "Free tuition? Sign me up."
scene ep3_hot_week24
my "What do we have to do, exactly?"
scene ep3_quri8
ri "I was relaxed, until you started bringing in more girls."
scene ep3_quri7
qu "It's called expanding, Riona."
scene ep3_quri8
ri "Not when we can't handle it!"
scene ep3_quri17
ri "And I'm still fucking concerned about who's been spreading that HOTs give free tuition."

scene ep3_maya_morning29 with wipeleft
my "I'm not going to pledge the HOTs."
my "I'll have to survive college without that tuition."
if ep3_mayaOfferedHelp:
    scene ep3_maya_morning29c
    mc "What if I helped you?"
    if ep3_mayaLewd:
        scene ep3_maya_lewd14
        mc "What parts of the list do you want me to help you with?"
        scene ep3_maya_lewd15
        my "No matter the tasks on that list..."
        my "I'm doing them."
        scene ep3_maya_lewd65
        my "That was my first time with a boy!"
scene ep3_chose_maya9
my "There's something I haven't told you..."
my "It started as the reason why I needed that money..."
my "...but thanks to Derek, and now even you, I've realized that I need it for an even bigger reason."
scene ep3_ending_0
play sound "sound_effects/door_knock.mp3"
"*{i}Door knocking{/i}*"
scene ep3_ending_3
my "What are you doing here?"
scene ep3_ending_6
my "[name]... This is my...girlfriend...Josy."

$ renpy.music.stop(channel="sfx1", fadeout=0)
play sound "sound_effects/whoosh_2.mp3"
label startUpdate4b:
scene black
$ renpy.pause(2)
hide screen previous_screen
stop music fadeout 3
$ renpy.pause(5)
scene black
$ renpy.pause(0.5)
hide screen phone_screen

label ep4_jm_intro_label:
if steamConfig or nonPatreonConfig:
    $ state = "ep4_steam"
elif True:
    $ state = "ep4"
call rpc from _call_rpc_3
play music "music/ep4/guitar_melancholy.mp3"
scene ep4_intro0 with fade
$ renpy.pause()
scene ep4_intro_a with dissolve
js "Ok, guys! Are we ready?"
scene ep4_intro_b with dissolve
js "Everyone! Say CHEEEESE!"
"CHEESE!!!"
scene white
play sound "sound_effects/camera_shutter.mp3"
$ renpy.pause(0.5)
scene ep4_intro_b with dissolve
$ renpy.pause(0.5)
scene ep4_intro_d with dissolve
de "Hey! Do it again! My timing was off!"
scene ep4_intro_e with dissolve
js "Your timing isn't off! You just can't air kick!"
scene ep4_intro_f with dissolve
de "That sounds like a bet!"
scene ep4_intro_g with dissolve
js "Hell yeah it is!"
scene ep4_intro_h with dissolve
de "I got $5 right here saying that the next picture will have me in it doing an air kick so fucking high that it will be out of frame!"
scene ep4_intro_i with dissolve
my "You're just gonna hurt yourself. Remember the cartwheel?"
scene ep4_intro_j with dissolve
de "I'm extremely proud of that cartwheel! I just...didn't nail the landing."
scene ep4_intro_k with dissolve
js "If you insist. I'm not the one to say no to free money."
de "Oh yeah? Just watch me!"
scene ep4_intro_b with dissolve
js "All right! Here we go again! Say CHEEESE!"
scene ep4_intro_n with dissolve
de "Wait wait wait! None of that fucking cheese bullshit!"
de "What are you, French?"
scene ep4_intro_o with dissolve
js "What do you want me to say, Mr. Stuntman?"
scene ep4_intro_n with dissolve
de "Give me a good old countdown. From ten to zero. New Year's style!"
scene ep4_intro_p with dissolve
js "From ten? Fuck, Derek! Does it take that long to time a jump?"
scene ep4_intro_q with dissolve
my "Haha! He's just hyping it up to impress Lynn."
de "What the fuck, sis!?"
de "You're supposed to be on my team!"
js "Hahaha!"
scene ep4_intro_s with dissolve
de "If that's the way you wanna play this, maybe you should tell Josy how you really feel about her?"
scene ep4_intro_t with dissolve
js "What's that?"
scene ep4_intro_u with dissolve
my "Nothing! Derek, shut up!"
my "Just do your stupid air kick already."
scene ep4_intro_b with dissolve
js "Ok, let's go! Three, two-"
de "That's not from ten!!!"
js "...one! FREEEENCH!"
scene white
play sound "sound_effects/camera_shutter.mp3"
scene ep4_intro1 with dissolve
$ renpy.pause(2)
scene ep4_intro_2 with dissolve
de "Here! Give me the camera! I think I nailed it."
scene ep4_intro_3 with dissolve
js "Your foot was almost out of frame...you know, the wrong side of it, but still..."
scene ep4_intro_4 with dissolve
de "This is bullshit. You should have counted from ten!"
scene ep4_intro_5 with dissolve
js "Don't worry, I'm sure Lynn was impressed, still. Right?"
scene ep4_intro_6 with dissolve
$ renpy.pause()
scene ep4_intro_7 with dissolve
de "Hey, Lynn! Watch my somersault!"
play sound "sound_effects/water_splash.mp3"
scene ep4_intro_8 with dissolve
$ renpy.sound.play("sound_effects/water_pool.mp3", channel="sfx1", loop=True)
js "Your brother is a real try-hard."
scene ep4_intro_9 with dissolve
my "Yeah, I'm just glad we're not identical twins."
my "Could you imagine there being two Dereks in this world?"
scene ep4_intro_8 with dissolve
js "He's fun to be around. We wouldn't be on this trip if it wasn't for him."
scene ep4_intro_9 with dissolve
my "I get the feeling he's going all in on Lynn and that we're just along for the ride."
my "You know, as cover?"
scene ep4_intro_11 with dissolve
js "Yeah, totally. Since school's over next year, we'll likely never see each other again."
js "He's doing the right thing with that Hail Mary attempt, in my mind."
scene ep4_intro_12 with dissolve
my "Not going to see each other again?"
my "Where are you going?"
scene ep4_intro_13 with dissolve
js "You think I will come back here for nothing?"
scene ep4_intro_14 with dissolve
my "What do you mean for nothing? Your mom and friends still live here."
scene ep4_intro_13 with dissolve
js "I have friends where my dad is, too."
js "And if I'd rather commute here than live with mom...that should speak volumes."
js "But I was hoping to get into B&R. My dad wants me to go."
scene ep4_intro_14 with dissolve
my "Do {b}you{/b} want to go?"
scene ep4_intro_13 with dissolve
js "Yeah, they have a killer economics program and it's close to my dad."
scene ep4_intro_14 with dissolve
my "Then it's not over. We'll still see each other."
scene ep4_intro_16 with dissolve
js "You're going there, too?"
scene ep4_intro_17 with dissolve
my "Not just me. Derek, as well."
scene ep4_intro_16 with dissolve
js "Can't shake him, huh?"
scene ep4_intro_17 with dissolve
my "He's my brother, I don't wanna shake him."
scene ep4_intro_13 with dissolve
js "Having a brother that you don't hate... I envy you."
scene ep4_intro_17 with dissolve
my "Sometimes I wish he was a little bit less...everything."
my "But I do love him."
scene ep4_intro_22 with dissolve
js "What did he mean before?"
scene ep4_intro_23 with dissolve
my "With...what?"
scene ep4_intro_22 with dissolve
js "That thing he said...about your feelings."
scene ep4_intro_23 with dissolve
my "Oh, that... No, really, it was nothing."
scene ep4_intro_22 with dissolve
js "Really?"
js "Because it kind of sounded like you-"
play sound "sound_effects/water_splash.mp3"
scene ep4_intro_26 with hpunch
js "Ahhh!!!"
scene ep4_intro_27 with dissolve
de "Stop being boring and jump in!"
scene ep4_intro_28 with dissolve
js "Haha! You bastard!"
$ renpy.music.stop(channel="sfx1", fadeout=3)
my "All right! Let's go!"
$ renpy.sound.play("sound_effects/bonfire.mp3", channel="sfx2", loop=True)
scene ep4_intro_29 with fade
js "I can totally see why you love this place."
js "Is it always this quiet?"
scene ep4_intro_30 with dissolve
de "Yeah! There's nothing but wildlife out here!"
de "Oh! Listen to this!"
scene ep4_intro_31 with dissolve
de "SHITBALLS!"
"*{i}Echo{i}* SHITBALLS SHITBALLS shitballs..."
scene ep4_intro_32 with dissolve
my "That's real mature, Derek."
scene ep4_intro_33 with dissolve
js "SHITBALLS!!!"
"*{i}Echo{i}* SHITBALLS SHITBALLS shitballs..."
scene ep4_intro_34 with dissolve
js "Hahaha!"
de "See? Jojo gets it!"
scene ep4_intro_35 with dissolve
my "DIARRHEA SHIT!!!"
"*{i}Echo{i}* DIARRHEA SHIT DIARRHEA SHIT diarrhea shit..."
scene ep4_intro_36 with dissolve
de "That's...gross."
scene ep4_intro_37 with dissolve
my "Shut up..."
scene ep4_intro_38 with dissolve
de "Cheers, Lynn!"
scene ep4_intro_39 with dissolve
js "Hey!"
my "Huh?"
js "Cheers!"
scene ep4_intro_42 with dissolve
my "Cheers!"
scene ep4_intro_43 with dissolve
js "Uh...ok."
scene ep4_intro_44 with dissolve
my "Awkward..."
js "Hahaha..."
my "I don't know what to say now."
js "I bet you could kill the mood by screaming diarrhea shit again."
scene ep4_intro_47 with hpunch
my "*{i}Coughs{/i}*"
scene ep4_intro_48 with dissolve
my "Oh! I got beer in my nose."
js "Hahaha!"
scene ep4_intro_49 with dissolve
js "Haha, here."
my "Thanks..."
scene ep4_intro_50 with dissolve
js "..."
scene ep4_intro_51 with dissolve
js "Come!"
my "Where are we going?"
js "You'll see! Follow me!"
$ renpy.music.stop(channel="sfx2", fadeout=3)
scene ep4_intro_53 with dissolve
my "The lake? Why?"
js "Didn't you ever go skinny-dipping before?"
my "No?"
scene ep4_intro_54 with dissolve
js "Trust me! It's fun!"
scene ep4_intro_55 with dissolve
$ renpy.pause()
scene ep4_intro_56 with dissolve
$ renpy.pause()
scene ep4_intro_56b with dissolve
$ renpy.pause()
scene ep4_intro_56c with dissolve
js "Don't leave me hanging! Get undressed!"
my "All right..."
scene ep4_intro_58 with dissolve
$ renpy.pause()
scene ep4_intro_59 with dissolve
$ renpy.pause()
scene ep4_intro_60 with dissolve
my "..."
scene ep4_intro_61 with dissolve
$ renpy.pause()
scene ep4_intro_62 with dissolve
$ renpy.pause()
scene ep4_intro_63 with dissolve
my "Now what?"
js "Now we jump!"
scene ep4_intro_64 with dissolve
js "Woho!!!"
"*{i}Echo{/i}* Woho woho..."
play sound "sound_effects/water_splash.mp3"
scene ep4_intro_65 with vpunch
$ renpy.pause()
scene ep4_intro_66 with dissolve
my "*{i}Shudders{/i}* Oh...wow...it's f-f-freezing!"
js "Yeah, totally!"
scene ep4_intro_67 with dissolve
js "Let's run back to the fire!"
$ renpy.sound.play("sound_effects/bonfire.mp3", channel="sfx1", loop=True)
scene ep4_intro_68 with dissolve
my "I'm so cold!"
js "Don't worry! You'll get warm in no time."
my "Where did they go?"
scene ep4_intro_69 with dissolve
"*{i}Moans{/i}* Oh, Derek..."
scene ep4_intro_70 with dissolve
js "*{i}Giggles{/i}*"
my "That...um...haha...was unexpected."
stop music fadeout 3
scene ep4_intro_71 with dissolve
js "I'll put on some music to give them some privacy."
play music "music/ep4/just_peachy.mp3"
scene ep4_intro_72 with dissolve
my "Oh, I like this song!"
scene ep4_intro_73 with dissolve
js "How come you knew about this place? It's pretty far from the city."
scene ep4_intro_74 with dissolve
my "We go here on caravan holidays. Every year we go someplace new, but we always start with this spot."
my "By the end of the holiday, you get pretty homesick, but starting with this place always makes it feel like summer's begun."
scene ep4_intro_73 with dissolve
js "Caravan holidays? I never went on one. What do you do on those? Just sleep in a caravan at different places?"
scene ep4_intro_74 with dissolve
my "Haha, yeah you could reduce it to that, but there's so much more to it."
my "It's a...lifestyle. Being on the road, seeing new places, meeting similar people..."
my "I've always loved it."
scene ep4_intro_73 with dissolve
js "Are you going next summer?"
scene ep4_intro_78 with dissolve
my "I think so. I hope there's time for it after graduating and all."
scene ep4_intro_73 with dissolve
js "Yeah, of course there is. I think I will spend that time getting some work experience and earn extra money."
scene ep4_intro_78 with dissolve
my "That's cool. I never had a summer job...or any job for that matter."
scene ep4_intro_81 with dissolve
js "This summer I sold strawberries. It was pretty sweet."
js "I basically sat outside listening to music all day and if I sold a lot I got to go home early."
scene ep4_intro_82 with dissolve
js "I got a great tan from it, too!"
scene ep4_intro_74 with dissolve
my "It sounds fun!"
scene ep4_intro_73 with dissolve
js "Why don't you try it this summer?"
scene ep4_intro_78 with dissolve
my "I don't think my dad would want that."
scene ep4_intro_73 with dissolve
js "Ok? But it's your choice, isn't it?"
scene ep4_intro_78 with dissolve
my "Hm... He's pretty fussy about what we do for vacation."
scene ep4_intro_73 with dissolve
js "All right."
scene ep4_intro_81 with dissolve
js "Are you still freezing?"
scene ep4_intro_82b with dissolve
my "A tad, but it's getting warmer."
my "How about you?"
scene ep4_intro_81 with dissolve
js "I'm good, but the fire is dying out."
js "I'd go to my tent and get my sweater, but it's currently being...occupied."
scene ep4_intro_82b with dissolve
my "You can...join me in mine, if you want."
scene ep4_intro_82c with dissolve
my "(Did I just ask that? Fuck! I feel queasy.)"
scene ep4_intro_81 with dissolve
js "Ok. Lead the way."
scene ep4_intro_82b with dissolve
my "Really? Yeah...ok..."
$ renpy.music.stop(channel="sfx1", fadeout=3)
label ep4_lewd_josy_maya_label:
if _in_replay:
    hide screen phone_screen
    play music "music/ep4/just_peachy.mp3"
scene ep4_intro_92 with dissolve
my "Here we are."
js "Your tent is tiny."
my "I know, it's one of those cheap ones."
my "It really isn't meant to fit two persons."
scene ep4_intro_94 with dissolve
js "Haha! No shit!? Hi!"
my "Hi..."
scene ep4_intro_96 with dissolve
js "So?"
my "So...what?"
scene ep4_intro_98 with dissolve
js "The sweater?"
scene ep4_intro_99 with dissolve
my "Oh! Right!"
my "It's right there behind your head."
scene ep4_intro_100 with dissolve
my "(!!!)"
scene ep4_intro_101 with dissolve
my "What are you doing?"
scene ep4_intro_102 with dissolve
js "I'm kissing you."
scene ep4_intro_101 with dissolve
my "Why?"
scene ep4_intro_102 with dissolve
js "Because I wanted to."
scene ep4_intro_101 with dissolve
my "Really?"
scene ep4_intro_102 with dissolve
js "Don't tell me you don't feel it, too."
js "This...tension."
scene ep4_intro_103 with dissolve
js "This is what you wanted...right?"
scene anim_jm_kiss_ep4 with dissolve
$ renpy.pause()
scene anim_jm_kiss2_ep4 with dissolve
$ renpy.pause()
scene anim_jm_kiss3_ep4 with dissolve
$ renpy.pause()
scene black with Fade(3,1,1.5)
$ renpy.end_replay()
$ persistent.ep4_lewd_maya_josy = True
$ calcScenes()
stop music fadeout 5
scene black with dissolve
show screen ep6_title_screen
$ renpy.pause(5)
play music "music/ep3/guitar_gentle.mp3"
show screen phone_screen
if ep3_choseDerek:
    jump ep4_night_talk_derek_label
elif ep3_choseSage:
    jump ep4_night_talk_sage_label
elif ep3_choseBella:
    jump ep4_night_talk_bella_label

label ep4_flashback_label:
play music "music/ep1/lonely.mp3"
scene ep4_flashback1 with fade
mc "Girlfriend?"
scene ep4_flashback2 with dissolve
js "Maya?"
scene ep4_flashback3 with dissolve
my "Don't worry...this is [name]."
my "We're...close."
scene ep4_flashback4 with dissolve
js "..."
scene ep4_flashback5 with dissolve
mc "..."
scene ep4_flashback6 with dissolve
my "What are you doing here?"
scene ep4_flashback7 with dissolve
js "I got in... They assigned me this dorm and told me it was available."
scene ep4_flashback6 with dissolve
my "Oh... They didn't forget..."
my "Um... [name] has been staying here..."
my "They don't know about it."
scene ep4_flashback9 with dissolve
js "Uh-huh..."
js "I...uh... I thought I saw a restroom back there."
js "I need to use it... Long trip, you know? Haha..."
scene ep4_flashback10 with dissolve
js "(What the fuck is this!? SHIT!)"
scene ep4_flashback11 with dissolve
my "Hey... I'm so sorry you had to find out like this."
scene ep4_flashback12 with dissolve
mc "You...you...what!?"
scene ep4_flashback13 with dissolve
my "I tried telling you about her!"
scene ep4_flashback12 with dissolve
mc "Yeah, you did! Two minutes ago!"
scene ep4_flashback13 with dissolve
my "And before that!"
my "But...I...I... Yeah! I know!"
scene ep4_flashback12 with dissolve
mc "Josy's your girlfriend!?"
scene ep4_flashback13 with dissolve
my "Let me explain!"
my "I know it's a shock! I'm shocked, too, right now!"
my "I was going to tell you about her! And also..."
scene ep4_flashback19 with dissolve
my "..."
scene ep4_flashback19b with dissolve
my "I think we were close to breaking up."
scene ep4_flashback19 with dissolve
mc "..."
scene ep4_flashback19b with dissolve
my "Things haven't been good between us lately."
my "My dad kept me from seeing her and that didn't do us any good."
my "And lately she's not been herself either."
scene ep4_flashback23 with dissolve
my "She doesn't answer my calls and last time I spoke to her she said she was giving up and moving far away."
my "She was going to come here and we were gonna be together, just like before..."
my "...but in secret."
my "That's what we agreed upon."
scene ep4_flashback24 with dissolve
my "But over the summer we drifted apart..."
my "...and I..."
my "I met you."
scene ep4_flashback25 with dissolve
mc "I...I think I'm gonna throw up or something."
play sound "sound_effects/message.mp3"
"*{i}Text message{/i}*"
$ chat_josy_history_is_them.append(True)
$ chat_josy_history.append("Please, meet me in the bathroom!")
scene ep4_flashback26 with dissolve
$ renpy.pause()
scene ep4_flashback25 with dissolve
stop music fadeout 3
mc "I...I'll be back in a bit."
scene ep4_flashback28 with dissolve
play music "music/ep3/guitar_melancholy2.mp3"
mc "Ok, where are you?"
js "I'm in here."
scene ep4_flashback29 with dissolve
mc "..."
mc "Maya is your {i}boyfriend{/i}?"
js "I never said I had a boyfriend."
mc "How crafty of you. Congratulations, you fooled me."
scene ep4_flashback33 with dissolve
js "I told you I wanted to explain when I got here."
js "You knew I was in a relationship already."
js "What difference does it make if it's with a boy or a girl?"
scene ep4_flashback32 with dissolve
mc "The difference it makes is that it's with Maya."
scene ep4_flashback33 with dissolve
js "How could I've known that you know her or that you're staying with her?"
js "What kind of a fucked up coincidence is that?"
js "I must be cursed. Nothing is going my way..."
scene ep4_flashback32 with dissolve
mc "You really should have told me everything from the start."
mc "That you had a girlfriend and that she went to B&R. It would have changed a lot!"
mc "That's why we're in this spot right now."
scene ep4_flashback33 with dissolve
js "I don't go around telling people about her."
js "Do you know how judgmental everyone is about a girl-girl relationship!?"
scene ep4_flashback36 with dissolve
js "And don't act like you're perfect!"
if ep2_fuckedJosy:
    js "You still made moves on me and even fucked me knowing I was in a relationship!"
elif True:
    js "You still made moves on me and even dated me knowing I was in a relationship!"
js "Neither of us are perfect."
js "I have flaws! I make mistakes!"
scene ep4_flashback37 with dissolve
mc "Is that what I am? A mistake?"
scene ep4_flashback33 with dissolve
js "No! I..."
js "I'm not sure of what you are..."
scene ep4_flashback32 with dissolve
mc "Wow...really? Because it sure as hell didn't sound like this last time! Was that all talk?"
scene ep4_flashback33 with dissolve
js "No, it wasn't all talk!"
js "Why do you think I called you with the news and not her?"
js "What are we going to do...?"
scene ep4_flashback32 with dissolve
mc "We?"
mc "I know what I'm doing..."
mc "I'm leaving."
scene ep4_flashback43 with dissolve
js "What?"
scene ep4_flashback44 with dissolve
mc "I'm not going to stay in that dorm with you and your girlfriend."
scene ep4_flashback43 with dissolve
js "Please, we can work this out. All we need to do is talk to each other."
scene ep4_flashback44 with dissolve
mc "And say what!? That we're all just a bunch of cheaters!?"
scene ep4_flashback43 with dissolve
js "What?"
scene ep4_flashback44 with dissolve
mc "And besides, you're not the only one who lied to me."
scene ep4_flashback43 with dissolve
js "Wait!"
scene ep4_flashback48 with dissolve
js "I said wait!"
my "What's happening?"
scene ep4_flashback50 with dissolve
mc "Good bye, Maya."
my "N-no! Wait!"
my "[name]!"
scene ep4_flashback52 with dissolve
$ renpy.pause()
scene ep4_flashback53 with dissolve
my "Holy fuck! This is a shitty, fucking mess!"
js "You're telling me..."
scene ep4_flashback55 with dissolve
my "You got in!?"
scene ep4_flashback54 with dissolve
js "Yeah."
scene ep4_flashback55 with dissolve
my "When!?"
scene ep4_flashback54 with dissolve
js "They wrote me this Monday, but I couldn't read my e-mail before this morning."
scene ep4_flashback56 with dissolve
my "Sure. Like I would believe that."
my "You're just covering up for ghosting me since Saturday."
scene ep4_flashback57 with dissolve
js "I know we've been fighting a lot, but I haven't ghosted you."
js "My dad and I fought. He took my phone and grounded me afterwards."
scene ep4_flashback56 with dissolve
my "Do you have it now?"
scene ep4_flashback57 with dissolve
js "Yeah, I swiped it this morning, packed my bags and got the hell out."
scene ep4_flashback56 with dissolve
my "Then why haven't you answered my texts?"
scene ep4_flashback61 with dissolve
js "And reply what!? I read your texts!"
js "Each one was meaner than the one before!"
js "I don't need that after this week."
scene ep4_flashback57 with dissolve
js "We just fight... Do you think I enjoy that?"
scene ep4_flashback55 with dissolve
my "Do you think {b}I{/b} enjoy that?"
scene ep4_flashback64 with dissolve
js "..."
my "..."
my "What happened to us?"
scene ep4_flashback64b with dissolve
js "Your dad happened to us."
scene ep4_flashback64 with dissolve
my "..."
scene ep4_flashback65 with dissolve
my "He can't find out we're sharing a dorm..."
scene ep4_flashback67 with dissolve
js "I know! It's not like I planned for this to happen."
js "He won't show up, right?"
scene ep4_flashback65 with dissolve
my "I don't know... He was here earlier today and next time it's likely just a phone call..."
my "Derek told me my dad asked him to keep an eye out, too."
my "He promised to warn me if dad contacted him."
scene ep4_flashback67 with dissolve
js "How long are you going to let him control you like this?"
scene ep4_flashback71 with dissolve
my "I have a plan for it."
scene ep4_flashback72 with dissolve
js "You do? Why haven't you told me about it?"
scene ep4_flashback71 with dissolve
my "I was going to tell you, but I wasn't sure if it would work. And after fighting with you so much..."
my "I..."
my "I realized the plan would still help me, even if it weren't for us anymore."
scene ep4_flashback74 with dissolve
js "..."
scene ep4_flashback75 with dissolve
js "You seem to think that I don't give a shit about you!"
scene ep4_flashback76 with dissolve
my "Do you!?"
scene ep4_flashback75 with dissolve
js "Yeah! I give a pretty big fucking diarrhea shit about you!"
scene ep4_flashback79 with dissolve
my "..."
scene ep4_flashback79b with dissolve
my "Hahaha..."
js "Hahaha."
scene ep4_flashback80 with dissolve
js "I...just want to be my old happy self."
js "I can't even remember the last time I didn't worry about us and my life."
js "Right now, I'm definitely not happy."
scene ep4_flashback80b with dissolve
my "I feel the same..."
scene ep4_flashback80 with dissolve
js "Tell me about your plan."
my "..."
scene ep4_flashback80b with dissolve
stop music fadeout 3
my "It all started when I heard this rumor..."
scene black with Fade(2, 2, 2)

if ep3_choseDerek:
    jump ep4_night_talk2_derek_label
elif ep3_choseSage:
    jump ep4_night_talk2_sage_label
elif ep3_choseBella:
    jump ep4_night_talk2_bella_label

label ep4_jmq_label:
play music "music/ep3/lets_begin.mp3"
scene ep4_jmq with wipeleft
qu "Rise and shine, sweet daughter o' mine! I have a task for you!"
scene ep4_jmq1 with dissolve
if not ep3_choseSage:
    qu "Oh? Either [name] shrunk himself and grew some titties or you got a new roommate."
    scene ep4_jmq2 with dissolve
    js "Who's this funny girl?"
elif True:
    qu "Oh? So, this is why he stays with Sage."
    scene ep4_jmq2 with dissolve
    js "Who's the loudmouth?"
scene ep4_jmq3 with dissolve
my "*{i}Yawns{/i}* This is Quinn, remember?"
scene ep4_jmq4 with dissolve
js "This is Quinn!? Oh, I thought she'd be taller."
scene ep4_jmq5 with dissolve
qu "Taller? Shut the fuck up! You're the size of a shrimp."
scene ep4_jmq6 with dissolve
js "Yikes. Sorry, I didn't mean anything by that."
js "Well, what do you want? We were sleeping here."
scene ep4_jmq7 with dissolve
qu "Maya, let's go. It's mother-daughter time."
scene ep4_jmq8 with dissolve
my "Um...Josy had a question for you."
js "Yeah! I want to pledge, too."
js "Maya talked me into it. It sounds like fun."
js "So, can I?"
scene ep4_jmq10 with dissolve
qu "I'm looking at you right now and I don't see it."
qu "You're not HOT material."
scene ep4_jmq11 with dissolve
js "Is this because I called you short before?"
scene ep4_jmq12 with dissolve
qu "You're really chipper, aren't you?"
qu "I hate chipper people."
scene ep4_jmq13 with dissolve
js "I like to laugh and make new friends."
js "I'd say I'm pretty easy-going. And I'm fun to be around!"
js "I like to party and I heard that it's what the HOTs are all about."
js "Besides, Maya and I have been friends since high school, so I think I would fit in perfectly."
scene ep4_jmq12 with dissolve
qu "Do you like the sound of your own voice or did you really think I'd pay attention to that vagina monologue?"
qu "No sale."
qu "Maya! Let's go!"
scene ep4_jmq15 with dissolve
js "Oh, and also..."
js "I'm Tommy's stepsister."
scene ep4_jmq16 with dissolve
$ renpy.pause()
scene ep4_jmq17 with dissolve
$ renpy.pause()
if ep3_choseDerek:
    jump ep4_derek_talk_label
label ep4_derek_pre_school_label:
scene ep4_derek_pre_school with wipeleft
$ renpy.pause()
scene ep4_derek_pre_schoolb with dissolve
de "There you are! Dude, I was worried."
play sound "sound_effects/hit.mp3"
scene ep4_derek_pre_school1b with hpunch
de "Turn your phone on!"
scene ep4_derek_pre_school1 with dissolve
mc "Sorry, something happened last night."
scene ep4_derek_pre_school2 with dissolve
de "No shit!? Sis called me."
de "She's been trying to reach you."
scene ep4_derek_pre_school1 with dissolve
mc "She's the last person I want to talk to right now."
mc "So, you heard?"
scene ep4_derek_pre_school4 with dissolve
de "Yeah, I didn't fully understand what she went on about, but..."
de "...you know about her...secret?"
scene ep4_derek_pre_school1 with dissolve
mc "About Josy? Yeah."
scene ep4_derek_pre_school2 with dissolve
de "Yeah...that's what's been bugging me..."
de "Not that she didn't tell you, because that's her deal..."
de "...but the cheating part."
scene ep4_derek_pre_school1 with dissolve
mc "That's only half of the story."
scene ep4_derek_pre_school4 with dissolve
de "What's the other half?"
scene ep4_derek_pre_school1 with dissolve
mc "That would be the half where Josy is the girl I've been dating."
scene ep4_derek_pre_school8 with dissolve
de "WHAT!?"
scene ep4_derek_pre_school9 with dissolve
mc "I met her this summer, at my summer job."
mc "We went out on a date..."
mc "I told her I had a crush on her and she told me she had one too."
mc "I kissed her and she kissed me back..."
scene ep4_derek_pre_school10 with dissolve
mc "After we stopped making out, she told me she was in a relationship."
mc "And now I know with who."
scene ep4_derek_pre_school11 with dissolve
de "She cheated on Maya?"
scene ep4_derek_pre_school9 with dissolve
mc "If that's called cheating, Maya cheated on Josy, too."
scene ep4_derek_pre_school11 with dissolve
de "You didn't..."
scene ep4_derek_pre_school9 with dissolve
mc "Whatever."
scene ep4_derek_pre_school11c with dissolve
de "I don't know what to say to you right now."
de "What do I tell Maya?"
scene ep4_derek_pre_school9 with dissolve
mc "You don't have to tell her anything. She can handle this herself."
scene ep4_derek_pre_school14 with dissolve
de "You look like you need a hug."
scene ep4_derek_pre_school15 with dissolve
mc "I...don't need a hug."
$ guideSuggestedPage = 93
scene ep4_derek_pre_school14 with dissolve
de "You need a hug."
scene ep4_derek_pre_school15 with dissolve
menu:
    "Hug him" if True:
        $ RPderek += 1
        $ dk(-1)
        scene ep4_derek_pre_school16 with dissolve
        de "That's it..."
        mc "What? No jokes?"
        de "Not this time."
        scene ep4_derek_pre_school15 with dissolve
    "Maybe it's you who need a hug" if True:
        mc "Maybe it's you who need a hug?"
        scene ep4_derek_pre_school14 with dissolve
        de "I need a hug."
        $ RPderek += 1
        $ dk(-1)
        scene ep4_derek_pre_school16 with dissolve
        de "That's it..."
        mc "What? No jokes?"
        de "Not this time."
        scene ep4_derek_pre_school15 with dissolve
    "Leave him hanging" if True:
        $ dk(1)
        mc "No, I'm good."
mc "By the way, I didn't drink any beer this morning."
scene ep4_derek_pre_school14 with dissolve
de "Hey! Don't you worry. We'll still make it."
label ep4_derek_talk_label:
scene ep4_derek_pre_school17 with wipeleft
mc "Could you go get my beer from Maya? I don't want to go back there."
if ep3_choseBella:
    mc "Right now, I'm staying with Bella...you know the librarian?"
elif ep3_choseSage:
    mc "Sage took me in until I get my shit sorted, as she phrased it."
scene ep4_derek_pre_school18 with dissolve
de "Yeah, don't worry. I got you, [mc_de]."
de "College, huh? The best days of our lives."
de "Hey! I know what will cheer you up!"

de "Wanna wear the helmet?"
scene ep4_derek_pre_school19 with dissolve
menu:
    "Yes" if True:
        $ ep4_wearHelmet = True
        $ ep4_morningHelmet = True
        $ ep3_hellWeekHelmet += 1
        mc "Haha... Sure. Give it here already."
    "No" if True:
        $ ep4_wearHelmet = False
        $ ep4_morningHelmet = False
        if dtype > 0:
            mc "No, I'm not in the mood for it."
        elif True:
            mc "No, thanks. I'm not in the mood for it."
if ep4_wearHelmet:
    scene ep4_derek_pre_school21 with dissolve
    de "Sweet! I hope you're in the mood for some of the other activities."
elif True:
    scene ep4_derek_pre_school21b with dissolve
    de "I hope you get in the mood for some of the other activities."
if ep4_wearHelmet:
    scene ep4_derek_pre_school22 with dissolve
elif True:
    scene ep4_derek_pre_school22b with dissolve
mc "Fuck, it's already Thursday... We have so much left to do."
if ep4_wearHelmet:
    scene ep4_derek_pre_school21 with dissolve
elif True:
    scene ep4_derek_pre_school21b with dissolve
de "About that nerd wedgie task...do you wanna do it?"
if ep4_wearHelmet:
    scene ep4_derek_pre_school22 with dissolve
elif True:
    scene ep4_derek_pre_school22b with dissolve
mc "I know some of the nerds, it would be awkward for me."
if ep4_wearHelmet:
    scene ep4_derek_pre_school21 with dissolve
elif True:
    scene ep4_derek_pre_school21b with dissolve
if ep3_choseDerek:
    de "Right... Bert is a nerd; it's crossed my mind to give him one."
elif True:
    de "Right... My roommate Bert is a nerd...and a fucking dick, too."
    de "It's crossed my mind to give him one."
de "But then it would be weird living with him..."
de "What do you think?"
if ep4_wearHelmet:
    scene ep4_derek_pre_school22 with dissolve
elif True:
    scene ep4_derek_pre_school22b with dissolve
mc "It's up to you. I can talk to Magnar and see if there's an easier way around it."
if ep4_wearHelmet:
    scene ep4_derek_pre_school21_2 with dissolve
elif True:
    scene ep4_derek_pre_school21_2b with dissolve
de "Oh! Another thing!"
de "Rusty told me that there's a party at the DIKs tomorrow night."
de "Maybe we can do more stuff then?"
de "Also, that car wash is happening on Saturday. The HOTs are doing it at the same time."
de "So, that will be fun!"
if ep4_wearHelmet:
    scene ep4_derek_pre_school22_2 with dissolve
elif True:
    scene ep4_derek_pre_school22_2b with dissolve
mc "How do you know all of this?"
if ep4_wearHelmet:
    scene ep4_derek_pre_school21_2 with dissolve
elif True:
    scene ep4_derek_pre_school21_2b with dissolve
de "Rusty tells me. It's a part of being a father, he said."
if ep4_wearHelmet:
    scene ep4_derek_pre_school22_2 with dissolve
elif True:
    scene ep4_derek_pre_school22_2b with dissolve
if dtype > 0:
    mc "Funny, because Tommy doesn't tell me shit."
elif True:
    mc "How ironic... Tommy doesn't tell me anything."
if ep4_wearHelmet:
    scene ep4_derek_pre_school23 with dissolve
elif True:
    scene ep4_derek_pre_school23b with dissolve
de "Do you want him to? I mean, you don't seem to like him a lot."
if ep4_wearHelmet:
    scene ep4_derek_pre_school22_2 with dissolve
elif True:
    scene ep4_derek_pre_school22_2b with dissolve
mc "I just feel a bit weird not getting the same treatment, that's all."
mc "I wish Rusty was my father, too."
if ep4_wearHelmet:
    scene ep4_derek_pre_school23 with dissolve
elif True:
    scene ep4_derek_pre_school23b with dissolve
de "How about if you start up a talk with Tommy? He seems to like DIK traditions and frat life..."
de "...maybe you could begin a conversation with that?"
if ep4_wearHelmet:
    scene ep4_derek_pre_school24 with dissolve
elif True:
    scene ep4_derek_pre_school24b with dissolve
mc "Yeah, either that or something about his sis coming here."
mc "You know...Josy."
if ep4_wearHelmet:
    scene ep4_derek_pre_school25 with dissolve
elif True:
    scene ep4_derek_pre_school25b with dissolve
de "What? No way!"
de "Is Tommy \"THE\" Tommy?"
de "Josy's evil stepbrother?"
if ep4_wearHelmet:
    scene ep4_derek_pre_school24 with dissolve
elif True:
    scene ep4_derek_pre_school24b with dissolve
mc "I thought you knew Josy. You seriously didn't know it was him?"
if ep4_wearHelmet:
    scene ep4_derek_pre_school27 with dissolve
elif True:
    scene ep4_derek_pre_school27b with dissolve
de "I only know her through my sis. We went to high school together, but you know..."
de "Maya was into her so that automatically turned me off."
if ep4_wearHelmet:
    scene ep4_derek_pre_school26b with dissolve
elif True:
    scene ep4_derek_pre_school26d with dissolve
de "Also, Jojo likes to yap and I wasn't the most attentive listener."
if ep4_wearHelmet:
    scene ep4_derek_pre_school27 with dissolve
elif True:
    scene ep4_derek_pre_school27b with dissolve
de "But whatever! Definitely don't mention what you did to his sister!"
de "If you think I was upset when I saw you and Maya..."
if ep4_wearHelmet:
    scene ep4_derek_pre_school22 with dissolve
elif True:
    scene ep4_derek_pre_school22b with dissolve
mc "Yeah, you wanted to fuck my dad, was it?"
if ep4_wearHelmet:
    scene ep4_derek_pre_school21 with dissolve
elif True:
    scene ep4_derek_pre_school21b with dissolve
de "He's on the back burner for now."
de "Just don't wake the devil in Tommy. That's all I'm saying."

label ep4_feminist_rally_label:
stop music
scene ep4_feminist_rally
play music "music/ep1/energetic.mp3"
play sound "sound_effects/megaphone.mp3"
wen "WHAT DO WE WANT!?"
"HIGHER SALARIES FOR WOMEN!"
wen "WHEN DO WE WANT IT!?"
"NOW!"
wen "WHAT DO WE WANT!?"
"HIGHER SALARIES FOR WOMEN!"
wen "WHEN DO WE WANT IT!?"
if ep4_wearHelmet:
    scene ep4_feminist_rally1b with dissolve
elif True:
    scene ep4_feminist_rally1 with dissolve
de "SHUT UP, WENDY!"
if ep4_wearHelmet:
    scene ep4_feminist_rally2 with dissolve
elif True:
    scene ep4_feminist_rally2b with dissolve
play sound "sound_effects/megaphone.mp3"
wen "TYPICAL MALE!"
wen "Women are worth the same as men! Correct!?"
if ep4_wearHelmet:
    scene ep4_feminist_rally4 with dissolve
elif True:
    scene ep4_feminist_rally4b with dissolve
de "Stop yelling! I'm trying to have a moment here with my friend!"
de "And I never said they weren't!"
if ep4_wearHelmet:
    scene ep4_feminist_rally3b with dissolve
elif True:
    scene ep4_feminist_rally3 with dissolve
wen "GREAT! That means that women are worth AT LEAST the same amount of pay! Correct!?"
if ep4_wearHelmet:
    scene ep4_feminist_rally4 with dissolve
elif True:
    scene ep4_feminist_rally4b with dissolve
de "Y-ye... No!? Are you fucking high?"
scene ep4_feminist_rally5 with dissolve
wen "See, everyone! This is the face of our enemy!"
if ep4_wearHelmet:
    scene ep4_feminist_rally4 with dissolve
elif True:
    scene ep4_feminist_rally4b with dissolve
de "I'm the enemy? Look at yourself!"
de "You want women to have higher salaries {b}just{/b} because they are women?"
de "What about merits!? What about skills!?"
de "What about the fact that women cost more in the workplace than men and are a bigger risk to hire due to pregnancies!?"
if ep4_wearHelmet:
    scene ep4_feminist_rally3b with dissolve
elif True:
    scene ep4_feminist_rally3 with dissolve
wen "You can't discriminate against a woman's right to bear a child!"
if ep4_wearHelmet:
    scene ep4_feminist_rally4 with dissolve
elif True:
    scene ep4_feminist_rally4b with dissolve
de "In a perfect world that may be the truth, but for small business owners you can't escape the fact that women are liabilities!"
de "And they aren't built the same as men either! And that can be a factor affecting productivity in jobs involving manual labor!"
de "So, no! Women aren't worth the same pay {b}just{/b} because they are women!"
de "Try to look at the world from more perspectives than your own, Wendy!"
if ep4_wearHelmet:
    scene ep4_feminist_rally9b with dissolve
elif True:
    scene ep4_feminist_rally9 with dissolve
de "You accuse men for getting paid more and getting ahead of women, but what you all are doing here right now is no better!"
de "You're not for equality! You just want to tip the fucking scale!"
stop music
if ep4_wearHelmet:
    scene ep4_feminist_rally10b with dissolve
elif True:
    scene ep4_feminist_rally10 with dissolve
ja "Derek. The counselor's office. Now!"
de "Fuck me..."
$ bios_history_derek += "Derek got into trouble with Jade after fighting with Wendy during their protest.\n\n"
$ bios_name_derek = True
$ chat_new_bios = True
label ep4_riona_quinn_label:
play music "music/ep1/unknown_power.mp3"
scene ep4_quri with dissolve
$ renpy.pause()
scene ep4_quri1 with dissolve
ri "Huh...?"
scene ep4_quri with dissolve
$ renpy.pause()
scene ep4_quri2 with dissolve
ri "Finally! So?"
scene ep4_quri3 with dissolve
qu "..."
ri "No... You're kidding me?"
scene ep4_quri5 with dissolve
qu "It's not over, but there's still some convincing to do."
scene ep4_quri4 with dissolve
ri "What did he say?"
scene ep4_quri5 with dissolve
qu "He said it was too risky. Thanks to Chad they got eyes on them."
scene ep4_quri4 with dissolve
ri "He's just being paranoid."
scene ep4_quri5 with dissolve
qu "That's what I said."
scene ep4_quri4 with dissolve
ri "Shit..."
scene ep4_quri6 with dissolve
qu "..."
scene ep4_quri4 with dissolve
ri "Why am I the only one worried here?"
scene ep4_quri6 with dissolve
qu "..."
scene ep4_quri4 with dissolve
ri "You have a plan, right?"
stop music fadeout 3
scene ep4_quri5 with dissolve
qu "Shut up and let me think..."
play music "music/ep2/phate.mp3"
scene ep4_quri10
qu "Hey! Give it back, I said one drag!"
scene ep4_quri11 with dissolve
$ renpy.pause()
scene ep4_quri12 with dissolve
tm "This is some quality shit!"
scene ep4_quri13 with dissolve
qu "You know who to thank for that."
scene ep4_quri14 with dissolve
tm "Whoa..."
qu "I told you to go easy! I wasn't being cheap when I said that."
scene ep4_quri16 with dissolve
tm "This is how you party..."
scene ep4_quri17 with dissolve
qu "No, that's how you party."
scene ep4_quri18 with dissolve
tm "I keep telling you, this is how it should be! HOTs and DIKs! DIKs and HOTs!"
tm "Together!"
scene ep4_quri19 with dissolve
qu "Look at you! Trying to take over this place just like that."
qu "It's not that easy, it's hard to break traditions."
scene ep4_quri20 with dissolve
tm "No shit!? I've been trying since I got here."
tm "But fuck traditions! Or better yet, make new ones!"
tm "Get rid of that fucking HOT-tri-alpha shit!"
tm "Think about it! If it weren't for Sage's and Chad's stupid relationship there would be nothing that really connects HOTs and alphas."
scene ep4_quri19 with dissolve
qu "Except for history."
scene ep4_quri20 with dissolve
tm "What we could do would be history one day, too!"
tm "We're vice presidents! We can call shots!"
tm "Rusty fucking loves it when I take charge."
scene ep4_quri19 with dissolve
qu "Sage's just the same..."
qu "So...what's your offer?"
scene ep4_quri23 with dissolve
tm "Look at this place! It's three times as big as the alphas' shitty villa!"
tm "Rusty makes sure there's a constant flow of alcohol without a campus security problem."
tm "All we need is some skirt to make this the best place ever."
tm "That's where you come in!"
scene ep4_quri19 with dissolve
qu "A place to party? You call that an offer?"
scene ep4_quri20 with dissolve
tm "A place to party for real! Catch my drift?"
tm "You know Sage... She wouldn't be cool with people using drugs in your house."
tm "And if you take a gamble with the alphas you're fucked."
tm "All that bragging about being natty tells me their parties must suck ass."
scene ep4_quri26 with dissolve
qu "Haha! They aren't natty! It's the equivalent of a party girl saying she's a virgin."
qu "It just sounds better."
scene ep4_quri20 with dissolve
tm "Yeah, yeah! But look at the DIKs!"
tm "Rusty is cool with all of this."
tm "John Boy's already in! Riona! Elena! Sarah! Melanie! Not to mention Heather!"
tm "That's a lot of people! And that's a great private party!"
tm "The best part about it, if you ever get caught by Sage or anyone else, you can blame it all on us."
tm "How's that for an offer?"
scene ep4_quri28 with dissolve
qu "You're offering to be a scapegoat? You're fucking nuts!"
qu "I like you. I wouldn't want that."
scene ep4_quri29 with dissolve
tm "That's how confident I am in this. No one will ever know!"
tm "Just look at how the counselors treat Rusty for being a Burgmeister!"
tm "Let's start small and gradually swap the alphas for the DIKs."
tm "And you keep on bringing me the good stuff."
scene ep4_quri30 with dissolve
qu "Throw in some extra money on that deal?"
scene ep4_quri31 with dissolve
tm "Every penny I get extra is already spent on you."
tm "Rusty won't go for a sponsor role, but it's not like the alphas pay you, right?"
scene ep4_quri32 with dissolve
tm "Maybe there are more DIKs that wanna join in? I could ask Jamie and Leon."
tm "You know you want to! Traditions are worth breaking."
tm "It's just like people changing jobs to get a better deal!"
scene ep4_quri33 with dissolve
qu "I shouldn't make deals while being high...but fuck it."
qu "It is a good offer. Besides, I'm sick of the fucking alphas anyway."
stop music
scene ep4_quri6
qu "..."
play music "music/ep1/unknown_power.mp3"
scene ep4_quri5 with dissolve
qu "I've got something. It's not the best plan..."
qu "...and it won't sit well with the DIKs..."
qu "...but if it works, we're right back on track."
scene ep4_quri4 with dissolve
ri "What's the plan?"
scene ep4_quri5 with dissolve
qu "We use Sage."
scene ep4_quri4 with dissolve
ri "Sage?"
scene ep4_quri5 with dissolve
qu "Yes. Sage."
scene ep4_quri38 with dissolve
ri "I'm lost."
scene ep4_quri37 with dissolve
qu "What do I always tell you to do?"
scene ep4_quri38 with dissolve
ri "That chess thing?"
scene ep4_quri37 with dissolve
qu "Exactly. You don't make a move without having planned for your next one."
qu "If Sage is the first move, what could the second one be?"
scene ep4_quri39 with dissolve
ri "..."
stop music fadeout 3
scene ep4_quri40 with dissolve
ri "Oh..."

label ep4_english_label:
play music "music/ep1/someways.mp3"
if ep4_wearHelmet:
    scene ep4_english1b with wipeleft
elif True:
    scene ep4_english1 with wipeleft
mc "(Of course... There's no escaping them... I should have known.)"
mc "(Well, I'm not going to sit anywhere near them.)"
scene ep4_english2 with dissolve
mc "Hey. Can I sit with you girls?"
scene ep4_english3 with dissolve
cam "Um... Sure?"
scene ep4_english4 with dissolve
mn "There's a seat by Maya."
scene ep4_english5 with dissolve
mc "Yeah, I see it."
scene ep4_english4 with dissolve
mn "Ok? I was just saying... Since you usually sit with her."
scene ep4_english6 with dissolve
cam "Did something happen?"

scene ep4_english7 with dissolve
menu:
    "Nothing" if True:
        mc "Nothing happened. I just wanted to sit with you two."
        scene ep4_english6 with dissolve
        cam "All right. DIKs and HOTs seem to get along, so why shouldn't we?"
    "None of your business" if True:
        $ dk(1)
        mc "That's none of your business."
        scene ep4_english8 with dissolve
        cam "Whoa... Ok."
scene ep4_english10 with dissolve
mc "(Why are they even sitting together?)"
scene ep4_english11 with dissolve
mc "(Maya said they were close to breaking up and I didn't think Josy wanted to be with Maya either...)"
cam "Where's Derek?"
scene ep4_english14 with dissolve
mc "Huh? Oh, he got into trouble with Jade, the Gender Studies teacher."
mc "There was a feminist protest outside and Derek likes finding trouble."
scene ep4_english15 with dissolve
cam "And you don't?"
scene ep4_english14 with dissolve
if affinity == "DIK":
    mc "Maybe a little bit, but I'm not about to take on a group of angry feminists."
    mc "What would be the point of that?"
    scene ep4_english17 with dissolve
    mn "That would be stupid..."
    mn "But you know...trouble can be fun."
elif True:
    mc "No, I'd rather stay out of it."
    scene ep4_english17 with dissolve
    mn "Pff... Trouble is way more fun."
scene ep4_english14 with dissolve
if ep3_helpedCamilaAndMona:
    mc "So, what's new with you guys? Did you find that...um...umbrella was it?"
    scene ep4_english17 with dissolve
    mn "Yeah, that one wasn't too hard."
    mn "But you really saved our asses with your underwear."
    if ep3_fuckedCamilaAndMona:
        scene ep4_english14 with dissolve
        mc "It was a fair trade if you ask me."
        scene ep4_english19 with dissolve
        cam "*{i}Mwah{/i}*"
elif True:
    mc "How's your scavenger hunt coming along? Found that underwear, yet?"
    scene ep4_english17 with dissolve
    mn "You'd be surprised how helpful men get when you pull your top down a bit before asking."
    cam "Hahaha!"
scene ep4_english15 with dissolve
cam "You have your Hell Week now, right? Having fun?"
scene ep4_english14 with dissolve
mc "It's ok. Some tasks are harder than others."
if ep3_helpedCamilaAndMona:
    scene ep4_english15 with dissolve
    cam "I was thinking..."
    cam "Since you helped us with one of our tasks, can we help you with one of yours?"
    scene ep4_english14 with dissolve
    mc "Let me think..."
    mc "Are either of you a feminist?"
    scene ep4_english25 with dissolve
    mn "Haha, no!"
    scene ep4_english14 with dissolve
    mc "A...teacher?"
    scene ep4_english15 with dissolve
    cam "I could dress up as a teacher if that would help?"
    scene ep4_english14 with dissolve
    if dtype > 0:
        mc "I'm sure that would help with something...but nothing for my list."
        scene ep4_english26 with dissolve
        cam "Haha!"
        scene ep4_english14 with dissolve
    elif True:
        mc "No, it would have to be the real deal..."
    label ep4_cam_mona_loop_label:
    menu:
        "Sex outdoors" if not ep4_camilaOffer:
            $ ep4_camilaOffer = True
            mc "I have a really hard one..."
            scene ep4_english30 with dissolve
            cam "..."
            mc "No, I wasn't talking about that."
            mc "Well...kind of."
            scene ep4_english14 with dissolve
            mc "I need to have sex outdoors with someone and get some kind of proof of it."
            mc "Would you be up for that?"
            scene ep4_english31 with dissolve
            cam "What kind of proof are we talking about?"
            scene ep4_english31b with dissolve
            mc "A picture or a DIK witness."
            scene ep4_english31 with dissolve
            cam "Does the picture have to show my face?"
            scene ep4_english31b with dissolve
            mc "No, but to be honest I think most would see it's you."
            mc "Your tattoo and hot body are unique."
            scene ep4_english33 with dissolve
            mn "I think he's trying to charm you, Camila."
            scene ep4_english15 with dissolve
            cam "You think?"
            cam "I'm flattered, but I'll have to pass on that one."
            if not ep4_monaSlap:
                scene ep4_english14 with dissolve
                jump ep4_cam_mona_loop_label
        "Slap me" if not ep4_monaSlap:
            $ ep4_monaSlap = True
            mc "Oh! Could you slap me in front of a DIK?"
            scene ep4_english25 with dissolve
            mn "We could do that."
            scene ep4_english14 with dissolve
            mc "Great! Just make it seem genuine. Like I did something to really piss you off."
            scene ep4_english25 with dissolve
            mn "Sure thing!"
            $ bios_history_camila += "Mona and Camila offered to help me get slapped for the pledge board task.\n\n"
            $ bios_name_camila = True
            $ bios_history_mona += "Mona and Camila offered to help me get slapped for the pledge board task.\n\n"
            $ bios_name_mona = True
            $ chat_new_bios = True
            if not ep4_camilaOffer:
                scene ep4_english14 with dissolve
                jump ep4_cam_mona_loop_label
        "Continue" if True:
            if ep4_camilaOffer or ep4_monaSlap:
                mc "I think that's it."
                scene ep4_english15 with dissolve
                cam "Great!"
            elif True:
                mc "You know what? I don't think you can help me with this."
                scene ep4_english15 with dissolve
                cam "Ok, good luck with it, then."
elif True:
    scene ep4_english15 with dissolve
    cam "Ok, well, good luck with it. You're almost there now."
stop music fadeout 3
scene ep4_english38 with dissolve
ca "Dawe, please take a seat. Class is starting."
scene ep4_english39 with dissolve
dw "Yeah, yeah."
$ guideSuggestedPage = 94
if not minigames:
    scene black with Fade(1.5, 1, 0.5)
    jump ep4_after_english_test
play music "music/ep3/sing_along_with_jim.mp3"
scene english_test_board
jump english101_test4
label ep4_after_english_test:
$ renpy.block_rollback()
scene ep4_after_english with dissolve
play music "music/ep2/journey_of_hope.mp3"
ca "(Hm...)"
ca "(No.)"
ca "(Not this one either...)"
scene ep4_after_english2 with dissolve
ca "(He's kind of cute...)"
ca "(But I'm not looking for cute...)"
scene ep4_after_english3 with dissolve
ca "(...and this one is way too hot for me.)"
ca "(If I swiped up on him, he would just laugh when he saw it...)"
scene ep4_after_english4 with dissolve
ca "(This isn't as anonymous that I had hoped for.)"
ca "(I feel so exposed...)"
ca "(It's like I'm literally saying \"I like you. Do you like me?\" to him in person.)"
scene ep4_after_english3 with dissolve
ca "(I wonder if there's another way of doing this.)"
ca "(A way that would let me say what I wanted without consequences...)"
ca "(Hm... I think I got something...)"
ca "(I can spend my free afternoon doing it!)"
scene ep4_after_english6 with dissolve
ca "Look at the time. That's all for today."
ca "Remember to read up on chapter two."
if ep4_wearHelmet:
    scene ep4_after_english7b with dissolve
elif True:
    scene ep4_after_english7 with dissolve
mc "(Nope...)"
mc "(I'm out of here...)"

label ep4_eco_label:
scene ep4_eco with wiperight
js "(Is this the right classroom? The maps really suck ass...)"
js "(And I was stupid enough to think I'd remember this place from that one visit during high school.)"
js "(I should have done what Maya did and went here more...)"
scene ep4_eco1 with dissolve
js "Is this seat taken?"
scene ep4_eco2 with dissolve
ji "No, please, go ahead."
scene ep4_eco2b with dissolve
ji "Are you new here?"
scene ep4_eco4 with dissolve
js "Yes, I'm one of the rejects."
scene ep4_eco5 with dissolve
ji "Excuse me?"
scene ep4_eco4 with dissolve
js "You know...the march thing?"
js "The march of the rejects?"
scene ep4_eco5 with dissolve
ji "I have never heard anything of the sort."
scene ep4_eco4 with dissolve
js "Oh... I thought it was a common name for students who got accepted after being on the waiting list."
scene ep4_eco9 with dissolve
ji "Haha! I think you mean replacements, not rejects."
scene ep4_eco10 with dissolve
js "Oh!"
js "It was my stepbrother who taught me that saying. Sorry."
js "I'm Josy, by the way."
scene ep4_eco9 with dissolve
ji "Jill. Nice to meet you."
ji "Welcome to B&R!"
scene ep4_eco12 with dissolve
js "Hey, thanks!"
js "Are you also a freshman?"
scene ep4_eco20 with dissolve
ji "No, I'm a third-year student. I've just been postponing this class for as long as possible."
scene ep4_eco12b with dissolve
js "It's not a fun class?"
scene ep4_eco20 with dissolve
ji "Financial Crisis? No, not really."
ji "It's probably ok, but there are so many more interesting classes out there."
ji "You'll see."
scene ep4_eco20b with dissolve
ji "Are you ok? You look a bit tense."
scene ep4_eco17 with dissolve
js "It's just first day nerves."
js "Plus, I feel a bit lost since I missed orientation."
scene ep4_eco20 with dissolve
ji "I remember the first day jitters."
ji "If you'd like, I can show you around afterwards?"
scene ep4_eco18b with dissolve
js "(Hm... Maya promised me that she would...but I could be making a new friend this way.)"
scene ep4_eco12 with dissolve
js "Sure! I would love that!"
scene ep4_eco20 with dissolve
ji "What other classes are you signed up for?"
scene ep4_eco12b with dissolve
js "English and Math, you know, Gen. Ed. classes."
scene ep4_eco24 with dissolve
ji "That's smart doing those early or you'll end up like me, postponing the less interesting ones."
scene ep4_eco23 with dissolve
js "You have the class literature already? Are we supposed to have that?"
scene ep4_eco24 with dissolve
ji "No, you're fine. You got here a bit later than everyone else and teachers understand that."
ji "By the way, the library sells class literature and my best friend works there."
ji "I can set you up with a copy if you'd like?"
scene ep4_eco12 with dissolve
js "That would be awesome. I feel like my brain is overflowing with information and impressions already."
scene ep4_eco24 with dissolve
ji "We can share it today."
stop music fadeout 3
js "All right."

label ep4_magnar_label:
if ep4_wearHelmet:
    scene ep4_magnar with wiperight
elif True:
    scene ep4_magnarb with wiperight
mg "You're asking me for permission to humiliate one of us in front of your chums for Hell Week?"
mg "Did I understand that correctly?"
if ep4_wearHelmet:
    scene ep4_magnar1 with dissolve
elif True:
    scene ep4_magnar1b with dissolve
mc "Those weren't my words."
if ep4_wearHelmet:
    scene ep4_magnar with dissolve
elif True:
    scene ep4_magnarb with dissolve
mg "Hell Week is so gruesome in your fraternities."
mg "The tri-alphas have their \"butt beer\", \"nerd puncher\" and \"skank hunt\"..."
mg "...you have your pledge board..."
mg "...and who knows what's going on in the Alpha Nu Omega mansion with their Dante week or whatever they tried naming it."
if ep4_wearHelmet:
    scene ep4_magnar1 with dissolve
elif True:
    scene ep4_magnar1b with dissolve
mc "What's the tri-betas' tradition?"
scene ep4_magnar3 with dissolve
mg "We engage in nightly games of Dungeons and Gremlins and review the new recruits' intelligence in various forms of tests."
mg "It's a much more friendly environment for a freshman."
scene ep4_magnar4 with dissolve
mc "What can I say? Different strokes..."
scene ep4_magnar3 with dissolve
mg "Different indeed."
mg "*{i}Sigh{/i}* Are you guys bullying the other fraternities as well or is it just us who are your punching bag?"
scene ep4_magnar4 with dissolve
mc "No, it's not just you guys."
mc "We're pranking the other frats, too."
scene ep4_magnar7 with dissolve
mg "Haha. That's nice to hear."
scene ep4_magnar4 with dissolve
if dtype > 0:
    mc "Hey, it wasn't me who wrote that task on the pledge board."
elif True:
    mc "Look, I'm sorry. I didn't write that task on the pledge board."
scene ep4_magnar3 with dissolve
mg "No, I fully grasp the situation. You're just the marionette..."
mg "...at least for this semester."
mg "I can't give you the permission to do what you ask."
mg "And I'd rather not see it be done against our will."
scene ep4_magnar7b with dissolve
mg "But...like the years before..."
mg "Saying no would be the definition of insanity."
mg "I'll be the martyr for your mission..."
mg "...for {color=#36ca2b}$${/color}."
scene ep4_magnar4 with dissolve
show screen moneymsg
menu:
    "Pay for it ({color=#36ca2b}$${/color})" if money > 1:
        $ ep4_paidMagnarWedgie = True
        $ mny(-2)
        mc "Ok, I can do that."
        hide screen moneymsg
        scene ep4_magnar7b with dissolve
        mg "Now what happens? Do we find your friends first?"
        scene ep4_magnar4 with dissolve
        mc "We could just record it on my phone right here."
        mc "It would be less humiliating and over in a minute."
        scene ep4_magnar9 with dissolve
        mg "*{i}Mumbles{/i}* Less humiliating, he says."
        mg "Ok. Go ahead."
        $ bios_history_magnar += "I paid to give Magnar a wedgie. He didn't seem thrilled about it.\n\n"
        $ bios_name_magnar = True
        $ chat_new_bios = True
    "Don't pay for it" if True:
        hide screen moneymsg
        $ ep4_paidMagnarWedgie = False
        mc "Never mind. This was a stupid idea."
        if ep4_wearHelmet:
            scene ep4_magnar with dissolve
        elif True:
            scene ep4_magnarb with dissolve
        mg "Then I'll fear the future to come."
        if not affinity == "DIK":
            $ RPnerds += 1
            if ep4_wearHelmet:
                scene ep4_magnar1 with dissolve
            elif True:
                scene ep4_magnar1b with dissolve
            mc "You'll have nothing to fear from me. I was just looking for an easy way out."
            mc "I'm not going to give you or your friends a wedgie."
            mc "I know what that feels like."
        $ bios_history_magnar += "I didn't give Magnar a wedgie.\n\n"
        $ bios_name_magnar = True
        $ chat_new_bios = True

label ep4_jj_label:
scene ep4_jj
js "Thank you so much!"
scene ep4_jj1 with dissolve
isa "You're welcome."
isa "You can always come to me if you need any help."
scene ep4_jj2 with dissolve
js "Your friend is very sweet and helpful."
ji "Yeah, Bella is the best."
scene ep4_jj4 with dissolve
isa "Are you two done?"
scene ep4_jj2 with dissolve
ji "And she has a hard time accepting compliments."
js "Haha!"
scene ep4_jj5 with dissolve
ji "Do you want to look around in the library or go grab some lunch?"
scene ep4_jj6 with dissolve
js "Whatever you think, I'm just happy you're giving me a tour."
scene ep4_jj5 with dissolve
ji "Then let's do lunch, I'm getting hungry."
scene ep4_jj5b with dissolve
ji "Bella? Will you join us?"
isa "I'll go get my purse."
if ep4_wearHelmet:
    scene ep4_jj7b with dissolve
elif True:
    scene ep4_jj7 with dissolve
mc "(Josy!? No... Not with Jill.)"
scene ep4_jj8 with dissolve
ji "Excuse me for a minute."
ji "[name]!"
scene ep4_jj9 with dissolve
ji "Hey, I'm glad I ran into you."
ji "How are you?"
mc "I'm...ok."
scene ep4_jj11 with dissolve
ji "Listen, I didn't want to ask you this over the phone..."
ji "...it feels so impersonal."
ji "I was going to ask you if you're up for that date tomorrow afternoon?"
scene ep4_jj12 with dissolve
js "(A date...?)"
scene ep4_jj13 with dissolve
mc "Um...yeah. That works."
scene ep4_jj11 with dissolve
ji "I didn't mean to put you on the spot, but I've been thinking about something I wanted to show you..."
ji "...and tomorrow is a perfect day for it. It's supposed to be sunny."
scene ep4_jj13 with dissolve
mc "Where are we going?"
scene ep4_jj11 with dissolve
ji "I'll send you the address later. Meet me there at 3 p.m. and I'll show you."
scene ep4_jj17 with dissolve
ji "Oh, I'm so rude!"
scene ep4_jj18 with dissolve
ji "Josy! I would like you to meet [name]."
ji "He's a...um...friend of mine."
scene ep4_jj19 with dissolve
js "He's actually a...friend of mine, too."
scene ep4_jj20 with dissolve
ji "What a surprise! So, you know each other from before?"
ji "Did you go to school together?"
scene ep4_jj19 with dissolve
js "No, we worked together this summer in a minimart."
scene ep4_jj20 with dissolve
ji "That makes me happy to hear."
ji "I'm sure we all will get along together great, then."
scene ep4_jj24 with dissolve
ji "We were just going to get lunch. Do you want to join us?"
scene ep4_jj25 with dissolve
mc "Sorry, I have plans."
scene ep4_jj24 with dissolve
ji "That's fine. I'll see you tomorrow, then."
scene ep4_jj26 with dissolve
mc "Yeah... See you."
$ bios_history_josy += "Josy seems to be starting a friendship with Jill...\n\n"
$ bios_name_josy = True
$ bios_history_jill += "Jill seems to be starting a friendship with Josy...\n\n"
$ bios_name_jill = True
$ chat_new_bios = True

label ep4_date_app_label:
play music "<from 3.5>music/ep4/fleetwood.mp3"
scene ep4_pre_date_app with wipeleft
jac "Haha! Crabs?"
jac "Both of you?"
scene ep4_pre_date_app2 with dissolve
le "Yeah, but you don't go around telling people about this, you hear?"
scene ep4_pre_date_app3 with dissolve
jm "You needed to know this because..."
jm "...you might have them, too."
scene ep4_pre_date_app4 with dissolve
jac "I don't think so."
jac "Do you?"
scene ep4_pre_date_app5 with dissolve
mc "Hey, don't look at me. I have no clue what they are getting at."
scene ep4_pre_date_app6 with dissolve
le "Did either of you fuck Arieth recently?"
scene ep4_pre_date_app7 with dissolve
jac "Oh, fuck..."
scene ep4_pre_date_app6 with dissolve
le "Don't panic. We got the medication for it, but you should shave your pubes and any other hair in that area."
le "Also, we need to tell everyone who has fucked her to get checked up."
le "But you know...without it reaching the public that all DIKs might have an STD."
if ep4_monaSlap:
    scene ep4_pre_date_slap with dissolve
    mn "There he is!"
    jac "What's going on?"
    play sound "sound_effects/slap.mp3"
    if ep4_wearHelmet:
        scene ep4_pre_date_slap2 with hpunch
    elif True:
        scene ep4_pre_date_slap2b with hpunch
    mn "How dare you!?"
    if steamAchievements and ep3_lilyHatesYou and not config.console and not config.developer:
        $ achievement.grant("SLAPME")
        init:
            $ achievement.register("SLAPME")
        $ achievement.Sync()
    cam "Yeah!"
    scene ep4_pre_date_slap3 with dissolve
    jac "Hey! Easy there!"
    mn "You have some nerve fucking us without calling us afterwards!"
    scene ep4_pre_date_slap5 with dissolve
    jac "Dude...really?"
    mc "Uh...I'm sorry?"
    scene ep4_pre_date_slap3 with dissolve
    mn "Spare me that excuse! I don't care how many times you made us cum!"
    mn "Or that your dick is so big it would put pornstars to shame!"
    mn "We're done with you!"
    scene ep4_pre_date_slap7 with dissolve
    mc "(Thank you, Camila and Mona...)"
    jac "You fucked both of them? Man... Up top!"
    play sound "sound_effects/slap.mp3"
    if ep4_wearHelmet:
        scene ep4_pre_date_slap9b with vpunch
    elif True:
        scene ep4_pre_date_slap9 with vpunch
    jac "[name], you son of a bitch!!"
    jm "And he got the third slap, boys!"
    le "At least there's some sunshine on this crabby day."
    $ bios_history_mc += "I got the third slap from Mona.\n\n"
    $ bios_name_mc = True
    $ chat_new_bios = True

if ep4_wearHelmet:
    scene ep4_pre_date_app9 with dissolve
elif True:
    scene ep4_pre_date_app9b with dissolve
de "[mc_de_up]! I got the beer!"

if ep4_derekFuckedArieth:
    if ep4_wearHelmet:
        scene ep4_pre_date_app8 with dissolve
    elif True:
        scene ep4_pre_date_app8b with dissolve
    jac "Dude, you need to get your dick checked."
    if ep4_wearHelmet:
        scene ep4_pre_date_app10 with dissolve
    elif True:
        scene ep4_pre_date_app10b with dissolve
    de "I check it every morning. It's beautiful."
    if ep4_wearHelmet:
        scene ep4_pre_date_app11 with dissolve
    elif True:
        scene ep4_pre_date_app11b with dissolve
    jac "Arieth is passing crabs around like it's a fucking buffet."
    if ep4_wearHelmet:
        scene ep4_pre_date_app12
    elif True:
        scene ep4_pre_date_app12b
    de "She's...WHAT!?"
    if ep4_wearHelmet:
        scene ep4_pre_date_app11 with dissolve
    elif True:
        scene ep4_pre_date_app11b with dissolve
    jac "Chill, Leon's already got the medication for it."
elif True:
    if ep4_wearHelmet:
        scene ep4_pre_date_app8 with dissolve
    elif True:
        scene ep4_pre_date_app8b with dissolve
    jac "Hey! Did you bang Arieth, yet?"
    if ep4_wearHelmet:
        scene ep4_pre_date_app10 with dissolve
    elif True:
        scene ep4_pre_date_app10b with dissolve
    de "No, why? Did she ask about me?"
    if ep4_wearHelmet:
        scene ep4_pre_date_app11 with dissolve
    elif True:
        scene ep4_pre_date_app11b with dissolve
    jac "Nah, I'm just checking. She's passing crabs around."
    if ep4_wearHelmet:
        scene ep4_pre_date_app10 with dissolve
    elif True:
        scene ep4_pre_date_app10b with dissolve
    de "...and she's off my to-do list."

scene ep4_pre_date_app15 with dissolve
jm "Don't tell anyone about this, ok?"
jm "Especially not Dany!"
scene ep4_pre_date_app16 with dissolve
le "Why are you so paranoid? Why would they tell Dany about this?"
jac "Dude, just break up with her already."
scene ep4_pre_date_app18 with dissolve
jm "I can't...she said she might be pregnant."
le "No way!"
jac "Whoa..."
$ bios_history_jamie += "Leon and Jamie got crabs from fucking Arieth.\n\n"
$ bios_history_jamie += "Jamie's girlfriend Dany might be pregnant.\n\n"
$ bios_name_jamie = True
$ bios_history_dany += "Dany told Jamie she might be pregnant.\n\n"
$ bios_name_dany = True
$ bios_history_leon += "Leon and Jamie got crabs from fucking Arieth.\n\n"
$ bios_name_leon = True
$ chat_new_bios = True
if ep4_wearHelmet:
    scene ep4_pre_date_app20 with dissolve
elif True:
    scene ep4_pre_date_app20b with dissolve
de "Hey, let's go. This seems like it's none of our business."

if ep4_wearHelmet:
    scene ep4_pre_date_app21 with dissolve
    de "And pass that helmet! It's my turn."
scene ep4_afternoon_derek3 with dissolve
mc "Tell me what happened with Jade. I didn't see you all morning."
scene ep4_afternoon_derek3b with dissolve
de "Oh! I really laid into her!"
de "You don't try to teach me how to talk to feminists!"
scene ep4_afternoon_derek3c with dissolve
mc "Really?"
scene ep4_afternoon_derek3d with dissolve
de "No..."
de "She tore me a new asshole. Apparently, I lack respect for women's issues."
if ep4_derekFuckedArieth:
    de "So, she's off my to-do list."
elif True:
    de "So, just like Arieth, she's off my to-do list."
scene ep4_afternoon_derek3e with dissolve
mc "You don't want to fuck her anymore?"
scene ep4_afternoon_derek3f with dissolve
de "I get the feeling she would be the one doing the fucking with that temperament."
de "And a word of advice, she does {b}NOT{/b} like to be asked about menopause."
scene ep4_afternoon_derek4 with dissolve
de "What about you? Feeling better?"
scene ep4_afternoon_derek5 with dissolve
mc "I don't know how I feel."
scene ep4_afternoon_derek6 with dissolve
de "Horny?"
scene ep4_afternoon_derek5 with dissolve
mc "Not at the moment."
scene ep4_afternoon_derek6 with dissolve
de "Wanna be?"
scene ep4_afternoon_derek5 with dissolve
mc "Where are you going with this?"
scene ep4_afternoon_derek7 with dissolve
de "I...um...may have mentioned to Rusty that you're feeling a bit down."
scene ep4_afternoon_derek8 with dissolve
if not ep2_toldMayaTruthAboutDate:
    mc "First you tell Maya about me dating someone and now you tell Rusty things?"
    mc "Can I even trust you with secrets?"
elif True:
    mc "That's none of his business! Why did you tell him that?"
scene ep4_afternoon_derek9 with dissolve
de "Sorry, it just slipped out. I was a bit tipsy."
de "Alcohol kinda has that effect on me..."
de "But the good part is that he wants to help!"
scene ep4_afternoon_derek8 with dissolve
mc "Help me? Really?"
scene ep4_afternoon_derek11 with dissolve
de "When Tommy learned that Josy arrived, he was very pissed off."
de "Apparently, she's joining the HOTs, too."
scene ep4_afternoon_derek8 with dissolve
mc "Fuck... Why would she do that!?"
scene ep4_afternoon_derek11 with dissolve
de "Seems like you share that feeling with Tommy."
de "Anyway, Rusty called Stanley and checked if it was ok to drop by The Pink Rose tonight."
de "Are you in?"
scene ep4_afternoon_derek8 with dissolve
mc "Hm...maybe."
if ep3_choseSage:
    if ep3_sclubParty:
        mc "I did have a blast last time, but I think I'm gonna spend the night with Sage."
        scene ep4_afternoon_derek11 with dissolve
        de "Ok, that's cool."
    elif True:
        mc "That place isn't really for me. I think I'm gonna spend the night with Sage."
        scene ep4_afternoon_derek11 with dissolve
        de "Ok, that's cool."
elif ep3_sclubParty:
    mc "I did have a blast last time."
    scene ep4_afternoon_derek11 with dissolve
    de "Well, think about it."
elif True:
    mc "I don't know... That place wasn't really for me."
    scene ep4_afternoon_derek11 with dissolve
    de "Stop that. Don't be that guy."
    de "Join us. Drink some beer and just relax."
    de "Think about it."
scene ep4_afternoon_derek14 with dissolve
de "And also...I got something for you."
de "Well, I didn't really get it yet, but almost."
de "Can I borrow your phone?"
mc "Ok?"
scene ep4_afternoon_derek16 with dissolve
de "Give me a minute..."
de "All right... [name]... [roosterNickMCCustom]..."
$ swyperNickMCCustom = roosterNickMCCustom
mc "My Rooster nick?"
$ swyper_app_enabled = True
de "And you're all set!"
scene ep4_afternoon_derek17 with dissolve
mc "What did you do?"
scene ep4_afternoon_derek18 with dissolve
de "I installed an app for you."
de "A dating app."
scene ep4_afternoon_derek17 with dissolve
mc "A dating app? You really want me to get over your sister and Josy that bad?"
scene ep4_afternoon_derek20 with dissolve
de "I have overreacted...a tad...in the past about you and Maya, I'll give you that."
de "But that's not why. I just want to show you that there are other fish in the sea."
scene ep4_afternoon_derek18 with dissolve
de "And a lot of them may smell worse, some are rotten, some swim away really fast..."
scene ep4_date_app8b with dissolve
de "...some just go...*{i}blub blub{/i}*"
scene ep4_afternoon_derek18 with dissolve
de "...but there are also some really hot ones that you might wanna fuck."
scene ep4_afternoon_derek17 with dissolve
mc "I'm confused, are you talking about actual fish or women?"
scene ep4_afternoon_derek18 with dissolve
de "Just check that app! Swyper! Swipe in the direction that your cock moves."
de "Up if you get a boner and down if you don't."
scene ep4_afternoon_derek17 with dissolve
mc "Swyper, huh? What a stupid name."
scene ep4_afternoon_derek18 with dissolve
de "Maybe all the good ones were taken?"
de "Anyway... I think playing the field would be good for you."
stop music fadeout 3
scene ep4_afternoon_derek17 with dissolve
mc "Thanks, buddy..."
$ bios_history_derek += "Derek installed a dating app on my phone. He wanted me to try dating others.\n\n"
$ bios_name_derek = True
$ chat_new_bios = True
$ new_swype = True
if ep3_choseSage:
    jump ep4_afternoon_sage_label
elif ep3_choseDerek:
    jump ep4_afternoon_derek_label
elif True:
    jump ep4_afternoon_bella_label

label ep4_friday_math_label:
$ guideSuggestedPage = 107
if ep3_choseDerek and not ep4_called_sage:
    scene ep4_friday_math_phone with wipeleft
    play music "music/ep1/art_nouveau.mp3"
    $ renpy.pause()
elif True:
    scene ep4_friday_math_phone with Fade(1.5,1,1.5)
    play music "music/ep1/art_nouveau.mp3"
    ji "{i}We're going to get sweaty today! Bring some clothes for exercise.{/i}"
    mc "(What did she plan for us?)"
scene ep4_friday_math with dissolve
de "Hey..."
de "Did you try Swyper, yet?"
scene ep4_friday_math1 with dissolve
mc "I checked it out for a bit."
scene ep4_friday_math2 with dissolve
de "It's a good one, right?"
scene ep4_friday_math1 with dissolve
menu:
    "Tell him about Cathy" if True:
        $ ep4_toldDerekAboutCathy = True
        mc "Don't tell anyone about this, but I'm pretty sure that Cathy is using that app, too."
        scene ep4_friday_math3 with dissolve
        de "For real?"
        scene ep4_friday_math1 with dissolve
        mc "Yeah, I was swiping away when I saw a profile of someone that looked a lot like her."
        mc "But she wore a mask in her pictures."
        mc "And most of her pictures were pretty...sexual."
        scene ep4_friday_math3 with dissolve
        de "Please tell me you swiped up on her!"
        scene ep4_friday_math1 with dissolve
        if swyper_liked_cathy:
            mc "Of course I did. I wanted to know if it's her."
            mc "And even if it's not her...she was hot."
        elif True:
            mc "No, I didn't. I got too scared of the thought that it could be her."
            scene ep4_friday_math6 with dissolve
            de "Damn..."
            de "I need to check that shit out later."
        $ bios_history_derek += "I told Derek that Cathy is using Swyper.\n\n"
        $ bios_name_derek = True
        $ chat_new_bios = True
    "Don't tell him" if True:
        mc "Yeah, it's a fun one."
        $ bios_history_derek += "I didn't tell Derek that Cathy is using Swyper.\n\n"
        $ bios_name_derek = True
        $ chat_new_bios = True
scene ep4_friday_math with dissolve
de "I'm glad to see that you're taking my advice to heart."
de "It's just like when you're shopping for shit, it never hurts to look around before you decide."
scene ep4_friday_math8 with dissolve
mc "(Could it really be her?)"
if swyper_cathy_state == "ep4_done":
    mc "(That sexting was really hot...)"
elif True:
    mc "(Some of those shots were pretty hot...)"
mc "(She doesn't seem like the type of woman to do something like that.)"
if ep4_toldDerekAboutCathy:
    scene ep4_friday_math10 with dissolve
    de "*{i}Whispers{/i}* Dude... She's swiping up and down, right now."
    de "*{i}Whispers{/i}* It's gotta be her."
    menu:
        "Agree" if True:
            mc "*{i}Whispers{/i}* Yeah, I think you're right..."
        "Disagree" if True:
            mc "*{i}Whispers{/i}* Come one, it could be another app."
        "Joke" if True:
            mc "*{i}Whispers{/i}* Yeah, it's unheard of that you swipe up and down on a phone."
            mc "*{i}Whispers{/i}* Idiot."
scene ep4_friday_math12b2 with dissolve
mc "(Is it her? It can't be her...)"
mc "(Nope...it's her. It's definitely her.)"
scene ep4_friday_math13
ca "[name]?"
scene ep4_friday_math12 with dissolve
mc "Uh...yes?"
scene ep4_friday_math13 with dissolve
ca "Focus and do your exercises, please."
if minigames:
    stop music fadeout 3
scene ep4_friday_math12 with dissolve
mc "Sorry... Of course."
if not minigames:
    scene black with Fade(1.5, 1, 0.5)
    jump ep4_after_math_test
play music "music/ep3/sing_along_with_jim.mp3"
scene desk_bg_test with wipeleft
jump math101_test4

label ep4_after_math_test:
$ renpy.block_rollback()
if minigames:
    scene ep4_math_after with wiperight
    play music "music/ep1/art_nouveau.mp3"
elif True:
    scene ep4_math_after with fade
de "[mc_de_up]?"
scene ep4_math_after1 with dissolve
mc "Yeah?"
scene ep4_math_after with dissolve
de "I feel pretty uncomfortable..."
scene ep4_math_after1 with dissolve
mc "With what?"
scene ep4_math_after with dissolve
de "Both my sister and Josy are sitting over there, constantly looking over at you."
de "I feel like I'm caught in the middle of this."
de "And I love you, dude...but I love my sister more."
de "And Josy's actually great, too."
scene ep4_math_after1 with dissolve
mc "I'm not stopping you. Go to them if you're that uncomfortable being with me."
mc "But I'm not ready to talk to them."
scene ep4_math_after4 with dissolve
de "No, I'm not going to them."
de "Is there something I can do for you, to help you with this?"
de "I could tell you how they met and some stuff about their relationship."
scene ep4_math_after3 with dissolve
mc "The only thing I really want right now is time to think about it for myself."
scene ep4_math_after4 with dissolve
de "Gotcha..."
scene ep4_math_after3 with dissolve
mc "Can we leave? It's time to get yelled at again."
scene ep4_math_after with dissolve
de "Ugh...yeah."

scene ep4_math_after7 with dissolve
mc "What's up with your T-shirts? Are you that stupid or are you trying to trigger Jade?"
scene ep4_math_after8 with dissolve
de "I bought these novelty T-shirts back when I thought they were really funny."
de "I never got the chance to wear them when I lived at home..."
de "...so, I'm taking my chances now."
scene ep4_math_after9 with dissolve
mc "The T-shirts are still pretty stupid."
scene ep4_math_after10 with dissolve
de "Noted."
stop music fadeout 3
scene ep4_math_after11 with dissolve
de "Dude! Look."
play music "music/ep3/hot_mustard.mp3"
scene ep4_math_after12 with dissolve
if not ep3_choseDerek:
    mc "Who's that?"
    de "That's Bert...my roommate. The nerd..."
elif True:
    mc "Bert? What about him."
de "This is a golden opportunity."
if ep4_paidMagnarWedgie:
    de "It's wedgie time..."
    mc "Wait, dude. I already did the wedgie task."
    scene ep4_math_after13 with dissolve
    mc "Here, look!"
    stop music fadeout 5
    scene ep4_math_after14 with dissolve
    de "He let you record that?"
    de "It looks really staged..."
    scene ep4_math_after13 with dissolve
    play music "music/ep1/art_nouveau.mp3"
    mc "It is staged, I paid him for it."
    scene ep4_math_after14 with dissolve
    de "I'm not sure about this..."
    scene ep4_math_after13 with dissolve
    mc "Why? I have proof of giving a nerd a wedgie."
    mc "None of Rusty's rules were broken."
    scene ep4_math_after16 with dissolve
    de "Yeah... You're right."
    de "Let's go with that one! Nicely done!"
    de "Bert's ass lives to see another day."
elif True:
    mc "Oh, you mean for a wedgie."
    de "Get that camera ready, [mc_de]..."
    de "I'm going for it."
    de "It's ass crack time."
    scene ep4_math_after18 with dissolve
    $ renpy.pause()
    play sound "sound_effects/wedgie.mp3"
    scene ep4_math_after19 with vpunch
    be "Ah!!!"
    if ep3_choseDerek:
        de "That's for always ruining my fun and trying to hit me with that shitty drone!"
    elif True:
        de "That's for always ruining my fun!"
    scene ep4_math_after20 with dissolve
    be "Derek! You dick!"
    stop music
    play sound "sound_effects/hit.mp3"
    scene ep4_math_after21 with vpunch
    de "Oof!!!"
    be "That's for always staying up late!"
    play sound "sound_effects/hit.mp3"
    scene ep4_math_after23b with hpunch
    be "This is for always farting when you sleep!"
    mc "(Um...should I stop filming this?)"
    play sound "sound_effects/hit.mp3"
    scene ep4_math_after23 with hpunch
    de "Ouch!!!"
    play sound "sound_effects/hit.mp3"
    scene ep4_math_after23b with hpunch
    $ renpy.pause(0.5)
    play sound "sound_effects/hit.mp3"
    scene ep4_math_after23 with hpunch
    $ renpy.pause(0.5)
    play sound "sound_effects/hit.mp3"
    scene ep4_math_after23b with hpunch
    if ep3_choseDerek:
        be "And that's for ruining one of my drones!"
    elif True:
        $ renpy.pause(0.5)
    play sound "sound_effects/wedgie.mp3"
    scene ep4_math_after22 with vpunch
    be "And that's for being naked all the time!"
    scene ep4_math_after24 with dissolve
    $ renpy.pause()
    scene ep4_math_after25 with dissolve
    mc "..."
    mc "Well..."
    mc "..."
    mc "You did it."
    $ bios_history_derek += "Derek gave his roommate Bert a wedgie.\n\n"
    $ bios_name_derek = True
    $ chat_new_bios = True
    play music "music/ep1/art_nouveau.mp3"
$ bios_bert = True
$ bios_name_bert = True
label ep4_gender_label:
$ guideSuggestedPage = 108
scene ep4_gender with wipeleft
de "I don't know about you, [mc_de]..."
de "...but I'm getting fucking sick of this class."
de "This class is like a band-aid on my balls."
de "And I keep ripping it off only to find it there again the next day."
de "It's the last time I'll take my sister's advice for something like this."
scene ep4_genderb with dissolve
de "She baited me. She baited me good."
de "With all that empty promise of easy credits and vaginas."
de "You know that feeling you get when you eat too much food?"
de "One look at most of these girls is enough for me to get full and go ompf."
scene ep4_gender1 with dissolve
mc "I'm pretty sick of this class, too."
scene ep4_gender2 with dissolve
de "I hate Wendy."
de "But today...I'll break free. Just watch me."
scene ep4_gender1 with dissolve
mc "How will you do that?"
scene ep4_gender2 with dissolve
de "As soon as it's time to choose a partner..."
de "...I'll pounce."
de "Anyone but Wendy. That's my goal."
de "I think I might have a shot at her ugly friend...Minny."
scene ep4_gender1 with dissolve
mc "Her name is Minny? Like the mouse?"
scene ep4_gender4 with dissolve
de "She does look like a fat rodent."

scene ep4_gender6 with dissolve
my "[name]? Can we talk, please?"
scene ep4_gender7 with dissolve
if dtype > 0:
    mc "Go away, Maya."
elif True:
    mc "Please... Leave me alone, Maya."
scene ep4_gender6 with dissolve
my "Is five minutes too much to ask for?"
scene ep4_gender7 with dissolve
if dtype > 0:
    mc "I said...go away. Please."
elif True:
    mc "I said leave me alone."
de "Man..."
scene ep4_gender9 with dissolve
ja "Ok, everyone. Let's get down and dirty and discuss feminism."
ja "I know that many of you have waited for this subject matter so let's not waste any time."
ja "I want to hear your passionate thoughts and views on why feminism is needed in this world."
ja "Everyone, find a partner."
scene ep4_gender10 with dissolve
de "Minny! Hey!"
stop music fadeout 3
scene ep4_gender11 with dissolve
my "Wait!"
scene ep4_gender12 with dissolve
mc "Hey, you! Let's partner up!"
scene ep4_gender13 with dissolve
stu "Uh...ok..."
jump gender101_test4

label ep4_after_gender_test4_label:
scene ep4_gender_after with dissolve
my "...wow."
my "You know..."
my "The things I told you, I wasn't going to tell anyone."
my "Ever!"
scene ep4_after_gender2 with dissolve
my "And I really was going to tell you."
my "Maybe that doesn't mean anything to you..."
my "...but for me...it means a lot."
scene ep4_after_gender3 with dissolve
my "I'll still be here for you...if you let me."
my "Please..."
my "...just don't forget that."
scene ep4_after_gender4 with dissolve
$ renpy.pause()
scene ep4_after_gender5 with dissolve
$ renpy.pause()
$ bios_history_maya += "Maya approached me trying to talk, but I wasn't ready for it and that made her sad.\n\n"
$ bios_name_maya = True
$ chat_new_bios = True
play music "music/ep1/energetic.mp3"
scene ep4_after_gender6
mi "You are wrong on so many levels it's baffling!"
scene ep4_after_gender7
de "I have full right to my opinions!"
scene ep4_after_gender6
mi "And that's exactly what those are! Opinions!"
mi "Opinions steeped in ignorance."
mi "Opinions that you treat like fact."
mi "Your opinions are highly temperamental, juvenile, misogynistic and have zero relevance to the facts and ironically even to the class literature."
mi "If you just had read the first paragraph you would clearly have known that feminism has always been about equality."
scene ep4_after_gender8
de "But-"
mi "And I'm not talking about female equality, I'm talking about mankind equality."
mi "Take a note from the French Revolution and The Revolutionary war where..."
scene ep4_after_gender9
de "W-Wendy?"
de "Can we talk?"
stop music fadeout 3
mi "Hey! We're having a discussion here!"

scene ep4_gender_dad with fade
play music "music/ep2/wings.mp3"
mc "(...)"
scene ep4_gender_dad1 with dissolve
mc "(What am I doing...?)"
scene ep4_gender_dad1b with dissolve
play sound "sound_effects/dial_tone.mp3"
mc "(...)"
scene ep4_gender_dad2 with dissolve
mc "Hey..."
scene ep4_gender_dad3 with dissolve
dad "{i}Son, I'm a bit busy at the moment.{/i}"
dad "{i}Did something happen? Is it important?{/i}"
scene ep4_gender_dad2 with dissolve
mc "Dad, I-"
scene ep4_gender_dad2b with dissolve
mc "No... It's not important."
mc "I had a bit of a dilemma..."
mc "My mind is going back and forth when I think about it and I don't know which way to go."
scene ep4_gender_dad3 with dissolve
dad "{i}You know exactly what to do, son.{/i}"
dad "{i}Do what I always taught you to do.{/i}"
dad "{i}Follow your heart.{/i}"
scene ep4_gender_dad2 with dissolve
mc "Follow my heart... Right..."
mc "Thanks, dad."
mc "I'll call you another time when you're not busy."
scene ep4_gender_dad3 with dissolve
dad "{i}Looking forward to it! I'd love to catch up with all of your crazy adventures."
dad "{i}Love you, son!"
scene ep4_gender_dad2b with dissolve
stop music fadeout 3
mc "Love you, dad."
if not ep3_acceptedJade:
    scene ep4_gender_dad10 with dissolve
    $ renpy.pause()
    jump ep4_jill_date_label

label ep4_gender_jade_label:
scene ep4_gender_dad1 with dissolve
$ renpy.pause()
play music "music/ep4/piano_cinematic.mp3"
scene ep4_gender_jade1c with dissolve
$ renpy.pause()
scene ep4_gender_jade1d with dissolve
ja "..."
scene ep4_gender_jade2 with dissolve
ja "Three years ago, Stephen came home drunk on a Saturday night."
ja "He had been out celebrating after yet again selling stocks from a very successful trade. As if we need more money..."
ja "He fumbled with the keys in the lock and when he finally managed to open the door, I was almost by it to unlock it for him."
scene ep4_gender_jade3 with dissolve
ja "He smiled a big goofy smile and gave me a slobbery kiss."
ja "I could taste that he had been indulging himself with his favorite scotch..."
ja "...that smoky flavor can't be mistaken for anything else."
scene ep4_gender_jade4 with dissolve
ja "He grabbed my ass and walked with me towards the bedroom."
ja "A drunk man isn't a turn on for a woman..."
ja "...especially when you're sober..."
ja "...but I didn't want his victorious day to end in disappointment, so I didn't resist him."
scene ep4_gender_jade3b with dissolve
ja "He fumbled with the buttons on my blouse, they got unbuttoned, but only due to force."
ja "That blouse was ruined in the process..."
scene ep4_gender_jade6 with dissolve
ja "He got on top of me and started to kiss my neck."
ja "And then he whispered into my ear..."
scene ep4_gender_jade7 with dissolve
ja "Cathy. Oh, Cathy."
ja "That was the first time I saw the signs."
scene ep4_gender_jade4 with dissolve
ja "Now, Cathy is a dear friend of mine. We've been teaching here at B&R for nearly ten years together."
ja "We spend a lot of time in each other's company during our free time, as well."
ja "We're going to the gym, eating dinner, shopping and venting to each other."
scene ep4_gender_jade6 with dissolve
ja "It was like a dagger straight into my back, so deep that it plunged all the way in and pierced my heart."
scene ep4_gender_jade9 with dissolve
ja "As he continued to kiss my neck, I couldn't keep the tears from falling."
ja "I never dared to confront him about it. Nor Cathy..."
scene ep4_gender_jade10 with dissolve
ja "I don't want or need to know if there was some truth behind those drunken words."
ja "Because it didn't matter..."
scene ep4_gender_jade9 with dissolve
ja "The love for my husband had already started fading for me that night..."
ja "I didn't want that to happen for Cathy, too."
scene ep4_gender_jade4c with dissolve
mc "Why are you telling me this?"
scene ep4_gender_jade10 with dissolve
ja "Because looking at you sitting here like this..."
ja "It's the same way I sat the night he whispered Cathy's name into my ear."
ja "All night. While he snored and slept like a drunken teenager. I just sat like that."
scene ep4_gender_jade4 with dissolve
$ guideSuggestedPage = 109
ja "I can recognize that feeling of betrayal from anywhere."
ja "What did she do? Maya, correct?"
scene ep4_gender_jade4b with dissolve
menu:
    "She kept things from me" if True:
        scene ep4_gender_jade4c with dissolve
        mc "She kept things from me..."
        mc "Secrets that would have changed a lot if she told me sooner."
        scene ep4_gender_jade4 with dissolve
        ja "I see."
        ja "Clear your head before you make your decision."
    "I don't want to talk about it" if True:
        mc "You're right that it's a feeling of betrayal...but I don't want to talk to anyone about it."
        scene ep4_gender_jade4 with dissolve
        ja "Give it time. Clear your head before you make your decision."
scene ep4_gender_jade4c with dissolve
mc "What was your decision?"
scene ep4_gender_jade10 with dissolve
ja "My decision was to ignore it...for the sake of our family."
ja "The first time he cheated, I just had a hunch. But that hunch hurt like hell."
ja "The second time, I found proof, but I remained silent."
ja "And after the third time..."
scene ep4_gender_jade10b with dissolve
ja "..."
scene ep4_gender_jade10 with dissolve
ja "Even if you choose apathy...rage doesn't escape you. It just builds up."
scene ep4_gender_jade19 with dissolve
ja "Haha... Look at me confiding in you, right now."
ja "It feels nice."
ja "You and I already have one secret to keep."
menu:
    "Make a move on her" if True:
        $ ep4_jadeOffer = True
        scene ep4_gender_jade21 with dissolve
        ja "..."
        scene ep4_gender_jade22 with dissolve
        ja "Um..."
        scene ep4_gender_jade23 with dissolve
        ja "Not here..."
        ja "Last time was a stupid risk."
        scene ep4_gender_jade24 with dissolve
        mc "I'm sorry... I shouldn't have done that."
        scene ep4_gender_jade25 with dissolve
        ja "Relax. I didn't say \"no\"..."
        ja "...I said \"not here\"."
        scene ep4_gender_jade24 with dissolve
        mc "Then where...?"
        scene ep4_gender_jade25 with dissolve
        ja "Tonight..."
        ja "The school parking lot at 10 p.m."
        ja "Come alone and don't mention this to a soul."
        scene ep4_gender_jade27 with dissolve
        $ renpy.pause()
        stop music fadeout 5
        scene ep4_gender_dad10 with dissolve
        $ renpy.pause()
        $ bios_history_jade += "Jade told me about her issues and sympathized with me. I made a move on her and she told me to meet her in the school parking lot at night.\n\n"
        $ bios_name_jade = True
        $ chat_new_bios = True
    "Leave" if True:
        scene ep4_gender_jade4c with dissolve
        mc "Thank you for telling me..."
        mc "I promise that it will stay with me."
        scene ep4_gender_jade20 with dissolve
        ja "..."
        stop music fadeout 5
        scene ep4_gender_dad10 with dissolve
        $ renpy.pause()
        $ bios_history_jade += "Jade told me about her issues and sympathized with me. I didn't make a move on her.\n\n"
        $ bios_name_jade = True
        $ chat_new_bios = True

label ep4_jill_date_label:
scene ep4_jill_date with wipeleft
mc "(I'm really not in the mood for this...)"
mc "(Where is she?)"
ji "[name]! Over here!"
play music "music/ep4/optimistic.mp3"
scene bg anim_jill_date_ep4 movie with dissolve
mc "(Wow...)"
scene ep4_jill_date2b with dissolve
ji "Hi!"
scene ep4_jill_date3 with dissolve
menu:
    "Say hi" if True:
        mc "Hey!"
    "Compliment her" if True:
        scene ep4_jill_date2 with dissolve
        if dtype > 0:
            mc "You look very hot in that outfit."
            scene ep4_jill_date4 with dissolve
            ji "Um. Ok. Thanks."
        elif True:
            $ RPjill += 1
            mc "What a nice outfit."
            scene ep4_jill_date5 with dissolve
            ji "Aw, thanks!"
scene ep4_jill_date6 with dissolve
ji "I didn't want to spoil the surprise of what we're doing..."
ji "...but I guess it's pretty obvious now, huh?"
scene ep4_jill_date7 with dissolve
mc "Yeah..."
menu:
    "Yoga" if True:
        mc "Yoga, huh?"
        scene ep4_jill_date8 with dissolve
        ji "No...we're going to play tennis."
        scene ep4_jill_date7 with dissolve
        mc "I'm joking... It was stupid."
        scene ep4_jill_date7b with dissolve
        ji "Haha..."
    "Bowling" if True:
        mc "We're going bowling, right?"
        scene ep4_jill_date8 with dissolve
        ji "No...we're going to play tennis."
        scene ep4_jill_date7 with dissolve
        mc "I'm joking... It was stupid."
        scene ep4_jill_date7b with dissolve
        ji "Haha..."
    "Tennis" if True:
        mc "It's been a long time since I played tennis."
        mc "I'm not sure if I still got it."
        scene ep4_jill_date6 with dissolve
        ji "Then we will find out today!"
scene ep4_jill_date12 with dissolve
mc "After you..."
scene ep4_jill_date14b with dissolve
ji "Hey... What happened?"
scene ep4_jill_date14 with dissolve
mc "Nothing... What do you mean?"
scene ep4_jill_date14b with dissolve
ji "Hm...call it intuition, but you seem sad."
scene ep4_jill_date14 with dissolve
mc "I don't think it's a good thing to talk about this during a first date."
mc "This is not fair to you."
mc "Maybe I should have called this off? I'm not feeling like myself today."
scene ep4_jill_date17 with dissolve
ji "Everyone has bad days."
ji "Now that I know that you're processing something, I'll try harder to cheer you up."
scene ep4_jill_date18 with dissolve
mc "I don't know... I tend to sulk for a while."
scene ep4_jill_date19 with dissolve
ji "..."
mc "What are you doing?"
scene ep4_jill_date20 with dissolve
ji "A silly face. Is it working?"
$ guideSuggestedPage = 110
scene ep4_jill_date19 with dissolve
menu:
    "Positive response" if True:
        $ RPjill += 1
        mc "Haha... Maybe a little bit."
        scene ep4_jill_date22 with dissolve
        ji "Great! That's a start."
        $ bios_history_jill += "Jill tried to cheer me up by making a silly face.\n\n"
        $ bios_name_jill = True
        $ chat_new_bios = True
    "Negative response" if True:
        if dtype > 0:
            mc "I'm not a child..."
        elif True:
            mc "No, not for this."
        scene ep4_jill_date22b with dissolve
        ji "Ok... Tough crowd."
        $ bios_history_jill += "Jill tried to cheer me up by making a silly face. I wasn't amused.\n\n"
        $ bios_name_jill = True
        $ chat_new_bios = True
scene ep4_jill_date23 with dissolve
ji "Listen, I bet that you will feel so much better if you just tell me why you're sad."
ji "Then we can move past it."
scene ep4_jill_date24 with dissolve
mc "I don't know if you want to hear this, really..."
mc "I wouldn't want to hear it if our roles were reversed."
scene ep4_jill_date23 with dissolve
ji "If it's something that big, I think it's better telling me it now than waiting for it to drop like a bomb later."
scene ep4_jill_date24 with dissolve
mc "Ok..."
mc "I've kind of been dating multiple girls lately."
mc "Two of them lied to me pretty big time and I recently found out about it."
mc "Right now, I feel pretty hurt and irritated in general."
scene ep4_jill_date26 with dissolve
mc "And I know you probably don't want to hear that I'm dating others..."
mc "...but I'm so unsure about so many things right now."
mc "I'm unsure about myself."
scene ep4_jill_date27 with dissolve
ji "It's not a shock to hear that you're dating others."
ji "Single people date and you're a cute guy."
ji "It's different from being in a relationship and seeing others. That's just despicable."
scene ep4_jill_date28 with dissolve
ji "I admit, it's not the best thing to hear for a girl... That there's competition and all."
ji "If the guy is worth the time, there's bound to be jealousy involved."
ji "But it's not dropping a bomb. Unless there's more to your story...?"
scene ep4_jill_date26 with dissolve
mc "One of the girls I've been dating is Josy."
scene ep4_jill_date28 with dissolve
ji "Now, see... I could sense that you were a bit off in the library."
ji "So, that's why?"
ji "She seems like a really sweet girl."
scene ep4_jill_date24 with dissolve
mc "Yeah, I don't know what to tell you..."
scene ep4_jill_date23 with dissolve
ji "Was that all you needed to get off your chest?"
scene ep4_jill_date24 with dissolve
mc "Yeah, for now."
scene ep4_jill_date27 with dissolve
ji "Good. I think that we should have our date now and you leave all those feelings you feel at the moment in this spot."
ji "When we're done, you can come back here and get them if you feel that you need them."
scene ep4_jill_date24 with dissolve
mc "Haha, that sounds weird."
mc "But I'll try that."
scene ep4_jill_date28 with dissolve
ji "Great! Let's go have fun!"
scene ep4_jill_date35 with dissolve
mc "Jill, thanks for listening..."

label ep4_pre_tennis_label:
scene ep4_pre_tennis with dissolve
ji "Hi! I've booked a court for two people."
ji "The name's Jill."
scene ep4_pre_tennis1 with dissolve
rc "Let me check... Jill... Found you!"
scene ep4_pre_tennis1b with dissolve
rc "I'm terribly sorry for the inconvenience, but a pipe burst in the ladies' dressing room sometime during lunch."
rc "It has been isolated and the pipe should be fixed within a few hours..."
rc "Until then, we have divided the men's dressing room into two, one side for men and one side for women..."
rc "...but, if you want to use the showers, you'll have to shower in shifts using the occupied sign in the dressing room."
scene ep4_pre_tennis with dissolve
ji "Ok, that's a bit inconvenient, but it shouldn't be a problem."
ji "Sorry about your water leak. I hope the damages aren't that bad."
scene ep4_pre_tennisb with dissolve
rc "Thank you so much! Unless you have any questions, you're on court number two today."
rc "Enjoy!"

label ep4_tennis_label:
scene ep4_tennis with wipeleft
mc "I'm a bit rusty when it comes to the rules..."
scene ep4_tennis1 with dissolve
ji "We don't have to play with strict rules, it's just for fun, right?"
scene ep4_tennis2 with dissolve
mc "Yeah, I hope I remember how to serve. I always found that very tricky."
if minigames:
    if tutorials:
        show screen tennis_tutorial_screen with dissolve
        $ renpy.pause()
    label ep4_tennis_label2:
    hide screen tennis_tutorial_screen with dissolve
    menu:
        "Play best out of 1 set (Easy)" if True:
            $ ep4_bestOutOf3 = False
        "Play best out of 3 sets (Hard)" if True:
            $ ep4_bestOutOf3 = True
scene ep4_tennis1 with dissolve
ji "You'll figure it out."
if ep4_bestOutOf3:
    ji "Let's play best out of three sets! I think that's plenty for a beginner."
elif True:
    ji "Let's play one set! I think that's enough for a beginner."
if not minigames:
    $ tmpInt = 0
    scene bg anim_mc_serve_ep4 movie with dissolve
    $ renpy.pause(4)
    play sound "sound_effects/tennis_hit.mp3"
    scene ep4_tennis_jill_hit
    pause
    scene ep4_tennis_mc_neutral
    menu:
        "Forehand" if True:
            play sound "sound_effects/tennis_hit.mp3"
            scene ep4_tennis_mc_hit3
            pause
            play sound "sound_effects/tennis_miss.mp3"
            scene ep4_tennis_jill_miss2
            pause
            scene ep4_tennis_jill_lose1
            ji "Argh! So close!"
            $ tmpInt += 1
        "Backhand" if True:
            play sound "sound_effects/tennis_hit.mp3"
            scene ep4_tennis_mc_hit4
            pause
            play sound "sound_effects/tennis_miss.mp3"
            scene ep4_tennis_jill_miss
            pause
            scene ep4_tennis_jill_lose2
            ji "Haha! Missed it!"
            $ tmpInt += 1
        "Smash" if True:
            play sound "sound_effects/tennis_miss.mp3"
            scene ep4_tennis_mc_miss2
            pause
            scene ep4_tennis_jill_win1
            ji "Yes!"

    scene bg anim_mc_serve_ep4 movie with dissolve
    $ renpy.pause(4)
    play sound "sound_effects/tennis_hit.mp3"
    scene ep4_tennis_jill_hit2
    pause
    scene ep4_tennis_mc_neutral2
    menu:
        "Forehand" if True:
            play sound "sound_effects/tennis_miss.mp3"
            scene ep4_tennis_mc_miss2
            pause
            scene ep4_tennis_jill_win2
            ji "Haha! That's my point!"
        "Backhand" if True:
            play sound "sound_effects/tennis_hit.mp3"
            scene ep4_tennis_mc_hit6
            pause
            play sound "sound_effects/tennis_hit.mp3"
            scene ep4_tennis_jill_hit3
            pause
            scene ep4_tennis_mc_neutral2
            menu:
                "Forehand" if True:
                    play sound "sound_effects/tennis_miss.mp3"
                    scene ep4_tennis_mc_miss2
                    pause
                    scene ep4_tennis_jill_win2
                    ji "Haha! That's my point!"
                "Backhand" if True:
                    play sound "sound_effects/tennis_miss.mp3"
                    scene ep4_tennis_mc_miss3
                    pause
                    scene ep4_tennis_jill_win2
                    ji "Haha! That's my point!"
                "Smash" if True:
                    play sound "sound_effects/tennis_hit.mp3"
                    scene ep4_tennis_mc_hit2
                    pause
                    play sound "sound_effects/tennis_miss.mp3"
                    scene ep4_tennis_jill_miss
                    pause
                    scene ep4_tennis_jill_lose3
                    ji "You're good!"
                    $ tmpInt += 1
        "Smash" if True:
            play sound "sound_effects/tennis_hit.mp3"
            scene ep4_tennis_mc_hit2
            pause
            play sound "sound_effects/tennis_miss.mp3"
            scene ep4_tennis_jill_miss3
            pause
            scene ep4_tennis_jill_lose3
            ji "You're good!"
            $ tmpInt += 1

    scene bg anim_mc_serve_ep4 movie with dissolve
    $ renpy.pause(4)
    play sound "sound_effects/tennis_hit.mp3"
    scene ep4_tennis_jill_hit
    pause
    scene ep4_tennis_mc_neutral
    menu:
        "Forehand" if True:
            play sound "sound_effects/tennis_hit.mp3"
            scene ep4_tennis_mc_hit3
            pause
            play sound "sound_effects/tennis_miss.mp3"
            scene ep4_tennis_jill_miss4
            pause
            scene ep4_tennis_jill_lose1
            ji "Argh! So close!"
            $ tmpInt += 1
        "Backhand" if True:
            play sound "sound_effects/tennis_hit.mp3"
            scene ep4_tennis_mc_hit5
            pause
            play sound "sound_effects/tennis_miss.mp3"
            scene ep4_tennis_jill_miss
            pause
            scene ep4_tennis_jill_lose2
            ji "Haha! Missed it!"
            $ tmpInt += 1
        "Smash" if True:
            play sound "sound_effects/tennis_hit.mp3"
            scene ep4_tennis_mc_hit2
            pause
            play sound "sound_effects/tennis_miss.mp3"
            scene ep4_tennis_mc_net
            pause
            scene ep4_tennis_jill_win1
            ji "Yes!"
    if tmpInt > 1:
        $ ep4_wonTennis = True
    elif True:
        $ ep4_wonTennis = False
    jump ep4_after_tennis_label
jump ep4_tennis_game_label

label ep4_after_tennis_label:
if ep4_wonTennis:
    scene ep4_after_tennis with dissolve
    ji "*{i}Breathes heavily{/i}* Wow! You're really good!"
    ji "That was definitely not a beginner I just played."
    scene ep4_after_tennis1 with dissolve
    mc "Thanks...but I really had to work for it."
    mc "I'm impressed."
elif True:
    scene ep4_after_tennis with dissolve
    ji "Hey, nice game!"
    scene ep4_after_tennis1 with dissolve
    mc "Thanks, but I need more practice to be at your level."
    scene ep4_after_tennis with dissolve
    ji "Don't beat yourself up over it. You did great!"
scene ep4_after_tennis5 with dissolve
ji "*{i}Phew{/i}*"
mc "You're exhausted too, huh?"
scene ep4_after_tennis6 with dissolve
ji "Yeah! I'm drained!"
scene ep4_after_tennis8 with dissolve
mc "Do you play often?"
scene ep4_after_tennis6 with dissolve
ji "Once in a while. I like variation in my exercise."
ji "I usually rotate between tennis, running, gym and yoga."
ji "How about you? You practice martial arts, right?"
scene ep4_after_tennis8 with dissolve
mc "Yes, but I practice on my own. I never went to a real class or anything."
mc "Aside from that, I like running and exercising outdoors."
scene ep4_after_tennis6 with dissolve
ji "You really do like to teach yourself things. Both physical training and music."
scene ep4_after_tennis8 with dissolve
mc "I haven't had another option, really."
scene ep4_after_tennis6 with dissolve
ji "Right."
scene ep4_after_tennis14 with dissolve
ji "Let's freshen up with a shower before we leave."
scene ep4_after_tennis15 with dissolve
mc "That's right... Temporary joint showers."
scene ep4_after_tennis16 with dissolve
ji "Um...yeah. It's pretty weird, huh?"
if affinity != "CHICK" or not renpy.variant("pc"):
    $ ep4_jillShower = False
    scene ep4_after_tennis18 with dissolve
    stop music fadeout 3
    ji "You go ahead and shower first, I'll go stretch meanwhile."
    jump ep4_jill_date_part2_label
elif True:
    scene ep4_after_tennis15 with dissolve
    $ ep4_jillShower = True
    menu:
        "Let her shower first" if True:
            mc "I'll wait outside until you're done."
            scene ep4_after_tennis18 with dissolve
            ji "Stop, don't be silly. You're not going to peek, are you?"
            scene ep4_after_tennis19 with dissolve
            menu:
                "Yes" if True:
                    $ RPjill -= 1
                    $ dk(1)
                    mc "Maybe just a little bit."
                    scene ep4_after_tennis20 with dissolve
                    ji "You better not."
                "No" if True:
                    $ RPjill += 1
                    $ dk(-1)
                    mc "Of course not."
                    scene ep4_after_tennis18 with dissolve
                    ji "Then we shouldn't have a problem."
            scene ep4_after_tennis19 with dissolve
            menu:
                "Shower with Jill" if True:
                    stop music fadeout 3
                    mc "Let's do this, then."
                "Don't shower with Jill" if True:
                    $ ep4_jillShower = False
                    stop music fadeout 3
                    mc "No, really. You go ahead, I'll wait in the dressing room until you're done."
                    jump ep4_jill_date_part2_label
        "Joke" if True:
            $ RPjill += 1
            mc "You're gonna have to promise not to peek then."
            scene ep4_after_tennis18 with dissolve
            ji "Haha! Me? What about you?"
            scene ep4_after_tennis19 with dissolve
            mc "Oh, I can handle my urges."
            mc "I'm just not sure if you can, too."
            scene ep4_after_tennis18 with dissolve
            stop music fadeout 3
            ji "I guess we'll see about that."
label ep4_jill_lewd_label:
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
$ renpy.sound.play("sound_effects/shower.mp3", channel="sfx2", loop=True)
play music "music/ep4/romantic_piano.mp3"
scene ep4_after_tennis25 with dissolve
mc "(She's on the other side of this wall...naked...)"
mc "(I better not think about that.)"
mc "Jill?"
scene ep4_after_tennis26 with dissolve
ji "Yeah?"
scene ep4_after_tennis27 with dissolve
mc "How's your shower?"
scene ep4_after_tennis28 with dissolve
ji "Haha! How's my shower?"
ji "It's great! Why do you ask?"
scene ep4_after_tennis29 with dissolve
mc "No reason."
scene ep4_after_tennis30 with dissolve
ji "How's yours?"
scene ep4_after_tennis31 with dissolve
mc "Warm...wet...and soapy."
scene ep4_after_tennis32 with dissolve
ji "No way! What a shock! That's just like mine. Haha!"
scene ep4_after_tennis33 with dissolve
mc "Yeah, yeah. But I think mine is a bit better than yours."
scene ep4_after_tennis34 with dissolve
ji "Yeah, right!"
ji "Here, let me feel..."
scene ep4_after_tennis34b with dissolve
ji "It's good, but it's not better than mine."
scene ep4_after_tennis35 with dissolve
menu:
    "Reach in" if True:
        $ ep4_touchedJillsBreasts = True
        mc "Oh really?"
        scene anim_jill_tits2_ep4 with dissolve
        ji "*{i}Gasps{/i}*"
        pause
        scene anim_jill_tits_ep4 with dissolve
        pause
        mc "Is this what I think it is?"
        ji "Um...yeah...it is..."
        ji "Maybe you should let it go?"
        scene ep4_after_tennis39 with dissolve
        mc "I'm really sorry."
        ji "(Did he really just touch my breast...?)"
        ji "(It was an accident...)"
        ji "(...but he didn't stop immediately.)"
        mc "..."
        mc "You win... Your shower is better."
        scene ep4_after_tennis40 with dissolve
        ji "Haha... I told you..."
        $ bios_history_jill += "I touched Jill's breasts by accident while showering.\n\n"
        $ bios_name_jill = True
        $ chat_new_bios = True
    "You win" if True:
        mc "You win! I'll take your word for it."
        ji "Haha!"
scene ep4_after_tennis41 with dissolve
ji "Ok, I'm done. I'm exiting the shower now."
$ renpy.music.stop(channel="sfx2", fadeout=3)
scene ep4_after_tennis42 with dissolve
mc "I'm done, too."
ji "No peeking..."
scene ep4_after_tennis43 with dissolve
mc "I won't."
mc "I'm...just coming over to get a towel."
scene ep4_after_tennis45 with dissolve
ji "*{i}Gasps{/i}*"
scene ep4_after_tennis46 with dissolve
ji "(Wow...)"
ji "(No! Not \"wow\"! Why did I do that?)"
scene ep4_after_tennis47 with dissolve
ji "[name]...?"
scene ep4_after_tennis48 with dissolve
mc "Yeah?"
scene ep4_after_tennis47 with dissolve
ji "I'm sorry...but the mirror...I peeked."
scene ep4_after_tennis48 with dissolve
mc "You did? Haha, why are you telling me that?"
scene ep4_after_tennis50 with dissolve
ji "It was an accident, but it still feels so wrong..."
ji "It's so not me."
scene ep4_after_tennis51 with dissolve
mc "It's ok. I can tell that it's not you."
scene ep4_after_tennis50 with dissolve
ji "No, it's not ok... I feel really stupid now."
ji "Especially since it was I who told you not to peek..."
scene ep4_after_tennis51 with dissolve
mc "Please, don't feel stupid. Like you said, it was an accident."
scene ep4_after_tennis54 with dissolve
ji "Yeah, it really was."
scene ep4_after_tennis55 with dissolve
menu:
    "Kiss her" if True:
        $ ep4_kissedJill = True
        mc "I think you're very cute for freaking out over that."
        scene ep4_after_tennis56 with dissolve
        ji "Haha, I wasn't freaking out."
        scene ep4_after_tennis57 with dissolve
        mc "Whatever it was..."
        mc "...I liked it."
        scene ep4_after_tennis58 with dissolve
        ji "(Wait...)"
        ji "(Is he trying to kiss me? Right now?)"
        scene ep4_after_tennis59 with dissolve
        ji "(He is! Oh... I...)"
        scene anim_jill_kiss_tennis_ep4 with dissolve
        $ renpy.pause()
        scene ep4_after_tennis61 with dissolve
        ji "Oh my... You actually...kissed me..."
        ji "Like this? In here?"
        scene ep4_after_tennis61b with dissolve
        mc "Sometimes you just have to go with the flow."
        scene ep4_after_tennis61 with dissolve
        ji "The flow, huh?"
        ji "I like it..."
        scene ep4_after_tennis62 with dissolve
        stop music fadeout 3
        ji "Haha, although I wish we hadn't been almost naked for our first real kiss."
        $ renpy.end_replay()
        $ persistent.ep4_lewd_jill = True
        $ calcScenes()
        $ bios_history_jill += "I kissed Jill after taking a shower at the tennis club.\n\n"
        $ bios_name_jill = True
        $ chat_new_bios = True
    "Don't kiss her" if not _in_replay:
        mc "Let's just forget that it happened."
        scene ep4_after_tennis56 with dissolve
        ji "All right..."

label ep4_jill_date_part2_label:
scene ep4_date_talk1 with wipeleft
play music "music/ep4/inspirational_piano_ambient.mp3"
ji "Tell me more about yourself. I feel like I don't have the complete picture of you."
scene ep4_date_talk2 with dissolve
mc "What do you want to know?"
scene ep4_date_talk1 with dissolve
ji "Do you have any siblings?"
scene ep4_date_talk2 with dissolve
mc "No, it's just been me and my dad."
mc "I don't have any close relatives either."
scene ep4_date_talk1 with dissolve
ji "Any pets?"
scene ep4_date_talk2 with dissolve
mc "No, but I always wanted a cat or a dog."
scene ep4_date_talk7 with dissolve
ji "Aw, I love dogs!"
ji "I never had one, but several friends of my family did."
ji "They used to let me pet and walk them."
scene ep4_date_talk2 with dissolve
mc "What about your family? Is it a big one?"
scene ep4_date_talk9 with dissolve
ji "No, it's not big. It's just me and my mom and dad."
ji "I had an older sister, but she passed away when I was young."
scene ep4_date_talk10 with dissolve
mc "I'm sorry..."
mc "And I know saying I'm sorry doesn't do anything for you."
scene ep4_date_talk9 with dissolve
ji "I don't choose to talk about her so much."
ji "I have my memories and mementos of her. That's what I need."
ji "She gives me strength daily and thinking about her, these days, only makes me happy and motivated."
scene ep4_date_talk10 with dissolve
mc "I'm glad to hear that."
scene ep4_date_talk9 with dissolve
ji "I do have a fair share of relatives, but we aren't that close and I don't consider them family."
ji "I'd say it's for appearances only."
scene ep4_date_talk10 with dissolve
mc "Appearances? Is that important to your family?"
scene ep4_date_talk9 with dissolve
ji "Well, we do have eyes on us, being who we are."
scene ep4_date_talk10 with dissolve
mc "Um...and who are you? I'm sorry, but I have no clue."
scene ep4_date_talk17 with dissolve
ji "Wait! You don't?"
scene ep4_date_talk18 with dissolve
mc "No? Should I?"
ji "(This is too good to be true!)"
scene ep4_date_talk19 with dissolve
ji "No, never mind. It's nothing important."
scene ep4_date_talk18 with dissolve
mc "Are you sure, it sounds like it is?"
scene ep4_date_talk21 with dissolve
ji "How do I explain this...?"
ji "None of the guys who approach me seem genuine."
ji "It's tough knowing what their intentions are, because of my family."
scene ep4_date_talk22 with dissolve
if ep3_bella_came_around or ep4_kissedJill:
    ji "With you, it's been different..."
elif True:
    ji "With you, it feels like it could be different..."
scene ep4_date_talk23 with dissolve
mc "Different?"
scene ep4_date_talk24 with dissolve
ji "Yes, but in a good way!"
ji "You get to know me for me and not for everything around me."
scene ep4_date_talk23 with dissolve
mc "I don't think I would treat you any differently if you told me who you are."
mc "Do you?"
scene ep4_date_talk24 with dissolve
ji "I don't know...but can we keep it this way? For now?"
scene ep4_date_talk23 with dissolve
mc "If it makes you feel better, it's fine by me."
scene ep4_date_talk24 with dissolve
ji "Haha! Great!"

scene ep4_jill2_date with wipeleft
ji "Hahaha! No way!?"
mc "I'm not lying! She pulled my ear while I was buck naked!"
scene ep4_jill2_date2 with dissolve
ji "Bella never told me those details."
scene ep4_jill2_date3 with dissolve
mc "Maybe she didn't want to embarrass me?"
scene ep4_jill2_date2 with dissolve
ji "Yeah, she isn't someone who would do that."
if ep3_bella_came_around:
    scene ep4_jill2_date5 with dissolve
    ji "I was so surprised when I realized that she liked you."
    scene ep4_jill2_date6 with dissolve
    mc "Why? You don't think I'm likable?"
    scene ep4_jill2_date7 with dissolve
    ji "Haha, I do! But it's very big that she does."
    ji "What can I say?"
    scene ep4_jill2_date8 with dissolve
    ji "It makes me more comfortable around you."
    scene ep4_jill2_date9 with dissolve
    if ep4_jillShower:
        mc "Hey, we've already shared a bed and showered next to each other."
    elif True:
        mc "Hey, we've already shared a bed."
    mc "I think we're past feeling uncomfortable."
    scene ep4_jill2_date10 with dissolve
    ji "[name]..."
elif True:
    scene ep4_jill2_date11 with dissolve
    ji "I have to say, I was a tad reluctant going out on a date with you."
    scene ep4_jill2_date12 with dissolve
    mc "Really? Why?"
    scene ep4_jill2_date11 with dissolve
    ji "Bella wasn't convinced that you're good for me."
    ji "She doesn't control what I do, but I do value her opinion."
    ji "I guess I'm a bit concerned whether she's right or wrong."
    scene ep4_jill2_date12 with dissolve
    menu:
        "I'm a nice guy" if True:
            $ ep4_jillNiceGuy = True
            mc "You'll have to decide that for yourself."
            mc "All I know is that I think I'm a nice guy."
            scene ep4_jill2_date15 with dissolve
            ji "That's good."
            $ bios_history_jill += "Jill wasn't sure that I was good for her, but I told her that I'm a nice guy.\n\n"
            $ bios_name_jill = True
            $ chat_new_bios = True
        "I'm probably not good for you" if True:
            $ ep4_jillNiceGuy = False
            mc "I'm probably not good for you."
            mc "I'm not the best person out there."
            mc "I have a lot of flaws and I make some lifestyle choices that you might not like."
            scene ep4_jill2_date11 with dissolve
            ji "I see."
            $ bios_history_jill += "Jill wasn't sure that I was good for her and I told her that I probably wasn't.\n\n"
            $ bios_name_jill = True
            $ chat_new_bios = True
$ guideSuggestedPage = 111
if ep4_jillNiceGuy:
    scene ep4_jill2_date8 with dissolve
    ji "What do you usually do on dates?"
elif True:
    ji "Um...what do you usually do on dates?"
if ep4_jillNiceGuy:
    scene ep4_jill2_date9 with dissolve
elif True:
    scene ep4_jill2_date12 with dissolve
mc "I haven't been on a lot of dates. Last time I had homemade dinner."
scene ep4_jill2_date15 with dissolve
ji "That sounds nice! Do you cook?"
scene ep4_jill2_date20 with dissolve
if ep3_choseBella:
    mc "No, but Bella promised to teach me."
    scene ep4_jill2_date8 with dissolve
    ji "She did? Just like that?"
    scene ep4_jill2_date9 with dissolve
    mc "I'm staying with her for a few days, due to the relationship problems I told you about."
    scene ep4_jill2_date23 with dissolve
    ji "Oh, I didn't realize it was that bad."
    ji "You could have called me, you know."
    scene ep4_jill2_date9 with dissolve
    mc "I thought about it, but I didn't want to cause more trouble for you."
    mc "Seeing how it went with Tybalt last time."
    scene ep4_jill2_date8 with dissolve
    ji "I understand. That's so nice of her to help you."
    scene ep4_jill2_date9 with dissolve
    mc "Yeah... She is...great."
    scene ep4_jill2_date25c with dissolve
    ji "..."
    if ep4_jillNiceGuy:
        scene ep4_jill2_date8 with dissolve
        ji "You'll have to show me what she taught you sometime."
        scene ep4_jill2_date9 with dissolve
        mc "Don't get your hopes up. My food is probably awful."
        scene ep4_jill2_date8 with dissolve
        ji "Haha! That's fine. It's been a while since I had that."
    scene ep4_jill2_date20 with dissolve
elif True:
    mc "No, I can't cook. I would like to learn it, but my dad just taught me the basics."
    mc "That's about what he knows."
mc "How about you? What do you usually do on dates?"
scene ep4_jill2_date29 with dissolve
ji "There haven't been that many for me either. A few in the past, but they were kind of forced."
scene ep4_jill2_date30 with dissolve
mc "Forced how?"
scene ep4_jill2_date29 with dissolve
ji "You know how it is..."
ji "A couple of persistent guys who stopped at nothing to take me out."
ji "The dates weren't enjoyable, really."
ji "So, I kind of swore off dating since."
if not ep4_jillNiceGuy:
    jump ep4_jill_end_date_label
label ep4_jill_lewd_label2:
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
    $ ep4_kissedJill = True
    play music "music/ep4/inspirational_piano_ambient.mp3"
scene ep4_jill2_date32 with dissolve
ji "My frame of reference of what you do on a date isn't the best."
ji "And those unspoken rules for dating make me feel a bit uncomfortable."
scene ep4_jill2_date33 with dissolve
mc "Unspoken rules? Like, don't burp or fart?"
mc "(Why did I say that?)"
scene ep4_jill2_date34 with dissolve
ji "Haha! No!"
ji "But those should be rules."
scene ep4_jill2_date32 with dissolve
ji "I meant more like rules for...intimacy and things of that nature."
scene ep4_jill2_date36 with dissolve
mc "I don't think I'm familiar with those rules."
scene ep4_jill2_date37 with dissolve
ji "They say that you should kiss on the first date..."
if ep4_kissedJill:
    scene ep4_jill2_date37b with dissolve
    ji "Haha... Well, we already did that..."
    scene ep4_jill2_date37 with dissolve
ji "And on the third date you should..."
scene ep4_jill2_date38 with dissolve
ji "Well...you know...?"
scene ep4_jill2_date36 with dissolve
menu:
    "Know what?" if True:
        $ dk(-1)
        mc "Know what?"
        scene ep4_jill2_date38 with dissolve
        ji "...have sex."
        scene ep4_jill2_date36 with dissolve
        mc "What? Really?"
        scene ep4_jill2_date38 with dissolve
        ji "That's what they say."
        scene ep4_jill2_date36 with dissolve
        mc "I've never heard of that."
    "Have sex?" if True:
        $ dk(1)
        mc "Have sex?"
        scene ep4_jill2_date38 with dissolve
        ji "Yeah... That's what they say."
        scene ep4_jill2_date36 with dissolve
mc "I don't think there's someone holding you to it."
scene ep4_jill2_date38 with dissolve
ji "I'm just a bit unsure about it all."
scene ep4_jill2_date36 with dissolve
mc "I think we'll take it one date at a time. That is if there's a second date..."
scene ep4_jill2_date43 with dissolve
ji "I hope so. I really enjoyed our first one, [name]."
ji "I have piano practice soon; I should get going."
scene ep4_jill2_date44 with dissolve
menu:
    "Go in for a kiss" if True:
        mc "I really enjoyed it, too."
        if not ep4_kissedJill:
            scene ep4_jill2_date45 with dissolve
            ji "What are you doing?"
            scene ep4_jill2_date46 with Dissolve(1, alpha=True)
            mc "I wanted to kiss you."
            scene ep4_jill2_date45b with dissolve
            ji "Oh..."
            ji "Ok..."
        scene ep4_jill2_date46b with dissolve
        $ renpy.pause()
        $ ep4_kissedJill2 = True
        scene anim_jill_kiss_ep4 with dissolve
        ji "(His lips are so soft...)"
        scene anim_jill_kiss2_ep4 with dissolve
        ji "(...and he's so gentle...)"
        ji "(This feels so much different from any other date I've ever been on...)"
        $ renpy.pause()
        scene ep4_jill2_date51 with dissolve
        mc "Thank you for the nice date."
        ji "..."
        scene ep4_jill2_date52 with dissolve
        ji "..."
        $ renpy.end_replay()
        $ persistent.ep4_lewd_jill2 = True
        $ calcScenes()
        $ bios_history_jill += "I kissed Jill after our date.\n\n"
        $ bios_name_jill = True
        $ chat_new_bios = True
    "Say goodbye" if not _in_replay:
        mc "Bye, Jill."
        scene ep4_jill2_date43 with dissolve
        ji "Bye..."
jump ep4_jill_end_date2_label
label ep4_jill_end_date_label:
scene ep4_jill2_date53b with dissolve
ji "Listen, I have piano practice soon; I should get going."
scene ep4_jill2_date53c with dissolve
mc "I get it. Thanks for the date. I had fun!"
scene ep4_jill2_date52b with dissolve
ji "Me too. Bye!"

label ep4_jill_end_date2_label:
scene ep4_jill2_date54 with dissolve
if ep4_kissedJill or ep4_kissedJill2:
    mc "(That was a very good date.)"
    mc "(I got to kiss her...)"
    mc "(...and we bonded pretty well.)"
    mc "(I'm a bit curious about her family...)"
    mc "(What could it possibly be?)"
    scene ep4_jill2_date55 with dissolve
    mc "(They are rich...probably famous...)"
    mc "(That doesn't matter, though. It's not why I want to date her.)"
    if ep4_playedGuitar:
        mc "(I can't wait to practice that song again for her.)"
    mc "(I totally forgot that I was sad...)"
    mc "(Wow...)"
    mc "(She completely took my mind off it.)"
    $ bios_history_jill += "The date with Jill was very good. We both enjoyed it.\n\n"
    $ bios_name_jill = True
    $ chat_new_bios = True
elif ep4_jillNiceGuy:
    mc "(That was a very good date.)"
    mc "(I enjoyed her company, but I don't know...)"
    mc "(I'm not sure I'm into her.)"
    scene ep4_jill2_date55 with dissolve
    mc "(I admit she took my mind off the whole Josy and Maya thing...)"
    $ bios_history_jill += "The date with Jill was good, but I don't think she's my kind of girl.\n\n"
    $ bios_name_jill = True
    $ chat_new_bios = True
elif True:
    mc "(That date could have gone better.)"
    mc "(It was fun and all, but it feels like we didn't really hit it off.)"
    mc "(Maybe she's not a girl for me?)"
    scene ep4_jill2_date55 with dissolve
    if affinity == "CHICK":
        mc "(We're alike in some ways.)"
        mc "(But she's so...sweet and innocent.)"
    elif True:
        mc "(We're pretty different from each other.)"
        mc "(She's so...sweet and innocent.)"
        mc "(I'm definitely not innocent.)"
    mc "(I admit she took my mind off the whole Josy and Maya thing...)"
    $ bios_history_jill += "The date with Jill wasn't very good. We're pretty different people.\n\n"
    $ bios_name_jill = True
    $ chat_new_bios = True
$ bios_history_jill += "Jill didn't want to tell me any details about her family.\n\n"
$ bios_name_jill = True
$ chat_new_bios = True
scene ep4_jill2_date58 with dissolve
mc "(The whole date felt so...grown up.)"
mc "(That's something that's completely missing in the DIK house...)"

label ep4_friday_dik_party_label:
play music "music/ep4/the_heat.mp3"
scene ep4_friday_dik_party1
tm "Spin the dildo works like this..."
tm "You spin the dildo and whoever the dildo stops at you have to make out with."
tm "And we're not talking about a little peck, we're talking a proper make out session."
scene ep4_friday_dik_party2 with dissolve
tm "With tongue and everything."
qu "We're playing spin the dildo?"
qu "Daughters, sit down."
scene ep4_friday_dik_party4 with dissolve
tm "No! No daughters!"
qu "No daughters, he says. Why beat around the bush?"
qu "There are already two daughters in that circle. Why not just say \"no Josy\"?"
scene ep4_friday_dik_party6 with dissolve
js "I can handle myself, Tommy."
scene ep4_friday_dik_party7 with dissolve
qu "Yeah, Tommy. Let her be a big girl."
scene ep4_friday_dik_party8 with dissolve
tm "This isn't about that! This game is for me, too."
scene ep4_friday_dik_party6b with dissolve
tm "How am I supposed to maintain a boner when I see her make out with someone?"
scene ep4_friday_dik_party9 with dissolve
qu "That's only gonna happen if that dildo lands on her, right?"
qu "Unless..."
scene ep4_friday_dik_party10 with dissolve
qu "Josy? Why don't you start spinning that dildo?"
scene ep4_friday_dik_party11 with hpunch
tm "Hey! I'm serious here! What the fuck is wrong with you?"
scene ep4_friday_dik_party12 with dissolve
qu "What's wrong with me? What the fuck is wrong with you?"
qu "You like me like this. It's not like you're blood relatives."
qu "Just fucking enjoy it!"
scene ep4_friday_dik_party13 with dissolve
de "See? You're not the only one who doesn't want her here!"
scene ep4_friday_dik_party14 with dissolve
mc "I didn't say that! I wanted her to come here from the start."
mc "This is really about your sis and all...it will take some time to get used to."
scene ep4_friday_dik_party13 with dissolve
de "You didn't talk to them yet?"
scene ep4_friday_dik_party14 with dissolve
mc "No, I've been avoiding them."
scene ep4_friday_dik_party13 with dissolve
de "For how long are you going to do that? We're gonna be here for years!"
scene ep4_friday_dik_party14 with dissolve
mc "I have a hard time turning on and off feelings like that."
scene ep4_friday_dik_party19 with dissolve
de "It's possible! You can choose to be happy! That's what I do!"
de "Life already sucks for so many reasons, but if you find yourself a good friend and force a smile on your face..."
de "...you'll manage even through the toughest of times!"
scene ep4_friday_dik_party12 with dissolve
qu "Lily! For the sake of Tommy's boner...spin that dildo!"
scene dildo_spin_ep4 with dissolve
ly "Here we go!"
scene dildo_spin_ep4_fr1 with dissolve
$ renpy.pause()
scene ep4_friday_dik_party22 with dissolve
tm "Oh!!! Daughter-daughter time! Everyone! Daughter-daughter time!"
qu "This you like, but your sister is off-limits, huh?"
tm "Shut up!"
scene ep4_friday_dik_party14 with dissolve
ly "Spin the dildo, Ash!"
scene ep4_friday_dik_party13 with dissolve
de "Come, [mc_de]! Let's watch!"
scene ep4_friday_dik_party26 with dissolve
tm "Wooooooooooo!"
menu:
    "Make fun of Tommy" if True:
        $ RPdiks += 1
        scene ep4_friday_dik_party28 with dissolve
        mc "Look guys! He goes \"WOOOO!\" like a fucking girl!"
        "Hahaha!"
    "Join him for a wooo" if True:
        $ RPdiks += 1
        scene ep4_friday_dik_party28 with dissolve
        mc "That's what I'm talking about! WOOOOO!!!"
    "Stay silent" if True:
        $ renpy.pause(0.5)
scene ep4_friday_dik_party29 with dissolve
tm "Son! Get in the circle!"
scene ep4_friday_dik_party28 with dissolve
mc "Why?"
scene ep4_friday_dik_party29 with dissolve
tm "No questions asked! It's an order, maggot!"
tm "Derek! You too!"
scene ep4_friday_dik_party31 with dissolve
$ renpy.pause()
scene dildo_spin_ep4 with dissolve
el "All right! Spin dildo! Spin!"
scene dildo_spin_ep4_fr7 with dissolve
$ renpy.pause()
scene ep4_friday_dik_party33 with dissolve
qu "Maya, Maya, Maya..."
tm "Put some more tongue into her!"
scene ep4_friday_dik_party34 with dissolve
$ renpy.pause()
scene dildo_spin_ep4 with dissolve
qu "Spin that dildo, Maya!"
scene dildo_spin_ep4_fr5 with dissolve
$ renpy.pause()
scene ep4_friday_dik_party37 with dissolve
qu "Look, Tommy! It's your favorite! Daughter-daughter time!"
tm "Fucking shit game!"
scene ep4_friday_dik_party38 with dissolve
qu "What are you waiting for? Make out already..."
qu "And make it a long session, ok?"
my "..."
scene ep4_friday_dik_party40 with dissolve
qu "Lucky you... Getting a front row seat to this."
if ep2_recommendedSage:
    qu "*{i}Whispers{/i}* It's good to know that she does what I tell her... I wonder what else she'll do."
scene ep4_friday_dik_party41 with dissolve
$ renpy.pause()
scene ep4_friday_dik_party42 with dissolve
qu "Tommy? Hey! Where are you going!?"
scene ep4_friday_dik_party43 with dissolve
js "Wow... Um..."
js "My turn..."
scene dildo_spin_ep4 with dissolve
$ renpy.pause()
scene dildo_spin_ep4_fr6 with dissolve
$ renpy.pause()
scene ep4_friday_dik_party43b with dissolve
js "Oh..."
scene ep4_friday_dik_party42b with dissolve
menu:
    "Make out" if True:
        $ ep4_made_out_josy = True
        scene ep4_friday_dik_party45 with dissolve
        $ renpy.pause()
        scene ep4_friday_dik_party46 with dissolve
        $ renpy.pause()
        scene ep4_friday_dik_party47 with dissolve
        ly "Now that's a kiss!"
        scene ep4_friday_dik_party49 with dissolve
        ar "Hello? [name]!?"
        de "SPIN THAT DILDO!"
        scene dildo_spin_ep4 with dissolve
        $ renpy.pause()
        scene ep4_friday_dik_party49b with dissolve
        de "Here we go girls! Who's it gonna be?"
        de "Who's the lucky gal? Who's gonna feel the soft lips of-"
        mc "Just stop."
        scene dildo_spin_ep4 with dissolve
        $ renpy.pause(2)
        scene dildo_spin_ep4_fr2 with dissolve
        $ renpy.pause()
        scene ep4_friday_dik_party51
        mc "Oh, hell no!"
        scene ep4_friday_dik_party52
        $ renpy.pause(0.5)
        scene ep4_friday_dik_party54
        $ renpy.pause(1)
        scene ep4_friday_dik_party53
        $ renpy.pause(2)
        scene ep4_friday_dik_party54
        $ renpy.pause(0.5)
        scene ep4_friday_dik_party52
        $ renpy.pause(0.5)
        scene ep4_friday_dik_party51
        de "Why did you-?"
        mc "You know exactly why."
    "Don't make out" if True:
        $ ep4_made_out_josy = False
        scene ep4_friday_dik_party43c with dissolve
        $ renpy.pause()
$ guideSuggestedPage = 112
jump ep4_freeroam_diks_label

label ep4_roof_label:
$ guideSuggestedPage = 113
scene ep4_roof with fade
qu "It's just a game!"
scene ep4_roof1 with dissolve
tm "Everything's a fucking game with you!"
scene ep4_roof2 with dissolve
qu "Why are you being such a bitch?"
scene ep4_roof1 with dissolve
tm "I hate that she's here!"
scene ep4_roof2 with dissolve
qu "Want me to kick her out?"
scene ep4_roof1 with dissolve
tm "Would you do that?"
scene ep4_roof6 with dissolve
qu "Wow! I was joking."
scene ep4_roof2 with dissolve
qu "I mean, I could probably make her leave..."
qu "Look at Maya. She's about to crumble."
scene ep4_roof1 with dissolve
tm "Good! Do it."
scene ep4_roof2 with dissolve
qu "...but I'm not gonna."
tm "..."
scene ep4_roof with dissolve
qu "Her presence really bugs you that much?"
scene ep4_roof1 with dissolve
tm "She...ruins my fun, ok?"
tm "How am I supposed to enjoy a party when she's here?"
tm "You have no fucking clue how she is!"
tm "She ratted me out to my mom for using her nail polish."
scene ep4_roof2 with dissolve
qu "I wouldn't have pegged you for a drag queen."
scene ep4_roof1 with dissolve
tm "I was inhaling it, stupid."
scene ep4_roof13 with dissolve
qu "Fuck me, what a moody dick!"
qu "Loosen up!"
scene ep4_roof15 with dissolve
tm "It feels like I'm babysitting!"
qu "You need to chill!"
qu "And speaking of inhaling stuff..."
tm "You've brought some?"
qu "Nail polish? No."
scene ep4_roof18 with dissolve
tm "Hahaha. Ok, fuck off."
scene ep4_roof19 with dissolve
qu "I've got something, but we should get some fresh air along with it."
scene ep4_roof20 with dissolve
$ renpy.pause()
scene ep4_roof21 with dissolve
tm "Hey! What the hell!"
tm "Are you spying on us?"
scene ep4_roof23 with dissolve
mc "No, I'm just waiting to take a piss. There's someone in there."
scene ep4_roof24 with dissolve
tm "You're gonna piss in Jamie's room?"
scene ep4_roof23 with dissolve
mc "Whoops... Wrong door. This is a big mansion."
scene ep4_roof28 with dissolve
tm "Quit your bullshit! Come with us."
mc "Another order?"
scene ep4_roof30 with dissolve
mc "Ok..."
scene ep4_roof31 with dissolve
tm "Watch your step or you'll end up needing that."
mc "A wheelchair? What's it doing up here?"
scene ep4_roof33 with dissolve
ri "Hey! Fuck you guys! You're gonna smoke without me?"
mc "Smoke?"
scene ep4_roof34 with dissolve
mc "That doesn't look like a cigarette."
qu "Hahaha!"
scene ep4_roof35 with dissolve
$ renpy.pause()
scene ep4_roof36 with dissolve
$ renpy.pause()
scene ep4_roof37 with dissolve
mc "*{i}Coughs{/i}* What the hell is that!?"
scene ep4_roof38 with dissolve
ri "Never tried weed before?"
mc "No."
ri "You've been missing out."
scene ep4_roof39 with dissolve
mc "Why does it smell so sweet?"
tm "HAHA! Look! A bitch parade!"
scene ep4_roof41 with dissolve
ri "Oh! Those guys! You should have seen Derek yesterday!"
ri "He really laid into them at their stupid protest."
scene ep4_roof42 with dissolve
tm "Leon! Go get Derek and tell him to go outside!"
tm "Feminists are marching the streets and I want a show."
play sound "sound_effects/shove.mp3"
scene ep4_roof43 with hpunch
mc "WHOA! SHIT!"
scene ep4_roof44 with dissolve
qu "Hahaha! Relax!"
mc "You're fucking crazy!"
scene ep4_roof46 with dissolve
$ renpy.pause()
scene ep4_roof47 with dissolve
$ renpy.pause(1.5)
show screen majorChoiceScale
menu:
    "Smoke weed" if True:
        $ addCPenalty()
        scene ep4_roof49 with dissolve
        mc "All right..."
        hide screen majorChoiceScale
        $ ep4_smoked_weed = True
        mc "What do I do?"
        scene ep4_roof50 with dissolve
        tm "You stick it up your ass."
        tm "Didn't you just watch three people smoke?"
        scene ep4_roof51 with dissolve
        mc "Fuck off... But really, how do I do it?"
        scene ep4_roof51b with dissolve
        qu "For starters, learn how to hold it properly."
        qu "Right now, you look like a fucking teenage girl smoking a cigarette."
        qu "Put it between your index finger and thumb."
        scene ep4_roof51c with dissolve
        mc "Like this?"
        scene ep4_roof51d with dissolve
        qu "Yeah, you got it."
        scene ep4_roof51c with dissolve
        mc "Why do I have to hold it like this?"
        mc "Because it's cool?"
        scene ep4_roof51e with dissolve
        tm "No, fuckface. That weed is precious and holding it like that lets you smoke it all."
        tm "Cupping your hand over the joint prevents it from dying out; it doesn't burn as good as a cigarette."
        scene ep4_roof52 with dissolve
        qu "Now, get those lips around it and inhale deep."
        qu "That's it. Hold your breath for as long as you can."
        qu "You'll feel a stinging sensation in your chest as your lungs fill with smoke."
        scene ep4_roof54 with dissolve
        qu "Don't be scared of it. It won't harm you."
        qu "When it gets too much for you, you just exhale!"
        scene ep4_roof55 with dissolve
        mc "*{i}Coughs{/i}*"
        qu "Hahaha!"
        scene ep4_roof56 with dissolve
        ri "This reminds me of my first time."
        scene ep4_roof57 with dissolve
        qu "Yeah, but you were what? 12? This is way funnier!"
        scene ep4_roof58 with dissolve
        mc "Damn my chest hurts..."
        scene ep4_roof59 with dissolve
        qu "You'll get used to it."
        scene ep4_roof58 with dissolve
        mc "When do I feel something from it?"
        scene ep4_roof51e with dissolve
        tm "Give it a few minutes. You'll know for sure when it kicks in."
        $ bios_history_mc += "I smoked weed with Tommy, Riona and Quinn.\n\n"
        $ bios_name_mc = True
        $ chat_new_bios = True
    "Don't smoke weed" if True:
        $ addDPenalty()
        hide screen majorChoiceScale
        $ ep4_smoked_weed = False
        mc "No. I don't do drugs."
        scene ep4_roof48 with dissolve
        tm "Alcohol is way fucking worse than this, you wimp."
        $ bios_history_mc += "I didn't smoke weed with Tommy, Riona and Quinn.\n\n"
        $ bios_name_mc = True
        $ chat_new_bios = True

scene ep4_roof38 with dissolve
ri "How's the pledge board coming along, [name]?"
ri "Tomorrow's the big night. Wrapped up most of it by now, right?"
scene ep4_roof_tommy1 with dissolve
tm "Haha! Good one. They are not even close."
tm "This might be the first year we actually reject maggots."
scene ep4_roof_tommy2 with dissolve
mc "That's what you think."
if ep4_monaSlap and ep4_paidMagnarWedgie:
    mc "I got the final slap and gave Magnar a wedgie yesterday."
elif ep4_monaSlap:
    mc "I got the final slap yesterday and Derek gave a wedgie to a nerd earlier today."
elif ep4_paidMagnarWedgie:
    mc "I gave Magnar a wedgie yesterday."
elif True:
    mc "Derek gave a wedgie to a nerd earlier today."
if not ep4_monaSlap:
    mc "We've just one more slap to go."
mc "The beers will be finished by tomorrow night and we have worn the helmet constantly."
mc "Tomorrow we'll have that sexy car wash. We're doing fine."
scene ep4_roof_tommy1 with dissolve
tm "Fine, he says. They're missing a lot of activities on that board."
ri "What's left?"
scene ep4_roof_tommy5 with dissolve
tm "I haven't heard anyone of you fuck neither a feminist or a teacher."
tm "Who did you fuck outdoors?"
tm "Why aren't the preps washing up from eggshells and yolk?"
tm "I'm calling it right now. You're screwed."
scene ep4_roof61 with dissolve
if not ep4_smoked_weed:
    stop music fadeout 3
tm "LOOK! There's Derek! I've gotta see this!"
if not ep4_smoked_weed:
    jump ep4_party_jm_label2
stop music
label ep4_quinn_lewd_label:
if _in_replay:
    hide screen phone_screen
    if persistent.name == None:
        $ name = "MC"
    elif True:
        $ name = persistent.name
    if persistent.mc_quinn == None:
        $ mc_quinn = "pervert"
    elif True:
        $ mc_quinn = persistent.mc_quinn
    if persistent.quinn == None:
        $ quinn = "Quinn"
    elif True:
        $ quinn = persistent.quinn
    $ ep4_paid_for_sex = True
play music "music/ep4/cosmos.mp3"
scene ep4_roof62 with hpunch
mc "Whoa..."
qu "Shit..."
scene ep4_roof64 with dissolve
qu "Hey! I think junior here is starting to feel it."
qu "Guys!?"
qu "Fuck..."
scene ep4_roof65 with dissolve
qu "Lie down, you shouldn't be standing for this."
mc "Shit... I-"
scene ep4_roof66 with dissolve
qu "Wow, your face is all pale! It really hit you hard, didn't it?"
scene bg anim_tripping_ep4 movie with dissolve
mc "Whoa..."
scene ep4_roof68 with dissolve
qu "Can't find any words?"
qu "Don't worry, that happens from time to time."
scene ep4_roof69 with dissolve
$ renpy.pause()
scene ep4_roof70 with dissolve
$ renpy.pause()
scene ep4_roof70b with dissolve
qu "Don't do anything stupid now. Just relax. This is the best part of it."
qu "Breathe and feel the calmness. How it sweeps over you."
scene ep4_roof71 with dissolve
qu "Next time you should try it while being sober! It gets even weirder."
qu "It's a shame that it doesn't last that long. Maybe up to an hour if you're lucky and stop smoking after it hits."
scene ep4_roof72 with dissolve
qu "Haha, I had labeled you as a perverted white knight pussy. But you're actually quite fun."
qu "Still a pussy, though. But a fun pussy!"
scene ep4_roof71 with dissolve
qu "No comebacks? Aw, that's the best part about teasing you."
qu "This really is your first time being high?"
scene ep4_roof74 with dissolve
mc "Yeah..."
scene ep4_roof71 with dissolve
qu "There are so many fun things you can do while being high!"
qu "And it's always a different experience!"
qu "Take eating, for example."
qu "It's insane how much you can eat when you're high! And everything tastes so good!"
scene ep4_roof74 with dissolve
mc "Yeah..."
scene ep4_roof77 with dissolve
qu "Hahaha! You don't even know! Why the fuck are you answering?"
scene ep4_roof74 with dissolve
mc "Yeah..."
scene ep4_roof77 with dissolve
qu "You're totally baked... I'm getting there, too."
qu "Fuck me..."
scene ep4_roof79 with dissolve
menu:
    "Lick her" if True:
        $ ep4_quinn_lewd = True
    "Rest your eyes" if not _in_replay:
        $ ep4_quinn_lewd = False
        stop music fadeout 3
        scene black with Fade(2,2,2)
        $ renpy.pause(0.5)
        jump ep4_party_jm_label

label ep4_quinn_lewd_label2:
scene ep4_quinn_lewd with dissolve
$ renpy.pause()
scene ep4_quinn_lewdb with dissolve
mc "*{i}Lick lick{/i}*"
qu "Hey... What are you doing?"
mc "It does taste great! Just like you said."
qu "I said eating tastes great! Haha..."
qu "Does it really taste good?"
mc "Yeah."
scene ep4_quinn_lewd2 with dissolve
qu "Hey, it does!"
scene anim_lick_quinn_ep4 with dissolve
qu "*{i}Lick lick{/i}*"
qu "Mmmm..."
scene ep4_quinn_lewd3 with dissolve
qu "Wanna check if I taste great in other places?"
scene ep4_quinn_lewd4 with dissolve
mc "Sure."
scene ep4_quinn_lewd3 with dissolve
qu "How much is it worth to you?"
scene ep4_quinn_lewd4 with dissolve
if ep4_paid_for_sex:
    mc "I'm done paying you for this."
elif True:
    mc "I'm not going to pay you for this."
mc "Can we just do it because we want to?"
scene ep4_quinn_lewd11 with dissolve
qu "..."
qu "Um..."
scene ep4_quinn_lewd13 with dissolve
qu "We can do that..."
qu "...this time."
qu "Wanna taste me?"
scene ep4_quinn_lewd13b with dissolve
menu:
    "Hell yeah" if True:
        scene ep4_quinn_lewd5 with dissolve
        mc "Hell yeah..."
        scene ep4_quinn_lewd6 with dissolve
        qu "What are you waiting for?"
        qu "Dig in!"
        scene anim_quinn_cunn_ep4 with dissolve
        mc "Yeah, this tastes great..."
        qu "Hahaha! Shut up and eat my pussy, [mc_quinn]."
        pause
        scene anim_quinn_cunn2_ep4 with dissolve
        qu "*{i}Moans{/i}*"
        qu "What a surprise...you actually don't suck at that."
        pause
        scene anim_quinn_cunn_ep4 with dissolve
        qu "Smoking weed and eating pussy... Mmm..."
        qu "This is a pretty good first time for you."
        pause
    "Taste me instead" if True:
        mc "What if you taste me instead?"
        play sound "sound_effects/zipper.mp3"
        scene ep4_quinn_lewd14 with dissolve
        $ renpy.pause()
        scene ep4_quinn_lewd14b with dissolve
        $ renpy.pause()
        scene anim_quinn_bj_ep4 with dissolve
        qu "*{i}Lick lick{/i}*"
        qu "I like when you're trying to control me."
        qu "I don't suck anyone's dick..."
        qu "*{i}Lick schlurp{/i}*"
        mc "I don't know if it's the weed or if you're just that good..."
        mc "...but this feels fucking amazing."
        qu "*{i}Suck suck{/i}*"
        qu "*{i}Lick schlurp{/i}*"
        mc "(She's swiveling her tongue around my cock as she bobs her head up and down...)"
        mc "(She's putting so much effort into it.)"
        pause
        scene anim_quinn_bj2_ep4 with dissolve
        qu "*{i}Suck suck{/i}*"
        mc "Yes...that's the spot...don't stop."
        pause
scene ep4_quinn_lewd15 with dissolve
qu "I wanna be your first."
mc "My first? Haha... You're not my first."
scene ep4_quinn_lewd17 with dissolve
qu "You've never fucked high before. That's a big first."
qu "You never forget that first time."
scene ep4_quinn_lewd18 with dissolve
qu "I wanna be the one you think about every time you blaze a fatty."
scene ep4_quinn_lewd18c with dissolve
qu "But damn...your cock is so fucking big."
mc "Have you seen my hand!? It's even bigger!"
qu "Hahaha! Shut up! That's the weed talking."
scene ep4_quinn_lewd18b with dissolve
qu "But for real...it's really huge."
mc "Thanks...I grow it myself."
qu "Haha, are you gonna shut up or keep making stupid jokes?"
scene ep4_quinn_lewd21 with dissolve
qu "Seriously! Check this!"
qu "That's how far up inside me you'll get."
qu "It's insane!"
scene ep4_quinn_lewd22 with dissolve
qu "Lay back and enjoy, [mc_quinn]..."
qu "I'm fucking wet already, this is gonna be like a slip and slide."
scene bg anim_quinn_slide_ep4 movie with dissolve
qu "Ahhhhh!"
scene ep4_quinn_lewd23 with dissolve
qu "Hey? Are you ok?"
qu "Did it hit you again?"
qu "You're gonna enjoy this next part."
scene anim_ride_quinn_ep4 with dissolve
qu "Just breathe and focus on your cock."
qu "Feel it... How my pussy envelops it..."
pause
scene anim_ride_quinn2_ep4 with dissolve
qu "With every single thrust of my hips..."
qu "...blood just rushes to your dick."
pause
scene anim_ride_quinn3_ep4 with dissolve
qu "Hey... Are you with me? Earth to [mc_quinn]..."
mc "Huh? Yeah... I'm back..."
mc "You're so soft... I can't believe this..."
mc "You look so rough...but your skin is melting in my hands."
qu "Hahaha, what the fuck are you even saying right now?"
pause
label ep4_quinn_sex_loop_label:
menu:
    "Cowgirl" if True:
        scene anim_ride_quinn_ep4 with dissolve
        pause
        scene anim_ride_quinn2_ep4 with dissolve
        pause
        scene anim_ride_quinn3_ep4 with dissolve
        pause
        jump ep4_quinn_sex_loop_label
    "Fuck her from the side" if True:
        scene anim_quinn_side_ep4 with dissolve
        qu "Mmm... Yes... That's the fucking spot..."
        scene anim_quinn_side2_ep4 with dissolve
        qu "Deeper!"
        mc "Yeah..."
        pause
        jump ep4_quinn_sex_loop_label
    "Continue" if True:
        $ renpy.pause(0.5)
scene ep4_quinn_lewd25 with dissolve
mc "Hey... Let me fuck you from behind."
scene ep4_quinn_lewd26 with dissolve
qu "You're not gonna fall off, are you?"
scene ep4_quinn_lewd25 with dissolve
mc "No, I'm feeling better..."
scene ep4_quinn_lewd26 with dissolve
qu "All right..."
scene anim_quinn_doggy1_ep4 with dissolve
qu "*{i}Moan{/i}* You're really going deep, aren't you?"
qu "You fuck as slow as a turtle...but damn...you're hitting the right spot..."
pause
scene anim_quinn_doggy2_ep4 with dissolve
mc "*{i}Breathing loudly{/i}* You're so...deep!"
qu "Hngn...I can almost feel you in my belly..."
mc "I wanna go deeper..."
qu "I don't think that's possible..."
mc "What if we use that chimney?"
qu "You wanna fuck me against the chimney?"
mc "Yeah..."
pause
scene ep4_quinn_lewd27 with dissolve
qu "Ok, be real fucking careful when you fuck me. I don't want you to fall off."
scene ep4_quinn_lewd28 with dissolve
mc "Haha..."
scene ep4_quinn_lewd27 with dissolve
qu "What are you laughing at?"
scene ep4_quinn_lewd28 with dissolve
mc "I can't believe how much you care for me."
mc "You're. So. Sweet."
scene ep4_quinn_lewd27 with dissolve
qu "And you're so fucking high!"
qu "I just don't want tomorrow's headlines to read \"High campus pervert dead from high fall\"."
qu "Shut up and fuck me!"
scene anim_quinn_doggy3_ep4 with dissolve
qu "*{i}Moans{/i}* Ok, this isn't deeper..."
qu "...but you're still filling me up."
pause
scene anim_quinn_doggy4_ep4 with dissolve
mc "Your ass is so hot..."
qu "Finally! A coherent sentence."
pause
scene anim_quinn_doggy5_ep4 with dissolve
mc "My dick feels like it's floating..."
qu "What!? Are you close to cumming?"
mc "I... I don't know... It's shaking a bit..."
pause
scene ep4_quinn_deepthroat with dissolve
qu "Here... Let me finish you off."
qu "Grab that chimney hard and fuck my throat until you cum."
scene anim_quinn_deepthroat_ep4 with dissolve
qu "*{i}Mphff{/i}*"
mc "I can't believe that you can take all of me like that..."
pause
scene anim_quinn_deepthroat2_ep4 with dissolve
qu "*{i}Suck suck{/i}*"
mc "Ok... I'm definitely feeling something now..."
pause
scene anim_quinn_deepthroat_ep4 with dissolve
mc "I'm gonna cum..."
pause
scene anim_quinn_deepthroat3_ep4 with dissolve
mc "Ahhh!"
qu "Mmm..."
pause
scene ep4_quinn_cum with dissolve
qu "Hahaha! You look like you've seen a ghost or something."
mc "What just happened...?"
qu "You'll make sense of this when you wake up tomorrow. I'm sure..."
$ renpy.end_replay()
$ persistent.ep4_lewd_quinn = True
$ calcScenes()
$ bios_history_quinn += "I fucked Quinn on the roof while being high.\n\n"
$ bios_name_quinn = True
$ chat_new_bios = True
stop music fadeout 3
scene ep4_roof_jacob with dissolve
$ renpy.sound.play("sound_effects/crickets.mp3", channel="sfx1", loop=True)
jac "(Man...a big place like this and we still run out bathrooms every time I need to take a piss...)"
jac "(It's fucking ridiculous...)"
scene ep4_roof_jacob1 with dissolve
jac "Hey, there buddy."
jac "Did you miss me?"
play sound "sound_effects/zipper.mp3"
scene ep4_roof_jacob2 with dissolve
jac "Ahh..."
scene ep4_roof_jacob3 with dissolve
jac "(What the...?)"
scene ep4_roof_jacob4 with dissolve
jac "(Dude! This maggot is fucking dope...)"
scene ep4_roof_jacob5 with dissolve
qu "Hey...lie down and rest..."
qu "I'm not letting you go until I'm sure you won't fall off the edge."
scene ep4_roof_jacob6 with dissolve
mc "This feeling is...surreal..."
mc "I've never been this calm before."
scene ep4_roof_jacob7 with dissolve
qu "I know... That's why I like to smoke."
$ renpy.music.stop(channel="sfx1", fadeout=3)
scene black with Fade(2,2,2)
$ renpy.pause(0.5)
scene ep4_roof80b with vpunch
$ renpy.sound.play("sound_effects/crickets.mp3", channel="sfx1", loop=True)
mc "Whoa..."
scene ep4_roof81 with dissolve
qu "Finally..."
qu "Feeling like yourself again?"
scene ep4_roof82b with dissolve
mc "Uhh... I'm still drunk."
scene ep4_roof83 with dissolve
$ renpy.music.stop(channel="sfx1", fadeout=3)
qu "Good enough. Let's head back inside."
jump ep4_party_jm_label2

label ep4_party_jm_label:
scene ep4_roof80 with vpunch
mc "Whoa..."
scene ep4_roof81 with dissolve
qu "Finally..."
qu "Feeling like yourself again?"
scene ep4_roof82 with dissolve
mc "Uhh... I'm still drunk."
scene ep4_roof83 with dissolve
qu "Good enough. Let's head back inside."

label ep4_party_jm_label2:
play music "music/ep4/reaching_halo.mp3"
scene ep4_party_jm with wipeleft
ash "You've been here since the start of the scavenger hunt, right?"
my "Yes, I have."
ash "Are you done with your list?"
my "No, Quinn had me paired up with Josy for it and we haven't really started."
my "How about you?"
scene ep4_party_jm4 with dissolve
ly "Yeah, we did a few, but most of them are stupid simple."
ly "And honestly, it's not that fun. It feels like we're running errands."
ly "Getting them alcohol and whatnot."
js "Getting alcohol? Our lists aren't the same, are they?"
scene ep4_party_jm with dissolve
ash "I checked with Mona and Camila earlier, the lists are totally different."
ash "It's almost impossible to cheat and help each other."
scene ep4_party_jm7 with dissolve
ly "Trying to take credit for my idea, are you?"
js "That's a bummer."
scene ep4_party_jm4 with dissolve
ly "You're really Tommy's sister?"
js "Stepsister... Why? Do you know him?"
scene ep4_party_jm11 with dissolve
ly "The way he described you, I thought you'd be ugly or fat."
ly "But you're neither. You're actually very pretty."
js "Um... Thanks?"
ly "You'd make a killing at the club."
scene ep4_party_jm15 with dissolve
js "What club?"
ly "The Pink Rose."
ly "You know how to dance?"
js "What kind of a dance are you talking about?"
scene ep4_party_jm14d with dissolve
ly "You know, the kind where you gyrate your hips."
ash "Lily's working extra as an exotic dancer."
ly "A stripper, Ash. Fancy words fool no one."
js "Oh! That's...cool."
scene ep4_party_jm14h with dissolve
ly "I don't believe you think that."
ly "And never mind. It was just a thought."
scene ep4_party_jm16 with dissolve
ash "[name]! Hey!"
scene ep4_party_jm19 with dissolve
mc "Hey, what's up?"
scene ep4_party_jm18 with dissolve
ash "Have you seen Derek? I've been looking for him."
scene ep4_party_jm19 with dissolve
mc "Last time I saw him he was chasing a feminist down the street."
scene ep4_party_jm18 with dissolve
ash "Thanks!"
scene ep4_party_jm22 with dissolve
js "Can I have a moment alone with him?"
scene ep4_party_jm23 with dissolve
$ renpy.pause()
scene ep4_party_jm24 with dissolve
js "Hey..."
js "I know you don't want to talk to me."
js "You have the same look on your face that Tommy had when he saw me here."
scene ep4_party_jm25 with dissolve
js "I just need to say one thing to you..."
js "Don't take what happened between you and me out on Maya."
js "I'd hate to see your friendship get ruined over this."
scene ep4_party_jm26 with dissolve
mc "If you think that's what this is..."
mc "...you couldn't be more wrong."
scene ep4_party_jm25 with dissolve
js "Then talk to me."
js "Talk to her. Talk to us!"
scene ep4_party_jm24 with dissolve
js "I've realized I already made my bed with my choices..."
if ep2_fuckedJosy and affinity != "DIK":
    js "...but if I got the chance to go back and change them...I wouldn't."
elif True:
    js "...and if I got the chance to go back and change them...maybe I would. I'm not sure..."
scene ep4_party_jm26 with dissolve
mc "And I've made my bed with mine, too."
mc "I need to talk to both of you..."
mc "...but not here."
mc "Somewhere private."
scene ep4_party_jm24 with dissolve
js "Right now?"
scene ep4_party_jm26 with dissolve
mc "Yes... I won't have this courage when I'm sober."
mc "There's a ruined library on the bottom floor. Meet me there."
scene ep4_party_jm31 with dissolve
js "I'll go get Maya..."
scene ep4_party_jm32 with dissolve
mc "(This is probably gonna hurt...a lot...)"
stop music fadeout 3
mc "(...but I have to do it.)"

scene ep4_josy_maya_talk with fade
play music "music/ep4/just_peachy.mp3"
$ renpy.pause()
scene ep4_josy_maya_talkb with dissolve
my "Hey..."
js "Hi."
scene ep4_josy_maya_talk2 with dissolve
mc "Maya..."
mc "Josy..."
scene ep4_josy_maya_talk4 with dissolve
mc "The lies and secrets won't end if I don't do this right now."
mc "I'm tired of it being this hard to be with you. It's exhausting, really."
scene ep4_josy_maya_talk5 with dissolve
mc "I met Josy this summer at our summer job."
mc "She was the girl I went back home to date last week."
if ep2_fuckedJosy:
    mc "We flirted, made out and had sex."
elif True:
    mc "We flirted and made out."
my "What?"
scene ep4_josy_maya_talk7 with dissolve
mc "Josy..."
mc "Maya's not innocent in this either."
if ep3_mayaLewd:
    mc "We have become very close to each other, we also flirted, made out..."
    mc "...and we pretty much had sex."
elif True:
    mc "We have become very close to each other and we also flirted and made out."
scene ep4_josy_maya_talk9 with dissolve
my "..."
scene ep4_josy_maya_talk9b with dissolve
js "..."
my "Is it true?"
scene ep4_josy_maya_talk9b2 with dissolve
js "It is..."
js "What about you?"
scene ep4_josy_maya_talk12 with dissolve
my "...yes."
my "There's no excuse for it."
my "[name] has been there for me when you weren't."
my "He's been my way to escape."
scene ep4_josy_maya_talk9b2 with dissolve
js "But...you don't like boys..."
scene ep4_josy_maya_talk12b with dissolve
my "I know!"
scene ep4_josy_maya_talk9b3 with dissolve
js "That's...that's...huge..."
scene ep4_josy_maya_talk12 with dissolve
my "Why...did you do it?"
scene ep4_josy_maya_talk9b4 with dissolve
js "For the same reasons as yours. He was there for me..."
js "He made me feel something again."
js "A feeling that wasn't worry."
js "With all that's been going on around us...I've really needed that."
scene ep4_josy_maya_talk18 with dissolve
my "..."
scene ep4_josy_maya_talk19 with dissolve
my "I..."
scene ep4_josy_maya_talk18 with dissolve
my "..."
scene ep4_josy_maya_talk19 with dissolve
my "Are we supposed to feel angry now?"
scene ep4_josy_maya_talk9b2 with dissolve
js "I don't know..."
js "Are you feeling angry?"
scene ep4_josy_maya_talk19 with dissolve
my "I'm trying to... I don't know why, but it feels like it's the natural thing to feel..."
my "So, I'm really trying as hard as I can to feel it..."
scene ep4_josy_maya_talk22 with dissolve
my "...but..."
my "...I don't feel it."
my "You cheated on me..."
my "...but so did I..."
my "...for the exact same reasons."
scene ep4_josy_maya_talk23 with dissolve
js "Maybe that's why we're understanding each other right now?"
js "We're the same."
js "We're just as bad."
scene ep4_josy_maya_talk23b with dissolve
js "..."
scene ep4_josy_maya_talk30 with dissolve
js "I...forgive you."
my "You do? Why?"
scene ep4_josy_maya_talk31b with dissolve
js "I know my actions haven't shown it..."
js "...and being forced to stay away from you...it made us weaker..."
js "...but you have to believe me..."
js "Deep down...I never stopped loving you."
js "Please...don't leave me..."
scene ep4_josy_maya_talk32 with dissolve
my "I've had many doubts about us lately..."
my "...but they were never because of what we are when we're together..."
my "...the doubts were because of what we are when we're apart."
my "I never stopped loving you, either."
my "And I forgive you, too."
scene ep4_josy_maya_talk33 with dissolve
$ renpy.pause()
scene ep4_josy_maya_talk34 with dissolve
$ renpy.pause()
scene ep4_josy_maya_talk35 with dissolve
my "This is why you stormed out."
scene ep4_josy_maya_talk36 with dissolve
mc "It's not the only reason...you know that."
scene ep4_josy_maya_talk37 with dissolve
my "Yeah... I know..."
my "You've given me too many chances..."
my "...and I've blown every single one of them by not letting you closer to me."
scene ep4_josy_maya_talk38 with dissolve
my "Keeping my guard up when I should have realized that you were worth letting it down for."
my "I really don't deserve another chance..."
my "...but I still want one."
scene ep4_josy_maya_talk40 with dissolve
js "I don't know what you did to Maya to make her feel like this..."
js "I only know what you made me feel."
js "So, I think I can understand what she's feeling."
scene ep4_josy_maya_talk41 with dissolve
js "You and I...we barely even got a chance..."
js "...and it wasn't an honest one..."
js "...and I still blew it."
scene ep4_josy_maya_talk40 with dissolve
js "I want another chance, too."
scene ep4_josy_maya_talk43 with dissolve
mc "I don't know what either of you mean by that."
mc "What's this chance you're talking about?"
mc "Are you talking about friendship or love? Which is it?"
scene ep4_josy_maya_talk44 with dissolve
js "..."
my "..."
scene ep4_josy_maya_talk45 with dissolve
my "Do we have to know?"
scene ep4_josy_maya_talk46 with dissolve
mc "These last couple of days I've felt like shit because of this."
mc "Derek has been there for me. Talking me through things, a lot."
mc "And even though he can be pretty damn stupid..."
mc "...he's opened my eyes to something."
scene ep4_josy_maya_talk47 with dissolve
js "What's that?"
scene ep4_josy_maya_talk46 with dissolve
mc "That I rush into things without thinking."
mc "Everything I've been doing lately has been on impulse."
mc "Especially when it comes to women."
scene ep4_josy_maya_talk49 with dissolve
mc "He's talked me into dating others."
mc "I have no idea of what I'm doing, but I think that it's been good for me."
scene ep4_josy_maya_talk46 with dissolve
mc "The only thing I know for sure is that it feels great getting this conversation off my chest."
label ep4_lewd_josy_maya2_label:
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
    if persistent.mc_josy == None:
        $ mc_josy = name
    elif True:
        $ mc_josy = persistent.mc_josy
    if persistent.josy == None:
        $ josy = "Josy"
    elif True:
        $ josy = persistent.josy
    $ ep2_fuckedJosy = True
    $ ep3_mayaLewd = True
    play music "music/ep4/just_peachy.mp3"
scene ep4_josy_maya_talk51 with dissolve
$ guideSuggestedPage = 114
mc "Maya..."
mc "Josy..."
mc "I don't hate you."
menu:
    "Try for something more" if True:
        $ ep4_rejectedMayaJosy = False
        $ ep4_wantedMoreMayaJosy = True
        mc "It's been the opposite..."
        scene ep4_josy_maya_talk56 with dissolve
        mc "I wanted to see if I could love you."
        mc "And I did feel something..."
        mc "I want to give you another chance..."
        mc "...but a part of me wishes that there's something more than friendship waiting for me down that road..."
        mc "...and that's what makes this situation so damned complicated."
        scene ep4_josy_maya_talk44 with dissolve
        my "..."
        js "..."
        scene ep4_josy_maya_talk58 with dissolve
        my "I can't say what I feel about this in front of you..."
        scene ep4_josy_maya_talk59 with dissolve
        js "Do you think I can?"
        js "It would be such a huge risk."
        scene ep4_josy_maya_talk58 with dissolve
        my "It would..."
        scene ep4_josy_maya_talk59 with dissolve
        js "I don't want to lose you."
        scene ep4_josy_maya_talk44 with dissolve
        my "..."
        scene ep4_josy_maya_talk58 with dissolve
        my "You wouldn't."
        scene ep4_josy_maya_talk59 with dissolve
        js "You say that now...but what about later? Are you really sure?"
        scene ep4_josy_maya_talk44 with dissolve
        my "..."
        scene ep4_josy_maya_talk62 with dissolve
        mc "I don't know if this helps you at all, but..."
        mc "Whenever I wasn't sure of what to do in life, my dad told me that making choices..."
        mc "...while following your heart, will take you exactly where you're supposed to be."
        mc "And that it is why some choices are harder to make than others..."
        mc "...especially when your heart tells you to go against the grain."
        mc "The biggest choices in life may be of great risk and promise a great reward."
        mc "The scariest part about making these big choices..."
        mc "...is that you have no clue if there's a turning back, if the outcome wasn't what you desired."
        mc "But even how scary it may feel...just remember that first part..."
        mc "Following your heart...will take you exactly where you're supposed to be."
        scene ep4_josy_maya_talk61 with dissolve
        js "*{i}Whispers{/i}*"
        my "*{i}Whispers{/i}*"
        js "*{i}Whispers{/i}*"
        $ tmpScore = 0
        if ep2_fuckedJosy:
            $ tmpScore += 1
        if ep3_mayaLewd:
            $ tmpScore += 1
        if _in_replay:
            jump ep4_kiss_jm_label
        if tmpScore > 0 and affinity != "DIK":
            $ pathMayaJosy = True
            label ep4_kiss_jm_label:
            scene ep4_josy_maya_talk43 with dissolve
            mc "..."
            mc "What did you decide?"
            scene ep4_josy_maya_talk65 with dissolve
            my "This..."
            scene anim_jm2_kiss_ep4 with dissolve
            $ renpy.pause()
            scene anim_jm2_kiss2_ep4 with dissolve
            $ renpy.pause()
            scene ep4_josy_maya_talk67 with dissolve
            js "Haha! What the hell are we doing?"
            my "We are following our hearts!"
            js "We are?"
            scene ep4_josy_maya_talk70 with dissolve
            $ renpy.pause()
            scene ep4_josy_maya_talk72 with dissolve
            mc "(Is this a dream?)"
            mc "(I just took a huge risk and got something I wanted...)"
            scene ep4_josy_maya_talk73 with dissolve
            mc "(I have no idea what will happen now...)"
            mc "(All I know is that I don't have to feel sad anymore...)"
            scene black with fade
            mc "(I followed my heart...)"
            stop music fadeout 3
            mc "(Dad...)"
            mc "(Thank you.)"
            $ renpy.end_replay()
            $ persistent.ep4_lewd_maya_josy2 = True
            $ calcScenes()
            if ep4_jadeOffer:
                $ ep4_rejectedJade = True
                $ renpy.sound.play("sound_effects/crickets.mp3", channel="sfx1", loop=True)
                scene ep4_rejected_jade with fade
                $ renpy.pause()
                scene ep4_rejected_jade2 with dissolve
                ja "..."
                play sound "sound_effects/burnout.mp3"
                scene ep4_rejected_jade3 with dissolve
                $ renpy.pause()
                $ renpy.music.stop(channel="sfx1", fadeout=3)
            $ bios_history_maya += "I told Josy and Maya about what we've done with each other. I also told them I wanted something more than just a friendship with them. They felt the same way.\n\n"
            $ bios_name_maya = True
            $ bios_history_josy += "I told Josy and Maya about what we've done with each other. I also told them I wanted something more than just a friendship with them. They felt the same way.\n\n"
            $ bios_name_josy = True
            $ chat_new_bios = True
            jump ep4_jm_dorm_talk_label
        elif True:
            $ pathMayaJosy = False
            scene ep4_josy_maya_talk62 with dissolve
            $ renpy.pause()
            scene ep4_josy_maya_talk74 with dissolve
            my "We're sorry...but we can't do it..."
            js "It's too big of a risk...and our hearts tell us it's wrong."
            scene ep4_josy_maya_talk62 with dissolve
            mc "Ok..."
            mc "That's it then..."
            mc "I wish you the best."
            mc "I'll give you another chance...but as a friend."
            scene ep4_josy_maya_talk53 with dissolve
            my "I'll take that offer any day."
            js "Me too."
            scene ep4_josy_maya_talk54b with dissolve
            mc "(Well...I did it...)"
            mc "(This wasn't just their choice. It was a big choice for me, too.)"
            mc "(I told them how I felt...)"
            scene ep4_josy_maya_talk55 with dissolve
            mc "(...even if it didn't go the way I'd hoped, I followed my heart.)"
            mc "(I can move on knowing that I tried and that it was meant to be this way.)"
            mc "(This isn't it for me... I'm supposed to be somewhere else...)"
            scene black with fade
            mc "(I followed my heart...)"
            mc "(Dad...)"
            stop music fadeout 3
            mc "(Thank you.)"
            $ bios_history_maya += "I told Josy and Maya about what we've done with each other. I also told them I wanted something more than just a friendship with them. They didn't feel the same way.\n\n"
            $ bios_name_maya = True
            $ bios_history_josy += "I told Josy and Maya about what we've done with each other. I also told them I wanted something more than just a friendship with them. They didn't feel the same way.\n\n"
            $ bios_name_josy = True
            $ chat_new_bios = True
            if ep4_jadeOffer:
                jump ep4_jade_parking_lot_label
            elif True:
                jump ep4_sat_morning_label
    "Stay friends" if not _in_replay:
        $ ep4_wantedMoreMayaJosy = False
        $ ep4_rejectedMayaJosy = True
        mc "And I'll give you another chance..."
        mc "...but only as a friend."
        mc "I can't do it any other way."
        scene ep4_josy_maya_talk53 with dissolve
        my "I'll take that offer any day."
        js "Me too."
        scene ep4_josy_maya_talk54b with dissolve
        mc "(I did it...)"
        mc "(I chose something.)"
        mc "(Even if my choice wasn't saying that someone is right for me...)"
        mc "(...choosing that someone isn't right for me is a huge thing, too.)"
        scene ep4_josy_maya_talk55 with dissolve
        mc "(I have no idea where the road I'm on will take me...)"
        mc "(All I know is that I don't have to feel sad anymore... Not about this.)"
        scene black with fade
        mc "(I followed my heart...)"
        mc "(Dad...)"
        stop music fadeout 3
        mc "(Thank you.)"
        $ bios_history_maya += "I told Josy and Maya about what we've done with each other. I also told them I only wanted friendship from them. They felt the same way.\n\n"
        $ bios_name_maya = True
        $ bios_history_josy += "I told Josy and Maya about what we've done with each other. I also told them I only wanted friendship from them. They felt the same way.\n\n"
        $ bios_name_josy = True
        $ chat_new_bios = True
        if ep4_jadeOffer:
            jump ep4_jade_parking_lot_label
        elif True:
            jump ep4_sat_morning_label

label ep4_jade_parking_lot_label:
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
$ ep4_fuckedJade = True
scene ep4_jade_parking_lot with fade
$ renpy.sound.play("sound_effects/crickets.mp3", channel="sfx1", loop=True)
mc "(I'm nervous...)"
mc "(I'm going to have an affair with a married woman.)"
mc "(And I'm going to get proof of it, too? Just for a pledge board?)"
scene ep4_jade_parking_lot1 with dissolve
mc "(This is so stupid...)"
mc "(I wanna fuck her, but it shouldn't be like this.)"
scene ep4_jade_parking_lot2 with dissolve
mc "(That must be her.)"
play music "music/ep3/black_box.mp3"
scene bg anim_jade_parking_ep4 movie with dissolve
$ renpy.pause()
scene ep4_jade_parking_lot4 with dissolve
ja "Did you come alone?"
scene ep4_jade_parking_lot5 with dissolve
mc "Yes, I've been here for 10 minutes. There's no one else here."
scene ep4_jade_parking_lot4 with dissolve
$ renpy.music.stop(channel="sfx1", fadeout=5)
ja "Get in."
scene ep4_jade_parking_lot6 with dissolve
mc "Hi..."
menu:
    "Go in for a kiss" if True:
        scene ep4_jade_parking_lot7 with dissolve
        ja "Uh-uh. Not here."
    "Don't kiss her" if True:
        $ renpy.pause(0.5)
play sound "sound_effects/burnout.mp3"
scene ep4_jade_parking_lot8 with dissolve
$ renpy.pause()
scene ep4_jade_parking_lot9 with dissolve
menu:
    "Where are we going?" if True:
        mc "Where are we going?"
        scene ep4_jade_parking_lot10 with dissolve
        ja "You'll see."
        scene ep4_jade_parking_lot9 with dissolve
        mc "That's mysterious."
        scene ep4_jade_parking_lot10 with dissolve
        ja "Let's just say that it's some place more secluded than the campus parking lot."
        ja "I can't comprehend why you thought I would give you a blowjob there."
        scene ep4_jade_parking_lot9 with dissolve
        mc "You're going to give me a blowjob?"
        scene ep4_jade_parking_lot12 with dissolve
        ja "For starters."
    "You look great" if True:
        scene ep4_jade_parking_lot9b with dissolve
        mc "(Damn...)"
        scene ep4_jade_parking_lot9 with dissolve
        mc "You look great tonight."
        scene ep4_jade_parking_lot10 with dissolve
        ja "I always look great."
        scene ep4_jade_parking_lot9 with dissolve
        mc "Of course, but tonight you look extra good."
        ja "..."
scene ep4_jade_parking_lot10 with dissolve
ja "How are you feeling?"
scene ep4_jade_parking_lot9 with dissolve
mc "Um...better?"
scene ep4_jade_parking_lot10 with dissolve
ja "That doesn't sound convincing."
scene ep4_jade_parking_lot9 with dissolve
mc "It is better, but it's been a rough couple of days."
scene ep4_jade_parking_lot13 with dissolve
ja "You have a lot to learn."
scene ep4_jade_parking_lot14 with dissolve
mc "What do you mean?"
scene ep4_jade_parking_lot13 with dissolve
ja "About how to handle heartbreak and not show weakness."
ja "And that smell I sense..."
ja "Let me tell you that you're not going to find the answer at the bottom of a bottle."
scene ep4_jade_parking_lot14 with dissolve
mc "..."
mc "How do {b}you{/b} do it?"
scene ep4_jade_parking_lot10 with dissolve
ja "I think about what's important. My career and kids."
ja "The love for my husband is low priority compared to that."
ja "And these days, it's as low as it can get."
scene ep4_jade_parking_lot9 with dissolve
mc "I'm sorry to hear that."
scene ep4_jade_parking_lot10 with dissolve
ja "Don't be."
ja "As I said, I have other priorities."
ja "And my priority tonight..."
scene ep4_jade_parking_lot12 with dissolve
ja "Is to use you."
ja "I'm not letting you go until you've made me feel like a woman again."
label ep4_jade_lewd1_label:
stop music fadeout 5
scene ep4_jade_lewd1 with fade
ja "We're here."
mc "Where is \"here\"?"
scene ep4_jade_lewd2 with dissolve
ja "Here is the place where a teacher will blow her student and swallow every single drop of cum."
scene ep4_jade_lewd3 with dissolve
mc "Just like that?"
scene ep4_jade_lewd4 with dissolve
ja "Just like that."
ja "Recline your seat, [mc_jade]."
play sound "sound_effects/zipper.mp3"
scene ep4_jade_lewd5 with dissolve
menu:
    "Roleplay" if True:
        $ jade = "Mommy"
        $ mc_jade = "Son"
        scene ep4_jade_lewd6 with dissolve
        ja "By the way..."
        ja "Do you like roleplaying?"
        scene ep4_jade_lewd6b with dissolve
        mc "(It's not gonna be that Dungeons and Gremlins crap, I hope.)"
        mc "What kind of roleplaying?"
        scene ep4_jade_lewd6 with dissolve
        ja "Just...call me Mommy. Ok?"
        scene ep4_jade_lewd6b with dissolve
        mc "Mommy?"
        scene ep4_jade_lewd6 with dissolve
        ja "Yes..."
        ja "Now ask Mommy to suck your cock."
    "Continue" if True:
        $ ep4_roleplay = False
        scene ep4_jade_lewd6 with dissolve
        ja "Now...ask me to suck your cock..."
scene ep4_jade_lewd6b with dissolve
mc "Suck my cock, [jade]."
play music "music/ep2/jingle.mp3"
scene anim_jade_bj_ep4 with dissolve
mc "Oh...[jade]... Yes, just like that."
ja "*{i}Suck schlurp{/i}*"
$ renpy.pause()
scene ep4_jade_lewd6c with dissolve
mc "Ahh...damn that feels good!"
scene anim_jade_bj_ep4 with dissolve
ja "*{i}Suck schlurp{/i}* Relax..."
ja "Let [jade] take care of you."
$ renpy.pause()
scene anim_jade_bj2_ep4 with dissolve
$ renpy.pause()
scene ep4_jade_lewd6d with dissolve
$ renpy.pause()
scene anim_jade_bj3_ep4 with dissolve
mc "Oh...[jade]... I'm gonna cum!!!"
scene ep4_jade_bj_cum with hpunch
$ renpy.pause(0.5)
scene ep4_jade_bj_cum with hpunch
$ renpy.pause(0.5)
scene ep4_jade_bj_cum with hpunch
ja "*{i}Gulp{/i}*"
scene ep4_jade_bj_cum2 with dissolve
$ renpy.pause()
scene ep4_jade_bj_cum4 with dissolve
ja "*{i}Lick{/i}*"
scene ep4_jade_bj_cum3 with dissolve
ja "*{i}Smack{/i}*"
scene ep4_jade_lewd7 with dissolve
mc "*{i}Breathes heavily{/i}*"
mc "Oh...[jade].... That was so fucking good..."
mc "I didn't want to cum that fast..."
scene ep4_jade_lewd9 with dissolve
mc "Fuck..."
scene ep4_jade_lewd8 with dissolve
ja "What's wrong, [mc_jade]?"
scene ep4_jade_lewd9b with dissolve
mc "I really wanted to fuck you tonight."
scene ep4_jade_lewd8 with dissolve
ja "You will. That's why we started out here."
ja "Now that I know you really want it..."
ja "...we're going back to my place."
ja "I couldn't take the risk before knowing it for sure."
scene ep4_jade_lewd7 with dissolve
mc "Your place? Your husband isn't at home?"
scene ep4_jade_lewd8 with dissolve
ja "Of course he is. You're gonna fuck me in front of him."
scene ep4_jade_lewd7 with dissolve
mc "WHAT!?"
scene ep4_jade_lewd14 with dissolve
ja "Hahaha..."
stop music fadeout 5
ja "Relax. I'm only pulling your leg."
scene ep4_jade_lewd8 with dissolve
ja "It's just going to be you and me, [mc_jade]."
scene ep4_jade_lewd16 with fade
play music "<from 46>music/ep4/midnight_stroll.mp3"
mc "You live in the city?"
scene ep4_jade_lewd17 with dissolve
ja "Yes, I do."
ja "Now this is important."
ja "In about one minute, I'm going to need you to duck and hide in the front seat."
ja "Stay hidden until I tell you the coast is clear. Do you understand?"
scene ep4_jade_lewd18 with dissolve
mc "Yes, [jade]..."
scene ep4_jade_lewd17 with dissolve
ja "Good boy."
scene ep4_jade_lewd19 with dissolve
ja "Ok. Now, hide."
scene ep4_jade_lewd18 with dissolve
mc "Can I talk?"
scene ep4_jade_lewd21 with dissolve
ja "Shh..."
scene ep4_jade_lewd20 with dissolve
menu:
    "Just stay hidden" if True:
        $ renpy.pause(0.5)
    "Tease her" if True:
        scene ep4_jade_lewd20b with dissolve
        mc "*{i}Whispers{/i}* Ok, [jade]..."
        ja "Such a naughty boy..."
        ja "Mmm..."
        scene ep4_jade_lewd23 with dissolve
        ja "When we get home...[jade] is going to punish you."

scene ep4_jade_lewd24 with dissolve
ja "Ok. I'm going to call the elevator. When the car beeps you get out and walk straight into it."
scene ep4_jade_lewd25 with dissolve
mc "(This is too hot... I feel like a secret agent.)"
play sound "sound_effects/car_beep.mp3"
scene ep4_jade_lewd25b with dissolve
"*{i}Car beeps{/i}*"
mc "(That's my cue.)"
scene ep4_jade_lewd26 with dissolve
ja "Good. Look straight ahead. No eye contact."
scene ep4_jade_lewd27 with dissolve
ja "You're getting off at floor 18. Exit and use the staircase. Go down to floor 17."
ja "Wait 3 minutes before exiting the stairwell. If I haven't knocked on the door...the coast is clear."
ja "My apartment is the first one on the right. Don't knock. Just enter."
mc "I got it."
scene ep4_jade_lewd28 with dissolve
$ renpy.pause()
scene ep4_jade_lewd29 with fade
mc "(Agent [name]...with a license to fuck married teachers.)"
mc "(Ok...that sounded stupid.)"
scene ep4_jade_lewd28b with dissolve
mc "(3 minutes are up...)"
mc "(She didn't knock...the coast is clear.)"
menu:
    "First door on the right" if True:
        scene ep4_jade_lewd29c with dissolve
        mc "(Just...enter.)"
    "First door on the left" if True:
        mc "(Just...enter.)"
        play sound "sound_effects/door_lock.mp3"
        scene ep4_jade_lewd29b with dissolve
        mc "(This door is locked...)"
        mc "(Wait...did she say left or right?)"
        scene ep4_jade_lewd29c with dissolve
        mc "(Let's try this one instead.)"
scene ep4_jade_lewd30 with dissolve
mc "(Ok...)"
mc "(Where is she?)"
mc "(I'm not gonna be an idiot and call out for her.)"
ja "Lock the door."
ja "The bedroom is to the left."
scene ep4_jade_lewd32 with dissolve
mc "Are you in here?"
scene ep4_jade_lewd33 with dissolve
$ renpy.pause()
scene ep4_jade_lewd34 with dissolve
ja "I'm impressed, [mc_jade]."
ja "You follow instructions well."
scene ep4_jade_lewd34b with dissolve
$ renpy.pause()
scene ep4_jade_lewd35 with dissolve
ja "Remove all your clothes and get on the bed."
scene ep4_jade_lewd36 with dissolve
mc "This is so hot, [jade]."
ja "Do you know what's even hotter?"
mc "No, what?"
play sound "sound_effects/door_lock.mp3"
scene ep4_jade_lewd39 with hpunch
ja "This."
mc "Handcuffs? Really?"
scene ep4_jade_lewd41 with dissolve
ja "Trust me, I'm not about to take a naked young student prisoner."
ja "This just adds some extra spice to it."
scene ep4_jade_lewd42 with dissolve
ja "Stay here while [jade] gets ready for you..."
scene ep4_jade_lewd43 with dissolve
mc "(This is awkward...)"
mc "(Naked and cuffed in my teacher's bed...)"
scene ep4_jade_lewd44 with dissolve
mc "(That photo...doesn't make this better.)"
scene ep4_jade_lewd45 with dissolve
mc "(She's sure taking her sweet time...)"
mc "(People actually use handcuffs when they have sex?)"
mc "(I thought that was a movie thing...)"
mc "(It's a bit scary... She could pretty much do whatever she wants to me and I couldn't do anything about it...)"
mc "(Oh God... I hope she's not planning to do something weird to me...)"
ja "Over here, [mc_jade]...[jade] is here."
scene ep4_jade_lewd47 with dissolve
menu:
    "You look so hot" if True:
        mc "You look so hot in that, [jade]..."
    "Turn around for me" if True:
        $ dk(1)
        mc "Oh, wow... Turn around for me..."
        scene ep4_jade_lewd48 with dissolve
        ja "Do you like it?"
        mc "Fuck yeah, I do!"
scene ep4_jade_lewd49 with dissolve
ja "Look at you..."
ja "Such a big strong young boy..."
ja "But right now, you're all powerless."
scene ep4_jade_lewd50 with dissolve
ja "All powerless..."
ja "...and [jade] is in control."
scene ep4_jade_lewd51 with dissolve
ja "Haha...I remember back when I was a teenager."
ja "It was always fascinating to see how hard boys got so quickly."
ja "And let me tell you, that's something that changes with age."
scene ep4_jade_lewd52 with dissolve
ja "I have barely touched you and you're already ready for me."
mc "Yeah, that's just how hot you are, [jade]."
scene ep4_jade_lewd54 with dissolve
ja "Can you feel my pussy through my panties?"
ja "The warmth...and the wetness...?"
scene ep4_jade_lewd55 with dissolve
ja "This time I don't want you to shoot your load so goddamn fast. Do you get that?"
ja "If you're even close to cumming, you tell me immediately."
ja "Because I'm going to wear that dick you have down to a knob."
scene ep4_jade_lewd56 with dissolve
ja "I'm going to show you that experience is way better than youth..."
ja "And that you don't have to spell coconut with your hips to give a man the ride of their life."
scene ep4_jade_lewd57 with dissolve
ja "What's that look on your face?"
ja "Are you scared?"
scene ep4_jade_lewd58 with dissolve
mc "A little bit...yeah."
scene ep4_jade_lewd57 with dissolve
ja "Good."
mc "What?"
stop music fadeout 3
scene ep4_jade_lewd60 with dissolve
ja "Shut up! It's [jade]'s turn to have her fun, now."
play music "music/ep3/some_obsession.mp3"
scene ep4_jade_lewd60b with dissolve
ja "Oh, yes!!!"
mc "Shiiit! Jade..."
if jade != "Jade":
    ja "Don't you break character! What's my name?"
    mc "It's [jade]..."
    ja "Damn straight and don't you forget it."
scene anim_jade_ride_ep4 with dissolve
mc "Ride me, [jade]..."
if jade != "Jade":
    ja "Shut up, [mc_jade]. Listen to what [jade] tells you!"
elif True:
    ja "Shut up, [mc_jade]. Listen to what I tell you!"
$ renpy.pause()
scene anim_jade_ride2_ep4 with dissolve
ja "Those cuffs aren't coming loose until I cum and you shoot a load over me."
$ renpy.pause()
scene anim_jade_ride3_ep4 with dissolve
mc "Wow, you're really bouncing hard..."
ja "FUCK ME!!!"
$ renpy.pause()
scene anim_jade_ride4_ep4 with dissolve
mc "(That look in her eyes...)"
mc "(Is it pure and raw lust? Seems like hatred, too...)"
mc "(She's using me to get an outlet for her frustrations...)"
mc "(It's so fucking hot!)"
scene anim_jade_ride5_ep4 with dissolve
ja "Oh, fuck me, [mc_jade]! This is so dirty and kinky!"
mc "Yeah, [jade]... Wanna know something that would make it even kinkier?"
ja "Yes! Tell me!"
mc "(Man...I hope I don't blow it...)"
mc "Grab my phone and film us fucking..."
mc "I want to watch that video and jack off to it later."
$ renpy.pause()
scene ep4_jade_lewd61 with dissolve
ja "..."
ja "You want to jack off to me fucking you?"
mc "Yeah... I don't wanna forget this moment, [jade]."
scene ep4_jade_lewd63 with dissolve
ja "The idea of it makes me so fucking horny..."
ja "The movie...cannot be shown to anyone. Do you understand me?"
scene ep4_jade_lewd64 with dissolve
mc "It's only for me... I promise!"
scene ep4_jade_lewd63 with dissolve
ja "You have to delete it after you've watched it. Promise me that!"
scene ep4_jade_lewd64 with dissolve
mc "I promise... I just want to see your hot body riding me again."
scene ep4_jade_lewd66 with dissolve
ja "Ok. I'm gonna give you something to jack off to, [mc_jade]."
scene anim_jade_ride6_ep4 with dissolve
ja "I'm gonna fuck your brains out, [mc_jade]!"
mc "Ride me, [jade]!"
$ renpy.pause()
scene ep4_jade_lewd67 with dissolve
ja "That's enough of that..."
ja "Let me spin around..."
scene anim_jade_ride7_ep4 with dissolve
ja "How do you like this?"
mc "Yes! Don't stop!"
ja "I could never do this position with Stephen's cock; it keeps falling out when I'm at the top..."
ja "But not with yours...it's right where it should be...pressing hard against my insides."
$ renpy.pause()
scene anim_jade_ride8_ep4 with dissolve
mc "You ride like a pro!"
ja "I told you. Nothing beats experience!"
ja "If you can't use it the right way, it doesn't matter how tight that pussy is."
$ renpy.pause()
scene ep4_jade_lewd68 with dissolve
ja "How are you feeling?"
scene ep4_jade_lewd69 with dissolve
mc "Great... I'm so fucking horny, I think I'm gonna burst."
scene ep4_jade_lewd68 with dissolve
ja "Not yet."
ja "I have something for us."
scene ep4_jade_lewd70 with dissolve
mc "Hey...what's that?"
ja "It's an oil..."
ja "This will give both you and me the most explosive orgasm you can get."
scene ep4_jade_lewd71 with dissolve
mc "It's cold..."
ja "When you're getting close to cumming, your cock will swell up with pleasure."
scene ep4_jade_lewd72 with dissolve
ja "Let's try something new..."
mc "This is so hot..."
play sound "sound_effects/slap.mp3"
scene ep4_jade_lewd74 with hpunch
ja "Shut up, [mc_jade]!"
mc "Yes...[jade]..."
scene anim_jade_doggy_ep4 with dissolve
ja "I'm in control now!"
ja "*{i}Moans{/i}*"
pause
scene anim_jade_doggy2_ep4 with dissolve
mc "It feels like the bed might break from this."
ja "Then let it break!"
pause
scene anim_jade_doggy3_ep4 with dissolve
ja "*{i}Moans{/i}*"
mc "(Shit! She's so fucking into it...)"
mc "(It's like she's obsessed! I don't know if I should be turned on or scared..."
mc "(...but I'm as hard as I can get!)"
scene ep4_jade_lewd72 with dissolve
ja "Enough of this!"
ja "It's your turn to pound me!"
scene ep4_jade_lewd76 with dissolve
ja "No matter how much I scream! You don't stop!"
scene ep4_jade_lewd76b with dissolve
ja "Pound me as hard as you fucking can!"
mc "Yes, [jade]."
scene anim_jade_doggy4_ep4 with dissolve
ja "*{i}Moans{/i}*"
ja "YES!!!"
ja "HARDER!"
pause
scene anim_jade_doggy5_ep4 with dissolve
ja "I said HARDER!!!"
mc "I'm doing it as hard as I can!"
pause
scene ep4_jade_lewd77 with dissolve
ja "Aarrgh!!!"
$ renpy.sound.play("sound_effects/glass.mp3", channel="sfx1", loop=False)
$ renpy.sound.play("sound_effects/shove.mp3", channel="sfx2", loop=False)
scene ep4_jade_lewd78 with hpunch
mc "Ouch!"
scene ep4_jade_lewd79 with dissolve
ja "Shut up!"
scene anim_jade_wall_ep4 with dissolve
ja "Fuck you Stephen! You pathetic sack of shit!!!"
ja "You think you can buy yourself titles instead of earning them don't you!?"
ja "Honorary Professor!? That's fucking pathetic!!!"
pause
scene anim_jade_doggy7_ep4 with dissolve
ja "I earned {b}my{/b} title! How about you try that for a change?"
pause
scene anim_jade_doggy8_ep4 with dissolve
mc "(She's really using me to get rid of those pent-up anger issues...)"
mc "(Does that work? I could try it, too...)"
pause
$ renpy.sound.play("sound_effects/shove.mp3", channel="sfx2", loop=False)
scene ep4_jade_lewd80 with hpunch
ja "Huh!?"
scene ep4_jade_lewd81 with dissolve
ja "Yes..."
scene ep4_jade_lewd82 with dissolve
ja "YES!"
scene anim_jade_doggy9_ep4 with dissolve
mc "That's it! Take my cock, [jade]!"
ja "*{i}Moans{/i}*"
scene ep4_jade_lewd83b
wife "Come to bed! What the hell is it that you're looking at for so long?"
scene ep4_jade_lewd83c
husband "Shut up, Lynda!"
scene anim_jade_doggy9_ep4 with dissolve
mc "SHIT!!! This is what you meant!!!"
mc "My dick! It's fucking swelling up!!!"
ja "MMMM!!! MMM!!!!!!"
scene anim_jade_cum_ep4 with dissolve
mc "AAAAHHH!!!!"
scene anim_jade_cum2_ep4 with dissolve
mc "FUCK!!! THAT'S TOO INTENSE!"
mc "AAAHHH!! Is it supposed to feel this much!?"
scene ep4_jade_lewd85 with dissolve
ja "HAHAHA! OH FUCK! HAHAHA!!!"
ja "I'm trembling!!!"
mc "AAHH!!!!"
scene ep4_jade_lewd86 with dissolve
ja "Thank you..."
ja "You have no idea how much I needed that."
stop music fadeout 5
scene ep4_jade_lewd87 with dissolve
mc "I think I came inside you a bit. You're on the pill, right?"
scene ep4_jade_lewd86 with dissolve
ja "No...but you don't need to worry about that."
scene ep4_jade_lewd88 with dissolve
ja "Join me for a bath, [mc_jade]."
ja "Let's get ourselves cleaned up."

play music "<from 20>music/ep4/relax.mp3"
scene ep4_jade_bath with fade
$ renpy.sound.play("sound_effects/bathing.mp3", channel="sfx1", loop=True)
ja "I'm sorry for being a bit...aggressive back there."
scene ep4_jade_bath1 with dissolve
mc "Aggressive? I thought it was passion."
scene ep4_jade_bath with dissolve
ja "Maybe a bit of both."
ja "It's the first time in many months I've had the chance to get that release."
scene ep4_jade_bath1 with dissolve
mc "I am so relaxed right now."
scene ep4_jade_bath4 with dissolve
ja "I've never done this before."
ja "With a student, I mean."
ja "It's a line I never thought I'd cross."
scene ep4_jade_bath1 with dissolve
mc "What made you do it?"
scene ep4_jade_bath with dissolve
ja "I'd chalk it up to the constant fights with Stephen, his cheating and you reciprocating my advances."
ja "I truly needed this."
scene ep4_jade_bath1 with dissolve
mc "Me too."
if ep3_envyLewd == 2:
    mc "I'm not that experienced with older women."
    mc "I fantasize about it, but never thought that teachers did it, too."
elif True:
    mc "I've never fucked an older woman before."
    mc "I have fantasized about it, but never thought that teachers did it, too."
scene ep4_jade_bath4 with dissolve
ja "It's not something you talk about, to anyone, but of course teachers have those fantasies."
ja "It will cross the mind of even the most prudish teacher."
ja "It's dirty and taboo. That's what makes it so much hotter."
scene ep4_jade_bath5 with dissolve
mc "I see."
scene ep4_jade_bath4 with dissolve
ja "Speaking of things you don't talk about..."
ja "What we just did can ruin both of our futures."
ja "Are you sure you're capable of keeping this secret?"
mc "(Fuck... I'm so torn...)"
scene ep4_jade_bath5 with dissolve
mc "Yeah..."
scene ep4_jade_bath4 with dissolve
ja "Good."
scene ep4_jade_bath1 with dissolve
mc "Will we be doing this again?"
scene ep4_jade_bath14 with dissolve
ja "Can't get enough of [jade], can you?"
scene anim_jade_fj_ep4 with dissolve
ja "Let me answer you like this..."
pause
scene anim_jade_fj2_ep4 with dissolve
ja "You like this, don't you?"
mc "Yeah, very much..."
pause
stop music
$ renpy.music.stop(channel="sfx1", fadeout=0)
scene ep4_jade_bath16
bu "Honey? Are you in the bath?"
play music "music/ep4/let_her_in.mp3"
scene ep4_jade_bath17
ja "Oh, no..."
play sound "sound_effects/water_splash.mp3"
scene ep4_jade_bath18 with vpunch
ja "Um...wait!"
play sound "sound_effects/door_lock.mp3"
scene ep4_jade_bath19 with vpunch
"*{i}Click{/i}*"
ja "I'm not decent, right now!"
bu "Come on, honey. I've seen you naked many times."
scene ep4_jade_bath22 with dissolve
ja "I'm mad at you!"
scene ep4_jade_bath23 with dissolve
bu "This again!?"
scene ep4_jade_bath22 with dissolve
ja "Not \"again\"! I never stopped being mad!"
scene ep4_jade_bath23 with dissolve
bu "Open up and let's talk it out."
scene ep4_jade_bath24 with dissolve
ja "*{i}Whispers{/i}* What are you doing?"
scene ep4_jade_bath25 with dissolve
ja "*{i}Moan{/i}*"
scene anim_jade_doggy10_ep4 with dissolve
bu "Honey?"
ja "Go away or I'll find something to throw at you!"
bu "This is ridiculous! Open up, right now, or I'll go get the screwdriver."
pause
scene ep4_jade_bath25b with dissolve
ja "No! If you get the screwdriver, you can bring the divorce papers with it!"
scene anim_jade_doggy11_ep4 with dissolve
bu "Will you stop threatening me with that! We're not getting divorced!"
ja "Only because you were stupid to not get a prenup, you jackass!"
ja "Leave me alone!"
bu "Fuck this! I'm trying here, honey! You've got to work with me on this."
ja "If you really want me to try, respect me and leave right now! Go to the bar and don't come back until they close!"
play sound "sound_effects/footsteps_indoors.mp3"
"*{i}Footsteps{i}*"
pause
scene ep4_jade_bath26 with hpunch
$ renpy.pause(0.5)
scene ep4_jade_bath26 with hpunch
$ renpy.pause(0.5)
scene ep4_jade_bath26 with hpunch
$ renpy.pause()
stop music fadeout 5
scene ep4_jade_bath27 with dissolve
ja "*{i}Breathes heavily{/i}*"
scene ep4_jade_bath29 with dissolve
ja "*{i}Whispers{/i}* If that didn't make me cum in silence, I would have slapped you."
ja "*{i}Whispers{/i}* Playtime is over. It's time for us to get you out of here."
$ renpy.end_replay()
$ persistent.ep4_lewd_jade = True
$ calcScenes()
$ bios_history_jade += "I fucked Jade and recorded a video of it. We almost got caught by her husband.\n\n"
$ bios_name_jade = True
$ chat_new_bios = True
if steamAchievements and not config.console and not config.developer:
    $ achievement.grant("HOTFORTEACHER")
    init:
        $ achievement.register("HOTFORTEACHER")
    $ achievement.Sync()
jump ep4_sat_morning_label

label ep4_jm_dorm_talk_label:
play music "music/ep4/all_of_the_pieces.mp3"
scene ep4_jm_dorm_talk with fade
mc "It's just been a couple of days, but it still feels weird to be back here..."
scene ep4_jm_dorm_talk1 with dissolve
my "Are you planning on moving back in?"
scene ep4_jm_dorm_talk2 with dissolve
mc "I don't know... I'm pretty sick of not having a real place to stay."
mc "All of this sneaking around, finding temporary solutions...it has to stop."
mc "And maybe it does, if I become a DIK tomorrow..."
scene ep4_jm_dorm_talk1 with dissolve
my "Let's wait and see, then..."
scene ep4_jm_dorm_talk2 with dissolve
mc "Yeah. At least you got yourself the perfect roommate."
scene ep4_jm_dorm_talk3 with dissolve
js "In a perfect world, maybe. I can't stay here like this. This won't work out for us in the long run, with Maya's dad and all."
my "Can we not talk about that tonight? I don't want it to ruin what just happened between us."
js "All right...but [name] knows why you're pledging the HOTs, right?"
scene ep4_jm_dorm_talk6 with dissolve
mc "Yeah, I know she needs the free tuition."
mc "Is that why you do it, too?"
scene ep4_jm_dorm_talk7 with dissolve
js "I'm not gonna lie...I'd love to be in a sorority..."
js "...but helping Maya is the real reason."
js "As you know, my dad already saved up for my tuition... I just need to get a hold of that money."
js "I kinda left without even talking to him..."
scene ep4_jm_dorm_talk7b with dissolve
js "So, if I get his money plus the money from the HOTs...this will all be over."
js "We just need to do that...um...scavenger hunt."
my "He knows about it..."
if ep3_mayaOfferedHelp:
    my "He's even offered to help me with that list..."
    if ep3_mayaLewd:
        my "...and he already has."
scene ep4_jm_dorm_talk9 with dissolve
js "That's awesome! Then we're totally gonna make it!"
js "You'll help us with completing that list, right?"
scene ep4_jm_dorm_talk10 with dissolve
mc "Have you seen what's on that list? There are so many sexual tasks on it."
scene ep4_jm_dorm_talk11 with dissolve
js "Yeah, I know. It's crazy..."
js "...but it's for free tuition..."
js "...do you even realize how much money that is?"
scene ep4_jm_dorm_talk12 with dissolve
my "But showing Quinn any proof of me doing those things makes me feel sick."
my "I've been thinking a lot about it... I want to complete that list, but..."
my "...it makes me feel like a...prostitute."
scene ep4_jm_dorm_talk12b with dissolve
js "Come on, we don't have to be stupid about it!"
js "We're obviously gonna fake it all!"
js "Ashley and Lily were trying to cheat, so why can't we?"
js "We can use internet porn or maybe...a dildo!"
scene ep4_jm_dorm_talk12 with dissolve
if ep3_mayaLewd:
    my "[name] came up with that idea, too."
my "It's not a bad idea...but real or fake...we still have to show that proof."
scene ep4_jm_dorm_talk13 with dissolve
mc "About Quinn... She just has to see the pictures or whatever...right?"
scene ep4_jm_dorm_talk14 with dissolve
my "Yeah?"
scene ep4_jm_dorm_talk13 with dissolve
mc "What if you just show it and never give it to her?"
scene ep4_jm_dorm_talk14 with dissolve
my "What if she takes it from us?"
scene ep4_jm_dorm_talk13 with dissolve
mc "I'll be with you when you show it to her. Then she can't steal it."
scene ep4_jm_dorm_talk14b with dissolve
js "What if she claims she never saw it?"
scene ep4_jm_dorm_talk13 with dissolve
mc "..."
mc "We show it to her and another HOT!"
mc "Someone we can trust. That way she can't lie about never seeing it."
scene ep4_jm_dorm_talk18 with dissolve
my "That's a really good idea!"
js "Yeah! So...we're gonna cheat, right?"
scene ep4_jm_dorm_talk20 with dissolve
my "What do you think?"
scene ep4_jm_dorm_talk21 with dissolve
mc "It's up to you..."
mc "I'd be lying if I said I didn't want to help you in person with that list..."
if ep3_mayaLewd:
    mc "...but cheating removes that forced feeling you were talking about earlier."
    scene ep4_jm_dorm_talk20 with dissolve
    my "Exactly..."
elif True:
    mc "...but cheating maybe is the best way for us to go."
    scene ep4_jm_dorm_talk20 with dissolve
    my "Yeah...so it doesn't feel forced."
scene ep4_jm_dorm_talk22 with dissolve
js "This is perfect! We have a whole week to do it, too!"
js "That's plenty of time to figure out the details!"
scene ep4_jm_dorm_talk23 with dissolve
mc "It should be possible."
scene ep4_jm_dorm_talk24 with dissolve
js "We're gonna make this work, Maya."
my "Yeah!"
scene ep4_jm_dorm_talk26 with dissolve
js "So...[name]..."
js "Are you staying the night?"
scene ep4_jm_dorm_talk27 with dissolve
mc "Sure, it's getting late."
scene ep4_jm_dorm_talk26 with dissolve
js "My bed or her bed?"
scene ep4_jm_dorm_talk27 with dissolve
if ep2_fuckedJosy and ep3_mayaLewd and renpy.variant("pc"):
    menu:
        "Sleep with Josy" if True:
            jump ep4_sleepJosy
        "Sleep with Maya" if True:
            jump ep4_sleepMaya
        "Sleep on the floor" if True:
            jump ep4_sleepBoth
elif True:
    menu:
        "Sleep with Josy" if True:
            jump ep4_sleepJosy
        "Sleep with Maya" if True:
            jump ep4_sleepMaya

label ep4_sleepBoth:
$ ep4_sleptWith = "both"
$ RPmaya += 1
$ RPjosy += 1
mc "I'll...take the floor."
scene ep4_jm_dorm_talk31 with dissolve
js "The floor? Why?"
my "Yeah, that's not comfortable at all."
scene ep4_jm_dorm_talk27 with dissolve
mc "I'll be fine with it."
scene ep4_jm_dorm_talk24 with dissolve
js "I think he doesn't want to choose."
my "That's cute."
js "Yeah."
scene ep4_jm_dorm_talk34 with dissolve
mc "No, I'm serious... It's not that bad."
scene ep4_jm_dorm_talk34b with dissolve
js "Move your ass."
my "Hahaha."
scene ep4_jm_dorm_talk35 with dissolve
js "There. That should make everyone happy."
scene ep4_jm_dorm_talk36 with dissolve
mc "(Yeah, that makes me happy...)"
scene ep4_jm_dorm_talk36b with dissolve
js "Are you coming?"
play sound "sound_effects/clothes.mp3"
scene ep4_jm_dorm_talk38 with vpunch
js "Haha! Look at him go!"
my "Hahaha!"
scene ep4_jm_dorm_talk39 with dissolve
mc "There..."
scene ep4_jm_dorm_talk40 with dissolve
$ renpy.pause()
scene ep4_jm_dorm_talk41 with dissolve
js "*{i}Whispers{/i}* I've missed you."
my "*{i}Whispers{/i}* Let's never fight like that again..."
stop music fadeout 3
jump ep4_sat_morning_label

label ep4_sleepJosy:
$ ep4_sleptWith = "josy"
$ RPjosy += 1
mc "Your bed. I've missed sleeping in it."
scene ep4_jm_dorm_talk26 with dissolve
js "All right."
scene ep4_jm_dorm_talk28b with dissolve
$ renpy.pause()
scene ep4_jm_dorm_talk28c with dissolve
js "Hop in."
scene ep4_jm_dorm_talk28d with dissolve
mc "Hey..."
scene ep4_jm_dorm_talk28e with dissolve
js "*{i}Mwah{/i}*"
scene ep4_jm_dorm_talk28f with dissolve
js "*{i}Whispers{/i}* I've missed you."
stop music fadeout 3
jump ep4_sat_morning_label

label ep4_sleepMaya:
$ ep4_sleptWith = "maya"
$ RPmaya += 1
mc "I'll go with Maya's bed. Unless she kicks me out of it."
scene ep4_jm_dorm_talk30 with dissolve
my "Haha! I promise to not do that."
scene ep4_jm_dorm_talk30b with dissolve
$ renpy.pause()
scene ep4_jm_dorm_talk30c with dissolve
my "Are you coming?"
scene ep4_jm_dorm_talk30d with dissolve
mc "Hi..."
scene ep4_jm_dorm_talk30e with dissolve
my "*{i}Mwah{/i}*"
scene ep4_jm_dorm_talk30f with dissolve
my "*{i}Whispers{/i}* Let's never fight like that again..."
stop music fadeout 3
jump ep4_sat_morning_label

label ep4_sat_morning_label:
scene ep4_sat_morning with Fade(2,2,2)
de "Are you ready?"
mc "Are you sure we're gonna do this?"
play music "music/ep4/optimistic.mp3"
de "There's no other way to do it."
de "This is it, you know? It's now or never."
mc "But what about the other tasks?"
scene ep4_sat_morning1 with dissolve
de "I...um...may have taken care of a few last night."
scene ep4_sat_morning2 with dissolve
mc "A few? Which ones?"
scene ep4_sat_morning1 with dissolve
de "Are we gonna drink or what?"
scene ep4_sat_morning2 with dissolve
mc "Tell me which tasks you did!"
scene ep4_sat_morning3 with dissolve
de "It's under control!"
de "And I really don't want to talk about it."
scene ep4_sat_morning2 with dissolve
mc "You're telling me later!"
scene ep4_sat_morning with dissolve
de "One-two-three-DRINK!"
if minigames:
    jump ep4_shot_game_label
scene ep4_derek_beer1 with dissolve
$ renpy.pause()
label ep4_sat_morning_label2:
play sound "sound_effects/bottle_clink.mp3"
scene ep4_sat_morning5 with dissolve
$ renpy.pause()
play sound "sound_effects/bottle_clink.mp3"
scene ep4_sat_morning6 with dissolve
mc "Why didn't we drink more earlier?"
scene ep4_sat_morning7 with dissolve
de "Because we're stupid! Don't stop!"
play sound "sound_effects/bottle_clink.mp3"
scene ep4_sat_morning8 with dissolve
$ renpy.pause()
play sound "sound_effects/bottle_clink.mp3"
scene ep4_sat_morning9 with dissolve
$ renpy.pause()
scene ep4_sat_morning10 with dissolve
de "DONE!"
play sound "sound_effects/burp.mp3"
scene ep4_sat_morning11 with dissolve
de "*{i}Burp{/i}*"
play sound "sound_effects/table_slam.mp3"
scene ep4_sat_morning12 with vpunch
$ renpy.pause()

scene ep4_sat_morning13 with wiperight
mc "You gotta tell me now..."
mc "What tasks did you do?"
scene ep4_sat_morning14 with dissolve
de "I got the third slap from Wendy."
if ep4_monaSlap:
    scene ep4_sat_morning13 with dissolve
    mc "Haha! No, you got the fourth slap!"
    mc "Mona slapped me two days ago."
    scene ep4_sat_morning16 with dissolve
    de "What...?"
    de "Doesn't matter... She would have slapped me anyway."
elif True:
    scene ep4_sat_morning13 with dissolve
    mc "That's great, dude..."
scene ep4_sat_morning14 with dissolve
de "So, that's one task that's done."
scene ep4_sat_morning17 with dissolve
mc "That's it?"
scene ep4_sat_morning18 with dissolve
de "No...um...I..."
de "I may have gotten two more."
scene ep4_sat_morning19 with dissolve
mc "Two more!? Wow! What the hell did you do?"
$ guideSuggestedPage = 115
scene ep4_sat_morning18 with dissolve
de "Do you trust me?"
scene ep4_sat_morning19 with dissolve
menu:
    "Yes" if True:
        $ ep4_toldDerekYouTrustHim = True
        mc "Yeah, I trust you."
        scene ep4_sat_morning18 with dissolve
        de "Great! Then, trust me with this."
    "No" if True:
        $ ep4_toldDerekYouTrustHim = False
        mc "Haha! No."
        scene ep4_sat_morning16 with dissolve
        de "You don't?"
        scene ep4_sat_morning19 with dissolve
        mc "You can't keep a secret if your life was depending on it."
        scene ep4_sat_morning18 with dissolve
        de "Yeah, right...but trust me with this!"
de "After doing the car wash, we just need to bang a teacher and we're done."
if ep4_fuckedJade:
    scene ep4_sat_morning13 with dissolve
    mc "(Jade... There's no turning back if I tell him about her...)"
    menu:
        "Tell him about Jade" if True:
            $ ep4_toldDerekAboutJade = True
            scene ep4_sat_morning26 with dissolve
            mc "Look at this."
            scene ep4_sat_morning27 with dissolve
            de "What the...!?"
            ja "{i}I'm gonna fuck your brains out, [mc_jade]!{/i}"
            mc "{i}Ride me, [jade]!{/i}"
            scene ep4_sat_morning28 with dissolve
            de "You beautiful bitch! You did it!"
            de "You actually fucked her!"
            de "Then we're totally gonna make it!"
            $ bios_history_derek += "I showed Derek the recording of me fucking Jade.\n\n"
            $ bios_name_derek = True
            $ chat_new_bios = True
        "Keep Jade a secret" if True:
            $ bios_history_derek += "I didn't show Derek the recording of me fucking Jade.\n\n"
            $ bios_name_derek = True
            $ chat_new_bios = True
            $ ep4_toldDerekAboutJade = False
            mc "(No... That will stay mine and Jade's secret...)"
            mc "(I'm gonna delete that video.)"
scene ep4_sat_morning13 with dissolve
mc "Is that really it?"
if not ep4_toldDerekAboutJade:
    scene ep4_sat_morning18 with dissolve
    de "It is, but fucking a teacher..."
    de "I still have no clue how to do it."
elif True:
    scene ep4_sat_morning14 with dissolve
    de "Hell yeah, [mc_de]! We're gonna be DIKs!"
scene ep4_sat_morning19 with dissolve
mc "You know...I could just deduce what you did last night, if I think about it."
scene ep4_sat_morning18 with dissolve
de "Please...don't think about it."
scene ep4_sat_morning19 with dissolve
mc "..."
mc "Did you fuck Wendy or Minny outdoors?"
scene ep4_sat_morning33 with dissolve
de "..."
mc "Hahaha!"
menu:
    "Wear the helmet" if True:
        $ ep4_wearHelmet = True
        $ ep4_saturdayHelmet = True
        $ ep3_hellWeekHelmet += 1
        scene ep4_sat_morning35 with dissolve
    "Let him keep it" if True:
        $ ep4_wearHelmet = False
        $ ep4_saturdayHelmet = False
        scene ep4_sat_morning13 with dissolve
mc "You sure are a team player."

label ep4_car_wash_label:
scene ep4_car_wash with wipeleft
dikcs "Hahaha!"
tm "That's some hot shit right there."
jac "My money's on sweetcheeks!"
if ep4_wearHelmet:
    scene ep4_car_wash2 with dissolve
elif True:
    scene ep4_car_wash2b with dissolve
le "I think they both got it!"
rs "Hell yeah! That's how it should be. This is a team effort, maggots!"
scene ep4_car_wash3 with dissolve
rs "In today's car wash it's HOTs versus DIKs!"
stop music fadeout 3
rs "And somehow the DIKs have never won."
label ep4_car_wash2_label:
play music "music/ep4/driving_rock.mp3"

scene ep4_car_wash4 with dissolve
$ renpy.pause()
scene ep4_car_wash5 with dissolve
$ renpy.pause()
scene ep4_car_wash6 with dissolve
$ renpy.pause()
scene ep4_car_wash7 with dissolve
$ renpy.pause()
scene ep4_car_wash8 with dissolve
$ renpy.pause()
scene ep4_car_wash9 with dissolve
$ renpy.pause()
scene ep4_car_wash9b with dissolve
$ renpy.pause()
scene ep4_car_wash9c with dissolve
$ renpy.pause()
scene ep4_car_wash9d with dissolve
$ renpy.pause()
scene ep4_car_wash9e with dissolve
$ renpy.pause()
scene ep4_car_wash9f with dissolve
$ renpy.pause()
scene ep4_car_wash10h with dissolve
if _in_replay:
    pause
elif True:
    mc "Somehow, huh?"
    scene ep4_car_wash with dissolve
    tm "Hey, if you manage to get $10 you should consider it a victory!"
    if ep4_wearHelmet:
        scene ep4_car_wash12 with dissolve
    elif True:
        scene ep4_car_wash12b with dissolve
    rs "Ok, everyone! Listen up!"
    rs "The rules are simple!"
    scene ep4_car_wash13 with dissolve
    rs "You get one hour to earn as much money as possible from washing cars!"
    rs "Wash the cars with sponges and bodies! Have fun with it!"
    if ep4_wearHelmet:
        scene ep4_car_wash12 with dissolve
    elif True:
        scene ep4_car_wash12b with dissolve
    rs "The team that earned the most money after the hour is up wins!"
    if ep4_wearHelmet:
        scene ep4_car_wash14 with dissolve
    elif True:
        scene ep4_car_wash14b with dissolve
    de "This is unfair! There are six of them! We're just two!"
    jm "That's not what's unfair, dude."
    if ep4_wearHelmet:
        scene ep4_car_wash12 with dissolve
    elif True:
        scene ep4_car_wash12b with dissolve
    rs "On your mark!"
    rs "Get set!"
    rs "WASH!"
    if ep4_wearHelmet:
        scene ep4_car_wash15
    elif True:
        scene ep4_car_wash15b
    play music "music/ep4/fluffing_a_duck.mp3"
    de "CAR WASH! GET YOUR CAR WASH HERE!"
    mc "They're not going to hear you yelling!"
    mc "Look at what the HOTs are doing! They have a sign! Fix our sign!!"
    play music "<from 40.1>music/ep4/driving_rock.mp3"
    scene ep4_car_wash13
    rs "The HOTs got one!"
scene ep4_car_wash18
$ renpy.pause()
scene ep4_car_wash19 with dissolve
$ renpy.pause()
scene anim_carwash_ep4 with dissolve
rs "Look at them go!"
$ renpy.pause()
scene ep4_car_wash19c with dissolve
$ renpy.pause()
scene ep4_car_wash19d with dissolve
$ renpy.pause()
scene ep4_car_wash19e with dissolve
$ renpy.pause()
if not _in_replay:
    play music "music/ep4/fluffing_a_duck.mp3"
    if ep4_wearHelmet:
        scene ep4_car_wash21
    elif True:
        scene ep4_car_wash21b
    mc "We're not getting anything here!"
    mc "What did you write on that sign?"
    scene ep4_car_wash22 with dissolve
    mc "$50!? Are you crazy!?"
    mc "Do you even know what a regular car wash costs?"
    if ep4_wearHelmet:
        scene ep4_car_wash23 with dissolve
    elif True:
        scene ep4_car_wash23b with dissolve
    de "This one is deluxe."
    scene ep4_car_wash24 with dissolve
    mc "Screw this! No one is gonna pay $50."
    de "$5!? Why don't you just give my body away for free!?"
    scene ep4_car_wash13 with dissolve
    rs "The HOTs got another one! The HOTs are on fire!"
    if ep4_wearHelmet:
        scene ep4_car_wash25 with dissolve
    elif True:
        scene ep4_car_wash25b with dissolve
    de "[mc_de_up]! We got one! WE GOT ONE!"
    if ep4_wearHelmet:
        scene ep4_car_wash26
    elif True:
        scene ep4_car_wash26b
    cs "That's right, boy. Reach in far now, you hear."
    de "Yes, Sir..."
    if ep4_wearHelmet:
        scene ep4_car_wash27 with dissolve
    elif True:
        scene ep4_car_wash27b with dissolve
    de "I feel so...violated..."
    play music "<from 60.1>music/ep4/driving_rock.mp3"
scene ep4_car_wash28
$ renpy.pause()
scene ep4_car_wash29 with dissolve
$ renpy.pause()
scene ep4_car_wash30 with dissolve
$ renpy.pause()
scene ep4_car_wash30b with dissolve
$ renpy.pause()
if not _in_replay:
    play music "music/ep4/fluffing_a_duck.mp3"
    if ep4_wearHelmet:
        scene ep4_car_wash31
    elif True:
        scene ep4_car_wash31b
    $ renpy.pause()
    if ep4_wearHelmet:
        scene ep4_car_wash32 with dissolve
    elif True:
        scene ep4_car_wash32b with dissolve
    $ renpy.pause()
    play music "<from 40.1>music/ep4/driving_rock.mp3"
scene ep4_car_wash34
$ renpy.pause()
scene ep4_car_wash35 with dissolve
$ renpy.pause()
scene ep4_car_wash36 with dissolve
$ renpy.pause()

if not _in_replay:
    play music "music/ep4/fluffing_a_duck.mp3"
    if ep4_wearHelmet:
        scene ep4_car_wash37
    elif True:
        scene ep4_car_wash37b
    de "Just ten minutes to go, [mc_de]!"
    de "How much did we make?"
    mc "What the fuck do you mean!?"
    mc "You're the one in charge of the money!"
    if ep4_wearHelmet:
        scene ep4_car_wash39 with dissolve
    elif True:
        scene ep4_car_wash39b with dissolve
    de "..."
    play music "<from 70.1>music/ep4/driving_rock.mp3"
scene anim_carwash2_ep4
$ renpy.pause()
scene anim_carwash3_ep4 with dissolve
$ renpy.pause()
$ renpy.end_replay()
$ persistent.ep4_lewd_carwash = True
$ calcScenes()
play music "music/ep4/fluffing_a_duck.mp3"
if ep4_wearHelmet:
    scene ep4_car_wash25
elif True:
    scene ep4_car_wash25b
de "We got one!"
mc "Don't you forget to charge her this time!"
if ep4_wearHelmet:
    scene ep4_car_wash44 with dissolve
elif True:
    scene ep4_car_wash44b with dissolve
rs "Put some ass into it, maggots!"
if ep4_wearHelmet:
    scene ep4_car_wash45 with dissolve
elif True:
    scene ep4_car_wash45b with dissolve
cs2 "You're quite the strapping young lad, aren't you?"
de "Thanks, Ma'am."
scene ep4_car_wash46 with dissolve
cs2 "Please, just call me Lydia."
if ep4_wearHelmet:
    scene ep4_car_wash45 with dissolve
elif True:
    scene ep4_car_wash45b with dissolve
cs2 "Where are you cute boys from?"
de "Burgmeister & Royce, Ma'am."
scene ep4_car_wash46 with dissolve
cs2 "Oh, you. It's Lydia."
cs2 "Burgmeister & Royce, you say?"
cs2 "You know, I used to teach there for 33 years."
if not ep4_toldDerekAboutJade:
    if ep4_wearHelmet:
        scene ep4_car_wash47 with dissolve
    elif True:
        scene ep4_car_wash47b with dissolve
    de "..."
elif True:
    if ep4_wearHelmet:
        scene ep4_car_wash45 with dissolve
    elif True:
        scene ep4_car_wash45b with dissolve
    de "You don't say..."
scene ep4_car_wash13 with dissolve
rs "One minute to go!"
rs "Wrap up your final customer!"
if not ep4_toldDerekAboutJade:
    if ep4_wearHelmet:
        scene ep4_car_wash48 with dissolve
    elif True:
        scene ep4_car_wash48b with dissolve
    play sound "sound_effects/burnout.mp3"
    mc "Derek?"
    if ep4_wearHelmet:
        scene ep4_car_wash49b with dissolve
    elif True:
        scene ep4_car_wash49 with dissolve
    mc "DEREK!"
    scene ep4_car_wash13 with dissolve
stop music fadeout 5
rs "Time's up!"
rs "HOTs! How much did you make?"
play music "music/ep4/inspiring_acoustic.mp3"
scene ep4_car_wash51 with dissolve
ly "$225!"
rs "That's amazing!"
rs "What about the DIKs!?"
if not ep4_toldDerekAboutJade:
    if ep4_wearHelmet:
        scene ep4_car_wash53 with dissolve
    elif True:
        scene ep4_car_wash53b with dissolve
    mc "Derek was in charge of the money..."
    mc "...and he left with an elderly customer."
elif True:
    if ep4_wearHelmet:
        scene ep4_car_wash54 with dissolve
    elif True:
        scene ep4_car_wash54b with dissolve
    de "How much did we make, [mc_de]?"
    if ep4_wearHelmet:
        scene ep4_car_wash55 with dissolve
    elif True:
        scene ep4_car_wash55b with dissolve
    mc "..."

label ep4_carwash_outro:
scene ep4_carwash_outro with dissolve
qu "Did you set it up?"
scene ep4_carwash_outro1 with dissolve
sa "Yeah, I did. It didn't take much convincing, really."
sa "He's been wanting to do something like this for a very long time."
scene ep4_carwash_outro2 with dissolve
qu "So, it's on?"
scene ep4_carwash_outro1 with dissolve
sa "Ugh... Yeah, but I don't like it."
scene ep4_carwash_outro2 with dissolve
qu "We are expanding like crazy this year, you know that, right?"
scene ep4_carwash_outro1 with dissolve
sa "Don't patronize me. Look who you're talking to."
scene ep4_carwash_outro4 with dissolve
qu "Six daughters, Sage! It's a record number for the HOTs."
scene ep4_carwash_outro1 with dissolve
sa "I wasn't the one insisting on letting Josy in. Also, I didn't think you would accept both Lily and Ashley, either."
scene ep4_carwash_outro2 with dissolve
qu "Even if I didn't, we would still be too many."
qu "We need that money..."
qu "...for the HOTs."
scene ep4_carwash_outro7 with dissolve
sa "..."
scene ep4_carwash_outro8 with dissolve
qu "But hey...if you're willing to let go of your pride..."
qu "...you could just run back home and ask for sponsorship."
scene ep4_carwash_outro9 with dissolve
sa "That's a fucking line you don't cross!"
scene ep4_carwash_outro10 with dissolve
qu "..."
scene ep4_carwash_outro11 with dissolve
sa "I'm helping you out and we'll do it your way..."
sa "...this time."
sa "But you're the one who has to break the news to Rusty and Tommy."
stop music fadeout 3
scene ep4_carwash_outro12 with dissolve
$ renpy.pause()

label ep4_dik_evaluation_label:
play music "music/ep4/fleetwood.mp3"
if not ep4_toldDerekAboutJade:
    if ep4_wearHelmet:
        scene ep4_dik_evaluation with wipeleft
    elif True:
        scene ep4_dik_evaluationb with wipeleft
    de "Hey."
    if ep4_wearHelmet:
        scene ep4_dik_evaluation2 with dissolve
    elif True:
        scene ep4_dik_evaluation2b with dissolve
    mc "Hey, where the fuck have you been?"
    if ep4_wearHelmet:
        scene ep4_dik_evaluation1b with dissolve
    elif True:
        scene ep4_dik_evaluation1 with dissolve
    de "Teacher task...check."
    if ep4_wearHelmet:
        scene ep4_dik_evaluation2 with dissolve
    elif True:
        scene ep4_dik_evaluation2b with dissolve
    mc "..."
    if ep4_wearHelmet:
        scene ep4_dik_evaluation4 with dissolve
    elif True:
        scene ep4_dik_evaluation4b with dissolve
    de "I understand why they call it Hell Week now."
    de "At least there won't be a pregnancy scare with this one..."
    if ep4_wearHelmet:
        scene ep4_dik_evaluation2 with dissolve
    elif True:
        scene ep4_dik_evaluation2b with dissolve
    mc "You're fucking nuts..."
    if ep4_wearHelmet:
        scene ep4_dik_evaluation5b with dissolve
    elif True:
        scene ep4_dik_evaluation5 with dissolve
    mc "No, don't show me the pictures!"
    if ep4_wearHelmet:
        scene ep4_dik_evaluation1b with dissolve
    elif True:
        scene ep4_dik_evaluation1 with dissolve
elif True:
    if ep4_wearHelmet:
        scene ep4_dik_evaluation1b with wipeleft
    elif True:
        scene ep4_dik_evaluation1 with wipeleft
de "We did it..."
de "Every single task..."
if ep4_wearHelmet:
    scene ep4_dik_evaluation6 with dissolve
elif True:
    scene ep4_dik_evaluation6b with dissolve
rs "Yoink!"
rs "You know what that means, right?"
scene ep4_dik_evaluation8 with dissolve
de "It's over..."
mc "It is!"
scene ep4_dik_evaluation9 with dissolve
de "It's over."
mc "We did it!"
scene ep4_dik_evaluation10 with dissolve
de "Hey! Can we cross our tasks off the pledge board?"
de "It's not up to date, at all."
scene ep4_dik_evaluation11 with dissolve
rs "Don't worry about that."
rs "This is your evaluation party. Everything will be thoroughly inspected."
scene ep4_dik_evaluation12 with dissolve
de "What's the matter?"
scene ep4_dik_evaluation13 with dissolve
mc "I have this weird feeling..."
scene ep4_dik_evaluation12 with dissolve
de "I know what you mean. Me too!"
de "I'm so fucking happy, right now."
scene ep4_dik_evaluation13 with dissolve
mc "No, it's not that..."
scene ep4_dik_evaluation16 with dissolve
mc "It feels like we forgot something..."
scene ep4_dik_evaluation17 with dissolve
$ renpy.pause()
scene ep4_dik_evaluation18 with dissolve
tm "Pick up... Just fucking pick up already."
scene ep4_dik_evaluation19 with dissolve
tm "{i}Where the fuck are you guys? You're supposed to be here. We have to start this.{/i}"
scene ep4_dik_evaluation20 with dissolve
tm "Listen up brothers and maggots!"
tm "This place will soon be swarming with girls!"
tm "We will have a huge fucking party tonight!"
tm "Maggots!"
tm "If you're invited or not depends on your evaluation."
tm "Everyone! Gather in the ceremonial hall!"
scene ep4_dik_evaluation23 with dissolve
de "This is a nice place! What a huge screen!"
scene ep4_dik_evaluation24 with dissolve
jm "Sit down in front, maggots. This is your night."
scene ep4_dik_evaluation25 with dissolve
mc "What's the evaluation like?"
jac "You'll see... Just relax and enjoy the show."
stop music
play sound "sound_effects/switch.mp3"
scene ep4_dik_evaluation27
le "*{i}Whispers{/i}* It's starting."
scene ep4_dik_evaluation28 with dissolve
play music "music/ep2/metal2.mp3"
rs "Brothers and maggots!"
rs "As your president, I officially declare Hell Week as being over!"
dikcs "*{i}Cheers{/i}*"
scene ep4_dik_evaluation29 with dissolve
rs "This past week our maggots have walked through Hell."
rs "Time has come to determine if the DIKs' forces will grow stronger..."
rs "...or if the weakest links will be cut from the chain to protect the future of our brotherhood."
rs "Let me present our Hell Week host..."
scene ep4_dik_evaluation30 with dissolve
rs "Diablo!"
dikcs "*{i}Cheers{/i}*"
tm "MAGGOTS!"
scene ep4_dik_evaluation31 with dissolve
tm "I am the one who'll cast the judgement..."
tm "I am the one who'll scrutinize every tiny detail of your endeavors..."
tm "I am the one who will decide your fate."
scene ep4_dik_evaluation32 with dissolve
tm "I am the one who will determine..."
tm "...if you walk out this mansion wearing..."
play sound "sound_effects/whoosh_2.mp3"
scene ep4_dik_evaluation33
tm "...the DIK jacket!"
stop music
play music "music/patched/track_previous.mp3"
jump ep4_save_here_label

label ep4_save_here_label:
hide screen phone_screen
scene black



$ renpy.pause(2)
$ persistent.ep4_completed = True
$ renpy.pause(1)
$ updateDikScore()
if steamAchievements and persistent.vault4 and not config.console and not config.developer:
    $ achievement.grant("VAULTLOOTER4")
    init:
        $ achievement.register("VAULTLOOTER4")
    $ achievement.Sync()
if steamAchievements and persistent.vault1 and persistent.vault2 and persistent.vault3 and persistent.vault4 and not config.console and not config.developer:
    $ achievement.grant("VAULTLOOTER")
    init:
        $ achievement.register("VAULTLOOTER")
    $ achievement.Sync()
if steamAchievements and not config.console and not config.developer:
    if maxedGender == 3 and maxedMath == 4 and maxedEnglish == 4:
        $ achievement.grant("TEACHERSPET")
        init:
            $ achievement.register("TEACHERSPET")
    if ep3_hellWeekHelmet == 5:
        $ achievement.grant("YOURMAJESTY")
        init:
            $ achievement.register("YOURMAJESTY")
    $ achievement.grant("EPISODE4")
    init:
        $ achievement.register("EPISODE4")
    if ep3_choseDerek:
        $ achievement.grant("BACHELORPAD")
        init:
            $ achievement.register("BACHELORPAD")
    elif ep3_choseSage:
        $ achievement.grant("PRESIDENTIALSUITE")
        init:
            $ achievement.register("PRESIDENTIALSUITE")
    elif ep3_choseBella:
        $ achievement.grant("THELAIROFTHEICEQUEEN")
        init:
            $ achievement.register("THELAIROFTHEICEQUEEN")
    if cpenalty == 0:
        $ achievement.grant("BEINGACHICK")
        init:
            $ achievement.register("BEINGACHICK")
    if dpenalty == 0:
        $ achievement.grant("BEINGADIK")
        init:
            $ achievement.register("BEINGADIK")
    $ achievement.Sync()
if steamConfig or nonPatreonConfig:
    if renpy.loadable("season2/scripts/update5.rpyc"):
        scene ep4_episode_endb
    elif True:
        scene ep4_season_end
elif True:
    if renpy.loadable("season2/scripts/update5.rpyc"):
        scene ep4_episode_endb
    elif True:
        scene ep4_episode_end
$ calcRenders()
$ renpy.pause()
scene black with fade
show screen scoremsg
$ renpy.pause(2)
hide screen scoremsg

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
    $ josyScore = RPjosy / 16.0
elif True:
    $ josyScore = RPjosy / -2.0
if RPmaya >= 0:
    $ mayaScore = RPmaya / 25.0
elif True:
    $ mayaScore = RPmaya / -5.0
if RPsage >=0:
    $ sageScore = RPsage / 18.0
elif True:
    $ sageScore = RPsage / -7.0
if RPisabella >= 0:
    $ isabellaScore = RPisabella / 13.0
elif True:
    $ isabellaScore = RPisabella / -9.0
if RPjill >= 0:
    $ jillScore = RPjill / 9.0
elif True:
    $ jillScore = RPjill / -5.0
$ episodeContLabel = "ep4_ending_label2"
jump ep4_report_jill_label
$ renpy.pause()
label ep4EndLabel:
stop music fadeout 2
$ renpy.pause(2)
hide screen phone_screen
if not steamConfig:
    $ badik_chapter = "1"
if renpy.loadable("season2/scripts/update5.rpyc"):
    jump startUpdate5
elif True:
    jump endOfVersion4
label endOfVersion4:
play music "music/ep4/jack_the_lumberer.mp3"
$ qM = quick_menu
$ quick_menu = 0
scene black
scene credits_long_intro
$ renpy.pause(1)
scene credits_long at transformBottom
$ renpy.pause(5)
$ renpy.pause()
hide massive_diks
stop music fadeout 5
if not steamConfig and not nonPatreonConfig:
    show version_end
    $ renpy.pause()
    hide version_end
scene twitter_promo
$ renpy.pause()
if not steamConfig and not nonPatreonConfig:
    scene patreon_promo
    $ renpy.pause()
elif steamConfig:
    if renpy.loadable("season2/scripts/update5.rpyc"):
        jump startUpdate5
    $ game_is_ending = True
    show screen dlc
    pause
    $ game_is_ending = False
elif True:
    if renpy.loadable("season2/scripts/update5.rpyc"):
        jump startUpdate5
$ quick_menu = qM
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
