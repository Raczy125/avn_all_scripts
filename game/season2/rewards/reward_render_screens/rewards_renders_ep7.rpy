
screen ep7_wallpaper_isabella_1:

    modal True tag reward_screen
    key "mouseup_2" action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    if toggled_2d_mode == 1:
        add "season2/rewards/ep7/ep7_wallpaper_isabella_1a.jpg"
    else:
        add "season2/rewards/ep7/ep7_wallpaper_isabella_1b.jpg"

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

screen ep7_wallpaper_isabella_2:

    modal True tag reward_screen
    key "mouseup_2" action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    if toggled_2d_mode == 1:
        add "season2/rewards/ep7/ep7_wallpaper_isabella_2a.jpg"
    else:
        add "season2/rewards/ep7/ep7_wallpaper_isabella_2b.jpg"

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

screen ep7_wallpaper_jill_1:

    modal True tag reward_screen
    key "mouseup_2" action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    if toggled_2d_mode == 1:
        add "season2/rewards/ep7/ep7_wallpaper_jill_1a.jpg"
    else:
        add "season2/rewards/ep7/ep7_wallpaper_jill_1b.jpg"

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

screen ep7_wallpaper_jill_2:

    modal True tag reward_screen
    key "mouseup_2" action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    if toggled_2d_mode == 1:
        add "season2/rewards/ep7/ep7_wallpaper_jill_2a.jpg"
    else:
        add "season2/rewards/ep7/ep7_wallpaper_jill_2b.jpg"

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

screen ep7_wallpaper_josy_1:

    modal True tag reward_screen
    key "mouseup_2" action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    if toggled_2d_mode == 1:
        add "season2/rewards/ep7/ep7_wallpaper_josy_1a.jpg"
    else:
        add "season2/rewards/ep7/ep7_wallpaper_josy_1b.jpg"

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

screen ep7_wallpaper_josy_2:

    modal True tag reward_screen
    key "mouseup_2" action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    if toggled_2d_mode == 1:
        add "season2/rewards/ep7/ep7_wallpaper_josy_2a.jpg"
    else:
        add "season2/rewards/ep7/ep7_wallpaper_josy_2b.jpg"

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

screen ep7_wallpaper_maya_1:

    modal True tag reward_screen
    key "mouseup_2" action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    if toggled_2d_mode == 1:
        add "season2/rewards/ep7/ep7_wallpaper_maya_1a.jpg"
    else:
        add "season2/rewards/ep7/ep7_wallpaper_maya_1b.jpg"

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

screen ep7_wallpaper_maya_2:

    modal True tag reward_screen
    key "mouseup_2" action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    if toggled_2d_mode == 1:
        add "season2/rewards/ep7/ep7_wallpaper_maya_2a.jpg"
    else:
        add "season2/rewards/ep7/ep7_wallpaper_maya_2b.jpg"

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

screen ep7_wallpaper_sage_1:

    modal True tag reward_screen
    key "mouseup_2" action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    if toggled_2d_mode == 1:
        add "season2/rewards/ep7/ep7_wallpaper_sage_1a.jpg"
    else:
        add "season2/rewards/ep7/ep7_wallpaper_sage_1b.jpg"

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

screen ep7_wallpaper_sage_2:

    modal True tag reward_screen
    key "mouseup_2" action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    if toggled_2d_mode == 1:
        add "season2/rewards/ep7/ep7_wallpaper_sage_2a.jpg"
    else:
        add "season2/rewards/ep7/ep7_wallpaper_sage_2b.jpg"

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


screen ep7_card_camila_1:

    modal True tag reward_screen
    key "mouseup_2" action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    if toggled_2d_mode == 1:
        add "season2/rewards/ep7/ep7_reward_2d_camila.jpg"
    elif toggled_2d_mode == 2:
        add "season2/rewards/ep8/ep8_reward_2d_camila_2.jpg"
    else:
        add "season2/rewards/epX/epX_reward_2d_camila_3.jpg"

    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    hbox:
        xalign 0.02
        yalign 0.02
        if toggled_2d_mode == 1:
            imagebutton:
                idle "toggle_2d_clothed"
                hover "toggle_2d_clothed"
                action NullAction()
        else:
            imagebutton:
                idle "toggle_2d_clothed_idle"
                hover "toggle_2d_clothed_hover"
                action SetVariable("toggled_2d_mode", 1)
        if toggled_2d_mode == 2:
            imagebutton:
                idle "toggle_2d_partial"
                hover "toggle_2d_partial"
                action NullAction()
        else:
            imagebutton:
                if persistent.art_unlocked_lvl2[current_2d_girl]:
                    idle "toggle_2d_partial_idle"
                    hover "toggle_2d_partial_hover"
                    action SetVariable("toggled_2d_mode", 2)
                else:
                    idle "toggle_2d_partial_disabled"
                    hover "toggle_2d_partial_disabled"
                    action NullAction()
        if toggled_2d_mode == 3:
            imagebutton:
                idle "toggle_2d_nude"
                hover "toggle_2d_nude"
                action NullAction()
        else:
            imagebutton:
                if persistent.art_unlocked_lvl3[current_2d_girl]:
                    idle "toggle_2d_nude_idle"
                    hover "toggle_2d_nude_hover"
                    action SetVariable("toggled_2d_mode", 3)
                else:
                    idle "toggle_2d_nude_disabled"
                    hover "toggle_2d_nude_disabled"
                    action NullAction()

screen ep7_card_cathy_1:

    modal True tag reward_screen
    key "mouseup_2" action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    if toggled_2d_mode == 1:
        add "season2/rewards/ep7/ep7_reward_2d_cathy.jpg"
    elif toggled_2d_mode == 2:
        add "season2/rewards/epX/epX_reward_2d_cathy_2.jpg"
    else:
        add "season2/rewards/epX/epX_reward_2d_cathy_3.jpg"

    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    hbox:
        xalign 0.02
        yalign 0.02
        if toggled_2d_mode == 1:
            imagebutton:
                idle "toggle_2d_clothed"
                hover "toggle_2d_clothed"
                action NullAction()
        else:
            imagebutton:
                idle "toggle_2d_clothed_idle"
                hover "toggle_2d_clothed_hover"
                action SetVariable("toggled_2d_mode", 1)
        if toggled_2d_mode == 2:
            imagebutton:
                idle "toggle_2d_partial"
                hover "toggle_2d_partial"
                action NullAction()
        else:
            imagebutton:
                if persistent.art_unlocked_lvl2[current_2d_girl]:
                    idle "toggle_2d_partial_idle"
                    hover "toggle_2d_partial_hover"
                    action SetVariable("toggled_2d_mode", 2)
                else:
                    idle "toggle_2d_partial_disabled"
                    hover "toggle_2d_partial_disabled"
                    action NullAction()
        if toggled_2d_mode == 3:
            imagebutton:
                idle "toggle_2d_nude"
                hover "toggle_2d_nude"
                action NullAction()
        else:
            imagebutton:
                if persistent.art_unlocked_lvl3[current_2d_girl]:
                    idle "toggle_2d_nude_idle"
                    hover "toggle_2d_nude_hover"
                    action SetVariable("toggled_2d_mode", 3)
                else:
                    idle "toggle_2d_nude_disabled"
                    hover "toggle_2d_nude_disabled"
                    action NullAction()

screen ep7_card_envy_1:

    modal True tag reward_screen
    key "mouseup_2" action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    if toggled_2d_mode == 1:
        add "season2/rewards/ep7/ep7_reward_2d_envy.jpg"
    elif toggled_2d_mode == 2:
        add "season2/rewards/ep8/ep8_reward_2d_envy_2.jpg"
    else:
        add "season2/rewards/epX/epX_reward_2d_envy_3.jpg"

    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    hbox:
        xalign 0.02
        yalign 0.02
        if toggled_2d_mode == 1:
            imagebutton:
                idle "toggle_2d_clothed"
                hover "toggle_2d_clothed"
                action NullAction()
        else:
            imagebutton:
                idle "toggle_2d_clothed_idle"
                hover "toggle_2d_clothed_hover"
                action SetVariable("toggled_2d_mode", 1)
        if toggled_2d_mode == 2:
            imagebutton:
                idle "toggle_2d_partial"
                hover "toggle_2d_partial"
                action NullAction()
        else:
            imagebutton:
                if persistent.art_unlocked_lvl2[current_2d_girl]:
                    idle "toggle_2d_partial_idle"
                    hover "toggle_2d_partial_hover"
                    action SetVariable("toggled_2d_mode", 2)
                else:
                    idle "toggle_2d_partial_disabled"
                    hover "toggle_2d_partial_disabled"
                    action NullAction()
        if toggled_2d_mode == 3:
            imagebutton:
                idle "toggle_2d_nude"
                hover "toggle_2d_nude"
                action NullAction()
        else:
            imagebutton:
                if persistent.art_unlocked_lvl3[current_2d_girl]:
                    idle "toggle_2d_nude_idle"
                    hover "toggle_2d_nude_hover"
                    action SetVariable("toggled_2d_mode", 3)
                else:
                    idle "toggle_2d_nude_disabled"
                    hover "toggle_2d_nude_disabled"
                    action NullAction()

screen ep7_card_isabella_1:

    modal True tag reward_screen
    key "mouseup_2" action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    if toggled_2d_mode == 1:
        add "season2/rewards/ep7/ep7_reward_2d_isabella.jpg"
    elif toggled_2d_mode == 2:
        add "season2/rewards/epX/epX_reward_2d_isabella_2.jpg"
    else:
        add "season2/rewards/epX/epX_reward_2d_isabella_3.jpg"

    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    hbox:
        xalign 0.02
        yalign 0.02
        if toggled_2d_mode == 1:
            imagebutton:
                idle "toggle_2d_clothed"
                hover "toggle_2d_clothed"
                action NullAction()
        else:
            imagebutton:
                idle "toggle_2d_clothed_idle"
                hover "toggle_2d_clothed_hover"
                action SetVariable("toggled_2d_mode", 1)
        if toggled_2d_mode == 2:
            imagebutton:
                idle "toggle_2d_partial"
                hover "toggle_2d_partial"
                action NullAction()
        else:
            imagebutton:
                if persistent.art_unlocked_lvl2[current_2d_girl]:
                    idle "toggle_2d_partial_idle"
                    hover "toggle_2d_partial_hover"
                    action SetVariable("toggled_2d_mode", 2)
                else:
                    idle "toggle_2d_partial_disabled"
                    hover "toggle_2d_partial_disabled"
                    action NullAction()
        if toggled_2d_mode == 3:
            imagebutton:
                idle "toggle_2d_nude"
                hover "toggle_2d_nude"
                action NullAction()
        else:
            imagebutton:
                if persistent.art_unlocked_lvl3[current_2d_girl]:
                    idle "toggle_2d_nude_idle"
                    hover "toggle_2d_nude_hover"
                    action SetVariable("toggled_2d_mode", 3)
                else:
                    idle "toggle_2d_nude_disabled"
                    hover "toggle_2d_nude_disabled"
                    action NullAction()

screen ep7_card_jade_1:

    modal True tag reward_screen
    key "mouseup_2" action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    if toggled_2d_mode == 1:
        add "season2/rewards/ep7/ep7_reward_2d_jade.jpg"
    elif toggled_2d_mode == 2:
        add "season2/rewards/epX/epX_reward_2d_jade_2.jpg"
    else:
        add "season2/rewards/epX/epX_reward_2d_jade_3.jpg"

    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    hbox:
        xalign 0.02
        yalign 0.02
        if toggled_2d_mode == 1:
            imagebutton:
                idle "toggle_2d_clothed"
                hover "toggle_2d_clothed"
                action NullAction()
        else:
            imagebutton:
                idle "toggle_2d_clothed_idle"
                hover "toggle_2d_clothed_hover"
                action SetVariable("toggled_2d_mode", 1)
        if toggled_2d_mode == 2:
            imagebutton:
                idle "toggle_2d_partial"
                hover "toggle_2d_partial"
                action NullAction()
        else:
            imagebutton:
                if persistent.art_unlocked_lvl2[current_2d_girl]:
                    idle "toggle_2d_partial_idle"
                    hover "toggle_2d_partial_hover"
                    action SetVariable("toggled_2d_mode", 2)
                else:
                    idle "toggle_2d_partial_disabled"
                    hover "toggle_2d_partial_disabled"
                    action NullAction()
        if toggled_2d_mode == 3:
            imagebutton:
                idle "toggle_2d_nude"
                hover "toggle_2d_nude"
                action NullAction()
        else:
            imagebutton:
                if persistent.art_unlocked_lvl3[current_2d_girl]:
                    idle "toggle_2d_nude_idle"
                    hover "toggle_2d_nude_hover"
                    action SetVariable("toggled_2d_mode", 3)
                else:
                    idle "toggle_2d_nude_disabled"
                    hover "toggle_2d_nude_disabled"
                    action NullAction()

screen ep7_card_jill_1:

    modal True tag reward_screen
    key "mouseup_2" action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    if toggled_2d_mode == 1:
        add "season2/rewards/ep7/ep7_reward_2d_jill.jpg"
    elif toggled_2d_mode == 2:
        add "season2/rewards/epX/epX_reward_2d_jill_2.jpg"
    else:
        add "season2/rewards/epX/epX_reward_2d_jill_3.jpg"

    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    hbox:
        xalign 0.02
        yalign 0.02
        if toggled_2d_mode == 1:
            imagebutton:
                idle "toggle_2d_clothed"
                hover "toggle_2d_clothed"
                action NullAction()
        else:
            imagebutton:
                idle "toggle_2d_clothed_idle"
                hover "toggle_2d_clothed_hover"
                action SetVariable("toggled_2d_mode", 1)
        if toggled_2d_mode == 2:
            imagebutton:
                idle "toggle_2d_partial"
                hover "toggle_2d_partial"
                action NullAction()
        else:
            imagebutton:
                if persistent.art_unlocked_lvl2[current_2d_girl]:
                    idle "toggle_2d_partial_idle"
                    hover "toggle_2d_partial_hover"
                    action SetVariable("toggled_2d_mode", 2)
                else:
                    idle "toggle_2d_partial_disabled"
                    hover "toggle_2d_partial_disabled"
                    action NullAction()
        if toggled_2d_mode == 3:
            imagebutton:
                idle "toggle_2d_nude"
                hover "toggle_2d_nude"
                action NullAction()
        else:
            imagebutton:
                if persistent.art_unlocked_lvl3[current_2d_girl]:
                    idle "toggle_2d_nude_idle"
                    hover "toggle_2d_nude_hover"
                    action SetVariable("toggled_2d_mode", 3)
                else:
                    idle "toggle_2d_nude_disabled"
                    hover "toggle_2d_nude_disabled"
                    action NullAction()

screen ep7_card_josy_1:

    modal True tag reward_screen
    key "mouseup_2" action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    if toggled_2d_mode == 1:
        add "season2/rewards/ep7/ep7_reward_2d_josy.jpg"
    elif toggled_2d_mode == 2:
        add "season2/rewards/epX/epX_reward_2d_josy_2.jpg"
    else:
        add "season2/rewards/epX/epX_reward_2d_josy_3.jpg"

    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    hbox:
        xalign 0.02
        yalign 0.02
        if toggled_2d_mode == 1:
            imagebutton:
                idle "toggle_2d_clothed"
                hover "toggle_2d_clothed"
                action NullAction()
        else:
            imagebutton:
                idle "toggle_2d_clothed_idle"
                hover "toggle_2d_clothed_hover"
                action SetVariable("toggled_2d_mode", 1)
        if toggled_2d_mode == 2:
            imagebutton:
                idle "toggle_2d_partial"
                hover "toggle_2d_partial"
                action NullAction()
        else:
            imagebutton:
                if persistent.art_unlocked_lvl2[current_2d_girl]:
                    idle "toggle_2d_partial_idle"
                    hover "toggle_2d_partial_hover"
                    action SetVariable("toggled_2d_mode", 2)
                else:
                    idle "toggle_2d_partial_disabled"
                    hover "toggle_2d_partial_disabled"
                    action NullAction()
        if toggled_2d_mode == 3:
            imagebutton:
                idle "toggle_2d_nude"
                hover "toggle_2d_nude"
                action NullAction()
        else:
            imagebutton:
                if persistent.art_unlocked_lvl3[current_2d_girl]:
                    idle "toggle_2d_nude_idle"
                    hover "toggle_2d_nude_hover"
                    action SetVariable("toggled_2d_mode", 3)
                else:
                    idle "toggle_2d_nude_disabled"
                    hover "toggle_2d_nude_disabled"
                    action NullAction()

screen ep7_card_lily_1:

    modal True tag reward_screen
    key "mouseup_2" action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    if toggled_2d_mode == 1:
        add "season2/rewards/ep7/ep7_reward_2d_lily.jpg"
    elif toggled_2d_mode == 2:
        add "season2/rewards/ep8/ep8_reward_2d_lily_2.jpg"
    else:
        add "season2/rewards/epX/epX_reward_2d_lily_3.jpg"

    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    hbox:
        xalign 0.02
        yalign 0.02
        if toggled_2d_mode == 1:
            imagebutton:
                idle "toggle_2d_clothed"
                hover "toggle_2d_clothed"
                action NullAction()
        else:
            imagebutton:
                idle "toggle_2d_clothed_idle"
                hover "toggle_2d_clothed_hover"
                action SetVariable("toggled_2d_mode", 1)
        if toggled_2d_mode == 2:
            imagebutton:
                idle "toggle_2d_partial"
                hover "toggle_2d_partial"
                action NullAction()
        else:
            imagebutton:
                if persistent.art_unlocked_lvl2[current_2d_girl]:
                    idle "toggle_2d_partial_idle"
                    hover "toggle_2d_partial_hover"
                    action SetVariable("toggled_2d_mode", 2)
                else:
                    idle "toggle_2d_partial_disabled"
                    hover "toggle_2d_partial_disabled"
                    action NullAction()
        if toggled_2d_mode == 3:
            imagebutton:
                idle "toggle_2d_nude"
                hover "toggle_2d_nude"
                action NullAction()
        else:
            imagebutton:
                if persistent.art_unlocked_lvl3[current_2d_girl]:
                    idle "toggle_2d_nude_idle"
                    hover "toggle_2d_nude_hover"
                    action SetVariable("toggled_2d_mode", 3)
                else:
                    idle "toggle_2d_nude_disabled"
                    hover "toggle_2d_nude_disabled"
                    action NullAction()

screen ep7_card_maya_1:

    modal True tag reward_screen
    key "mouseup_2" action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    if toggled_2d_mode == 1:
        add "season2/rewards/ep7/ep7_reward_2d_maya.jpg"
    elif toggled_2d_mode == 2:
        add "season2/rewards/epX/epX_reward_2d_maya_2.jpg"
    else:
        add "season2/rewards/epX/epX_reward_2d_maya_3.jpg"

    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    hbox:
        xalign 0.02
        yalign 0.02
        if toggled_2d_mode == 1:
            imagebutton:
                idle "toggle_2d_clothed"
                hover "toggle_2d_clothed"
                action NullAction()
        else:
            imagebutton:
                idle "toggle_2d_clothed_idle"
                hover "toggle_2d_clothed_hover"
                action SetVariable("toggled_2d_mode", 1)
        if toggled_2d_mode == 2:
            imagebutton:
                idle "toggle_2d_partial"
                hover "toggle_2d_partial"
                action NullAction()
        else:
            imagebutton:
                if persistent.art_unlocked_lvl2[current_2d_girl]:
                    idle "toggle_2d_partial_idle"
                    hover "toggle_2d_partial_hover"
                    action SetVariable("toggled_2d_mode", 2)
                else:
                    idle "toggle_2d_partial_disabled"
                    hover "toggle_2d_partial_disabled"
                    action NullAction()
        if toggled_2d_mode == 3:
            imagebutton:
                idle "toggle_2d_nude"
                hover "toggle_2d_nude"
                action NullAction()
        else:
            imagebutton:
                if persistent.art_unlocked_lvl3[current_2d_girl]:
                    idle "toggle_2d_nude_idle"
                    hover "toggle_2d_nude_hover"
                    action SetVariable("toggled_2d_mode", 3)
                else:
                    idle "toggle_2d_nude_disabled"
                    hover "toggle_2d_nude_disabled"
                    action NullAction()

screen ep7_card_melanie_1:

    modal True tag reward_screen
    key "mouseup_2" action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    if toggled_2d_mode == 1:
        add "season2/rewards/ep7/ep7_reward_2d_melanie.jpg"
    elif toggled_2d_mode == 2:
        add "season2/rewards/epX/epX_reward_2d_melanie_2.jpg"
    else:
        add "season2/rewards/epX/epX_reward_2d_melanie_3.jpg"

    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    hbox:
        xalign 0.02
        yalign 0.02
        if toggled_2d_mode == 1:
            imagebutton:
                idle "toggle_2d_clothed"
                hover "toggle_2d_clothed"
                action NullAction()
        else:
            imagebutton:
                idle "toggle_2d_clothed_idle"
                hover "toggle_2d_clothed_hover"
                action SetVariable("toggled_2d_mode", 1)
        if toggled_2d_mode == 2:
            imagebutton:
                idle "toggle_2d_partial"
                hover "toggle_2d_partial"
                action NullAction()
        else:
            imagebutton:
                if persistent.art_unlocked_lvl2[current_2d_girl]:
                    idle "toggle_2d_partial_idle"
                    hover "toggle_2d_partial_hover"
                    action SetVariable("toggled_2d_mode", 2)
                else:
                    idle "toggle_2d_partial_disabled"
                    hover "toggle_2d_partial_disabled"
                    action NullAction()
        if toggled_2d_mode == 3:
            imagebutton:
                idle "toggle_2d_nude"
                hover "toggle_2d_nude"
                action NullAction()
        else:
            imagebutton:
                if persistent.art_unlocked_lvl3[current_2d_girl]:
                    idle "toggle_2d_nude_idle"
                    hover "toggle_2d_nude_hover"
                    action SetVariable("toggled_2d_mode", 3)
                else:
                    idle "toggle_2d_nude_disabled"
                    hover "toggle_2d_nude_disabled"
                    action NullAction()

screen ep7_card_quinn_1:

    modal True tag reward_screen
    key "mouseup_2" action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    if toggled_2d_mode == 1:
        add "season2/rewards/ep7/ep7_reward_2d_quinn.jpg"
    elif toggled_2d_mode == 2:
        add "season2/rewards/ep8/ep8_reward_2d_quinn_2.jpg"
    else:
        add "season2/rewards/epX/epX_reward_2d_quinn_3.jpg"

    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    hbox:
        xalign 0.02
        yalign 0.02
        if toggled_2d_mode == 1:
            imagebutton:
                idle "toggle_2d_clothed"
                hover "toggle_2d_clothed"
                action NullAction()
        else:
            imagebutton:
                idle "toggle_2d_clothed_idle"
                hover "toggle_2d_clothed_hover"
                action SetVariable("toggled_2d_mode", 1)
        if toggled_2d_mode == 2:
            imagebutton:
                idle "toggle_2d_partial"
                hover "toggle_2d_partial"
                action NullAction()
        else:
            imagebutton:
                if persistent.art_unlocked_lvl2[current_2d_girl]:
                    idle "toggle_2d_partial_idle"
                    hover "toggle_2d_partial_hover"
                    action SetVariable("toggled_2d_mode", 2)
                else:
                    idle "toggle_2d_partial_disabled"
                    hover "toggle_2d_partial_disabled"
                    action NullAction()
        if toggled_2d_mode == 3:
            imagebutton:
                idle "toggle_2d_nude"
                hover "toggle_2d_nude"
                action NullAction()
        else:
            imagebutton:
                if persistent.art_unlocked_lvl3[current_2d_girl]:
                    idle "toggle_2d_nude_idle"
                    hover "toggle_2d_nude_hover"
                    action SetVariable("toggled_2d_mode", 3)
                else:
                    idle "toggle_2d_nude_disabled"
                    hover "toggle_2d_nude_disabled"
                    action NullAction()

screen ep7_card_riona_1:

    modal True tag reward_screen
    key "mouseup_2" action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    if toggled_2d_mode == 1:
        add "season2/rewards/ep7/ep7_reward_2d_riona.jpg"
    elif toggled_2d_mode == 2:
        add "season2/rewards/ep8/ep8_reward_2d_riona_2.jpg"
    else:
        add "season2/rewards/epX/epX_reward_2d_riona_3.jpg"

    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    hbox:
        xalign 0.02
        yalign 0.02
        if toggled_2d_mode == 1:
            imagebutton:
                idle "toggle_2d_clothed"
                hover "toggle_2d_clothed"
                action NullAction()
        else:
            imagebutton:
                idle "toggle_2d_clothed_idle"
                hover "toggle_2d_clothed_hover"
                action SetVariable("toggled_2d_mode", 1)
        if toggled_2d_mode == 2:
            imagebutton:
                idle "toggle_2d_partial"
                hover "toggle_2d_partial"
                action NullAction()
        else:
            imagebutton:
                if persistent.art_unlocked_lvl2[current_2d_girl]:
                    idle "toggle_2d_partial_idle"
                    hover "toggle_2d_partial_hover"
                    action SetVariable("toggled_2d_mode", 2)
                else:
                    idle "toggle_2d_partial_disabled"
                    hover "toggle_2d_partial_disabled"
                    action NullAction()
        if toggled_2d_mode == 3:
            imagebutton:
                idle "toggle_2d_nude"
                hover "toggle_2d_nude"
                action NullAction()
        else:
            imagebutton:
                if persistent.art_unlocked_lvl3[current_2d_girl]:
                    idle "toggle_2d_nude_idle"
                    hover "toggle_2d_nude_hover"
                    action SetVariable("toggled_2d_mode", 3)
                else:
                    idle "toggle_2d_nude_disabled"
                    hover "toggle_2d_nude_disabled"
                    action NullAction()

screen ep7_card_sage_1:

    modal True tag reward_screen
    key "mouseup_2" action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    if toggled_2d_mode == 1:
        add "season2/rewards/ep7/ep7_reward_2d_sage.jpg"
    elif toggled_2d_mode == 2:
        add "season2/rewards/epX/epX_reward_2d_sage_2.jpg"
    else:
        add "season2/rewards/epX/epX_reward_2d_sage_3.jpg"

    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    hbox:
        xalign 0.02
        yalign 0.02
        if toggled_2d_mode == 1:
            imagebutton:
                idle "toggle_2d_clothed"
                hover "toggle_2d_clothed"
                action NullAction()
        else:
            imagebutton:
                idle "toggle_2d_clothed_idle"
                hover "toggle_2d_clothed_hover"
                action SetVariable("toggled_2d_mode", 1)
        if toggled_2d_mode == 2:
            imagebutton:
                idle "toggle_2d_partial"
                hover "toggle_2d_partial"
                action NullAction()
        else:
            imagebutton:
                if persistent.art_unlocked_lvl2[current_2d_girl]:
                    idle "toggle_2d_partial_idle"
                    hover "toggle_2d_partial_hover"
                    action SetVariable("toggled_2d_mode", 2)
                else:
                    idle "toggle_2d_partial_disabled"
                    hover "toggle_2d_partial_disabled"
                    action NullAction()
        if toggled_2d_mode == 3:
            imagebutton:
                idle "toggle_2d_nude"
                hover "toggle_2d_nude"
                action NullAction()
        else:
            imagebutton:
                if persistent.art_unlocked_lvl3[current_2d_girl]:
                    idle "toggle_2d_nude_idle"
                    hover "toggle_2d_nude_hover"
                    action SetVariable("toggled_2d_mode", 3)
                else:
                    idle "toggle_2d_nude_disabled"
                    hover "toggle_2d_nude_disabled"
                    action NullAction()

screen ep7_card_sarah_1:

    modal True tag reward_screen
    key "mouseup_2" action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    if toggled_2d_mode == 1:
        add "season2/rewards/ep7/ep7_reward_2d_sarah.jpg"
    elif toggled_2d_mode == 2:
        add "season2/rewards/ep8/ep8_reward_2d_sarah_2.jpg"
    else:
        add "season2/rewards/epX/epX_reward_2d_sarah_3.jpg"

    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action (SetVariable("toggled_2d_mode", 1),Hide("reward_screen"))

    hbox:
        xalign 0.02
        yalign 0.02
        if toggled_2d_mode == 1:
            imagebutton:
                idle "toggle_2d_clothed"
                hover "toggle_2d_clothed"
                action NullAction()
        else:
            imagebutton:
                idle "toggle_2d_clothed_idle"
                hover "toggle_2d_clothed_hover"
                action SetVariable("toggled_2d_mode", 1)
        if toggled_2d_mode == 2:
            imagebutton:
                idle "toggle_2d_partial"
                hover "toggle_2d_partial"
                action NullAction()
        else:
            imagebutton:
                if persistent.art_unlocked_lvl2[current_2d_girl]:
                    idle "toggle_2d_partial_idle"
                    hover "toggle_2d_partial_hover"
                    action SetVariable("toggled_2d_mode", 2)
                else:
                    idle "toggle_2d_partial_disabled"
                    hover "toggle_2d_partial_disabled"
                    action NullAction()
        if toggled_2d_mode == 3:
            imagebutton:
                idle "toggle_2d_nude"
                hover "toggle_2d_nude"
                action NullAction()
        else:
            imagebutton:
                if persistent.art_unlocked_lvl3[current_2d_girl]:
                    idle "toggle_2d_nude_idle"
                    hover "toggle_2d_nude_hover"
                    action SetVariable("toggled_2d_mode", 3)
                else:
                    idle "toggle_2d_nude_disabled"
                    hover "toggle_2d_nude_disabled"
                    action NullAction()


screen ep7_cardr1:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep7/ep7_reward_riona_1.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep7_cardr2:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep7/ep7_reward_riona_2.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep7_cardr3:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep7/ep7_reward_riona_3.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep7_cardr4:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep7/ep7_reward_riona_4.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep7_cardr5:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep7/ep7_reward_riona_5.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep7_cardr6:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep7/ep7_reward_riona_6.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep7_cardr7:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep7/ep7_reward_riona_7.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep7_cardr8:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep7/ep7_reward_riona_8.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep7_cardr9:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep7/ep7_reward_riona_9.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep7_cardr10:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep7/ep7_reward_riona_10.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep7_cardr11:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep7/ep7_reward_riona_11.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep7_cardr12:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep7/ep7_reward_riona_12.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep7_cardr13:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep7/ep7_reward_riona_13.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep7_cardr14:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep7/ep7_reward_riona_14.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep7_cardr15:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep7/ep7_reward_riona_15.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep7_cardr16:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep7/ep7_reward_riona_16.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")


screen ep7_cardj1:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep7/ep7_reward_jill_1.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep7_cardj2:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep7/ep7_reward_jill_2.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep7_cardj3:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep7/ep7_reward_jill_3.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep7_cardj4:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep7/ep7_reward_jill_4.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep7_cardj5:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep7/ep7_reward_jill_5.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep7_cardj6:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep7/ep7_reward_jill_6.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep7_cardj7:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep7/ep7_reward_jill_7.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep7_cardj8:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep7/ep7_reward_jill_8.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep7_cardj9:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep7/ep7_reward_jill_9.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep7_cardj10:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep7/ep7_reward_jill_10.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep7_cardj11:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep7/ep7_reward_jill_11.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep7_cardj12:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep7/ep7_reward_jill_12.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep7_cardj13:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep7/ep7_reward_jill_13.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep7_cardj14:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep7/ep7_reward_jill_14.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep7_cardj15:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep7/ep7_reward_jill_15.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep7_cardj16:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep7/ep7_reward_jill_16.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep7_cardj17:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep7/ep7_reward_jill_17.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep7_cardj18:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep7/ep7_reward_jill_18.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep7_cardj19:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep7/ep7_reward_jill_19.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")

screen ep7_cr1:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep7/ep7_reward_cr_1.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep7_cr2:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep7/ep7_reward_cr_2.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep7_cr3:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep7/ep7_reward_cr_3.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep7_cr4:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep7/ep7_reward_cr_4.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep7_cr5:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep7/ep7_reward_cr_5.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep7_cr6:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep7/ep7_reward_cr_6.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep7_cr7:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep7/ep7_reward_cr_7.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
screen ep7_cr8:

    modal True tag reward_screen
    key "mouseup_2" action Hide("reward_screen")
    add "season2/rewards/ep7/ep7_reward_cr_8.jpg"
    vbox xalign 0.5 yalign 0.5:
        imagebutton:
            focus_mask True
            idle Transform ("images/rewards/general/invisible_rew_button.png")
            hover Transform ("images/rewards/general/invisible_rew_button.png")
            action Hide("reward_screen")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
