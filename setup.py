__version__ = '0.0.1'

from pathlib import Path

DIR = Path(__file__).parent.resolve()

from setuptools import setup

setup(
    name="beherit",
    version=__version__,
    author="Jhenner Tigreros",
    author_email="jtigreros16@gmail.com",
    url="https://github.com/JhennerTigreros/beherit",
    description="A simple library to deploy neural models",
    extras_require={
        "linting": [
            "pylint",
            "ruff",
            "pre-commit"
        ],
        "tests": "pytest",
    },
)