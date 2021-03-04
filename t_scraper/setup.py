#!/usr/bin/env python3

from setuptools import setup, find_packages
with open('requirements.txt') as requirements:
    required = requirements.read().splitlines()

setup(
    name='twitterscraper',
    version='1.6.1',
    description='Tool for scraping Tweets',
    license='MIT',
    packages=find_packages(exclude=["build.*", "tests", "tests.*"]),
    install_requires=required,
    entry_points={
        "console_scripts": [
            "twitterscraper = twitterscraper.main:main"
        ]
    })
