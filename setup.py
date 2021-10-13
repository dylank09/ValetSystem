
from setuptools import setup, find_packages
from valetsystem.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='valetsystem',
    version=VERSION,
    description='MyApp Does Amazing Things!',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Dylan Kearney',
    author_email='dylank09@gmail.com',
    url='https://github.com/dylank09/ValetSystem/',
    license='unlicensed',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'valetsystem': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        valetsystem = valetsystem.main:main
    """,
)
