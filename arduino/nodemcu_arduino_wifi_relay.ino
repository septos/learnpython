#include <CTBot.h>;
#include <CTBotDataStructures.h>;
#include <CTBotDefines.h>;
#include <CTBotInlineKeyboard.h>;
#include <CTBotReplyKeyboard.h>;
#include <CTBotSecureConnection.h>;
#include <CTBotStatusPin.h>;
#include <CTBotWifiSetup.h>;
#include <Utilities.h>;
#include <ArduinoJson.h>;
//variable untuk bot telegram
CTBot mybot;
//konfigurasi konek ke wifi
String ssid = "ASUS_X";
String pass = "123456789";
//Variable token dan id telegram        
String token = "1458896459:AAHEZiK8dSSPHdK_CjUAIH2ozsYKmpNci4Y";
const int id = 1383279356;

//tambahan relay on
const int relay[1] = {16};
bool nyala = HIGH;
bool mati = LOW;
String perintahnyala[1] = {"relay 1 nyala"};
String perintahmati[1] = {"relay 1 mati"};


void setup() {
  // Serial monitor
  Serial.begin(9600);
  Serial.println("Memulai aplikasi telegram bot");

  //koneksi ke wifi
  mybot.wifiConnect(ssid, pass);
  //set token
  mybot.setTelegramToken(token);

  //cek koneksi wifi internet
  if (mybot.testConnection())
    Serial.println("Koneksi berhasil");
  else
    Serial.println("Koneksi gagal");

  //set pinMode
  for(int i=0; i<=0; i++){
    pinMode(relay[i], OUTPUT);
    }
  for(int i=0; i<=0; i++){
    digitalWrite(relay[i], mati);
    }   
}

void loop() {
  // baca pesan masuk dari telegram
  TBMessage msg;
  
  // set perintah
  if(mybot.getNewMessage(msg)){
    Serial.println("Pesan di telegram : " + msg.text);
    for(int i=0; i<=0; i++){
      if(msg.text.equalsIgnoreCase(perintahnyala[i])){
        digitalWrite(relay[i], nyala);
        mybot.sendMessage(msg.sender.id, perintahnyala[i]);
      }else if(msg.text.equalsIgnoreCase(perintahmati[i])){
        digitalWrite(relay[i], mati);
        mybot.sendMessage(msg.sender.id, perintahmati[i]);
      }
    }
}
  delay(10);
}



  //-------------------------------------------
//  if(mybot.getNewMessage(msg))
//  {
//    //tampilkan di serial monitor
//    Serial.println("Pesan masuk : " + msg.text);
//  }
//  String pesan = msg.text;
//  if (pesan == "Hallo")
//  {mybot.sendMessage(id, "Haloo juga");}
//  else if(pesan == "Apa kabar?")
//  {mybot.sendMessage(id, "Kabar baik");}
//  else if (pesan == "L1 ON")
//  {mybot.sendMessage(id, "Lampu 1 ON");}
//  else if (pesan == "L1 OFF")
//  {mybot.sendMessage(id, "Lampu 1 OFF");}  
//}
