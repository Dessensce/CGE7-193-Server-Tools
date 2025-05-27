'''
make sure you have these librarys installed:
    python-a2s
    tkinter
    webbrowser
    time

install these with pip install python-a2s tkinter webbrowser time
'''


import a2s
import time
import tkinter as tk
import webbrowser

address = ("wavespray.dathost.net", 22912)

def open_rcon_setupinfo():
    print("opening")
    webbrowser.open("https://github.com/Dessensce/CGE7-193-Server-Tools/blob/main/RCON_Setup.md")  # Replace with your desired URL

def updateinfo():
    try:
        info = a2s.info(address, timeout=60)
        players = a2s.players(address, timeout=60)

        # Extract player names only
        player_names = [player.name for player in players]
        player_list_text = "\n".join(player_names) if player_names else "No players online"

        PlayerCount.config(text=f"{info.player_count}/{info.max_players} Players")
        CurrentMap.config(text=f"Current Map: {info.map_name}")
        PasswordEnabled.config(text=f"Password Enabled: {info.password_protected}")
        PlayerList.config(text=player_list_text)
    except Exception as e:
        CurrentMap.config(text="Error getting data")
        PlayerCount.config(text="Error getting data")
        PasswordEnabled.config(text="Error getting data")
        PlayerList.config(text="Error getting data")

    root.after(1000, updateinfo)

root = tk.Tk()
root.title("CGE7-193 Server Monitor")
root.geometry("300x300")  

Server_Name = tk.Label(root, text="cge7-193")
Server_Name.pack()  

PlayerCount = tk.Label(root, text="loading...")
PlayerCount.pack()  

CurrentMap = tk.Label(root, text="loading...")
CurrentMap.pack()  

PasswordEnabled = tk.Label(root, text="loading...")
PasswordEnabled.pack()  

ServerIP = tk.Label(root, text="Server IP: wavespray.dathost.net:22912\n")
ServerIP.pack()

PlayerList_info = tk.Label(root, text="Players:")
PlayerList_info.pack()

PlayerList = tk.Label(root, text="\nloading...")
PlayerList.pack()


root.resizable(False, False)

updateinfo()

# Start the GUI event loop
root.mainloop()



