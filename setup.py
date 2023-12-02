from setuptools import setup, find_packages

setup(
    name = 'dcmlpkg',
    version='0.0.1',
    description='Python Package for some useful function for Machine Learning Project',
    packages=find_packages(),
    install_requires = [
        'pandas>= 2.0.0', 
        'numpy>=1.11.1',       
                                
                        ]
)