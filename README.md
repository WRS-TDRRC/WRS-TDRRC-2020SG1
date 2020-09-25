# WRS-TDRRC-2020SG1  _RELEASE VERSION_  
The Stage Gate Model 2020-1 of World Robot Summit(Competition) Tunnel Disaster Response and Recovery Challenge.  
THIS IS THE RELEASE VERSION.  

## SOFTWARE IMPORTANT INFORMATION for WRC 2020  
### ABOUT Choreonoid  
Version 1.8 with a tag specified by the development version management.  
EX.) git clone -b tag https://github.com/choreonoid/choreonoid.git  
  
### ABOUT Robotic middle-ware  
 * Recommend using ROS1 Melodic  
We have got information that the choreonoid developer will support the connection between choreonoid and ROS1.  
  
 * Not recommend using OpenRTM  
We got information that the choreonoid developer does not have any plan to support the connection between choreonoid and RTM.  
There is information that the RTM version 1.1.2 and 1.2.0 were used with older choreonoid. But there is no information on whether the choreonoid developer will support.  
  
### ABOUT AGX Dynamics  
We are consideringa suitable virsion of AGX.  
Currently, Version 2.23.0.4 which was nearest version for Ubuntu 18.04 from WRS2018 and verified by the committee.  
  

## Requirements  

  1. [Choreonoid (tag=wrs2019)](https://choreonoid.org/en/manuals/latest/index.html), [Installing Choreonoid](https://choreonoid.org/en/manuals/latest/install/build-ubuntu.html#development-version). If you use ROS melodic, see also [Teleoperation Sample using ROS](https://choreonoid.org/en/manuals/latest/wrs2018/teleoperation-ros.html)  
  2. [AGX for Choreonoid](https://choreonoid.org/en/manuals/latest/agxdynamics/index.html), [Downloading AGX](https://www.algoryx.se/download/?id=1887), [Installing AGX](https://www.algoryx.se/documentation/complete/agx/tags/latest/UserManual/source/installation.html#install-on-ubuntu-16-04). The AGX highest version is 2.23.0.4 which was nearest version for Ubuntu 18.04 from WRS2018 and verified by the committee. There are capability that higher version which can be used will be found.  

## How to use this repository.  
If you have to install choreonoid now, please follow below commands:  

    $ cd ~  
    $ git clone -b "wrs2019" https://github.com/choreonoid/choreonoid.git  
    $ ~/choreonoid/misc/script/install-requisites-ubuntu-18.04.sh  
    $ sudo apt-get install qt5-default libqt5x11extras5-dev qt5-style-plugins  
    $ cd ~/choreonoid/ext  
    $ git clone https://github.com/WRS-TDRRC/WRS-TDRRC-2020SG1 WRS2020SG
    $ cd ~/choreonoid && mkdir build && cd build  
    $ cmake .. -DBUILD_AGX_DYNAMICS_PLUGIN=ON -DBUILD_AGX_BODYEXTENSION_PLUGIN=ON -DBUILD_COMPETITION_PLUGIN=ON -DENABLE_CORBA=ON -DBUILD_CORBA_PLUGIN=ON -DBUILD_MULTICOPTER_PLUGIN=ON -DBUILD_MULTICOPTER_SAMPLES=ON -DBUILD_SCENE_EFFECTS_PLUGIN=ON -DBUILD_WRS2018=ON  
    $ make -j8  
  
Or you are already using choreonoid, please follow below commands:  
(When your choreonoid is under ~/choreonoid)  

    $ cd ~/choreonoid && git checkout "wrs2019"
    $ cd ~/choreonoid/ext  
    $ git clone https://github.com/WRS-TDRRC/WRS-TDRRC-2020SG1 WRS2020SG
    $ cd ~/choreonoid/build  
    $ cmake .. -DBUILD_AGX_DYNAMICS_PLUGIN=ON -DBUILD_AGX_BODYEXTENSION_PLUGIN=ON -DBUILD_COMPETITION_PLUGIN=ON -DENABLE_CORBA=ON -DBUILD_CORBA_PLUGIN=ON -DBUILD_MULTICOPTER_PLUGIN=ON -DBUILD_MULTICOPTER_SAMPLES=ON -DBUILD_SCENE_EFFECTS_PLUGIN=ON -DBUILD_WRS2018=ON  
    $ make -j8  

Before run, you have to add "source /opt/Algoryx/AgX-2.23.0.4/setup_env.bash" at the end of ~/.bashrc , and reopen the terminal.  
Please find further details(field images, run scripts, and some attentions related the stage gate rules) in the [wiki page](https://github.com/WRS-TDRRC/WRS-TDRRC-2020SG1/wiki).  

## The location of the simulation log files  
After running a simulation, you can find a simulation log file under ~/choreonoid/ext/WRS2020SG/project.  
Please see also [Choreonoid documentation](https://choreonoid.org/en/manuals/1.7/simulation/execution-and-playback.html).  

Edited: 7th Feb. 2020
