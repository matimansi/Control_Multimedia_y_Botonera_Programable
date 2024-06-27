import serial
import keyboard

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

esp = serial.Serial('COM5', 9600)

while True:
    esp_leido = esp.readline().decode().rstrip()
    print(esp_leido)
    if esp_leido == "1":
        subir_volumen()
    elif esp_leido == "-1":
        bajar_volumen()
    elif esp_leido == "boton_encoder":
        mutear()
        #play_pause()
        #cancion_sig()
        #cancion_ant()
