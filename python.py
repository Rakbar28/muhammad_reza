#!/usr/bin/python

import csv
import json
import yaml


csvFilePath = 'inventory.csv'
jsonFilePath = 'inventory.json'
yamlFilePath = 'inventory.yaml'

header = ["DC"]
rows=[{"DC":"DC3" },
     {"DC":"DC3" }    
     {"DC":"DC3" },
     {"DC":"DC3" },

      ]
print ("\n")
print ("-------------------------------------------------------------------------------------------")
print ("Jawaban nomor 1 ")
print ("-------------------------------------------------------------------------------------------")
print ("\n")

#tulis kedalam file csv
with open(csvFilePath,'w') as tulis_file:
    tulis_file_csv = csv.DictWriter(tulis_file, header)
    tulis_file_csv.writeheader()
    tulis_file_csv.writerows(rows)

#membuka file csv yang telah dibuat
with open(csvFilePath) as buka_file:
  buka_file_csv = csv.reader(buka_file)
  for row in buka_file_csv:
    print(row)
buka_file.close()

print ("\n")
print ("-------------------------------------------------------------------------------------------")
print ("Jawaban nomor 2 ")
print ("-------------------------------------------------------------------------------------------")
print ("\n")

#write file json
with open(jsonFilePath, 'w') as json_file:
  json_file.write(json.dumps(rows, indent=4))

#open file json
with open(jsonFilePath, 'r') as json_files:
    data = json.load(json_files)
    for x in data:
     print(json.dumps(x, indent=4))

print ("\n")
print ("-------------------------------------------------------------------------------------------")
print ("Jawaban nomor 3 ")
print ("-------------------------------------------------------------------------------------------")
print ("\n")

#write file YAML
with open(yamlFilePath, 'w') as yaml_file:
   yaml_data = yaml.dump(rows, yaml_file)
   yaml_file.close()

#open file YAML
with open(yamlFilePath, 'r') as yaml_files:
   list_dc = yaml.load(yaml_files, Loader=yaml.FullLoader)
   sort_list = yaml.dump(list_dc, sort_keys=True)
   print(sort_list)
