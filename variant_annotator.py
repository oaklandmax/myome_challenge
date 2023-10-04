#!/usr/bin/python3

import csv
import requests
import time
import sys


class VariantAnnotator:
    
    variant_list = []
    
    def __init__(self) -> None:
        timestr = time.strftime("%Y%m%d-%H%M%S")
        self.filename_out = 'annotated_data_' + timestr + '.tsv'
        self.create_output_file()
        self.read_stdin_clean()
    
    def read_stdin_clean(self):
        # TODO: check for stdin
        for line in sys.stdin:
            self.variant_list.append(line.strip())  # Remove trailing whitespace and return chars

            
    # def get_variants_from_file(self, filename_in) -> None:
    #     # TODO: fix this data dir to be more local. very important
    #     data_dir = '/home/max/python/myome/myome_challenge/'
    #     with open(data_dir + filename_in) as my_file:
    #         # self.variant_list = my_file.readlines()
    #         self.variant_list = my_file.read().splitlines()  # removes newline and spaces
            
    def get_annotations(self, variant_in) -> dict:    
        url = 'https://rest.ensembl.org/vep/human/hgvs/' + variant_in
        response = requests.get(url, headers={"Content-Type" : "application/json"})
        
        # Only process successful (200) responses
        if response.status_code == 200:
            annotation_json_data = response.json()[0]  # json object is returned in a one item list. just return the zero item for ease of reading
            # print(json.dumps(annotation_json_data, indent=1))

            # Put data in a dict for later processing. Dict is good as we can reference by name later.
            # TODO: check for missing data? Not sure.
            annotation_dict = {
                'variant': variant_in,
                'assembly_name': annotation_json_data['assembly_name'],
                'most_severe_consequence': annotation_json_data['most_severe_consequence'],
                'seq_region_name': annotation_json_data['seq_region_name'],
                'start': annotation_json_data['start'],
                'end': annotation_json_data['end'],
                'strand': annotation_json_data['strand'],
                'gene_symbol': annotation_json_data['transcript_consequences'][0]['gene_symbol']
            }
            print(variant_in, file=sys.stdout)
            return annotation_dict
        else:
            print('The input value: "' + variant_in + '" failed with a response of: "' + str(response.status_code) + '"', file=sys.stderr)
            return {} # This could also return None but we returns a dict for funtion output consistancy
            
    def create_output_file(self)-> None:
        # TODO: fix the path that this file gets written to
        with open(self.filename_out, 'w', newline='') as tsvfile:
            writer = csv.writer(tsvfile, delimiter='\t', lineterminator='\n')
            writer.writerow(['variant', 'assembly_name', 'seq_region_name', 'start', 'end', 'most_severe_consequence', 'strand', 'genes'])

    def process_results_to_file(self, annotation_in) -> None:
        # TODO: fix the path that this file gets written to
        with open(self.filename_out, 'a', newline='') as tsvfile_data:
            writer = csv.writer(tsvfile_data, delimiter='\t', lineterminator='\n')
            # writerow takes single arg, so putting values in a single array element, I could probably just pass annotation_in, but the order of elements is not guaranteed to match the header.
            writer.writerow(
                [
                    annotation_in['variant'],
                    annotation_in['assembly_name'],
                    annotation_in['most_severe_consequence'],
                    annotation_in['seq_region_name'],
                    annotation_in['start'],
                    annotation_in['end'],
                    annotation_in['strand'],
                    annotation_in['gene_symbol']
                ]
            )
        

####################################################
# Instantiate the Object  and Process the Variants #
####################################################

v = VariantAnnotator()
# v.get_variants_from_file('variants.txt')
print('Processing Variants', file=sys.stdout)
for variant in v.variant_list:
    annotation = v.get_annotations(variant)
    if annotation:
        v.process_results_to_file(annotation)
print('Done Processing Variants, output written to ' + v.filename_out, file=sys.stdout)

