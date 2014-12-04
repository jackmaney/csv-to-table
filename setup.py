from setuptools import find_packages, setup

requirements = []

with open("requirements.txt") as f:
    for line in f:
        line = line.strip()
        requirements.append(line)

setup(
    name="csv_to_table",
    version="0.0.3",
    description="Generates a CREATE TABLE statement from a CSV file by guessing at column types",
    author="Jack Maney",
    author_email="jackmaney@gmail.com",
    url="https://github.com/jackmaney/csv_to_table.py.git",
    license="MIT",
    scripts=["csv_to_table.py"],
    long_description=open("README.md").read(),
    entry_points={"console_scripts": ["csv-to-table=csv_to_table:main"]},
    classifiers=["Development Status :: 3 - Alpha",
                 "Intended Audience :: Science/Research",
                 "License :: OSI Approved :: MIT License",
                 "Programming Language :: Python :: 2 :: Only",
                 "Topic :: Utilities"],
    packages=find_packages(),
    install_requires=requirements
)
