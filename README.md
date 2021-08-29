# WRS-TDRRC-2020SG1  _RELEASE VERSION_  
The Stage Gate Model 2020-1 of World Robot Summit(Competition) Tunnel Disaster Response and Recovery Challenge.  
THIS IS THE RELEASE VERSION.  

## SOFTWARE IMPORTANT INFORMATION for WRC 2020  
### ABOUT Choreonoid  
Version 1.8 with a tag specified by the development version management.  
EX.) git clone -b tag https://github.com/choreonoid/choreonoid.git  

### ABOUT Robotic middle-ware  
 * Recommend using ROS1  
We have got information that the choreonoid developer will support the connection between choreonoid and ROS1.  
TO GET MORE DETAILS, STRONGLY RECOMMEND TO VISIT THE FOLLOWING CHOREONOID SITES:

    * [Cooperation with ROS](https://choreonoid.org/en/documents/latest/ros/index.html)  
    * [World Robot Summit 2018](https://choreonoid.org/en/documents/latest/wrs2018/index.html)  

 * Not recommend using OpenRTM  
We got information that the choreonoid developer does not have any plan to support the connection between choreonoid and RTM.  
There is information that the RTM version 1.1.2 and 1.2.0 were used with older choreonoid. But there is no information on whether the choreonoid developer will support.  

### ABOUT AGX Dynamics  
We are considering the suitable version of AGX.  
Currently, Version 2.30.4.0 (the former version was 2.29.4.0) is recommended by the committee.  
To install version 2.30.4.0, use the command "gdebi" instead of "dpkg".  
TO GET MORE DETAILS, STRONGLY RECOMMEND TO VISIT THE FOLLOWING CHOREONOID SITE:

  * [Installation of AGX Dynamics](https://translate.google.com/translate?sl=auto&tl=en&u=https://choreonoid.org/ja/documents/latest/agxdynamics/install/install-agx-ubuntu.html%23id5)  

## Requirements  

  1. OS  
    * Ubuntu 18.04 LTS  
  2. Choreonoid  
    * Using choreonoid with ROS1:  
      [Building Choreonoid related packages(with ROS)](https://choreonoid.org/en/documents/latest/ros/build-choreonoid.html)  
    * [Choreonoid Operation Manual](https://choreonoid.org/en/manuals/latest/index.html)
    * [Building Choreonoid](https://choreonoid.org/en/manuals/latest/install/build-ubuntu.html#development-version)  
  3. AGX  
    * [AGX for Choreonoid](https://choreonoid.org/en/manuals/latest/agxdynamics/index.html)  
    * [Downloading AGX](https://www.algoryx.se/download/?id=2592)  
    * [Installation of AGX Dynamics(in the Choreonoid site)](https://translate.google.com/translate?sl=auto&tl=en&u=https://choreonoid.org/ja/documents/latest/agxdynamics/install/install-agx-ubuntu.html%23id5)  
    * [Installing AGX(in the Algoryx site)](https://www.algoryx.se/documentation/complete/agx/tags/latest/UserManual/source/installation.html#install-on-ubuntu-16-04)  
  4. Other elementally packages for using choreonoid with ROS1  
    * [Installing ROS](https://choreonoid.org/en/documents/latest/ros/install-ros.html)  

## How to use this repository WITH ROS on Unbuntu 18.04  
If you have to install choreonoid now, please follow below commands:  
At first, you should install AGX Dynamics. Please check above "ABOUT AGX DYNAMICS", and make sure the version of AGX.  
And next, do below commands:  

    $ sudo apt-get install gdebi-core python-catkin-tools qt5-default libqt5x11extras5-dev qt5-style-plugins  
    $ cd ~  
    $ mkdir -p catkin_ws/src  
    $ cd catkin_ws  
    $ catkin init  
    $ cd src  
    $ git clone -b WRS2020 https://github.com/choreonoid/choreonoid.git  
    $ git clone https://github.com/choreonoid/choreonoid_ros.git  
    $ git clone https://github.com/choreonoid/choreonoid_ros_samples.git  
    $ git clone https://github.com/choreonoid/choreonoid_joy.git  
    $ git clone https://github.com/WRS-TDRRC/WRS-TDRRC-2020SG1 choreonoid/ext/WRS2020SG  
    $ choreonoid/misc/script/install-requisites-ubuntu-18.04.sh  
    $ cd ..    
    $ catkin config --cmake-args -DBUILD_COMPETITION_PLUGIN=ON -DBUILD_AGX_DYNAMICS_PLUGIN=ON -DBUILD_AGX_BODYEXTENSION_PLUGIN=ON -DBUILD_SCENE_EFFECTS_PLUGIN=ON -DBUILD_MULTICOPTER_PLUGIN=ON -DBUILD_MULTICOPTER_SAMPLES=ON -DBUILD_CHOREONOID_EXECUTABLE=OFF -DUSE_PYTHON3=OFF -DCMAKE_BUILD_TYPE=Release -DENABLE_INSTALL_RPATH_USE_LINK_PATH=ON   
    $ catkin build  

Before run, you have to add "source /opt/Algoryx/AGX-VERSION-NUMBER/setup_env.bash" at the end of ~/.bashrc , and reopen the terminal.  
Please find field images and run scripts in the [wiki page](https://github.com/WRS-TDRRC/WRS-TDRRC-2020SG1/wiki).  

* TERMINAL 1:  
    $ roscore  

* TERMINAL 2:  
    $ cd ~/catkin_ws  
    $ source devel/setup.bash  
    $ rosrun choreonoid_joy node  

* TERMINAL 3:  
    $ cd ~/catkin_ws  
    $ source devel/setup.bash  
    $ rosrun choreonoid_ros choreonoid devel/share/choreonoid-1.8/WRS2020SG/script/SG1L-DoubleArmV7A-ROS.py  

* TERMINAL 4:  
    $ rqt_image_view  

## How to use this repository WITHOUT ROS.  
If you have to install choreonoid now, please follow below commands:  

    $ cd ~  
    $ git clone -b WRS2020 https://github.com/choreonoid/choreonoid.git  
    $ ~/choreonoid/misc/script/install-requisites-ubuntu-18.04.sh  
    $ sudo apt-get install qt5-default libqt5x11extras5-dev qt5-style-plugins  
    $ cd ~/choreonoid/ext  
    $ git clone https://github.com/WRS-TDRRC/WRS-TDRRC-2020SG1 WRS2020SG
    $ cd ~/choreonoid && mkdir build && cd build  
    $ cmake .. -DBUILD_AGX_DYNAMICS_PLUGIN=ON -DBUILD_AGX_BODYEXTENSION_PLUGIN=ON -DBUILD_COMPETITION_PLUGIN=ON -DBUILD_MULTICOPTER_PLUGIN=ON -DBUILD_MULTICOPTER_SAMPLES=ON -DBUILD_SCENE_EFFECTS_PLUGIN=ON -DENABLE_INSTALL_RPATH_USE_LINK_PATH=ON  
    $ make -j8  

Or you are already using choreonoid, please follow below commands:  
(When your choreonoid is under ~/choreonoid)  

    $ cd ~/choreonoid/ext  
    $ git clone https://github.com/WRS-TDRRC/WRS-TDRRC-2020SG1 WRS2020SG
    $ cd ~/choreonoid/build  
    $ cmake .. -DBUILD_AGX_DYNAMICS_PLUGIN=ON -DBUILD_AGX_BODYEXTENSION_PLUGIN=ON -DBUILD_COMPETITION_PLUGIN=ON -DBUILD_MULTICOPTER_PLUGIN=ON -DBUILD_MULTICOPTER_SAMPLES=ON -DBUILD_SCENE_EFFECTS_PLUGIN=ON -DENABLE_INSTALL_RPATH_USE_LINK_PATH=ON  
    $ make -j8  

Before run, you have to add "source /opt/Algoryx/AGX-VERSION-NUMBER/setup_env.bash" at the end of ~/.bashrc , and reopen the terminal.  
Please find further details(field images, run scripts, and some attentions related the stage gate rules) in the [wiki page](https://github.com/WRS-TDRRC/WRS-TDRRC-2020SG1/wiki).  

## The location of the simulation log files  
After running and stopping a simulation, you can save a simulation log archive consisted from a raw simulation log file and all models needed to playback the simulation log.  
You can a raw simulation log file under \~/catkin_ws/share/choreonoid-1.8/WRS2020SG/project (if you use Choreonoid without ROS: \~/choreonoid/ext/WRS2020SG/project), too.  

  * How to save the simulation log archive.  
    1. Find "WorldLogFile" item in the left pane items tree.  
    2. Do mouse right click the WorldLogFile item.  
    3. Select "Save project as log playback archive".  
    4. On the appeared dialog window, select a directory to save the simulation archive and name it.  

  * How to playback the simulation log.   

    * Choreonoid with ROS:

      $ rosrun choreonoid_ros choreonoid PATH_TO_ARCHIVE/ARCHIVE_NAME.cnoid  

    * Choreonoid with ROS:

      $ build/bin/choreonoid PATH_TO_ARCHIVE/ARCHIVE_NAME.cnoid  

Edited: 20th Oct. 2021
