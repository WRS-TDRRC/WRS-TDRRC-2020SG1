# WRS-TDRRC-2020SG1 _PRELIMINARY VERSION_
The Stage Gate Model 2020-1 of World Robot Summit(Competition) Tunnel Disaster Response and Recovery Challenge.  
CAUTION: THIS IS A PRELIMINARY VERSION. THE FINAL VERSION WILL COME SOON.

## Requirements  

  1. [Choreonoid version 1.7](https://choreonoid.org/en/manuals/1.7/index.html)  
  2. [AGX for Choreonoid](https://choreonoid.org/en/manuals/latest/agxdynamics/index.html), [Downloading AGX](https://www.algoryx.se/download/?id=1887)  

## How to use this repository.  
If you have to install choreonoid now, please follow below commands:  

    $ cd ~  
    $ git clone -b "release-1.7" https://github.com/s-nakaoka/choreonoid.git  
    $ cd choreonoid/ext  
    $ wget https://github.com/WRS-TDRRC/WRS-TDRRC-2020SG1/blob/master/WRS2020SG.zip  
    $ unzip WRS2020SG.zip  
    $ cd ~/choreonoid && mkdir build && cd build  
    $ cmake .. -DBUILD_AGX_DYNAMICS_PLUGIN=ON -DBUILD_AGX_BODYEXTENSION_PLUGIN=ON -DBUILD_MULTICOPTER_PLUGIN=ON -DBUILD_MULTICOPTER_SAMPLES=ON -DBUILD_WRS2018=ON  
    $ make -j8  
  
Or you are already using choreonoid version 1.7, please follow below commands:  
(When your choreonoid is under ~/choreonoid)  

    $ cd ~/choreonoid/ext  
    $ wget https://github.com/WRS-TDRRC/WRS-TDRRC-2020SG1/blob/master/WRS2020SG.zip  
    $ unzip WRS2020SG.zip  
    $ cd ~/choreonoid/build  
    $ cmake . -DBUILD_AGX_DYNAMICS_PLUGIN=ON -DBUILD_AGX_BODYEXTENSION_PLUGIN=ON -DBUILD_MULTICOPTER_PLUGIN=ON -DBUILD_MULTICOPTER_SAMPLES=ON -DBUILD_WRS2018=ON  
    $ make -j8  

Please find field images and run scripts in the [wiki page](https://github.com/WRS-TDRRC/WRS-TDRRC-2020SG1/wiki).  

## The location of the simulation log files  
After running a simulation, you can find a simulation log file under ~/choreonoid/ext/WRS2020SG/project.  
Please see also [Choreonoid documentation](https://choreonoid.org/en/manuals/1.7/simulation/execution-and-playback.html).  

Edited: 16th Jan. 2020
