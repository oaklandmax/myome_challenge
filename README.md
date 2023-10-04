# MyOme Variant Annotation Technical Challenge

## Description
This package takes input from a file of genome variations and looks up the specified annotions in the ensembl.org database via their REST service, and writes the output to a Tab Separated Values (TSV) file in the directory the user was in when executing the file. 

The output file name format is 'annotated_data_\<timestamp\>.tsv'

## Installation instuctions

Change directory to wherever you installed the variant_annotator.py file is and make it executable if it is not already:
```
$ chmod 775 variant_annotator.py
```
Copy 'variant_annotator.py' to 'variant_annotator' in a bin directory on your path. On my system I chose ~/.local/bin, for example, but if you have a bin directory on your path that you prefer, it will work as well.
```
$ cp <path to>/variant_annotator.py ~/.local/bin/variant_annotator
```

You can then execute the program from the directory of your choice as, correcting for the path of the input file variants.txt:
```
$ variant_annotator <variants_txt
```
The output file as described above will get written to the directory that the program is called from.

## Output
### File Output
The sample here may appear line wrapped, but both the output file and the stdout/stderr have one set of data per line.

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
Processing Variants
NC_000001.11:g.215674515G>A
NC_000001.11:g.40819893G>A
The input value: "NC_000001.11:g.40819893T>A" failed with a response of: "400"
NC_000002.12:g.39006443C>T
NC_000006.12:g.152387156G>A
NC_000001.11:g.215674515G>A
Done Processing Variants, output written to annotated_data_20231004-112430.tsv
```

## Code Planning
As described this task could have been done proceedurally, but I think it is both more readable, and more flexible with an OOP structure. Even so, I have kept the instatiation as small as possible.

I chose the packages to include carefully.


## Questions and Answers
##### Suppose we now want to create a web microservice that accepts a GET (or POST) request with the variant in HGVS format and returns the annotation as JSON. What tools or standards would you implement this? How does your code structure change?
I think we are currently using HGVS format for the variation, but I'n not an expert on that. To restructure the program to accept GET and POST requests we would need to create endpoints to accept the requests.

##### Start-ups and start-up employees must balance quick and satisfactory (i.e., good enough) results with more deliberate and reliable results. The same is true for code. You do not have enough time to write the ultimate answer to variant annotation. What is important to get "right" now and what can be deferred.

My priorities when creating this project was to get the variant list from the user as specified, retreive the data variant annotation data from the server, process it to extract the relevant data, and write it to the file in the specified format. Thats the minimum viable product to start with.

Following that, I added error checking where quickly possible, some logging of activity and errors to stdout and stderr, and commented the code for clarity.

Next steps would be to add execption handling for stdin and other points of possible failure and some testing, though if I were doing TDD that would have preceeded occuerred while developing the functions or before.

Lastly I am focussed on packaging the files and uploading them. I have built python libraries in pip, but havent done much packaging in github.

##### What's the simplest method you can think of to handle cases of duplicated variants in the input?

The simplest would be to check the variant id against the list of already completed queries. If I am processing item 12 and there is a duplicate item in the data array at position 4, then we can see 12 is a dupicate of a variant that has already been run. Or if you are checking across multiple runs of files, you could just make a db table and add them as you go, making a quick check to see if the variant is listed. This could also be done with a flat file.

##### What optimizations would you pursue in your code if you had time? How would you prioritize your effort?

Test driven development and exception handling.
