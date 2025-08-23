## 🔧 Projects

---

### 🚗 Driving Licence Controlled Smart Vehicle  
🔧 **Tech Stack:** STM32, Arduino, C/C++, RC522 RFID, R305 Fingerprint Sensor, GSM (SIM800L), GPS Module  

This project is an embedded vehicle authentication system that prevents unauthorized or underage users from starting a vehicle. It requires the driver to scan an encrypted RFID-based driving license and match their fingerprint before ignition is enabled. Additionally, the system includes accident detection with GPS location reporting through GSM in emergency scenarios.

#### 🔨 My Role & Contributions:
- **Designed complete hardware architecture** integrating STM32 and Arduino platforms with biometric sensors.
- **Implemented authentication logic** using UART protocols for both RFID and fingerprint modules.
- **Wrote embedded C/C++ code** for multi-stage authentication, including:
  - RFID decryption
  - Fingerprint matching
  - Real-time system state handling
- **Developed EEPROM-based storage system** to retain authorized user profiles locally.
- **Integrated accident detection logic** using vibration threshold + GPS location fetch.
- **Sent emergency alerts via GSM** (SMS) using AT commands with dynamic GPS data.
- **Deployed real-time feedback via LEDs** and LCD to guide the driver through authentication steps.
- Successfully demonstrated the project for government funding and **secured ₹73,000 under SSIP** for real-world viability.

---

### 🔥 Autoclave – Heater Controller  
🔧 **Tech Stack:** Nuvoton Mini51 MCU, Embedded C, ADC, PWM, EEPROM, Seven-Segment Display  

An industrial-grade temperature control unit developed for autoclaves or lab-grade sterilizers. The system uses ADC to read temperature, controls heater power via relay + PWM, and stores user-defined thresholds using EEPROM. Designed for high reliability and safety.

#### 🔨 My Role & Contributions:
- **Developed core logic from scratch** using Embedded C in Keil uVision for Mini51 microcontroller.
- **Integrated temperature sensors (analog)** and implemented a **real-time ADC-to-temperature converter**.
- **Used PWM and relay switching** logic to maintain temperature with ±1°C calibration accuracy.
- **Implemented EEPROM memory handling** to store last-set values (min/max temp) even after power loss.
- **Designed interactive user interface** using 3-digit Seven-Segment display and key input:
  - Set temperature limits
  - View current readings
  - Toggle system ON/OFF
- **Calibrated system using test tools** (multimeter + digital thermometer) to fine-tune sensor offsets.
- Enhanced operational safety by adding system timeout and overheat protection logic.
- Focused on memory efficiency and system stability for long-duration continuous usage.

---

### ⚡ Pulse Generator – LCD Controlled  
🔧 **Tech Stack:** Nuvoton M0518 MCU, Embedded C, Timers, EEPROM, LCD 16x2  

A configurable industrial pulse generator used for simulating test signals, frequency sweeps, or pulse injection into circuits. Built with a clean menu-based interface displayed on a 16x2 LCD and operated using pushbuttons.

#### 🔨 My Role & Contributions:
- **Led this project independently** from ideation to implementation and testing.
- Designed embedded logic for:
  - **Precise pulse generation using timers**
  - Adjustable RPM-based frequency output
  - Pulse width and delay control
- **Built a user interface with menu navigation**:
  - Select pulse mode (manual/automatic)
  - Set RPM (100–9999 range)
  - Start/stop pulse sequence
- **Used EEPROM for memory persistence** to retain last-used settings and user preferences.
- **Validated outputs using an oscilloscope** to ensure pulse accuracy and signal consistency.
- Focused on:
  - Memory-constrained UI design
  - Low-latency user inputs
  - Real-time counter refresh without UI flickering
- Final product mimicked commercial test tools in usability and precision, making it ideal for lab testing or production line diagnostics.

---
