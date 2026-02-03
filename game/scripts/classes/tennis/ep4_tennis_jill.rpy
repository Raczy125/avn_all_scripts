screen tennis_stats_screen:
    tag tennis_stats_screen
    add "[tennis_vs]" xpos 0 ypos 0
    text "{size=+10}[tennis_pc_games_won]{/size}" xalign 0.128 yalign 0.015
    text "{color=#000000}{size=+10}[tennis_pc_game_score]{/size}{/color}" xalign 0.17 yalign 0.015

    text "{size=+10}[tennis_cpu_games_won]{/size}" xalign 0.128 yalign 0.09
    text "{color=#000000}{size=+10}[tennis_cpu_game_score]{/size}{/color}" xalign 0.17 yalign 0.09

transform tennis_bar_movement:
    xpos 1795
    ypos 940
    easeout 1 xpos 1800 ypos 55
    easeout 1 xpos 1800 ypos 940

image tennis_power_arrow_moving:
    "tennis_power_arrow"
    tennis_bar_movement
screen tennis_select_screen:

    modal True tag tennis_select_screen
    imagebutton:
        idle "tennis_bar"
        hover "tennis_bar"
        action NullAction()
        xalign 0.98
        yalign 0.5

    imagebutton:
        idle "tennis_ball_hit"
        hover "tennis_ball_hit"
        action (Hide('tennis_select_screen'),SetVariable("tennisSelectDigit", 1), Jump("tennis_select_label"))
        xpos tennis_xpos_arr[0]
        ypos tennis_ypos_arr[0]
    imagebutton:
        idle "tennis_ball_miss"
        hover "tennis_ball_miss"
        action (Hide('tennis_select_screen'),SetVariable("tennisSelectDigit", 0), Jump("tennis_select_label"))
        xpos tennis_xpos_arr[1]
        ypos tennis_ypos_arr[1]
    imagebutton:
        idle "tennis_ball_miss"
        hover "tennis_ball_miss"
        action (Hide('tennis_select_screen'),SetVariable("tennisSelectDigit", 0), Jump("tennis_select_label"))
        xpos tennis_xpos_arr[2]
        ypos tennis_ypos_arr[2]
    imagebutton:
        idle "tennis_ball_miss"
        hover "tennis_ball_miss"
        action (Hide('tennis_select_screen'),SetVariable("tennisSelectDigit", 0), Jump("tennis_select_label"))
        xpos tennis_xpos_arr[3]
        ypos tennis_ypos_arr[3]

    add "tennis_power_arrow_moving"
    timer 0.05 repeat True action If(t_time > 0, true=SetVariable('t_time', t_time - 0.05), false=NullAction())
    timer tennis_select_timer action [Hide('tennis_select_screen'), SetVariable("tennisSelectDigit", 0),Jump("tennis_select_label")]

label tennis_select_label:
$ renpy.block_rollback()
if t_time < 0.05:
    $ t_time = 0
if t_time >= 1.6:
    $ tennis_time_multiplier = 0
elif t_time >= 1.39:
    $ tennis_time_multiplier = 0.5
elif t_time >= 1.249:
    $ tennis_time_multiplier = 0.8
elif t_time >= 1.1:
    $ tennis_time_multiplier = 1.0
elif t_time >= 1.0:
    $ tennis_time_multiplier = 1.1
elif t_time >= 0.7:
    $ tennis_time_multiplier = 1.2
elif t_time >= 0.5:
    $ tennis_time_multiplier = 1.1
elif t_time >= 0.39:
    $ tennis_time_multiplier = 1.0
elif t_time >= 0.2:
    $ tennis_time_multiplier = 0.8
elif t_time >= 0.08:
    $ tennis_time_multiplier = 0.5
elif True:
    $ tennis_time_multiplier = 0

if tennisSelectDigit == 0:
    $ tennis_attack_multiplier = 0
    jump tennis_mc_missed_label
elif True:
    $ tennis_attack_multiplier = 20
    if tennis_attack_multiplier == 0:
        jump tennis_mc_missed_label
    elif tennis_isServing:
        $ renpy.pause(3.8-t_time)
jump tennis_mc_hit_label

label ep4_tennis_game_label:
$ tennis_vs = "tennis_vs_jill"
hide screen phone_screen
label tennis_start_label:
$ renpy.block_rollback()

$ tennis_jill_hit_array = ["ep4_tennis_jill_hit1_label", "ep4_tennis_jill_hit2_label", "ep4_tennis_jill_hit3_label", "ep4_tennis_jill_hit4_label", "ep4_tennis_jill_hit5_label", "ep4_tennis_jill_hit6_label", "ep4_tennis_jill_hit7_label", "ep4_tennis_jill_hit8_label"]
$ tennis_jill_miss_array = ["ep4_tennis_jill_miss1_label", "ep4_tennis_jill_miss2_label", "ep4_tennis_jill_miss3_label", "ep4_tennis_jill_miss4_label"]
$ tennis_jill_lose_array = ["ep4_tennis_jill_lose1_label", "ep4_tennis_jill_lose2_label", "ep4_tennis_jill_lose3_label", "ep4_tennis_jill_lose4_label"]
$ tennis_jill_serve_array = ["ep4_tennis_jill_serve1_label", "ep4_tennis_jill_serve2_label", "ep4_tennis_jill_serve3_label", "ep4_tennis_jill_serve4_label"]
$ tennis_jill_win_array = ["ep4_tennis_jill_win1_label", "ep4_tennis_jill_win2_label", "ep4_tennis_jill_win3_label"]

$ tennis_mc_hit_array = ["ep4_tennis_mc_hit1_label", "ep4_tennis_mc_hit2_label", "ep4_tennis_mc_hit3_label", "ep4_tennis_mc_hit4_label", "ep4_tennis_mc_hit5_label", "ep4_tennis_mc_hit6_label"]
$ tennis_mc_miss_array = ["ep4_tennis_mc_miss1_label", "ep4_tennis_mc_miss2_label", "ep4_tennis_mc_miss3_label", "ep4_tennis_mc_net_label"]
$ tennis_mc_neutral_array = ["ep4_tennis_mc_neutral_label", "ep4_tennis_mc_neutral2_label"]

$ tennis_pc_games_won = 0
$ tennis_cpu_games_won = 0
$ tennis_pc_game_score = "0"
$ tennis_cpu_game_score = "0"
$ tennis_opponent = "Jill"

$ tennis_difficulty = 0
$ tennis_time_multiplier = 0
$ tennis_select_timer  = 2
$ tennis_starting = True
$ tennis_isServing = True
$ tennis_attack_multiplier = 1.0
$ tennis_cpu_attack_multiplier = 1.0

$ tennisSelectDigit = 0
$ qM = quick_menu
$ quick_menu = 0

show screen tennis_stats_screen
$ renpy.block_rollback()

label tennis_decide_turn_label:
$ tennis_pc_hp = 100
$ tennis_cpu_hp = 100
$ tennis_game_has_been_won = False
if tennis_difficulty == 1:
    $ tennis_pc_hp = 100
    $ tennis_cpu_hp = 140
    $ tennis_cpu_attack_multiplier = 1.6
elif tennis_difficulty == 2:
    $ tennis_pc_hp = 100
    $ tennis_cpu_hp = 140
    $ tennis_cpu_attack_multiplier = 1.6
if tennis_starting:
    $ tennis_isServing = True
    jump tennis_mc_serve_label
elif True:
    jump tennis_cpu_serve_label

label tennis_mc_serve_label:
scene ep4_mc_serve
show tennis_serve
$ renpy.pause(1.5)
hide tennis_serve
show bg anim_mc_serve_ep4 movie
jump tennis_pre_select_label

label tennis_cpu_serve_label:
$ renpy.jump(tennis_jill_serve_array[renpy.random.randint(0,3)])

label tennis_pre_neutral_label:
$ renpy.block_rollback()
$ renpy.pause(1.5)

label tennis_neutral_label:
$ renpy.block_rollback()
$ renpy.jump(tennis_mc_neutral_array[renpy.random.randint(0,1)])

label tennis_pre_select_label:
$ renpy.block_rollback()
$ t_time = 1.95

$ tennis_xpos_arr = [renpy.random.randint(50,1600),0,0,0]
$ tmpInt2 = 1
while tmpInt2 < 4:
    $ tmpInt = renpy.random.randint(50,1600)
    if tmpInt2 == 1:
        if tmpInt > tennis_xpos_arr[tmpInt2-1] + 200 or tmpInt < tennis_xpos_arr[tmpInt2-1] - 200:
            $ tennis_xpos_arr[tmpInt2] = tmpInt
            $ tmpInt2 += 1
    elif tmpInt2 == 2:
        if tmpInt > tennis_xpos_arr[tmpInt2-1] + 200 or tmpInt < tennis_xpos_arr[tmpInt2-1] - 200:
            if tmpInt > tennis_xpos_arr[tmpInt2-2] + 200 or tmpInt < tennis_xpos_arr[tmpInt2-2] - 200:
                $ tennis_xpos_arr[tmpInt2] = tmpInt
                $ tmpInt2 += 1
    elif True:
        if tmpInt > tennis_xpos_arr[tmpInt2-1] + 200 or tmpInt < tennis_xpos_arr[tmpInt2-1] - 200:
            if tmpInt > tennis_xpos_arr[tmpInt2-2] + 200 or tmpInt < tennis_xpos_arr[tmpInt2-2] - 200:
                if tmpInt > tennis_xpos_arr[tmpInt2-3] + 200 or tmpInt < tennis_xpos_arr[tmpInt2-3] - 200:
                    $ tennis_xpos_arr[tmpInt2] = tmpInt
                    $ tmpInt2 += 1

$ tennis_ypos_arr = [renpy.random.randint(150,850),renpy.random.randint(150,850),renpy.random.randint(150,850),renpy.random.randint(150,850)]

show screen tennis_select_screen
$ renpy.pause()



label tennis_mc_got_hit_label:
play sound "sound_effects/tennis_hit2.mp3"
$ tennis_dmg = int(renpy.random.randint(10*tennis_cpu_attack_multiplier, 20*tennis_cpu_attack_multiplier))
$ tennis_pc_hp -= tennis_dmg
if tennis_pc_hp < 0:
    $ tennis_pc_hp = 0
$ renpy.pause(1.5)
if tennis_pc_hp <= 0:
    play sound "sound_effects/tennis_miss.mp3"
    $ tennis_lost_point = True
    $ renpy.jump(tennis_mc_miss_array[renpy.random.randint(0,2)])
jump tennis_neutral_label

label tennis_mc_missed_label:
$ renpy.block_rollback()
play sound "sound_effects/tennis_miss.mp3"
$ tennis_lost_point = True
if tennis_isServing:
    $ renpy.jump(tennis_mc_miss_array[0])
elif True:
    $ renpy.jump(tennis_mc_miss_array[renpy.random.randint(0,3)])

label tennis_mc_hit_label:
$ renpy.block_rollback()
if tennis_isServing:
    jump tennis_mc_hit2_label
elif True:
    play sound "sound_effects/tennis_hit.mp3"
    $ renpy.jump(tennis_mc_hit_array[renpy.random.randint(0,5)])

label tennis_mc_hit2_label:
$ tennis_dmg = int((renpy.random.randint(10*tennis_attack_multiplier, 20*tennis_attack_multiplier)/10) * tennis_time_multiplier)
$ tennis_cpu_hp -= tennis_dmg
if tennis_cpu_hp < 0:
    $ tennis_cpu_hp = 0
if tennis_isServing:
    $ tennis_isServing = False
elif True:
    $ renpy.pause(1.5)
if tennis_cpu_hp <= 0:
    play sound "sound_effects/tennis_miss.mp3"
    $ tennis_lost_point = False
    $ renpy.jump(tennis_jill_miss_array[renpy.random.randint(0,3)])
play sound "sound_effects/tennis_hit2.mp3"
$ renpy.jump(tennis_jill_hit_array[renpy.random.randint(0,7)])

label tennis_calculate_stats:
$ renpy.pause(1.5)
if tennis_lost_point:
    if tennis_cpu_game_score == "0":
        $ tennis_cpu_game_score = "15"
    elif tennis_cpu_game_score == "15":
        $ tennis_cpu_game_score = "30"
    elif tennis_cpu_game_score == "30":
        $ tennis_cpu_game_score = "40"
    elif tennis_cpu_game_score == "40" and tennis_pc_game_score == "ad":
        $ tennis_pc_game_score = "40"
    elif tennis_cpu_game_score == "ad":
        $ tennis_cpu_games_won += 1
        $ tennis_game_has_been_won = True
        $ tennis_cpu_game_score = "0"
        $ tennis_pc_game_score = "0"
    elif tennis_cpu_game_score == "40" and tennis_pc_game_score == "40":
        $ tennis_cpu_game_score = "ad"
    elif tennis_cpu_game_score == "40":
        $ tennis_cpu_games_won += 1
        $ tennis_game_has_been_won = True
        $ tennis_cpu_game_score = "0"
        $ tennis_pc_game_score = "0"
elif True:
    if tennis_pc_game_score == "0":
        $ tennis_pc_game_score = "15"
    elif tennis_pc_game_score == "15":
        $ tennis_pc_game_score = "30"
    elif tennis_pc_game_score == "30":
        $ tennis_pc_game_score = "40"
    elif tennis_pc_game_score == "40" and tennis_cpu_game_score == "ad":
        $ tennis_cpu_game_score = "40"
    elif tennis_pc_game_score == "ad":
        $ tennis_pc_games_won += 1
        $ tennis_game_has_been_won = True
        $ tennis_cpu_game_score = "0"
        $ tennis_pc_game_score = "0"
    elif tennis_pc_game_score == "40" and tennis_cpu_game_score == "40":
        $ tennis_pc_game_score = "ad"
    elif tennis_pc_game_score == "40":
        $ tennis_pc_games_won += 1
        $ tennis_game_has_been_won = True
        $ tennis_cpu_game_score = "0"
        $ tennis_pc_game_score = "0"

if tennis_lost_point:
    $ renpy.jump(tennis_jill_win_array[renpy.random.randint(0,2)])
elif True:
    $ renpy.jump(tennis_jill_lose_array[renpy.random.randint(0,3)])
label tennis_calculate_stats2:
if ep4_bestOutOf3 and tennis_pc_games_won + tennis_cpu_games_won == 1:
    $ tennis_difficulty = 1
elif ep4_bestOutOf3 and tennis_pc_games_won + tennis_cpu_games_won == 2:
    $ tennis_difficulty = 2
if ep4_bestOutOf3 and tennis_pc_games_won == 2:
    $ tennis_victory = True
    jump tennis_fight_done
elif ep4_bestOutOf3 and tennis_cpu_games_won == 2:
    $ tennis_victory = False
    jump tennis_fight_done
if ep4_bestOutOf3 and tennis_pc_games_won == 2:
    $ tennis_victory = True
    jump tennis_fight_done
elif not ep4_bestOutOf3 and tennis_cpu_games_won == 1:
    $ tennis_victory = False
    jump tennis_fight_done
elif not ep4_bestOutOf3 and tennis_pc_games_won == 1:
    $ tennis_victory = True
    jump tennis_fight_done
elif tennis_game_has_been_won:
    $ tennis_game_has_been_won = False
    if tennis_starting:
        $ tennis_starting = False
    elif True:
        $ tennis_starting = True
jump tennis_decide_turn_label

if tennis_match_lost:
    jump tennis_fight_done
elif True:
    jump tennis_decide_turn_label

label tennis_fight_done:
hide screen tennis_stats_screen
if tennis_victory:
    if not persistent.ep4_card14:
        $ persistent.ep4_card14 = True
        $ persistent.rew_camila_unlocked += 1
        $ chat_new_rewards = True
        $ calcRenders()
        show screen srmsg
        $ renpy.pause(3)
        hide screen srmsg
    $ ep4_wonTennis = True
    if steamAchievements and ep4_bestOutOf3 and not config.console and not config.developer:
        $ achievement.grant("WIMBLEDON")
        init:
            $ achievement.register("WIMBLEDON")
        $ achievement.Sync()
elif True:
    $ ep4_wonTennis = False
$ renpy.block_rollback()
$ quick_menu = qM
show screen phone_screen
jump ep4_after_tennis_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
