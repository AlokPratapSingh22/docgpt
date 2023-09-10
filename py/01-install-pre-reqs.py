#!/usr/bin/env python3

import os

""" Set variables """
BASE_DIR = os.getcwd()
# BLAKE_COMPILER_PATH = BASE_DIR + "/blake-2b-py"

""" Install ubuntu packages """
packages = ['build-essential', 'zlib1g-dev', 'libncurses5-dev', 'libgdbm-dev', 'libnss3-dev', 'libssl-dev',
            'libreadline-dev', 'libffi-dev', 'libsqlite3-dev', 'wget', 'python3-pip', 'libbz2-dev', 'make']

os.system('sudo apt-get update')

for package in packages:
    command = "sudo apt install -y {}".format(package)
    os.system(command)

# # """install rustup"""
# if os.path.exists(BLAKE_COMPILER_PATH):

#     os.chdir(BLAKE_COMPILER_PATH)

#     print("installing rustup...")
#     os.system("sh install.sh")
