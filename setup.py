#!/usr/bin/env python

from setuptools import setup
import django_swagger

description = "An adapter to use swagger-ui with django-tastypie"

try:
    longdesc = open('README.rst').read()
except Exception:
    longdesc = description

setup(
    # Metadata
    name='django-swagger-rk',
    description=description,
    long_description=longdesc,
    author='RK',
    author_email='test',
    classifiers=[
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
    url='https://github.com/Rohit1601/django-swagger-rk',
    download_url='https://github.com/Rohit1601/django-swagger-rk/downloads',
    license='BSD',
    packages=['django_swagger'],
    include_package_data=True,
    zip_safe=False,
)
