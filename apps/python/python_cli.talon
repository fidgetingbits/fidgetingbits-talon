tag: terminal
-

###
# Python
###
(pie | python) new [virtual] (env | environment): "python -m venv env"
python module: "python -m "
python reactivate: "deactivate && source env/bin/activate\n"
python (activate | enter) [env | environment]: "source env/bin/activate\n"
python (deactivate | leave) [env | environment]: "deactivate\n"

python three eight env: "virtualenv -p python3.8 py38"
python three nine env: "virtualenv -p python3.9 py39"

pie new env with rex: "python -m venv env/ && source env/bin/activate && pip install -r requirements.txt"
