#!/bin/bash

FILES=../../data/NDA/tabulated/ABCDr5-1/core/imaging/*.csv

for f in $FILES
do
    python deap_to_nda_rename.py -f $f
done

