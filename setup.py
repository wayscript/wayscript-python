#!/usr/bin/env python

# Copyright (c) 2019 WayScript, Inc. All rights reserved.
# Licensed under the MIT License.

import setuptools

with open("README.md", "r", encoding="UTF-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="wayscript",
    version='0.0.0',
    author="Team WayScript",
    author_email="founders@wayscript.com",
    description="Quickly build services, data pipelines, internal tools, and more.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['slack-sdk', 'requests>=2.22.0'],
    url="https://github.com/wayscript/wayscript-python",
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where="src"),
    license='MIT',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications",
        "Topic :: Database",
        "Topic :: Office/Business",
        "Topic :: Utilities",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
    ],
    keywords=[ 'wayscript', 'productivity', 'software', 'scripts', 'cloud', 'tools', 'backend',
               'trigger', 'integration', 'dev', 'http', 'webhook' ],
    zip_safe=False,
)
