from setuptools import setup, find_packages

ver = 'v0.4.1'

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name = 'thelogger',       
  packages = ['thelogger', 'thelogger.notify'],  
  version = ver,      
  license='Apache 2.0',       
  description = 'Easy logging, timing and email notifications of code execution.',  
  long_description = long_description,
  long_description_content_type = 'text/markdown',   
  keywords = ['log', 'logging', 'logger', 'email', 'timimg', 'notification'],  
  install_requires = ['pandas','tabulate', 'importlib-metadata >= 1.0 ; python_version < "3.8"',
  'pytz', 'psutil', 'tzlocal'], 
  python_requires='>3.8',
  classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',     
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
