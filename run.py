import json, time, requests, os, subprocess, shutil

data = requests.get("https://raw.githubusercontent.com/szynkorowskiyt-tech/Subnautica-Ultimate-Modpack/refs/heads/main/data.json").json()

def wait(ms=1000):

    time.sleep(ms // 1000)

print("\nIf errors/FAQ: https://leysmc.pl/files/myprojects/subnautica_eleton671_modpack/faq.html")

wait(5000)

try:

    with open("config.json", "r") as file:

        config = json.load(file)

except FileNotFoundError:

    print("\nConfig file not found!")

    input("\nPress enter to continue...")

    exit()

wait()

while True:
    if data["version_number"] > config["version_number"]:
        temp = input("\nNew Update Available! Download? True/False: ")
        if temp == "True":
            print("\nDownload from github!")
            input("\nPress enter to continue...")
            exit(1)
        elif temp == "False":
            print("\nSkipping")
            break
        else:
            print("\nWrong Action!")
temp = None
wait()
print("You can change any setting in file config.json!")
wait()
if data[controller_support]
    shutil.copytree("game/bepinex", "", dirs_exist_ok=True)
if "steam.exe" in subprocess.check_output("tasklist", text=True).lower():
    print("\nsteam is not running (run steam)!")

    input("\nPress enter to continue...")

    exit()

if not os.path.exists("game/BepInEx"):
    print("\nBepInEx not found!")

    input("\nPress enter to continue...")

    exit()
try:
    os.startfile("game/subnautica.exe")

except FileNotFoundError:

    print("\ngame/subnautica.exe not found!")

    input("\nPress enter to continue...")

    exit()
