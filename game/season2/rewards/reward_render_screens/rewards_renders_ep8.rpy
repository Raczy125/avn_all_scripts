
screen ep8_cr1:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_cr_1.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep8_cr2:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_cr_2.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep8_cr3:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_cr_3.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep8_cr4:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_cr_4.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep8_cr5:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_cr_5.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep8_cr6:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_cr_6.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep8_cr7:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_cr_7.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep8_cr8:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_cr_8.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")


screen ep8_wallpaper_isabella_1:

    modal True tag reward_screen
    key "mouseup_2" action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    if toggled_2d_mode == 1:
        add "season2/rewards/ep8/ep8_wallpaper_isabella_1a.jpg"
    else:
        add "season2/rewards/ep8/ep8_wallpaper_isabella_1b.jpg"

    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    hbox:
        xalign 0.02
        yalign 0.02
        if toggled_2d_mode == 2:
            imagebutton:
                idle "toggle_2d_clothed_idle"
                hover "toggle_2d_clothed_hover"
                action SetVariable("toggled_2d_mode", 1)
            imagebutton:
                idle "toggle_2d_nude"
                hover "toggle_2d_nude"
                action SetVariable("toggled_2d_mode", 1)
        else:
            imagebutton:
                idle "toggle_2d_clothed"
                hover "toggle_2d_clothed"
                action SetVariable("toggled_2d_mode", 2)
            imagebutton:
                idle "toggle_2d_nude_idle"
                hover "toggle_2d_nude_hover"
                action SetVariable("toggled_2d_mode", 2)

screen ep8_wallpaper_jill_1:

    modal True tag reward_screen
    key "mouseup_2" action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    if toggled_2d_mode == 1:
        add "season2/rewards/ep8/ep8_wallpaper_jill_1a.jpg"
    else:
        add "season2/rewards/ep8/ep8_wallpaper_jill_1b.jpg"

    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    hbox:
        xalign 0.02
        yalign 0.02
        if toggled_2d_mode == 2:
            imagebutton:
                idle "toggle_2d_clothed_idle"
                hover "toggle_2d_clothed_hover"
                action SetVariable("toggled_2d_mode", 1)
            imagebutton:
                idle "toggle_2d_nude"
                hover "toggle_2d_nude"
                action SetVariable("toggled_2d_mode", 1)
        else:
            imagebutton:
                idle "toggle_2d_clothed"
                hover "toggle_2d_clothed"
                action SetVariable("toggled_2d_mode", 2)
            imagebutton:
                idle "toggle_2d_nude_idle"
                hover "toggle_2d_nude_hover"
                action SetVariable("toggled_2d_mode", 2)

screen ep8_wallpaper_josy_1:

    modal True tag reward_screen
    key "mouseup_2" action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    if toggled_2d_mode == 1:
        add "season2/rewards/ep8/ep8_wallpaper_josy_1a.jpg"
    else:
        add "season2/rewards/ep8/ep8_wallpaper_josy_1b.jpg"

    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    hbox:
        xalign 0.02
        yalign 0.02
        if toggled_2d_mode == 2:
            imagebutton:
                idle "toggle_2d_clothed_idle"
                hover "toggle_2d_clothed_hover"
                action SetVariable("toggled_2d_mode", 1)
            imagebutton:
                idle "toggle_2d_nude"
                hover "toggle_2d_nude"
                action SetVariable("toggled_2d_mode", 1)
        else:
            imagebutton:
                idle "toggle_2d_clothed"
                hover "toggle_2d_clothed"
                action SetVariable("toggled_2d_mode", 2)
            imagebutton:
                idle "toggle_2d_nude_idle"
                hover "toggle_2d_nude_hover"
                action SetVariable("toggled_2d_mode", 2)

screen ep8_wallpaper_maya_1:

    modal True tag reward_screen
    key "mouseup_2" action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    if toggled_2d_mode == 1:
        add "season2/rewards/ep8/ep8_wallpaper_maya_1a.jpg"
    else:
        add "season2/rewards/ep8/ep8_wallpaper_maya_1b.jpg"

    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    hbox:
        xalign 0.02
        yalign 0.02
        if toggled_2d_mode == 2:
            imagebutton:
                idle "toggle_2d_clothed_idle"
                hover "toggle_2d_clothed_hover"
                action SetVariable("toggled_2d_mode", 1)
            imagebutton:
                idle "toggle_2d_nude"
                hover "toggle_2d_nude"
                action SetVariable("toggled_2d_mode", 1)
        else:
            imagebutton:
                idle "toggle_2d_clothed"
                hover "toggle_2d_clothed"
                action SetVariable("toggled_2d_mode", 2)
            imagebutton:
                idle "toggle_2d_nude_idle"
                hover "toggle_2d_nude_hover"
                action SetVariable("toggled_2d_mode", 2)

screen ep8_wallpaper_quinn_1:

    modal True tag reward_screen
    key "mouseup_2" action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    if toggled_2d_mode == 1:
        add "season2/rewards/ep8/ep8_wallpaper_quinn_1a.jpg"
    else:
        add "season2/rewards/ep8/ep8_wallpaper_quinn_1b.jpg"

    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    hbox:
        xalign 0.02
        yalign 0.02
        if toggled_2d_mode == 2:
            imagebutton:
                idle "toggle_2d_clothed_idle"
                hover "toggle_2d_clothed_hover"
                action SetVariable("toggled_2d_mode", 1)
            imagebutton:
                idle "toggle_2d_nude"
                hover "toggle_2d_nude"
                action SetVariable("toggled_2d_mode", 1)
        else:
            imagebutton:
                idle "toggle_2d_clothed"
                hover "toggle_2d_clothed"
                action SetVariable("toggled_2d_mode", 2)
            imagebutton:
                idle "toggle_2d_nude_idle"
                hover "toggle_2d_nude_hover"
                action SetVariable("toggled_2d_mode", 2)

screen ep8_wallpaper_sage_1:

    modal True tag reward_screen
    key "mouseup_2" action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    if toggled_2d_mode == 1:
        add "season2/rewards/ep8/ep8_wallpaper_sage_1a.jpg"
    else:
        add "season2/rewards/ep8/ep8_wallpaper_sage_1b.jpg"

    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    hbox:
        xalign 0.02
        yalign 0.02
        if toggled_2d_mode == 2:
            imagebutton:
                idle "toggle_2d_clothed_idle"
                hover "toggle_2d_clothed_hover"
                action SetVariable("toggled_2d_mode", 1)
            imagebutton:
                idle "toggle_2d_nude"
                hover "toggle_2d_nude"
                action SetVariable("toggled_2d_mode", 1)
        else:
            imagebutton:
                idle "toggle_2d_clothed"
                hover "toggle_2d_clothed"
                action SetVariable("toggled_2d_mode", 2)
            imagebutton:
                idle "toggle_2d_nude_idle"
                hover "toggle_2d_nude_hover"
                action SetVariable("toggled_2d_mode", 2)

screen ep8_wallpaper_envy_1:

    modal True tag reward_screen
    key "mouseup_2" action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    if toggled_2d_mode == 1:
        add "season2/rewards/ep8/ep8_wallpaper_envy_1a.jpg"
    else:
        add "season2/rewards/ep8/ep8_wallpaper_envy_1b.jpg"

    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    hbox:
        xalign 0.02
        yalign 0.02
        if toggled_2d_mode == 2:
            imagebutton:
                idle "toggle_2d_clothed_idle"
                hover "toggle_2d_clothed_hover"
                action SetVariable("toggled_2d_mode", 1)
            imagebutton:
                idle "toggle_2d_nude"
                hover "toggle_2d_nude"
                action SetVariable("toggled_2d_mode", 1)
        else:
            imagebutton:
                idle "toggle_2d_clothed"
                hover "toggle_2d_clothed"
                action SetVariable("toggled_2d_mode", 2)
            imagebutton:
                idle "toggle_2d_nude_idle"
                hover "toggle_2d_nude_hover"
                action SetVariable("toggled_2d_mode", 2)

screen ep8_wallpaper_jade_1:

    modal True tag reward_screen
    key "mouseup_2" action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    if toggled_2d_mode == 1:
        add "season2/rewards/ep8/ep8_wallpaper_jade_1a.jpg"
    else:
        add "season2/rewards/ep8/ep8_wallpaper_jade_1b.jpg"

    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    hbox:
        xalign 0.02
        yalign 0.02
        if toggled_2d_mode == 2:
            imagebutton:
                idle "toggle_2d_clothed_idle"
                hover "toggle_2d_clothed_hover"
                action SetVariable("toggled_2d_mode", 1)
            imagebutton:
                idle "toggle_2d_nude"
                hover "toggle_2d_nude"
                action SetVariable("toggled_2d_mode", 1)
        else:
            imagebutton:
                idle "toggle_2d_clothed"
                hover "toggle_2d_clothed"
                action SetVariable("toggled_2d_mode", 2)
            imagebutton:
                idle "toggle_2d_nude_idle"
                hover "toggle_2d_nude_hover"
                action SetVariable("toggled_2d_mode", 2)

screen ep8_wallpaper_madame_1:

    modal True tag reward_screen
    key "mouseup_2" action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    if toggled_2d_mode == 1:
        add "season2/rewards/ep8/ep8_wallpaper_madame_1a.jpg"
    else:
        add "season2/rewards/ep8/ep8_wallpaper_madame_1b.jpg"

    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    hbox:
        xalign 0.02
        yalign 0.02
        if toggled_2d_mode == 2:
            imagebutton:
                idle "toggle_2d_nocum_idle"
                hover "toggle_2d_nocum_hover"
                action SetVariable("toggled_2d_mode", 1)
            imagebutton:
                idle "toggle_2d_cum"
                hover "toggle_2d_cum"
                action SetVariable("toggled_2d_mode", 1)
        else:
            imagebutton:
                idle "toggle_2d_nocum"
                hover "toggle_2d_nocum"
                action SetVariable("toggled_2d_mode", 2)
            imagebutton:
                idle "toggle_2d_cum_idle"
                hover "toggle_2d_cum_hover"
                action SetVariable("toggled_2d_mode", 2)


screen ep8_cards1:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_sally_1.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep8_cards2:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_sally_2.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep8_cards3:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_sally_3.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep8_cards4:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_sally_4.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep8_cards5:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_sally_5.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep8_cards6:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_sally_6.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep8_cards7:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_sally_7.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep8_cards8:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_sally_8.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep8_cards9:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_sally_9.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep8_cards10:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_sally_10.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep8_cards11:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_sally_11.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep8_cards12:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_sally_12.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep8_cards13:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_sally_13.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep8_cards14:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_sally_14.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep8_cards15:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_sally_15.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep8_cards16:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_sally_16.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep8_cards17:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_sally_17.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep8_cards18:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_sally_18.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep8_cards19:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_sally_19.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")


screen ep8_cardsa1:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_sage_1.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep8_cardsa2:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_sage_2.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep8_cardsa3:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_sage_3.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep8_cardsa4:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_sage_4.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep8_cardsa5:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_sage_5.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep8_cardsa6:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_sage_6.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep8_cardsa7:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_sage_7.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep8_cardsa8:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_sage_8.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep8_cardsa9:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_sage_9.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep8_cardsa10:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_sage_10.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep8_cardsa11:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_sage_11.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep8_cardsa12:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_sage_12.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep8_cardsa13:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_sage_13.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep8_cardsa14:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_sage_14.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep8_cardsa15:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_sage_15.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep8_cardsa16:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_sage_16.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep8_cardsa17:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_sage_17.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep8_cardsa18:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep8/ep8_reward_sage_18.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
