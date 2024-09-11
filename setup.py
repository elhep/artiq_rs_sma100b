from setuptools import find_packages, setup
from setuptools.command.install import install
import subprocess

with open("requirements.txt") as f:
    required = f.read().splitlines()


class PostInstallCommand(install):
    def run(self):
        install.run(self)
        subprocess.call(['bash', 'install.sh'])


setup(
    name="artiq_rs_sma100b",
    install_requires=required,
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "aqctl_artiq_rs_sma100b = artiq_rs_sma100b.aqctl_artiq_rs_sma100b:main",
        ],
    },
)
