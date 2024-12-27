// This code reads data from a soil moisture sensor connected to an Arduino board. 
// It checks the moisture level and turns on or off two connected devices (like LEDs or motors) based on the sensor's readings.

// Define a variable to store the sensor's reading
int soil_moisture_sensor = 0;

void setup() {
  // Set pin A0 (analog pin) as input for the soil moisture sensor
  pinMode(A0, INPUT);
  
  // Start serial communication to send data to the computer
  Serial.begin(9600);
  
  // Set pin 7 as output (e.g., for an LED or a device)
  pinMode(7, OUTPUT);
  
  // Set pin 8 as another output (e.g., for another LED or device)
  pinMode(8, OUTPUT);
}

void loop() {
  // Read the analog value from the soil moisture sensor
  soil_moisture_sensor = analogRead(A0);
  
  // Print the sensor's reading to the serial monitor
  Serial.println(soil_moisture_sensor);
  
  // If the soil moisture level is very low (less than 100):
  if (soil_moisture_sensor < 100) {
    // Turn on the devices connected to pins 7 and 8
    digitalWrite(7, HIGH);
    digitalWrite(8, HIGH);
  } else {
    // Otherwise, turn off the devices
    digitalWrite(7, LOW);
    digitalWrite(8, LOW);
  }

  // Short delay to reduce how fast the loop runs (for smoother simulation)
  delay(10); 
}
