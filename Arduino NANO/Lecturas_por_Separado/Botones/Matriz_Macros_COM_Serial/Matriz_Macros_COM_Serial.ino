#include <Keypad.h>

const byte FILAS = 2;
const byte COLUMNAS = 4;

char macros[FILAS][COLUMNAS] =
{
    {'1', '2', '3', '4'},
    {'5', '6', '7', '8'}
};

byte pines_filas[FILAS] = {8, 7};
byte pines_columnas[COLUMNAS] = {9, 10, 11, 12};

Keypad matriz_macros = Keypad(makeKeymap(macros), pines_filas, pines_columnas, FILAS, COLUMNAS);

void setup() 
{
    Serial.begin(9600);
}

void loop() 
{
    char boton_macro = matriz_macros.getKey();

    if (boton_macro)
    {
        Serial.print("macro_");
        Serial.println(boton_macro);
    }
}
