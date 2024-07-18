from setuptools import setup

# read the contents of README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='floryn',
    packages=['floryn'],
    version='0.0.1',
    description='Plot percentage filled text',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='M Iqbal Tawakal',
    author_email='mit.iqi@gmail.com',
    url='https://github.com/mitbal/floryn',
    keywords='plot matplotlib seaborn',
    classifiers=[],
    install_requires=[
        'matplotlib>=3.9.0',
        'seaborn>=0.13.2',
        'numpy>=1.26.4',
        'scikit-image>=0.24.0'
    ]
)
