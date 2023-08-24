echo [1]Creating Python Environment
python3 -m venv PyEnv
echo [1]Done.
echo [2]Activating the Environment.
source PyEnv/bin/activate
echo [2]Done.
echo [3]Installing the needed Packages
pip3 install numpy
pip3 install py_canoe
pip3 install pandas
echo [3]Done.
