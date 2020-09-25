if(NOT ENABLE_GUI)
  return()
endif()

option(BUILD_WRS2020SG "Building the WRS2020SG files" ON)
if(NOT BUILD_WRS2020SG)
  return()
endif()

if(UNIX)
  add_custom_target(
    symlink_to_WRS2020SG ALL
    COMMAND ${CMAKE_COMMAND} -E create_symlink
    ${CMAKE_CURRENT_SOURCE_DIR} ${CNOID_BINARY_SHARE_DIR}/WRS2020SG)
endif()

install(DIRECTORY
  model
  project
  script
  test
  DESTINATION ${CNOID_SHARE_SUBDIR}/WRS2020SG)

add_subdirectory(controller)
