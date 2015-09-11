#!/bin/bash

for file in $(./getFailures.sh); do
  mv ${file} ${file}.bak
done
