#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
===============================
HtmlTestRunner
===============================


.. image:: https://img.shields.io/pypi/v/protloc.svg
        :target: https://pypi.python.org/pypi/protloc
.. image:: https://img.shields.io/travis/alfontal/protloc.svg
        :target: https://travis-ci.org/alfontal/protloc

Neural networks to predict subcellular localization of proteins.


Links:
---------
* `Github <https://github.com/alfontal/protloc>`_
"""

from setuptools import setup, find_packages

requirements = [ ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Alejandro Fontal",
    author_email='jandrofontal@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Neural networks to predict subcellular localization of proteins.",
    install_requires=requirements,
    license="MIT license",
    long_description=__doc__,
    include_package_data=True,
    keywords='protloc',
    name='protloc',
    packages=find_packages(include=['protloc']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/alfontal/protloc',
    version='0.1.0',
    zip_safe=False,
)
