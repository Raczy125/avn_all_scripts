label header_ep4_label:

$ currentEpisode = 4
$ vault_ep4 = False
$ safe_digit_1 = 0
$ safe_digit_2 = 0
$ safe_digit_3 = 0
$ safe_digit_4 = 0
window hide

if not bios_alex:
    $ bios_alex     = True
    $ bios_beth     = True
    $ bios_brandi   = True
    $ bios_dany     = True
    $ bios_envy     = True
    $ bios_jimmy    = True
    $ bios_john     = True
    $ bios_lynette  = True
    $ bios_minny    = True
    $ bios_rose     = True
    $ bios_stanley  = True
    $ bios_wendy    = True

    if ep1_insulted_cafeteria_worker:
        $ bios_history_beth += "I told Sage a joke but ended up insulting Beth.\n\n"
    if ep2_cafeteriaWorkerInsulted:
        $ bios_history_beth += "Beth poured a drink on me because I insulted her.\n\n"

    if ep3_envyLewd == 1:
        $ bios_history_envy += "I got a blowjob from Envy at The Pink Rose.\n\n"
    elif ep3_envyLewd == 2:
        $ bios_history_envy += "I fucked Envy at The Pink Rose.\n\n"
    $ chat_new_bios = True

$ bios_bert     = False
$ bios_eugene   = True

default ep4_missedSage = False
if not ep2SageGuitarTeacher:
    $ ep4_missedSage = True
default ep3_fuckedRionaQuinn = False
if ep3_quri_mode > 0:
    $ ep3_fuckedRionaQuinn = True
default ep4_paid_for_sex = False
if ep3_fuckedRionaQuinn or quinn_shop_japanese_lvl > 0 or quinn_shop_spicy_lvl > 0 or ep2_fuckHOT:
    $ ep4_paid_for_sex = True

default ep4_wantedMoreMayaJosy = False
default ep4_talkedMelanie = False
default ep4_toldDerekYouTrustHim = False
default ep4_lickedAshley = False
default ep4_grindedLily = False
default ep4_touchedJillsBreasts = False
default ep4_lecturedBella = False
default ep4_rejectedMayaJosy = False
default guessedName = "Karen"
default ep4_jadeOffer = False
default ep4_rejectedJade = False
default ep4_fuckedJade = False
default ep4_rose_vaginal = False
default ep4_toldDerekAboutJade = False
default ep4_sawDrone = False
default ep4_talkedDroneDerek = False
default ep4_derekGone = False
default ep4_talkedToStudent = False
default ep4_talkedBert = False
default ep4_RonGone = False
default ep4_join_chess_club = False
default ep4_likeQuinn = False
default ep4_toldElenaInterested = False
default ep4_overreacted = False
default ep4_fuckedMelanie = False
default ep4_saturdayHelmet = False
default ep4_morningHelmet = False
default ep4_ugliest_ass = ""
default ep4_hottest_ass = ""
default ep4_hold_sage_hand = False
default ep4_sage_drink = False
default ep4_made_out_josy = False
default ep4_smoked_weed = False
default ep4_quinn_lewd = False
default ep4_bella_lewd = False
default ep4_sage_horny = False
default ep4_monaSlap = False
default ep4_camilaOffer = False
default ep4_knowLily = True
default ep4_paidMagnarWedgie = False
default ep4_sageLikeDaringSex = False
default ep4_swyperCathy = False
default ep4_kissedJill = False
default ep4_kissedJill2 = False
default ep4_wonTennis = False
default ep4_bestOutOf3 = False
default ep4_pinkRoseEvent = False
default ep4_SageMovieEvent = False
default ep4_jillShower = False
default ep4_jillNiceGuy = True
default ep4_checkedSwyper = False
default ep4_drunkBeerFreeroam = False
default ep4_playedGuitar = False
default pathMayaJosy = False
default ep4_fuckedSage = False
default ep4_called_sage2 = False
default ep4_heatherRoom = 0
default ep4_heather_event = False
default ep4_fr_sage_elena = False
default ep4_fr_sage_sauna = False
default ep4_fr_sage_sage = False
default ep4_cathyPostDeleted = False
default ep4_cluckDerekState = 0
default ep4_toldDerekAboutCathy = False
default ep4_called_sage = False
default ep4_bellaDishes = False
default ep4_bellaWaterCan = False
default ep4_changedSwimTrunks = False
default ep4_waterCharges = 0
default ep4_roomTempWater = False
default ep4_wateredPlant = False
default ep4_soil_state = []
default ep4_bellaHint = 0
default ep4_plantsWatered = 0
default ep4_wateringSatisfaction = "NONE"
default ep4_derekFuckedArieth = False
if ep2_shotWon:
    if ep2_danceSage or ep2_fuckHOT:
        $ ep4_derekFuckedArieth = True

default ep4_quinnAppeared = False
default ep4_talkedJacob = False
default ep4_talkedLeon = False
default ep4_talkedJohnBoy = False
default ep4_talkedRusty2 = False
default ep4_talkedRiona = False
default ep4_talkedNick = False
default ep4_talkedHeather = False
default ep4_monaState = 0
default ep4_sage_fr_key = False
default ep4_fr_quinn_event = False
default ep4_riona_fr_event = False
default ep4_camila_fr_event = False
default ep4_kissedRiona = False
default ep4_discussed_melanie = False
default ep4_discussed_jill = False
default ep4_discussed_isabella = False
default ep4_discussed_riona = False
default ep4_discussed_heather = False
default ep4_roseAppeared = False
default ep4_talkedTommy = False
default ep4_talkedDerek = False
default ep4_talkedRusty = False
default ep4_talkedSandy = False
default ep4_talkedEnvy = False
default ep4_talkedBrandi = False

default swyper_profile_pic = 1
default new_swype = False
default swyper_likes = 55
default swyper_dislikes = 12
default swyper_profile_count = 0
default swyper_liked_catrin = False
default swyper_liked_nicole = False
default swyper_liked_cathy = False
default swyper_liked_ida = False
default swyper_liked_ellie = False
default swyper_current_pic = 0
default swyper_chat_new_cathy = True
default swyper_chat_new_catrin = True
default swyper_chat_new_ida = True
default swyper_chat_new_nicole = True
default swyper_chat_new_ellie = True
default swyper_gallery_new_cathy = True
default swyper_gallery_new_catrin = True
default swyper_gallery_new_ida = True
default swyper_gallery_new_nicole = True
default swyper_gallery_new_ellie = True

default swyper_gallery_array_catrin = ["swyper_catrin_pic1", "swyper_catrin_pic2", "swyper_catrin_pic3"]
default swyper_gallery_array_cathy = ["swyper_cathy_pic1","swyper_cathy_pic2","swyper_cathy_pic3","swyper_cathy_pic4"]
default swyper_gallery_array_ida = ["swyper_ida_pic1","swyper_ida_pic2"]
default swyper_gallery_array_ellie = ["swyper_ellie_pic1","swyper_ellie_pic2","swyper_ellie_pic3"]
default swyper_gallery_array_nicole = ["swyper_nicole_pic1","swyper_nicole_pic2","swyper_nicole_pic3"]

default swyper_gallery_number_of_pics_catrin = 2
default swyper_gallery_number_of_pics_cathy = 3
default swyper_gallery_number_of_pics_ida = 1
default swyper_gallery_number_of_pics_ellie = 2
default swyper_gallery_number_of_pics_nicole = 2

default swyper_new_swype = True
default swyper_new_chat = False
default swyper_new_gallery = False
default swyper_reply = ""
default swyper_reply_array = ["","",""]
default swyper_next_state_array = ["","",""]
default swyper_chat_mc_avatar = "swyper_chat_mc1_avatar"

default swyper_catrin_state = "1"
default swyper_cathy_state = "1"
default swyper_ida_state = "1"
default swyper_ellie_state = "1"
default swyper_nicole_state = "1"

default swyper_catrin_history = ["How tall are you?"]
default swyper_cathy_history = ["Hey."]
default swyper_ida_history = ["Hey!!! Another swype guy! I remember swyping up on you! You're hot!"]
default swyper_ellie_history = ["Show me what you got!"]
default swyper_nicole_history = ["Well, look who it is..."]

default swyper_catrin_history_is_her = [True]
default swyper_cathy_history_is_her = [True]
default swyper_ida_history_is_her = [True]
default swyper_ellie_history_is_her = [True]
default swyper_nicole_history_is_her = [True]

default swyper_rejected_by_catrin = False
default swyper_rejected_by_ida = False
default swyper_rejected_by_ellie = False
default swyper_rejected_by_cathy = False
default swyper_rejected_by_nicole = False
default ep4_roseLewd = False
$ phone_clear_jump_label = "previousEp4Label"
default ep4_wearHelmet = False
jump clear_phone_chat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
