#!/usr/local/bin/python3.9
# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4:

from setuptools import setup, find_packages
from setuptools.command.install import install
import os
import shutil

config_dir = '/usr/local/etc/xsser'
core_dir = '/usr/local/etc/xsser/core'
doc_dir = '/usr/local/etc/xsser/doc'
gtk_dir = '/usr/local/etc/xsser/gtk'

for path in [config_dir, core_dir, doc_dir, gtk_dir]:
    os.makedirs(path, exist_ok=True)

dirs = ['core', 'doc', 'gtk']

for i in dirs:
    local_dir = i  # Assuming 'core' is in the current working directory
    target_dir = '/usr/local/etc/xsser/' + i

    if os.path.exists(local_dir):
        for item in os.listdir(local_dir):
            local_item = os.path.join(local_dir, item)
            target_item = os.path.join(target_dir, item)

            # Check if the item is a file and copy it
            if os.path.isfile(local_item):
                shutil.copy(local_item, target_item)
            # Check if the item is a directory and copy it recursively
            elif os.path.isdir(local_item):
                shutil.copytree(local_item, target_item, dirs_exist_ok=True)

image_files = []
doc_files = []
gtk_doc_files = []

for afile in os.listdir('doc'):
    if afile != '.svn':
        doc_files.append('doc/' + afile)
for afile in os.listdir('gtk/docs'):
    if afile != '.svn':
        gtk_doc_files.append('gtk/docs/' + afile)
data_files = ['gtk/images/world.png',
              'gtk/images/xsser.jpg',
              'gtk/images/xssericon_16x16.png',
              'gtk/images/xssericon_24x24.png',
              'gtk/map/GeoIP.dat']
gtk_files = ['gtk/xsser.ui']
gtk_app_files = ['gtk/xsser.desktop']

setup(
    name="xsser",
    version="1.8.4",
    packages=['core', 'core.fuzzing', 'core.post', 'core.driver', 'gtk'],  # Explicitly list the packages
    data_files=[('/usr/share/doc/xsser/', doc_files),
                ('/usr/share/xsser/gtk/images/', data_files),
                ('/usr/share/xsser/gtk/docs/', gtk_doc_files),
                ('/usr/share/applications/', gtk_app_files),
                ('/usr/share/xsser/gtk/', gtk_files)],
    entry_points={
        'console_scripts': ['xsser = xsser:main'],
    },
    test_suite="tests",
)
