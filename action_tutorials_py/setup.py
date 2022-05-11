from setuptools import setup
import subprocess, os, platform
from glob import glob
package_name = 'action_tutorials_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='harrypotter',
    maintainer_email='harrypotter@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'client=action_tutorials_py.fibonacci_action_client:main',
            'server=action_tutorials_py.fibonacci_action_server:main',
            'talker=action_tutorials_py.node_publisher:main',
            'listener=action_tutorials_py.node_subscriber:main',
        ],
    },
)
