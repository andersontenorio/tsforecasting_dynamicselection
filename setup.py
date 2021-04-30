from setuptools import setup, find_packages

with open('README.md') as f:
    readme: str = f.read()

setup(
    name="tsforecasting_dynamicselection",
    description="Dynamic Selection for Time Series Forecasting",
    packages=find_packages(exclude=["tests"]),
    version=0.1,
    license="MIT",
    author="Anderson Tenório Sergio",
    long_description=readme,
    author_email="anderson.sergio@gmail.com",
    url="https://github.com/andersontenorio/tsforecasting_dynamicselection",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: MIT",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Time Series Forecasting"
    ],
    python_requires='>=3.8.*',
    install_requires=[
        "numpy"
    ],
    extras_require={
        'tests': [""],
        'style': ["flake8", "mypy"]
    }
)