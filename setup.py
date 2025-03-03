from setuptools import setup, find_packages
import os

# Read README.md if it exists
try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = "A specialized security tool for analyzing URLs that employ bot detection techniques"

# Define the requirements directly in setup.py
requirements = [
    "undetected-chromedriver>=3.5.0",
    "selenium>=4.9.0",
    "requests>=2.28.2",
    "python-dotenv>=1.0.0",
    "urllib3>=2.0.0"
]

# Try to read requirements from file if it exists
if os.path.exists("requirements.txt"):
    try:
        with open("requirements.txt", "r", encoding="utf-8") as fh:
            file_requirements = fh.read().splitlines()
            file_requirements = [line for line in file_requirements 
                                if line and not line.startswith('#')]
            if file_requirements:
                requirements = file_requirements
    except Exception:
        pass

setup(
    name="script_of_mensis",
    version="1.0.0",
    author="Rezznux",
    author_email="your.email@example.com",  # Update with your email
    description="A specialized security tool for analyzing URLs that employ bot detection techniques",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Rezznux/Script_of_Mensis",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "vileblood=script_of_mensis.scripts.vileblood:main",
        ],
    },
    # Include non-Python files
    package_data={
        "script_of_mensis": ["../config/*", "../data/**/*"],
    },
)