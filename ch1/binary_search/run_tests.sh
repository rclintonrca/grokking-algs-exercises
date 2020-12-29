#!/bin/bash

# this shell script should run tests for each of the languages

# Python
cd python && python -m unittest
cd ..
# JS
# nvm use 10
cd javascript && yarn test
cd ..

# Scala
