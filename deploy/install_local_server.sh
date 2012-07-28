#!/bin/bash
# All python requirements are installed into a virtual environment

echo "install virtual env"
sudo easy_install virtualenv

echo "create and activate virtual environment"
virtualenv --no-site-packages env
. env/bin/activate

echo "install requirements"
pip install -r deploy/python_requirements.txt
