#!/bin/bash
apt install python3-pycryptodome

git clone https://github.com/Legrandin/pycryptodome.git;
cd pycryptodome;
python3 setup.py build;
python3 setup.py install
