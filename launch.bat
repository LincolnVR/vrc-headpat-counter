@echo off
echo "Installing requirements (be sure to have python installed and in PATH)"
pip install -r osc_counter/requirements.txt
python osc_counter/setup.py
pause