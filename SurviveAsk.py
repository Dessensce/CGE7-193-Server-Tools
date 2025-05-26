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
#import keyboard 
#probably gonna implement a killswitch soon, just been having issues with the keyboard lib on linux

password = input("Please enter your rcon password:")

def Command(commandString):
    with Client('127.0.1.1', 27015, passwd=password) as client:
        client.run(commandString)

Command('spectate')
Command('jointeam auto')
time.sleep(1)
Command('joinclass engineer')
time.sleep(0.5)

while True:
    Command('eureka_teleport 0')
    time.sleep(1)
