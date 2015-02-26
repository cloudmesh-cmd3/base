#!/usr/bin/env python

#from distutils.core import setup

from setuptools import setup, find_packages
from setuptools.command.install import install
import glob
import os
from cloudmesh_base.base import banner

# try:
#     from fabric.api import local
# except:
#     os.system("pip install fabric")
#     from fabric.api import local

home = os.path.expanduser("~")

        
class InstallBase(install):
    """Install the package."""
    def run(self):
        banner("Install Cloudmesh Base")
        install.run(self)

class InstallRequirements(install):
    """Install the requirements."""
    def run(self):
        banner("Install Cloudmesh Base Requirements")
        os.system("pip install -r requirements.txt")
        
class InstallAll(install):
    """Install requirements and the package."""
    def run(self):
        banner("Install Cloudmesh Base Requirements")
        os.system("pip install -r requirements.txt")
        banner("Install Cloudmesh Base")        
        install.run(self)
        
setup(
    name='cloudmesh_base',
    version=__import__('cloudmesh_base').__version__,
    description='A set of simple base functions and classes useful for cloudmesh and other programs',
    # description-file =
    #    README.rst
    author='The Cloudmesh Team',
    author_email='laszewski@gmail.com',
    url='http://github.org/cloudmesh/base',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering',
        'Topic :: System :: Clustering',
        'Topic :: System :: Distributed Computing',
        'Topic :: System :: Boot',
        'Topic :: System :: Systems Administration',
        'Framework :: Flask',
        'Environment :: OpenStack',
    ],
    packages=find_packages(),
    include_package_data=True,
#    data_files=[
#        (home + '/.cloudmesh', [
#            'etc/FGLdapCacert.pem',
#            'etc/india-havana-cacert.pem',
#            'etc/cloudmesh_flavor.yaml']),
#        (home + '/.cloudmesh/etc', [
#            'etc/cloudmesh.yaml',
#            'etc/me-none.yaml',
#            'etc/cloudmesh.yaml',
#            'etc/cloudmesh_server.yaml',
#            'etc/cloudmesh_rack.yaml',
#            'etc/cloudmesh_celery.yaml',
#            'etc/cloudmesh_mac.yaml',
#            'etc/cloudmesh_flavor.yaml',
#            'etc/ipython_notebook_config.py']),
#    ],
#    entry_points={'console_scripts': [
#        'cm-cluster = cloudmesh.cluster.cm_shell_cluster:main',
#    ]},
    cmdclass={
        'install': InstallBase,
        'requirements': InstallRequirements,
        'all': InstallAll,
        },
)

