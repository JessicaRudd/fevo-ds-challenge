from pathlib import Path
from setuptools import find_packages, setup

BASE_DIR = Path(__file__).parent

# Load packages from requirements.txt
with open(Path(BASE_DIR, "requirements.txt"), "r") as file:
    required_packages = [ln.strip() for ln in file.readlines()]

test_packages = [
    "pytest==6.1.2",
    "pytest-cov==2.10.1",
    "pytest-parametrize-cases==0.1.2",
]

dev_packages = [
    "black==20.8b1",
    "flake8==3.8.3",
    "isort==5.9.3",
    "mccabe==0.6.0",
    "pre-commit==2.19.0",
    "jupyterlab>=3.0.0",
    "jupyterlab-templates==0.3.1",
    "coverage[toml]",
]

docs_packages = [
    "mkdocs==1.1.2",
    "mkdocs-macros-plugin==0.5.0",
    "mkdocs-material==6.2.4",
    "mkdocstrings==0.14.0",
    "sphinx==4.5.0",
    "myst-parser==0.17.2",
]

setup(
    name='fevo-ds-challenge',
    packages=find_packages(),
    version='0.1.0',
    description='data, code, documentation related to the FEVO interview data scientist challenge',
    author='Jessica M. Rudd, PhD',
    license='MIT',
    python_requires=">=python3",
    install_requires=[required_packages],
    extras_require={
        "test": test_packages,
        "dev": test_packages + dev_packages + docs_packages,
        "docs": docs_packages,
    },
)
