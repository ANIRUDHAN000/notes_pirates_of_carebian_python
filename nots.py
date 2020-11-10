import  musicalbeeps
from time import sleep
player = musicalbeeps.Player(volume=1, mute_output=False)
NOTS = ["ACDD", "DEFF", "FGEE", "DCCD", " ", "ACDD",
"DEFF",
"FGEE",
"DCD",
" ",
"ACDD",
"DFGG",
"GAA#A#",
"AGAD",
"DEFFGAD",
"DFEEFDE",
" ", 
"ACDD",
"DEFF",
"FGEE",
"DCCD",
" ", 
"ACDD",
"DEFF",
"FGEE",
"DCD",
" ",
'ACDD',
"DFGG",
"GAA#A#AGAD",
"DEFFGAD",
"DFEEDCD",
" ", 
"DEFFFGAFDA",
"A#A#GDA#",
"DDC#"]

def play(NOTS):
    for n in NOTS:
        sleep(.22)
        if n == " ":
            sleep(.28)
        else:
            for i in range(0,len(n)):
                try:
                    if n[i + 1] == "#" or n[i + 1] == "b":
                        x = n[i] + n[i + 1]
                        player.play_note(f"{x}4", 0.15)   
                        i +1
                        print(x)
                        continue
                except:
                    pass
                x = n[i]
                player.play_note(f"{x}4", 0.15)
play(NOTS)
