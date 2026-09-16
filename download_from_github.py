import tkinter as tk
import webbrowser


def download():
	webbrowser.open("https://github.com/szynkorowskiyt-tech/Subnautica-Ultimate-Modpack/releases")


def close():
	root.destroy()


root = tk.Tk()
root.title("Download Required")
root.geometry("450x220")
root.resizable(False, False)

title = tk.Label(
	root,
	text="Download Required",
	font=("Arial", 16, "bold")
)
title.pack(pady=(25, 10))

message = tk.Label(
	root,
	text="This file needs to be downloaded from GitHub.\nClick Download to open the download page.",
	font=("Arial", 11),
	justify="center"
)
message.pack(pady=10)

buttons = tk.Frame(root)
buttons.pack(pady=20)

download_button = tk.Button(
	buttons,
	text="Download",
	width=12,
	command=download
)
download_button.pack(side="left", padx=8)

close_button = tk.Button(
	buttons,
	text="Close",
	width=12,
	command=close
)
close_button.pack(side="left", padx=8)

root.mainloop()
