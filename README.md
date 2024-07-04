.gitignore
env/

python -m venv env 
env\Scripts\activate.ps1
pip install -r requirements.txt

pip freeze > requirements.txt

git add .
git commit -m ""
git push