from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pycompress",
    version="0.0.2",
    author="Nico Hanisch",
    author_email="donsprallo@gmail.com",
    description="A data compression tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/donsprallo/DataCompression",
    packages=[
        'datacompression',
        'datacompression.compression'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL3 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "progress",
    ],
    entry_points={
        'console_scripts': [
            'pycompress=datacompression.main:main'
        ]
    },
)
