# -*- coding: utf-8 -*-
"""
Setup.py for Skyperious. 

------------------------------------------------------------------------------
This file is part of Skyperious - Skype chat history tool.
Released under the MIT License.

@author      Erki Suurjaak
@created     10.12.2014
@modified    03.08.2020
------------------------------------------------------------------------------
"""
import glob
import os
import setuptools

from skyperious import conf

setuptools.setup(
    name=conf.Title,
    version=conf.Version,
    description="Skype chat history tool",
    url="https://github.com/suurjaak/Skyperious",

    author="Erki Suurjaak",
    author_email="erki@lap.ee",
    license="MIT",
    platforms=["any"],
    keywords="skype sqlite merge export",

    install_requires=["appdirs", "beautifulsoup4", "ijson", "pyparsing", "Pillow<=6.2.2", "python-dateutil", "SkPy", "wxPython>=4.0", "XlsxWriter"],
    entry_points={"gui_scripts": ["skyperious = skyperious.main:run"]},

    packages=setuptools.find_packages(),
    include_package_data=True, # Use MANIFEST.in for data files
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Unix",
        "Operating System :: MacOS",
        "Topic :: Communications :: Chat",
        "Topic :: Database",
        "Topic :: Utilities",
        "Topic :: Desktop Environment",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
    ],

    long_description_content_type="text/markdown",
    long_description=
"""Skyperious is a Skype chat history tool, written in Python.

You can open Skype SQLite databases and work with their contents:

- search across all messages and contacts
- read chat history in full, see chat statistics and word clouds
- export chats as HTML, text or spreadsheet
- synchronize messages from Skype online service
- view any database table and export their data, fix database corruption
- change, add or delete data in any table
- execute direct SQL queries

and

- synchronize messages in two Skype databases, merging their differences
""",
)
