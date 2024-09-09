@echo off

cd %~dp0

call %~dp0\.venv\Scripts\activate.bat

python TheLoupe.py

deactivate

pause