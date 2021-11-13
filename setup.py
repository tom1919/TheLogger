from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
  name = 'thelogger',       
  packages = ['thelogger'],  
  version = 'v0.1.0',      
  license='Apache 2.0',       
  description = 'super easy to use logger object',  
  long_description = long_description,
  long_description_content_type = 'text/markdown',
  author = 'Tom1919',                   
  author_email = 'py.notify1@gmail.com',      
  url = 'https://github.com/tom1919/TheLogger,  
  download_url = 'https://github.com/tom1919/TheLogger/archive/refs/tags/v0.1.0.tar.gz',   
  keywords = ['log', 'logging', 'logger'],  
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',     
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)