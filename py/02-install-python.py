#!/usr/bin/env python3

""" Install Python 3.10.4 """
import requests
import os
import tarfile
import subprocess as sp

""" Set variables """
version = "3.10.4"
dir_name = '/tmp/download'
filename = "Python-" + version + ".tgz"

""" Create directory """
print("Create directory")
try:
    os.mkdir(dir_name)
    os.chdir(dir_name)
    print("Directory {} created".format(dir_name))
except FileExistsError:
    print("Directory {} already exists".format(dir_name))

""" Download Python-3.10.4 """
file_path = dir_name + "/" + "Python-" + version + ".tgz"
URL = "https://www.python.org/ftp/python/{}/{}".format(version, filename)
print("Downloading {}".format(URL))
response = requests.get(URL)
open(file_path, 'wb').write(response.content)

""" Extract """
if filename.endswith(".tgz"):
    tar = tarfile.open(file_path, "r")
    print("Extracting {}".format(filename))
    tar.extractall()
    tar.close()

""" Install Python3.10.x """
print("Installing Python{}".format(version))
python_dir = dir_name + "/" + "Python-" + version
os.chdir(python_dir)
os.system('./configure --enable-optimizations && make -j 4 \
          && sudo make altinstall')

"""Check installed Python version """
python_version = sp.getoutput('python3.10 -V')
if python_version == "Python 3.10.4":
    print("Python version {} installed successfully".format(version))
else:
    print("Python version {} is not installed successfully".format(version))

""" Clean up """
print("Cleaning up")
print("Deleted {}".format(dir_name))
os.system('sudo rm -rf {}'.format(dir_name))
