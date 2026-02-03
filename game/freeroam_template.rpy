label ep__label:
$ renpy.block_rollback()
$ currentFreeRoamLabel = ""
$ phone_call_enabled = True
if not persistent.ep_card:
    scene ep_
elif True:
    scene ep_nocard
label ep__label_nofx:

$ ui.imagebutton("arrow_invis", "fr_ep1_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840)
$ ui.imagebutton("fr_ep1_dad", "fr_ep1_go_right", clicked=ui.returns("go_right"), xpos=1690, ypos=250)
$ ui.imagebutton("fr_ep1_dad", "fr_ep1_go_left", clicked=ui.returns("go_left"), xpos=20, ypos=250)
$ ui.imagebutton("ep1_hallway2_shower", "fr_ep1_go_up", clicked=ui.returns("go_up"), xpos=0, ypos=20)

if not persistent.ep1_card12:
    $ ui.imagebutton("fr_ep1_card12", "fr_ep1_card12_hover", clicked=ui.returns("hidden_card"), xpos=936, ypos=760)
$ result = ui.interact()
if result == "go_down":
    jump _label
elif result == "go_up":
    jump _label
elif result == "go_right":
    jump _label
elif result == "go_left":
    jump _label
elif result == "hidden_card":
    $ renpy.block_rollback()
    $ persistent.ep_card = True
    $ persistent.rew__unlocked += 1
    $ chat_new_rewards = True
    scene ep_ with dissolve
    hide screen phone_screen
    show screen srmsg
    $ renpy.pause(3)
    hide screen srmsg
    show screen phone_screen
    jump ep__label_nofx
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
