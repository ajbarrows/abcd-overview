# ABCD Tools

Unofficial tools to make life a little easier. 


## DEAP to NDA Rename Tool

ABCD releases 5.0 and 5.1 depart from the previous naming conventions for tabular data in a big way. This is particularly impactful for the tabular imaging data which used to be named using standard parcellation atlas labels, but now ... isn't. 

`abcd_5-1_dictionary.csv` is simply an exported version of the [ABCD Study Data Dictionary](https://data-dict.abcdstudy.org/?). 

`deap_to_nda_rename.py` uses this dictionary to rename any (one hopes) ABCD 5.0+ tabular file. Please let us know if this is not the case.

```
$ python deap_to_nda_rename.py --help
usage: deap_to_nda_rename.py [-h] [-f INFILE] [-o OUTFILE] [-d DICTPATH]

options:
  -h, --help            show this help message and exit
  -f INFILE, --infile INFILE
  -o OUTFILE, --outfile OUTFILE
  -d DICTPATH, --dictpath DICTPATH
```


Example:

```
python deap_to_nda_rename.py -f mri_y_tfmr_nback_2bv0b_dsk.csv
```

By default, this function will not overwrite the input file but instead create a new one ending with `_renamed.csv`.