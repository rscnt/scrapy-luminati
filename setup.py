from setuptools import setup

with open("README.rst") as f:
    readme = f.read()


setup(
    name='scrapy-luminati',
    version='1.7.4-luuk',
    license='BSD',
    description='Luminati middleware for Scrapy',
    long_description=readme,
    maintainer='Raul Gallegos',
    maintainer_email='raul.ogh@gmail.com',
    author='Scrapinghub',
    author_email='opensource@scrapinghub.com',
    url='https://github.com/scrapy-plugins/scrapy-crawlera',
    packages=['scrapy_luminati'],
    platforms=['Any'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Framework :: Scrapy',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: Proxy Servers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=['scrapy>=1.0.0', 'six', 'w3lib'],
)
