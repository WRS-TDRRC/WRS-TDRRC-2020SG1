import WRSUtil
WRSUtil.loadProject(
    "SingleSceneView", "SG1L", [ "AGXSimulator", "AISTSimulator" ], "Quadcopter",
    enableMulticopterSimulation = True, enableVisionSimulation = True, remoteType = "ROS")
