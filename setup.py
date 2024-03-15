from setuptools import setup, find_packages

setup(
    name="zompy",
    version="0.1.0",
    author="Enrico Mautone",
    author_email="enrico.mautone@gmail.com",
    description="A powerful python web crawler",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/enrico-mautone/zompy",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=open('requirements.txt').read().splitlines(),
)
