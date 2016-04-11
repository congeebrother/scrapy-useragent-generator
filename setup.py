import re


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


version = ''
with open('useragent-generator/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

setup(
    name='scrapy-useragent-generator',
    version=version,
    description='based on user_agent,generat random useragent by platform',
    packages=['useragent-generator'],
    include_package_data=True,
    url='https://github.com/congeebrother/scrapy-useragent-generator',
    author='daniel liu',
    author_email='daniel_001@126.com',
    install_requires=[
        'scrapy>1.0.0',
        'user_agent',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
)