# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from exifreader import __version__, __doc__

readme_file = open("README.md", "rt").read()

setup(
    name="ExifReader",
    version=__version__,
    author="Cyb3r Jak3",
    author_email="jake@jwhite.network",
    license="BSD",
    python_requires=">=3.4",
    packages=find_packages(),
    install_requires=[
        "defusedxml >= 0.6.0"
    ],
    scripts=["EXIF.py"],
    url="https://gitlab.com/Cyb3r-Jak3/exifreader",
    project_urls={
        "Issues": "https://gitlab.com/Cyb3r-Jak3/ExifReader/issues",
        "Source Code": "https://gitlab.com/Cyb3r-Jak3/ExifReader/-/tree/publish",
        "CI": "https://gitlab.com/Cyb3r-Jak3/ExifReader/pipelines",
        "Releases": "https://github.com/Cyb3r-Jak3/ExifReader"
    },
    keywords="exif image metadata photo",
    description=" ".join(__doc__.splitlines()).strip(),
    long_description=readme_file,
    long_description_content_type='text/markdown',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Utilities",
    ],
)
