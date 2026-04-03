int SIGNAL_GENERATOR_1  = 2;
int SIGNAL_GENERATOR_2  = 3;

int SENSOR_1 = A0;
int SENSOR_2 = A1;
int SENSOR_3 = A2;
int SENSOR_4 = A3;
int SENSOR_5 = A4;
int SENSOR_6 = A5;
int SENSOR_7 = A6;
int SENSOR_8 = A7;

int senses = 10;
int current = 0;
double avg = 0;




void setup() {
  // put your setup code here, to run once
  Serial.begin(9600);

  pinMode(SENSOR_1, INPUT);
  pinMode(SENSOR_2, INPUT);
  pinMode(SENSOR_3, INPUT);
  pinMode(SENSOR_4, INPUT);
  pinMode(SENSOR_5, INPUT);
  pinMode(SENSOR_6, INPUT);
  pinMode(SENSOR_7, INPUT);
  pinMode(SENSOR_8, INPUT);
  pinMode(SIGNAL_GENERATOR_1, OUTPUT);
  pinMode(SIGNAL_GENERATOR_2, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  analogWrite(SIGNAL_GENERATOR_1, 127);
  analogWrite(SIGNAL_GENERATOR_2, 127);

  int d1 = analogRead(SENSOR_1);
  int d2 = analogRead(SENSOR_2);
  int d3 = analogRead(SENSOR_3);
  int d4 = analogRead(SENSOR_4);
  int d5 = analogRead(SENSOR_5);
  int d6 = analogRead(SENSOR_6);
  int d7 = analogRead(SENSOR_7);
  int d8 = analogRead(SENSOR_8);

  //Serial.print(d1);
  //Serial.print(", ");
  //Serial.print(d2);
  //Serial.print(", ");
  //Serial.print(d3);
  //Serial.print(", ");
  //Serial.print(d4);
  //Serial.print(", ");
  //Serial.print(d5);
  //Serial.print(", ");
  //Serial.print(d6);
  //Serial.print(", ");
  //Serial.print(d7);
  //Serial.print(", ");

  if (d8 != 0){
    current += 1;
    avg += d8;
    if (current >= senses){
      Serial.println(avg/senses);
      avg = 0;
      current = 0;
    }
  }
  //Serial.println(d8);
}
