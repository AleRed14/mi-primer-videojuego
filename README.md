python -m venv env 
.gitignore
env/
env\Scripts\activate.ps1
pip freeze > requirements.txt
pip install -r requirements.txt