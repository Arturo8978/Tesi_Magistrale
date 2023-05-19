
//includo le librerie necessarie

//#include <Wire.h>
#include <Adafruit_BMP085.h>

Adafruit_BMP085 BMP180;      //istanza alla classe Adafruit_BMP085 chiamata BMP180  (il pin A4 va collegato a SDA, il pin A5 SCL del sensore BMP180)

                      
void setup() {
  //inizializzo la seriale

  Serial.begin(9600);
  delay(1000);
  
  //controllo se il sensore è connesso
  if (!BMP180.begin()) {                   //funziome che restituisce 1 quando il sensore è connesso
  Serial.println("Attenzione, il sensore barometrico BMP180 non è connesso!");
  while (1) {}                             //ciclo infinito che blocca il codice successivo se verificata la condizione IF
  }
}
  
void loop() {

    float temperatura = BMP180.readTemperature();
    float pressione = BMP180.readPressure();   
    Serial.println(  (String)pressione +","+ (String)temperatura);
    delay(1000);
    }
