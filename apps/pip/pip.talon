tag: user.pip
-

pip install: "pip install "
pip install requirements: "pip install -r requirements.txt"
pip remove: "pip remove "
pip freeze requirements: "pip freeze > requirements.txt"
pip download: "pip download "
pip show: "pip show "
# XXX - this won't work outside of linux obviously
pip show versions:
    insert("pip install == 2>&1 | head -1 | cut -f3- -d: | cut -f1 -d\\) | tr ', ' \"\\n\" | sed '/^\\s*$/d' | sort -n")
    key(left:100)
    key(right:11)
pip list: "pip list\n"
pip search: "pip search "
pip version: "pip --version\n"
pip help: "pip --help\n"
