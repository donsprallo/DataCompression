from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pycompress-don",
    version="0.0.2",
    author="Nico Hanisch",
    author_email="donsprallo@gmail.com",
    description="A data compression tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/donsprallo/DataCompression",
    packages=[
        'pycompress',
        'pycompress.compression'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        'Environment :: Console',
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        'Topic :: Utilities',
    ],
    python_requires='>=3.6',
    install_requires=[
        "progress",
    ],
    entry_points={
        'console_scripts': [
            'pycompress=pycompress.main:main'
        ]
    },
)
