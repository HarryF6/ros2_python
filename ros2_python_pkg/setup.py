from click import launch
from setuptools import setup
import subprocess, os, platform
from glob import glob
package_name = 'action_tutorials_py'

package_name = 'ros2_python_pkg'

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
    #generar ejecutables en python
    entry_points={
        'console_scripts': [
            'talker=node_publisher:main',
            'listener=node_subscriber:main',
        ],
    },
)
