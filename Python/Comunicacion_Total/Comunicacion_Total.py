import serial
import keyboard
from pycaw.pycaw import AudioUtilities
import subprocess

ruta_chrome = "C:/Program Files/Google/Chrome/Application/chrome.exe"
ruta_LTspice = "C:/Users/Usuario/AppData/Local/Programs/ADI/LTspice/LTspice.exe" 
ruta_word = "C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE"

def boton_1():
	subprocess.Popen([ruta_chrome])

def boton_2():
	subprocess.Popen([ruta_LTspice])

def boton_3():
	subprocess.Popen([ruta_word])

def subir_volumen():
	keyboard.send("volume_up")

def bajar_volumen():
	keyboard.send("volume_down")

def play_pause():
	keyboard.send('G')

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
		play_pause()
	elif esp_leido == "boton_1":
		boton_1()
	elif esp_leido == "boton_2":
		boton_2()
	elif esp_leido == "boton_3":
		boton_3()
	else:
		vol = ["", "", "", ""]
		elementos = esp_leido.split("-")
		vol = [float(elemento) for elemento in elementos]
		mezclador_volumen(vol)
