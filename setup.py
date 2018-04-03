#!/usr/bin/env python

from setuptools import setup, find_packages

__author__ = "fraq <briggs.brenton@gmail.com>"
__copyright__ = "Copyright 2018, Legobot"

description = 'Lego for organizing text and generating markoved responses'
name = 'legos.markov'
setup(
    name=name,
    version='0.1.2',
    namespace_packages=name.split('.')[:-1],
    license='MIT',
    description=description,
    author='fraq',
    url='https://github.com/Legobot/' + name,
    install_requires=['legobot>=1.2.1,<=2.0.0',
                      'markovify',
                      'nltk'
                      ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Development Status :: 4 - Beta'
    ],
    packages=find_packages()
)
