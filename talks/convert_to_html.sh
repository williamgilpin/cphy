#!/bin/bash

# Create a subdirectory if it doesn't exist
mkdir -p html_static

# Loop through each .ipynb file and convert it to HTML in the subdirectory
for i in *.ipynb; do
  jupyter nbconvert --to html "$i" --output-dir=html_static
done
