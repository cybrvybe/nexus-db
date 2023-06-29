from setuptools import setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setup(
    name="oversoul-db",
    version="0.1",
    packages=["oversoul_db"],
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "oversoul=oversoul_db.cli.main:main",
        ],
    },
)
