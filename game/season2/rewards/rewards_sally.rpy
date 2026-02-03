screen rewards_sally:
    tag menu
    add "rewards/general/rewards_new_bg.jpg"
    add "spr_crp1"
    add "spr_crp2"
    add "spr_crp3"
    add "spr_crp4"
    add "spr_crp5"
    add "spr_crp6"
    add "rewards/general/rew_sally2.jpg" xalign 0.0 yalign 0.9
    add "rewards/general/rewards_new_fg2.png"

    imagebutton:
        idle "rewards/general/rew_x_idle.png"
        hover "rewards/general/rew_x_hover.png"
        action ShowMenu("rewards")
        xalign 0.99
        yalign 0.00
    key "mouseup_2" action ShowMenu("rewards")

    text "Rewards - {color=#BCB88A}Sally{/color}" style "reward_header_style" xalign 0.02 yalign 0.004

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

        if persistent.ep8_cards1:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep8/rew_ep8_sally1.png")
                    hover Transform ("images/season2/rewards/ep8/rew_ep8_sally1_hover.png")
                    action (SetVariable("tmpInt2",0),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][0]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Ep 8 - Free roam" style "reward_locked_style"

        if persistent.ep8_cards2:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep8/rew_ep8_sally2.png")
                    hover Transform ("images/season2/rewards/ep8/rew_ep8_sally2_hover.png")
                    action (SetVariable("tmpInt2",1),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][1]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Ep 8 - Free roam" style "reward_locked_style"

        if persistent.ep8_cards3:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep8/rew_ep8_sally3.png")
                    hover Transform ("images/season2/rewards/ep8/rew_ep8_sally3_hover.png")
                    action (SetVariable("tmpInt2",2),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][2]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                if not minigames:
                    text "Ep 8 - Vault" style "reward_locked_style"
                else:
                    text "Ep 8 - Brawler" style "reward_locked_style"

        if persistent.ep8_cards4:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep8/rew_ep8_sally4.png")
                    hover Transform ("images/season2/rewards/ep8/rew_ep8_sally4_hover.png")
                    action (SetVariable("tmpInt2",3),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][3]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Ep 8 - Free roam" style "reward_locked_style"

        if persistent.ep8_cards5:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep8/rew_ep8_sally5.png")
                    hover Transform ("images/season2/rewards/ep8/rew_ep8_sally5_hover.png")
                    action (SetVariable("tmpInt2",4),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][4]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Ep 8 - Free roam" style "reward_locked_style"

        if persistent.ep8_cards6:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep8/rew_ep8_sally6.png")
                    hover Transform ("images/season2/rewards/ep8/rew_ep8_sally6_hover.png")
                    action (SetVariable("tmpInt2",5),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][5]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Ep 8 - Free roam" style "reward_locked_style"

        if persistent.ep8_cards7:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep8/rew_ep8_sally7.png")
                    hover Transform ("images/season2/rewards/ep8/rew_ep8_sally7_hover.png")
                    action (SetVariable("tmpInt2",6),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][6]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Ep 8 - Free roam" style "reward_locked_style"

        if persistent.ep8_cards8:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep8/rew_ep8_sally8.png")
                    hover Transform ("images/season2/rewards/ep8/rew_ep8_sally8_hover.png")
                    action (SetVariable("tmpInt2",7),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][7]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Ep 8 - Free roam" style "reward_locked_style"

        if persistent.ep8_cards9:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep8/rew_ep8_sally9.png")
                    hover Transform ("images/season2/rewards/ep8/rew_ep8_sally9_hover.png")
                    action (SetVariable("tmpInt2",8),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][8]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Ep 8 - Free roam" style "reward_locked_style"

        if persistent.ep8_cards10:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep8/rew_ep8_sally10.png")
                    hover Transform ("images/season2/rewards/ep8/rew_ep8_sally10_hover.png")
                    action (SetVariable("tmpInt2",9),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][9]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                if not minigames:
                    text "Ep 8 - Vault" style "reward_locked_style"
                else:
                    text "Ep 8 - Brawler" style "reward_locked_style"

        if persistent.ep8_cards11:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep8/rew_ep8_sally11.png")
                    hover Transform ("images/season2/rewards/ep8/rew_ep8_sally11_hover.png")
                    action (SetVariable("tmpInt2",10),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][10]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                if not minigames:
                    text "Ep 8 - Vault" style "reward_locked_style"
                else:
                    text "Math class" style "reward_locked_style"

        if persistent.ep8_cards12:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep8/rew_ep8_sally12.png")
                    hover Transform ("images/season2/rewards/ep8/rew_ep8_sally12_hover.png")
                    action (SetVariable("tmpInt2",11),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][11]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                if not minigames:
                    text "Ep 8 - Vault" style "reward_locked_style"
                else:
                    text "Gender Studies" style "reward_locked_style"

        if persistent.ep8_cards13:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep8/rew_ep8_sally13.png")
                    hover Transform ("images/season2/rewards/ep8/rew_ep8_sally13_hover.png")
                    action (SetVariable("tmpInt2",12),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][12]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                if not minigames:
                    text "Ep 8 - Vault" style "reward_locked_style"
                else:
                    text "English class" style "reward_locked_style"

        if persistent.ep8_cards14:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep8/rew_ep8_sally14.png")
                    hover Transform ("images/season2/rewards/ep8/rew_ep8_sally14_hover.png")
                    action (SetVariable("tmpInt2",13),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][13]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Ep 8 - Free roam" style "reward_locked_style"

        if persistent.ep8_cards15:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep8/rew_ep8_sally15.png")
                    hover Transform ("images/season2/rewards/ep8/rew_ep8_sally15_hover.png")
                    action (SetVariable("tmpInt2",14),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][14]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Ep 8 - Vault" style "reward_locked_style"

        if persistent.ep8_cards16:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep8/rew_ep8_sally16.png")
                    hover Transform ("images/season2/rewards/ep8/rew_ep8_sally16_hover.png")
                    action (SetVariable("tmpInt2",15),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][15]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Ep 8 - Vault" style "reward_locked_style"

        if persistent.ep8_cards17:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep8/rew_ep8_sally17.png")
                    hover Transform ("images/season2/rewards/ep8/rew_ep8_sally17_hover.png")
                    action (SetVariable("tmpInt2",16),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][16]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Ep 8 - Vault" style "reward_locked_style"

        if persistent.ep8_cards18:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep8/rew_ep8_sally18.png")
                    hover Transform ("images/season2/rewards/ep8/rew_ep8_sally18_hover.png")
                    action (SetVariable("tmpInt2",17),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][17]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Ep 8 - Vault" style "reward_locked_style"

        if persistent.ep8_cards19:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("images/season2/rewards/ep8/rew_ep8_sally19.png")
                    hover Transform ("images/season2/rewards/ep8/rew_ep8_sally19_hover.png")
                    action (SetVariable("tmpInt2",18),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][18]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "gallery/locked.png"
                text "Ep 8 - Vault" style "reward_locked_style"

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
