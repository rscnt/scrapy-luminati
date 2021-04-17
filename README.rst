===============
scrapy-crawlera
===============

.. image:: https://img.shields.io/pypi/v/scrapy-crawlera.svg
   :target: https://pypi.python.org/pypi/scrapy-crawlera
   :alt: PyPI Version

.. image:: https://travis-ci.org/scrapy-plugins/scrapy-crawlera.svg?branch=master
   :target: http://travis-ci.org/scrapy-plugins/scrapy-crawlera
   :alt: Build Status

.. image:: http://codecov.io/github/scrapy-plugins/scrapy-crawlera/coverage.svg?branch=master
   :target: http://codecov.io/github/scrapy-plugins/scrapy-crawlera?branch=master
   :alt: Code Coverage

scrapy-crawlera provides easy use of `Crawlera <http://scrapinghub.com/crawlera>`_ with Scrapy.

Requirements
============

* Python 2.7 or Python 3.4+
* Scrapy

Installation
============

You can install scrapy-crawlera using pip::

    pip install scrapy-crawlera


Documentation
=============

Documentation is available online at https://scrapy-crawlera.readthedocs.io/ and in the ``docs`` directory.


To enable the use of the luminati proxy, set as `True` either
`luminati_enabled` in the spider config or `LUMINATI_ENABLED` in the project
configs.

Other config values are:

Project config:

- `LUMINATI_USER` 
- `LUMINATI_PASSWORD` 
- `LUMINATI_DOWNLOAD_TIMEOUT` 
- `LUMINATI_MAXBANS` 
- `LUMINATI_FORCE_ENABLE_ON_HTTP_CODES` 

Spider config:

- `luminati_user` 
- `luminati_password` 
- `luminati_download_timeout` 
- `luminati_maxbans` 
- `luminati_force_enable_on_http_codes` 
