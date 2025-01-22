#define PIN_TRIG 15
#define PIN_ECHO 4


#define LED_5CM 17 
#define LED_10CM 5
#define LED_15CM 18

void setup(){ 
  Serial.begin(115200);

  pinMode(PIN_TRIG, OUTPUT); 
  pinMode(PIN_ECHO, INPUT);

  pinMode(LED_5CM, OUTPUT);   
  pinMode(LED_10CM, OUTPUT);  
  pinMode(LED_15CM, OUTPUT); 

  digitalWrite(LED_5CM, LOW); 
  digitalWrite(LED_10CM, LOW);
  digitalWrite(LED_15CM, LOW);
}

void loop() {
  if (distance < 5) {
    digitalWrite(LED_5CM, HIGH);    // Enciende LED para 5 cm
    digitalWrite(LED_10CM, LOW);   // Apaga los otros LEDs
    digitalWrite(LED_15CM, LOW);
  } else if (distance < 10) {
    digitalWrite(LED_10CM, HIGH);   // Enciende LED para 10 cm
    digitalWrite(LED_5CM, LOW);    // Apaga los otros LEDs
    digitalWrite(LED_15CM, LOW);
  } else if (distance < 15) {
    digitalWrite(LED_15CM, HIGH);   // Enciende LED para 15 cm
    digitalWrite(LED_5CM, LOW);    // Apaga los otros LEDs
    digitalWrite(LED_10CM, LOW);
  } else {
    // Si la distancia es mayor a 15 cm, apaga todos los LEDs
    digitalWrite(LED_5CM, LOW);
    digitalWrite(LED_10CM, LOW);
    digitalWrite(LED_15CM, LOW);
  }
  delay(1000);
}
