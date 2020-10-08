import WRSUtil
WRSUtil.loadProject(
    "SingleSceneView", "SG2", [ "AGXSimulator", "AISTSimulator" ], "Quadcopter",
    enableMulticopterSimulation = True, enableVisionSimulation = True, remoteType = "ROS")
