@echo off

rem kill services

rem launch services
start runserver.bat
start mq_voucher.bat
start celery.bat
