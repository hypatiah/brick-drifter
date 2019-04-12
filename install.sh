#!/bin/bash

mkdir mygames
mkdir -p mygames/Figs
cd mygames

wget https://lsesec.com/publicprojects/pythonweek/raw/master/Game/pygame_tuto.ipynb
wget https://lsesec.com/publicprojects/pythonweek/blob/f51f7993c92ca1178cf27faba68ceae4084a7a5e/Game/Figs/car.jpg -p Figs
wget https://lsesec.com/publicprojects/pythonweek/blob/0c2ae5136767b241403d5db96dbd3db264846344/Game/Figs/car2.jpg -P Figs
wget https://lsesec.com/publicprojects/pythonweek/blob/0c2ae5136767b241403d5db96dbd3db264846344/Game/Figs/carMov.png -P Figs
wget https://lsesec.com/publicprojects/pythonweek/blob/0c2ae5136767b241403d5db96dbd3db264846344/Game/Figs/drawing.png -P Figs

python3 -m venv venv
source venv/bin/activate

pip install jupyter
pip install pygame
pip install numpy

cd terminal

jupyter notebook
