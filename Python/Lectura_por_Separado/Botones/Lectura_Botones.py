import serial
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

esp = serial.Serial('COM5', 9600)

while True:
	esp_leido = esp.readline().decode().rstrip()
	botones = ["", "", ""]
	elementos = esp_leido.split("-")
	botones = [(elemento) for elemento in elementos]
	print(botones)
	if botones[0] == "1":
		boton_1()
	if botones[1] == "1":
		boton_2()
	if botones[2] == "1":
		boton_3()
