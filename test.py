#!/usr/bin/env python3

# from jsonschema import validate
from jsonschema import Draft7Validator, RefResolver 
import os
import json

doc1 = {
   "id" : "1",
   "collection" : "HMP",
   "basename": "myFile_1.txt",
   "format": "FASTQ",
   "data_type": "sequence_reads",
   "size_in_bytes" : 1024,
   "urls": [
      "http:server1/url1",
      "https://server2.edu/url_2"
   ],
   "creation_date": "2020-01-01",
   "lastmod_date": "2020-02-15",
   "repo_submissions": {
      "SRA": "2020-11-01",
      "CFDE_C2M2": "2035-04-15"
   },
   "produced_by": "EVENT_1",
   "processed_by": [
      "EVENT_2",
      "EVENT_3",
      "EVENT_4"
   ],
   "part_of_study": [
      "STUDY_1",
      "STUDY_2"
   ],
   "comment": "Unstructured text comment from data source goes here!",
   "tags": [
      "HMDEMO",
      "SRP002430",
      "WUGSC"
   ],
   "_search": {
      "data_type": {
         "abbrev": "HM16S",
         "name": "Raw 16S reads and library metadata",
         "paper": "2012_paper",
         "version": "v1"
      },
      "prep": {
         "prep_id": "700016142",
         "run_id": "SRR047485",
         "snprnt": "700016136"
      },
      "study_abbrev": "HHS"
   },
   "dummy_HMP_property": "dummy_value"
}

doc2 = {
   "id" : "2",
   "collection" : "NeMO",
   "some_essential_mouse_property": "this_is_required_by_core_subtype_mouse_subject_schema",
   "some_inessential_mouse_property": 42,
   "essential_NeMO_mouse_property": "this_is_required_by_NeMO_mouse_subject_schema"
}

doc3 = {
   "id" : "3",
   "collection" : "HMP",
   "basename": "myFile_ERR.dat",
   "size_in_bytes" : 4096,
   "dummy_NeMO_property": "dummy_NeMO_value"
}

print(os.getcwd())

# Doc 1: 
abs_schema_path = os.getcwd() + "/dataset_specific_extension_schemas/HMP/base_types/file_HMP.json"

with open(abs_schema_path, 'r') as fp:
   schema = json.loads(fp.read())

resolver = RefResolver(
   # Comment from web:
   # The key part is here where we build a custom RefResolver 
   # and tell it where *this* schema lives in the filesystem
   # Note that `file:` is for unix systems
   base_uri='file:{}'.format(abs_schema_path),
   referrer=None
)

Draft7Validator.check_schema(schema) # Comment from web: 'Unnecessary but a good idea'

validator = Draft7Validator(schema, resolver=resolver, format_checker=None)

try:
    print("Validating doc1 with " + abs_schema_path)
    validator.validate(doc1)
    print("Valid")
except Exception as e:
    print(e)

# Doc 2:
abs_schema_path = os.getcwd() + "/dataset_specific_extension_schemas/NeMO/subtypes/mouse_subject_NeMO.json"

with open(abs_schema_path, 'r') as fp:
   schema = json.loads(fp.read())

resolver = RefResolver(
   # Comment from web:
   # The key part is here where we build a custom RefResolver 
   # and tell it where *this* schema lives in the filesystem
   # Note that `file:` is for unix systems
   base_uri='file:{}'.format(abs_schema_path),
   referrer=None
)

Draft7Validator.check_schema(schema) # Comment from web: 'Unnecessary but a good idea'

validator = Draft7Validator(schema, resolver=resolver, format_checker=None)

try:
    print("Validating doc2 with " + abs_schema_path)
    validator.validate(doc2)
    print("Valid")
except Exception as e:
    print(e)

# Doc 3:


#try:
#    print("Validating doc3")
#    validator.validate(doc3)
#    print("Valid")
#except Exception as e:
#    print(e)


