#!/bin/bash

celery -A hello_celery worker -l info -P eventlet
