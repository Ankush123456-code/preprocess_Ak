import setuptools

with open('README.md', 'r') as file:
    long_description = file.read()

setuptools.setup(
    name='preprocess_Ak',  ## this should be unique
    version='0.0.1',
    author="Ankush kunwar",
    author_email="ankushkunwar1840@gmail.com",
    description='clean your text',
    Long_despription=long_description,
    Long_description_content="text/markdown",
    pakage=setuptools.find_packages(),
    Classifiers=['Programming Language:: Python :: 3',
                 'License :: OSI Approved :: MIT License',
                 'Operating System :: OS Independent'],
    python_require='>=3.5'
)
