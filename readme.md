# Automatic Plant Watering System (IoT-Based)

## Project Overview
The **Automatic Plant Watering System** is an IoT-based project designed to monitor soil moisture levels and automate plant watering. The system integrates hardware simulation (using Tinkercad) with a MERN-based web application to display real-time data and maintain a record of soil moisture levels. Additionally, a **machine learning model** predicts whether a plant needs watering based on environmental conditions.

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
├── Dataset & ML Model
│   ├── Dataset
│   │   └── TARP.csv (Dataset for predicting plant watering needs)
│   ├── MLmodel
│   │   └── machineLearningModel.py (Predicts watering status based on environmental data)
```

---

## 1. **Arduino**
- **Location:** `Arduino/automatic_plant_watering_system1`
- **File:** `automatic_plant_watering_system1.ino`
- **Description:**
  - Reads soil moisture sensor values using Arduino.
  - Turns on or off connected devices (like a water pump) based on moisture levels.
  - Code developed and tested using Tinkercad simulation.

---

## 2. **MERN Stack**
### Backend:
- **Endpoint 1:** Receives soil moisture values from the simulation and stores them in the database.
- **Endpoint 2:** Provides all stored soil moisture values to display in the frontend.

### Frontend:
- Displays the stored soil moisture data in a user-friendly interface.

---

## 3. **Simulate**
- **File:** `simulate.py`
- **Description:**
  - Simulates the soil moisture sensor by sending values to the MERN backend.
  - Used as a workaround to connect Tinkercad simulation with the MERN app.

---

## 4. **Tinkercad**
- **Block Code Screenshot:** A visual representation of the system logic in Tinkercad.
- **System Diagram:** A high-level diagram of the system.
- **Digital Circuit:** The digital circuit design used in Tinkercad.
- **Components List:** An Excel file listing all hardware components used.

---

## 5. **Dataset & ML Model**
### **Dataset**
- **File:** `TARP.csv`
- **Description:** This dataset is used to train the machine learning model. It contains features such as:
  - Soil Moisture
  - Temperature
  - Soil Humidity
  - Time
  - Air Temperature
  - Wind Speed
  - Air Humidity
  - Wind Gust
  - Pressure
  - pH Level
  - Rainfall
  - Nutrients (N, P, K)

### **ML Model**
- **File:** `machineLearningModel.py`
- **Description:** This Python-based machine learning model is trained on the dataset to predict whether a plant needs watering. Instead of using fixed thresholds (e.g., if soil moisture < 30%, turn the pump on), the model **learns from environmental data patterns** to make smarter watering decisions.
  
---

## How to Run the Project

### **1. Hardware Simulation (Tinkercad)**
- Open Tinkercad and load the digital circuit.
- Use the `.ino` file in the Arduino IDE for the simulation.
- Monitor the serial output to view soil moisture levels.

### **2. Backend (MERN App)**
- Navigate to the `MERN/Backend` folder.
- Install dependencies:
  ```bash
  npm install
  ```
- Start the server:
  ```bash
  npm run dev
  ```

### **3. Frontend (MERN App)**
- Navigate to the `MERN/Frontend` folder.
- Install dependencies:
  ```bash
  npm install
  ```
- Start the application:
  ```bash
  npm run dev
  ```

### **4. Simulation Script**
- Navigate to the `Simulate` folder.
- Run the simulation script:
  ```bash
  python simulate.py
  ```
- Ensure the backend is running to accept the simulated data.

### **5. Running the Machine Learning Model**
- Navigate to `Dataset & ML Model/MLmodel`.
- Install required dependencies:
  ```bash
  pip install -r requirements.txt
  ```
- Run the model to test predictions:
  ```bash
  python machineLearningModel.py
  ```
- Input sample environmental data to get a prediction.

---

## **Components**
### **Hardware:**
- **Arduino Uno R3**
- **Soil Moisture Sensor**
- **Relay Module**
- **DC Motor (Water Pump)**
- **LED**
- **Resistor**
- **Power Supply**

### **Software:**
- **Tinkercad** → Hardware simulation.
- **MERN Stack** → Web application development.
- **Python** → Machine learning model for plant watering predictions.

---

## License
This project is licensed under the MIT License. See `LICENSE` for details.

---

### 🚀 **Want to Contribute?**
Feel free to open an issue or submit a pull request! Contributions are welcome. 

---
