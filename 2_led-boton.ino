const int ledPin = 13;  
const int buttonPin = 7;  

void setup() {
  pinMode(ledPin, OUTPUT); 
  pinMode(buttonPin, INPUT_PULLUP);  
}

void loop() {
  if (digitalRead(buttonPin) == LOW) {  
    digitalWrite(ledPin, !digitalRead(ledPin)); 
    delay(200);  s
  }
}
