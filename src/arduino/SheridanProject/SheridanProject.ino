void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop() {
  //old sensor, high is dry
  //keep power disconnected from the moisture sensor when not being used, to maximize lifespan
  
  digitalWrite(0, HIGH);
  digitalWrite(13, HIGH); // blink light when sensor is powered
  int moisture = analogRead(A0);
  Serial.println(moisture);
  digitalWrite(0, LOW);
  digitalWrite(13, LOW);

  delay(5000);


  //if sensor level is low AND time since last water is 1 or 2 days AND not longer than 4 or 5 days
    //turn on water pump for some seconds
    //turn off
    //spin servo 180 degrees
    //turn on water pump for some seconds
    //turn off



  
}
