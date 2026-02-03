label ep1_freeroam_hots_label:
scene ep1_raid with wiperight
play music "music/ep4/jack_the_lumberer.mp3"
mc "(This is insane...)"
scene ep1_raid1 with dissolve
mc "(What do I say if someone catches me?)"
play sound "sound_effects/door_close.mp3"
scene ep1_raid2 with dissolve
mc "(I better not stick around here for too long...)"
mc "(In and out...let's just do this.)"
$ current_task = "Steal a pair of panties\nfrom the HOT girls."
$ chat_new_tasks = True
$ found_money = False
show white_screen with dissolve
show text "{font=collegiate.ttf}{size=+40}{color=#fe961b}Task:{/color} Steal a pair of panties from the HOT girls.{/size}{/font}":
    ypos 0.825
    xpos 0.5
$ ui.imagebutton("invisible_viewport", "invisible_viewport", clicked=ui.returns("OK"), xpos=0, ypos=0)
$ result = ui.interact()
if result == "OK":
    hide text "{font=collegiate.ttf}{size=+40}{color=#fe961b}Task:{/color} Steal a pair of panties from the HOT girls.{/size}{/font}"
    hide white_screen with dissolve
$ renpy.block_rollback()
if not persistent.ep1_card8:
    scene ep1_raid2b_card with dissolve
elif True:
    scene ep1_raid2b with dissolve
jump ep1_raid_hall_a_label_nofx

label ep1_raid_hall_a_label:
if not persistent.ep1_card8:
    scene ep1_raid2b_card
elif True:
    scene ep1_raid2b
label ep1_raid_hall_a_label_nofx:
$ renpy.block_rollback()
$ ui.imagebutton("fr_ep1_dad", "fr_ep1_go_right", clicked=ui.returns("go_right"), xpos=1690, ypos=250)
$ ui.imagebutton("fr_ep1_dad", "fr_ep1_go_left", clicked=ui.returns("go_left"), xpos=20, ypos=250)
$ ui.imagebutton("ep1_raid2b_idle", "ep1_raid2b_hover", clicked=ui.returns("hall"), xpos=0, ypos=0, focus_mask=True)
if not persistent.ep1_card8:
    $ ui.imagebutton("ep1_raid2b_hidden_card", "ep1_raid2b_hidden_card_hover", clicked=ui.returns("hidden_card"), xpos=640, ypos=686)
$ result = ui.interact()
if result == "go_right":
    jump ep1_raid_doors_label
elif result == "go_left":
    jump ep1_raid_sofa_label
elif result == "hall":
    jump ep1_raid_hall_label
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep1_card8 = True
    $ persistent.rew_riona_unlocked += 1
    $ chat_new_rewards = True
    $ calcRenders()
    scene ep1_raid2b with dissolve
    hide screen phone_screen
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    show screen phone_screen
    jump ep1_raid_hall_a_label_nofx

label ep1_raid_doors_label:
scene ep1_raid2d
$ renpy.block_rollback()
$ ui.imagebutton("fr_ep1_dad", "fr_ep1_go_left", clicked=ui.returns("go_left"), xpos=20, ypos=250)
$ ui.imagebutton("ep1_raid2d_left_idle", "ep1_raid2d_left_hover", clicked=ui.returns("left_door"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep1_raid2d_middle_idle", "ep1_raid2d_middle_hover", clicked=ui.returns("middle_door"), xpos=0, ypos=0, focus_mask=True)
if not ep1_raid_quinn_room:
    $ ui.imagebutton("ep1_raid2d_right_idle", "ep1_raid2d_right_hover", clicked=ui.returns("right_door"), xpos=0, ypos=0, focus_mask=True)
$ result = ui.interact()
if result == "go_left":
    jump ep1_raid_hall_a_label
elif result == "left_door":
    mc "(It's locked...)"
    mc "(Hm...it looks like the number {color=#00ff00}6{/color} is carved on the door frame. Weird...)"
    jump ep1_raid_doors_label
elif result == "middle_door":
    jump ep1_raid_closet_label
elif result == "right_door" and not ep1_raid_quinn_room:
    $ ep1_raid_quinn_room = True
    jump ep1_raid_quinn_label

label ep1_raid_sofa_label:
$ renpy.block_rollback()
scene ep1_raid2c
$ ui.imagebutton("fr_ep1_dad", "fr_ep1_go_right", clicked=ui.returns("go_right"), xpos=1690, ypos=250)
$ result = ui.interact()
if result == "go_right":
    jump ep1_raid_hall_a_label

label ep1_raid_closet_label:
if not persistent.ep1_card9 and not found_money:
    scene ep1_raid2f_money_card
elif not persistent.ep1_card9:
    scene ep1_raid2f_card
elif not found_money:
    scene ep1_raid2f_money
elif True:
    scene ep1_raid2f
if not found_money:
    $ ui.imagebutton("ep1_raid2f_money_hidden", "ep1_raid2f_money_hidden_hover", clicked=ui.returns("money"), xpos=993, ypos=203)
if not persistent.ep1_card9:
    $ ui.imagebutton("ep1_raid2f_card_hidden", "ep1_raid2f_card_hidden_hover", clicked=ui.returns("hidden_card"), xpos=899, ypos=870)
$ ui.imagebutton("fr_ep1_dad", "fr_ep1_go_left", clicked=ui.returns("go_left"), xpos=20, ypos=250)
$ result = ui.interact()
if result == "go_left":
    jump ep1_raid_doors_label
elif result == "money":
    $ mny(dollar)
    $ found_money = True
    show screen moneymsg
    if not persistent.ep1_card9:
        scene ep1_raid2f_card with dissolve
    elif True:
        scene ep1_raid2f with dissolve
    $ renpy.pause(3)
    hide screen moneymsg
    jump ep1_raid_closet_label
elif result == "hidden_card":
    hide screen phone_screen
    show screen srmsg
    $ renpy.block_rollback()
    $ persistent.ep1_card9 = True
    $ persistent.rew_josy_unlocked += 1
    $ chat_new_rewards = True
    $ calcRenders()
    if not found_money:
        scene ep1_raid2f_money with dissolve
    elif True:
        scene ep1_raid2f with dissolve
    $ renpy.pause(3)
    hide screen srmsg
    show screen phone_screen
    jump ep1_raid_closet_label


label ep1_raid_quinn_label:
$ renpy.block_rollback()
scene ep1_raid2g with dissolve
mc "(Oh fuck! I'm out of here...)"
cam "And that's all there is to it?"
qu "Yes, that's all there is to it. No other strings attached."
scene ep1_raid2g3 with dissolve
cam "Is this something all of you have done?"
scene ep1_raid2g2 with dissolve
qu "It's not forced, Camila."
qu "I don't ask everyone to do it."
qu "But based on what I see here standing right in front of me..."
qu "...you would be perfect for this."
scene ep1_raid2d with dissolve
jump ep1_raid_doors_label

label ep1_raid_hall_label:
$ renpy.block_rollback()
scene ep1_raid2e
$ ui.imagebutton("ep1_raid2e_right_idle", "ep1_raid2e_right_hover", clicked=ui.returns("right_door"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep1_raid2e_left_idle", "ep1_raid2e_left_hover", clicked=ui.returns("left_door"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("arrow_invis", "fr_ep1_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840)
$ result = ui.interact()

if result == "right_door":
    mc "(It's locked...)"
    jump ep1_raid_hall_label
elif result == "left_door":
    jump ep1_raid_shower_label
elif result == "go_down":
    jump ep1_raid_hall_a_label

label ep1_raid_shower_label:
if not persistent.ep1_card10:
    scene ep1_raid_shower_card with dissolve
elif True:
    scene ep1_raid_shower with dissolve
label ep1_raid_shower_label_nofx:
$ renpy.block_rollback()
if ep1_first_time_shower:
    $ ep1_first_time_shower = False
    mc "(The HOT girl's showers? Please, let there be some panties in here.)"

$ ui.imagebutton("fr_go_up_small_idle", "fr_go_up_small_hover", clicked=ui.returns("ep1_shower2"), xpos=220, ypos=400)
$ ui.imagebutton("arrow_invis", "fr_ep1_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840)
if not persistent.ep1_card10:
    $ ui.imagebutton("fr_ep1_hidden10", "fr_ep1_hidden10_hover", clicked=ui.returns("ep1_shower_hidden"), xpos=1042, ypos=790)
$ result = ui.interact()
if result == "ep1_shower2":
    jump ep1_raid_shower2_label
elif result == "go_down":
    jump ep1_raid_hall_label
elif result == "ep1_shower_hidden":
    hide screen phone_screen
    show screen srmsg
    $ renpy.block_rollback()
    $ persistent.ep1_card10 = True
    $ persistent.rew_riona_unlocked += 1
    $ chat_new_rewards = True
    $ calcRenders()
    scene ep1_raid_shower with dissolve
    $ renpy.pause(3)
    hide screen srmsg
    show screen phone_screen
    jump ep1_raid_shower_label_nofx

label ep1_raid_shower2_label:
$ renpy.block_rollback()
scene ep1_raid_shower2
$ ui.imagebutton("arrow_invis", "fr_ep1_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840)
$ ui.imagebutton("ep1_raid_panties", "ep1_raid_panties_hover", clicked=ui.returns("ep1_raid_panties"), xpos=1000, ypos=700)
$ result = ui.interact()
if result == "go_down":
    jump ep1_raid_shower_label
elif result == "ep1_raid_panties":
    jump ep1_raid_panties_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
