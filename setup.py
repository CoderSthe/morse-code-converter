from setuptools import setup, find_packages

setup(
    name='morse_code_converter',
    version='1.0.0',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Morse Code Converter',
    long_description=open("README.md").read(),
    url='https://github.com/CoderSthe/morse-code-converter',
    author='Sithembiso Mdhluli',
    author_email='mdhluli269@gmail.com'
)