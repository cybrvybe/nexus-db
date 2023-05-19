from setuptools import setup

setup(
    name="nexus-db",
    version="0.1",
    packages=["nexus_db"],
    entry_points={
        "console_scripts": [
            "nexus=nexus_db.cli.main:main",
        ],
    },
)
