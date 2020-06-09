# Build Guide

## Tools You Will Need
- A lot of patience and time
- Soldering station (be safe!)
- 3D printer (or use an online service)
- PCB Manufacture (use an online service)

## Parts
- Raspberry Pi 3B with micro SD card (Micro Controller)
- Powerboost 1000C (Li-Po Charger)
- 8800mAh Li-Po Battery
- 16 Channel PWM Driver (interface over I2C)
- SenseBorg HAT PCB
- Raspberry Pi HAT header pins
- Male Breakaway headers (quite a few ~50 pins, pin spacing 2.54mm)
- 16 NPN Transistors (max current at least 200mA, max voltage at least : 10V)
- 16 Resistors (1K, 0.25W)
- 16 Diodes (optional flyback, max current at least : 200mA, max voltage at least : 10V)
- 16 Pancake Haptic Motors (around 1G force, 5V, current draw max ~100mA)
- Backpack straps with buckle ends (used for the belt)
- M5 self tapping screws (up to 65mm length)
- M2.5 Nuts and Bolts (8 of each, length up to 30mm)
- LOTS of Female jumper cables (>50)
- 9DOF Accelerometer (interface over I2C)
- Lots of wire (~20m)
- 3D Printed custom parts

## Making the SenseBorg HAT
The SenseBorg HAT is the main electronics control hub in this project. It serves primarily as a signal booster for the haptic motors, with 16 distinct inputs and outputs. Signals given as inputs are switched from the main Li-Po power supply, so can draw much more current than the PWM driver can provide, which the motors require.
The HAT also breaks out extra power pins, and I2C pins, and has jumper headers for motors and PWM signals to plug into.


1. Download the PCB files from the build folder of this respository.
2. Either open the .brd files in Eagle and export gerber files as required by your PCB making service, or use the gerber files provided.
3. Get the PCB made, and delivered.
4. Solder the transistors, resistors, diodes and headers.
5. You should now be left with a functional SenseBorg HAT.


## Making the Motor Clips
TODO

## Wiring Overview
The whole system is powered by the 8800mAh Li-Po. This lipo plugs into the PowerBoost 1000C via the battery connector. If your battery doesn't have a connector, it can be soldered in to the BAT and GND connections. Also solder in headers to the adjacent 5V and GND connections. Finally cut your USB cable about 15cm from the micro USB end. Strip the cut end of the cable and isolate the power and ground wires. Solder these to the 5V and GND connections on the board. Since you've already soldered headers to the main breakouts, use the connections meant for a USB A header which we won't need for this project.

The Powerboost 1000C also boosts the Lipo's 3.3V to 5V, so this power needs to be connected to everything which needs power in the system. Use female-female jumpers to connect the PWR headers from the Powerboost 1000C to the VIN on the SenseBorg HAT. The USB cable will be plug into the Raspberry Pi to power it.

The SenseBorg HAT is placed onto the Raspberry Pi (as HAT's are). +5V, GND, SDA and SCL should be connected to the relevant pins on the 16 Channel servo driver (solder headers to this). Use these pins from the HAT's GPIO header pins, to save the extra I2C and PWR pins broken out for your I2C sensor.

Use female-female jumper cables to connect each PWM output from the 16 Channel PWM driver to each of the 16 inputs on the SenseBorg HAT (each input is the single pin on each triangle (the other two are for the motors)).

Use female-female jumper cables, spliced with longer wires to create super long female-female jumper cables to connect each motor output (each pair from the groups of 3 headers on the SenseBorg HAT), to the two pins on each motor clip. Polarity doesn't matter.
These are all the electronic connections required. Have a look at photos for reference, and the circuit diagram too.

TODO ADD PHOTOS, SCHEMATICS, DIAGRAMS, MORE INFO ETC