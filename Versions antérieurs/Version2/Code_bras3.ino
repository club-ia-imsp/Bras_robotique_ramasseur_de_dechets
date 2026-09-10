#include <Servo.h>

Servo myservo1;
Servo myservo2;
Servo myservo3;
Servo myservo4;
int joystickX1 = A1;
int joystickY1= A2;
int joystickX2 = A3;
int joystickY2 = A4;                                                                                    ;
int servoPin1 = 3;
int servoPin2= 5;
int servoPin3 = 6;
int servoPin4 = 9;
int i=0;
int j=0;
int k=0;
int l=0;



void setup() {
 
  myservo1.attach(servoPin1);
   myservo2.attach(servoPin2);
    myservo3.attach(servoPin3);
     myservo4.attach(servoPin4);
     myservo1.write(20);
     myservo2.write(50);
     myservo3.write(16);
     myservo4.write(00);
  Serial.begin(9600);
}

void loop() {
  int valY1 = analogRead(joystickX1);
  int valX1 = analogRead(joystickY1);
  int valX2 = analogRead(joystickX2);
  int valY2 = analogRead(joystickY2);
  
  
  if(( valX1 < 300)&&(i<=180))
  {
    myservo1.write(i);
    i+= 5;
  }
  else if(( valX1 > 700)&&(i>=0))
  {
    myservo1.write(i);
    i-= 5;
  };
    if(( valY1 < 300)&&(j<=180))
  {
    myservo2.write(j);
    j+= 5;
  }
  else if(( valY1 > 700)&&(j>=0))
  {
   myservo2.write(j);
    j-= 5;
  };
   if(( valX2 < 300)&&(k<=180))
  {
    myservo3.write(k);
    k+= 5;
  }
  else if(( valX2 > 700)&&(k>=0))
  {
   myservo3.write(k);
    k-= 5;
  };
   if(( valY2 < 300)&&(l<=180))
  {
    myservo4.write(l);
    l+= 5;
  }
  else if(( valY2 > 700)&&(l>=0))
  {
   myservo4.write(l);
    l-= 5;
  };

  

  Serial.print("Joystick X1: ");
  Serial.print(valX1);
  Serial.print(" -> Angle X1: ");
  Serial.println(i);

Serial.print("Joystick Y1: ");
  Serial.print(valY1);
  Serial.print(" -> Angle Y1: ");
  Serial.println(j);

Serial.print("Joystick X2: ");
  Serial.print(valX2);
  Serial.print(" -> Angle X2: ");
  Serial.println(k);

Serial.print("Joystick Y2: ");
  Serial.print(valY2);
  Serial.print(" -> Angle Y2: ");
  Serial.println(l);
  delay(30);
}
