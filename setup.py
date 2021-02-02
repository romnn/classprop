#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import find_packages, setup
from pathlib import Path

short_description = "No description has been added so far."

version = "0.1.1"

try:
    if (Path().parent / "README.rst").is_file():
        with open(str(Path().parent / "README.rst")) as readme_file:
            long_description = readme_file.read()
    elif (Path().parent / "README.md").is_file():
        import m2r

        long_description = m2r.parse_from_file(Path().parent / "README.md")
    else:
        raise AssertionError("No readme file")
except (ImportError, AssertionError):
    long_description = short_description

requirements = ["Click>=6.0"]
test_requirements = [
    "tox",
    "pytest",
    "pytest-cov",
    "pytest-xdist",
    "pytest-sugar",
    "mypy",
    "pyfakefs",
]
coverage_requirements = ["coverage", "codecov"]
docs_requirements = []
formatting_requirements = ["flake8", "black==19.10b0", "isort"]
tool_requirements = [
    "m2r",
    "twine",
    "invoke",
    "ruamel.yaml",
    "pre-commit",
    "cookiecutter",
    "bump2version",
]
dev_requirements = (
    requirements
    + test_requirements
    + coverage_requirements
    + docs_requirements
    + formatting_requirements
    + tool_requirements
)

setup(
    author="romnn",
    author_email="contact@romnn.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.6",
    install_requires=requirements,
    setup_requires=tool_requirements,
    tests_require=test_requirements,
    extras_require=dict(
        dev=dev_requirements, docs=docs_requirements, test=test_requirements
    ),
    license="MIT",
    description=short_description,
    long_description=long_description,
    include_package_data=True,
    package_data={"classprop": []},
    keywords="classprop",
    name="classprop",
    packages=find_packages(include=["classprop"]),
    test_suite="tests",
    url="https://github.com/romnn/classprop",
    version=version,
    zip_safe=False,
)
