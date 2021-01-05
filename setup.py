import setuptools

setuptools.setup(
    name='arenadb',
    version='0.0.1',
    description='CLI for ArenaDB',
    py_modules=['arenadb', 'alias'],
    entry_points={
        'console_scripts': ['arenadb=arenadb:main']
    }
)
