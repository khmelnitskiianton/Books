#define voltageAC_pin A0
#define voltageShunt_pin A1
#define Shunt 30.0f

float voltageAC    = 0;
float voltageShunt = 0;

void setup() {
  Serial.begin(9600);
  pinMode(voltageAC_pin, INPUT);
  pinMode(voltageShunt_pin, INPUT);
}

float getCurrent() {
  return analogRead(voltageShunt_pin) / 1024.0f * 5.0f * 1000.0f / (150000.0f + 910.0f) * 910.0f / Shunt;
}

float getVoltage() {
  return analogRead(voltageAC_pin) / 1024.0f * 5.0f * 2.0f;
}

bool voltage[1024] = {0};

void loop() {
  int value = analogRead(voltageAC_pin);
  if(voltage[value] < 2) {
      voltage[value] =  voltage[value] + 1;
      Serial.print(getVoltage());
      Serial.print("; ");
      Serial.println(getCurrent());
  }
}
