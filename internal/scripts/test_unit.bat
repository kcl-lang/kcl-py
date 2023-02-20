cd %~dp0
cd ..\\..

set "PYTHONPATH=%cd%"

python3 -m pip install -r .\kclvm\scripts\requirements.txt
python3 -m pip install --upgrade pip
python3 -m pip install pytest pytest-xdist

cd %cd%\\test\\test_units
python3 -m pytest -vv -n 10
