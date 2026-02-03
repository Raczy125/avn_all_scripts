init -1 python:
    def play_tennis_hit(trans, st, at):
        renpy.play("sound_effects/tennis_hit.mp3", "sfx1")
image anim_mc_serve_ep4 = Movie(channel="anim_mc_serve_ep4", play="images/movies/ep4/anim_tennis_mc_serve_ep4.webm")
image bg anim_mc_serve_ep4 movie:
    "anim_mc_serve_ep4"
    pause 2.50
    function play_tennis_hit
    pause 1.50
    "ep4_mc_serve2"


label ep4_tennis_jill_serve1_label:
scene ep4_tennis_jill_serve
jump tennis_mc_got_hit_label

label ep4_tennis_jill_serve2_label:
scene ep4_tennis_jill_serve2
jump tennis_mc_got_hit_label

label ep4_tennis_jill_serve3_label:
scene ep4_tennis_jill_serve3
jump tennis_mc_got_hit_label

label ep4_tennis_jill_serve4_label:
scene ep4_tennis_jill_serve4
jump tennis_mc_got_hit_label


label ep4_tennis_jill_miss1_label:
scene ep4_tennis_jill_miss
jump tennis_calculate_stats

label ep4_tennis_jill_miss2_label:
scene ep4_tennis_jill_miss2
jump tennis_calculate_stats

label ep4_tennis_jill_miss3_label:
scene ep4_tennis_jill_miss3
jump tennis_calculate_stats

label ep4_tennis_jill_miss4_label:
scene ep4_tennis_jill_miss4
jump tennis_calculate_stats


label ep4_tennis_jill_hit1_label:
scene ep4_tennis_jill_hit
jump tennis_mc_got_hit_label

label ep4_tennis_jill_hit2_label:
scene ep4_tennis_jill_hit2
jump tennis_mc_got_hit_label

label ep4_tennis_jill_hit3_label:
scene ep4_tennis_jill_hit3
jump tennis_mc_got_hit_label

label ep4_tennis_jill_hit4_label:
scene ep4_tennis_jill_hit4
jump tennis_mc_got_hit_label

label ep4_tennis_jill_hit5_label:
scene ep4_tennis_jill_hit5
jump tennis_mc_got_hit_label

label ep4_tennis_jill_hit6_label:
scene ep4_tennis_jill_hit6
jump tennis_mc_got_hit_label

label ep4_tennis_jill_hit7_label:
scene ep4_tennis_jill_hit7
jump tennis_mc_got_hit_label

label ep4_tennis_jill_hit8_label:
scene ep4_tennis_jill_hit8
jump tennis_mc_got_hit_label


label ep4_tennis_jill_win1_label:
scene ep4_tennis_jill_win1
ji "Yes!"
jump tennis_calculate_stats2

label ep4_tennis_jill_win2_label:
scene ep4_tennis_jill_win2
ji "Haha! That's my point!"
jump tennis_calculate_stats2

label ep4_tennis_jill_win3_label:
scene ep4_tennis_jill_win3
ji "Good game!"
jump tennis_calculate_stats2


label ep4_tennis_jill_lose1_label:
scene ep4_tennis_jill_lose1
ji "Argh! So close!"
jump tennis_calculate_stats2

label ep4_tennis_jill_lose2_label:
scene ep4_tennis_jill_lose2
ji "Haha! Missed it!"
jump tennis_calculate_stats2

label ep4_tennis_jill_lose3_label:
scene ep4_tennis_jill_lose3
ji "You're good!"
jump tennis_calculate_stats2

label ep4_tennis_jill_lose4_label:
scene ep4_tennis_jill_lose4
ji "Wow, I didn't even have time to react!"
jump tennis_calculate_stats2


label ep4_tennis_mc_miss1_label:
scene ep4_tennis_mc_miss
jump tennis_calculate_stats

label ep4_tennis_mc_miss2_label:
scene ep4_tennis_mc_miss2
jump tennis_calculate_stats

label ep4_tennis_mc_miss3_label:
scene ep4_tennis_mc_miss3
jump tennis_calculate_stats

label ep4_tennis_mc_net_label:
scene ep4_tennis_mc_net
jump tennis_calculate_stats


label ep4_tennis_mc_neutral_label:
scene ep4_tennis_mc_neutral
jump tennis_pre_select_label

label ep4_tennis_mc_neutral2_label:
scene ep4_tennis_mc_neutral2
jump tennis_pre_select_label


label ep4_tennis_mc_hit1_label:
scene ep4_tennis_mc_hit
jump tennis_mc_hit2_label

label ep4_tennis_mc_hit2_label:
scene ep4_tennis_mc_hit2
jump tennis_mc_hit2_label

label ep4_tennis_mc_hit3_label:
scene ep4_tennis_mc_hit3
jump tennis_mc_hit2_label

label ep4_tennis_mc_hit4_label:
scene ep4_tennis_mc_hit4
jump tennis_mc_hit2_label

label ep4_tennis_mc_hit5_label:
scene ep4_tennis_mc_hit5
jump tennis_mc_hit2_label

label ep4_tennis_mc_hit6_label:
scene ep4_tennis_mc_hit6
jump tennis_mc_hit2_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
