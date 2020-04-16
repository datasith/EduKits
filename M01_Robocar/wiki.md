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

To train a wheeled vehicle to complete a closed track course *autonomously* through the collection of images and steering angles during manually controlled runs. Training occurs on either your computer or [Amazon's Deep Learning](https://aws.amazon.com/deep-learning/) cloud platform, and it's based on the processing of the images and steering data by a Keras/TensorFlow neural network model in software.

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
  <a href="https://www.youtube.com/watch?v=bEzZYanygzA&t=492">
    <img src="https://github.com/acrobotic/EduKits/blob/master/images/drive_ui.png?raw=true" />
  </a>
</p>
You can now control your car from a web browser at the URL: **http://raspberry-pi-ip-address:8887**

<!-- GETTING STARTED -->
## Usage

* Get ready to work on your Machine Learning model:

This will require you to access the **Raspberry Pi** remotely. The chapter on **Linux Fundamentals** for the **[Intro to Physical Computing module](https://github.com/acrobotic/EduKits/wiki/M00%E2%80%9300-PhysComp:-Intro-to-Physical-Computing)** is a good place to start for those needing a little more experience. Once you're ready, establish an `ssh` connection with your **Raspberry Pi**.

* Practice and restart the **Robocar Software**:

Practice driving around the track until you're confident you can drive 10 laps without mistake. Once you're ready, restart the software from an `ssh` connection.

<!-- ... -->
    systemctl --user restart donkeycar.service

* Collect (good) data:

After restarting the software, press `Start Recording` using the web interface. The joystick will auto record with any non-zero throttle. If you crash or run off the track press Stop Car immediately to stop recording. After you've collected 10-20 laps of good data (5-20k images) you can stop your car with:

<!-- ... -->
    systemctl --user stop donkeycar.service

The data you've collected is in the data folder in the most recent `tub` folder. The `tubs` can be located by:

<!-- ... -->
    ls ~/Work/borrego/data/

* Copy the data to your computer (or an Amazon server):

In a terminal session on your host computer use `scp` to copy the contents of your `data` folder from the **Raspberry Pi**, or the latest `tub` for the sake of efficiency.

<!-- ... -->
    scp -r pi@raspberry-pi-ip-address:~/Work/borrego/data/*  ~/your-car-name/data/
    
* Train a model:

As the **Raspberry Pi** lacks the computing power to train the **Machine Learning** model quickly, you can now run the training script on the latest `tub` on your computer. This requires passing the path to that tub as an argument to the `manage.py` script. You can optionally pass path masks, such as ./data/* or ./data/tub_?_17-08-28 to gather multiple tubs. For example:

<!-- ... -->
    python ~/mycar/manage.py train --tub <tub folder names comma separated> --model ./models/mypilot.h5

Optionally you can pass no arguments for the `tub`, and then all `tubs` will be used in the default data directory.

<!-- ... -->
    python ~/mycar/manage.py train --model ~/mycar/models/mypilot.h5
    
* Copy the model back to the Robocar:

We'll need to copy the trained model from the previous step into the appropriate directory on the **Raspberry Pi**. We'll use `scp` once again with the source and destination in reverse order:

<!-- ... -->
    scp -r ~/your-car-name/models/* pi@raspberry-pi-ip-address:~/Work/borrego/models/.
    
* Run your Robocar in autopilot mode:

Position the **Robocar** on the track so that it is ready to drive. Ensuring that the background process is stopped:

<!-- ... -->
    systemctl --user status donkeycar.service

Navigate to the approriate directory:

<!-- ... -->
    cd ~/Work/borrego

And then start the `manage.py` script passing it your model to drive:

<!-- ... -->
    python manage.py drive --model models/mypilot.h5
    
* Congrats, you're now running an autonomous vehicle!
