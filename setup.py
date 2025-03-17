from setuptools import setup, find_packages

def read_requirements():
    with open("requirements.txt") as f:
        return f.read().splitlines()

setup(
    name="atlas_algo_trading",
    version="1.0.0",
    packages=find_packages(),
    install_requires=read_requirements(),
    author="Moises Nava",
    author_email="navam9897@gmail.com",
    description="This module use the Metatatrader5 library to connect with the platform, the functions were adapted to make it easier",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Windows",
    ],
    python_requires=">=3.9",
)