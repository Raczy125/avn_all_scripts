screen rewards_2d:
    tag menu
    add "rewards/general/rewards_new_bg.jpg"
    add "spr_crp1"
    add "spr_crp2"
    add "spr_crp3"
    add "spr_crp4"
    add "spr_crp5"
    add "spr_crp6"
    add "images/season2/rewards/general/rew_2d_art2.jpg" xalign 0.0 yalign 0.9
    add "rewards/general/rewards_new_fg2.png"

    imagebutton:
        idle "rewards/general/rew_x_idle.png"
        hover "rewards/general/rew_x_hover.png"
        action ShowMenu("rewards")
        xalign 0.99
        yalign 0.00
    key "mouseup_2" action ShowMenu("rewards")

    text "Rewards - {color=#67ed55}2D art{/color}" style "reward_header_style" xalign 0.02 yalign 0.004

    vpgrid:
        xalign 0.85
        ypos 0.14
        ysize 0.8
        cols 4
        spacing 10
        draggable True
        mousewheel True

        scrollbars "vertical"
        side_xalign 0.5

        for x in range(0,len(art_girl_name_list)):
            if persistent.art_unlocked_lvl1[x]:
                vbox xalign 0.5 yalign 0.5:
                    imagebutton:
                        focus_mask True
                        idle Transform ("images/season2/rewards/ep7/rew_ep7_2d_"+art_girl_name_list[x].lower()+".png")
                        hover Transform ("images/season2/rewards/ep7/rew_ep7_2d_"+art_girl_name_list[x].lower()+"_hover.png")

                        action (SetVariable("tmpInt2",x),Show("rewards_renders_screen"))
                    if persistent.rewards_seen_list[tmpInt][x][0] or (persistent.rewards_seen_list[tmpInt][x][1] and persistent.art_unlocked_lvl2[x]) or (persistent.rewards_seen_list[tmpInt][x][2] and persistent.art_unlocked_lvl3[x]):
                        text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                    else:
                        text "" style "reward_new_style"
            else:
                vbox xalign 0.5 yalign 0.5:
                    add "gallery/locked.png"
                    text "2D art shop" style "reward_locked_style"

        if persistent.ep7_wpi1:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep7/ep7_wallpaper_isabella_1a_idle.png")
                    hover Transform ("images/season2/rewards/ep7/ep7_wallpaper_isabella_1a_hover.png")
                    action (SetVariable("tmpInt2",len(art_girl_name_list)),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(art_girl_name_list)]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Isabella - Ep 7" style "reward_locked_style"

        if persistent.ep7_wpi2:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep7/ep7_wallpaper_isabella_2a_idle.png")
                    hover Transform ("images/season2/rewards/ep7/ep7_wallpaper_isabella_2a_hover.png")
                    action (SetVariable("tmpInt2",len(art_girl_name_list)+1),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(art_girl_name_list)+1]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Isabella - Ep 7" style "reward_locked_style"

        if persistent.ep7_wpj1:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep7/ep7_wallpaper_jill_1a_idle.png")
                    hover Transform ("images/season2/rewards/ep7/ep7_wallpaper_jill_1a_hover.png")
                    action (SetVariable("tmpInt2",len(art_girl_name_list)+2),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(art_girl_name_list)+2]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Jill - Ep 7" style "reward_locked_style"

        if persistent.ep7_wpj2:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep7/ep7_wallpaper_jill_2a_idle.png")
                    hover Transform ("images/season2/rewards/ep7/ep7_wallpaper_jill_2a_hover.png")
                    action (SetVariable("tmpInt2",len(art_girl_name_list)+3),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(art_girl_name_list)+3]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Jill - Ep 7" style "reward_locked_style"

        if persistent.ep7_wpjo1:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep7/ep7_wallpaper_josy_1a_idle.png")
                    hover Transform ("images/season2/rewards/ep7/ep7_wallpaper_josy_1a_hover.png")
                    action (SetVariable("tmpInt2",len(art_girl_name_list)+4),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(art_girl_name_list)+4]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Josy - Ep 7" style "reward_locked_style"

        if persistent.ep7_wpjo2:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep7/ep7_wallpaper_josy_2a_idle.png")
                    hover Transform ("images/season2/rewards/ep7/ep7_wallpaper_josy_2a_hover.png")
                    action (SetVariable("tmpInt2",len(art_girl_name_list)+5),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(art_girl_name_list)+5]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Josy - Ep 7" style "reward_locked_style"

        if persistent.ep7_wpm1:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep7/ep7_wallpaper_maya_1a_idle.png")
                    hover Transform ("images/season2/rewards/ep7/ep7_wallpaper_maya_1a_hover.png")
                    action (SetVariable("tmpInt2",len(art_girl_name_list)+6),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(art_girl_name_list)+6]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Maya - Ep 7" style "reward_locked_style"

        if persistent.ep7_wpm2:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep7/ep7_wallpaper_maya_2a_idle.png")
                    hover Transform ("images/season2/rewards/ep7/ep7_wallpaper_maya_2a_hover.png")
                    action (SetVariable("tmpInt2",len(art_girl_name_list)+7),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(art_girl_name_list)+7]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Maya - Ep 7" style "reward_locked_style"

        if persistent.ep7_wps1:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep7/ep7_wallpaper_sage_1a_idle.png")
                    hover Transform ("images/season2/rewards/ep7/ep7_wallpaper_sage_1a_hover.png")
                    action (SetVariable("tmpInt2",len(art_girl_name_list)+8),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(art_girl_name_list)+8]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Sage - Ep 7" style "reward_locked_style"

        if persistent.ep7_wps2:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep7/ep7_wallpaper_sage_2a_idle.png")
                    hover Transform ("images/season2/rewards/ep7/ep7_wallpaper_sage_2a_hover.png")
                    action (SetVariable("tmpInt2",len(art_girl_name_list)+9),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(art_girl_name_list)+9]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Sage - Ep 7" style "reward_locked_style"

        if persistent.ep8_wpi1:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep8/ep8_wallpaper_isabella_1a_idle.png")
                    hover Transform ("images/season2/rewards/ep8/ep8_wallpaper_isabella_1a_hover.png")
                    action (SetVariable("tmpInt2",len(art_girl_name_list)+10),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(art_girl_name_list)+10]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Isabella - Ep 8" style "reward_locked_style"

        if persistent.ep8_wpj1:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep8/ep8_wallpaper_jill_1a_idle.png")
                    hover Transform ("images/season2/rewards/ep8/ep8_wallpaper_jill_1a_hover.png")
                    action (SetVariable("tmpInt2",len(art_girl_name_list)+11),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(art_girl_name_list)+11]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Jill - Ep 8" style "reward_locked_style"

        if persistent.ep8_wpjo1:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep8/ep8_wallpaper_josy_1a_idle.png")
                    hover Transform ("images/season2/rewards/ep8/ep8_wallpaper_josy_1a_hover.png")
                    action (SetVariable("tmpInt2",len(art_girl_name_list)+12),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(art_girl_name_list)+12]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Josy - Ep 8" style "reward_locked_style"

        if persistent.ep8_wpm1:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep8/ep8_wallpaper_maya_1a_idle.png")
                    hover Transform ("images/season2/rewards/ep8/ep8_wallpaper_maya_1a_hover.png")
                    action (SetVariable("tmpInt2",len(art_girl_name_list)+13),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(art_girl_name_list)+13]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Maya - Ep 8" style "reward_locked_style"

        if persistent.ep8_wpq1:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep8/ep8_wallpaper_quinn_1a_idle.png")
                    hover Transform ("images/season2/rewards/ep8/ep8_wallpaper_quinn_1a_hover.png")
                    action (SetVariable("tmpInt2",len(art_girl_name_list)+14),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(art_girl_name_list)+14]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Quinn - Ep 8" style "reward_locked_style"

        if persistent.ep8_wps1:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep8/ep8_wallpaper_sage_1a_idle.png")
                    hover Transform ("images/season2/rewards/ep8/ep8_wallpaper_sage_1a_hover.png")
                    action (SetVariable("tmpInt2",len(art_girl_name_list)+15),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(art_girl_name_list)+15]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Sage - Ep 8" style "reward_locked_style"

        if persistent.ep8_wpe1:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep8/ep8_wallpaper_envy_1a_idle.png")
                    hover Transform ("images/season2/rewards/ep8/ep8_wallpaper_envy_1a_hover.png")
                    action (SetVariable("tmpInt2",len(art_girl_name_list)+16),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(art_girl_name_list)+16]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Envy & Lily - Ep 8" style "reward_locked_style"

        if persistent.ep8_wpjade1:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep8/ep8_wallpaper_jade_1a_idle.png")
                    hover Transform ("images/season2/rewards/ep8/ep8_wallpaper_jade_1a_hover.png")
                    action (SetVariable("tmpInt2",len(art_girl_name_list)+17),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(art_girl_name_list)+17]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Jade - Ep 8" style "reward_locked_style"

        if persistent.ep8_wpmad1:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep8/ep8_wallpaper_madame_1a_idle.png")
                    hover Transform ("images/season2/rewards/ep8/ep8_wallpaper_madame_1a_hover.png")
                    action (SetVariable("tmpInt2",len(art_girl_name_list)+18),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(art_girl_name_list)+18]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "{size=-5}Madame Rose - Ep 8{/size}" style "reward_locked_style"

        vbox xalign 0.5 yalign 0.5:
            add "gallery/disabled_btn.png"
            text "" style "reward_locked_style"
        vbox xalign 0.5 yalign 0.5:
            add "gallery/disabled_btn.png"
            text "" style "reward_locked_style"
        vbox xalign 0.5 yalign 0.5:
            add "gallery/disabled_btn.png"
            text "" style "reward_locked_style"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
