from setuptools import setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name='flask_python_backend',
    version='1.0.0',
    install_requires=requirements,
    packages=[''],
    url='https://github.com/hemanthsunny/flask_python_backend',
    license='PREMIUM',
    author='Naga Perla',
    author_email='hemanth.vja@gmail.com',
    description='Sample project'
)

