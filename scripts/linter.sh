#!/bin/bash
echo "running black for auto fixers"

path='C:/Users/alejo/OneDrive/Documents/Proyectos/stock-app/stock_app'

poetry run black "$path"

echo "running Running flake8 for detecting errors"

poetry run flake8 "$path"

if [ $? -eq 0 ]; then
    echo "Successfully linted"
    exit 0
else
    echo "Fix lint errors!"
    exit 1
fi
