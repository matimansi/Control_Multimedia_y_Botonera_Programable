import serial
import keyboard
from pycaw.pycaw import AudioUtilities
import subprocess

ruta_chrome = "C:/Program Files/Google/Chrome/Application/chrome.exe"

ruta_yt_music = "C:/Program Files/Google/Chrome/Application/chrome_proxy.exe"

ruta_ds = "C:/Users/Usuario/AppData/Local/Discord/Update.exe"

ruta_vscode = "C:/Users/Usuario/AppData/Local/Programs/Microsoft VS Code/Code.exe"

ruta_notion = "C:/Users/Usuario/AppData/Local/Programs/Notion/Notion.exe"

ruta_LTspice = "C:/Users/Usuario/AppData/Local/Programs/ADI/LTspice/LTspice.exe" 

ruta_kicad = "C:/Program Files/KiCad/8.0/bin/kicad.exe"

ruta_word = "C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE"

def boton_macro_1():
	subprocess.Popen([ruta_chrome])

def boton_macro_2():
	#subprocess.Popen([ruta_yt_music])
	keyboard.press_and_release('win+2')

def boton_macro_3():
	#subprocess.Popen([ruta_ds])
	keyboard.press_and_release('win+5')

def boton_macro_4():
	subprocess.Popen([ruta_vscode])

def boton_macro_5():
	subprocess.Popen([ruta_notion])

def boton_macro_6():
	subprocess.Popen([ruta_LTspice])

def boton_macro_7():
	subprocess.Popen([ruta_kicad])

def boton_macro_8():
	subprocess.Popen([ruta_word])

def boton_multimedia_1():
	# Cancion Anterior
	keyboard.send('Q')

def boton_multimedia_2():
	# Play / Pausa
	keyboard.send('G')

def boton_multimedia_3():
	# Cancion Siguiente
	keyboard.send('P')

def subir_volumen():
	keyboard.send("volume_up")

def bajar_volumen():
	keyboard.send("volume_down")
	
def mute():
	keyboard.send('D')

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

			if "ms-teams.exe" in nombre_aplicacion.lower():
				control_volumen = sesion.SimpleAudioVolume
				control_volumen.SetMasterVolume(vol[2], None)

esp = serial.Serial('COM5', 9600)

while True:
	esp_leido = esp.readline().decode().rstrip()
	print(esp_leido)
	
	if esp_leido == "1":
		subir_volumen()
	elif esp_leido == "-1":
		bajar_volumen()
	elif esp_leido == "boton_encoder":
		mute()
	elif esp_leido == "boton_multimedia_1":
		boton_multimedia_1()
	elif esp_leido == "boton_multimedia_2":
		boton_multimedia_2()
	elif esp_leido == "boton_multimedia_3":
		boton_multimedia_3()
	elif esp_leido == "boton_macro_1":
		boton_macro_1()
	elif esp_leido == "boton_macro_2":
		boton_macro_2()
	elif esp_leido == "boton_macro_3":
		boton_macro_3()
	elif esp_leido == "boton_macro_4":
		boton_macro_4()
	elif esp_leido == "boton_macro_5":
		boton_macro_5()
	elif esp_leido == "boton_macro_6":
		boton_macro_6()
	elif esp_leido == "boton_macro_7":
		boton_macro_7()
	elif esp_leido == "boton_macro_8":
		boton_macro_8()
	else:
		vol = ["", "", "", ""]
		elementos = esp_leido.split("-")
		vol = [float(elemento) for elemento in elementos]
		mezclador_volumen(vol)
