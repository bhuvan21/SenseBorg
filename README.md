# SenseBorg
A modular platform for human sensory substitution via haptic feedback.  

## Introduction
The concept of sensory substitution involves supplying sensory stimuli through a sensory modality usually used for gathering different sensory data  – and has an important role to play in rehabilitation those with vestibular impairments. Sensory substitution requires the use of a specific device, which uses artificial sensors to collect sensory data, and delivers this data to a subject via one of their sensory modalities (e.g touch, audio, visual). Devices which do this are called sensory substitution devices (SSDs).


## The Project
Sensory Substitution Devices require two parts.  
1. Some way to provide artificial stimuli  
2. Some way to generate this stimuli (usually a sensor of some kind)  

Good examples of this are the BrainPort and feelSpace belt devices. My project nicknamed "SenseBorg" (think Senses + Cyborg) is my contribution to this under-explored area of research.  

These two parts of my project are:
1. A custom belt, with up to 16 embedded haptic motors, for generating artificial stimuli with selectable position and strength.  
2. An IMU headband for sensing rotational acceleration, as an approximation of the sense of balance.  

The second part of the project can be easily substituted for any other sensor, which could be used to conduct experiments into learning other sensorimotor contingencies.  
Thus, this project provides a platform for providing artificial stimuli for use in more general sensory substitution experiments.


## The Belt
The specifics of the physical hardware in the SenseBorg belt is more detailed in the build folder, specifically BUILD.md. However, the basic features are as follows.  
- 12h battery life
- 16 different motor channels, each with PWM control
- Wifi enabled
- Bluetooth capabilities
- Modular as haptic motors can be placed variably on the belt to accomodate for different waist sizes
- ~2A Charging rate (if your charger can handle it) for overnight charging


## This Repository
This repository contains the software and hardware information for the SenseBorg belt itself. Of course, a lot of the software is specific to interfacing with my specific sensor system, and translating this into targeted haptic feedback. Please have a look at build/BUILD.md for a build guide. This project is currently in it's first iteration, so is subject to change and improvement.


## Results
After a first experiment, the hypothesis that the wearing of this belt would result in an increase in the wearer's sense of balance, was shown to be statistically significant. (Balance was tested via a sharpened Romberg Test, the belt was worn over a week period for 12 hours a day, the statistical difference was measured via a T-test, and the final p < 0.01)
My research paper based on this device is currently pending publication.
