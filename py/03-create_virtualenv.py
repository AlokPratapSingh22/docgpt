#!/usr/bin/env python3.10

import os
import shutil
from pathlib import Path

""" Delete virtual environment if exist and create it """
base_path = Path(os.getcwd() + "/venv")
if base_path.exists() and base_path.is_dir():
    print("Delete virtual environment...")
    shutil.rmtree(base_path)

""" Create virtual environment """
print("Create virtual environment...")
os.system("python3.10 -m venv venv")

""" Activate virtual environment and install python packages """
print("Install packages...")
os.system('. venv/bin/activate && python3.10 -m pip install --upgrade pip && pip install -r requirements.txt')
