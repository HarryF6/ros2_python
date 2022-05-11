from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='action_tutorials_py',
            executable='talker',
            output="screen",
        ),

         Node(
            package='action_tutorials_py',
            executable='listener',
            output="screen",
        ),
         Node(
            package='action_tutorials_py',
            executable='client',
            output="screen",
        ),

         Node(
            package='action_tutorials_py',
            executable='server',
            output="screen",
        ),
       
    ])

    #para python hay que copiar la carpeta launch en share/PROJECT_NAME