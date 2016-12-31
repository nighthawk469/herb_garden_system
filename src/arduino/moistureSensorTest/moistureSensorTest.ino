void setup() {
  Serial.begin(9600);

   //Setup Channel A
  pinMode(12, OUTPUT); //Initiates Motor Channel A pin
  pinMode(9, OUTPUT); //Initiates Brake Channel A pin
//
//  //Setup Channel B
  pinMode(13, OUTPUT); //Initiates Motor Channel A pin
  pinMode(8, OUTPUT); //Initiates Brake Channel B pin

  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);

}

void loop() {
  int sensorValue = analogRead(A3);
  Serial.println(sensorValue);
  
  if (sensorValue > 400)
  {
    digitalWrite(8, HIGH); //Engage the Brake for Channel A
    
    digitalWrite(2, HIGH);
    delay(1000);
    digitalWrite(2, LOW);
  }
  else if (sensorValue < 400 && sensorValue > 150)
  {
    digitalWrite(8, HIGH); //Engage the Brake for Channel A
    
    digitalWrite(4, HIGH);
    delay(1000);
    digitalWrite(4, LOW);
  }
  else if (sensorValue < 150)
  {   
    digitalWrite(5, HIGH);
    delay(1000);
    digitalWrite(5, LOW);

//    //spin motor A
    digitalWrite(13, HIGH); //Establishes forward direction of Channel A
    digitalWrite(8, LOW);   //Disengage the Brake for Channel A
    analogWrite(11, 100);
  }
  
  
  


}
