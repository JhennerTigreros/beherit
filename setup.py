__version__ = '0.0.1'

from glob import glob

from pybind11.setup_helpers import Pybind11Extension
from setuptools import setup

ext_modules = [
    Pybind11Extension(
        "beherit",
        sorted(glob("beherit/*.cpp")),
        define_macros=[("VERSION_INFO", __version__)],
    ),
]

setup(
    name="beherit",
    version=__version__,
    author="Jhenner Tigreros",
    author_email="jtigreros16@gmail.com",
    url="https://github.com/JhennerTigreros/beherit",
    description="A simple library to deploy neural models",
    ext_modules=ext_modules,
    extras_require={
        "linting": [
            "pylint",
            "ruff",
            "pre-commit"
        ],
        "tests": "pytest",
    },
)
