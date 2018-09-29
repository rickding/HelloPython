@echo off

git status
git remote update
git checkout master
git pull
git status

pip install -r requirements.txt
call migrate.bat
