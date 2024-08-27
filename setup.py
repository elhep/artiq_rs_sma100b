from setuptools import find_packages, setup

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="artiq_rs_sma100b",
    install_requires=required,
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "aqctl_artiq_rs_sma100b = artiq_rs_sma100b.artiq_rs_sma100b:main",
        ],
    },
)
