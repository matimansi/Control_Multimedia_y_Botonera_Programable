/*
    BIBLIOTECAS
*/

#include <Keypad.h>

/*
    DEFINES ENCODER
*/

#define DT 4
#define CLK 2
#define BOTON_ENCODER 3

/*
    DEFINES POTES
*/

#define POTE_1 A0
#define POTE_2 A1
#define POTE_3 A2
#define POTE_4 A3
#define CANT_POTES 4

/*
    DEFINES BOTONES MULTIMEDIA
*/

#define BOTON_MULTIMEDIA_1 13
#define BOTON_MULTIMEDIA_2 6
#define BOTON_MULTIMEDIA_3 5
#define CANT_BOTONES_MULTIMEDIA 3

/*
    DEFINES TIEMPOS
*/

#define TIEMPO_INFO 100

/*
    DECLARACION MATRIZ DE BOTONES MACRO
*/

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

/*
    VARIABLES GLOBALES
*/

bool old_clk;
volatile bool dt = 0;
volatile int encoder_output = 0;
volatile bool flag_encoder = false, flag_boton_encoder = false;
bool flag_if_encoder = false;

float old_volumen[CANT_POTES];

bool botones_multimedia[CANT_BOTONES_MULTIMEDIA] = {0};
bool flags[CANT_BOTONES_MULTIMEDIA] = {false, false, false};

unsigned long tiempo_actual;

/*
    PROTOTIPOS FUNCIONES
*/

void encoder_interrup(void);
void boton_encoder_interrup(void);

float lectura_pote_1(void);
float lectura_pote_2(void);
float lectura_pote_3(void);
float lectura_pote_4(void);
float conversor_lectura_volumen(float);

void com_botones_multimedia (void);
void lectura_botones_multimedia (void);

void botones_macros (void);


void setup()
{
	pinMode(DT, INPUT);
	pinMode(CLK, INPUT);
	pinMode(BOTON_ENCODER, INPUT);
	pinMode(POTE_1, INPUT);
	pinMode(POTE_2, INPUT);
	pinMode(POTE_3, INPUT);
    pinMode(POTE_4, INPUT);
	pinMode(BOTON_MULTIMEDIA_1, INPUT);
    pinMode(BOTON_MULTIMEDIA_1, INPUT);
    pinMode(BOTON_MULTIMEDIA_1, INPUT);

	attachInterrupt(digitalPinToInterrupt(CLK), encoder_interrup, FALLING);
	attachInterrupt(digitalPinToInterrupt(BOTON_ENCODER), boton_encoder_interrup, FALLING);

    Serial.begin(9600);

	tiempo_actual = millis();
	old_clk = digitalRead(CLK);
}

void loop()
{
	float volumen[CANT_POTES];
    
    botones_macros();

    com_botones_multimedia();
    
    if ((millis() - tiempo_actual) > TIEMPO_INFO)
    {
        volumen[0] = lectura_pote_1();
        volumen[1] = lectura_pote_2();
        volumen[2] = lectura_pote_3();
        volumen[3] = lectura_pote_4();

        Serial.print(volumen[0]);
        Serial.print("-");
        Serial.print(volumen[1]);
        Serial.print("-");
        Serial.print(volumen[2]);
        Serial.print("-");
        Serial.println(volumen[3]);
        tiempo_actual = millis();
    }

	if (flag_encoder == true)
	{
        if (flag_if_encoder == true)
        {
            Serial.println(encoder_output);
            flag_encoder = false;
            flag_if_encoder = false;
        }
	}
	if (flag_boton_encoder == true)
	{
		Serial.println("boton_encoder");
		flag_boton_encoder = false;
	}
	delay(10);
}

void encoder_interrup(void)
{ 
    if (flag_if_encoder == false)
    {
        dt = digitalRead(DT);
        if (dt == HIGH) encoder_output = 1;
        else if (dt == LOW) encoder_output = -1;
        flag_encoder = true;
    }
    flag_if_encoder = true;
}

void boton_encoder_interrup(void)
{
	flag_boton_encoder = true;
}

void botones_macros (void)
{
    char boton_macro = matriz_macros.getKey();
    if (boton_macro)
    {
        Serial.print("macro_");
        Serial.println(boton_macro);
    }
}

void com_botones_multimedia (void)
{
    lectura_botones_multimedia();

    for (int i = 0; i < CANT_BOTONES_MULTIMEDIA; i++)
    {
        if ((botones_multimedia[i] == HIGH) && (flags[i] == false))
        {
            Serial.print("boton_multimedia_");
            Serial.println(i+1);
            flags[i] = true;
        }
        if ((botones_multimedia[i] == LOW) && (flags[i] == true)) flags[i] = false;
    }
}

void lectura_botones_multimedia (void)
{
    botones_multimedia[0] = digitalRead(BOTON_MULTIMEDIA_1);
    botones_multimedia[1] = digitalRead(BOTON_MULTIMEDIA_2);
    botones_multimedia[2] = digitalRead(BOTON_MULTIMEDIA_3);
}

float lectura_pote_1(void)
{
	int lectura_pote_1;
	float volumen;
	lectura_pote_1 = analogRead(POTE_1);
	//Serial.println(lectura_pote_1);
	volumen = conversor_lectura_volumen(lectura_pote_1);
	return volumen;
}

float lectura_pote_2(void)
{
	int lectura_pote_2;
	float volumen;
	lectura_pote_2 = analogRead(POTE_2);
	//Serial.println(lectura_pote_2);
	volumen = conversor_lectura_volumen(lectura_pote_2);
	return volumen;
}

float lectura_pote_3(void)
{
	int lectura_pote_3;
	float volumen;
	lectura_pote_3 = analogRead(POTE_3);
	//Serial.println(lectura_pote_3);
	volumen = conversor_lectura_volumen(lectura_pote_3);
	return volumen;
}

float lectura_pote_4(void)
{
	int lectura_pote_4;
	float volumen;
	lectura_pote_4 = analogRead(POTE_4);
	//Serial.println(lectura_pote_4);
	volumen = conversor_lectura_volumen(lectura_pote_4);
	return volumen;
}

float conversor_lectura_volumen(float x)
{
	float volumen;
	volumen = (x * 100) / 1023;
	volumen /= 100;
	return volumen;
}
