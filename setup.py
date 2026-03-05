from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read().splitlines()

setup(
    name="github-unfollow-nonfollowers",
    version="1.0.0",
    author="Bd-Mutant7",
    description="A Python script to unfollow GitHub users who don't follow you back",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Bd-Mutant7/github-unfollow-nonfollowers",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "github-unfollow=unfollow_nonfollowers:main",
        ],
    },
)
