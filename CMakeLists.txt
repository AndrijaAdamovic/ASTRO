cmake_minimum_required(VERSION 3.8)
project(astro)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(serial REQUIRED)
find_package(hardware_interface REQUIRED)
find_package(controller_manager REQUIRED)
find_package(rclcpp REQUIRED)
find_package(pluginlib REQUIRED)

# add_library(astro SHARED src/astro_diffdrive.cpp src/wheel.cpp src/arduino_comms.cpp)

ament_target_dependencies(
  diffdrive_arduino
  hardware_interface
  controller_manager
  serial
  rclcpp
  pluginlib
)

# pluginlib_export_plugin_description_file(hardware_interface astro_hardware.xml)

# target_include_directories(
#   astro_diffdrive
#   PRIVATE
#   include
# )

# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

install(
  DIRECTORY config description launch meshes rviz
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
