'''
you'll need to make file in your TF2 Directory (tf/cfg) called autoexec.cfg if it doesnt exist, and add this to it:
    rcon_password (choose a password)
    net_start

after that, you need to add '-usercon' to your steam launch options for tf2
then change the '127.0.1.1' to '127.0.0.1' most likely
to check, do 'net_status' in the console, then it will say "Net Status for host" then the IP you need to enter.
after that, make sure you have python installed from here: https://www.python.org/downloads/release/python-3132/
then in that installer, make sure in the options "install pip", and "add to path" are checked (might be worded differently)
then, in a command prompt / terminal run "Python3 --version", if it says python then a version number, your goood
now run "pip install rcon" in a terminal.

Congrats, your done!

now just run this, then, once your out of the box(tm), 

if you have any issues, or the timing is off, contact Dessensce on Discord

also feel free to tinker with this, this is open source for a reason!

'''

import time
from rcon.source import Client

valid_positions = {
    "824.000000 -1144.000000",
    "568.000000 -1144.000000",
    "824.000000 -1216.000000",
    "568.000000 -1216.000000",
    "824.000000 -1280.000000",
    "568.000000 -1280.000000",
    "568.000000 -1088.000000",
    "824.000000 -1088.000000"
}

password = input("Please enter your rcon password:")

def Command(commandString):
    with Client('127.0.1.1', 27015, passwd=password) as client:
        client.run(commandString)
        
Command('spectate')
Command('jointeam auto')
time.sleep(1)
Command('joinclass engineer')
Command('unbind w; unbind a; unbind s; unbind d; unbind space; unbind ctrl')
time.sleep(0.5)
Command('slot3')

while True:
    pos = Command('getpos')

    posNoAng = pos.split(';')[0]
    TruePos = posNoAng.replace("setpos ", "")
    xy_pos = " ".join(TruePos.split()[:2])
    print(TruePos)
    if xy_pos in valid_positions:
        break
    else:
        Command('eureka_teleport 0')
        time.sleep(1)

Command('bind w +forward; bind a +moveleft; bind s +back; bind d +moveright; bind space +jump; bind ctrl +duck')
