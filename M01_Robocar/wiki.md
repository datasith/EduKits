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
    · <a href="https://discord.gg/v3EWWZJ">Join the Community</a>
    · <a href="https://github.com/acrobotic/EduKits/issues">Bugs & Features</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [Overview](#overview)
  * [Objective](#objective) 
  * [Resources](#resources)
  * [Pre-requisites](#pre-requisites)
  * [Parts List](#parts-list)
  * [Built With](#built-with)
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

### Parts List
<p align="center">
  <a href="https://youtube.com/acrobotic/">
    <img src="https://github.com/acrobotic/EduKits/blob/master/images/robocar_parts.jpg?raw=true" />
  </a>
</p>

The **[Robocar Kit](https://acrobotic.com/products/Robocar)** comes pre-assembled, but it is comprised by:

* 2 x DC Motors, wheels, and mounting brackets
* Caster wheel
* Laser-cut chassis
* USB camera
* Battery meter
* PCA9685 PWM board
* L298N motor driver
* Battery holder
* Raspberry Pi 3
* MicroSD card with a pre-flashed custom image of Raspbian
* HDMI cable
* USB adapter for MicroSD cards
* Assembly hardware

The **Robocar Software** is loaded onto the latest image of the [Raspbian Operating System](https://www.raspberrypi.org/downloads/raspbian/), and it's pre-flashed onto the MicroSD card included with the kit.

### Built With

At the center of this **EduKit Module** we have:

* **[1:18-scale Robocar](https://acrobotic.com/products/Robocar)** with differential steering
* **[Tensorflow](https://www.tensorflow.org/)** Machine Learning library for Python
* **[Amazon's Deep Learning](https://aws.amazon.com/deep-learning/)** cloud platform
* **[Donkey](https://www.donkeycar.com/)**  a high-level self-driving library for Python
* **[Raspberry Pi](https://www.raspberrypi.org/)** single-board computer

<!-- GETTING STARTED -->
## Getting Started

<!-- Assembly Video -->

The **[Robocar Kit](https://acrobotic.com/products/Robocar)** comes with a pre-flashed image loaded with the latest version of Raspbian, and the **Robocar Software**, which is a fork of the original **[Donkey Car](https://www.donkeycar.com/)** software that's been adapted to run on this specific robotic platform. For those starting from scratch, the first two guides should get them up to speed.

* Flashing Raspbian to an SD Card (optional):
<p align="center">
  <a href="https://youtu.be/ndkM6O9tTm8">
    <img src="http://img.youtube.com/vi/ndkM6O9tTm8/0.jpg" />
  </a>
</p>
You can also follow the same procedure for flashing the custom version developed for the **Robocar EduKit Module** located on the corresponding [**Google Drive directory**](https://drive.google.com/open?id=14y48VQQDh2FVl9tFWuCMQ13i5h8Ak8fS).

* Connecting the Raspberry Pi to Wi-Fi (necessary) and configuring remote access over SSH (optional);
<p align="center">
  <a href="https://youtu.be/h3cCHN3MBvs">
    <img src="http://img.youtube.com/vi/h3cCHN3MBvs/0.jpg" />
  </a>
</p>
**TL;DW**: connect the MicroSD card to the computer and in the partition `boot` create two files named `wpa_supplicant.conf` and `ssh`. The former should contain:

<!-- ... -->
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1
    country=YOUR_COUNTRY_CODE

    network={
        scan_ssid=1
        ssid="YOUR_SSID"
        psk="YOUR_PASSWORD"
    }
Note that there might be issues with **5GHz networks**. The latter file should be empty.

* Drive your Robocar:
<p align="center">
  <a href="https://youtube.com/acrobotic/">
    <img src="https://github.com/acrobotic/EduKits/blob/master/images/robocar_parts.jpg?raw=true" />
  </a>
</p>
You can now control your car from a web browser at the URL: **http://raspberry-pi-ip-address:8887**


















