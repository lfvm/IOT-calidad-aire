#include <Arduino_JSON.h>
#include <WiFiNINA.h>

char ssid[] = "iPhone de valdeon";
char password[] = "fer30300";
int sensorpin = A0;

int status = WL_IDLE_STATUS;

char server[] = "3b07-148-241-111-162.ngrok.io";   

WiFiClient client;

void setup(){
  Serial.begin(9600);

  while (status != WL_CONNECTED) {
    Serial.println("Attempting to connect to Network: ");
    Serial.println(ssid);
    status = WiFi.begin(ssid,password);
    delay (1000);
  }

  Serial.print("Connected to SSID: ");
  Serial.println(WiFi.SSID());
  IPAddress ip = WiFi.localIP();
  IPAddress gateway = WiFi.gatewayIP();
  Serial.print("IP Address: ");
  Serial.println(ip);

}

void loop(){

   int medicion;
   JSONVar data;
    

   //obtener valor sensor

   medicion = analogRead(sensorpin);

   float voltaje = medicion * (5.0 /1023.0);
   float rs = 1000*( (5-voltaje) / voltaje);
   double co =-0.913*log(rs) + 9.6282;
   
   int id = 14;

   data["valorMedicion"] = co;
   data["idDispositivo"] = id;

   String dataString = JSON.stringify(data);
   
   if (client.connect(server, 80)) {
    client.println("POST /mediciones/nuevo HTTP/1.1");
    client.println("Host: 3b07-148-241-111-162.ngrok.io");
    client.println("Content-Type: application/json");
    client.print("Content-Length: ");
    client.println(dataString.length());
    client.println();
    client.print(dataString);
   }
   
   if (client.connected()) {
    client.stop();
  }
  
  Serial.println(dataString);

  delay(5000);
  
}
