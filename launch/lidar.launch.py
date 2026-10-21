#!/usr/bin/env python3
"""Launch the Hesai LiDAR driver."""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'config',
            default_value=PathJoinSubstitution([
                FindPackageShare('hesai_ros_driver'),
                'config',
                'config.yaml',
            ]),
            description='Path to the Hesai LiDAR YAML config file.',
        ),
        Node(
            namespace='hesai_ros_driver',
            package='hesai_ros_driver',
            executable='hesai_ros_driver_node',
            output='screen',
            parameters=[{'config_path': LaunchConfiguration('config')}],
        ),
    ])
