from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='trucklang',
    version='0.1.1',
    author='Anmol Gautam',
    author_email="tarptaeya@gmail.com",
    description="A dynamic object oriented programming language with a focus on simplicity",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/tarptaeya/truck",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.5",
)
