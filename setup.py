import setuptools

from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="randombtc",
    version="0.1",
    description="Deterministic universal random number generator with entropy from the Bitcoin blockchain",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/callebtc/randombtc",
    author="callebtc",
    author_email="callebtc@nomail.com",
    license="MIT",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=requirements,
    include_package_data=True,
)
