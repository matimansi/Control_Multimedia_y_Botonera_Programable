#define DT 4
#define CLK 2
#define BOTON_ENCODER 3
#define TIEMPO_ESPERA 500

bool old_clk;
unsigned long tiempo_actual;

void setup() 
{
	pinMode(DT, INPUT);
	pinMode(CLK, INPUT);
	pinMode(BOTON_ENCODER, INPUT);
	Serial.begin(9600);
	tiempo_actual = millis();
	old_clk = digitalRead(CLK);
}

void loop() 
{
	bool dt, clk, boton;
	dt = digitalRead(DT);
	clk = digitalRead(CLK);
	boton = digitalRead(BOTON_ENCODER);
	if ((old_clk == HIGH) && (clk == LOW))
	{
		if (dt == HIGH) Serial.println("1");
		else Serial.println("-1");
	}
	if (boton == LOW)
	{
		if (millis() - tiempo_actual >= TIEMPO_ESPERA)
		{
			Serial.println("BOTON");
			tiempo_actual = millis();
		}
	}
	old_clk = clk;
}
