import os
import glob

from setuptools import find_packages, setup

package_name = 'micky_planning'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'nodes'), glob.glob('nodes/*.py')),
        (os.path.join('share', package_name , 'launch'), glob.glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'nodes', 'config'), glob.glob('nodes/config/*.yaml')),
        (os.path.join('share', package_name, 'nodes', 'config', 'rviz'), glob.glob('nodes/config/rviz/*.rviz')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='TODO',
    maintainer_email='TODO@todo.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'reference_node = nodes.reference_node:main',
        ],
    },
)