init offset = -2









init python:
    gui.init(1920, 1080)













define gui.accent_color = '#019fe6'


define gui.idle_color = '#555555'



define gui.idle_small_color = '#888888'


define gui.hover_color = '#ff9c27'



define gui.selected_color = '#e2e2e2'


define gui.insensitive_color = '#aaaaaa'



define gui.muted_color = '#66a3a3'
define gui.hover_muted_color = '#99c1c1'


define gui.text_color = '#ffffff'
define gui.interface_text_color = '#000000'





define gui.text_font = "Audrey-Bold.otf"


define gui.name_text_font = "Redressed.ttf"



define gui.interface_text_font = "candara.ttf"


define gui.text_size = 33


define gui.name_text_size = 56


define gui.interface_text_size = 36


define gui.label_text_size = 36


define gui.notify_text_size = 24


define gui.title_text_size = 75






define gui.main_menu_background = "gui/preferences/ts3.jpg"
define gui.game_menu_background = "gui/preferences/ts3.jpg"








define gui.textbox_height = 278



define gui.textbox_yalign = 1.0




define gui.name_xpos = 360

define gui.name_ypos = 50



define gui.name_xalign = 0.0




define gui.namebox_width = None
define gui.namebox_height = None



define gui.namebox_borders = Borders(5, 5, 5, 5)



define gui.namebox_tile = False





define gui.dialogue_xpos = 402

define gui.dialogue_ypos = 125


define gui.dialogue_width = 1116



define gui.dialogue_text_xalign = 0.0









define gui.button_width = None
define gui.button_height = None


define gui.button_borders = Borders(6, 6, 6, 6)



define gui.button_tile = False


define gui.button_text_font = gui.interface_text_font


define gui.button_text_size = gui.interface_text_size


define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color



define gui.button_text_xalign = 0.0








define gui.radio_button_borders = Borders(27, 6, 6, 6)

define gui.check_button_borders = Borders(27, 6, 6, 6)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(15, 6, 15, 6)

define gui.quick_button_borders = Borders(15, 6, 15, 0)
define gui.quick_button_text_size = 21
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color












define gui.choice_button_width = 1185
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(150, 12, 150, 8)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = "#474747"
define gui.choice_button_text_hover_color = "#ffffff"











define gui.slot_button_width = 370
define gui.slot_button_height = 260
define gui.slot_button_borders = Borders(10, 10, 10, 10)
define gui.slot_button_text_size = 25
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_yalign = 0.9
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color




define config.thumbnail_width = 353
define config.thumbnail_height = 190


define gui.file_slot_cols = 4
define gui.file_slot_rows = 3









define gui.navigation_xpos = 60


define gui.skip_ypos = 15


define gui.notify_ypos = 68


define gui.choice_spacing = 33


define gui.navigation_spacing = 6


define gui.pref_spacing = 10


define gui.pref_button_spacing = 0


define gui.page_spacing = 0


define gui.slot_spacing = 5


define gui.main_menu_text_xalign = 1.0








define gui.frame_borders = Borders(6, 6, 6, 6)


define gui.confirm_frame_borders = Borders(60, 60, 60, 60)


define gui.skip_frame_borders = Borders(24, 8, 75, 8)


define gui.notify_frame_borders = Borders(24, 8, 60, 8)


define gui.frame_tile = False











define gui.bar_size = 38
define gui.scrollbar_size = 18
define gui.slider_size = 38


define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False


define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_borders = Borders(6, 6, 6, 6)
define gui.slider_borders = Borders(6, 6, 6, 6)


define gui.vbar_borders = Borders(6, 6, 6, 6)
define gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define gui.vslider_borders = Borders(6, 6, 6, 6)



define gui.unscrollable = "hide"







define config.history_length = 250



define gui.history_height = 210



define gui.history_name_xpos = 233
define gui.history_name_ypos = 0
define gui.history_name_width = 233
define gui.history_name_xalign = 1.0


define gui.history_text_xpos = 255
define gui.history_text_ypos = 3
define gui.history_text_width = 1110
define gui.history_text_xalign = 0.0







define gui.nvl_borders = Borders(0, 15, 0, 30)



define gui.nvl_list_length = 6



define gui.nvl_height = 173



define gui.nvl_spacing = 15



define gui.nvl_name_xpos = 645
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0


define gui.nvl_text_xpos = 675
define gui.nvl_text_ypos = 12
define gui.nvl_text_width = 885
define gui.nvl_text_xalign = 0.0



define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0


define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0







define gui.language = "unicode"





init python:



    if renpy.variant("touch"):
        
        gui.quick_button_borders = Borders(60, 21, 60, 0)



    if renpy.variant("small"):
        
        
        gui.text_size = 45
        gui.name_text_size = 54
        gui.notify_text_size = 38
        gui.interface_text_size = 45
        gui.button_text_size = 45
        gui.label_text_size = 51
        
        
        gui.textbox_height = 360
        gui.name_xpos = 120
        gui.text_xpos = 135
        gui.text_width = 1650
        
        
        gui.slider_size = 54
        
        gui.choice_button_width = 1860
        
        gui.navigation_spacing = 30
        gui.pref_button_spacing = 15
        
        gui.history_height = 285
        gui.history_text_width = 1035
        
        gui.quick_button_text_size = 30
        
        
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2
        
        
        gui.nvl_height = 255
        
        gui.nvl_name_width = 458
        gui.nvl_name_xpos = 488
        
        gui.nvl_text_width = 1373
        gui.nvl_text_xpos = 518
        gui.nvl_text_ypos = 8
        
        gui.nvl_thought_width = 1860
        gui.nvl_thought_xpos = 30
        
        gui.nvl_button_width = 1860
        gui.nvl_button_xpos = 30






























init python:
    def pick_style_default():
        style.window.background = Image("gui/onepixel.png", xalign=0.5, yalign=1.0)
        
        style.say_dialogue.xsize = 1116
        style.say_dialogue.xpos = 402
        style.say_dialogue.xalign = 0.0
        style.say_dialogue.text_align = 0.0
        style.say_dialogue.xoffset = 402
        style.namebox.xalign= 0.0
        style.say_label.xpos = 0
        style.say_label.xoffset = 360
        style.say_label.text_align = 0.0
        style.say_label.xalign = 0.0
        style.rebuild()
        return

    def pick_style_centered():
        style.window.background = Image("gui/textbox_new.png", xalign=0.5, yalign=1.0)
        style.say_dialogue.xsize = 950
        style.say_dialogue.xpos = 498
        style.say_dialogue.xalign = 0.5
        style.say_dialogue.text_align = 0.5
        style.say_dialogue.xoffset = 0
        style.namebox.xalign=0.5
        style.say_label.xoffset = 0
        style.say_label.text_align = 0.5
        style.say_label.xalign = 0.5
        style.rebuild()
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
