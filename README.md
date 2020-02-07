# WRS-TDRRC-2020SG1  _RELEASE VERSION_  
The Stage Gate Model 2020-1 of World Robot Summit(Competition) Tunnel Disaster Response and Recovery Challenge.  
THIS IS THE RELEASE VERSION.  

## Requirements  

  1. [Choreonoid (tag=wrs2019)](https://choreonoid.org/en/manuals/latest/index.html)  
  2. [AGX for Choreonoid](https://choreonoid.org/en/manuals/latest/agxdynamics/index.html), [Downloading AGX](https://www.algoryx.se/download/?id=1887), The AGX highest version which we concirned that it is working is 2.27.1.3 .  

## How to use this repository.  
If you have to install choreonoid now, please follow below commands:  

    $ cd ~  
    $ git clone -b "wrs2019" https://github.com/s-nakaoka/choreonoid.git  
    $ cd choreonoid/ext  
    $ wget https://github.com/WRS-TDRRC/WRS-TDRRC-2020SG1/blob/master/WRS2020SG.zip  
    $ unzip WRS2020SG.zip  
    $ cd ~/choreonoid && mkdir build && cd build  
    $ cmake .. -DBUILD_AGX_DYNAMICS_PLUGIN=ON -DBUILD_AGX_BODYEXTENSION_PLUGIN=ON -DBUILD_COMPETITION_PLUGIN=ON -DENABLE_CORBA=ON -DBUILD_CORBA_PLUGIN=ON -DBUILD_OPENRTM_PLUGIN=ON -DBUILD_OPENRTM_SAMPLES=ON -DBUILD_MULTICOPTER_PLUGIN=ON -DBUILD_MULTICOPTER_SAMPLES=ON -DBUILD_SCENE_EFFECTS_PLUGIN=ON -DBUILD_WRS2018=ON  
    $ make -j8  
  
Or you are already using choreonoid, please follow below commands:  
(When your choreonoid is under ~/choreonoid)  

    $ cd ~/choreonoid && git checkout "wrs2019"
    $ cd ~/choreonoid/ext  
    $ wget https://github.com/WRS-TDRRC/WRS-TDRRC-2020SG1/blob/master/WRS2020SG.zip  
    $ unzip WRS2020SG.zip  
    $ cd ~/choreonoid/build  
    $ cmake .. -DBUILD_AGX_DYNAMICS_PLUGIN=ON -DBUILD_AGX_BODYEXTENSION_PLUGIN=ON -DBUILD_COMPETITION_PLUGIN=ON -DENABLE_CORBA=ON -DBUILD_CORBA_PLUGIN=ON -DBUILD_OPENRTM_PLUGIN=ON -DBUILD_OPENRTM_SAMPLES=ON -DBUILD_MULTICOPTER_PLUGIN=ON -DBUILD_MULTICOPTER_SAMPLES=ON -DBUILD_SCENE_EFFECTS_PLUGIN=ON -DBUILD_WRS2018=ON  
    $ make -j8  

Please find further details(field images, run scripts, and some attentions related the stage gate rules) in the [wiki page](https://github.com/WRS-TDRRC/WRS-TDRRC-2020SG1/wiki).  

## The location of the simulation log files  
After running a simulation, you can find a simulation log file under ~/choreonoid/ext/WRS2020SG/project.  
Please see also [Choreonoid documentation](https://choreonoid.org/en/manuals/1.7/simulation/execution-and-playback.html).  

Edited: 7th Feb. 2020
