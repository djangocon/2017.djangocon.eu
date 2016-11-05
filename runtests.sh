#!/bin/bash
set -e

# Prerequisites
# npm
# npm install -g grunt grunt-cli
# gem install bundle
# virtualenv

fail=0
if [[ "z$CI_USE_GRUNT" == "z" ]]; then
    npm install > /dev/null
    bundle install --deployment > /dev/null
    echo "===== Frontend tests ====="
    grunt ci || fail=1
    # if executed with bundle: bundle exec scss-lint
fi

if [[ "z$CI_SERVER" = "zyes" ]]; then
    PROJECT_DIR=`pwd`
    PROJECT_ID=`basename $PROJECT_DIR`
    VENV_DIR="/srv/virtualenvs/$PROJECT_ID"
else
    VENV_DIR=".testenv"
fi

if [[ ! -e $VENV_DIR ]]; then
    virtualenv --python=/usr/bin/python3.5 $VENV_DIR #> /dev/null
fi

. $VENV_DIR/bin/activate
pip install -U pip setuptools pip-tools > /dev/null
pip install -r requirements-test.txt > /dev/null
pip install coverage > /dev/null
mkdir -p log
echo "===== Flake 8 ====="
flake8 djangocon_europe conference || fail=1
echo "Done"
echo "===== isort ====="
isort -c -rc -df djangocon_europe conference || fail=1
echo "Done"
echo "===== Django tests ====="
coverage erase
coverage run manage.py test --settings=djangocon_europe.settings_tests || fail=1
#if [[ $fail -eq 0 ]]; then
#    if [[ "z$CI_SERVER" = "zyes" ]]; then
#        coverage report
#    else
#        coverage report -m
#    fi
#fi

exit $fail
