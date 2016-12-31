void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop() {
  // keep power disconnected from the moisture sensor when not being used, to maximize lifespan
  digitalWrite(0, HIGH);
  digitalWrite(13, HIGH); // blink light when sensor is powered
  int moisture = analogRead(A0);
  Serial.println(moisture);
  digitalWrite(0, LOW);
  digitalWrite(13, LOW);

  delay(5000);
}
