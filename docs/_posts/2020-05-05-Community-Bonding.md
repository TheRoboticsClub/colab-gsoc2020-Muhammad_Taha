---
title:  "Community Bonding Period"
date:   2020-05-05
categories: update
tags: jekyll
---
May 4, 2020 - May 31, 2020

## Week-1
The first week was spent in having an intitial meeting with my mentor in which we discussed how out project was going to be organized. I was  asked to create this blog using Jekyll minimal mistakes template and briefed about how to maintain it. We also discussed about our weekly meetings and how we should keep track of our development progess. I was given access to the the required repositories on GitHub and had a look at the previous prototype of the VisualCircuit Tool. I also read the code-base of the IceStudio tool, as some of its modules are to be used by our tool.

## Week-2
During the second week, I was asked to develop a basic functioning prototype of the front-end in Node.js by using IceStudio as a starting point. Unfortunately I ran into some installation issues with IceStudio. I created an issue on the IceStudio repository:
https://github.com/FPGAwars/icestudio/issues/410. 

Then I started working on next week's task which was to create a basic prototype of the Python back-end using threads. It consisted on implementing basic Python driver blocks and setting up appropriate connections using wires. I created a new branch for the project which was completely independent of the previous version of VisualCircuit.

The project can be found on:
https://github.com/JdeRobot/VisualCircuit/tree/experimental

In the beginning, a camera, an edge detector and a screen module were implemented. The Addition of Modules issue and the pull request can be found on:
https://github.com/JdeRobot/VisualCircuit/issues/13

The YouTube video for the working python prototype can be found on:
https://www.youtube.com/watch?v=bemMHKJL1Iw

## Week-3
During the third week, the threaded application was to be converted into a multi-process based solution as Python threading module does not support multiple cores due to Global Interpreter Lock (GIL). This was challenging because all of the driver blocks needed to be run on seperate processes at fast iterations with minimal overhead. As the wires between the blocks were shared memory so the  processes were not mutually exclusive and I needed to synchronize them to prevent race conditions. The solution which I went with was shared memory in the Python multiprocessing module. The shared memory was basically a numpy array with fixed size created using the multiprocessing.Array() function. There was a Wire class that acted as an interface for reading, writing and synchronizing the shared memory. Each instance of wire inherited the shared memory and was passed into its corresponding process. The processes used this Wire instance to read and write to the shared memory.

![alt_text]({{ "assets/images/week3.jpg" | absolute_url }})
