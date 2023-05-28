from setuptools import setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setup(
    name="nexus-db",
    version="0.1",
    packages=["nexus_db"],
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "nexus=nexus_db.cli.main:main",
        ],
    },
)
