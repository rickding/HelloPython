@echo off

rem Install manually: git, python
rem sudo apt-get install git
rem sudo apt-get install python3.6
rem sudo apt-get install python-pip

git clone git@gitee.com:dds18/Facet.git

cd Facet
git checkout master

cd dba

rem Install with pip: django, mysql, redis, rabbit-mq
pip install -r requirements.txt

rem mysql-server

rem redis-server

rem rabbit-mq-server
