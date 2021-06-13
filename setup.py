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
    scripts=["bin/new_friend.py"],
    install_requires=requirements,
)
