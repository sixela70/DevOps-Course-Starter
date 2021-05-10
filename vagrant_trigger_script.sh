#!/bin/bash

cd /vagrant
poetry install
nohup poetry run flask run --host 0.0.0.0 > logs.txt 2>&1 &