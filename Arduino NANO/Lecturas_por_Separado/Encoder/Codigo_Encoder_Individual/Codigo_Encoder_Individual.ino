#define DT 22
#define CLK 23
#define BOTON_ENCODER 21

bool old_clk;
int contador = 50;

void setup() 
{
	pinMode(DT, INPUT);
	pinMode(CLK, INPUT);
    pinMode(BOTON_ENCODER, INPUT);
	Serial.begin(9600);
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
        if (dt == HIGH)
        {
            if (contador < 100) contador++;
            //Serial.println("horario");
        }
        else
        {
            if (contador > 0) contador--;
            //Serial.println("antihorario");

        }
        Serial.println(contador);
    }
    if (boton == LOW) Serial.println("BOTON");
    old_clk = clk;
}
