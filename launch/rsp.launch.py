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
    run_ekf = LaunchConfiguration('run_ekf')

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

    robot_localization_node = Node(
       package='robot_localization',
       executable='ekf_node',
       name='ekf_filter_node',
       output='screen',
       parameters=[os.path.join(pkg_path, 'config/ekf.yaml'), {'use_sim_time': LaunchConfiguration('use_sim_time')}],
       condition=IfCondition(run_ekf)
    )

    return LaunchDescription([
        DeclareLaunchArgument('use_sim_time', default_value='false', description='Use sim time if true'),
        DeclareLaunchArgument('run_jspg', default_value='false', description='Run joint_state_publisher_gui Node'),
        DeclareLaunchArgument('run_rviz', default_value='false', description='Run Rviz'),
        DeclareLaunchArgument('run_ekf', default_value='true', description='Run Robot Localization Ekf Node'),
        rviz_node,
        jspg_node,
        robot_state_publisher_node,
        robot_localization_node
    ])