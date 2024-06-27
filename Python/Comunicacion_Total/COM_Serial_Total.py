import serial
import time
from pycaw.pycaw import AudioUtilities
import subprocess
import keyboard

esp = serial.Serial('COM5', 9600)

ruta_chrome = "C:/Program Files/Google/Chrome/Application/chrome.exe"
ruta_vscode = "C:/Users/Usuario/AppData/Local/Programs/Microsoft VS Code/Code.exe"

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
	
def subir_volumen():
	keyboard.send("volume_up")

def bajar_volumen():
	keyboard.send("volume_down")

def mutear():
	keyboard.send("D")

def play_pause():
	keyboard.send('G')

def cancion_sig():
	keyboard.send('Q')

def cancion_ant():
	keyboard.send('P')
	
def mezclador_volumen(vol):
	sesiones = AudioUtilities.GetAllSessions()
	for sesion in sesiones:
		proceso = sesion.Process
		#print(proceso)
		if proceso:
			nombre_aplicacion = proceso.name()
			#print(nombre_aplicacion)
			if "chrome.exe" in nombre_aplicacion.lower():
				control_volumen = sesion.SimpleAudioVolume
				control_volumen.SetMasterVolume(vol[0], None)

			if "microsoft.media.player.exe" in nombre_aplicacion.lower():
				control_volumen = sesion.SimpleAudioVolume
				control_volumen.SetMasterVolume(vol[1], None)

			if "discord.exe" in nombre_aplicacion.lower():
				control_volumen = sesion.SimpleAudioVolume
				control_volumen.SetMasterVolume(vol[2], None)

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
	print(esp_leido)
	if esp_leido == "1":
		subir_volumen()
	elif esp_leido == "-1":
		bajar_volumen()
	elif esp_leido == "boton_encoder":
		mutear()
	elif esp_leido == "boton_multimedia_1":
		cancion_ant()
	elif esp_leido == "boton_multimedia_2":
		play_pause()
	elif esp_leido == "boton_multimedia_3":
		cancion_sig()
	elif esp_leido == "macro_1":
		macro_1()
	elif esp_leido == "macro_2":
		macro_2()
	elif esp_leido == "macro_3":
		macro_3()
	elif esp_leido == "macro_4":
		macro_4()
	elif esp_leido == "macro_5":
		macro_5()
	elif esp_leido == "macro_6":
		macro_6()
	elif esp_leido == "macro_7":
		macro_7()
	elif esp_leido == "macro_8":
		macro_8()
	else:
		vol = ["", "", "", ""]
		elementos = esp_leido.split("-")
		vol = [float(elemento) for elemento in elementos]
		mezclador_volumen(vol)