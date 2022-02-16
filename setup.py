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
    name='django-tastypie-swagger',
    version='.'.join(map(str, django_swagger.VERSION)),
    description=description,
    long_description=longdesc,
    author='Concentric Sky',
    author_email='code@concentricsky.com',
    classifiers=[
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
    url='https://github.com/concentricsky/django-tastypie-swagger',
    download_url='https://github.com/concentricsky/django-tastypie-swagger/downloads',
    license='BSD',
    packages=['django_swagger'],
    include_package_data=True,
    zip_safe=False,
)
