from setuptools import setup

setup(
    name="Flutter pubspec updater",
    version="1.1",
    author="Gianluca Lofrumento",
    author_email="gianluca.lofrumento@gmail.com",
    description="Update all the packages in pubspec.yaml of a Flutter project.",
    scripts=["pubspec_update"],
    requires=[
        "aiohttp",
        "argparse",
        "asyncio",
        "pyyaml",
        "beautifulsoup4",
        "tabulate"
    ]
)