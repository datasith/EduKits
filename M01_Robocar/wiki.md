<!--
https://www.youtube.com/playlist?list=PLNFq0T6Z3JPuNaD2kJnZPvROaix67L9bl
https://diyrobocars.com/
-->

<!-- HEADER -->
<br />
<p align="center">

  <h2 align="center">ACROBOTIC EduKit Module 01 – Robocar</h2>

  <p align="center">
    Featuring a wheeled robotic platform for exploring Machine Learning.
    <br />
    <br />
    <a href="https://acrobotic.com/EduKits">Get Hardware</a>
    · <a href="https://discord.gg/hbGxaa">Join Community</a>
    · <a href="https://github.com/acrobotic/EduKits/issues">Bugs & Features</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [Overview](#overview)
  * [Pre-requisites](#pre-requisites)
  * [Parts list](#parts-list)
* [Getting Started](#getting-started)
  * [Connecting to your Robocar](#connecting-to-your-robocar)
* [Usage](#usage)

<!-- ABOUT THE PROJECT -->
## Overview
<p align="center">
  <a href="https://youtube.com/acrobotic/">
    <img src="https://github.com/acrobotic/EduKits/blob/master/images/robocar.jpg?raw=true" />
  </a>
</p>

Recent advances in *driverless vehicle technologies* are rapidly paving the way for autonomous driving. Specifically, breakthroughs in deep learning and its application to autonomous driving. This EduKit Module uses a wheeled robotic platform for exploring the subject of **Machine Learning** applied to **Computer Vision**.

### Objective

To train a wheeled vehicle to complete a closed track course *autonomously* through the collection of images and steering angles during manually controlled runs. Training occurs on [Amazon's Deep Learning](https://aws.amazon.com/deep-learning/) cloud platform, based on the processing of the 
images and steering data by a Keras/TensorFlow neural network model in software.

### Resources

As with every **EduKit Module**, there are several resources included:

* [**Github repository**](https://github.com/acrobotic/EduKits/tree/master/M01_Robocar): code and presentation slides (.pdf)
* [**Github wiki**](#) (this page): user guide
* [**YouTube playlist**](): complimentary tutorial and demo videos
* [**Google Drive directory**](https://drive.google.com/open?id=14y48VQQDh2FVl9tFWuCMQ13i5h8Ak8fS): presentation (.key, .ppt) and supporting materials

### Pre-requisites

Although the **[Robocar Kit](https://acrobotic.com/products/Robocar)** comes ready to run out-of-the-box, some familiarity with programming in Python, as well as with network management is recommended. The chapter on **Linux Fundamentals** for the **[Intro to Physical Computing module](https://github.com/acrobotic/EduKits/wiki/M00%E2%80%9300-PhysComp:-Intro-to-Physical-Computing)** is a good place to start for those needing a little more experience.

### Parts list
<p align="center">
  <a href="https://youtube.com/acrobotic/">
    <img src="https://github.com/acrobotic/EduKits/blob/master/images/robocar_parts.jpg?raw=true" />
  </a>
</p>


### Built With

At the center of this **EduKit Module** we have:

* **[1:18-scale Robocar](https://acrobotic.com/products/Robocar)** with differential steering
* **[Tensorflow](https://www.tensorflow.org/)** Machine Learning library for Python
* **[Amazon's Deep Learning](https://aws.amazon.com/deep-learning/)** cloud platform
* **[Donkey](https://www.donkeycar.com/)**  a high-level self-driving library for Python
* **[Raspberry Pi](https://www.raspberrypi.org/)** single-board computer

<!-- GETTING STARTED -->
## Getting Started

### Module Structure

With ease of use, redistribution, modification, and organization in mind, each **EduKit Module** consists of a few components where all of the materials for each subject can be gathered. These are:

* A **Github repository** in an aptly named sub-directory
* A **Github wiki** in the Github Wiki
* A **YouTube playlist** of complimentary tutorial videos in YouTube
* A **Google Drive directory**

##### Github repository

Here you can find the software and guides for the exercises and demos in each module. It also includes a .pdf version of the instructional presentation for each topic covered in the module. Each repository includes a `README` file with an outline of the contents, and a link to the corresponding wiki page and Google Drive directory.

##### Github wiki

Here you can find an in-depth breakdown of the steps needed to complete the activities and exercises in a module.


##### YouTube playlist

A video collection of demos and step-by-step guides for completing the activities in the module.

##### Gogle Drive directory

Here you can find the original source files of the presentation, and any other large-sized files not apt for storing on the module's Github repository.


### Pre-requisites

With the goal of the widest adoption possible of these **EduKit Modules**, there are no major pre-requisites for getting started. The module "*PhysComp: Intro to Physical Computing*" is aimed to get anyone familiar with the tools needed.

Whereas becoming an expert programmer, data analyst, electronic hardware engineer, etc., can take several years, the goal of the **EduKit Modules** is to provide a shor-term (20~30 hours) of hands-on exposure to a subject matter. This can be done for fun, vocational learning, or as part of an academic curriculum.

### Resources

Outside of the topics covered in **EduKit Modules** the tools used can be applied for a wide variety of applications. The following resources are useful for those interested in exploring beyond the confines of these modules:

* **[Donkey Car Project](https://www.donkeycar.com/)**
* **[Raspberry Pi Education](https://www.raspberrypi.org/education/)**
* **[Instructables](https://instructables.com/)**
* **[Adafruit Learning Resources](https://learn.aduafruit.com)**
* **[ACROBOTIC Projects](https://www.youtube.com/playlist?list=PLNFq0T6Z3JPtnqTKEkmqCogIqQYHUmYu8)**

<!-- USAGE EXAMPLES -->
## Usage

These are some examples of use cases of the EduKit modules in the wild:

For more examples, please refer to the [Wiki](https://github.com/acrobotic/EduKits/wiki)



<!--

Follow the [instructions for installing WebIOPi](https://github.com/acrobotic/Ai_Demos_RPi/tree/master/demos/gpio#webiopi). Run the `setup.sh` script and when prompted to access your Pi from over the Internet, select 'yes'. If you have already installed WebIOPi, run the `./weaved-setup.bin` to install the Weaved IoT Kit and access your device over Internet. You will need to register at [http://developer.weaved.com](http://developer.weaved.com) to access your device.

https://drive.google.com/open?id=14y48VQQDh2FVl9tFWuCMQ13i5h8Ak8fS

## Robotics

### List of Parts

See the spreadsheet for more info about the parts you can use for this application; the main ones are:

1. [Acrobotic Robocar Kit: Mobile Robot Kit with 6V DC MotorsZoom](https://acrobotic.com/kit-00005)
1. [DRV8835 Dual Motor Driver Kit for Raspberry Pi B+](https://acrobotic.com/rpi-00014)

The Robocar Robotics Kit is a great platform for getting started quickly.  The need for a motor driver is due to the Raspberry Pi not being able to source enough current to drive the motors directly.  We've chosen the DRV8835 Dual Motor Driver Kit for Raspberry Pi B+ as it directly plugs onto the Pi, minimizing the wiring and setup for getting started.

Follow the instructions on the Github repository for getting the motors moving:
[https://github.com/pololu/drv8835-motor-driver-rpi](https://github.com/pololu/drv8835-motor-driver-rpi)

You'll need a 6V power supply (a 4xAA battery holder is included in the Kit) to power up the motors. The wiring and placement of the driver board on the Pi should look like this:
![Robocar Robotics Paltform - Wiring](https://github.com/acrobotic/Ai_Demos_RPi/blob/master/images/wiring_markii.jpg)
![Robocar Robotics Paltform - Wiring](https://github.com/acrobotic/Ai_Demos_RPi/blob/master/images/notes_markii.jpg)

## Kiosk/Multimedia display

Other than a VESA-compatible enclosure, you don't necessarily need hardware parts to get started with a kiosk-type application. Notable examples:

1. [https://github.com/MobilityLab/TransitScreen/wiki/Raspberry-Pi](https://github.com/MobilityLab/TransitScreen/wiki/Raspberry-Pi)
1. [One way to get started drawing graphics on an external display is using pygame](https://learn.adafruit.com/pi-video-output-using-pygame/overview)
1. [Tracking the International Space Station (ISS Above)](http://issabove.com)
1. [Using PyMame for building a 1200-game Vintage Arcade](http://hackaday.io/project/2090-raspberry-pi-vintage-arcade) (DIY Kit at acrobotic.com will be available on March 27th, 2015).

-->