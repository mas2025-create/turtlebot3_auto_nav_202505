from setuptools import setup

package_name = 'turtlebot3_auto_nav'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='masanari sakaki',
    maintainer_email='sakura.ms0513@gmail.com',
    description='Auto navigation with TurtleBot3 and Nav2',
    license='MIT',
    entry_points={
        'console_scripts': [
            'navigator = turtlebot3_auto_nav.navigator:main',
        ],
    },
)

