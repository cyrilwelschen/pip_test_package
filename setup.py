import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pip_test_package",
    version="0.0.1",
    author="Cyril Welschen",
    author_email="cj.welschen@gmail.com",
    description="First test for pip python package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cyrilwelschen/pip_test_package",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
