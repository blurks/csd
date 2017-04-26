from setuptools import setup, find_packages


setup(
    name='csd',
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
    author='Robert Forkel, MPI SHH',
    author_email='forkel@shh.mpg.de',
    url='http://csd.clld.org',
    keywords='web pyramid pylons',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'clld>=3.0.2',
        'clldmpg>=2.0.0',
    ],
    tests_require=[
        'WebTest >= 1.3.1',  # py3 compat
        'mock>=2.0',
    ],
    test_suite="csd",
    entry_points="""\
[paste.app_factory]
main = csd:main
""")
