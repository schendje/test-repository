from distutils.core import setup

setup(
    name='Magicmap',
    version='0.1.0',
    author='Jef van Schendel',
    author_email='mail@jefvanschendel.nl',
    packages=['magicmap'],
    scripts=['bin/generate-magicmap.py'],
    url='',
    license='LICENSE.txt',
    description='Magicmap description',
    long_description=open('README.md').read(),
    install_requires=[],
)
