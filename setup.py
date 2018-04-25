from setuptools import setup

setup(
    name='tempmonitor',
    version='0.0.1a',
    packages=['tempmonitor'],
    url='https://github.com/jtcressy/tempmonitor',
    license='GPL',
    author='jtcressy',
    author_email='joel@jtcressy.net',
    description='Temperature monitor for raspberry pi sense hat',
    scripts=['bin/tempmonitor'],
    entry_points={
        'console_scripts': ['tempmonitor=tempmonitor.commandline:main'],
    }
)
