import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gcp-python-logging",
    version="1.1.0",
    author="Daniel Hawes",
    author_email="hawesdb@gmail.com",
    description="A python module for the handy printing of logs to StackDriver based on severity",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hawesdb/gcp-python-logging",
    packages=setuptools.find_packages(),
    install_requires=[
        'google-cloud-logging'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)