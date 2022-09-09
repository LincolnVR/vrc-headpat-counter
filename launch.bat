@echo off
echo "Installing requirements (be sure to have python installed and in PATH)"
pip install -r requirements.txt
python3 osc_counter/setup.py
pause
