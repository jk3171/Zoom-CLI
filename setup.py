import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zoom-cli",
    version="0.2",
    author="JK3171",
    author_email="JK3171@JK3171Tech.com",
    description="An easier way to automate joining Zoom meetings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jk3171/Zoom-CLI",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Business/Education"
    ],
    entry_points='''
        [console_scripts]
        zcli=zoomcli.zoomcli:zoomcli
    '''
)