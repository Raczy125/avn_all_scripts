label after_load:

    if discordrun:
        python:
            try:
                import io
                import os
                io.open("game/state.txt", 'w+', encoding = "utf-8").write(state)
            except:
                import io
                try:
                    open("game/state.txt", 'w+')
                    io.open("game/state.txt", 'w+', encoding = "utf-8").write("err3")
                    state = "err3"
                except:
                    pass

    return

label before_main_menu:

    if discordrun:
        python:
            import io
            state = "mm"
            try:
                io.open("game/state.txt", 'w+', encoding = "utf-8").write(state)
            except:
                pass

    return

label quit:

    if discordrun:
        python:
            import os
            os.popen('taskkill /f /im python.exe')

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
