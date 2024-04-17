#define	BOTON_1 33
#define	BOTON_2 32
#define	BOTON_3	35
#define	CANT_BOTONES 3
#define TIEMPO_ESPERA 500

bool lectura_boton_1(void);
bool lectura_boton_2(void);
bool lectura_boton_3(void);

unsigned long tiempo_actual;

void setup() 
{
	pinMode(BOTON_1, INPUT);
	pinMode(BOTON_2, INPUT);
	pinMode(BOTON_3, INPUT);
	Serial.begin(9600);
	tiempo_actual = millis();
}

void loop() 
{
	bool botones[CANT_BOTONES];
	botones[0] = lectura_boton_1();
	botones[1] = lectura_boton_2();
	botones[2] = lectura_boton_3();
	for (int i = 0; i < CANT_BOTONES; i++)
	{
		if (botones[i] == 1)
		{
			if (millis() - tiempo_actual >= TIEMPO_ESPERA)
			{
				if (botones[i] == 1)
				{
					for (int i = 0; i < CANT_BOTONES; i++)
					{
						Serial.print(botones[i]);
						if (i != (CANT_BOTONES - 1)) Serial.print("-");
						else Serial.println("");
					}
					tiempo_actual = millis();
				}
			}
		}
	}
}

bool lectura_boton_1 (void)
{
	return (digitalRead(BOTON_1));
}

bool lectura_boton_2 (void)
{
	return (digitalRead(BOTON_2));
}

bool lectura_boton_3 (void)
{
	return (digitalRead(BOTON_3));
}
