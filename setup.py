from setuptools import setup

setup(
    name='memcache_lock',
    version='0.1',
    description='Locking mechanism for Python 2.7 GAE, using memcache',
    url='https://github.com/linuxpi/memcache_lock',
    author='Varun Bansal',
    author_email='varunb94@gmail.com',
    license='MIT',
    packages=['memcache_lock'],
    zip_safe=False
)