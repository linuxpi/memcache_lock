import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='memcache_lock',
    version='0.0.3',
    description='Locking mechanism for Python 2.7 GAE, using memcache',
    long_description=read('README.md'),
    url='https://github.com/linuxpi/memcache_lock',
    author='Varun Bansal',
    author_email='varunb94@gmail.com',
    license='MIT',
    packages=find_packages(),
    zip_safe=False,
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2'
    )
)
