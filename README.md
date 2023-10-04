# MyOme Variant Annotation Technical Challenge

## Description
This package takes input from a file of Genome Variations and looks up the specified annotions in the ensembl.org database via their REST service, and writes the output to a Tab Separated Values (TSV) file in the directory the user was in when executing the file. 

The output file name format is 'annotated_data_\<timestamp\>.tsv'

## Installation instuctions

Change directory to wherever you installed the variant_annotator.py file is and make it executable if it is not already:
```
$ chmod 775 variant_annotator.py
```
Copy 'variant_annotator.py' to 'variant_annotator' in a bin directory on your path. On my system I chose ~/.local/bin, for example, but if you have a bin directory on your path that you prefer, it will work as well.
```
$ cp <path to>/variant_annotator.py ~/.local/bin/annotator.py
```

You can then execute the program from the directory of your choice as, correcting for the path of the input file variants.txt:
```
$ variant_annotator <variants_txt
```

