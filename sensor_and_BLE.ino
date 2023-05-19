
//includo le librerie necessarie

#include <SoftwareSerial.h>
//#include <Wire.h>
#include <Adafruit_BMP085.h>

Adafruit_BMP085 BMP180;      //istanza alla classe Adafruit_BMP085 chiamata BMP180  (il pin A4 va collegato a SDA, il pin A5 SCL del sensore BMP180)
SoftwareSerial BTSerial(7, 6); //crea un nuovo oggetto di tipo SoftwareSerial chiamato BTSerial (PIN 6 DIRETTAMENTE AL MICRO, PIN 7 PARTITORE) {SoftwareSerial(rxPin, txPin)dal punto di vista di arduino}
                      
void setup() {
  //inizializzo la seriale
  BTSerial.begin(9600);
  Serial.begin(9600);
  delay(1000);
  
  //controllo se il sensore è connesso
  if (!BMP180.begin()) {                   //funziome che restituisce 1 quando il sensore è connesso
  Serial.println("Attenzione, il sensore barometrico BMP180 non è connesso!");
  while (1) {}                             //ciclo infinito che blocca il codice successivo se verificata la condizione IF
  }
}
  
void loop() {
  //scrivo le varie misurazioni sul seriale e sul modulo :
  //temperatura
    float temperatura = BMP180.readTemperature();
    Serial.print("Temperatura = ");
    Serial.print(temperatura);
    Serial.println(" *C");
    //BTSerial.println(temperatura);
   

  //pressione atmosferica
    float pressione = BMP180.readPressure();
    Serial.print("Pressione atmosferica = ");
    Serial.print(pressione);
    Serial.println(" Pa ");
    BTSerial.println(  (String)pressione +","+ (String)temperatura);
    delay(500);
    }
