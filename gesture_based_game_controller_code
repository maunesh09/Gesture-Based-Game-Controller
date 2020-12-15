
#define BLYNK_PRINT Serial
#include <BlynkSimpleEsp8266.h> 
#include <ESP8266WiFi.h>
#include<Adafruit_NeoPixel.h>
Adafruit_NeoPixel strip = Adafruit_NeoPixel(10,12, NEO_GRB +NEO_KHZ800);

char auth[] = "*********************"; //Blynk auth token

char ssid[] = "Maunesh";     // variable to store wifi credential
char pass[] = "***********"; // variable to store wifi credentials

void red()
 {
  for(uint16_t i=0; i<10; i++)
   {
    strip.setPixelColor(i,strip.Color(255,0,0)); //red,green,blue
   }
  strip.show();//turns on the rgb
}

void green()
 {
  for(uint16_t i=0; i<10; i++)
   {
    strip.setPixelColor(i,strip.Color(0,255,0)); //red,green,blue
   } 
   strip.show();//turns on the rgb
 }

void blue()
 {
  for(uint16_t i=0; i<10; i++)
  {
    strip.setPixelColor(i,strip.Color(0,0,255)); //red,green,blue
  }
  strip.show();//turns on the rgb
 }

void ledoff()
 {
  for(uint16_t i=0; i<10; i++)
   {
    strip.setPixelColor(i,strip.Color(0,0,0)); //red,green,blue
   }
   strip.show();//turns on the rgb
 }

void setup() 
{
      // starts the serial communication
 strip.begin();
 Serial.begin(115200);
 Blynk.begin(auth, ssid, pass);
 strip.setBrightness(25);
}

//Virtual Pin V4 is for using Smart Phone's inbuilt Acceletometer for Gestures

BLYNK_WRITE(V4) 
{
  int x = param[0].asFloat();
  int y = param[1].asFloat();
  int z = param[2].asFloat();

if (z>0 && x==0 && y==0) //stop
 {
  ledoff();
  Serial.println('0');
  //Serial.println("    Stop/ No key Pressed");
 }

if(x==0 && y<0 && z>0) //forward or W or Up_Key

 {
  green();
  Serial.println('8');  // provide num so that python can get the num to give key strokes
 
 }

if(x==0 && y>0 && z>0) //backwords or S 
{
  red();
  //Serial.println("    S / DOWN");
  Serial.println('2');
}

if(x<0 && y<0 && z>0) //forward_right or W-D
{
  
  Serial.println('9');
  uint16_t i=0;
  strip.setPixelColor(i,strip.Color(0, 0, 0));
  strip.show();
 //delay(20);
 
  i=1;
  strip.setPixelColor(i,strip.Color(0, 0, 0));
  strip.show();
 //delay(20);
  
  i=2;
  strip.setPixelColor(i,strip.Color(0, 0, 0));
  strip.show();
 //delay(20);
  
  i=3;
  strip.setPixelColor(i,strip.Color(0, 0, 0));
  strip.show();
 //delay(20);
  
  i=4;
  strip.setPixelColor(i,strip.Color(0, 0, 0));
  strip.show();
 //delay(20);

  
  i=5;
  strip.setPixelColor(i,strip.Color(0, 255, 0));
  strip.show();
 //delay(20);
 
  i=6;
  strip.setPixelColor(i,strip.Color(0,255, 0));
  strip.show();
 //delay(20);
  
  i=7;
  strip.setPixelColor(i,strip.Color(0,255,0));
  strip.show();
 //delay(20);
  
 
  i=8;
  strip.setPixelColor(i,strip.Color(0,255,0));
  strip.show();
 //delay(20);
  
  i=9;
  strip.setPixelColor(i,strip.Color(0,255, 0));
  strip.show();
 //delay(20);
 }

if(x>0 && y<0 && z>0) // Forward_Left or A-W
{
  
  Serial.println('7');
  uint16_t i=0;
  strip.setPixelColor(i,strip.Color(0,255, 0));
  strip.show();
 // delay(20);
 
  i=1;
  strip.setPixelColor(i,strip.Color(0,255, 0));
  strip.show();
  //delay(20);
  
  i=2;
  strip.setPixelColor(i,strip.Color(0,255, 0));
  strip.show();
  //delay(20);
  
  i=3;
  strip.setPixelColor(i,strip.Color(0,255, 0));
  strip.show();
 // delay(20);
  
  i=4;
  strip.setPixelColor(i,strip.Color(0,255, 0));
  strip.show();
//  delay(20);

  
  i=5;
  strip.setPixelColor(i,strip.Color(0, 0, 0));
  strip.show();
 //delay(20);
 
  i=6;
  strip.setPixelColor(i,strip.Color(0,0, 0));
  strip.show();
 //delay(20);
  
  i=7;
  strip.setPixelColor(i,strip.Color(0,0,0));
  strip.show();
//delay(20);
  
  
  i=8;
  strip.setPixelColor(i,strip.Color(0,0,0));
  strip.show();
 //delay(20);
  
  i=9;
  strip.setPixelColor(i,strip.Color(0,0,0));
  strip.show();
 //delay(20);

}

if(x<-4 && y>2 && z>0) //S-D or Bakwards_Right
{
 
  Serial.println('3');
  uint16_t i=0;
  strip.setPixelColor(i,strip.Color(0, 0, 0));
  strip.show();
 //delay(20);
 
  i=1;
  strip.setPixelColor(i,strip.Color(0, 0, 0));
  strip.show();
 //delay(20);
  
  i=2;
  strip.setPixelColor(i,strip.Color(0, 0, 0));
  strip.show();
 //delay(20);
  
  i=3;
  strip.setPixelColor(i,strip.Color(0, 0, 0));
  strip.show();
 //delay(20);
  
  i=4;
  strip.setPixelColor(i,strip.Color(0, 0, 0));
  strip.show();
 //delay(20);

  
  i=5;
  strip.setPixelColor(i,strip.Color(255, 0, 0));
  strip.show();
 //delay(20);
 
  i=6;
  strip.setPixelColor(i,strip.Color(255,0, 0));
  strip.show();
 //delay(20);
  
  i=7;
  strip.setPixelColor(i,strip.Color(255,0,0));
  strip.show();
 //delay(20);
  
 
  i=8;
  strip.setPixelColor(i,strip.Color(255,0,0));
  strip.show();
 //delay(20);
  
  i=9;
  strip.setPixelColor(i,strip.Color(255,0, 0));
  strip.show();
 //delay(20);
}


if(x>0 && y>0 && z>0) // S-A or Reverse_Left
{
   
  Serial.println('1');
  uint16_t i=0;
  strip.setPixelColor(i,strip.Color(255, 0, 0));
  strip.show();
 // delay(20);
 
  i=1;
  strip.setPixelColor(i,strip.Color(255, 0, 0));
  strip.show();
  //delay(20);
  
  i=2;
  strip.setPixelColor(i,strip.Color(255, 0, 0));
  strip.show();
  //delay(20);
  
  i=3;
  strip.setPixelColor(i,strip.Color(255,0, 0));
  strip.show();
 // delay(20);
  
  i=4;
  strip.setPixelColor(i,strip.Color(255,0, 0));
  strip.show();
//  delay(20);

  
  i=5;
  strip.setPixelColor(i,strip.Color(0, 0, 0));
  strip.show();
 //delay(20);
 
  i=6;
  strip.setPixelColor(i,strip.Color(0,0, 0));
  strip.show();
 //delay(20);
  
  i=7;
  strip.setPixelColor(i,strip.Color(0,0,0));
  strip.show();
//delay(20);
  
  
  i=8;
  strip.setPixelColor(i,strip.Color(0,0,0));
  strip.show();
 //delay(20);
  
  i=9;
  strip.setPixelColor(i,strip.Color(0,0,0));
  strip.show();
 //delay(20);
 
}


//setup end
}

void loop()
{
  Blynk.run();
}

