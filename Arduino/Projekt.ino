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
float SumTemp = 0.0;
float SumHum = 0.0;
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
  pinMode(A15, INPUT);                //Input TMP36 Wasser
  pinMode(51, OUTPUT);                //Grün (Piezo-Fogger)
  pinMode(52, OUTPUT);                //Gelb (Heizstab Wasser)
  pinMode(53, OUTPUT);                //Rot (Wärmelampe)
}

void loop() {
  if (Serial.available()) {
      InputString = Serial.readString();    //Format: control+Fogger+Heizstab+Heizlampe
        if (InputString == "debug") {       //Serielle Ausgabe in Klartext
          read_sensor("TMP36");
          read_sensor("DHT");
          outputDebug();
        }
        
        else if (InputString == "data") {   //Serielle Ausgabe als String
          read_sensor("TMP36");
          read_sensor("DHT");
          outputData();
        }
        
        else {
          int durchlauf = 0;
          InputString.toCharArray(CharString, 20);    //Zerteilen des Inputs in die einzelnen Werte
          ptr = strtok(CharString, delimiter);

          while(ptr != NULL) {
            durchlauf++;
            //Serial.print(durchlauf);
            //Serial.print(". ");
            //Serial.println(ptr);
            
            if (durchlauf == 1 && strcmp(ptr, "control") == 0 || control == true){     //Steuerbefehl vorhanden und Steuerung der Sensoren -> Setzen des Booleans control
              if (control != true){
                control = true;
                //Serial.println("Is Control");
              }
              
              switch (durchlauf) {
                case 1:                   // Erster Durchlauf
                  //Serial.println("Durchlauf 1");
                  
                  break;
                  
                case 2:                   // Zweiter Durchlauf (Steuersignal 1)
                  //Serial.print("Steuersignal 1 ist ");
                  if (atoi(ptr) != 0 && atoi(ptr) != 1) {
                    create_error(1);
                    error++;
                  }
                  else {
                    set1 = atoi(ptr);
                  }
                  //Serial.println(set1);
                  break;
                  
                case 3:                   // Dritter Durchlauf (Steuersignal 2)
                  //Serial.print("Steuersignal 2 ist ");
                  if (atoi(ptr) != 0 && atoi(ptr) != 1) {
                    create_error(1);
                    error++;
                  }
                  else {
                    set2 = atoi(ptr);
                  }
                  //Serial.println(set2);
                  break;
                  
                case 4:                   // Vierter Durchlauf (Steuersignal 3)
                  //Serial.print("Steuersignal 3 ist ");
                  if (atoi(ptr) != 0 && atoi(ptr) != 1) {
                    create_error(1);
                    error++;
                  }
                  else {
                    set3 = atoi(ptr);
                  }
                  //Serial.println(set3);
                  break;
                  
                default:
                  create_error(3);
                  error++;
                  break;
               }
              
              //Serial.println(control);
            }

            if (control == false) {              //Fehlerhafte Eingabe
              create_error(4);
              error++;
            }
            
            ptr = strtok(NULL, delimiter);
          }

          if (error == 0 && durchlauf == 4) {
            if (set1 == 0) {digitalWrite(Piezo, LOW);}
            if (set1 == 1) {digitalWrite(Piezo, HIGH);}
            if (set2 == 0) {digitalWrite(Heizstab, LOW);}
            if (set2 == 1) {digitalWrite(Heizstab, HIGH);}
            if (set3 == 0) {digitalWrite(Lampe, LOW);}
            if (set3 == 1) {digitalWrite(Lampe, HIGH);}
            Serial.println("ok");
          }
          if (durchlauf < 4 && control == true) {
            create_error(2);
            error++;
          }
          if (error > 0) {
            //Serial.println("Aufgetretene Fehler:");
            Serial.print("error+errorcount_");
            Serial.println(error);
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
  if (isnan(AirTemp) || isnan(AirHum)) {
    create_error(5);                                    //DHT-Sensor hat keine Verbindung
  }
  //if (analogRead(TMP36) == 69) {
  //  create_error(6);                                  //TMP36-Sensor hat keine Verbindung
  //}
  else {
    Serial.println(String(WaterTemp)+"+"+String(AirTemp)+"+"+String(AirHum));   //Format: Wassertemperatur+Lufttemperatur+Luftfeuchte
  }
}

void create_error(int error_number) {
  switch (error_number) {
    case 1:                       //Wert zum Steuern der Ausgänge ungleich 0 oder 1
      Serial.println("error+unexpected_control_value");
      break;
    
    case 2:                       //Zu niedrige Anzahl der Steuerwerte
      Serial.println("error+unexpected_control_count_low");
      break;
    
    case 3:                       //Zu hohe Anzahl der Steuerwerte
      Serial.println("error+unexpected_control_count_high");
      break;
    
    case 4:                       //Empfangene Daten können nicht interpretiert werden
      Serial.println("error+input_garbage");
      break;
    
    case 5:                       //Verbindung zum DHT11-Sensor verloren
      Serial.println("error+broken_sensor_dht");
      break;
    
    case 6:                       //Verbindung zum analogen Sensor verloren
      Serial.println("error+broken_sensor_analog");
      break;
  }
}

void read_sensor(String sensor_name){
  if (sensor_name == "DHT") {                           //Auslesen der Lufttemperatur und Luftfeuchte
    for (int count = 0; count <= 9; count++) {          //10 Durchläufe für Ausgleich der Sensorungenauigkeit
      SumTemp += dht.readTemperature();
      SumHum += dht.readHumidity();
    }
    AirTemp = SumTemp / 10;
    AirHum = SumHum / 10;
    SumTemp = 0.0;
    SumHum = 0.0;
  }
  
  if (sensor_name == "TMP36") {                         //Auslesen der Wassertemperatur
    for (int count = 0; count <= 9; count++) {          //10 Durchläufe für Ausgleich der Sensorungenauigkeit
      SumTemp += (((analogRead(TMP36)*5.0)/1024.0) - 0.5) * 100 ;
    }
    WaterTemp = SumTemp / 10;
    SumTemp = 0.0;
  }
}
