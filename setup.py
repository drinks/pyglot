from distutils.core import setup

long_description = open('README.md').read()

setup(name="pyglot",
      version="0.1.0",
      py_modules=["pyglot"],
      description="A library for interacting with the Google Translate API",
      author="Dan Drinkard <dan.drinkard@gmail.com>",
      author_email="dan.drinkard@gmail.com",
      license="BSD",
      url="http://github.com/dandrinkard/pyglot",
      long_description=long_description,
      platforms=["any"],
      classifiers=["Development Status :: 4 - Beta",
                   "Intended Audience :: Developers",
                   "Natural Language :: English",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Topic :: Software Development :: Libraries :: Python Modules",
                   ],
       install_requires=["simplejson >= 1.8"]
      )
