#define POTE_1 13
#define POTE_2 14
#define POTE_3 27
#define POTE_4 26

float lectura_pote_1(void);
float lectura_pote_2(void);
float lectura_pote_3(void);
float lectura_pote_4(void);
float conversor_lectura_volumen(float);

void setup()
{
	pinMode(POTE_1, INPUT);
	pinMode(POTE_2, INPUT);
	pinMode(POTE_3, INPUT);
	Serial.begin(9600);
}

void loop()
{
	float volumen_1, volumen_2, volumen_3, volumen_4;
	volumen_1 = lectura_pote_1();
	volumen_2 = lectura_pote_2();
	volumen_3 = lectura_pote_3();
	volumen_4 = lectura_pote_4();
	Serial.print(volumen_1);
	Serial.print("-");
	Serial.print(volumen_2);
	Serial.print("-");
	Serial.print(volumen_3);
	Serial.print("-");
	Serial.println(volumen_4);
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
	volumen = (x * 100) / 4095;
	volumen /= 100;
	return volumen;
}
