from setuptools import setup

setup(
    name='arenadb',
    version='0.0.1',
    description='CLI for ArenaDB',
    packages=['.'],
    entry_points={
        'console_scripts': ['arenadb=main.main']
    },
)
