<h1 align="center">Tirth Patel</h1>
<h3 align="center"><i>Embedded Systems | Firmware Development | Electronics Hardware</i></h3>

<p align="center">
  <img src="https://img.shields.io/badge/Microcontrollers-STM32%20%7C%20Nuvoton-blue?style=flat-square&logo=arm" />
  <img src="https://img.shields.io/badge/Firmware-C%20%7C%20Embedded%20C-informational?style=flat-square&logo=c" />
  <img src="https://img.shields.io/badge/Debugging-Real%20Time%20Systems-critical?style=flat-square&logo=raspberrypi" />
  <img src="https://img.shields.io/badge/Team-Project%20Driven-success?style=flat-square&logo=github" />
</p>

---

### 📍 Pomona, CA | 📧 [tirth.p2812@gmail.com](mailto:tirth.p2812@gmail.com) | 🔗 [GitHub](https://github.com/tirth2812)

Welcome to my GitHub portfolio! I'm an **Electrical and Electronics Engineer** with hands-on experience in firmware development, embedded UI design, and microcontroller-based system integration.

> “Innovation lives at the intersection of firmware.”

---

## 🧠 Summary

Electrical and Electronics Engineer with hands-on experience as an Embedded Software Engineer, focused on firmware design, hardware testing, computer architecture, and system optimization. Experienced in C/C++ programming, debugging, and structured test planning to deliver reliable microcontroller-based solutions. Experienced in troubleshooting integrated hardware/software systems and collaborating with cross-functional teams to achieve project milestones. Experienced with STM32, Arduino, and Nuvoton microcontrollers, working with UART, I²C, SPI, EEPROM, sensors, and displays to build real-time embedded solutions. Accomplishments include leading a startup-funded smart vehicle project (₹73,000 SSIP Fund) and participating in hackathons with innovative embedded system designs. 

---

## 🎓 Education

**MS – Electrical and Electronics Engineering**  
📍 California State Polytechnic University, Pomona, USA  
🗓️ Jan 2025 – Present

**BE – Electronics and Communication Engineering**  
📍 Gujarat Technological University, India  
🗓️ Jun 2020 – Jun 2024

---

## 💼 Work Experience

### 🔹 System Engineer  
**Northrop Grumman Collaboration Project** | Aug 2025 – Present  

- Derived system-level requirements and identified potential risks for UGV (Unmanned Ground Vehicle) systems.  
- Created models and diagrams to support key design reviews including **System Requirements Review (SRR)** and **Preliminary Design Review (PDR)**.  
- Prepared technical documentation to ensure alignment with Northrop Grumman standards.  
- Coordinated with the Electrical Team and sub-teams to align work with overall mission objectives.  
- Supported validation of electrical subsystems and ensured consistency with mission requirements.  

---

### 🔹 Embedded Software Developer  
**Inoweave** | Jan 2024 – Jun 2024  

- Programmed **STM32** and **Nuvoton microcontrollers (MCUs)** in C/C++, applying **Test-Driven Development (TDD)** and **Continuous Integration/Continuous Deployment (CI/CD)** practices with daily Git commits to ensure reliable firmware performance with ±1 °C calibration accuracy.  
- Designed **pulse-generation logic** and implemented **signal-processing routines**, using automated testing and structured debugging to improve timing precision and responsiveness.  
- Built real-time **graphical displays** using LCDs, Lunacy, and TouchGFX, and optimized low-level firmware to improve user feedback responsiveness by ~50%.  
- Integrated communication protocols such as **Inter-Integrated Circuit (I²C)** and **Universal Asynchronous Receiver-Transmitter (UART)** for reliable device interfacing and data exchange.  
- Authored **design documentation** and participated in **design reviews** to ensure traceability, maintainability, and compliance with engineering standards.  

---

### 🔹 Hardware Testing & Assembly  
**Nexinnovation** | Jun 2023 – Jul 2023  

- Executed comprehensive hardware testing using **oscilloscopes, multimeters, and signal analyzers**, verifying full system functionality and ensuring performance adherence.  
- Conducted diagnostic evaluations and structured debugging procedures to identify hardware issues, achieving a ~20% reduction in failure rates.  
- Coordinated assembly and testing tasks in collaboration with project partners, improving completion efficiency by ~15% while meeting strict project schedules.  
- Gained experience in **teamwork, troubleshooting, and assembling embedded hardware prototypes** to deliver reliable results.  

---

### 🔹 GTU Surat Student Coordinator  
**Gujarat Technological University** | Jun 2022 – Jun 2024  

- Increased Instagram engagement for **@anveshan.gecsurat** by 30%.  
- Designed consistent **visual UI/UX** for events and updates.  


---

## 🔧 Projects

---

### [🚗 Driving Licence Controlled Smart Vehicle](https://github.com/tirth2812/driving_licence_controlled_smart_vehicle)  
🔧 **Tech Stack:** STM32, Arduino, C/C++, RC522 RFID, R305 Fingerprint Sensor, GSM (SIM800L), GPS Module  

This project is an embedded vehicle authentication system that prevents unauthorized or underage users from starting a vehicle. It requires the driver to scan an encrypted RFID-based driving license and match their fingerprint before ignition is enabled. Additionally, the system includes accident detection with GPS location reporting through GSM in emergency scenarios.

#### 🔨 My Role & Contributions:
- **Designed complete hardware architecture** integrating STM32 and Arduino platforms with biometric sensors.
- **Handled full hardware wiring and physical assembly**, ensuring reliable power distribution, module placement, and secure signal routing across all components.
- **Integrated accident detection logic** using vibration threshold 
- **Deployed real-time feedback via LEDs** and LCD to guide the driver through authentication steps.
- Successfully demonstrated the project for government funding and **secured ₹73,000 under SSIP** for real-world viability.
---

### [🔥 Autoclave – Heater Controller](https://github.com/tirth2812/Heater_controller)  
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

### [⚡ Pulse Generator](https://github.com/tirth2812/Pulse_generator)  
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


## 🛠️ Skills

Programming Languages: 
C, C++, Python, Java, Verilog, Assembly, HTML, Embedded Language

Software Tools: 
Keil uVision, Xilinx Vivado, Visual StudioCode, Git, Microsoft Office Suite, MATLAB

Embedded & System Skills: 
GPIO, PWM, Timers, ADC, I2C, SPI, UART, EEPROM, RTOS fundamentals, TCP/IP, Firmware Design, data structures, Embedded Code, Operating Systems, Debugging Procedures, Troubleshooting, Arduino, STM32, object-oriented computer programming, systems programming.

Strengths: 
Software Engineering, Optimization, Low-level System Design, Problem-Solving, Algorithmic Thinking, Independent Projects, Team Collaboration, Cross-functional Collaboration, Detail-oriented, Analytical Skills, Growth Mindset

Workplace Competencies: 
Teamwork, Professionalism, Time Management, Organizational Skills, Abilityto Work Independently.


---

## 🏆 Achievements

- 🏆 **SSIP Startup Grant** – ₹73,000 for Smart Vehicle Project  
- ⚙️ **Solo Builder** – Designed and deployed full pulse generation system  
- 🎨 **Design Lead** – Created social content for GTU @anveshan.gecsurat

---

## 🌐 Contact

- 📧 Email: [tirth.p2812@gmail.com](mailto:tirth.p2812@gmail.com)  
- 📱 Phone: +1 (909) 762-0503  
- 🌍 Location: Pomona, CA  
- 📄 [**Resume**](https://www.dropbox.com/scl/fi/130l3w20dr65ry51caii7/TIRTH-PATEL.pdf?rlkey=0hdpqypl48ai3q8f8yrkiwunm&st=7xcx5n2l&dl=1)


---

<p align="center">
  <b><p align="center">
  <b>Every experiment leads to growth — thank you for visiting! 🌱🔬</b>
</p>

</p>
