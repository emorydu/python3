import setuptools
from pathlib import Path


setuptools.setup(
    name="emorydupdf",
    version="1.0",
    long_description=Path("README.md").read_text(),
    packages=setuptools.find_packages(exclude=["tests", "data"]),
)

# python setup.py sdist bdist_wheel
# twine upload dist/*
