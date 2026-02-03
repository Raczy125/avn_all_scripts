label splashscreen:
    if steamConfig:
        $ persistent.steam_owns_al = is_subscribed_app_al()
        $ persistent.steam_owns_guide_s1 = is_subscribed_app_guide_s1()
        $ persistent.steam_owns_s2 = is_subscribed_app_s2()
        $ persistent.steam_owns_guide_s2 = is_subscribed_app_guide_s2()
    if not steamConfig and not nonPatreonConfig:
        scene black
        play sound "gui/pinkcake_sound.mp3"
        $ renpy.movie_cutscene("gui/pinkcake_video.webm")
        stop sound
        scene black with dissolve
    if not persistent.default_text_box_mode:
        $ style.window.background = Image("gui/textbox_new.png", xalign=0.5, yalign=1.0)
        $ style.say_dialogue.xsize = 950
        $ style.say_dialogue.xpos = 498
        $ style.say_dialogue.xalign = 0.5
        $ style.say_dialogue.text_align = 0.5
        $ style.say_dialogue.xoffset = 0
        $ style.namebox.xalign=0.5
        $ style.say_label.xoffset = 0
        $ style.say_label.text_align = 0.5
        $ style.say_label.xalign = 0.5
        $ style.rebuild()
    window hide
    $ persistent.current_episode = 8
    if persistent.firstTimePlaying:
        play music "music/patched/track_previous.mp3"
        if not steamConfig and not nonPatreonConfig:
            scene black with Pause(1)
        show game_warning with dissolve
        $ renpy.pause(2)
        scene black
        stop music
        dpc "Hold on! Hold on! Stop the music!"
        dpc "Jill, you're up."
        scene disclaimer2 with dissolve
        $ renpy.music.set_volume(0.5,channel='music')
        play music "music/ep1/anachronist.mp3"
        $ renpy.sound.set_volume(1.0,channel='jill')
        $ renpy.sound.play("voice/jill_intro/intro_jill.mp3", channel="jill", loop=False)
        ji "Hi there!"
        $ renpy.sound.play("voice/jill_intro/intro_jill_2.mp3", channel="jill", loop=False)
        ji "{color=#ff7ffa}Dr PinkCake{/color} sent me to talk to you a bit before we start."
        $ renpy.sound.play("voice/jill_intro/intro_jill_3.mp3", channel="jill", loop=False)
        ji "You know, just some formalities."
        $ renpy.sound.play("voice/jill_intro/intro_jill_4.mp3", channel="jill", loop=False)
        ji "You're over 18 years old, right?"
        scene disclaimer5 with dissolve
        menu:
            "Yes" if True:
                scene disclaimer3 with dissolve
                $ renpy.sound.play("voice/jill_intro/intro_jill_5.mp3", channel="jill", loop=False)
                ji "That's great!"
            "Yes (lie)" if True:
                scene disclaimer3 with dissolve
                $ renpy.sound.play("voice/jill_intro/intro_jill_6.mp3", channel="jill", loop=False)
                ji "Haha, ok! {color=#ff7ffa}Dr PinkCake{/color} rummaged through his dad's porno magazines when he was 10 years old; you'll be fine."
                scene black
                dpc "That's not what you're supposed to say, Jill. You're supposed to tell them that they must be of a legal age to play it."
                $ renpy.sound.play("voice/jill_intro/intro_jill_7.mp3", channel="jill", loop=False)
                ji "That's not going to stop them."
                dpc "Do you want legal problems? I don't!"
                $ renpy.sound.play("voice/jill_intro/intro_jill_8.mp3", channel="jill", loop=False)
                ji "Fine..."
                scene disclaimer2 with dissolve
                $ renpy.sound.play("voice/jill_intro/intro_jill_9.mp3", channel="jill", loop=False)
                ji "You're not supposed to play this game if you're not of legal age. Please shut it down now."
                scene disclaimer5 with dissolve
                dpc "They're still there, aren't they?"
                scene disclaimer2 with dissolve
                $ renpy.sound.play("voice/jill_intro/intro_jill_10.mp3", channel="jill", loop=False)
                ji "Yup."
                scene disclaimer5 with dissolve
                dpc "Well, we tried."
            "No" if True:
                scene disclaimer2 with dissolve
                $ renpy.sound.play("voice/jill_intro/intro_jill_11.mp3", channel="jill", loop=False)
                ji "Ok, then you really should turn off the game right now."
                $ renpy.sound.play("voice/jill_intro/intro_jill_12.mp3", channel="jill", loop=False)
                ji "Go ahead."
                scene disclaimer5 with dissolve
                dpc "They're still there, aren't they?"
                scene disclaimer2 with dissolve
                $ renpy.sound.play("voice/jill_intro/intro_jill_10.mp3", channel="jill", loop=False)
                ji "Yup."
                scene disclaimer5 with dissolve
                dpc "Well, we tried."

        scene disclaimer3 with dissolve
        $ renpy.sound.play("voice/jill_intro/intro_jill_13.mp3", channel="jill", loop=False)
        ji "Before we start, I'm going to ask you a few questions."
        $ renpy.sound.play("voice/jill_intro/intro_jill_14.mp3", channel="jill", loop=False)
        ji "Are you familiar with {color=#ff7ffa}Dr PinkCake's{/color} previous work?"
        scene disclaimer5 with dissolve
        menu:
            "Yes" if True:
                scene disclaimer6 with dissolve
                $ renpy.sound.play("voice/jill_intro/intro_jill_15.mp3", channel="jill", loop=False)
                ji "Uh-huh. Good."
                $ renpy.sound.play("voice/jill_intro/intro_jill_16.mp3", channel="jill", loop=False)
                ji "Then I'm sure you have some expectations or preconceived notions about what this game will be."
            "No" if True:
                scene disclaimer6 with dissolve
                $ renpy.sound.play("voice/jill_intro/intro_jill_17.mp3", channel="jill", loop=False)
                ji "Ok, that's fine. He created this game named Acting Lessons during 2018 that you might want to play."
                $ renpy.sound.play("voice/jill_intro/intro_jill_18.mp3", channel="jill", loop=False)
                ji "What he wanted me to say is that his...erm...style and approach to write these games are different."
        $ renpy.sound.play("voice/jill_intro/intro_jill_19.mp3", channel="jill", loop=False)
        ji "I wanted to take this moment to warn you of the contents in this game."
        $ renpy.sound.play("voice/jill_intro/intro_jill_20.mp3", channel="jill", loop=False)
        ji "You might come here expecting to get a fun and happy love story with lots of sexual content."
        scene black
        dpc "Tell them there will be loads of sex, Jill!!!"
        $ renpy.sound.play("voice/jill_intro/intro_jill_21.mp3", channel="jill", loop=False)
        ji "Really? I thought you wanted to be a serious adult novelist?"
        dpc "Gah!"
        scene disclaimer6 with dissolve
        $ renpy.sound.play("voice/jill_intro/intro_jill_22.mp3", channel="jill", loop=False)
        ji "Anyway, this game is not all about fun and happy times."
        $ renpy.sound.play("voice/jill_intro/intro_jill_23.mp3", channel="jill", loop=False)
        ji "Are you in a dark period of your life?"
        scene disclaimer7 with dissolve
        menu:
            "Yes" if True:
                scene disclaimer6 with dissolve
                $ renpy.sound.play("voice/jill_intro/intro_jill_24.mp3", channel="jill", loop=False)
                ji "Ok. That sucks. We've all been there or will be there at some point."
                scene disclaimer7 with dissolve
                dpc "Life is an inevitable march towards death, Jill!"
            "No" if True:
                scene disclaimer6 with dissolve
                $ renpy.sound.play("voice/jill_intro/intro_jill_25.mp3", channel="jill", loop=False)
                ji "Ok! That's good to know."
                scene disclaimer7 with dissolve
                dpc "A happy player, huh? I miss those days when I wasn't miserable..."
        scene disclaimer6 with dissolve
        $ renpy.sound.play("voice/jill_intro/intro_jill_26.mp3", channel="jill", loop=False)
        ji "Don't listen to him..."
        $ renpy.sound.play("voice/jill_intro/intro_jill_27.mp3", channel="jill", loop=False)
        ji "Are you easily offended?"
        scene disclaimer7 with dissolve
        menu:
            "Yes" if True:
                scene disclaimer6 with dissolve
                $ renpy.sound.play("voice/jill_intro/intro_jill_28.mp3", channel="jill", loop=False)
                ji "Then this game is definitely not for you."
            "No" if True:
                dpc "Great to hear, you fucking cunt!"
                dpc "Did he, she or it take offense?"
                scene disclaimer6 with dissolve
                $ renpy.sound.play("voice/jill_intro/intro_jill_29.mp3", channel="jill", loop=False)
                ji "No, I think we're good."
        $ renpy.sound.play("voice/jill_intro/intro_jill_30.mp3", channel="jill", loop=False)
        ji "Before starting the game, please ask yourself this question..."
        $ renpy.sound.play("voice/jill_intro/intro_jill_31.mp3", channel="jill", loop=False)
        ji "Am I ok with playing a game that might make me feel angry and/or sad?"
        $ renpy.sound.play("voice/jill_intro/intro_jill_32.mp3", channel="jill", loop=False)
        ji "If the answer is no, please do yourself a favor and stop right now."
        $ renpy.sound.play("voice/jill_intro/intro_jill_33.mp3", channel="jill", loop=False)
        ji "I'd hate to see you reach a point in the story that would upset you."
        scene disclaimer7 with dissolve
        dpc "I wouldn't, but I wanted to put up a disclaimer ahead of all the whining and other forms of fucking bullsh-"
        $ renpy.sound.play("voice/jill_intro/intro_jill_34.mp3", channel="jill", loop=False)
        scene black
        ji "Hey, you're talking to players and possible fans. Be nice!"

        scene disclaimer9 with dissolve
        $ persistent.firstTimePlaying = False
        $ renpy.sound.play("voice/jill_intro/intro_jill_35.mp3", channel="jill", loop=False)
        ji "Well, that's all I'm going to bother you with, for now."
        $ renpy.sound.play("voice/jill_intro/intro_jill_36.mp3", channel="jill", loop=False)
        ji "Don't worry, this conversation is a one-time thing. The next time you start the game you won't see it."
        if not steamConfig and not nonPatreonConfig:
            $ renpy.sound.play("voice/jill_intro/intro_jill_37.mp3", channel="jill", loop=False)
            ji "Have fun and enjoy!"
            scene black
            dpc "Tell them to donate money! I need their money!"
            scene disclaimer9 with dissolve
            $ renpy.sound.play("voice/jill_intro/intro_jill_38.mp3", channel="jill", loop=False)
            ji "If you happen to like the game, any donation you pledge at {color=#ff7ffa}Dr PinkCake's{/color} Patreon page will help him develop the game."
            $ renpy.sound.play("voice/jill_intro/intro_jill_39.mp3", channel="jill", loop=False)
            ji "He's a single indie developer doing this all by himself. Your pledge makes this game a reality."
        scene disclaimer10 with dissolve
        stop music fadeout 3
        $ renpy.sound.play("voice/jill_intro/intro_jill_40.mp3", channel="jill", loop=False)
        ji "Enough chatting. Without further ado..."
        $ renpy.sound.play("voice/jill_intro/intro_jill_41.mp3", channel="jill", loop=False)
        ji "Let me proudly present, {font=collegiate.ttf}Being a DIK{/font}."
        scene black with fade
        dpc "Did you show them your tits, Jill?"
        $ renpy.sound.play("voice/jill_intro/intro_jill_42.mp3", channel="jill", loop=False)
        ji "Wasn't it enough that I had to wear this slutty outfit?"
        dpc "You were supposed to show them your tits..."
        $ renpy.sound.play("voice/jill_intro/intro_jill_43.mp3", channel="jill", loop=False)
        ji "You go out there and show them your tits!"
        dpc "Well, I would, but then this would be a totally different kind of game and hairy tits isn't a common fetish-"
        $ renpy.music.set_volume(1,channel='music')
        dpc "Shit, is this thing still on?"
    play music "music/patched/track_previous.mp3"
    if not steamConfig and not nonPatreonConfig:
        scene black with Pause(1)
    show game_warning with dissolve
    $ renpy.pause()
    if steamConfig:
        show legal_info_steam_version with dissolve
    elif nonPatreonConfig:
        show legal_info with dissolve
        $ renpy.pause()
        show gog_screen with dissolve
        hide legal_info with dissolve
    elif True:
        show legal_info_patreon_version with dissolve
    $ renpy.pause()
    scene black with dissolve
    with Pause(0.5)
    return

init python:
    import math
    def name_func(newstring):
        store.name = newstring
        renpy.restart_interaction()
    def sname_func(newstring):
        store.name = newstring
        renpy.restart_interaction()

init python:
    def badik_chapter_save(d):
        d["badik_chapter"] = badik_chapter
    config.save_json_callbacks = [badik_chapter_save]
    def steamConfig_save(d):
        d["steamConfig"] = steamConfig
    config.save_json_callbacks = [steamConfig_save]
    achievement.Sync()

init python:
    g = Gallery()
    g.transition = dissolve
    loopMusic = False
    loopFightMusic = False
    loopPartyMusic = False
    loopMansionMusic = False
    loopMorningMusic = False
    loopLibraryMusic = False

    def queueChanCallback():
        if loopPartyMusic:
            randomswamp = renpy.random.choice(
            ("music/ep4/reaching_halo.mp3", "music/ep4/the_heat.mp3", "music/ep3/raveyard.mp3", "music/ep3/roads.mp3", "music/ep2/fallen_colors.mp3", "music/ep2/night_lights.mp3", "music/ep2/phate.mp3", "music/ep2/skyline.mp3", "music/ep2/sound_of_summer.mp3", "music/ep2/stryv.mp3"))
            renpy.music.queue(randomswamp, channel="music", loop=False, fadein=0, tight=True)
        elif loopLibraryMusic:
            randomswamp = renpy.random.choice(
            ("music/ep5/licensed_music/track11.mp3", "music/ep5/licensed_music/track14.mp3", "music/ep5/licensed_music/track5.mp3"))
            renpy.music.queue(randomswamp, channel="music", loop=False, fadein=0, tight=True)
        elif loopMusic:
            if renpy.loadable("season2/scripts/update5.rpyc"):
                randomswamp = renpy.random.choice( ("music/ep1/slow_day_blues.mp3","music/ep1/surf_punk_rock.mp3","music/ep1/threes_a_crowd.mp3","music/ep1/energetic.mp3","music/ep1/art_nouveau.mp3","music/ep1/apra_hyde.mp3","music/ep1/mumford.mp3","music/ep1/windswept.mp3","music/ep1/funk_rock.mp3","music/ep1/golden_alley.mp3","music/ep1/never_give_up.mp3","music/ep1/roadtrip.mp3","music/ep1/someways.mp3","music/ep1/winter_sunshine.mp3","music/ep1/classicals_breakbeat.mp3","music/ep1/credits.mp3","music/ep1/food_chain.mp3","music/ep1/scrapbook.mp3","music/ep1/my_heart.mp3","music/patched/track_previous.mp3","music/ep1/trow.mp3","music/ep1/fresh_air.mp3", "music/ep1/time_goes_by.mp3", "music/ep1/this_silence.mp3", "music/ep2/acoustic.mp3" ,"music/ep1/dont_count_on_me.mp3", "music/ep1/emptyv.mp3", "music/ep1/they_say.mp3", "music/ep1/unknown_power.mp3", "music/ep1/your_smile.mp3", "music/ep2/by_your_side.mp3","music/ep2/wings.mp3", "music/ep2/freedom.mp3", "music/ep2/journey_of_hope.mp3", "music/ep2/relaxing_ballad.mp3", "music/ep2/winter.mp3", "music/ep2/rockin_riff.mp3", "music/ep2/simple_ballad.mp3", "music/ep2/jingle.mp3", "music/ep2/feel_bad.mp3", "music/ep3/get_back.mp3", "music/ep3/dc_love_go_go.mp3", "music/ep3/sunny_acoustic_rock.mp3", "music/ep3/lets_begin.mp3", "music/ep3/chill.mp3", "music/ep5/licensed_music/track5.mp3","music/ep5/licensed_music/track7.mp3","music/ep5/licensed_music/track11.mp3","music/ep5/licensed_music/track14.mp3","music/ep5/licensed_music/track17.mp3","music/ep5/medicate_me.mp3","music/ep5/down.mp3","music/ep5/inspiring.mp3") )
            else:
                randomswamp = renpy.random.choice( ("music/ep1/slow_day_blues.mp3","music/ep1/surf_punk_rock.mp3","music/ep1/threes_a_crowd.mp3","music/ep1/energetic.mp3","music/ep1/art_nouveau.mp3","music/ep1/apra_hyde.mp3","music/ep1/mumford.mp3","music/ep1/windswept.mp3","music/ep1/funk_rock.mp3","music/ep1/golden_alley.mp3","music/ep1/never_give_up.mp3","music/ep1/roadtrip.mp3","music/ep1/someways.mp3","music/ep1/winter_sunshine.mp3","music/ep1/classicals_breakbeat.mp3","music/ep1/credits.mp3","music/ep1/food_chain.mp3","music/ep1/scrapbook.mp3","music/ep1/my_heart.mp3","music/patched/track_previous.mp3","music/ep1/trow.mp3","music/ep1/fresh_air.mp3", "music/ep1/time_goes_by.mp3", "music/ep1/this_silence.mp3", "music/ep2/acoustic.mp3" ,"music/ep1/dont_count_on_me.mp3", "music/ep1/emptyv.mp3", "music/ep1/they_say.mp3", "music/ep1/unknown_power.mp3", "music/ep1/your_smile.mp3", "music/ep2/by_your_side.mp3","music/ep2/wings.mp3", "music/ep2/freedom.mp3", "music/ep2/journey_of_hope.mp3", "music/ep2/relaxing_ballad.mp3", "music/ep2/winter.mp3", "music/ep2/rockin_riff.mp3", "music/ep2/simple_ballad.mp3", "music/ep2/jingle.mp3", "music/ep2/feel_bad.mp3", "music/ep3/get_back.mp3", "music/ep3/dc_love_go_go.mp3", "music/ep3/sunny_acoustic_rock.mp3", "music/ep3/lets_begin.mp3", "music/ep3/chill.mp3") )
            renpy.music.queue(randomswamp, channel="music", loop=False, fadein=0, tight=True)
        elif loopFightMusic:
            randomswamp = renpy.random.choice( ("music/ep1/anachronist.mp3","music/ep1/energetic.mp3","music/ep1/credits.mp3","music/ep1/food_chain.mp3","music/ep1/my_heart.mp3","music/patched/track_previous.mp3", "music/ep1/time_goes_by.mp3", "music/ep1/this_silence.mp3", "music/ep1/dont_count_on_me.mp3", "music/ep1/emptyv.mp3", "music/ep2/metal.mp3") )
            renpy.music.queue(randomswamp, channel="music", loop=False, fadein=0, tight=True)
        elif loopMansionMusic:
            randomswamp = renpy.random.choice( ("music/ep5/licensed_music/track4.mp3", "music/ep2/freedom.mp3","music/ep2/marty.mp3", "music/ep5/licensed_music/track3.mp3") )
            renpy.music.queue(randomswamp, channel="music", loop=False, fadein=0, tight=True)
        elif loopMorningMusic:
            randomswamp = renpy.random.choice( ("music/ep5/licensed_music/track5.mp3","music/ep5/licensed_music/track7.mp3","music/ep5/licensed_music/track11.mp3","music/ep5/licensed_music/track14.mp3","music/ep5/licensed_music/track17.mp3") )
            renpy.music.queue(randomswamp, channel="music", loop=False, fadein=0, tight=True)
    renpy.music.set_queue_empty_callback(queueChanCallback, channel='music')
    def skipSongFunc():
        renpy.music.stop('music')


init -1 python:
    if getattr(renpy.display.get_info(), 'oldmenu', None) is None:
        renpy.display.get_info().oldmenu = renpy.exports.menu

    def menu_override(items, set_expr, args, kwargs, item_arguments):
        items = [ (renpy.exports.substitute(label) + (" (disabled)" if not renpy.python.py_eval(condition) else ""), "True", value)
                  for label, condition, value in items ]
        
        return renpy.display.get_info().oldmenu(items, set_expr)
    renpy.exports.menu = menu_override
define config.image_cache_size_mb = 300
label start:
    default badik_chapter = "1"
    default dtype = 0
    default dik = 0
    default tmpdik = 0
    default majordik = 0
    default majorchick = 0
    default dpenalty = 0
    default cpenalty = 0
    default tmpParty = False
    default tmpLibrary = False
    default tmpMusic = False

    default name = ""
    default money = 0
    default failedEnglish = 0
    default failedMath = 0
    default failedGender = 0
    default maxedEnglish = 0
    default maxedMath = 0
    default maxedGender = 0
    default nerdNotes = False
    default tutorials = True

    default RPnerds = 0
    default RPjocks = 0
    default RPpreps = 0
    default RPdiks = 0

    default RPhot = 0

    default RPmaya = 0
    default RPjosy = 0
    default RPsage = 0
    default RPisabella = 0
    default RPjill = 0
    default RPderek = 0
    default josyScore = 0
    default mayaScore = 0
    default sageScore = 0
    default isabellaScore = 0
    default jillScore = 0

    default currentEpisode = 1
    default vault_ep1 = False
    default vault_ep5 = False
    default safe_new_renders = True
    default notifications = True
    default brawlerStoryFight = ""
    default brawlerStoryFightLabel = ""
    default episodeIsEnding = False
    default totalChickChoices = 0
    default totalDikChoices = 0

    default stevePainting = 0
    default acceptedMoneyFromDad = False
    default ep1_josy_chat1_state = 0
    default intervenedChad = False
    default introducedSage = False
    default assman = False
    default preferredmilf = 0
    default ep1_dad_college = False
    default ep1_dad_women = False
    default ep1_showered = False
    default ep1_troy_talk = False
    default ep1_studied_d1 = False
    default ep1_called_josy = False
    default ep1_played_guitar = False
    default ep1_fr_talked_to_derek = False
    default ep1_fr_quinn = False
    default ep1_blank_on_name = False
    default ep1_bought_student_soda = False
    default ep1_insulted_cafeteria_worker = False
    default ep1_lewd_camila_quinn = False
    default ep1_played_along = False
    default ep1_kissed_maya = False
    default ep1_jade_pleased = False
    default ep1_beat_up_troy_won = False
    default ep1_maya_attracted = False
    default ep1_maya_question_indoors = False
    default ep1_maya_question_blanket = False
    default ep1_maya_question_bath = False
    default ep1_maya_question_party = False
    default ep1_maya_question_money = False
    default ep1_dik_end = False
    default ep1_josy_prefer_beer = False
    default ep1_josy_prefer_wine = False
    default ep1_josy_prefer_flowers = False

    default ep1_beat_up_troy = False
    default ep1_accepted_quinn_offer = False

    default lewd_scene_selection_hover = False
    default lewd_pussy_available = False
    default lewd_ass_available = False
    default lewd_tits_available = False
    default lewd_lips_available = False
    default lewd_hand_available = False
    default lewd_fingers_available = False
    default lewd_jade_phase = 0
    default lewd_cathy_phase = 0
    default lewd_riona_phase = 0
    default lewd_camila_phase = 0
    default lewd_quinn_phase = 0
    default lewd_sage_phase = 0
    default lewd_jill_phase = 0
    default lewd_maya_phase = 0
    default lewd_josy_phase = 0
    default lewd_isabella_phase = 0
    default current_lewd_cum_label = ""
    default current_lewd_pussy_label = ""
    default current_lewd_ass_label = ""
    default current_lewd_tits_label = ""
    default current_lewd_lips_label = ""
    default current_lewd_hand_label = ""
    default current_lewd_fingers_label = ""

    default freeRoamID = 1
    default firstTimeFreeRoam = True
    default firstTimeShower = True
    default firstTimeFreeRoamMCDormEp1 = True
    default ep1_fr_dad = False
    default ep1_first_time_closet = True
    default ep1_first_time_shower = True
    default ep1_hallway_state = 0
    default firstTimeBathroom = True
    default ep1_saw_glory_hole = False
    default ep1_maya_talk = False
    default found_money = False
    default ep1_raid_quinn_room = False

    default seen_josy_pic = False
    default seen_derek_pic = False
    default seen_sage_pic = False
    default seen_isabella_pic = False
    default seen_jill_pic = False
    default seen_maya_pic = False
    default seen_quinn_pic = False
    default seen_magnar_pic = False
    default seen_dad_pic = False
    default phone_call_enabled = False
    default phone_call_josy = "NONE"
    default phone_call_dad = "NONE"
    default phone_call_maya = "NONE"
    default phone_call_sage = "NONE"
    default phone_call_jill = "NONE"
    default phone_call_isabella = "NONE"
    default phone_call_derek = "NONE"
    default phone_call_magnar = "NONE"
    default phone_call_quinn = "NONE"
    default phone_bg = 0

    default phone_chat_josy = 0
    default phone_chat_dad = 0
    default phone_chat_maya = 0
    default phone_chat_jill = 0
    default phone_chat_sage = 0
    default phone_chat_isabella = 0
    default phone_chat_derek = 0
    default phone_chat_magnar = 0
    default phone_chat_quinn = 0

    default viewing_image = False
    default phone_clear_jump_label = ""


    default safe_digit_1 = 0
    default safe_digit_2 = 0
    default safe_digit_3 = 0
    default safe_digit_4 = 0
    default studied = False
    default english_cheat = False
    default minigames = True
    default phone_label_offset = 0.845
    default englishPresented = False
    default genderPresented = False
    default passedEnglish = 0
    default passedMath = 0
    default passedGender = 0
    default mathTestScore = 0
    default englishTestScore = 0
    default bonusPercentageEnglish = 0
    default bonusPercentageMath = 0
    default bonusPercentageGender = 0

    default afterMagnarShopLabel = ""
    default talkMagnarShopLabel = ""
    default listenMagnarShopLabel = ""
    default afterDerekShopLabel = ""
    default talkDerekShopLabel = ""
    default listenDerekShopLabel = ""
    default afterQuinnShopLabel = ""
    default talkQuinnShopLabel = ""
    default listenQuinnShopLabel = ""
    default firstTimeGloryHole = True
    default quinn_shop_freebie = False
    default quinn_shop_spicy_lvl = 0
    default quinn_shop_japanese_lvl = 0
    default quinn_shop_special_lvl = 0
    default quinn_shop_special_available = False
    default englishBoost = 0
    default mathBoost = 0
    default genderBoost = 0
    default englishCheatBoost = 0
    default mathCheatBoost = 0
    default genderCheatBoost = 0


    default bios_anthony = False
    default bios_camila = False
    default bios_cathy = False
    default bios_chad = False
    default bios_dawe = False
    default bios_derek = False
    default bios_isabella = False
    default bios_jacob = False
    default bios_jade = False
    default bios_jill = False
    default bios_magnar = False
    default bios_maya = False
    default bios_quinn = False
    default bios_riona = False
    default bios_rusty = False
    default bios_sage = False
    default bios_tommy = False
    default bios_troy = False
    default bios_tybalt = False
    default bios_burke = False

    default bios_arieth = False
    default bios_ashley = False
    default bios_elena = False
    default bios_heather = False
    default bios_jamie = False
    default bios_johnboy = False
    default bios_leon = False
    default bios_lily = False
    default bios_melanie = False
    default bios_mona = False
    default bios_nick = False
    default bios_ron = False
    default bios_sally = False
    default bios_sarah = False
    default bios_zoey = False

    default bios_txt_arieth = "That's Dawe's girlfriend, Arieth. She's a HOT sorority sister and seems loose."
    default bios_txt_ashley = "Ashley's a freshman, too. She's in my classes. Derek talks to her a lot."
    default bios_txt_elena = "Elena likes to party without clothes with her boyfriend, John Boy. She's a HOT sorority sister."
    default bios_txt_heather = "Heather is Tommy's girlfriend. She's in the HOT sorority."
    default bios_txt_jamie = "Jamie is a DIK and Leon was his maggot brother. They tend to stick together."
    default bios_txt_johnboy = "John Boy is a DIK and was Jacob's maggot brother. He likes to party without clothes with his HOT girlfriend, Elena."
    default bios_txt_leon = "Leon is a DIK and Jamie was his maggot brother. They tend to stick together."
    default bios_txt_lily = "Lily is a freshman who also works at The Pink Rose. The DIKs all seem to like her very much."
    default bios_txt_melanie = "Melanie is a HOT sorority sister. She's best friends with Sarah."
    default bios_txt_mona = "Mona is a freshman who is pledging the HOTs."
    default bios_txt_nick = "Nick the DIK. A mellow and nice dude."
    default bios_txt_ron = "Ron is a tri-beta and a bit of a cunt..."
    default bios_txt_sally = "I think Sally might be Magnar's girlfriend. She sure seems to like him a lot."
    default bios_txt_sarah = "Sarah is a HOT sorority sister. She's best friends with Melanie."
    default bios_txt_zoey = "Zoey... My first best friend who turned into my girlfriend briefly before leaving for San Diego to become a surfer."

    default bios_history_arieth = ""
    default bios_history_ashley = ""
    default bios_history_elena = ""
    default bios_history_heather = ""
    default bios_history_jamie = ""
    default bios_history_johnboy = ""
    default bios_history_leon = ""
    default bios_history_lily = ""
    default bios_history_melanie = ""
    default bios_history_mona = ""
    default bios_history_nick = ""
    default bios_history_ron = ""
    default bios_history_sally = ""
    default bios_history_sarah = ""
    default bios_history_zoey = ""

    default bios_name_arieth = True
    default bios_name_ashley = True
    default bios_name_elena = True
    default bios_name_heather = True
    default bios_name_jamie = True
    default bios_name_johnboy = True
    default bios_name_leon = True
    default bios_name_lily = True
    default bios_name_melanie = True
    default bios_name_mona = True
    default bios_name_nick = True
    default bios_name_ron = True
    default bios_name_sally = True
    default bios_name_sarah = True
    default bios_name_zoey = True

    default bios_alex = False
    default bios_bert = False
    default bios_beth = False
    default bios_brandi = False
    default bios_dany = False
    default bios_envy = False
    default bios_eugene = False
    default bios_jimmy = False
    default bios_john = False
    default bios_lynette = True
    default bios_minny = False
    default bios_rose = False
    default bios_stanley = False
    default bios_wendy = False

    default bios_txt_alex = "A member of the tri-alpha fraternity."
    default bios_txt_bert = "Bert is Derek's roommate and a member of the tri-beta fraternity."
    default bios_txt_beth = "She works in the school cafeteria. I've seen her at DIK parties."
    default bios_txt_brandi = "Brandi works at The Pink Rose as a stripper."
    default bios_txt_dany = "Dany is in my Gender Studies class. She's Jamie's girlfriend."
    default bios_txt_envy = "Envy works at The Pink Rose as a stripper."
    default bios_txt_eugene = "Eugene is a member of the tri-beta fraternity."
    default bios_txt_jimmy = "A member of the tri-alpha fraternity."
    default bios_txt_john = "A member of the tri-alpha fraternity."
    default bios_txt_lynette = "My mom passed away as I was born. I only got to know her through my dad."
    default bios_txt_minny = "Minny is in my Gender Studies class. She seems to be a hardcore feminist."
    default bios_txt_rose = "Rose works at The Pink Rose as a stripper."
    default bios_txt_stanley = "Stanley works as a bouncer at The Pink Rose."
    default bios_txt_wendy = "Wendy is in my Gender Studies class. She seems to be a hardcore feminist."

    default bios_history_alex = ""
    default bios_history_bert = ""
    default bios_history_beth = ""
    default bios_history_brandi = ""
    default bios_history_dany = ""
    default bios_history_envy = ""
    default bios_history_eugene = ""
    default bios_history_jimmy = ""
    default bios_history_john = ""
    default bios_history_lynette = ""
    default bios_history_minny = ""
    default bios_history_rose = ""
    default bios_history_stanley = "Stanley seems to help Rusty set up parties at the club.\n\n"
    default bios_history_wendy = ""

    default bios_name_alex = True
    default bios_name_bert = True
    default bios_name_beth = True
    default bios_name_brandi = True
    default bios_name_dany = True
    default bios_name_envy = True
    default bios_name_eugene = True
    default bios_name_jimmy = True
    default bios_name_john = True
    default bios_name_lynette = True
    default bios_name_minny = True
    default bios_name_rose = True
    default bios_name_stanley = True
    default bios_name_wendy = True

    default bios_caleb = False
    default bios_gordon = False
    default bios_christian = False
    default bios_lucas = False
    default bios_rich = False
    default bios_trent = False

    default bios_txt_caleb = "A big and scary dude pledging the tri-alpha fraternity."
    default bios_txt_gordon = "An Alpha Nu Omega pledge."
    default bios_txt_christian = "An Alpha Nu Omega pledge."
    default bios_txt_lucas = "An Alpha Nu Omega pledge."
    default bios_txt_rich = "The vice president of the Alpha Nu Omega fraternity."
    default bios_txt_trent = "A member of the Alpha Nu Omega fraternity."

    default bios_history_caleb = ""
    default bios_history_gordon = ""
    default bios_history_christian = ""
    default bios_history_lucas = ""
    default bios_history_rich = ""
    default bios_history_trent = ""

    default bios_name_caleb = True
    default bios_name_gordon = True
    default bios_name_christian = True
    default bios_name_lucas = True
    default bios_name_rich = True
    default bios_name_trent = True

    default bios_txt_mc = "That's me. A regular 18 year old with martial arts and music as favorite hobbies. Growing up I didn't get a lot of attention from girls; mostly because of being bullied for being poor. But lately things have been looking good for me."
    default bios_txt_dad = "I love my dad. He's always been there for me. He works in construction, but struggles to make ends meet due to some legal issues in his past."
    default bios_txt_josy = "Josy. It didn't take long until I had a crush on her. She has a warm personality and a way to always capture the room she's in."
    default bios_txt_steve = "Steve... The son of the boss at my summer job. He has this arrogant attitude and it's obvious that he thinks he's better than everyone else because his dad owns a minimart. Come on...you're not that rich, Steve!"
    default bios_txt_anthony = "A dimwitted jock. Not really a rare breed around here, it seems."
    default bios_txt_camila = "Camila. She's also a freshman. Question is if she's a submissive person in general or if there's something else causing her to play along?"
    default bios_txt_cathy = "Cathy is my English and Math teacher. I would describe her as harsh but fair."
    default bios_txt_chad = "The president of the tri-alphas and Sage's boyfriend. I'd rather stay away from him, but I may already be on his radar."
    default bios_txt_dawe = "Dawe...what a cunt. I don't know a lot about him, but he seems no different from any other jock, in my eyes."
    default bios_txt_derek = "This guy doesn't seem to take much seriously. He appears to be a douchebag, but there's strangely something with him that I want to like. I can't put my finger on it."
    default bios_txt_isabella = "A librarian at the school library. She's gotten the nickname \"The Ice Queen\" from students. It's a mean nickname, but I kind of get why. She has this mean stare...it scares me."
    default bios_txt_jacob = "A DIK brother. Nothing special about him."
    default bios_txt_jade = "Looking at Jade, I would never have guessed that she was a feminist teacher...sorry...I meant teacher in gender studies. Even if her class blows, she seems kind of cool."
    default bios_txt_jill = "Jill. Beautiful, nice and rich. She seems to have it all... There's got to be something wrong with her...right?"
    default bios_txt_magnar = "Magnar, a really nerdy dude with a weird Scandinavian name. He can hook me up with study materials for classes. Having such a friend might actually pay off."
    default bios_txt_maya = "Maya's a cute and nice girl. She seems to be pretty down to earth and mellow."
    default bios_txt_quinn = "Hm...there's nothing that says soft or sweet about Quinn. Her looks are sexy as hell, but she looks like she has quite the temper."
    default bios_txt_riona = "A sexy girl that dresses very slut-...erm...loosely. She doesn't look to be that happy."
    default bios_txt_rusty = "The president of the DIKs. He seems to be pretty cool, definitely a nicer person than his vice president, Tommy."
    default bios_txt_sage = "A fiery redhead with an attitude. Sage is the president of HOT and girlfriend to Chad, the president of the tri-alphas. She seems sure that Chad's cheating on her with someone."
    default bios_txt_tommy = "The vice president of the DIKs. A total douche, at least to non-DIKs."
    default bios_txt_troy = "The asshole I share a dorm room with. I don't know why he assumes attack position immediately. There seems to be no way for me to convince him I'm not a bad guy."
    default bios_txt_tybalt = "The president of the preps fraternity, Alpha Nu Omega. Appears to be filthy rich."
    default bios_txt_burke = "Professor Stephen Burke. Professor of economics and teacher of several business classes. He's sharply dressed and charming."

    default bios_history_mc = ""
    default bios_history_dad = ""
    default bios_history_burke = ""
    default bios_history_josy = ""
    default bios_history_steve = ""
    default bios_history_anthony = ""
    default bios_history_camila = ""
    default bios_history_cathy = ""
    default bios_history_chad = ""
    default bios_history_dawe = ""
    default bios_history_derek = ""
    default bios_history_isabella = ""
    default bios_history_jacob = ""
    default bios_history_jade = ""
    default bios_history_jill = ""
    default bios_history_magnar = ""
    default bios_history_maya = ""
    default bios_history_quinn = ""
    default bios_history_riona = ""
    default bios_history_rusty = ""
    default bios_history_sage = ""
    default bios_history_tommy = ""
    default bios_history_troy = ""
    default bios_history_tybalt = ""

    default bios_name_mc = True
    default bios_name_dad = True
    default bios_name_burke = True
    default bios_name_josy = True
    default bios_name_steve = True
    default bios_name_anthony = True
    default bios_name_camila = True
    default bios_name_cathy = True
    default bios_name_chad = True
    default bios_name_dawe = True
    default bios_name_derek = True
    default bios_name_isabella = True
    default bios_name_jacob = True
    default bios_name_jade = True
    default bios_name_jill = True
    default bios_name_magnar = True
    default bios_name_maya = True
    default bios_name_quinn = True
    default bios_name_riona = True
    default bios_name_rusty = True
    default bios_name_sage = True
    default bios_name_tommy = True
    default bios_name_troy = True
    default bios_name_tybalt = True

    default current_bios_txt = ""
    default current_bios_history = ""
    default current_bios_name = ""
    default current_bios_avatar = ""

    default current_task = "None"

    default number_derek = False
    default number_isabella = False
    default number_maya = False
    default number_sage = False
    default number_jill = False
    default number_quinn = False
    default number_magnar = False

    default pet_reset = ""
    default josy = "Josy"
    default maya = "Maya"
    default sage = "Sage"
    default isabella = "Isabella"
    default jill = "Jill"
    default quinn = "Quinn"
    default riona = "Riona"
    default jade = "Jade"
    default cathy = "Cathy"
    default camila = "Camila"
    default gameBoost = 0
    default phone_chat_josy_new = False
    default phone_chat_dad_new = False
    default phone_chat_maya_new = False
    default phone_chat_isabella_new = False
    default phone_chat_sage_new = False
    default phone_chat_jill_new = False
    default phone_chat_quinn_new = False
    default phone_chat_magnar_new = False
    default phone_chat_derek_new = False

    default game_money_available = True
    default brawler_render_available = True
    default brawler_money_available = True
    default brawler_skillpoint_available = True
    default currentFreeRoamLabel = ""
    default currentSexLabel = ""
    default music_new_songs = True
    default chat_new_bg = True
    default chat_new_bios = True
    default chat_new_rewards = False
    default chat_new_tasks = True
    default chat_new_names = True
    default chat_new_stats = True
    default chat_ySize = 0.068
    default new_cluck = False
    default rooster_app_enabled = False
    default roosterState = "ep3_1"

    default bonusPointsSports = 1
    default bonusPointsSportsDerek = 0
    default sports_heal_skill = False
    default sports_roundhouse_skill = False
    default sports_store_sp1 = False
    default sports_store_sp2 = False
    default sports_store_sp3 = False
    default sports_pow = 0
    default sports_dex = 0
    default sports_hp = 0
    default sports_mov = 0
    default sports_tutorial = False
    default sports_opponent_idx = 0
    default sports_counter_skill = False
    default brawler_hard_mode = False
    default brawler_question = False
    default brawler_difficulty = 0

    default sports_opponents = ["Nerd", "#c700dd", "sports_avatar_nerd", "Prep", "#87fa5a", "sports_avatar_prep", "Jock", "#23b4fc", "sports_avatar_jock", "Chad", "#23b4fc", "sports_avatar_chad", "Troy", "#ff0000", "sports_avatar_troy"]
    default sports_opponents_tiles = ["sports_nerd_tile", "sports_nerd_tile_attackable","sports_prep_tile", "sports_prep_tile_attackable", "sports_jock_tile","sports_jock_tile_attackable", "sports_chad_tile", "sports_chad_tile_attackable", "sports_troy_tile", "sports_troy_tile_attackable"]
    default sports_opponents_stats = [1, 1, 3, 1, 2, 2, 2, 2, 4, 4, 2, 2, 4, 4, 4, 4, 1, 1, 2, 3, 3, 3, 2, 2]
    default sports_skillpointsleft = 0

    default cpu_name = sports_opponents[sports_opponent_idx*3]
    default cpu_color = sports_opponents[sports_opponent_idx*3+1]
    default cpu_avatar = sports_opponents[sports_opponent_idx*3+2]
    default sports_cpu_hp = sports_opponents_stats[sports_opponent_idx*4]
    default sports_cpu_pow = sports_opponents_stats[sports_opponent_idx*4 + 1]
    default sports_cpu_dex = sports_opponents_stats[sports_opponent_idx*4 + 2]
    default sports_cpu_mov = sports_opponents_stats[sports_opponent_idx*4 + 3]
    default cpu_hp_state = 1
    default sports_pc_hp = 90 + 10 * sports_hp
    default sports_rounded_player_hp = sports_pc_hp
    default sports_rounded_cpu_hp = sports_cpu_hp
    default sports_pow_multi = [0.0, 1.0, 1.25 ,1.5, 2.0]
    default sports_victory = False

    default bg_ok_choice = False
    default menuGalleryOpen = False
    default unlockedScenes = 0
    default affinity = "NEUTRAL"
    default swyper_app_enabled = False
    default newSwypeMsgNicole = 0
    default newSwypeMsgCatrin = 0
    default newSwypeMsgCathy = 0
    default newSwypeMsgEllie = 0
    default newSwypeMsgArieth = 0
    default newSwypeMsgNora = 0

    default chat_reply = ""
    default chat_reply_array = ["","",""]
    default drunk_reply_array = ["","",""]
    default chat_next_state_array = ["","",""]
    default chat_mc_avatar = "swyper_chat_mc1_avatar"

    default chat_dad_state = "1"
    default chat_derek_state = "1"
    default chat_isabella_state = "1"
    default chat_jill_state = "1"
    default chat_josy_state = "1"
    default chat_magnar_state = "1"
    default chat_maya_state = "1"
    default chat_quinn_state = "1"
    default chat_sage_state = "1"

    default chat_dad_history = []
    default chat_derek_history = []
    default chat_isabella_history = []
    default chat_jill_history = []
    default chat_josy_history = []
    default chat_magnar_history = []
    default chat_maya_history = []
    default chat_quinn_history = []
    default chat_sage_history = []

    default chat_dad_history_is_them = []
    default chat_derek_history_is_them = []
    default chat_isabella_history_is_them = []
    default chat_jill_history_is_them = []
    default chat_josy_history_is_them = []
    default chat_magnar_history_is_them = []
    default chat_maya_history_is_them = []
    default chat_quinn_history_is_them = []
    default chat_sage_history_is_them = []

    default newMessageIntJosy = 0
    default newMessageIntSage = 0
    default newMessageIntDerek = 0
    default newMessageIntDad = 0
    default newMessageIntIsabella = 0
    default newMessageIntJill = 0
    default newMessageIntMagnar = 0
    default newMessageIntQuinn = 0
    default newMessageIntMaya = 0


    default roosterPostsArray = []
    default roosterLikesArray = []
    default roosterLikedArray = []
    default roosterAvatarArray = []
    default roosterNickArray = []
    default roosterTextArray = []
    default roosterPhotoArray = []
    default roosterCommentSectionArray = []
    default roosterCurrentIdx = 0

    default mc_avatar = "rooster_mini_mc1"
    default bios_avatar_mc = "bios_avatar_mc1"
    default mbios_mc = "mbios_mc1"
    default mbios_mc_new_hover = "mbios_mc1_new_hover"
    default mbios_mc_new = "mbios_mc1_new"
    default mbios_mc_hover = "mbios_mc1_hover"
    default roosterNickMCCustom = "Tremolo"
    default roosterNickMC = "[name]@[roosterNickMCCustom]"
    default swyperNickMCCustom = "Tremolo"
    default tmpname = ""
    default tmpnameRooster = "Tremolo"
    default tmpnameSwyper = "Tremolo"
    default roosterNickAlex = "Alex@OnePunchAlex"
    default roosterNickAnthony = "Anthony@BigA"
    default roosterNickArieth = "Arieth@AriethPassword1234"
    default roosterNickAshley = "Ashley@JustAsh"
    default roosterNickBert = "Bert@Thalidomide"
    default roosterNickBeth = "Beth@MoreThanJustAWaitress"
    default roosterNickBrandi = "Brandi@MochaLatte"
    default roosterNickBurke = "Burke@ProfessorStephenBurke"
    default roosterNickCaleb = "Caleb@FeelThePump"
    default roosterNickCamila = "Camila@Cammy"
    default roosterNickCathy = "Cathy@CathyJones79"
    default roosterNickChad = "Chad@MadLadChad"
    default roosterNickChristian = "Christian@PlayOnPlayer"
    default roosterNickDany = "Dany@BunnyHop"
    default roosterNickDawe = "Dawe@BigDickDawe"
    default roosterNickDerek = "Derek@BigBootyLover"
    default roosterNickDik = "DIKsOfficial@DIKsOfficial"
    default roosterNickElena = "Elena@CuteButt"
    default roosterNickEnvy = "Nicole@TwoToTango"
    default roosterNickEugene = "Eugene@MrDynamite"
    default roosterNickGordon = "Gordon@Diamonds"
    default roosterNickHeather = "Heather@HOTHeather"
    default roosterNickIsabella = "Isabella@IsabellaRoberts"
    default roosterNickJacob = "Jacob@DIKJacob"
    default roosterNickJade = "Jade@DrJadeBurke"
    default roosterNickJamie = "Jamie@DIKJam"
    default roosterNickJill = "Jill@EbonyAndIvory"
    default roosterNickJimmy = "Jimmy@Chevy69"
    default roosterNickJohn = "John@MilkMan"
    default roosterNickJohnBoy = "JohnBoy@DIKJB"
    default roosterNickJosy = "Josy@MsSunshine"
    default roosterNickLeon = "Leon@DIKLeon"
    default roosterNickLily = "Lily@LikeTheFlower"
    default roosterNickLucas = "Lucas@TheThird"
    default roosterNickMagnar = "Magnar@SirMagnar"
    default roosterNickMaya = "Maya@MayaTheMoviebuff"
    default roosterNickMelanie = "Melanie@CaraMel"
    default roosterNickMinny = "Minny@FemGirlPower"
    default roosterNickMona = "Mona@MonaLisa"
    default roosterNickNick = "Nick@DIKNick"
    default roosterNickOliver = "Oliver@Buttons"
    default roosterNickQuinn = "Quinn@QuinnOfHearts"
    default roosterNickRich = "Rich@IAmRich"
    default roosterNickRiona = "Riona@HOTRiona"
    default roosterNickRon = "Ron@MegatRon"
    default roosterNickRose = "Rose@GinAndTonic"
    default roosterNickRusty = "Rusty@DIKPresidentRusty"
    default roosterNickSage = "Sage@HOTPresidentSage"
    default roosterNickSally = "Sally@Sallycylic"
    default roosterNickSarah = "Sarah@HOTSarah"
    default roosterNickTommy = "Tommy@DIKTommyTheDestroyer"
    default roosterNickTrent = "Trent@LordTrent"
    default roosterNickTroy = "Troy@FingerRoll"
    default roosterNickTybalt = "Tybalt@PresidentTybaltBurke"
    default roosterNickWendy = "Wendy@TheRealestWoman"
    default roosterNickAlt = "Tyballs@PresidentTyballs"

    default rooster_jump_label = ""
    default rooster_reply = ""

    default roosterHistory_text_JillEp3 = []
    default roosterHistory_text_RustyEp3 = []
    default roosterHistory_text_MayaEp3 = []
    default roosterHistory_text_QuinnEp3 = []
    default roosterHistory_text_CathyEp3 = []
    default roosterHistory_text_RionaEp3 = []
    default roosterHistory_text_SageEp3 = []
    default roosterHistory_text_DaweEp4 = []
    default roosterHistory_text_JillEp4 = []
    default roosterHistory_text_SageEp4 = []
    default roosterHistory_text_DerekEp4 = []
    default roosterHistory_text_IsabellaEp4 = []
    default roosterHistory_text_Sage2Ep4 = []
    default roosterHistory_text_TybaltEp4 = []
    default roosterHistory_text_CamilaEp4 = []
    default roosterHistory_text_CathyEp4 = []

    default roosterHistory_avatar_JillEp3 = []
    default roosterHistory_avatar_RustyEp3 = []
    default roosterHistory_avatar_MayaEp3 = []
    default roosterHistory_avatar_QuinnEp3 = []
    default roosterHistory_avatar_CathyEp3 = []
    default roosterHistory_avatar_SageEp3 = []
    default roosterHistory_avatar_RionaEp3 = []
    default roosterHistory_avatar_DaweEp4 = []
    default roosterHistory_avatar_JillEp4 = []
    default roosterHistory_avatar_SageEp4 = []
    default roosterHistory_avatar_DerekEp4 = []
    default roosterHistory_avatar_IsabellaEp4 = []
    default roosterHistory_avatar_Sage2Ep4 = []
    default roosterHistory_avatar_TybaltEp4 = []
    default roosterHistory_avatar_CamilaEp4 = []
    default roosterHistory_avatar_CathyEp4 = []

    default roosterHistory_nick_JillEp3 = []
    default roosterHistory_nick_RustyEp3 = []
    default roosterHistory_nick_MayaEp3 = []
    default roosterHistory_nick_RionaEp3 = []
    default roosterHistory_nick_QuinnEp3 = []
    default roosterHistory_nick_CathyEp3 = []
    default roosterHistory_nick_SageEp3 = []
    default roosterHistory_nick_DaweEp4 = []
    default roosterHistory_nick_JillEp4 = []
    default roosterHistory_nick_SageEp4 = []
    default roosterHistory_nick_DerekEp4 = []
    default roosterHistory_nick_IsabellaEp4 = []
    default roosterHistory_nick_Sage2Ep4 = []
    default roosterHistory_nick_TybaltEp4 = []
    default roosterHistory_nick_CamilaEp4 = []
    default roosterHistory_nick_CathyEp4 = []

    default roosterHistory_likes_JillEp3 = []
    default roosterHistory_likes_RustyEp3 = []
    default roosterHistory_likes_MayaEp3 = []
    default roosterHistory_likes_RionaEp3 = []
    default roosterHistory_likes_QuinnEp3 = []
    default roosterHistory_likes_CathyEp3 = []
    default roosterHistory_likes_SageEp3 = []
    default roosterHistory_likes_DaweEp4 = []
    default roosterHistory_likes_JillEp4 = []
    default roosterHistory_likes_SageEp4 = []
    default roosterHistory_likes_DerekEp4 = []
    default roosterHistory_likes_IsabellaEp4 = []
    default roosterHistory_likes_Sage2Ep4 = []
    default roosterHistory_likes_TybaltEp4 = []
    default roosterHistory_likes_CamilaEp4 = []
    default roosterHistory_likes_CathyEp4 = []

    default roosterHistory_liked_JillEp3 = []
    default roosterHistory_liked_RustyEp3 = []
    default roosterHistory_liked_MayaEp3 = []
    default roosterHistory_liked_RionaEp3 = []
    default roosterHistory_liked_QuinnEp3 = []
    default roosterHistory_liked_CathyEp3 = []
    default roosterHistory_liked_SageEp3 = []
    default roosterHistory_liked_DaweEp4 = []
    default roosterHistory_liked_JillEp4 = []
    default roosterHistory_liked_SageEp4 = []
    default roosterHistory_liked_DerekEp4 = []
    default roosterHistory_liked_IsabellaEp4 = []
    default roosterHistory_liked_Sage2Ep4 = []
    default roosterHistory_liked_TybaltEp4 = []
    default roosterHistory_liked_CamilaEp4 = []
    default roosterHistory_liked_CathyEp4 = []

    default roosterChoices_JillEp3 = []
    default roosterChoices_RustyEp3 = []
    default roosterChoices_MayaEp3 = []
    default roosterChoices_RionaEp3 = []
    default roosterChoices_QuinnEp3 = []
    default roosterChoices_CathyEp3 = []
    default roosterChoices_SageEp3 = []
    default roosterChoices_DaweEp4 = []
    default roosterChoices_JillEp4 = []
    default roosterChoices_SageEp4 = []
    default roosterChoices_DerekEp4 = []
    default roosterChoices_IsabellaEp4 = []
    default roosterChoices_Sage2Ep4 = []
    default roosterChoices_TybaltEp4 = []
    default roosterChoices_CamilaEp4 = []
    default roosterChoices_CathyEp4 = []

    default ep4_cluckDaweState = 0
    default ep4_cluckSage2State = 0
    default ep4_cluckJillState = 0
    default rooster_liked_tybalt_post_ep4 = False
    default rooster_liked_tybalt2_post_ep4 = False
    default new_rooster_int = 0
    default state = "df"
    default e_time = 0
    default c_time = 0
    default t_time = 0
    default maxedMath_s2 = 0
    default maxedEnglish_s2 = 0
    default maxedGender_s2 = 0
    default map_fast_travel_enabled = True
    default map_system_list = []
    default permanent_affinity = False
    default phone_opened = False
    default wallet_lvl = 0
    default mphone_current_input = ""
    default dollar = 1
    default mc_camila = ""
    default mc_cathy = ""
    default mc_isabella = ""
    default mc_jade = ""
    default mc_jill = ""
    default mc_josy = ""
    default mc_maya = ""
    default mc_quinn = ""
    default mc_riona = ""
    default mc_sage = ""
    default failedGame = False

    default earnedMoney = 0
    default spentMoney = 0
    default maxedPaths = 0
    $ achievement.register("MAGAZINECOLLECTOR")
    $ achievement.register("ALLSCENES")
    $ achievement.register("NOTSOPOORAFTERALL")
    $ achievement.register("POORAGAIN")
    $ achievement.register("JAILBREAK")
    default steamAchievements = False
    default steamConfig = False
    default nonPatreonConfig = False
    default foundCards = 0
    default foundCards_s2 = 0
    default unlockedScenes_s2 = 0
    default game_is_ending = False
    default randInt = 0
    default guideSuggestedPage = 1
    define max_page_walkthrough = 162
    default guideCurrentPage = 1
    default rewards_renders_list = []
    default tmpBool = False
    default tmpBool2 = False
    default tmpInt = 0
    default tmpInt2 = 0
    default toggled_2d_mode = 1
    default episode_title_name = "The Initiation"
    default laptop_wallpapers = ["default_wallpaper","default_wallpaper1","default_wallpaper2","default_wallpaper3","default_wallpaper4","default_wallpaper5","default_wallpaper6","default_wallpaper7","default_wallpaper8","default_wallpaper9","default_wallpaper10","default_wallpaper11","default_wallpaper12","default_wallpaper13","default_wallpaper14","default_wallpaper15","default_wallpaper16","default_wallpaper17"]
    default currentWallpaperPreview = 0
    default currentWallpaperPage = 0
    default laptop_wallpapers_criteria_met = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    default laptop_wallpapers_unlocked = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    default mphone_bios_chars = []
    default mphone_current_bios_char = 0
    default mphone_bios_sort_by = ["Alphabetical","Girls","Guys","DIKs","HOTs","Jocks","Preps","Nerds","Staff/Teachers"]
    default mphone_bios_sort_by_idx = 0
    default mphone_triple_tile_is_playing = False

    default triple_tile_new_highscore = 0
    default triple_tile_score = 0
    default triple_tile_turn = 0
    default triple_turn_to_beat = 15
    default triple_card_number_of_cards = 6
    default triple_tile_chosen_tile = -1
    default triple_tile_game_over = False
    default triple_tile_show_numbers = False
    default triple_tile_easy_mode = False
    default triple_tile_new_high_score = 0
    default triple_tile_hovered_tile = [-1,-1]
    default triple_tile_hs_checked = False


    default triple_tile_spr = [[False,False,False],[False,False,False],[False,False,False]]
    default triple_tile_sets = [[0,0,0],[0,0,0],[0,0,0]]
    default triple_tile_grid = [[[0,0,0],[0,0,0],[0,0,0]], [[0,0,0],[0,0,0],[0,0,0]], [[0,0,0],[0,0,0],[0,0,0]]]
    default triple_tile_grid_spr = [[[0,0,0],[0,0,0],[0,0,0]], [[0,0,0],[0,0,0],[0,0,0]], [[0,0,0],[0,0,0],[0,0,0]]]

    jump ep1_start_label
init:
    $ config.debug_image_cache = True

    if renpy.loadable("season2/scripts/update5.rpyc"):
        $ spr_mm_quinn_s2 = ["gui/main_menu_sprites/season2/spr_quinn_alley.jpg", 1.07, "gui/main_menu_sprites/season2/spr_quinn.png", 1.18,"gui/main_menu_sprites/season2/spr_quinn_rain.png", 1.5]
        $ spr_mm_jocks_s2 = ["spr_jock_bg", 1.07, "spr_jock_ant", 1.15, "spr_jock_dawe", 1.28]
        $ spr_mm_derek_s2 = ["gui/main_menu_sprites/season2/spr_derek_bg.jpg", 1.02, "gui/main_menu_sprites/season2/spr_derek_wendy.png", 1.08,"gui/main_menu_sprites/season2/spr_derek_derek.png", 1.12]
        $ spr_mm_jb_s2 = ["gui/main_menu_sprites/season2/spr_jb_bg.jpg", 1.02, "gui/main_menu_sprites/season2/spr_jb_jill.png", 1.08,"gui/main_menu_sprites/season2/spr_jb_bella.png", 1.12]
        $ spr_mm_rc_s2 = ["gui/main_menu_sprites/season2/spr_rc_bg.jpg", 1.02, "gui/main_menu_sprites/season2/spr_rc_trees.png", 1.07,"gui/main_menu_sprites/season2/spr_rc_riona.png", 1.12]
        $ spr_mm_hots_s2 = ["gui/main_menu_sprites/season2/spr_hots_bg.jpg", 1.02, "gui/main_menu_sprites/season2/spr_hots_melanie.png", 1.07,"gui/main_menu_sprites/season2/spr_hots_lily.png", 1.12]
        $ spr_mm_sage_s2 = ["gui/main_menu_sprites/season2/spr_sage_bg.jpg", 1.02, "gui/main_menu_sprites/season2/spr_sage_sage.png", 1.07,"gui/main_menu_sprites/season2/spr_sage_steam.png", 1.12]
        $ spr_mm_jm_s2 = ["gui/main_menu_sprites/season2/spr_jm_bg.jpg", 1.02, "gui/main_menu_sprites/season2/spr_jm_jetty.png", 1.07,"gui/main_menu_sprites/season2/spr_jm_josy.png", 1.12]
        $ spr_mm_jade_s2 = ["gui/main_menu_sprites/season2/spr_jade_bg.jpg", 1.02, "gui/main_menu_sprites/season2/empty.png", 1.07,"gui/main_menu_sprites/season2/spr_jade_jade.png", 1.12]
        $ spr_mm_tybalt_s2 = ["gui/main_menu_sprites/season2/spr_tybalt_bg.jpg", 1.02, "gui/main_menu_sprites/season2/spr_tybalt_trent.png", 1.07,"gui/main_menu_sprites/season2/spr_tybalt_tybalt.png", 1.12]
        $ spr_mm_nerds_s2 = ["gui/main_menu_sprites/season2/spr_nerds_bg.jpg", 1.02, "gui/main_menu_sprites/season2/spr_nerds_sally.png", 1.07,"spr_nerds_glowing", 1.12]
        $ spr_mm_mc_s2 = ["gui/main_menu_sprites/season2/spr_mc_bg.jpg", 1.02, "gui/main_menu_sprites/season2/empty.png", 1.07,"gui/main_menu_sprites/season2/spr_mc_mc.png", 1.08]
        $ spr_mm_rose_s2 = ["gui/main_menu_sprites/season2/spr_rose_bg.jpg", 1.02, "gui/main_menu_sprites/season2/empty.png", 1.07,"gui/main_menu_sprites/season2/spr_rose_rose.png", 1.08]
        $ spr_mm_diks_s2 = ["gui/main_menu_sprites/season2/spr_diks_bg.jpg", 1.02, "gui/main_menu_sprites/season2/empty.png", 1.07,"gui/main_menu_sprites/season2/spr_diks_elena.png", 1.08]
        $ spr_mm_diks2_s2 = ["gui/main_menu_sprites/season2/spr_diks2_bg.jpg", 1.02, "gui/main_menu_sprites/season2/empty.png", 1.07,"gui/main_menu_sprites/season2/spr_diks2_vinny.png", 1.09]
        $ spr_mm_arr_s2 = [spr_mm_quinn_s2, spr_mm_jocks_s2, spr_mm_jb_s2, spr_mm_rc_s2, spr_mm_hots_s2, spr_mm_sage_s2, spr_mm_jm_s2, spr_mm_jade_s2, spr_mm_derek_s2, spr_mm_tybalt_s2, spr_mm_nerds_s2, spr_mm_mc_s2, spr_mm_rose_s2, spr_mm_diks_s2, spr_mm_diks2_s2]
        $ renpy.random.shuffle(spr_mm_arr_s2)

    $ spr_mm_sage = ["gui/main_menu_sprites/spr_sage_dorm.jpg",1.03,"gui/main_menu_sprites/spr_sage_lamp.png",1.05,"gui/main_menu_sprites/spr_sage.png",1.1]
    $ spr_mm_jocks = ["gui/main_menu_sprites/spr_jocks.jpg", 1.07, "gui/main_menu_sprites/spr_anthony.png", 1.15,"gui/main_menu_sprites/spr_dawe.png", 1.28]
    $ spr_mm_hots = ["gui/main_menu_sprites/spr_hots.jpg", 1.07, "gui/main_menu_sprites/spr_quinn.png", 1.15,"gui/main_menu_sprites/spr_quinn_lolly.png", 1.28]
    $ spr_mm_maya = ["gui/main_menu_sprites/spr_maya_bed.jpg", 1.07, "gui/main_menu_sprites/spr_maya.png", 1.1,"gui/main_menu_sprites/spr_maya_basket.png", 1.15]
    $ spr_mm_josy = ["gui/main_menu_sprites/spr_forest.jpg", 1.03, "gui/main_menu_sprites/spr_josy_tree.png", 1.04,"gui/main_menu_sprites/spr_josy.png", 1.05]
    $ spr_mm_jill = ["gui/main_menu_sprites/spr_mansion.jpg", 1.03, "gui/main_menu_sprites/spr_jill.png", 1.12, "gui/main_menu_sprites/spr_gates.png", 1.07]
    $ spr_mm_bella = ["gui/main_menu_sprites/spr_bella_home.jpg", 1.05, "gui/main_menu_sprites/spr_bella.png", 1.08, "gui/main_menu_sprites/spr_bella_table.png", 1.3]
    $ spr_mm_tommy = ["gui/main_menu_sprites/spr_tommy_bg.jpg", 1.05, "gui/main_menu_sprites/spr_tommy.png", 1.08,"gui/main_menu_sprites/spr_tommy_coin.png", 1.2]
    $ spr_mm_jade = ["gui/main_menu_sprites/spr_jade_bg.jpg", 1.05, "gui/main_menu_sprites/spr_derek.png", 1.08, "gui/main_menu_sprites/spr_jade.png", 1.1]
    $ spr_mm_magnar = ["gui/main_menu_sprites/spr_magnar_bg.jpg",1.05, "gui/main_menu_sprites/spr_magnar.png", 1.15, "gui/main_menu_sprites/spr_books.png",1.3]
    $ spr_mm_cathy = ["gui/main_menu_sprites/spr_cathy_bg.jpg",1.05, "gui/main_menu_sprites/spr_cathy_main.png", 1.15, "gui/main_menu_sprites/spr_cathy_desk.png",1.3]
    $ spr_mm_hots2 = ["gui/main_menu_sprites/spr_hots_bg.jpg",1.05, "gui/main_menu_sprites/spr_hots_main.png", 1.09, "gui/main_menu_sprites/spr_hots_girls.png",1.2]
    $ spr_mm_rose = ["gui/main_menu_sprites/spr_rose_bg.jpg",1.05, "gui/main_menu_sprites/spr_rose_main.png", 1.08, "gui/main_menu_sprites/spr_rose_girls.png",1.2]
    $ spr_mm_arr = [spr_mm_sage, spr_mm_jocks, spr_mm_hots, spr_mm_maya, spr_mm_josy, spr_mm_jill, spr_mm_bella, spr_mm_tommy, spr_mm_jade, spr_mm_magnar, spr_mm_cathy, spr_mm_rose, spr_mm_hots2]
    $ renpy.random.shuffle(spr_mm_arr)

    $ musicCreditsOpen = False

    $ renpy.music.register_channel("sfx1", "sfx")
    $ renpy.music.register_channel("sfx2", "sfx")
    $ renpy.music.register_channel("music1", "music")
    $ renpy.music.register_channel("jill", "voice")
    $ renpy.music.register_channel("bella", "voice")

    if persistent.current_episode == None:
        $ persistent.current_episode = 1
    if persistent.tutorials == None:
        $ persistent.tutorials = False
    if persistent.pet_app_unlocked == None:
        $ persistent.pet_app_unlocked = False
    if persistent.firstTimePlaying == None:
        $ persistent.firstTimePlaying = True
    if persistent.josy == None:
        $ persistent.josy = "Josy"
    if persistent.maya == None:
        $ persistent.maya = "Maya"
    if persistent.sage == None:
        $ persistent.sage = "Sage"
    if persistent.isabella == None:
        $ persistent.isabella = "Isabella"
    if persistent.jill == None:
        $ persistent.jill = "Jill"
    if persistent.quinn == None:
        $ persistent.quinn = "Quinn"
    if persistent.riona == None:
        $ persistent.riona = "Riona"
    if persistent.jade == None:
        $ persistent.jade = "Jade"
    if persistent.cathy == None:
        $ persistent.cathy = "Cathy"
    if persistent.camila == None:
        $ persistent.camila = "Camila"

    if persistent.ep1_card1 == None:
        $ persistent.ep1_card1 = False
    if persistent.ep1_card2 == None:
        $ persistent.ep1_card2 = False
    if persistent.ep1_card3 == None:
        $ persistent.ep1_card3 = False
    if persistent.ep1_card4 == None:
        $ persistent.ep1_card4 = False
    if persistent.ep1_card5 == None:
        $ persistent.ep1_card5 = False
    if persistent.ep1_card6 == None:
        $ persistent.ep1_card6 = False
    if persistent.ep1_card7 == None:
        $ persistent.ep1_card7 = False
    if persistent.ep1_card8 == None:
        $ persistent.ep1_card8 = False
    if persistent.ep1_card9 == None:
        $ persistent.ep1_card9 = False
    if persistent.ep1_card10 == None:
        $ persistent.ep1_card10 = False
    if persistent.ep1_card11 == None:
        $ persistent.ep1_card11 = False
    if persistent.ep1_card12 == None:
        $ persistent.ep1_card12 = False
    if persistent.ep1_card13 == None:
        $ persistent.ep1_card13 = False
    if persistent.ep1_card14 == None:
        $ persistent.ep1_card14 = False
    if persistent.ep1_card15 == None:
        $ persistent.ep1_card15 = False
    if persistent.ep1_card16 == None:
        $ persistent.ep1_card16 = False
    if persistent.ep1_card17 == None:
        $ persistent.ep1_card17 = False
    if persistent.ep1_card18 == None:
        $ persistent.ep1_card18 = False

    if persistent.rew_josy_unlocked == None:
        $ persistent.rew_josy_unlocked = 0
    if persistent.rew_maya_unlocked == None:
        $ persistent.rew_maya_unlocked = 0
    if persistent.rew_isa_unlocked == None:
        $ persistent.rew_isa_unlocked = 0
    if persistent.rew_sage_unlocked == None:
        $ persistent.rew_sage_unlocked = 0
    if persistent.rew_quinn_unlocked == None:
        $ persistent.rew_quinn_unlocked = 0
    if persistent.rew_jade_unlocked == None:
        $ persistent.rew_jade_unlocked = 0
    if persistent.rew_jill_unlocked == None:
        $ persistent.rew_jill_unlocked = 0
    if persistent.rew_riona_unlocked == None:
        $ persistent.rew_riona_unlocked = 0
    if persistent.rew_camila_unlocked == None:
        $ persistent.rew_camila_unlocked = 0
    if persistent.rew_mixed_unlocked == None:
        $ persistent.rew_mixed_unlocked = 0
    if persistent.rew_cathy_unlocked == None:
        $ persistent.rew_cathy_unlocked = 0

    if persistent.default_text_box_mode == None:
        $ persistent.default_text_box_mode = True
    if persistent.text_box_tutorial == None:
        $ persistent.text_box_tutorial = False
    if persistent.map_fast_travel == None:
        $ persistent.map_fast_travel = True
    if persistent.steam_owns_al == None:
        $ persistent.steam_owns_al = False
    if persistent.steam_owns_guide_s1 == None:
        $ persistent.steam_owns_guide_s1 = False
    if persistent.walkthrough_tutorial == None:
        $ persistent.walkthrough_tutorial = False
    if persistent.walkthrough_tutorial_s2 == None:
        $ persistent.walkthrough_tutorial_s2 = False
    if persistent.steam_owns_s2 == None:
        $ persistent.steam_owns_s2 = False
    $ config.autosave_on_choice = False
    $ _preferences.gl_powersave = False
    if persistent.autosave == None:
        $ persistent.autosave = True
    if persistent.autosave == None:
        $ persistent.autosave = True
    $ config.has_autosave = persistent.autosave
    if persistent.rewards_screen_on_hover == None:
        $ persistent.rewards_screen_on_hover = False
    if persistent.chat_new_rewards == None:
        $ persistent.chat_new_rewards = False

init python:
    def is_subscribed_app_al():
        return is_subscribed_app(1045520)
    def is_subscribed_app_guide_s1():
        return is_subscribed_app(1223490)
    def activate_overlay_to_store_al():
        activate_overlay_to_store(1045520, 0)
    def activate_overlay_to_store_badik():
        activate_overlay_to_store(1126320, 0)
    def activate_overlay_to_store_badik_s1_guide():
        activate_overlay_to_store(1223490, 0)
    def activate_overlay_to_store_badik_s2():
        activate_overlay_to_store(1215820, 0)
    def activate_overlay_to_store_badik_s2_guide():
        activate_overlay_to_store(1631620, 0)
    def is_subscribed_app_s2():
        return is_subscribed_app(1215820)
    def is_subscribed_app_guide_s2():
        return is_subscribed_app(1631620)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
