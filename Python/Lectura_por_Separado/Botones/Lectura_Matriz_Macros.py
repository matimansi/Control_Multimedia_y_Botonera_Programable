import serial
import subprocess
import keyboard
import time

ruta_chrome = "C:/Program Files/Google/Chrome/Application/chrome.exe"
ruta_vscode = "C:/Users/Usuario/AppData/Local/Programs/Microsoft VS Code/Code.exe"
# ruta_yt_music = "C:/Program Files/Google/Chrome/Application/chrome_proxy.exe"
# ruta_ds = "C:/Users/Usuario/AppData/Local/Discord/Update.exe"
# ruta_notion = "C:/Users/Usuario/AppData/Local/Programs/Notion/Notion.exe"
# ruta_LTspice = "C:/Users/Usuario/AppData/Local/Programs/ADI/LTspice/LTspice.exe" 
# ruta_kicad = "C:/Program Files/KiCad/8.0/bin/kicad.exe"
# ruta_word = "C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE"

def macro_1():
	subprocess.Popen([ruta_chrome, "--profile-directory=Default"])

def macro_2():
	subprocess.Popen([ruta_chrome, "--profile-directory=Profile 2"])

def macro_3():
	subprocess.Popen([ruta_chrome, "--profile-directory=Default"])
	time.sleep(0.2)
	keyboard.write("https://github.com/matimansi")
	keyboard.press_and_release("enter")

def macro_4():
	keyboard.press_and_release('win+3')

def macro_5():
	keyboard.press_and_release('win+5')

def macro_6():
	keyboard.press_and_release('win+6')

def macro_7():
	subprocess.Popen([ruta_vscode])

def macro_8():
	keyboard.press_and_release('win+i')

esp = serial.Serial('COM5', 9600)

# Diccionario de macros
macros = {
    "macro_1": macro_1,
    "macro_2": macro_2,
    "macro_3": macro_3,
    "macro_4": macro_4,
    "macro_5": macro_5,
    "macro_6": macro_6,
    "macro_7": macro_7,
    "macro_8": macro_8,
}

while True:
    esp_leido = esp.readline().decode().rstrip()
    macro = esp_leido
    print(macro)
    if macro in macros:
        macros[macro]()
    else:
        print("Macro no reconocida:", repr(macro))
		