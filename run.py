import json
import requests
import os
import subprocess
import sys
import time

URL = "https://raw.githubusercontent.com/szynkorowskiyt-tech/Subnautica-Ultimate-Modpack/refs/heads/main/data.json"

# --- najpierw config (bo wait_time zależy od niego) ---
try:
    with open("config.json", "r") as file:
        config = json.load(file)
except FileNotFoundError:
    print("\nConfig file not found!")
    input("\nPress enter to continue...")
    sys.exit(1)

def wait():
    time.sleep(config.get("wait_time", 0.5))

print("\nIf errors/FAQ: https://leysmc.pl/files/myprojects/subnautica_eleton671_modpack/faq.html")
wait()

# --- pobieranie danych z internetu ---
try:
    data = requests.get(URL, timeout=10).json()
    wait()
except Exception as e:
    print(f"\nFailed to fetch update data: {e}")
    wait()
    input("\nPress enter to continue...")
    sys.exit(1)

# --- sprawdzanie aktualizacji ---
try:
    if data.get("version_number", 0) > config.get("version_number", 0):
        temp = input("\nNew Update Available! Download? True/False: ").strip()
        wait()

        if temp.lower() == "true":
            print("\nDownload from GitHub!")
            wait()
            input("\nPress enter to continue...")
            sys.exit(0)

        elif temp.lower() == "false":
            print("\nSkipping update...")
            wait()
        else:
            print("\nWrong Action!")
            wait()
except Exception as e:
    print(f"\nUpdate check error: {e}")
    wait()

print("\nYou can change any setting in file config.json!")
wait()

# --- sprawdzanie Steam ---
tasklist = subprocess.check_output("tasklist", text=True).lower()
wait()

if "steam.exe" not in tasklist:
    print("\nSteam is NOT running (please start Steam)!")
    wait()
    input("\nPress enter to continue...")
    sys.exit(1)

# --- sprawdzanie gry ---
if not os.path.exists("game/BepInEx"):
    print("\nBepInEx not found!")
    wait()
    input("\nPress enter to continue...")
    sys.exit(1)

# --- uruchomienie gry ---
game_path = "game/subnautica.exe"

if not os.path.exists(game_path):
    print("\ngame/subnautica.exe not found!")
    wait()
    input("\nPress enter to continue...")
    sys.exit(1)

try:
    os.startfile("game\\subnautica.exe")
    wait()
except Exception as e:
    print(f"\nFailed to launch game: {e}")
    wait()
    input("\nPress enter to continue...")
    sys.exit(1)
