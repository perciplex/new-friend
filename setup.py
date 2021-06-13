#!/usr/bin/env python

from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="new_friend",
    version="1.0",
    description="Replace your friends on Slack.",
    author="Perciplex",
    packages=find_packages(),
    setup_requires=['wheel'],
    install_requires=requirements,
)
