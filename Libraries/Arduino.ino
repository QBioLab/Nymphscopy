int pin = 0;
int action = 0;
int i = 0;
char buff[8];

void setup()
{
	Serial.begin(9600);
	pinMode(2, OUTPUT);
	pinMode(3, OUTPUT);
	pinMode(4, OUTPUT);
	pinMode(5, OUTPUT);
	pinMode(6, OUTPUT);
	pinMode(7, OUTPUT);
	pinMode(9, OUTPUT);
	pinMode(10, OUTPUT);
	digitalWrite(2, LOW);
	digitalWrite(3, LOW);
	digitalWrite(4, LOW);
	digitalWrite(5, LOW);
	digitalWrite(6, LOW);
	digitalWrite(7, LOW);
	analogWrite(9, 0);
	analogWrite(10, 0);
	Serial.println("Hello!,How are you Python?");
}

void loop()
{
	for( i = 0; i < 8; i++ )
		buff[i] = 10;
	if( Serial.available() > 0 )
		Serial.readBytesUntil('\n', buff, 255);
	if( buff[0] != 10 )
	{
		//to convert char into int
		pin = buff[0] - 48;
		action = buff[1] - 48;
	//Serial.println(pin);
	//Serial.println(action);
		if( pin >= 2 && pin <= 7 )
		{
			if( action == 1 )
				digitalWrite( pin, HIGH );
			else if( action == 0 )
				digitalWrite( pin, LOW );
		}
		else if( pin == 9 || pin == 10 )
			analogWrite( pin, action );
	}
	//delay(10);

}
