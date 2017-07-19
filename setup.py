from setuptools import setup

setup(
    name='is-taken',
    packages=['istaken'],
    version='0.1.5',
    entry_points={
        'console_scripts': [
            'is-taken = istaken.main:main'
        ]
    },
    description='Check if a PyPI package name is taken.',
    url='https://github.com/Frederick-S/is-taken'
)
