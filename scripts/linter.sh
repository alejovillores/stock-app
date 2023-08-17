#!/usr/bin/env bash

echo "running black for auto fixers"

poetry run black ../stock_app

echo "running Running flake8 for detecting errors"

poetry run flake8 ../stock_app

if [[ $? -eq 0 ]]; then
    echo "Successfully linted"
    exit 0
else
    echo "Fix lint errors!"
    exit 1
fi



