# Urx examples
Urx is an open source library to control a UR robot via python. This repo shows some codes to use it and some additional features like getting the length between the two fingers of a gripper. The original python-urx library can be found at [Python-urx package](https://github.com/SintefManufacturing/python-urx).  
An ATI Ethernet Axia F/T Sensor is added to our UR robot, an additional library to connect to it via python is also used. The original library can be found at [NetFT package](https://github.com/CameronDevine/NetFT)

## Install URX
* Open a terminal in the same folder as the README.md and type  ``` pip install python-urx ```
* Open a terminal in the same folder as the README.md and type  ``` pip install NetFT-master```
* In order to use the library you must define the static IP addresses of the UR robot and of your personal computer (see TCP_Robot and TCP\_MON\_ORDI variables in urx-examples.py). In order to avoid network latency you should better connect your computer directly to the UR robot. You also have to define in the parameter menu of the UR computer the static IP address of your computer (same as TCP\_MON\_ORDI). 


## Modifications
To discover, add or modify some skills, go into  
  * python-urx/urx/robot.py
  * python-urx/urx/urrobot.py
  * NetFT-master/NetFT/__init__.py

After any changes, go into the terminal of the corresponding folder and key in ``` pip  install .  ```


## Examples
Examples are in urx-examples.py.


