@echo off
python -m pip install virtualenv
python -m venv env
pip install -U pyinstaller
pip install pycaw
pyinstaller --noconsole --add-data "robin.wav;." --add-data "sound_opening.wav;." main.py