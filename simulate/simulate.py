# To simulate the serial output from Tinkercad and send it to our MERN app, we need to create a script that acts as a bridge. 
# This bridge will mimic the serial data being received and forward it as HTTP requests to our MERN backend.

import requests # Library to send http request
import time
import random

# Define the backend endpoint URL
backend_url = "http://localhost:3000/soil-data"

while True:
    # Simulate a moisture value 
    moisture_value = random.randint(0, 876)  # Adjust range to your soil sensor output
    print(f"Simulated Moisture Value: {moisture_value}")

    # Send the data to your MERN backend
    try:
        response = requests.post(backend_url, json={"moistureValue": moisture_value})
        print(f"Server Response: {response.text}")
    except Exception as e:
        print(f"Error sending data: {e}")

    # Wait for a second to mimic real-time data flow
    time.sleep(1)
