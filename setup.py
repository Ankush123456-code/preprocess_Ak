import setuptools

with open('README.md', 'r') as file:
    long_description = file.read()

setuptools.setup(
    name='preprocess_Ak',  ## this should be unique
    include_package_data=True,
    version='0.0.1',
    author="Ankush kunwar",
    author_email="ankushkunwar1840@gmail.com",
    keywords="preprocessing package",
    description='clean your text',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent"],
    python_require='>=3.5',
    install_requires=['requests']
)
