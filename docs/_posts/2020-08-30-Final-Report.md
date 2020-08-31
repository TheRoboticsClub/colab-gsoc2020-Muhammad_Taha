---
title:  "Final Report"
date:   2020-08-30
categories: progess
tags: jekyll

---


## Summary

JdeRobot is an open toolkit for developing robotics applications. The toolkit provides several tools, libraries and reusable nodes for Robotics and Computer Vision. My project was an addition of a new tool to this organization. This project aimed at developing a tool that provides a simple drag-and-drop interface consisting of blocks and wires which then synthesizes the program into a Python application. This shortens the development time greatly as well as makes development quite easy. Also, as the modules provide built-in functionality, the software would be much more optimized, robust and modular.


## Contributions

As my work was building a complete tool rather than contributing to a specific project. I can divide my work into 5 parts:


### Python Back End:

In this section as I had to implement everything from scratch, so I uploaded the files directly. It is described in the documentation. Other pull requests are below:

[Shift from Multi-threading to Multi-Processing](https://github.com/JdeRobot/VisualCircuit/issues/15)

[Wire Support](https://github.com/JdeRobot/VisualCircuit/issues/22)

[Improvements in Block Synthesis](https://github.com/JdeRobot/VisualCircuit/issues/42)


### Development of Modules:

[Adding Blocks](https://github.com/JdeRobot/VisualCircuit/issues/13)

[Sample Blocks](https://github.com/JdeRobot/VisualCircuit/issues/20)


### NodeJS Front End:

In this section, I uploaded the files directly as they were imported from icestudio and the other pull requests are below:

[Clean IceStudio Traces](https://github.com/JdeRobot/VisualCircuit/pull/19)

[Changing extensions from .ice to .vc](https://github.com/JdeRobot/VisualCircuit/issues/41)

[Minor changes to directories and paths](https://github.com/JdeRobot/VisualCircuit/pull/23)

[Assigning thumbnails to blocks](https://github.com/JdeRobot/VisualCircuit/issues/28)


### Adding Functionalities:

[F1 Support](https://github.com/JdeRobot/VisualCircuit/issues/31)

[ROS Topics based communication support](https://github.com/JdeRobot/VisualCircuit/issues/25)

[Add Custom Code Block](https://github.com/JdeRobot/VisualCircuit/issues/32)

[Block Composition](https://github.com/JdeRobot/VisualCircuit/issues/45)

[Add User Defined Block](https://github.com/JdeRobot/VisualCircuit/issues/37)

[Creating Console using Tkinter](https://github.com/JdeRobot/VisualCircuit/issues/36)

[Editable Python Code in Frontend](https://github.com/JdeRobot/VisualCircuit/issues/35)

[View Python Code in Frontend](https://github.com/JdeRobot/VisualCircuit/issues/34)

[Adding Parameters Support](https://github.com/JdeRobot/VisualCircuit/issues/33)


### Demo's and Documentation:

Some major demo's along with their videos can be found here:

[Tweet 1](https://twitter.com/JdeRobot/status/1298632443969392640)

[Tweet 2](https://twitter.com/JdeRobot/status/1293209125208367105)

[Tweet 3](https://twitter.com/JdeRobot/status/1280055010747875328)


The documentation can be found here: [Link to Documentation](https://jderobot.github.io/VisualCircuit/documentation/)


## Difficulties

I faced some difficulties in the communication between blocks. I needed a light weight and low overhead way of communication between the block. The Python library did not work so well as it had some bug. The good thing was that it led me to a much better solution using POSIX IPC.
Another difficulty was getting support for ROS Noetic. As ROS Noetic is very recent it had a lot of issues in installation as well as very less hardware was supported on it. Also, if there was any problem, I had to solve it by myself because there were no available online resources.

## Improved skills

I learnt a lot about sofware development and how to properly document and manage code. I also learnt about the problems that occur during development and how to resolve them. I also think my programming skills and knowledge about robotics significantly increased. 

## Further work

I plan to extend this further as a project in my university. I already discussed the future roadmap for this tool with my mentor and we are trying to make this into a solid tool. There are many milestones that we have discussed and I plan to work on this for the next 8-10 months.

## Acknowledgment

Taking part in this GSOC was an awesome experience and I want to particularly thank my mentor JoseMaria Canas for his supervision.
