from setuptools import setup

setup(
    name='flask-test',
    version='0.1',
    packages=['app'],
    install_requires=[
        'flask',
        'flask-apscheduler',
        'gunicorn',
    ],
)
