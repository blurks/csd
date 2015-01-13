from setuptools import setup, find_packages

requires = [
    'clld>=0.28',
    'clldmpg>=0.5',
    ]

tests_require = [
    'WebTest >= 1.3.1', # py3 compat
    'mock',
]

setup(name='csd',
      version='0.0',
      description='csd',
      long_description='',
      classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=tests_require,
      test_suite="csd",
      entry_points="""\
[paste.app_factory]
main = csd:main
""",
      )
