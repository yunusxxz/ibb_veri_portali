from setuptools import setup, find_packages

setup(
    name="ibb_veri_portali",
    version="0.2.0",
    description="Ibb Portal",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="yunusx",
    author_email="isikyunusemre63@gmail.com",
    url="https://github.com/yunusxxz",
    packages=find_packages(),
    install_requires=["pandas", "requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6"
)
