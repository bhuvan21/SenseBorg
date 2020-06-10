# Build Guide
I appreciate this guide is very long, but it contains all the information needed to build one SenseBorg Belt, and my IMU headband.  
Please read the whole guide, as I'll admit not all information is placed in the best order (but it is all here)

![Blueprint](/build/blueprint.jpg?raw=true)

## Tools You Will Need
- A lot of patience and time
- Soldering station (be safe!)
- Hot glue gun or superglue
- Wire Stripper (or scissors if you're willing)
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
- Heatshrink (ideally)
- Hot Glue sticks (ideally)
- 3D Printed custom parts
- A fanny pack

## Making the SenseBorg HAT
The SenseBorg HAT is the main electronics control hub in this project. It serves primarily as a signal booster for the haptic motors, with 16 distinct inputs and outputs. Signals given as inputs are switched from the main Li-Po power supply, so can draw much more current than the PWM driver can provide, which the motors require.
The HAT also breaks out extra power pins, and I2C pins, and has jumper headers for motors and PWM signals to plug into.


1. Download the PCB files from the build folder of this respository.
2. Either open the .brd files in Eagle and export gerber files as required by your PCB making service, or use the gerber files provided.
3. Get the PCB made, and delivered.
4. Solder the transistors, resistors, diodes and headers.
5. You should now be left with a functional SenseBorg HAT.

![Blank HAT](/build/unsoldered_hat.jpg?raw=true)
![Soldered HAT](/build/soldered_hat.jpg?raw=true)

## Making the Motor Clips
Each haptic motor is part of a motor clip. These motor clips clip around the belt at regular intervals, with the motors facing towards to wearer. This solution allows for a variable number of motors and placements. This helpes the belt work for all waist sizes. Each motor clips requires:
- 3D Printed Motor Clip
- Pancake Vibration Motor
- 2 breakaway headers

1. 3D print the Motor Clip (found in motorclip.stl)
2. Solder the ends of the wires on the pancake motor to the two breakaway headers. Use heatshrink (ideally)
3. If your motor has adhesive on the back, pull off the protective tab and stick the pancake motor into the circular indent on the clip. The wires from the motor should be facing towards the indented rectangle on the clip (towards the pivot of the clip).
4. Wrap the wires around the pivot of the clip, so that the headers rest parallel to the clip on the other side, in the provided indent. Secure them in place with glue of some kind.

You should now have finished a single motor clip. You will need ~16 of these.

![Motor Clip Side](/build/motorclip_side.jpg?raw=true)
![Motor Clip Back](/build/motorclip_back.jpg?raw=true)


## Board Arrangement
There is probably a better way of arranging all these boards, but improvements will come in V2.
The box and its top will need to be 3D printed (see box.stl and top.stl)
Below is a diagram of where the boards should go, and a picture of what this looks like.
Ideally all the nuts and bolts will hold everything in place, but feel free to be liberal with glue if needed (an unfortunate reality)

PIC

## Wiring Overview
This section lists all the wiring that needs to be done. I suggest doing all the soldering first, and then doing the wiring after placing all the boards into the container.
The whole system is powered by the 8800mAh Li-Po. This lipo plugs into the PowerBoost 1000C via the battery connector. If your battery doesn't have a connector, it can be soldered in to the BAT and GND connections. Also solder in headers to the adjacent 5V and GND connections. Finally cut your USB cable about 15cm from the micro USB end. Strip the cut end of the cable and isolate the power and ground wires. Solder these to the 5V and GND connections on the board. Since you've already soldered headers to the main breakouts, use the connections meant for a USB A header which we won't need for this project.

The Powerboost 1000C also boosts the Lipo's 3.3V to 5V, so this power needs to be connected to everything which needs power in the system. Use female-female jumpers to connect the PWR headers from the Powerboost 1000C to the VIN on the SenseBorg HAT. The USB cable will be plug into the Raspberry Pi to power it.

The SenseBorg HAT is placed onto the Raspberry Pi (as HAT's are). +5V, GND, SDA and SCL should be connected to the relevant pins on the 16 Channel servo driver (solder headers to this). Use these pins from the HAT's GPIO header pins, to save the extra I2C and PWR pins broken out for your I2C sensor.

Use female-female jumper cables to connect each PWM output from the 16 Channel PWM driver to each of the 16 inputs on the SenseBorg HAT (each input is the single pin on each triangle (the other two are for the motors)).

Use female-female jumper cables, spliced with longer wires to create super long (~70-90cm) female-female jumper cables to connect each motor output (each pair from the groups of 3 headers on the SenseBorg HAT), to the two pins on each motor clip. Polarity doesn't matter.
Use similarly long jumper cables to connect the broken out I2C and PWR pins to connect the pi to the I2C sensor.
These are all the electronic connections required. Have a look at photos for reference, and the circuit diagram too.


## Putting Together

1. Place all boards in as specified in the Board Arrangement section. Ensure they are held in place by the relevant nuts and bolts.
2. Plug the battery into the Powerboost, and place the battery outside the box.
3. Connect PWR from the HAT VIN with jumper wires.
4. Connect PWR and I2C from the HAT to the PWM driver.
5. Connect each of the 16 PWM outputs from the PWM driver to each of the 16 PWM inputs.
6. Connect each pair of 16 super long jumper cables (tape two together in the mid section to ensure you have both ends of a motor for each pair) to each of the double header motor outputs from the HAT.
7. Bring the ends of these 32 jumpers through the circular hole in the box and out.
8. Use 4 more of these long jumpers to connect to the broken out I2C and PWR on the HAT. Mark these with tape on their ends to avoid confusion with motor jumpers. Bring these out of the box the same way.
9. Plug the micro USB cable from the Powerboost into the pi.
10. Check all electronics are connected correctly (check Wiring Overview and circuit diagram)
11. Place the battery inside the box (should fit comfortably).
12. Place the lid on top of the box (may have to rotate or flip to get holes to line up)
13. Use the self tapping screws to secure the lid onto the box.
14. Connect each pair of motor long jumpers to the headers on a motor clip.
15. Connect the I2C connections to your I2C sensor.
16. Clip the clips uniformly around a length of backpack strap (should be the target waist length + a few inches for tightening). Be careful with how you route wires here, it will matter.
17. Add the buckle pieces on either end of the strap.
18. Cut another length of strapping, and add buckles to this too.
19. Attach this across the fanny pack in some way, with the pack attached at the middle of the belt.
20. Place the electronics box into the pack, and zip up as much as possible, whilst letting wires come out.
21. You may now need to adjust how you've routed your motor wires, to minimise crossovers, but you should now be done!

|  1  |  2  |  3  |  4  |
|:---:|:---:|:---:|:---:|
| ![Assembly 1](/build/assembly1.jpg?raw=true) | ![Assembly 2](/build/assembly2.jpg?raw=true) | ![Assembly 3](/build/assembly3.jpg?raw=true) | ![Assembly 4](/build/assembly4.jpg?raw=true) |

![Finished](/build/complete.jpg?raw=true)

To put on the belt, first attach the belt holding the electronics pack, then the belt with the motors. Ensure the two belts do not overlap, and are around your midsection. It may be easier to do this whilst standing up!

Congrats, the belt is now done from a hardware standpoint! If you would also like to make the headband I did, to approximate the sense of balance, instructions are below.
Have a look at the Belt class to see how the code works. You will likely have to use calibrate_order.py to determine which PWM outputs map to which motors, so that they can be interfaced with smoothly. Once all done, edit test_main.py and go for it! If you are using a different sensor, you'll have to implement your own mainloop, similar to my example

## IMU Headband
Acquire a regualr head/hair band. It should be thin, so that a clip can fit on it.
1. 3D Print a regular clip (clip.stl)
2. Secure an IMU either of the clip's flat faces. (glue)
3. Clip the clip onto the headband such that when word, the IMU is position near the back of the head, straight up.
4. Connect the long jumper I2C and PWR connections to the IMU.

![IMU Clip](/build/IMU_clip.jpg?raw=true)  
![IMU Headband](/build/IMU_headband.jpg?raw=true)

TODO ADD PHOTOS, SCHEMATICS, DIAGRAMS, MORE INFO ETC