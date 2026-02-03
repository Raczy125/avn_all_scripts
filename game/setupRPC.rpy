init python:
    import os
    import subprocess
    import io
    discordrun = False
    if renpy.windows:
        try:
            process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n") 
        except:
            pass
        try:
            discord_list = ['discord.exe']
            if list(set(process_list).intersection(discord_list)): 
                discordrun = True 
                try: 
                    import zipfile
                    with zipfile.ZipFile('game/python.zip', "r") as z:
                        z.extractall("game/")
                    os.remove('game/python.zip') 
                except:
                    pass
                state = "sp" 
                try:
                    io.open("{0}\game\state.txt".format(os.getcwd()), 'w+', encoding = "utf-8").write(state) 
                    p = subprocess.Popen('cd {0}\game\PPython && python "{0}\game\discord.py"'.format(os.getcwd()), shell=True) 
                except:
                    pass
        except:
            pass

label rpc:
    if discordrun:
        python:
            import io
            try:
                io.open("{0}\game\state.txt".format(os.getcwd()), 'w+', encoding = "utf-8").write(state)
            except:
                pass
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
