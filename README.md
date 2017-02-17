# ev3dev-curriculum
College curriculum for using ev3dev in a Python programming course.<br>
<br>
This repository is meant to be used as the starting code for students that are learning to use the Lego EV3 Mindstorms robot + ev3dev with Python.<br><br>
Some background information will be provided here with links to other documentation.  The assumption is that before
you begin using this repository to learn ev3-python you first have setup your Lego Mindstorm EV3 with ev3dev as
discussed in the **Background information**.

Once all the setup is done (by an instructor before the clas begins) this repository can be used with students.
 - [Link to instructor pre-class setup](https://drive.google.com/open?id=1jNlT9JKff3p9TyrDQwF3XjakaLEp_ilD1wNaHr7c67o)
  
  ### Introductory material
  - [Installing PyCharm Professional](https://drive.google.com/open?id=1MXThtuT79o6_SmovrWtPNulhi423kdGGDxMsu7LZXt4)
  - [Robot Overview](https://drive.google.com/open?id=17xGhRQt3VTX3Ltg_2FE2_aC7nSCNqHZzLzyaS6N8Yb4)
  - [Git Setup](https://drive.google.com/open?id=12pTxnipJExUwPePExfMmDJIu1Yi-nSzfA7sVh1mHTg4)
  - [Connecting from PyCharm to EV3](https://drive.google.com/open?id=15cYiil-p30to6tcTKZdxGlgHFTFg8EivHJV6Z-Om64s)
   
  ### Motor Drive
  - [Lecture slides](https://drive.google.com/open?id=1rjkOZNw0mO0pH7Ovhy-7riYG3Xa4xq4rKbwMPhDppJs)
  - [Starting code](https://github.com/Rosebotics/ev3dev-curriculum/tree/master/sandbox/src/motors)
  - [Checkoff sheet](https://drive.google.com/open?id=14_BQghdiRCOzJ5V_edXhcmaZFhH1qzkzL2u50uH6_o0)

  ### Digital Inputs (and a few other things)
  - [Lecture slides](https://drive.google.com/open?id=1mUxsC-cUO4S5bwhTAQG0G10IO0gsbAU5YEORxeh0mMc)
  - [Starting code](https://github.com/Rosebotics/ev3dev-curriculum/tree/master/sandbox/src/motors)
  - [Checkoff sheet](https://drive.google.com/open?id=1jrrmd-c1ZuWV1qujV8d-H327HWFmADSCdm9wgafYQ8M)

  ### MQTT Communication
  - [Lecture slides](https://drive.google.com/open?id=1gQt1K4X2xzcspKMn2S0X98vhzVNmLA-xoQe5rp58CVE)
  - [Starting code](https://github.com/Rosebotics/ev3dev-curriculum/tree/master/sandbox/src/motors)
  - [Checkoff sheet](https://drive.google.com/open?id=1f83A70S_OA6eor-Ta9HsM40V9qwOVa12JU_e0qaujm4)

  ### Analog Sensor
  - [Lecture slides](https://drive.google.com/open?id=1U00IlFqIT_S2v9HV-TKSO6Y6foH4sDom9yytsV_PWfY)
  - [Starting code](https://github.com/Rosebotics/ev3dev-curriculum/tree/master/sandbox/src/motors)
  - [Checkoff sheet](https://drive.google.com/open?id=1J5Is9eiEueDT-mcJAhQSatzsXma4JVPaU4a7vXlkXAc)
  - [Color squares](https://drive.google.com/open?id=1ed_vWTfOu15ziF8nfZwhjrRcSufKODhQtAmY8lsGNAc)


## Background information
Typically the EV3 is programmed with a block based programming language that is available for Windows and OS X. 
https://www.lego.com/en-us/mindstorms/downloads/download-software

There is also a lightweight version of that program available for iPad and Android tablets: 
https://www.lego.com/en-us/mindstorms/apps/ev3-programmer-app

Block based languages are a great way to get started, but at some point in your programming journey, it's time to move
away from block based languages (like Scratch) and move into the more traditional text-based programming languages.
One of the best, first languages to learn is Python. Using the Lego EV3 with Python can be a lot of fun and it can help
motivate learning.  There are really only 2 factors limiting more schools from using EV3 + Python.
- Costs (sorry can't help you with that one)
- Technical challenges (that one we can help with)

Indeed it takes someone with a bit of tech savvy to get started, but there are a lot of great tools to help.
This repository uses some of those great tools and tries to provide examples and links to use them.

First we start with the operating system on the EV3 programming brick.  Instead of using the default operating system
that ships with the EV3 from Lego we'll dual boot using an SD card. The new os is called **ev3dev** and it's based on Linux.
http://www.ev3dev.org/

ev3dev can use many different programming languages, not just Python. We only care about Python though.  In
order to use Python we need to leverage a Python library, so that we have commands to communicate the the motors and 
sensors on the board.  The built-in Python library that ships with ev3dev is called python-ev3dev.<br>
Github: https://github.com/rhempel/ev3dev-lang-python
<br>
Documentation: http://python-ev3dev.readthedocs.io/en/latest/

In order to use ev3dev with read the Getting Started page on ev3dev.org.
http://www.ev3dev.org/docs/getting-started/

Then for the robots we use at Rose-Hulman I did some additional customizations. Starting in 2016 we built a fleet of 10
EV3 robots to use in our CSSE120 Introduction to Programming course at Rose-Hulman. Here is a doc which
documents some Rose-Hulman specific work and our customizations. 
https://docs.google.com/document/d/1jNlT9JKff3p9TyrDQwF3XjakaLEp_ilD1wNaHr7c67o/edit?usp=sharing

Once you have your robots setup and rockin you need material to teach students how to use the robot.  That is where
this repository begins.

## What is in this repository

  The purpose of this repository is to share the work we’ve done at Rose-Hulman to use ev3dev in the classroom.  We’ve setup a series of exercises for students to learn the Python ev3dev API.  Instructors at other schools can use any amount of our content in their own course or simply review our work as inspiration.
  
This repository is broken into different folders that each have a different purpose:
- `examples` - Finished examples that can be run to demo different robot features. Reference the code in this folder when doing your own work. 
- `libs` - A special folder that will contain modules that are available to all other modules. Students will be given an mqtt module and will be expected to build their own robot controller module.
- `sandbox` - This folder has 5 subfolders that all start out identical.  Each identical subfolder is for 1 team member to work individually while learning ev3dev and while doing initial development in a contained environment for their work.
- `project` - This folder is for the course final project code.  Modules can be moved from the sandbox into this folder and work and be integrated into a single combined project.

## Getting started

To get started with this tutorial you need upload the code into a folder on EV3.  Since this
repository is for csse120 (change that name as needed to match your course) you need to make sure to push the code onto the EV3 into the folder /home/robot/csse120.  That folder path is only important for the libs folder which must be at the folder path /home/robot/csse120/libs.  This path can change if an instructor does the setup differently.

Once uploaded to your EV3 try some of the example programs, then start working the TODOs in a sandbox folder.
We recommend you use PyCharm Professional (not PyCharm Edu).  University students can get
a free copy of PyCharm Professional.   https://www.jetbrains.com/student/

To setup PyCharm Professional with EV3 visit this tutorial.
http://www.ev3dev.org/docs/tutorials/setting-up-python-pycharm/#additional-features-for-the-pycharm-professional-version
or use the documentation links provided at the start of this README.

Once you are up and running you can start using this repository.
