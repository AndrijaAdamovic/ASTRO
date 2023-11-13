import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration, ThisLaunchFileDir, PathJoinSubstitution, PythonExpression
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch_ros.actions import Node
from launch.conditions import IfCondition
from launch_ros.substitutions import FindPackageShare

import xacro


def generate_launch_description():

    use_sim_time = LaunchConfiguration('use_sim_time')
    run_jspg = LaunchConfiguration('run_jspg')
    run_rviz = LaunchConfiguration('run_rviz')

    pkg_path = os.path.join(get_package_share_directory('astro'))
    xacro_file = os.path.join(pkg_path,'description','astro.urdf.xacro')
    robot_description_config = xacro.process_file(xacro_file)

    params = {'robot_description': robot_description_config.toxml(), 'use_sim_time': use_sim_time}
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[params]
    )

    rviz_config_file = PathJoinSubstitution([FindPackageShare("astro"), "rviz", "view_robot.rviz"])
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        output='screen',
        arguments=['-d', rviz_config_file],
        condition=IfCondition(run_rviz)
    )

    jspg_node = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
        output="screen",
        condition=IfCondition(run_jspg)
    )

    return LaunchDescription([
        DeclareLaunchArgument('use_sim_time', default_value='false', description='Use sim time if true'),
        DeclareLaunchArgument('run_jspg', default_value='true', description='Run joint_state_publisher_gui node'),
        DeclareLaunchArgument('run_rviz', default_value='true', description='Run Rviz'),
        rviz_node,
        jspg_node,
        robot_state_publisher_node
    ])