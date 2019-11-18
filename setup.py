from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setup(
    name='pytorch_ssd',
    version='0.1',
    url='https://github.com/lambdaofgod/pytorch_ssd',
    author='Jakub Bartczuk',
    packages=find_packages(),
    install_requires=requirements
)
