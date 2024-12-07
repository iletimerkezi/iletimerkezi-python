from setuptools import setup, find_packages

setup(
    name="iletimerkezi",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests>=2.25.0;python_version>='3.7'",  # Optional HTTP client
        "urllib3>=1.26.0",  # Required for default HTTP client
    ],
    extras_require={
        'dev': [
            'pytest>=6.0',
            'pytest-cov>=2.0',
            'black>=22.0',
            'mypy>=0.900',
        ],
    },
    python_requires=">=3.7",
)
