import codecs
import os
from setuptools import find_packages, setup
PACKAGE_NAME = "tx-strictdoc"
VERSION = "0.1.1"
AUTHOR = "Michael Naderhirn"
AUTHOR_EMAIL = "m.naderhirn@gmail.com"
DESCRIPTION = "The strictdoc language for writing technical specifications"
KEYWORDS = "textX DSL python domain specific languages"
LICENSE = "MIT"
URL = "https://github.com/Strumenta/textx-tutorial"
setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    url=URL,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    keywords=KEYWORDS,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True,
    package_data={"": ["*.tx"]},
    install_requires=["textx_ls_core"],
    entry_points={"textx_languages": ["strictdoc = tx_strictdoc:strictdoc"]},
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)