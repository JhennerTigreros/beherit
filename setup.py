__version__ = '0.0.1'

from glob import glob
from pathlib import Path

DIR = Path(__file__).parent.resolve()

import os
import sys

sys.path.append(str(DIR / "extern" / "pybind11"))

from pybind11.setup_helpers import ParallelCompile, Pybind11Extension

del sys.path[-1]

from setuptools import setup

INCLUDE_DIRS = [
    "extern/pybind11/include",
]

ParallelCompile("CMAKE_BUILD_PARALLEL_LEVEL").install()
cxx_std = int(os.environ.get("CMAKE_CXX_STANDARD", "17"))

ext_modules = [
    Pybind11Extension(
        "beherit",
        sorted(glob("beherit/**/**.cpp")),
        cxx_std=cxx_std,
        include_dirs=INCLUDE_DIRS,
        define_macros=[("VERSION_INFO", __version__), ("PYBIND11_DETAILED_ERROR_MESSAGES", "1")],
        include_pybind11=False,
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
