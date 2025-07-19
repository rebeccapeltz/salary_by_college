python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

pip install --upgrade pip setuptools wheel
pip uninstall numpy pandas
pip install numpy pandas

pip install --no-binary :all: numpy

1003  ls .venv
 1004  sudo rm -rf .venv
 1005  python3 -m venv .venv
 1006  source .venv/bin/activate
 1007  pip install -r requirements.txt
 1008  pip install --upgrade pip
 1009  python3 dash_app.py
 1010  pip install pandas
 1011  pip show pandas
 1012  which python3
 1013  python3
 1014  pip install --upgrade pip setuptools wheel
 1015  pip uninstall numpy pandas
 1016  pip install numpy pandas
 1017  python3 dash_app.py
 1018  python3 dash_app.py --expose_to_public_internet