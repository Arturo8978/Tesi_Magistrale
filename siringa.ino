#include <SoftwareSerial.h>
#include <Adafruit_BMP085.h>

Adafruit_BMP085 BMP180;
int volume=0;

void setup() 
{
  Serial.begin(9600);
   delay(1000);

   //controllo se il sensore è connesso
  if (!BMP180.begin()) {                   //funziome che restituisce 1 quando il sensore è connesso  (altre modalità: BMP085_ULTRALOWPOWER 0 , BMP085_STANDARD 1 , BMP085_HIGHRES 2 ,BMP085_ULTRAHIGHRES 3 )
  Serial.println("Attenzione, il sensore barometrico BMP180 non è connesso!");
  while (1) {}                             //ciclo infinito che blocca il codice successivo se verificata la condizione IF
  }
}

void loop() 
{
  // Leggo l'input sul PIN A analogico 0:
  int sensorValue = analogRead(A0);                             // cavo giallo A0, cavo verde Vcc, cavo marrone GND
float voltage= sensorValue * (5.0 / 1023.0);


 if ((voltage<=5) && (voltage >4.995112)){ 
  volume=0;
  }
else if ((voltage<=4.995112) && (voltage >4.975)){ 
  volume=1;
  }
else if ((voltage<=4.975) && (voltage >4.96)){
  volume=2;
  }
else if ((voltage<=4.96) && (voltage >4.91)){ 
  volume=3;
  }
else if ((voltage<=4.91) && (voltage >4.87)){ 
  volume=4;
  }
else if ((voltage<=4.87) && (voltage >4.82)){ 
  volume=5;
  }
else if ((voltage<=4.82) && (voltage >4.78)){ 
  volume=6;
  }
else if ((voltage<=4.78) && (voltage >4.6)){
  volume=7;
  }
else if ((voltage<=4.6) && (voltage >4.33)){
  volume=8;
  }
else if ((voltage<=4.33) && (voltage >4.07)){
  volume=9;
}
else if ((voltage<=4.07) && (voltage >3.82)){ 
  volume=10;
  }
else if ((voltage<=3.82) && (voltage >3.57)){
  volume=11;
  }
else if ((voltage<=3.57) && (voltage >3.32)){ 
  volume=12;
  }
else if ((voltage<=3.32) && (voltage >3.05)){ 
  volume=13;
  }
else if ((voltage<=3.05) && (voltage >2.8)){
  volume=14;
  }
else if ((voltage<=2.8) && (voltage >2.56)){ 
  volume=15;
  }
else if ((voltage<=2.56) && (voltage >2.32)){ 
  volume=16;
  }
else if ((voltage<=2.32) && (voltage >2.06)){
  volume=17;
  }
else if ((voltage<=2.06) && (voltage >1.84)){
  volume=18;
  }
else if ((voltage<=1.84) && (voltage >1.6)){ 
  volume=19;
  }
else if ((voltage<=1.6) && (voltage >1.35)){
  volume=20;
  }
else if ((voltage<=1.35) && (voltage >1.11)){
  volume=21;
  }
else if ((voltage<=1.11) && (voltage >0.9)){ 
  volume=22;
  }
else if ((voltage<=0.9) && (voltage >0.7)){ 
  volume=23;
  }
else if ((voltage<=0.7) && (voltage >0.47)){ 
  volume=24;
  }
else if ((voltage<=0.47) && (voltage >0.24)){ 
  volume=25;
  }
else if ((voltage<=0.24) && (voltage >0.19)){
  volume=26;
  }
else if ((voltage<=0.19) && (voltage >0.14)){ 
  volume=27;
  }
else if ((voltage<=0.14) && (voltage >0.1)){ 
  volume=28;
  }
else if ((voltage<=0.1) && (voltage >0.06)){
  volume=29;
  }
else if ((voltage<=0.06) && (voltage >0.03)){
  volume=30;
  }
else if ((voltage<=0.03) && (voltage >0.02)){ 
  volume=31;
  }
else if ((voltage<=0.02) && (voltage >0.004)){ 
  volume=32;
  }
else if ((voltage<=0.004) && (voltage >0)){
  volume=33;
}
   
  // Stampo il valore letto del volume:
  //Serial.print("Valore letto: ");
  //Serial.println(volume);

  //temperatura
    float temperatura = BMP180.readTemperature();
  //  Serial.print("Temperatura = ");
   // Serial.print(temperatura);
   // Serial.println(" *C");
   
   

  //pressione atmosferica
    float pressione = BMP180.readPressure();
   // Serial.print("Pressione = ");
   // Serial.print(pressione);
    //Serial.println(" Pa ");

Serial.println( (String)volume +","+ (String)pressione +","+ (String)temperatura);
    

  delay(1000); // attendo 1 secondi
}
