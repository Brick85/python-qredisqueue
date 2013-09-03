#!/usr/bin/env python
from setuptools import setup

setup(name='python-qredisqueue',
      version='0.0.1',
      description='Simple redis-based queue.',
      long_description='Simple redis-based queue. Taked from http://peter-hoffmann.com/2012/python-simple-queue-redis-queue.html',
      author='Vital Belikov',
      author_email='vital@qwe.lv',
      packages=['qredisqueue'],
      url='https://github.com/Brick85/python-qredisqueue/',
      include_package_data=True,
      zip_safe=False,
      requires=['redis(>=2.8)'],
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Natural Language :: English',
                   'Operating System :: Unix',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: Utilities'],
      license='New BSD')
