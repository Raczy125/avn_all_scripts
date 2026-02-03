screen rewards_envy:
    tag menu
    add "rewards/general/rewards_new_bg.jpg"
    add "spr_crp1"
    add "spr_crp2"
    add "spr_crp3"
    add "spr_crp4"
    add "spr_crp5"
    add "spr_crp6"
    add "rewards/general/rew_envy2.jpg" xalign 0.0 yalign 0.9
    add "rewards/general/rewards_new_fg2.png"

    imagebutton:
        idle "rewards/general/rew_x_idle.png"
        hover "rewards/general/rew_x_hover.png"
        action ShowMenu("rewards")
        xalign 0.99
        yalign 0.00
    key "mouseup_2" action ShowMenu("rewards")
    text "Rewards - {color=#42f450}Envy{/color}" style "reward_header_style" xalign 0.02 yalign 0.004

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

        if persistent.ep6_carde1:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep6/rew_ep6_envy1.png")
                    hover Transform ("images/season2/rewards/ep6/rew_ep6_envy1_hover.png")
                    action (SetVariable("tmpInt2",0),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][0]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Ep 6 - Free roam" style "reward_locked_style"

        if persistent.ep6_carde2:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep6/rew_ep6_envy2.png")
                    hover Transform ("images/season2/rewards/ep6/rew_ep6_envy2_hover.png")
                    action (SetVariable("tmpInt2",1),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][1]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Ep 6 - Free roam" style "reward_locked_style"

        if persistent.ep6_carde3:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep6/rew_ep6_envy3.png")
                    hover Transform ("images/season2/rewards/ep6/rew_ep6_envy3_hover.png")
                    action (SetVariable("tmpInt2",2),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][2]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Ep 6 - Free roam" style "reward_locked_style"

        if persistent.ep6_carde4:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep6/rew_ep6_envy4.png")
                    hover Transform ("images/season2/rewards/ep6/rew_ep6_envy4_hover.png")
                    action (SetVariable("tmpInt2",3),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][3]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Ep 6 - Free roam" style "reward_locked_style"

        if persistent.ep6_carde5:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep6/rew_ep6_envy5.png")
                    hover Transform ("images/season2/rewards/ep6/rew_ep6_envy5_hover.png")
                    action (SetVariable("tmpInt2",4),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][4]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Ep 6 - Free roam" style "reward_locked_style"

        if persistent.ep6_carde6:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep6/rew_ep6_envy6.png")
                    hover Transform ("images/season2/rewards/ep6/rew_ep6_envy6_hover.png")
                    action (SetVariable("tmpInt2",5),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][5]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Ep 6 - Free roam" style "reward_locked_style"

        if persistent.ep6_carde7:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep6/rew_ep6_envy7.png")
                    hover Transform ("images/season2/rewards/ep6/rew_ep6_envy7_hover.png")
                    action (SetVariable("tmpInt2",6),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][6]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                if minigames:
                    text "Ep 6 - Shot game" style "reward_locked_style"
                else:
                    text "Ep 6 - Vault" style "reward_locked_style"

        if persistent.ep6_carde8:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep6/rew_ep6_envy8.png")
                    hover Transform ("images/season2/rewards/ep6/rew_ep6_envy8_hover.png")
                    action (SetVariable("tmpInt2",7),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][7]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                if minigames:
                    text "Ep 6 - Shot game" style "reward_locked_style"
                else:
                    text "Ep 6 - Vault" style "reward_locked_style"

        if persistent.ep6_carde9:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep6/rew_ep6_envy9.png")
                    hover Transform ("images/season2/rewards/ep6/rew_ep6_envy9_hover.png")
                    action (SetVariable("tmpInt2",8),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][8]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Ep 6 - Vault" style "reward_locked_style"

        if persistent.ep6_carde10:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep6/rew_ep6_envy10.png")
                    hover Transform ("images/season2/rewards/ep6/rew_ep6_envy10_hover.png")
                    action (SetVariable("tmpInt2",9),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][9]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Ep 6 - Vault" style "reward_locked_style"

        if persistent.ep6_carde11:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep6/rew_ep6_envy11.png")
                    hover Transform ("images/season2/rewards/ep6/rew_ep6_envy11_hover.png")
                    action (SetVariable("tmpInt2",10),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][10]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Ep 6 - Vault" style "reward_locked_style"

        if persistent.ep6_carde12:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep6/rew_ep6_envy12.png")
                    hover Transform ("images/season2/rewards/ep6/rew_ep6_envy12_hover.png")
                    action (SetVariable("tmpInt2",11),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][11]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Ep 6 - Vault" style "reward_locked_style"

        if persistent.ep6_carde1b:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep6/rew_ep6_envy1b.png")
                    hover Transform ("images/season2/rewards/ep6/rew_ep6_envy1b_hover.png")
                    action (SetVariable("tmpInt2",12),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][12]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Ep 6 - Free roam" style "reward_locked_style"

        if persistent.ep6_carde2b:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep6/rew_ep6_envy2b.png")
                    hover Transform ("images/season2/rewards/ep6/rew_ep6_envy2b_hover.png")
                    action (SetVariable("tmpInt2",13),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][13]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Ep 6 - Free roam" style "reward_locked_style"

        if persistent.ep6_carde3b:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep6/rew_ep6_envy3b.png")
                    hover Transform ("images/season2/rewards/ep6/rew_ep6_envy3b_hover.png")
                    action (SetVariable("tmpInt2",14),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][14]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Ep 6 - Free roam" style "reward_locked_style"

        if persistent.ep6_carde4b:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep6/rew_ep6_envy4b.png")
                    hover Transform ("images/season2/rewards/ep6/rew_ep6_envy4b_hover.png")
                    action (SetVariable("tmpInt2",15),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][15]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Ep 6 - Free roam" style "reward_locked_style"

        if persistent.ep6_carde5b:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep6/rew_ep6_envy5b.png")
                    hover Transform ("images/season2/rewards/ep6/rew_ep6_envy5b_hover.png")
                    action (SetVariable("tmpInt2",16),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][16]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Ep 6 - Free roam" style "reward_locked_style"

        if persistent.ep6_carde6b:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep6/rew_ep6_envy6b.png")
                    hover Transform ("images/season2/rewards/ep6/rew_ep6_envy6b_hover.png")
                    action (SetVariable("tmpInt2",17),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][17]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Ep 6 - Free roam" style "reward_locked_style"

        if persistent.ep6_carde7b:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep6/rew_ep6_envy7b.png")
                    hover Transform ("images/season2/rewards/ep6/rew_ep6_envy7b_hover.png")
                    action (SetVariable("tmpInt2",18),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][18]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                if minigames:
                    text "Ep 6 - Shot game" style "reward_locked_style"
                else:
                    text "Ep 6 - Vault" style "reward_locked_style"

        if persistent.ep6_carde8b:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep6/rew_ep6_envy8b.png")
                    hover Transform ("images/season2/rewards/ep6/rew_ep6_envy8b_hover.png")
                    action (SetVariable("tmpInt2",19),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][19]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                if minigames:
                    text "Ep 6 - Shot game" style "reward_locked_style"
                else:
                    text "Ep 6 - Vault" style "reward_locked_style"

        if persistent.ep6_carde9b:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep6/rew_ep6_envy9b.png")
                    hover Transform ("images/season2/rewards/ep6/rew_ep6_envy9b_hover.png")
                    action (SetVariable("tmpInt2",20),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][20]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Ep 6 - Vault" style "reward_locked_style"

        if persistent.ep6_carde10b:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep6/rew_ep6_envy10b.png")
                    hover Transform ("images/season2/rewards/ep6/rew_ep6_envy10b_hover.png")
                    action (SetVariable("tmpInt2",21),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][21]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Ep 6 - Vault" style "reward_locked_style"

        if persistent.ep6_carde11b:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep6/rew_ep6_envy11b.png")
                    hover Transform ("images/season2/rewards/ep6/rew_ep6_envy11b_hover.png")
                    action (SetVariable("tmpInt2",22),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][22]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Ep 6 - Vault" style "reward_locked_style"

        if persistent.ep6_carde12b:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep6/rew_ep6_envy12b.png")
                    hover Transform ("images/season2/rewards/ep6/rew_ep6_envy12b_hover.png")
                    action (SetVariable("tmpInt2",23),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][23]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Ep 6 - Vault" style "reward_locked_style"

        vbox xalign 0.5 yalign 0.5:
            add "gallery/disabled_btn.png"
            text "" style "reward_locked_style"
        vbox xalign 0.5 yalign 0.5:
            add "gallery/disabled_btn.png"
            text "" style "reward_locked_style"

        vbox xalign 0.5 yalign 0.5:
            add "gallery/disabled_btn.png"
            text "" style "reward_locked_style"
        vbox xalign 0.5 yalign 0.5:
            add "gallery/disabled_btn.png"
            text "" style "reward_locked_style"
        vbox xalign 0.5 yalign 0.5:
            add "gallery/disabled_btn.png"
            text "" style "reward_locked_style"
        vbox xalign 0.5 yalign 0.5:
            add "gallery/disabled_btn.png"
            text "" style "reward_locked_style"
        vbox xalign 0.5 yalign 0.5:
            add "gallery/disabled_btn.png"
            text "" style "reward_locked_style"

        vbox xalign 0.5 yalign 0.5:
            add "gallery/disabled_btn.png"
            text "" style "reward_locked_style"
        vbox xalign 0.5 yalign 0.5:
            add "gallery/disabled_btn.png"
            text "" style "reward_locked_style"
        vbox xalign 0.5 yalign 0.5:
            add "gallery/disabled_btn.png"
            text "" style "reward_locked_style"
        vbox xalign 0.5 yalign 0.5:
            add "gallery/disabled_btn.png"
            text "" style "reward_locked_style"
        vbox xalign 0.5 yalign 0.5:
            add "gallery/disabled_btn.png"
            text "" style "reward_locked_style"
        vbox xalign 0.5 yalign 0.5:
            add "gallery/disabled_btn.png"
            text "" style "reward_locked_style"
        vbox xalign 0.5 yalign 0.5:
            add "gallery/disabled_btn.png"
            text "" style "reward_locked_style"
        vbox xalign 0.5 yalign 0.5:
            add "gallery/disabled_btn.png"
            text "" style "reward_locked_style"
        vbox xalign 0.5 yalign 0.5:
            add "gallery/disabled_btn.png"
            text "" style "reward_locked_style"
        vbox xalign 0.5 yalign 0.5:
            add "gallery/disabled_btn.png"
            text "" style "reward_locked_style"
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
