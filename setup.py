"""

"""

import setuptools

REQUIRED = [
    "numpy",
    'pandas',
    'random',

]

with open('README.md', 'r')as files:
    LONG_DESCRIPTION = file.read()

setuptools.setup(
    name = 'lambdata-vdeb',
    version = '0.0.1',
    author = 'vdeb'
    description = '',
    long_description = LONG_DESCRIPTION,
    long_description_content = 'text/markdown',
    url = 'https://github.com/VPDeb/LambData',
    packages = setuptools.find_packages(),
    python_requires ='>=3.8',
    install_requires = REQUIRED,
    classifiers=[
        'Program Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ]
)