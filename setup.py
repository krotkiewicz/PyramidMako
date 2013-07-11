import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
    'SQLAlchemy',
    'transaction',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'zope.sqlalchemy',
    'waitress',
    'beautifulsoup4',
    'mock',
    'lxml',
    'nokaut',
    'allegro',
    'wtforms',
]

depedency_list = [
    'https://github.com/waldest/nokaut/archive/master.tar.gz#egg=nokaut',
    'https://github.com/waldest/allegro/archive/master.tar.gz#egg=allegro'
]

setup(name='PyramidMako',
      version='1',
      description='PyramidMako',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='pyramidmako',
      dependency_links=depedency_list,
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = pyramidmako:main
      [console_scripts]
      initialize_PyramidMako_db = pyramidmako.scripts.initializedb:main
      """,
      )
