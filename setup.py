#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from setuptools import setup, find_packages
import os
import fancy_cronfield

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Framework :: Django',
    'Framework :: Django :: 1.5',
    'Framework :: Django :: 1.6',
    'Framework :: Django :: 1.7',
    'Framework :: Django :: 1.8',
    'Framework :: Django :: 1.9',
    'Framework :: Django :: 1.10',
    'Framework :: Django :: 1.11',
    'Framework :: Django :: 2.0',
    'Framework :: Django :: 2.1',
]

INSTALL_REQUIREMENTS = [
    'django>=1.5,<=2.3',
    'python-crontab==1.9.3',
]

readme_path = os.path.join(os.path.dirname(__file__), 'README.rst')
long_description = open(readme_path).read()

setup(
    name="django-fancy-cronfield",
    author="Saeed Salehian",
    author_email="saeed.sq@gmail.com",
    version=fancy_cronfield.__version__,
    description="A nice and customizable cron field with easy to use UI",
    long_description=long_description,
    url='https://github.com/saeedsq/django-fancy-cronfield',
    license='BSD License',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=INSTALL_REQUIREMENTS,
    extras_require={},
    packages=find_packages(exclude=[]),
    include_package_data=True,
    zip_safe=False,
    test_suite='runtests.main',
)
