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
The output file as described above will get written to the directory that the program is called from.

## Output
### File Output
The output file name format is 'annotated_data_\<timestamp\>.tsv'
The file that is produced has tab separated values, one set of annotations per line, and looks like this:
```
variant assembly_name   seq_region_name start   end     most_severe_consequence strand  genes
NC_000001.11:g.215674515G>A     GRCh38  missense_variant        1       215674515       215674515       1       USH2A
NC_000001.11:g.40819893G>A      GRCh38  missense_variant        1       40819893        40819893        1       KCNQ4
NC_000002.12:g.39006443C>T      GRCh38  synonymous_variant      2       39006443        39006443        1       SOS1
NC_000006.12:g.152387156G>A     GRCh38  synonymous_variant      6       152387156       152387156       1       SYNE1
NC_000001.11:g.215674515G>A     GRCh38  missense_variant        1       215674515       215674515       1       USH2A
```
### Screen Output
The program will display the variant id, and will display any variants that errored along with the response code that was returned as it processes the variants:
```
NC_000001.11:g.215674515G>A
NC_000001.11:g.40819893G>A
The input value: "NC_000001.11:g.40819893T>A" failed with a response of: "400"
NC_000002.12:g.39006443C>T
NC_000006.12:g.152387156G>A
NC_000001.11:g.215674515G>A
```