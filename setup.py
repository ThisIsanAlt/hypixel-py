import setuptools


setuptools.setup(
    name="hypixel_py",
    version="0.0.1",
    author="ThisIsanAlt",
    description="Simple wrapper for the Hypixel API.",
    url="https://github.com/ThisIsanAlt/hypixel-py",
    project_urls={
        "Bug Tracker": "https://github.com/ThisIsanAlt/hypixel-py/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)