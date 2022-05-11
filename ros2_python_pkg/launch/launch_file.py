from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ros2_python_pkg',
            executable='talker',
            output="screen",
        ),

         Node(
            package='ros2_python_pkg',
            executable='listener',
            output="screen",
        ),
       
    ])