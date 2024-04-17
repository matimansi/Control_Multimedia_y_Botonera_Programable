import serial
from pycaw.pycaw import AudioUtilities

esp = serial.Serial('COM5', 9600)

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

while True:
	esp_leido = esp.readline().decode().rstrip()
	#print(esp_leido)
	vol = ["", "", "", ""]
	elementos = esp_leido.split("-")
	vol = [float(elemento) for elemento in elementos]
	print(vol)
	mezclador_volumen(vol)
