













define config.name = _("Being a DIK")





define gui.show_name = True




define config.version = "0.8.3"





define gui.about = _p("""
""")






define build.name = "BeingADIK"







define config.has_sound = True
define config.has_music = True
define config.has_voice = True













define config.main_menu_music = "music/patched/track_previous.mp3"










define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.intra_transition = dissolve




define config.after_load_transition = None




define config.end_game_transition = None















define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 0





default preferences.afm_time = 15


















define config.save_directory = "BeingaDIK-1535311494"
define config.default_fullscreen = False












define config.window_icon = "gui/window_icon.png"






init python:



















    build.archive("scripts", "all")
    build.archive("base", "all")
    build.archive("images", "all")
    build.archive("patched_movies", "all")
    build.archive("movies", "all")
    build.archive("gui", "all")
    build.archive("sound", "all")
    build.archive("sound_season2", "all")
    build.archive("gallery", "all")
    build.archive("patch_v042", "all")
    build.archive("movies_ep5", "all")
    build.archive("movies_ep6", "all")
    build.archive("movies_ep7", "all")
    build.archive("movies_ep8", "all")
    build.archive("gallery_season2", "all")
    build.archive("gui_season2", "all")
    build.archive("classes_season2", "all")

    build.archive("scripts_season2", "all")
    build.archive("patch_v051", "all")

    build.archive("music_ep1", "all")
    build.archive("music_ep2", "all")
    build.archive("music_ep3", "all")
    build.archive("music_ep4", "all")
    build.archive("music_ep5", "all")
    build.archive("music_ep6", "all")
    build.archive("music_ep7", "all")
    build.archive("music_ep8", "all")
    build.archive("ep1_images", "all")
    build.archive("ep2_images", "all")
    build.archive("ep3_images", "all")
    build.archive("ep4_images", "all")
    build.archive("ep5_images", "all")
    build.archive("ep6_images", "all")
    build.archive("ep7_images", "all")
    build.archive("ep8_images", "all")

    build.archive("walkthrough_season1", "all")
    build.archive("walkthrough_season2", "all")


    build.classify("game/walkthrough/season1/**.**", "None")
    build.classify("game/walkthrough/season2/**.**", "None")

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify("game/**.rpy", None)
    build.classify('**.docx', None)
    build.classify('**.txt', None)


    build.classify("game/images/classes/path_game/bugfix/**.**","archive")


    build.classify("game/music/ep8/**.**","music_ep8")
    build.classify("game/images/season2/ep8/**.**","ep8_images")
    build.classify("game/images/season2/rewards/ep8/**.**","ep8_images")
    build.classify("game/images/season2/movies/ep8/**.**","movies_ep8")


    build.classify("game/images/season2/new_phone/**.**","gui_season2")
    build.classify("game/images/season2/rewards/general/**.**","gui_season2")
    build.classify("game/music/ep7/**.**","music_ep7")
    build.classify("game/images/season2/ep7/**.**","ep7_images")
    build.classify("game/images/season2/rewards/ep7/**.**","ep7_images")
    build.classify("game/images/season2/movies/ep7/**.**","movies_ep7")
    build.classify("game/images/season2/classes/**.**", "classes_season2")


    build.classify("game/music/ep6/**.**","music_ep6")
    build.classify("game/images/season2/ep6/**.**","ep6_images")
    build.classify("game/images/season2/rewards/ep6/**.**","ep6_images")
    build.classify("game/images/season2/movies/ep6/**.**","movies_ep6")



    build.classify("game/images/season2/patched/**.**","patch_v051")


    build.classify("game/gui/main_menu_sprites/season2/**.**","gui_season2")
    build.classify("game/season2/**.**","scripts_season2")
    build.classify("game/sound_effects/season2/**.**","sound_season2")
    build.classify("game/music/ep5/**.**","music_ep5")
    build.classify("game/images/season2/ep5/**.**","ep5_images")
    build.classify("game/images/season2/rewards/ep5/**.**","ep5_images")
    build.classify("game/images/season2/movies/ep5/**.**","movies_ep5")
    build.classify("game/images/season2/gallery/**.**","gallery_season2")
    build.classify("game/images/season2/gui/**.**","gui_season2")


    build.classify("game/images/classes/tennis/tennis_tutorial.jpg", "patch_v042")
    build.classify("game/images/movies/patched/**.**","patch_v042")


    build.classify("game/*.rpyc", "scripts")
    build.classify("game/scripts/**.**", "scripts")
    build.classify("game/images/ep1/**.**", "ep1_images")
    build.classify("game/images/ep2/**.**", "ep2_images")
    build.classify("game/images/ep3/**.**", "ep3_images")
    build.classify("game/images/ep4/**.**", "ep4_images")
    build.classify("game/images/classes/**.**", "images")
    build.classify("game/images/freeroam_common/**.**", "images")
    build.classify("game/music/ep1/**.**","music_ep1")
    build.classify("game/music/ep2/**.**","music_ep2")
    build.classify("game/music/ep3/**.**","music_ep3")
    build.classify("game/music/ep4/**.**","music_ep4")
    build.classify("game/sound_effects/**.**","sound")
    build.classify("game/voice/**.**","sound")
    build.classify("game/images/rewards/**.**", "images")
    build.classify("game/images/movies/patched/**.**","patched_movies")
    build.classify("game/images/movies/**.**","movies")

    build.classify("game/images/gallery/**.**", "gallery")
    build.classify("game/images/gui/**.**", "gui")
    build.classify("game/gui/**.**", "gui")

    build.classify("game/**.png", "archive")
    build.classify("game/**.ico", "archive")
    build.classify("game/**.icns", "archive")
    build.classify("game/**.webm", "archive")

    build.classify("game/**.rpyc", "archive")
    build.classify("game/**.mp3", "archive")


    build.documentation('*.html')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
