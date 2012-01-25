int led=9;
int led2=13;
int pot=5;
int pot2=4;
int state=0;
int states=0;
int state2=0;
int states2=0;

void setup(){
  Serial.begin(9600);
  pinMode(led,OUTPUT);
  pinMode(led2,OUTPUT);
  pinMode(pot,INPUT);
  pinMode(pot2,INPUT);
}

void loop(){
if(Serial.available()>=1){
  switch( byte( Serial.read() )){
  case 'r':
  
state= analogRead(pot);
state2= analogRead(pot2);
states = map(state, 1023, 0, 0, 255);
states2 = map(state2, 0, 1023, 0, 255);
analogWrite(led2,state2);
analogWrite(led,states);
Serial.println(state);

Serial.println(state2);
//delay(1000);
break;


case 's':


digitalWrite(led2,LOW);
delay(1000);
digitalWrite(led2,HIGH);
delay(1000);
break;

case 'p':
while(Serial.read()!='m'){
state=  analogRead(pot);
states = map(state, 0, 1023, 0, 255);  
digitalWrite(led2,HIGH);
analogWrite(led,states);
Serial.println(state);
delay(1000);}
break;


}}
}

