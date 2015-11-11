django-colorful
===============

[![Build Status](https://travis-ci.org/charettes/django-colorful.svg?branch=master)](https://travis-ci.org/charettes/django-colorful)
[![Coverage Status](https://coveralls.io/repos/charettes/django-colorful/badge.svg?branch=master&service=github)](https://coveralls.io/github/charettes/django-colorful?branch=master)

**django-colorful** is an extension to the Django web framework that provides
database and form color fields (only RGB atm).

Originally written by Simon Charette
Inspired by http://djangosnippets.org/snippets/1261/

Forked to use HTML5 input types.

Installation
------------

Downloading the source and running:

    $ python setup.py install

Latest git version:

    $ pip install -e git+git://github.com/adongy/django-colorful.git#egg=django-colorful

Usage
-------------
In order to use a color field you just have to add it to your model definition:

    from django.db import models
    from colorful.fields import RGBColorField

    class Tag(models.Model):
        color = RGBColorField()
