# Automatic Plant Watering System (IoT-Based)

## Project Overview
The **Automatic Plant Watering System** is an IoT-based project designed to monitor soil moisture levels and automate plant watering. The system integrates hardware simulation (using Tinkercad) with a MERN-based web application to display real-time data and maintain a record of soil moisture levels.

## Directory Structure
```
.
├── Arduino
│   └── automatic_plant_watering_system1
│       └── automatic_plant_watering_system1.ino
├── MERN
│   ├── Backend
│   │   └── (Contains endpoints for handling soil moisture data)
│   ├── Frontend
│       └── (Displays soil moisture data)
├── Simulate
│   └── simulate.py
├── Tinkercad
│   ├── block_code_screenshot.png
│   ├── system_diagram.png
│   ├── digital_circuit.png
│   └── components_list.xlsx
```

### 1. Arduino
- **Location:** `Arduino/automatic_plant_watering_system1`
- **File:** `automatic_plant_watering_system1.ino`
- **Description:**
  - Reads soil moisture sensor values using Arduino.
  - Turns on or off connected devices (like a water pump) based on moisture levels.
  - Code developed and tested using Tinkercad simulation.

### 2. MERN
- **Backend:**
  - **Endpoint 1:** Receives soil moisture values from the simulation and stores them in the database.
  - **Endpoint 2:** Provides all stored soil moisture values to display in the frontend.
- **Frontend:**
  - Displays the stored soil moisture data in a user-friendly interface.

### 3. Simulate
- **File:** `simulate.py`
- **Description:**
  - Simulates the soil moisture sensor by sending values to the MERN backend.
  - Used as a workaround to connect Tinkercad simulation with the MERN app.

### 4. Tinkercad
- **Contents:**
  - **Block Code Screenshot:** A visual representation of the system logic in Tinkercad.
  - **System Diagram:** A high-level diagram of the system.
  - **Digital Circuit:** The digital circuit design used in Tinkercad.
  - **Components List:** An Excel file listing all hardware components used.

## How to Run the Project

### 1. Hardware Simulation (Tinkercad)
- Open Tinkercad and load the digital circuit.
- Use the `.ino` file in the Arduino IDE for the simulation.
- Monitor the serial output to view soil moisture levels.

### 2. Backend (MERN App)
- Navigate to the `MERN/Backend` folder.
- Install dependencies using `npm install`.
- Start the server using `npm run dev`.

### 3. Frontend (MERN App)
- Navigate to the `MERN/Frontend` folder.
- Install dependencies using `npm install`.
- Start the application using `npm run dev`.

### 4. Simulation Script
- Navigate to the `Simulate` folder.
- Run the simulation script using:
  ```
  python simulate.py
  ```
- Ensure the backend is running to accept the simulated data.

## Components
### Hardware:
- **Arduino Uno R3**
- **Soil Moisture Sensor**
- **Relay Module**
- **DC Motor (Water Pump)**
- **LED**
- **Resistor**
- **Power Supply**

### Software:
- **Tinkercad:** For hardware simulation.
- **MERN Stack:** For web application development.
- **Python:** For data simulation script.
  
## License
This project is licensed under the MIT License. See `LICENSE` for details.

---
Feel free to contribute or raise issues if you encounter any problems!

