from setuptools import setup, find_packages

setup (
    name="rtk-cli",
    version="0.0.1",
    description="A CLI Tool for identifying Heisig-method primitives and explanations for Kanji characters",
    author="Cole Lanham",
    author_email="coleklanham@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
             "rtk-cli = cli.rtk_cli:run_cli"
        ]
    }
)