#!/usr/bin/env python3

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='talker_py',
            executable='talker',
            name='coordinate_publisher',
            output='screen',
            parameters=[
                # You can add parameters here if needed
            ],
            arguments=[
                # Default arguments for x and y coordinates
                '2.0',  # x coordinate
                '2.0'   # y coordinate
            ]
        )
    ])