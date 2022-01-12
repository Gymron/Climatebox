#include <DHT.h>                      //DHT11 Sensor initialisieren

String InputString = "";              //Empfangene Daten
int TMP36 = A15;                      //TMP36 Wasser Pinbenennung
int Piezo = 51;                       //Piezo-Fogger Pinbenennung
int Heizstab = 52;                    //Heizstab Pinbenennung
int Lampe = 53;                       //Heizlampe Pinbenennung
int set1 = 0;
int set2 = 0;
int set3 = 0;
int error = 0;
float AirTemp = 0.0;
float AirHum = 0.0;
float WaterTemp = 0.0;
bool control = false;

char CharString[20];
char delimiter[] = "+";               //Strings zum String zerteilen
char *ptr;

DHT dht(42, DHT11);

void setup() {
  Serial.begin(9600);                 //Start des seriellen Monitors
  dht.begin();                        //Aktivieren des DHT11 Sensors
  pinMode(A0, INPUT);                 //Input TMP36 Wasser
  pinMode(51, OUTPUT);                //Grün (Piezo-Fogger)
  pinMode(52, OUTPUT);                //Gelb (Heizstab Wasser)
  pinMode(53, OUTPUT);                //Rot (Wärmelampe)
}

void loop() {
  if (Serial.available()) {
      InputString = Serial.readString();    //Format: control+Fogger+Heizstab+Heizlampe
        if (InputString == "debug") {       //Serielle Ausgabe in Klartext
          outputDebug();
        }
        
        else if (InputString == "data") {   //Serielle Ausgabe als String
          outputData();
        }
        
        else {
          int durchlauf = 0;
          InputString.toCharArray(CharString, 20);    //Zerteilen des Inputs in die einzelnen Werte
          ptr = strtok(CharString, delimiter);

          while(ptr != NULL) {
            durchlauf++;
            Serial.print(durchlauf);
            Serial.print(". ");
            Serial.println(ptr);
            
            if (durchlauf == 1 && strcmp(ptr, "control") == 0 || control == true){     //Steuerbefehl vorhanden und Steuerung der Sensoren -> Setzen des Booleans control
              if (control != true){control = true;}
              Serial.println("Is Control");
              
              switch (durchlauf) {
                case 1:                   // Erster Durchlauf
                  Serial.println("Durchlauf 1");
                  
                  break;
                  
                case 2:                   // Zweiter Durchlauf (Steuersignal 1)
                  Serial.print("Steuersignal 1 ist ");
                  set1 = atoi(ptr);
                  Serial.println(set1);
                  break;
                  
                case 3:                   // Zweiter Durchlauf (Steuersignal 2)
                  Serial.print("Steuersignal 2 ist ");
                  set2 = atoi(ptr);
                  Serial.println(set2);
                  break;
                  
                case 4:                   // Zweiter Durchlauf (Steuersignal 3)
                  Serial.print("Steuersignal 3 ist ");
                  set3 = atoi(ptr);
                  Serial.println(set3);
                  break;
                  
                default:
                  Serial.println("error+unexpected_control_value");
                  error++;
                  break;
               }
              
              Serial.println(control);
            }
            
            ptr = strtok(NULL, delimiter);
          }

          if (error == 0) {
            if (set1 == 0) {digitalWrite(Piezo, LOW);}
            if (set1 == 1) {digitalWrite(Piezo, HIGH);}
            if (set2 == 0) {digitalWrite(Heizstab, LOW);}
            if (set2 == 1) {digitalWrite(Heizstab, HIGH);}
            if (set3 == 0) {digitalWrite(Lampe, LOW);}
            if (set3 == 1) {digitalWrite(Lampe, HIGH);}
          }
          if (error > 0) {
            Serial.print("Aufgetretene Fehler: ");
            Serial.print(error);
          }
          
          error = 0;
          durchlauf = 0;
          set1 = 0;
          set2 = 0;
          set3 = 0;
          control = false;
         }
         
      InputString = "";
    }
  
  //Auslesen der Wassertemperatur
  WaterTemp = (((analogRead(TMP36)*5.0)/1024.0) - 0.5) * 100 ;

  //Auslesen der Lufttemperatur und Luftfeuchte
  AirTemp = dht.readTemperature();
  AirHum = dht.readHumidity();
  
  //delay(500);    // Wartezeit zwischen Messungen
}

void outputDebug() {    //Übertragen (Ausgeben) der Daten
  // Ausgabe der Wassertemperatur
  Serial.print("Wassertemperatur: ");
  Serial.print(WaterTemp);
  Serial.println(" °C");

  //Ausgeben der Lufttemperatur und Luftfeuchte
  Serial.print("Lufttemperatur: ");
  Serial.print(AirTemp);
  Serial.println(" °C");
  Serial.print("Luftfeuchtigkeit: ");
  Serial.print(AirHum);
  Serial.println(" %");
}

void outputData() {   //Übertragen (Ausgeben) des Strings
  Serial.println(String(WaterTemp)+"+"+String(AirTemp)+"+"+String(AirHum));   //Format: Wassertemperatur+Lufttemperatur+Luftfeuchte
}
