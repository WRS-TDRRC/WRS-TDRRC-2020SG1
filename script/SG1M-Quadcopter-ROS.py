import WRSUtil
WRSUtil.loadProject(
    "SingleSceneView", "SG1M", [ "AGXSimulator", "AISTSimulator" ], "Quadcopter",
    enableMulticopterSimulation = True, enableVisionSimulation = True, remoteType = "ROS")
