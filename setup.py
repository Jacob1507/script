from setuptools import setup, find_packages


def read_requirements():
    with open("requirements.txt") as req:
        content = req.read()
        requirements = content.split("\n")
        return requirements


setup(
    name="script",
    version=0.1,
    packages=find_packages(),
    include_package_data=True,
    install_requirements=read_requirements(),
    url="https://github.com/Jacob1507/balldontlie_script",
    license='MIT',
    entry_points="""
        [console_scripts]
        script=script.cli:cli
    """
)
