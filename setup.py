import re, uuid

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='python-loklak-api',
	  version='1.0',
	  description="Python API for loklak, Anonymous distributed P2P Systems.",
      'author='Sudheesh Singanamalla',
      'author_email='sudheesh95@gmail.com',
      url='https://github.com/sudheesh001/python-loklak-api',
      license='',
      platforms='Linux/Mac',
      py_modules=['loklak'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Topic :: Internet',
          ],
      keywords="Twitter Loklak Anonymous API",
      install_requires = [
        "asyncoro==3.5",
        "requests==2.8.1",
        "wsgiref==0.1.2"
      ],
      zip_safe=False,
      download_url = 'https://github.com/sudheesh001/python-loklak-api',
      entry_points={'console_scripts': ['python-loklak-api = loklak:main']},
      )
