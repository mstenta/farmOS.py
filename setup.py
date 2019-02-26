import setuptools

with open('README.md', 'r') as fh:
    readme = fh.read()

setuptools.setup(
    name='farmOS',
    version='0.0.1',
    author='Michael Stenta',
    author_email='mike@mstenta.net',
    description='A Python library for interacting with farmOS over API. ',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/farmOS/farmOS.py',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
)
