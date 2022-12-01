#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages
import os

with open('README.md', encoding='utf-8') as readme_file:
    readme = readme_file.read()

thelibFolder = os.path.dirname(os.path.realpath(__file__))
requirements = [ ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Simon Cozens",
    author_email='simon@simon-cozens.org',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Data derived from the OpenType specification",
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='opentypespec',
    name='opentypespec',
    packages=find_packages(include=['opentypespec', 'opentypespec.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/simoncozens/opentypespec-py',
    version='1.9.0',
    zip_safe=False,
)
